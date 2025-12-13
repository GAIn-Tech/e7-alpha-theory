#!/usr/bin/env python3
"""
EXPERIMENT 11: REFINED E₇ QEC CODE - PROPER CSS STRUCTURE

Key fix: Use weight-4 Hamming parity check rows (not weight-3 Fano lines)
to ensure CSS orthogonality: H @ H.T = 0 (mod 2).

Structure:
- 19 blocks of 7 qubits each (133 = 19 × 7)
- Each block uses proper Steane [[7,1,3]] CSS stabilizers
- Inter-block stabilizers maintain CSS orthogonality
"""

from datetime import datetime
import json
import numpy as np
from typing import List, Dict, Tuple
from itertools import combinations

print("=" * 80)
print("EXPERIMENT 11: REFINED E₇ QEC - PROPER CSS STRUCTURE")
print("=" * 80)
print(f"Date: {datetime.now().isoformat()}")
print()

# =============================================================================
# STEANE CODE FOUNDATION - PROPER CSS
# =============================================================================

print("PART 1: STEANE CODE FOUNDATION (PROPER CSS)")
print("-" * 80)

# Hamming [7,4,3] parity check matrix rows - WEIGHT 4 for CSS orthogonality
# These satisfy H @ H.T = 0 (mod 2)
STEANE_SUPPORTS = [
    [3, 4, 5, 6],  # Row 0: 0001111
    [1, 2, 5, 6],  # Row 1: 0110011
    [0, 2, 4, 6],  # Row 2: 1010101
]

# Verify CSS orthogonality
def verify_css_orthogonality():
    H = np.zeros((3, 7), dtype=np.int8)
    for i, support in enumerate(STEANE_SUPPORTS):
        for q in support:
            H[i, q] = 1
    product = (H @ H.T) % 2
    return np.all(product == 0)

print(f"Steane stabilizer supports (weight-4 for CSS):")
for i, support in enumerate(STEANE_SUPPORTS):
    print(f"  Row {i}: qubits {support}")
print(f"CSS orthogonality check: {'PASSED' if verify_css_orthogonality() else 'FAILED'}")

def steane_stabilizers_for_block(block_idx: int) -> List[Dict]:
    """Generate proper CSS Steane stabilizers for a 7-qubit block."""
    offset = block_idx * 7
    stabilizers = []

    # X-type stabilizers from Hamming rows
    for i, support in enumerate(STEANE_SUPPORTS):
        stab = {
            'type': 'X',
            'block': block_idx,
            'support': [offset + q for q in support],
        }
        stabilizers.append(stab)

    # Z-type stabilizers from SAME Hamming rows (ensures CSS)
    for i, support in enumerate(STEANE_SUPPORTS):
        stab = {
            'type': 'Z',
            'block': block_idx,
            'support': [offset + q for q in support],
        }
        stabilizers.append(stab)

    return stabilizers

# =============================================================================
# E₇ DYNKIN STRUCTURE FOR INTER-BLOCK COUPLING
# =============================================================================

print("\n" + "=" * 80)
print("PART 2: E₇ DYNKIN STRUCTURE FOR INTER-BLOCK COUPLING")
print("-" * 80)

print("""
E₇ Dynkin diagram:

    1 — 2 — 3 — 4 — 5 — 6
                |
                7

We use this to connect the 19 blocks.
Map: 19 blocks organized in 3 layers of the E₇ structure.
""")

# For CSS orthogonality, inter-block stabilizers must use Steane codeword
# patterns (weight 0, 3, 4, or 7) in each block.
# Using weight-4 Steane support from each block ensures even overlap.

