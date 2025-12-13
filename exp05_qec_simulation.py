#!/usr/bin/env python3
"""
EXPERIMENT 5: QEC Code Simulation with Qiskit

HYPOTHESIS: The Steane [[7,1,3]] code (7 qubits = rank(E₇)) has special properties

METHODS:
1. Implement Steane code in Qiskit
2. Test error correction capabilities
3. Compare with other codes (e.g., 5-qubit code)
4. Verify the claim that 7 qubits relates to E₇

BACKGROUND:
The Steane code uses 7 physical qubits to encode 1 logical qubit.
It can correct any single-qubit error (distance d=3).
"""

from datetime import datetime
import json
import numpy as np

print("=" * 70)
print("EXPERIMENT 5: QEC CODE SIMULATION (QISKIT)")
print("=" * 70)
print(f"Date: {datetime.now().isoformat()}")
print()

# Try to import Qiskit
try:
    from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
    from qiskit_aer import AerSimulator
    from qiskit_aer.noise import NoiseModel, depolarizing_error
    QISKIT_AVAILABLE = True
    print("✓ Qiskit and Qiskit-Aer imported successfully")
except ImportError as e:
    QISKIT_AVAILABLE = False
    print(f"✗ Qiskit import failed: {e}")
    print("  Will proceed with theoretical analysis only")

print()

# =============================================================================
# PART 1: STEANE CODE STRUCTURE ANALYSIS
# =============================================================================

print("PART 1: STEANE [[7,1,3]] CODE STRUCTURE")
print("-" * 70)

print("""
The Steane code parameters:
  n = 7 physical qubits
  k = 1 logical qubit
  d = 3 minimum distance

Key observation:
  7 = rank(E₇)

The Steane code is based on the [7,4,3] Hamming code (classical).
""")

# Steane code stabilizers
steane_stabilizers = {
    'X-type': [
        [1, 0, 1, 0, 1, 0, 1],  # X on qubits 0,2,4,6
        [0, 1, 1, 0, 0, 1, 1],  # X on qubits 1,2,5,6
        [0, 0, 0, 1, 1, 1, 1],  # X on qubits 3,4,5,6
    ],
    'Z-type': [
        [1, 0, 1, 0, 1, 0, 1],  # Z on qubits 0,2,4,6
        [0, 1, 1, 0, 0, 1, 1],  # Z on qubits 1,2,5,6
        [0, 0, 0, 1, 1, 1, 1],  # Z on qubits 3,4,5,6
    ]
}

print("Steane code stabilizers (6 total = 2 × 3):")
print("  X-type (3 stabilizers):")
for i, stab in enumerate(steane_stabilizers['X-type']):
    qubits = [j for j, v in enumerate(stab) if v == 1]
    print(f"    S_X{i+1}: X on qubits {qubits}")

print("  Z-type (3 stabilizers):")
for i, stab in enumerate(steane_stabilizers['Z-type']):
    qubits = [j for j, v in enumerate(stab) if v == 1]
    print(f"    S_Z{i+1}: Z on qubits {qubits}")

print(f"\nNumber of stabilizers: {len(steane_stabilizers['X-type']) + len(steane_stabilizers['Z-type'])}")
print(f"Expected: n - k = 7 - 1 = 6 ✓")

# =============================================================================
# PART 2: E₇ CONNECTION ANALYSIS
# =============================================================================

print("\n" + "=" * 70)
print("PART 2: E₇ CONNECTION ANALYSIS")
print("-" * 70)

print("""
Claim: The Steane code's use of 7 qubits reflects E₇ structure.

Analysis:
- The Steane code uses 7 qubits = rank(E₇) ✓
- But is this just coincidence or structural?

Historical fact:
- The Steane code was discovered in 1996 by Andrew Steane
- It's based on the classical [7,4,3] Hamming code
- The Hamming code uses 7 bits because 7 = 2³ - 1 (perfect code)

So the "7" comes from:
  7 = 2³ - 1 (Hamming theory)
NOT from:
  7 = rank(E₇) (Lie algebra)

This appears to be COINCIDENTAL, not structural.
""")

# =============================================================================
# PART 3: QISKIT SIMULATION (if available)
# =============================================================================

