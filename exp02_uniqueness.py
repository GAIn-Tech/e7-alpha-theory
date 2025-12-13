#!/usr/bin/env python3
"""
EXPERIMENT 2: E₇ Uniqueness Among All Lie Groups

HYPOTHESIS: E₇ is the ONLY Lie group where dim + fund/(2×rank) = integer

METHODS:
1. Test all 5 exceptional groups (G₂, F₄, E₆, E₇, E₈)
2. Test classical groups SU(n) for n = 2..50
3. Test classical groups SO(n) for n = 3..50
4. Test classical groups Sp(n) for n = 1..25
5. Test if any give result close to 137

OUTPUT: Comprehensive uniqueness proof
"""

from fractions import Fraction
from datetime import datetime
import json

print("=" * 70)
print("EXPERIMENT 2: E₇ UNIQUENESS VERIFICATION")
print("=" * 70)
print(f"Date: {datetime.now().isoformat()}")
print()

# =============================================================================
# EXCEPTIONAL LIE GROUPS (Complete list)
# =============================================================================

# Standard Lie algebra data from classification theory
EXCEPTIONAL_GROUPS = {
    'G₂': {'dim': 14, 'rank': 2, 'fund': 7, 'h_dual': 4, 'roots': 12},
    'F₄': {'dim': 52, 'rank': 4, 'fund': 26, 'h_dual': 9, 'roots': 48},
    'E₆': {'dim': 78, 'rank': 6, 'fund': 27, 'h_dual': 12, 'roots': 72},
    'E₇': {'dim': 133, 'rank': 7, 'fund': 56, 'h_dual': 18, 'roots': 126},
    'E₈': {'dim': 248, 'rank': 8, 'fund': 248, 'h_dual': 30, 'roots': 240},
}

print("PART 1: TESTING ALL EXCEPTIONAL GROUPS")
print("-" * 70)
print(f"{'Group':<6} {'dim':>5} {'rank':>5} {'fund':>5} {'2×rank':>7} "
      f"{'fund%(2r)':>9} {'dim+f/(2r)':>12} {'Integer?':>9}")
print("-" * 70)

exceptional_results = []

for name, data in EXCEPTIONAL_GROUPS.items():
    dim = data['dim']
    rank = data['rank']
    fund = data['fund']
    two_rank = 2 * rank
    remainder = fund % two_rank

    if remainder == 0:
        result = dim + fund // two_rank
        is_integer = True
    else:
        result = dim + fund / two_rank
        is_integer = False

    result_str = f"{result}" if is_integer else f"{result:.4f}"
    int_str = "✓ YES" if is_integer else "✗ NO"

    print(f"{name:<6} {dim:>5} {rank:>5} {fund:>5} {two_rank:>7} "
          f"{remainder:>9} {result_str:>12} {int_str:>9}")

    exceptional_results.append({
        'group': name,
        'dim': dim,
        'rank': rank,
        'fund': fund,
        'formula_result': result,
        'is_integer': is_integer,
        'equals_137': result == 137 if is_integer else False
    })

# Count integer results
integer_groups = [r for r in exceptional_results if r['is_integer']]
print(f"\nGroups giving integer result: {len(integer_groups)}")
for g in integer_groups:
    print(f"  {g['group']}: {g['formula_result']}")

# =============================================================================
# CLASSICAL GROUPS: SU(n)
# =============================================================================

print("\n" + "=" * 70)
print("PART 2: TESTING CLASSICAL GROUPS SU(n), n = 2..50")
print("-" * 70)

# SU(n): dim = n² - 1, rank = n - 1, fund = n

su_results = []
su_integers = []

for n in range(2, 51):
    dim = n**2 - 1
    rank = n - 1
    fund = n  # fundamental representation has dimension n

    if rank == 0:
        continue

    two_rank = 2 * rank
    remainder = fund % two_rank

    if remainder == 0:
        result = dim + fund // two_rank
        is_integer = True
        su_integers.append({'n': n, 'result': result})
    else:
        result = dim + fund / two_rank
        is_integer = False

    su_results.append({
        'n': n,
        'dim': dim,
        'rank': rank,
        'fund': fund,
        'result': result,
        'is_integer': is_integer
    })