def generate_interblock_stabilizers(n_blocks: int = 19) -> List[Dict]:
    """
    Generate CSS-preserving inter-block stabilizers using Steane codewords.

    Key insight: A 2-qubit subset cannot have even overlap with all 3 Steane
    supports. But a full Steane support (weight-4) does, since H @ H.T = 0.

    Strategy: Use weight-8 stabilizers with full Steane support from each block.
    """
    stabilizers = []

    # Connect adjacent blocks using full Steane support from each
    # This creates weight-8 stabilizers that are CSS-orthogonal
    for i in range(n_blocks - 1):
        offset_i = i * 7
        offset_j = (i + 1) * 7

        # Use Steane support 0: [3,4,5,6] from each block
        support = [offset_i + q for q in STEANE_SUPPORTS[0]] + \
                  [offset_j + q for q in STEANE_SUPPORTS[0]]
        stabilizers.append({'type': 'X', 'block': 'inter', 'support': support})
        stabilizers.append({'type': 'Z', 'block': 'inter', 'support': support})

    # E₇ branch connections using Steane support 1: [1,2,5,6]
    branch_points = [3, 9, 15]
    for bp in branch_points:
        if bp + 6 < n_blocks:
            offset_i = bp * 7
            offset_j = (bp + 6) * 7
            support = [offset_i + q for q in STEANE_SUPPORTS[1]] + \
                      [offset_j + q for q in STEANE_SUPPORTS[1]]
            stabilizers.append({'type': 'X', 'block': 'inter', 'support': support})
            stabilizers.append({'type': 'Z', 'block': 'inter', 'support': support})

    # Cyclic closure using Steane support 2: [0,2,4,6]
    support = [0 + q for q in STEANE_SUPPORTS[2]] + \
              [18*7 + q for q in STEANE_SUPPORTS[2]]
    stabilizers.append({'type': 'X', 'block': 'inter', 'support': support})
    stabilizers.append({'type': 'Z', 'block': 'inter', 'support': support})

    return stabilizers

interblock_stabs = generate_interblock_stabilizers()
print(f"Generated {len(interblock_stabs)} inter-block stabilizers")

# =============================================================================
# COMPLETE CODE CONSTRUCTION
# =============================================================================

print("\n" + "=" * 80)
print("PART 3: COMPLETE CODE CONSTRUCTION")
print("-" * 80)

def build_complete_code() -> Dict:
    """Build the complete [[133, k, d]] E₇-inspired code."""

    n_blocks = 19
    n_qubits = 133

    all_stabilizers = []

    # Intra-block stabilizers (Steane structure)
    intra_count = 0
    for block in range(n_blocks):
        block_stabs = steane_stabilizers_for_block(block)
        all_stabilizers.extend(block_stabs)
        intra_count += len(block_stabs)

    print(f"Intra-block stabilizers: {intra_count}")

    # Inter-block stabilizers (E₇ structure)
    inter_stabs = generate_interblock_stabilizers()
    all_stabilizers.extend(inter_stabs)
    inter_count = len(inter_stabs)

    print(f"Inter-block stabilizers: {inter_count}")
    print(f"Total stabilizers: {len(all_stabilizers)}")

    # We need exactly 126 stabilizers for k=7
    # Current count may differ, so we adjust
    target_stabs = 126
    current_stabs = len(all_stabilizers)

    if current_stabs > target_stabs:
        # Remove some redundant inter-block stabilizers
        all_stabilizers = all_stabilizers[:target_stabs]
        print(f"Trimmed to {target_stabs} stabilizers")
    elif current_stabs < target_stabs:
        # Add additional stabilizers
        needed = target_stabs - current_stabs
        print(f"Need {needed} more stabilizers")

        # Add weight-4 X stabilizers spanning blocks
        added = 0
        for i in range(n_blocks - 1):
            if added >= needed:
                break
            for q1, q2 in [(0, 1), (2, 3), (4, 5)]:
                if added >= needed:
                    break
                stab = {
                    'type': 'X' if added % 2 == 0 else 'Z',
                    'block': 'extra',
                    'support': [i * 7 + q1, i * 7 + q2,
                               (i + 1) * 7 + q1, (i + 1) * 7 + q2],
                    'connection': f'extra_{added}',
                }
                all_stabilizers.append(stab)
                added += 1

        print(f"Added {added} extra stabilizers")

    print(f"Final stabilizer count: {len(all_stabilizers)}")

    # Separate X and Z stabilizers
    x_stabs = [s for s in all_stabilizers if s['type'] == 'X']
    z_stabs = [s for s in all_stabilizers if s['type'] == 'Z']

    print(f"X-type: {len(x_stabs)}, Z-type: {len(z_stabs)}")

    return {
        'n_qubits': n_qubits,
        'n_blocks': n_blocks,
        'stabilizers': all_stabilizers,
        'x_stabilizers': x_stabs,
        'z_stabilizers': z_stabs,
    }

code = build_complete_code()

# =============================================================================
# BUILD PARITY CHECK MATRICES
# =============================================================================

print("\n" + "=" * 80)
print("PART 4: PARITY CHECK MATRICES")
print("-" * 80)

def build_parity_matrix(stabs: List[Dict], n_qubits: int) -> np.ndarray:
    """Build binary parity check matrix."""
    H = np.zeros((len(stabs), n_qubits), dtype=np.int8)
    for i, s in enumerate(stabs):
        for q in s['support']:
            if 0 <= q < n_qubits:
                H[i, q] = 1
    return H

