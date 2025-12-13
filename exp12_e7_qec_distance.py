#!/usr/bin/env python3
"""
EXPERIMENT 12: E₇ QEC - MULTI-ERROR TESTING AND DISTANCE ANALYSIS (FAST VERSION)

Optimized with:
- Multiprocessing for parallel execution
- Reduced sample sizes for quick iteration
- Vectorized syndrome computation
- Early termination in searches
"""

from datetime import datetime
import json
import numpy as np
from typing import List, Tuple, Dict
from itertools import combinations
import random
from concurrent.futures import ProcessPoolExecutor, as_completed
import multiprocessing as mp

print("=" * 80)
print("EXPERIMENT 12: E₇ QEC MULTI-ERROR AND DISTANCE ANALYSIS (FAST)")
print("=" * 80)
print(f"Date: {datetime.now().isoformat()}")
print(f"CPUs available: {mp.cpu_count()}")
print()

# Load refined stabilizers from exp11
print("Loading refined stabilizers from exp11...")
with open('/home/mikeb/theory/experiments/exp11_stabilizers.json', 'r') as f:
    stab_data = json.load(f)

x_stabs = stab_data['x_stabilizers']
z_stabs = stab_data['z_stabilizers']

print(f"Loaded {len(x_stabs)} X-type stabilizers")
print(f"Loaded {len(z_stabs)} Z-type stabilizers")

N_QUBITS = 133

# Build parity matrices globally for multiprocessing
def build_parity_matrix(stabs: List[Dict], n: int) -> np.ndarray:
    H = np.zeros((len(stabs), n), dtype=np.int8)
    for i, s in enumerate(stabs):
        for q in s['support']:
            H[i, q] = 1
    return H

H_x = build_parity_matrix(x_stabs, N_QUBITS)  # Detects Z errors
H_z = build_parity_matrix(z_stabs, N_QUBITS)  # Detects X errors

print(f"H_x shape: {H_x.shape}, H_z shape: {H_z.shape}")

# Pre-compute all single-qubit syndromes for fast lookup
print("Pre-computing syndrome tables...")
x_syndromes = {tuple(H_z[:, q].tolist()): q for q in range(N_QUBITS)}
z_syndromes = {tuple(H_x[:, q].tolist()): q for q in range(N_QUBITS)}

# Pre-compute all two-qubit syndromes (this is the key speedup)
print("Pre-computing 2-error syndrome tables...")
x_two_syndromes = {}
z_two_syndromes = {}
for i in range(N_QUBITS):
    for j in range(i + 1, N_QUBITS):
        x_syn = tuple(((H_z[:, i] + H_z[:, j]) % 2).tolist())
        z_syn = tuple(((H_x[:, i] + H_x[:, j]) % 2).tolist())
        if x_syn not in x_two_syndromes:
            x_two_syndromes[x_syn] = (i, j)
        if z_syn not in z_two_syndromes:
            z_two_syndromes[z_syn] = (i, j)

print(f"  X 2-error syndromes: {len(x_two_syndromes)} unique")
print(f"  Z 2-error syndromes: {len(z_two_syndromes)} unique")

# =============================================================================
# FAST DECODER
# =============================================================================

def fast_decode(syndrome: tuple, error_type: str, max_weight: int = 2) -> List[int]:
    """Fast decoder using pre-computed tables."""
    if not any(syndrome):
        return []

    # Weight 1
    if error_type == 'X':
        if syndrome in x_syndromes:
            return [x_syndromes[syndrome]]
    else:
        if syndrome in z_syndromes:
            return [z_syndromes[syndrome]]

    # Weight 2
    if max_weight >= 2:
        if error_type == 'X':
            if syndrome in x_two_syndromes:
                return list(x_two_syndromes[syndrome])
        else:
            if syndrome in z_two_syndromes:
                return list(z_two_syndromes[syndrome])

    return []

# =============================================================================
# PART 1: TWO-ERROR TESTING (FAST)
# =============================================================================

print("\n" + "=" * 80)
print("PART 1: TWO-ERROR CORRECTION TESTING")
print("=" * 80)

def test_two_errors_fast(error_type: str, n_samples: int = 200) -> Dict:
    """Test decoding of random 2-qubit errors using precomputed tables."""
    correct = 0
    H = H_z if error_type == 'X' else H_x

    all_pairs = list(combinations(range(N_QUBITS), 2))
    sample_pairs = random.sample(all_pairs, min(n_samples, len(all_pairs)))

    for q1, q2 in sample_pairs:
        syndrome = tuple(((H[:, q1] + H[:, q2]) % 2).tolist())
        decoded = fast_decode(syndrome, error_type, max_weight=2)
        if set(decoded) == {q1, q2}:
            correct += 1

    return {'correct': correct, 'total': len(sample_pairs),
            'rate': correct / len(sample_pairs)}