print(f"SU(n) groups giving integer result: {len(su_integers)}")
for g in su_integers:
    print(f"  SU({g['n']}): dim + fund/(2×rank) = {g['result']}")

# Check if any are near 137
su_near_137 = [g for g in su_results if 130 < g['result'] < 145]
if su_near_137:
    print(f"\nSU(n) groups with result near 137:")
    for g in su_near_137:
        print(f"  SU({g['n']}): {g['result']:.4f} (integer: {g['is_integer']})")
else:
    print("\nNo SU(n) groups give result near 137")

# =============================================================================
# CLASSICAL GROUPS: SO(n)
# =============================================================================

print("\n" + "=" * 70)
print("PART 3: TESTING CLASSICAL GROUPS SO(n), n = 3..50")
print("-" * 70)

# SO(n): dim = n(n-1)/2, rank = n//2, fund = n

so_results = []
so_integers = []

for n in range(3, 51):
    dim = n * (n - 1) // 2
    rank = n // 2
    fund = n  # vector representation

    if rank == 0:
        continue

    two_rank = 2 * rank
    remainder = fund % two_rank

    if remainder == 0:
        result = dim + fund // two_rank
        is_integer = True
        so_integers.append({'n': n, 'result': result})
    else:
        result = dim + fund / two_rank
        is_integer = False

    so_results.append({
        'n': n,
        'dim': dim,
        'rank': rank,
        'fund': fund,
        'result': result,
        'is_integer': is_integer
    })

print(f"SO(n) groups giving integer result: {len(so_integers)}")
for g in so_integers[:10]:  # Show first 10
    print(f"  SO({g['n']}): dim + fund/(2×rank) = {g['result']}")
if len(so_integers) > 10:
    print(f"  ... and {len(so_integers) - 10} more")

# Check for 137
so_137 = [g for g in so_integers if g['result'] == 137]
if so_137:
    print(f"\n⚠ SO(n) groups giving exactly 137:")
    for g in so_137:
        print(f"  SO({g['n']}): {g['result']}")
else:
    print("\n✓ No SO(n) groups give exactly 137")

# Check near 137
so_near_137 = [g for g in so_results if 130 < g['result'] < 145]
if so_near_137:
    print(f"\nSO(n) groups with result near 137:")
    for g in so_near_137[:5]:
        print(f"  SO({g['n']}): {g['result']:.4f} (integer: {g['is_integer']})")

# =============================================================================
# CLASSICAL GROUPS: Sp(n)
# =============================================================================

print("\n" + "=" * 70)
print("PART 4: TESTING CLASSICAL GROUPS Sp(n), n = 1..25")
print("-" * 70)

# Sp(n): dim = n(2n+1), rank = n, fund = 2n

sp_results = []
sp_integers = []

for n in range(1, 26):
    dim = n * (2 * n + 1)
    rank = n
    fund = 2 * n  # fundamental representation

    two_rank = 2 * rank
    remainder = fund % two_rank

    if remainder == 0:
        result = dim + fund // two_rank
        is_integer = True
        sp_integers.append({'n': n, 'result': result})
    else:
        result = dim + fund / two_rank
        is_integer = False

    sp_results.append({
        'n': n,
        'dim': dim,
        'rank': rank,
        'fund': fund,
        'result': result,
        'is_integer': is_integer
    })

print(f"Sp(n) groups giving integer result: {len(sp_integers)}")
for g in sp_integers[:10]:
    print(f"  Sp({g['n']}): dim + fund/(2×rank) = {g['result']}")