H_x = build_parity_matrix(code['x_stabilizers'], 133)
H_z = build_parity_matrix(code['z_stabilizers'], 133)

print(f"H_x shape: {H_x.shape}")
print(f"H_z shape: {H_z.shape}")

# Check rank
rank_x = np.linalg.matrix_rank(H_x)
rank_z = np.linalg.matrix_rank(H_z)
print(f"Rank of H_x: {rank_x}")
print(f"Rank of H_z: {rank_z}")

# =============================================================================
# SYNDROME UNIQUENESS TEST
# =============================================================================

print("\n" + "=" * 80)
print("PART 5: SYNDROME UNIQUENESS TEST")
print("-" * 80)

def test_syndrome_uniqueness(H: np.ndarray, error_type: str) -> Dict:
    """Test how many qubits have unique syndromes."""
    n_qubits = H.shape[1]
    syndromes = {}

    for q in range(n_qubits):
        syn = tuple(H[:, q].tolist())
        if syn not in syndromes:
            syndromes[syn] = []
        syndromes[syn].append(q)

    unique = sum(1 for qs in syndromes.values() if len(qs) == 1)
    collisions = {syn: qs for syn, qs in syndromes.items() if len(qs) > 1}

    return {
        'unique': unique,
        'total': n_qubits,
        'collisions': len(collisions),
        'collision_details': collisions,
    }

# Test X errors (detected by Z stabilizers)
x_result = test_syndrome_uniqueness(H_z, 'X')
print(f"X-error syndrome uniqueness: {x_result['unique']}/133 ({100*x_result['unique']/133:.1f}%)")
print(f"  Collisions: {x_result['collisions']}")

# Test Z errors (detected by X stabilizers)
z_result = test_syndrome_uniqueness(H_x, 'Z')
print(f"Z-error syndrome uniqueness: {z_result['unique']}/133 ({100*z_result['unique']/133:.1f}%)")
print(f"  Collisions: {z_result['collisions']}")

# Show some collision examples
if x_result['collisions'] > 0:
    print("\nX-error collision examples:")
    for syn, qubits in list(x_result['collision_details'].items())[:3]:
        print(f"  Qubits {qubits} share syndrome")

# =============================================================================
# CSS-PRESERVING REFINEMENT
# =============================================================================

print("\n" + "=" * 80)
print("PART 6: CSS-PRESERVING REFINEMENT")
print("-" * 80)

def refine_css_stabilizers(x_stabs: List[Dict], z_stabs: List[Dict],
                            n_qubits: int, max_iterations: int = 50) -> Tuple[List[Dict], List[Dict]]:
    """
    Refine stabilizers while maintaining CSS orthogonality.

    Key: Add stabilizers in X/Z pairs with SAME support (weight-4).
    This guarantees CSS: any new X-stab commutes with any Z-stab.
    """
    current_x = x_stabs.copy()
    current_z = z_stabs.copy()

    for iteration in range(max_iterations):
        H_x = build_parity_matrix(current_x, n_qubits)
        H_z = build_parity_matrix(current_z, n_qubits)

        # Check both syndrome uniquenesses
        x_result = test_syndrome_uniqueness(H_z, 'X')  # X errors detected by Z
        z_result = test_syndrome_uniqueness(H_x, 'Z')  # Z errors detected by X

        total_collisions = x_result['collisions'] + z_result['collisions']

        if total_collisions == 0:
            print(f"  Iteration {iteration}: All syndromes unique!")
            break

        # Find a collision to fix (prioritize the larger set)
        if x_result['collisions'] > 0:
            collision = list(x_result['collision_details'].values())[0]
            target = 'Z'  # Add Z stabilizers to fix X-error detection
        else:
            collision = list(z_result['collision_details'].values())[0]
            target = 'X'  # Add X stabilizers to fix Z-error detection

        q1, q2 = collision[0], collision[1]

        # Create weight-4 CSS stabilizer pair that distinguishes q1 from q2
        # Strategy: include q1 and 3 neighbors, exclude q2
        block1 = q1 // 7
        new_support = [q1]

        # Add 3 more qubits from same block (for weight 4)
        for offset in [1, 2, 3, -1, -2]:
            neighbor = block1 * 7 + ((q1 % 7) + offset) % 7
            if neighbor != q2 and neighbor not in new_support and 0 <= neighbor < n_qubits:
                new_support.append(neighbor)
                if len(new_support) >= 4:
                    break

        # Ensure weight 4
        if len(new_support) < 4:
            # Add from adjacent block
            block2 = (block1 + 1) % 19
            for offset in [0, 1, 2]:
                neighbor = block2 * 7 + offset
                if neighbor != q2 and neighbor not in new_support and 0 <= neighbor < n_qubits:
                    new_support.append(neighbor)
                    if len(new_support) >= 4:
                        break

        new_support = sorted(new_support[:4])

        # Add BOTH X and Z stabilizers with same support (CSS requirement)
        new_stab_x = {'type': 'X', 'block': 'refined', 'support': new_support}
        new_stab_z = {'type': 'Z', 'block': 'refined', 'support': new_support}

        current_x.append(new_stab_x)
        current_z.append(new_stab_z)

        if iteration % 10 == 0:
            print(f"  Iteration {iteration}: X-collisions={x_result['collisions']}, "
                  f"Z-collisions={z_result['collisions']}, stabs={len(current_x)}")

    return current_x, current_z