if QISKIT_AVAILABLE:
    print("\n" + "=" * 70)
    print("PART 3: QISKIT SIMULATION")
    print("-" * 70)

    def create_steane_encoder():
        """Create circuit to encode |0⟩ into Steane code."""
        qr = QuantumRegister(7, 'q')
        circuit = QuantumCircuit(qr)

        # Encode |0⟩ → |0_L⟩
        # Step 1: Create superposition on ancillas
        circuit.h(qr[0])
        circuit.h(qr[1])
        circuit.h(qr[2])

        # Step 2: CNOT gates to create encoded state
        circuit.cx(qr[0], qr[4])
        circuit.cx(qr[0], qr[6])
        circuit.cx(qr[1], qr[3])
        circuit.cx(qr[1], qr[6])
        circuit.cx(qr[2], qr[3])
        circuit.cx(qr[2], qr[4])
        circuit.cx(qr[2], qr[5])

        return circuit

    def create_error_syndrome_circuit():
        """Create circuit for syndrome measurement."""
        qr = QuantumRegister(7, 'data')
        anc = QuantumRegister(6, 'ancilla')
        cr = ClassicalRegister(6, 'syndrome')
        circuit = QuantumCircuit(qr, anc, cr)

        # Measure X-type stabilizers (detect Z errors)
        # S_X1: X on 0,2,4,6
        circuit.h(anc[0])
        for i in [0, 2, 4, 6]:
            circuit.cx(anc[0], qr[i])
        circuit.h(anc[0])

        # S_X2: X on 1,2,5,6
        circuit.h(anc[1])
        for i in [1, 2, 5, 6]:
            circuit.cx(anc[1], qr[i])
        circuit.h(anc[1])

        # S_X3: X on 3,4,5,6
        circuit.h(anc[2])
        for i in [3, 4, 5, 6]:
            circuit.cx(anc[2], qr[i])
        circuit.h(anc[2])

        # Measure Z-type stabilizers (detect X errors)
        # S_Z1: Z on 0,2,4,6
        for i in [0, 2, 4, 6]:
            circuit.cx(qr[i], anc[3])

        # S_Z2: Z on 1,2,5,6
        for i in [1, 2, 5, 6]:
            circuit.cx(qr[i], anc[4])

        # S_Z3: Z on 3,4,5,6
        for i in [3, 4, 5, 6]:
            circuit.cx(qr[i], anc[5])

        # Measure ancillas
        circuit.measure(anc, cr)

        return circuit

    # Test the encoder
    print("Testing Steane encoder circuit...")
    encoder = create_steane_encoder()
    print(f"  Encoder depth: {encoder.depth()}")
    print(f"  Number of gates: {len(encoder.data)}")

    # Run simulation
    print("\nRunning noiseless simulation...")
    simulator = AerSimulator()
    encoder_with_measure = encoder.copy()
    encoder_with_measure.measure_all()

    job = simulator.run(encoder_with_measure, shots=1000)
    result = job.result()
    counts = result.get_counts()

    print(f"  Output states (top 5):")
    sorted_counts = sorted(counts.items(), key=lambda x: -x[1])
    for state, count in sorted_counts[:5]:
        print(f"    |{state}⟩: {count} shots ({100*count/1000:.1f}%)")

    # Test with noise
    print("\nTesting with depolarizing noise...")
    noise_model = NoiseModel()

    # Add depolarizing error
    error_prob = 0.01  # 1% error rate
    error_1q = depolarizing_error(error_prob, 1)
    error_2q = depolarizing_error(error_prob, 2)

    noise_model.add_all_qubit_quantum_error(error_1q, ['h'])
    noise_model.add_all_qubit_quantum_error(error_2q, ['cx'])

    noisy_simulator = AerSimulator(noise_model=noise_model)
    job_noisy = noisy_simulator.run(encoder_with_measure, shots=1000)
    result_noisy = job_noisy.result()
    counts_noisy = result_noisy.get_counts()

    print(f"  With 1% depolarizing noise:")
    print(f"  Number of distinct output states: {len(counts_noisy)}")

    # Calculate fidelity (approximate)
    # In noiseless case, we expect specific states
    # With noise, we get a distribution
    most_common = sorted_counts[0][0]
    noisy_count = counts_noisy.get(most_common, 0)
    approx_fidelity = noisy_count / 1000

    print(f"  Approximate fidelity: {approx_fidelity:.3f}")

else:
    print("\n" + "=" * 70)
    print("PART 3: QISKIT SIMULATION (SKIPPED - Qiskit not available)")
    print("-" * 70)

# =============================================================================
# PART 4: COMPARISON WITH OTHER CODES
# =============================================================================

print("\n" + "=" * 70)
print("PART 4: COMPARISON WITH OTHER QEC CODES")
print("-" * 70)

codes = [
    {'name': '3-qubit repetition', 'n': 3, 'k': 1, 'd': 1, 'type': 'classical'},
    {'name': '5-qubit perfect', 'n': 5, 'k': 1, 'd': 3, 'type': 'quantum'},
    {'name': 'Steane [[7,1,3]]', 'n': 7, 'k': 1, 'd': 3, 'type': 'quantum'},
    {'name': 'Shor [[9,1,3]]', 'n': 9, 'k': 1, 'd': 3, 'type': 'quantum'},
    {'name': 'Surface d=3', 'n': 9, 'k': 1, 'd': 3, 'type': 'topological'},
]

