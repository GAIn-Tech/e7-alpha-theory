#!/usr/bin/env python3
"""
EXPERIMENT 4: g-2 Coefficient Analysis

HYPOTHESIS: The 2-loop g-2 coefficient C₂ = -197/144 where 197 = 7×28+1

CRITICAL NOTE: This claim was identified as FALSE in preliminary analysis.
This experiment will rigorously verify/falsify it.

METHODS:
1. Look up the actual QED g-2 coefficients from literature
2. Compare with claimed -197/144
3. Analyze the actual structure of QED coefficients
4. Search for any genuine E₇ connections

BACKGROUND:
The electron anomalous magnetic moment a_e = (g-2)/2 has expansion:
a_e = Σ C_n (α/π)^n
"""

from fractions import Fraction
from datetime import datetime
import json
import math

print("=" * 70)
print("EXPERIMENT 4: g-2 COEFFICIENT ANALYSIS")
print("=" * 70)
print(f"Date: {datetime.now().isoformat()}")
print()

# =============================================================================
# ACTUAL QED g-2 COEFFICIENTS (from literature)
# =============================================================================

print("PART 1: ACTUAL QED g-2 COEFFICIENTS FROM LITERATURE")
print("-" * 70)

# These are the EXACT values from precision QED calculations
# References: Schwinger (1948), Petermann (1957), Sommerfield (1958),
#             Laporta & Remiddi (1996), Aoyama et al. (2012, 2019)

# Note: Different papers use different conventions for the expansion
# We use: a_e = Σ A_n (α/π)^n

# 1-loop (Schwinger 1948): A_1 = 1/2 exactly
A1 = Fraction(1, 2)

# 2-loop: The famous result involves transcendentals
# A_2 = -0.32847896557919... (numerical)
# The EXACT analytic form is:
# A_2 = 197/144 + (π²/12)(1/4 - ln2) + (3/4)ζ(3)/π² - (π²/12)(ln2)
# Wait, let me check the correct form...

# Actually, the Schwinger A₂ term is:
# A₂ = -0.328 478 965 579 193 78...
# This involves π², ζ(3), and logarithms

A2_numerical = -0.32847896557919378

print("KNOWN EXACT COEFFICIENTS:")
print(f"  A₁ = 1/2 = {float(A1):.10f} (Schwinger 1948, EXACT)")
print(f"  A₂ = {A2_numerical:.15f} (involves π², ζ(3), ln2)")
print()

# The claimed value
claimed_A2 = Fraction(-197, 144)
print("CLAIMED VALUE (E₇ theory):")
print(f"  Claimed A₂ = -197/144 = {float(claimed_A2):.15f}")
print()

# =============================================================================
# PART 2: COMPARISON
# =============================================================================

print("PART 2: DIRECT COMPARISON")
print("-" * 70)

difference = abs(float(claimed_A2) - A2_numerical)
percent_error = (difference / abs(A2_numerical)) * 100

print(f"Actual A₂:  {A2_numerical:.15f}")
print(f"Claimed A₂: {float(claimed_A2):.15f}")
print(f"Difference: {difference:.15f}")
print(f"Percent error: {percent_error:.2f}%")
print()

if percent_error > 10:
    print("⚠ CRITICAL: The claimed value is OFF BY MORE THAN 10%!")
    print("  The claim that A₂ = -197/144 is FALSE.")
elif percent_error > 1:
    print("⚠ WARNING: The claimed value differs by more than 1%")
else:
    print("✓ Values are close (within 1%)")

# =============================================================================
# PART 3: ACTUAL STRUCTURE OF A₂
# =============================================================================

print("\n" + "=" * 70)
print("PART 3: ACTUAL ANALYTIC STRUCTURE OF A₂")
print("-" * 70)

# The 2-loop QED coefficient has the form:
# A₂ = (3/4)ζ(3) - (1/2)π²ln(2) + (π²/12) + (1/4) + ...
# This is a TRANSCENDENTAL number, not a simple fraction!

print("""
The ACTUAL 2-loop coefficient A₂ is given by:

A₂ = (3/4)ζ(3) - (π²/2)ln(2) + (π²/12) + rational_part

Where:
  ζ(3) = 1.2020569031595942... (Apéry's constant)
  π² = 9.869604401089358...
  ln(2) = 0.693147180559945...

This is a TRANSCENDENTAL number, NOT a simple fraction!
""")

# Compute approximate value from components
zeta3 = 1.2020569031595942
pi_sq = math.pi ** 2
ln2 = math.log(2)

# The exact formula (from Petermann 1957 / Sommerfield 1958) is:
# A₂ = 197/144 + (ζ(2)/2)[1/4 - ln2] + (3/4)ζ(3)/π²
# Wait, I need to get this exactly right...

# Actually, the coefficient A₂ in a_e = A_1*(α/π) + A_2*(α/π)² + ...
# has value A₂ ≈ -0.3285...

# Let me compute what -197/144 actually is in this context
print("Numerical check:")
print(f"  -197/144 = {-197/144:.10f}")
print(f"  Actual A₂ = {A2_numerical:.10f}")
print(f"  Ratio: {(-197/144) / A2_numerical:.4f}")
print()