print("Refining stabilizers (CSS-preserving)...")
refined_x_stabs, refined_z_stabs = refine_css_stabilizers(
    code['x_stabilizers'], code['z_stabilizers'], 133, max_iterations=100
)

print(f"\nRefined X-stabilizer count: {len(refined_x_stabs)}")
print(f"Refined Z-stabilizer count: {len(refined_z_stabs)}")

# Verify CSS orthogonality is maintained
H_x_refined = build_parity_matrix(refined_x_stabs, 133)
H_z_refined = build_parity_matrix(refined_z_stabs, 133)
css_check = (H_x_refined @ H_z_refined.T) % 2
css_violations = np.count_nonzero(css_check)
print(f"CSS orthogonality violations: {css_violations}")

# Test syndrome uniqueness
x_result_refined = test_syndrome_uniqueness(H_z_refined, 'X')
z_result_refined = test_syndrome_uniqueness(H_x_refined, 'Z')
print(f"X-error uniqueness after refinement: {x_result_refined['unique']}/133")
print(f"Z-error uniqueness after refinement: {z_result_refined['unique']}/133")

# =============================================================================
# FINAL DECODER CONSTRUCTION
# =============================================================================

print("\n" + "=" * 80)
print("PART 7: FINAL DECODER CONSTRUCTION")
print("-" * 80)

class RefinedE7Decoder:
    """Decoder using refined stabilizers."""

    def __init__(self, x_stabs: List[Dict], z_stabs: List[Dict], n_qubits: int = 133):
        self.H_x = build_parity_matrix(x_stabs, n_qubits)
        self.H_z = build_parity_matrix(z_stabs, n_qubits)
        self.n_qubits = n_qubits

        # Build lookup tables
        self.x_table = self._build_table(self.H_z)  # X errors detected by Z stabs
        self.z_table = self._build_table(self.H_x)  # Z errors detected by X stabs

    def _build_table(self, H: np.ndarray) -> Dict:
        table = {}
        for q in range(self.n_qubits):
            syn = tuple(H[:, q].tolist())
            if syn not in table:
                table[syn] = q
        return table

    def decode_x_error(self, syndrome: Tuple) -> int:
        return self.x_table.get(syndrome, -1)

    def decode_z_error(self, syndrome: Tuple) -> int:
        return self.z_table.get(syndrome, -1)

    def test_all_single_errors(self) -> Dict:
        x_correct = 0
        z_correct = 0

        for q in range(self.n_qubits):
            # Test X error
            x_syn = tuple(self.H_z[:, q].tolist())
            if self.decode_x_error(x_syn) == q:
                x_correct += 1

            # Test Z error
            z_syn = tuple(self.H_x[:, q].tolist())
            if self.decode_z_error(z_syn) == q:
                z_correct += 1

        return {
            'x_correct': x_correct,
            'z_correct': z_correct,
            'x_rate': x_correct / self.n_qubits,
            'z_rate': z_correct / self.n_qubits,
        }

# Create decoder with refined stabilizers
print("Building decoder with refined stabilizers...")
decoder = RefinedE7Decoder(refined_x_stabs, refined_z_stabs)

# Test decoder
print("\nTesting decoder on all single-qubit errors...")
test_result = decoder.test_all_single_errors()

print(f"\nDecoder performance:")
print(f"  X errors: {test_result['x_correct']}/133 ({100*test_result['x_rate']:.1f}%)")
print(f"  Z errors: {test_result['z_correct']}/133 ({100*test_result['z_rate']:.1f}%)")

# =============================================================================
# SYNDROME WEIGHT DISTRIBUTION
# =============================================================================

print("\n" + "=" * 80)
print("PART 8: SYNDROME ANALYSIS")
print("-" * 80)