print(f"{'Code':<25} {'n':>3} {'k':>3} {'d':>3} {'Rate':>8} {'Notes':<20}")
print("-" * 70)

for code in codes:
    rate = code['k'] / code['n']
    e7_note = ""
    if code['n'] == 7:
        e7_note = "n = rank(E₇)"
    print(f"{code['name']:<25} {code['n']:>3} {code['k']:>3} {code['d']:>3} {rate:>8.3f} {e7_note:<20}")

print("""
Analysis:
- The 5-qubit code achieves the same distance (d=3) with fewer qubits
- The Steane code is NOT the most efficient for n=7
- The "7 = rank(E₇)" appears to be coincidental
""")

# =============================================================================
# PART 5: PROPOSED [[133,7,7]] E₇ CODE
# =============================================================================

print("\n" + "=" * 70)
print("PART 5: ANALYSIS OF PROPOSED [[133,7,7]] E₇ CODE")
print("-" * 70)

print("""
The theory proposed a [[133,7,7]] code with:
  n = 133 = dim(E₇)
  k = 7 = rank(E₇)
  d = 7 = rank(E₇)

Questions to address:
1. Is this code constructible?
2. Does it have advantages over existing codes?
""")

# Compare with surface code
n_e7 = 133
k_e7 = 7
d_e7 = 7

# Surface code with same distance: needs d² = 49 qubits for 1 logical qubit
n_surface = 49
k_surface = 1
d_surface = 7

print(f"\nE₇ code vs Surface code (same distance d=7):")
print(f"  E₇ [[133,7,7]]:  {n_e7} physical → {k_e7} logical, rate = {k_e7/n_e7:.4f}")
print(f"  Surface d=7:     {n_surface} physical → {k_surface} logical, rate = {k_surface/n_surface:.4f}")
print(f"  7× Surface d=7:  {7*n_surface} physical → 7 logical, rate = {7/(7*n_surface):.4f}")

print(f"\n  Per-logical-qubit overhead:")
print(f"    E₇:     {n_e7/k_e7:.1f} physical per logical")
print(f"    Surface: {n_surface/k_surface:.1f} physical per logical")

if n_e7/k_e7 < n_surface/k_surface:
    print(f"\n  → E₇ code is {(n_surface/k_surface)/(n_e7/k_e7):.2f}× more efficient!")
else:
    print(f"\n  → Surface code is more efficient")

print("""
HOWEVER:
- The [[133,7,7]] code is THEORETICAL - not yet constructed
- The distance d=7 is assumed, not proven
- Physical implementation is challenging
- No decoder algorithm exists yet
""")

# =============================================================================
# FINAL RESULTS
# =============================================================================

print("\n" + "=" * 70)
print("EXPERIMENT 5: FINAL RESULTS")
print("=" * 70)

all_results = {
    'experiment': 'exp05_qec_simulation',
    'timestamp': datetime.now().isoformat(),
    'qiskit_available': QISKIT_AVAILABLE,
    'claims_tested': [
        'Steane code uses 7 qubits = rank(E₇)',
        'Proposed [[133,7,7]] code has advantages',
    ],
    'findings': {
        'steane_7_coincidental': True,
        'e7_code_theoretical': True,
        'e7_code_efficiency': 'Better rate than surface code IF assumptions hold',
    },
    'conclusion': None,
    'confidence': None
}

print("""
CONCLUSIONS:

1. Steane code uses 7 qubits:
   - This is from Hamming theory (7 = 2³ - 1), NOT from E₇
   - The match with rank(E₇) = 7 is COINCIDENTAL
   - Status: COINCIDENTAL CONNECTION

2. Proposed [[133,7,7]] E₇ code:
   - If constructible, would have 2.6× better rate than surface codes
   - But the code is THEORETICAL ONLY
   - Distance d=7 is ASSUMED, not proven
   - No construction or decoder exists
   - Status: UNVERIFIED (theoretical proposal)

OVERALL: The QEC claims are NOT proven.
  - The Steane-E₇ connection is coincidental
  - The [[133,7,7]] code is a theoretical proposal only
""")

all_results['conclusion'] = 'UNVERIFIED'
all_results['confidence'] = 'LOW'

# Save results
with open('/home/mikeb/theory/experiments/exp05_results.json', 'w') as f:
    json.dump(all_results, f, indent=2)
print(f"\nResults saved to exp05_results.json")

print("\n" + "=" * 70)