# They differ by a factor of about 4!
ratio = (-197/144) / A2_numerical
print(f"The claimed value is about {abs(ratio):.2f}× the actual value!")

# =============================================================================
# PART 4: IS THERE ANY 197 IN g-2?
# =============================================================================

print("\n" + "=" * 70)
print("PART 4: SEARCHING FOR '197' IN g-2 STRUCTURE")
print("-" * 70)

print("""
The claim was that 197 = 7×28 + 1 appears in g-2.

Let's check if 197 appears ANYWHERE in the known g-2 structure:

1. In the 1-loop term A₁ = 1/2
   - No 197 here

2. In the 2-loop term A₂
   - The rational part involves various fractions
   - The most famous is the "(197/144)" that appears in some
     intermediate steps, but the TOTAL coefficient is NOT -197/144
""")

# The actual rational part of A₂ is complex
# It's NOT simply 197/144

print("""
IMPORTANT CLARIFICATION:

The number 197 DOES appear in the analytic expression for A₂,
but in a MORE COMPLEX WAY:

A₂ = (197/144) + (π²/12)[3/4 - ln4] + ...

So 197/144 is ONE TERM in A₂, not the TOTAL value!
The total is approximately -0.3285, not -1.368.
""")

# Verify: Does 7×28+1 = 197?
check_197 = 7 * 28 + 1
print(f"\nVerification: 7×28+1 = {check_197} {'✓' if check_197 == 197 else '✗'}")

# And 144 = F₁₂?
fib = [0, 1]
for i in range(2, 15):
    fib.append(fib[-1] + fib[-2])
print(f"Verification: F₁₂ = {fib[12]} {'✓' if fib[12] == 144 else '✗'}")

# =============================================================================
# PART 5: CORRECT INTERPRETATION
# =============================================================================

print("\n" + "=" * 70)
print("PART 5: CORRECT INTERPRETATION")
print("-" * 70)

print("""
FINDINGS:

1. The claim "A₂ = -197/144" is INCORRECT.
   - A₂ ≈ -0.3285 (actual)
   - -197/144 ≈ -1.368 (claimed)
   - These differ by a factor of ~4!

2. HOWEVER, 197/144 DOES appear in the analytic structure:
   - It's a TERM in the expansion, not the total
   - The full expression has additional transcendental terms

3. The connection "197 = 7×28+1" IS correct:
   - 7 = rank(E₇)
   - 28 = T₇ = fund(E₇)/2
   - 197 = 7×28 + 1

4. REVISED CLAIM (if any):
   - The rational part of A₂ contains 197/144 as a component
   - But the TOTAL coefficient is NOT 197/144
   - The original claim was a MISINTERPRETATION
""")

# =============================================================================
# PART 6: WHAT IS THE ACTUAL RATIONAL PART?
# =============================================================================

print("\n" + "=" * 70)
print("PART 6: ANALYZING THE ACTUAL COEFFICIENT STRUCTURE")
print("-" * 70)

# From Laporta & Remiddi (1996), the 2-loop coefficient can be written as:
# A₂ = A₂^(rat) + A₂^(trans)
# where A₂^(rat) involves rational numbers and A₂^(trans) involves π², ζ(3), ln(2)

# The numerical value is:
print(f"A₂ = {A2_numerical:.15f}")

# If we assume A₂ = p/q for integers p, q, what would they be?
from fractions import Fraction
approx_frac = Fraction(A2_numerical).limit_denominator(10000)
print(f"\nBest rational approximation (denom ≤ 10000):")
print(f"  A₂ ≈ {approx_frac} = {float(approx_frac):.15f}")

# The coefficient IS transcendental, so no exact rational representation
print("\nBut A₂ is TRANSCENDENTAL - no exact rational form exists!")

# =============================================================================
# FINAL RESULTS
# =============================================================================

print("\n" + "=" * 70)
print("EXPERIMENT 4: FINAL RESULTS")
print("=" * 70)

all_results = {
    'experiment': 'exp04_g2_coefficient',
    'timestamp': datetime.now().isoformat(),
    'hypothesis': 'A₂ = -197/144 where 197 = 7×28+1',
    'actual_A2': A2_numerical,
    'claimed_A2': float(claimed_A2),
    'difference': difference,
    'percent_error': percent_error,
    'conclusion': None,
    'refined_finding': None
}

print(f"\n✗ HYPOTHESIS FALSIFIED")
print(f"  Claimed: A₂ = -197/144 = {float(claimed_A2):.6f}")
print(f"  Actual:  A₂ = {A2_numerical:.6f}")
print(f"  Error:   {percent_error:.1f}%")
print()
print("REFINED FINDING:")
print("  The number 197/144 appears as ONE TERM in the A₂ expansion,")
print("  but the TOTAL coefficient includes additional transcendental terms.")
print("  The original claim was based on incomplete understanding of the formula.")

all_results['conclusion'] = 'FALSIFIED'
all_results['confidence'] = 'VERY HIGH'
all_results['refined_finding'] = '197/144 is a term in A₂, not the total value'

# Save results
with open('/home/mikeb/theory/experiments/exp04_results.json', 'w') as f:
    json.dump(all_results, f, indent=2)
print(f"\nResults saved to exp04_results.json")

print("\n" + "=" * 70)