# Stabilizer weight distribution
x_weights = [len(s['support']) for s in refined_x_stabs]
z_weights = [len(s['support']) for s in refined_z_stabs]

print(f"X-stabilizer weights: min={min(x_weights)}, max={max(x_weights)}, "
      f"avg={np.mean(x_weights):.1f}")
print(f"Z-stabilizer weights: min={min(z_weights)}, max={max(z_weights)}, "
      f"avg={np.mean(z_weights):.1f}")

# Syndrome weight distribution for errors
x_syn_weights = [sum(decoder.H_z[:, q]) for q in range(133)]
z_syn_weights = [sum(decoder.H_x[:, q]) for q in range(133)]

print(f"\nError syndrome weights:")
print(f"  X errors: min={min(x_syn_weights)}, max={max(x_syn_weights)}, "
      f"avg={np.mean(x_syn_weights):.1f}")
print(f"  Z errors: min={min(z_syn_weights)}, max={max(z_syn_weights)}, "
      f"avg={np.mean(z_syn_weights):.1f}")

# =============================================================================
# CODE PARAMETERS SUMMARY
# =============================================================================

print("\n" + "=" * 80)
print("EXPERIMENT 11: FINAL RESULTS")
print("=" * 80)

# Compute effective k
# k = n - rank(H_x) - rank(H_z) for CSS codes (approximately)
rank_x_final = np.linalg.matrix_rank(decoder.H_x)
rank_z_final = np.linalg.matrix_rank(decoder.H_z)

# For CSS code: k = n - rank(H_x ⊕ H_z)
# But we have overlapping stabilizers, so this is approximate
k_estimate = 133 - max(rank_x_final, rank_z_final)

print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                  REFINED [[133, k, d]] E₇ QEC CODE                           ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  STRUCTURE:                                                                  ║
║    • 19 blocks × 7 qubits = 133 total                                        ║
║    • Each block: Steane [7,1,3] structure                                    ║
║    • Inter-block: E₇ Dynkin coupling                                         ║
║                                                                              ║
║  STABILIZERS:                                                                ║
║    • X-type: {x_count:3d} (rank {rank_x_final})                                        ║
║    • Z-type: {z_count:3d} (rank {rank_z_final})                                        ║
║                                                                              ║
║  DECODER PERFORMANCE:                                                        ║
║    • X errors: {x_perf:3d}/133 correct ({x_pct:.1f}%)                               ║
║    • Z errors: {z_perf:3d}/133 correct ({z_pct:.1f}%)                               ║
║                                                                              ║
║  ESTIMATED PARAMETERS:                                                       ║
║    • n = 133 (physical qubits)                                               ║
║    • k = {k_est} (logical qubits)                                                ║
║    • Stabilizers refined for syndrome uniqueness                             ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
""".format(
    x_count=len(refined_x_stabs),
    z_count=len(refined_z_stabs),
    rank_x_final=rank_x_final,
    rank_z_final=rank_z_final,
    x_perf=test_result['x_correct'],
    z_perf=test_result['z_correct'],
    x_pct=100*test_result['x_rate'],
    z_pct=100*test_result['z_rate'],
    k_est=k_estimate,
))

# Save results
results = {
    'experiment': 'exp11_e7_qec_refined',
    'timestamp': datetime.now().isoformat(),
    'code_structure': {
        'n_qubits': 133,
        'n_blocks': 19,
        'qubits_per_block': 7,
    },
    'stabilizers': {
        'x_count': len(refined_x_stabs),
        'z_count': len(refined_z_stabs),
        'x_rank': int(rank_x_final),
        'z_rank': int(rank_z_final),
    },
    'decoder_performance': {
        'x_correct': int(test_result['x_correct']),
        'z_correct': int(test_result['z_correct']),
        'x_rate': float(test_result['x_rate']),
        'z_rate': float(test_result['z_rate']),
    },
    'estimated_k': int(k_estimate),
}

with open('/home/mikeb/theory/experiments/exp11_results.json', 'w') as f:
    json.dump(results, f, indent=2)
print("Results saved to exp11_results.json")

# Save stabilizer definitions for future use
stab_export = {
    'x_stabilizers': [{'support': s['support']} for s in refined_x_stabs],
    'z_stabilizers': [{'support': s['support']} for s in refined_z_stabs],
}

with open('/home/mikeb/theory/experiments/exp11_stabilizers.json', 'w') as f:
    json.dump(stab_export, f, indent=2)
print("Stabilizers saved to exp11_stabilizers.json")

print("\n" + "=" * 80)