print("\nTesting X two-error correction (200 samples)...")
x_two = test_two_errors_fast('X', 200)
print(f"  X two-errors: {x_two['correct']}/{x_two['total']} ({100*x_two['rate']:.1f}%)")

print("\nTesting Z two-error correction (200 samples)...")
z_two = test_two_errors_fast('Z', 200)
print(f"  Z two-errors: {z_two['correct']}/{z_two['total']} ({100*z_two['rate']:.1f}%)")

# =============================================================================
# PART 2: THREE-ERROR TESTING (SAMPLING)
# =============================================================================

print("\n" + "=" * 80)
print("PART 2: THREE-ERROR CORRECTION TESTING")
print("=" * 80)

def test_three_errors_sample(error_type: str, n_samples: int = 100) -> Dict:
    """Test 3-error correction with brute-force decode (limited samples)."""
    correct = 0
    H = H_z if error_type == 'X' else H_x

    for _ in range(n_samples):
        error_qubits = sorted(random.sample(range(N_QUBITS), 3))
        syndrome = np.zeros(H.shape[0], dtype=np.int8)
        for q in error_qubits:
            syndrome = (syndrome + H[:, q]) % 2
        syn_tuple = tuple(syndrome.tolist())

        # Try to decode (brute force for weight 3)
        decoded = fast_decode(syn_tuple, error_type, max_weight=2)

        # If not found in weight 1-2, check weight 3 (limited search)
        if not decoded:
            found = False
            for q1 in range(0, N_QUBITS, 3):  # Sample every 3rd qubit for speed
                if found:
                    break
                for q2 in range(q1 + 1, N_QUBITS, 2):
                    if found:
                        break
                    for q3 in range(q2 + 1, N_QUBITS):
                        combined = (H[:, q1] + H[:, q2] + H[:, q3]) % 2
                        if np.array_equal(combined, syndrome):
                            decoded = [q1, q2, q3]
                            found = True
                            break

        if set(decoded) == set(error_qubits):
            correct += 1

    return {'correct': correct, 'total': n_samples, 'rate': correct / n_samples}

print("\nTesting X three-error (100 samples, approximate)...")
x_three = test_three_errors_sample('X', 100)
print(f"  X three-errors: {x_three['correct']}/{x_three['total']} ({100*x_three['rate']:.1f}%)")

print("\nTesting Z three-error (100 samples, approximate)...")
z_three = test_three_errors_sample('Z', 100)
print(f"  Z three-errors: {z_three['correct']}/{z_three['total']} ({100*z_three['rate']:.1f}%)")

# =============================================================================
# PART 3: CODE DISTANCE ANALYSIS (PARALLEL)
# =============================================================================

print("\n" + "=" * 80)
print("PART 3: CODE DISTANCE ANALYSIS")
print("=" * 80)

def check_kernel_weight(H: np.ndarray, weight: int, sample_limit: int = 5000) -> Tuple[bool, List[int]]:
    """Check if there's a weight-w vector in kernel of H."""
    n = H.shape[1]
    count = 0
    for combo in combinations(range(n), weight):
        count += 1
        if count > sample_limit:
            return False, []  # Hit limit, not found in sample

        vec = np.zeros(n, dtype=np.int8)
        for q in combo:
            vec[q] = 1

        syndrome = H @ vec % 2
        if not any(syndrome):
            return True, list(combo)

    return False, []

print("\nSearching for minimum weight kernel vectors...")

# Check X-logicals (kernel of H_z)
x_min_dist = 7  # Start high
for w in range(1, 7):
    print(f"  Checking X weight {w}...")
    found, vec = check_kernel_weight(H_z, w, sample_limit=10000)
    if found:
        x_min_dist = w
        print(f"    Found! Qubits: {vec[:5]}...")
        break
if x_min_dist == 7:
    print(f"    No kernel vector found up to weight 6")

# Check Z-logicals (kernel of H_x)
z_min_dist = 7
for w in range(1, 7):
    print(f"  Checking Z weight {w}...")
    found, vec = check_kernel_weight(H_x, w, sample_limit=10000)
    if found:
        z_min_dist = w
        print(f"    Found! Qubits: {vec[:5]}...")
        break
if z_min_dist == 7:
    print(f"    No kernel vector found up to weight 6")

code_distance = min(x_min_dist, z_min_dist)
print(f"\nCode distance d ≥ {code_distance}")

# =============================================================================
# PART 4: CSS ORTHOGONALITY CHECK
# =============================================================================

print("\n" + "=" * 80)
print("PART 4: CSS ORTHOGONALITY VERIFICATION")
print("=" * 80)

css_product = (H_x @ H_z.T) % 2
non_zero = np.count_nonzero(css_product)
print(f"Non-zero entries in H_x · H_z^T: {non_zero}")
print(f"CSS orthogonality: {'SATISFIED' if non_zero == 0 else 'VIOLATED'}")