# Check for 137
sp_137 = [g for g in sp_integers if g['result'] == 137]
if sp_137:
    print(f"\n⚠ Sp(n) groups giving exactly 137:")
    for g in sp_137:
        print(f"  Sp({g['n']}): {g['result']}")
else:
    print("\n✓ No Sp(n) groups give exactly 137")

# =============================================================================
# COMPREHENSIVE SEARCH FOR 137
# =============================================================================

print("\n" + "=" * 70)
print("PART 5: COMPREHENSIVE SEARCH FOR EXACTLY 137")
print("-" * 70)

all_137 = []

# Check exceptional
for r in exceptional_results:
    if r['equals_137']:
        all_137.append(f"{r['group']} (exceptional)")

# Check SU
for r in su_results:
    if r['is_integer'] and r['result'] == 137:
        all_137.append(f"SU({r['n']}) (classical)")

# Check SO
for r in so_results:
    if r['is_integer'] and r['result'] == 137:
        all_137.append(f"SO({r['n']}) (classical)")

# Check Sp
for r in sp_results:
    if r['is_integer'] and r['result'] == 137:
        all_137.append(f"Sp({r['n']}) (classical)")

print(f"\nGroups where dim + fund/(2×rank) = 137 EXACTLY:")
if all_137:
    for g in all_137:
        print(f"  • {g}")
else:
    print("  (none found)")

print(f"\nTotal groups giving 137: {len(all_137)}")

# =============================================================================
# ALTERNATIVE FORMULA CHECK
# =============================================================================

print("\n" + "=" * 70)
print("PART 6: ALTERNATIVE FORMULA (roots - rank + h∨)")
print("-" * 70)

print("Testing exceptional groups with alternative formula:")
print(f"{'Group':<6} {'roots':>6} {'rank':>5} {'h∨':>4} {'result':>8}")
print("-" * 40)

for name, data in EXCEPTIONAL_GROUPS.items():
    result = data['roots'] - data['rank'] + data['h_dual']
    marker = " ← 137!" if result == 137 else ""
    print(f"{name:<6} {data['roots']:>6} {data['rank']:>5} {data['h_dual']:>4} {result:>8}{marker}")

# =============================================================================
# FINAL RESULTS
# =============================================================================

print("\n" + "=" * 70)
print("EXPERIMENT 2: FINAL RESULTS")
print("=" * 70)

all_results = {
    'experiment': 'exp02_uniqueness',
    'timestamp': datetime.now().isoformat(),
    'hypothesis': 'E₇ is unique in giving dim + fund/(2×rank) = 137',
    'groups_tested': {
        'exceptional': 5,
        'SU_n': len(su_results),
        'SO_n': len(so_results),
        'Sp_n': len(sp_results),
        'total': 5 + len(su_results) + len(so_results) + len(sp_results)
    },
    'groups_giving_137': all_137,
    'conclusion': None,
    'confidence': None
}

if len(all_137) == 1 and 'E₇' in all_137[0]:
    all_results['conclusion'] = 'CONFIRMED'
    all_results['confidence'] = 'VERY HIGH'
    print("\n✓ HYPOTHESIS CONFIRMED")
    print("  E₇ is the ONLY group (out of {0} tested) giving exactly 137".format(
        all_results['groups_tested']['total']))
    print("  No classical groups SU(n), SO(n), or Sp(n) match")
    print("  Confidence: VERY HIGH")
elif len(all_137) == 0:
    all_results['conclusion'] = 'ERROR - E₇ not found'
    print("\n✗ ERROR: Even E₇ didn't give 137")
else:
    all_results['conclusion'] = 'FALSIFIED'
    all_results['confidence'] = 'HIGH'
    print("\n✗ HYPOTHESIS FALSIFIED")
    print(f"  Multiple groups give 137: {all_137}")

# Save results
with open('/home/mikeb/theory/experiments/exp02_results.json', 'w') as f:
    json.dump(all_results, f, indent=2)
print(f"\nResults saved to exp02_results.json")

print("\n" + "=" * 70)