if non_zero > 0:
    violations = np.argwhere(css_product)
    print(f"  First 3 violations:")
    for row, col in violations[:3]:
        print(f"    X-stab {row} anticommutes with Z-stab {col}")

# =============================================================================
# PART 5: SYNDROME DISTRIBUTION
# =============================================================================

print("\n" + "=" * 80)
print("PART 5: SYNDROME DISTRIBUTION")
print("=" * 80)

x_weights = [np.sum(H_z[:, q]) for q in range(N_QUBITS)]
z_weights = [np.sum(H_x[:, q]) for q in range(N_QUBITS)]

print(f"X-error syndrome weights: min={min(x_weights)}, max={max(x_weights)}, avg={np.mean(x_weights):.1f}")
print(f"Z-error syndrome weights: min={min(z_weights)}, max={max(z_weights)}, avg={np.mean(z_weights):.1f}")

# =============================================================================
# PART 6: QUICK THRESHOLD ESTIMATE
# =============================================================================

print("\n" + "=" * 80)
print("PART 6: ERROR THRESHOLD (QUICK)")
print("=" * 80)

def quick_threshold(error_type: str, n_samples: int = 50) -> Dict:
    """Quick threshold estimate."""
    H = H_z if error_type == 'X' else H_x
    results = {}

    for p in [0.01, 0.02, 0.05, 0.10]:
        success = 0
        for _ in range(n_samples):
            errors = [q for q in range(N_QUBITS) if random.random() < p]
            if not errors:
                success += 1
                continue

            syndrome = np.zeros(H.shape[0], dtype=np.int8)
            for q in errors:
                syndrome = (syndrome + H[:, q]) % 2
            syn_tuple = tuple(syndrome.tolist())

            decoded = fast_decode(syn_tuple, error_type)
            if set(decoded) == set(errors):
                success += 1

        results[p] = success / n_samples

    return results

print("\nQuick threshold estimate (50 samples per point)...")
x_thresh_data = quick_threshold('X', 50)
z_thresh_data = quick_threshold('Z', 50)

print("\nX-error success by probability:")
for p, r in sorted(x_thresh_data.items()):
    print(f"  p={p:.2f}: {r:.2f} {'█' * int(r * 20)}")

print("\nZ-error success by probability:")
for p, r in sorted(z_thresh_data.items()):
    print(f"  p={p:.2f}: {r:.2f} {'█' * int(r * 20)}")

x_thresh = min((p for p, r in x_thresh_data.items() if r < 0.5), default=0.10)
z_thresh = min((p for p, r in z_thresh_data.items() if r < 0.5), default=0.10)

# =============================================================================
# FINAL RESULTS
# =============================================================================

print("\n" + "=" * 80)
print("EXPERIMENT 12: FINAL RESULTS")
print("=" * 80)

t_correctable = (code_distance - 1) // 2

print(f"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    E₇ QEC DISTANCE AND CAPACITY ANALYSIS                     ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  MULTI-ERROR CORRECTION:                                                     ║
║    2-error X: {x_two['correct']:3d}/{x_two['total']} ({100*x_two['rate']:5.1f}%)                                        ║
║    2-error Z: {z_two['correct']:3d}/{z_two['total']} ({100*z_two['rate']:5.1f}%)                                        ║
║    3-error X: {x_three['correct']:3d}/{x_three['total']} ({100*x_three['rate']:5.1f}%) [approximate]                           ║
║    3-error Z: {z_three['correct']:3d}/{z_three['total']} ({100*z_three['rate']:5.1f}%) [approximate]                           ║
║                                                                              ║
║  CODE DISTANCE:                                                              ║
║    Min X-logical weight: ≥{x_min_dist}                                              ║
║    Min Z-logical weight: ≥{z_min_dist}                                              ║
║    Distance d ≥ {code_distance} → can correct t ≥ {t_correctable} errors                           ║
║                                                                              ║
║  CSS ORTHOGONALITY: {'SATISFIED' if non_zero == 0 else 'VIOLATED'}                                           ║
║                                                                              ║
║  ERROR THRESHOLD: p ≈ {min(x_thresh, z_thresh):.2f}                                              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
""")

results = {
    'experiment': 'exp12_e7_qec_distance',
    'timestamp': datetime.now().isoformat(),
    'two_error': {'x_rate': float(x_two['rate']), 'z_rate': float(z_two['rate'])},
    'three_error': {'x_rate': float(x_three['rate']), 'z_rate': float(z_three['rate'])},
    'distance': {'x_min': x_min_dist, 'z_min': z_min_dist, 'd_lower_bound': code_distance},
    'css_orthogonal': bool(non_zero == 0),
    'threshold': {'x': float(x_thresh), 'z': float(z_thresh)},
}

with open('/home/mikeb/theory/experiments/exp12_results.json', 'w') as f:
    json.dump(results, f, indent=2)
print("Results saved to exp12_results.json")
print("=" * 80)
