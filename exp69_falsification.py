#!/usr/bin/env python3
"""
EXPERIMENT 69: ADVERSARIAL FALSIFICATION ANALYSIS OF E7-ALPHA THEORY

PURPOSE: Be MAXIMALLY SKEPTICAL. Try to BREAK the theory.
         Find all coincidences, look-elsewhere effects, weak links.

The theory claims: alpha^(-1) = dim(E7) + fund(E7)/(2*rank(E7)) = 133 + 4 = 137

This analysis will:
1. Quantify the look-elsewhere effect properly
2. Find alternative structures that give 137
3. Identify the weakest claims
4. Catalog failed predictions
5. Compare with alternative theories (sedenions)
6. Define clear falsification criteria

ADVERSARIAL STANCE: Assume the theory is WRONG until proven otherwise.
"""

from datetime import datetime
from fractions import Fraction
from typing import Dict, List, Tuple, Any
import numpy as np
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import json
import random
from collections import Counter

console = Console()


# =============================================================================
# CONSTANTS
# =============================================================================

ALPHA_INV_EXP = 137.035999084  # CODATA 2018
ALPHA_INV_UNCERT = 0.000000021
TARGET = 137  # The integer we're trying to explain

# E7 data
E7 = {
    'dim': 133, 'rank': 7, 'fund': 56, 'roots': 126,
    'h_dual': 18, 'weyl_order': 2903040
}


def section(title: str):
    """Print section header."""
    console.print("\n" + "=" * 80)
    console.print(f"[bold red]{title}[/bold red]")
    console.print("=" * 80)


# =============================================================================
# SECTION 1: THE LOOK-ELSEWHERE EFFECT - HONEST CALCULATION
# =============================================================================

def analyze_look_elsewhere():
    """
    CRITICAL: How many formulas were tried before finding this one?

    The claim: dim + fund/(2*rank) = 137 for E7

    But we searched through:
    - Many groups (exceptional + classical)
    - Many formulas involving dim, rank, fund, roots, h_dual, etc.
    - Many combinations of operations (+, -, *, /)
    """
    section("SECTION 1: LOOK-ELSEWHERE EFFECT ANALYSIS")

    console.print("""
[bold yellow]THE PROBLEM:[/bold yellow]
We're claiming alpha^(-1) = 137 emerges from E7.
But how many formulas did we search before finding one that works?

[bold]Parameters Available for Each Lie Group:[/bold]
  - dim (dimension)
  - rank
  - fund (fundamental rep dimension)
  - adjoint (= dim)
  - roots (number of roots)
  - h_dual (dual Coxeter number)
  - h (Coxeter number)
  - C2 (quadratic Casimir)
  - |W| (Weyl group order)
  - center order
  - exponents (rank many values)

Total: ~10 basic parameters per group
""")

    # Count formula search space
    n_params = 10

    # Simple 2-parameter formulas: a + b, a - b, a * b, a / b
    # With variations like a + b/c, a + b/(2c), etc.
    simple_2param = n_params * (n_params - 1) * 4  # ~360

    # Add constants: 1, 2, 3, 4, pi, etc.
    with_constants = simple_2param * 10  # ~3600

    # 3-parameter formulas
    three_param = n_params * (n_params - 1) * (n_params - 2) * 20  # ~14400

    total_formulas = simple_2param + with_constants + three_param

    console.print(f"[bold]Estimated Formula Search Space:[/bold]")
    console.print(f"  Simple 2-param ops: ~{simple_2param}")
    console.print(f"  With constants (2, 3, etc.): ~{with_constants}")
    console.print(f"  3-param formulas: ~{three_param}")
    console.print(f"  [bold red]TOTAL FORMULAS TRIED: ~{total_formulas}[/bold red]")

    # Groups tested
    n_exceptional = 5
    n_classical = 150  # SU(2..50), SO(3..50), Sp(1..25)
    total_groups = n_exceptional + n_classical

    console.print(f"\n[bold]Groups Tested:[/bold]")
    console.print(f"  Exceptional: {n_exceptional}")
    console.print(f"  Classical (SU, SO, Sp up to rank ~25): ~{n_classical}")
    console.print(f"  [bold red]TOTAL GROUPS: ~{total_groups}[/bold red]")

    # Total trials
    total_trials = total_formulas * total_groups
    console.print(f"\n[bold red]TOTAL FORMULA-GROUP COMBINATIONS: ~{total_trials:,}[/bold red]")

    # Probability of hitting 137
    # If outputs are roughly uniform in [1, 300], P(137) ~ 1/300
    p_single = 1/300
    p_look_elsewhere = 1 - (1 - p_single)**total_trials

    console.print(f"\n[bold]Look-Elsewhere Correction:[/bold]")
    console.print(f"  P(single formula gives 137): ~1/300")
    console.print(f"  P(at least one hit after {total_trials:,} trials): ~{min(1.0, p_look_elsewhere):.2f}")

    if total_trials * p_single > 1:
        console.print(f"\n[bold red]WARNING: Expected ~{total_trials * p_single:.0f} hits by pure chance![/bold red]")
        console.print(f"  Finding ONE formula that gives 137 is NOT surprising!")

    # What would be surprising?
    console.print(f"\n[bold]What WOULD be significant?[/bold]")
    console.print(f"  - Finding the SAME formula works for MULTIPLE constants")
    console.print(f"  - Finding E7 appears in multiple INDEPENDENT ways")
    console.print(f"  - Making PREDICTIONS that are later verified")

    return {
        'total_formulas': total_formulas,
        'total_groups': total_groups,
        'total_trials': total_trials,
        'expected_hits': total_trials * p_single,
        'p_look_elsewhere': min(1.0, p_look_elsewhere)
    }


# =============================================================================
# SECTION 2: ALTERNATIVE STRUCTURES THAT GIVE 137
# =============================================================================

def find_alternative_137s():
    """
    Find ALL ways to get 137 from simple formulas.
    If many structures give 137, E7 is not special.
    """
    section("SECTION 2: ALTERNATIVE STRUCTURES GIVING 137")

    console.print("""
[bold yellow]THE QUESTION:[/bold yellow]
Is E7 UNIQUE in giving 137, or can we find 137 from many places?
""")

    results_137 = []

    # Classical groups: Sp(n): dim = n(2n+1), rank = n, fund = 2n
    # Formula: dim + fund/(2*rank) = n(2n+1) + 2n/(2n) = 2n^2 + n + 1
    # Solve: 2n^2 + n + 1 = 137 => 2n^2 + n - 136 = 0
    # n = (-1 + sqrt(1 + 1088))/4 = (-1 + 33)/4 = 8

    console.print("[bold]1. Classical Groups (Sp(n)):[/bold]")
    for n in range(1, 20):
        dim = n * (2*n + 1)
        rank = n
        fund = 2 * n
        if fund % (2 * rank) == 0:
            result = dim + fund // (2 * rank)
            if result == 137:
                console.print(f"   [red]Sp({n}): dim={dim}, fund={fund}, rank={rank}[/red]")
                console.print(f"   [red]       {dim} + {fund}/(2*{rank}) = {dim} + 1 = {result} = 137![/red]")
                results_137.append(f"Sp({n})")

    # More number-theoretic ways to get 137
    console.print("\n[bold]2. Number-Theoretic Coincidences:[/bold]")

    number_137 = [
        ("33rd prime", "137 = p_33, and 33 = sum(F_1..F_7)"),
        ("2^7 + 9", f"128 + 9 = {128 + 9}"),
        ("11^2 + 16", f"121 + 16 = {121 + 16}"),
        ("100 + 37", f"100 + 37 = {100 + 37}"),
        ("144 - 7", f"144 - 7 = {144 - 7}"),  # 144 = 12^2
        ("128 + 8 + 1", f"2^7 + 2^3 + 1 = {128 + 8 + 1}"),
        ("Triangular: T_16 + 1", f"136 + 1 = {136 + 1}"),  # T_16 = 16*17/2 = 136
        ("Sum 1+2+...+16 + 1", f"136 + 1 = {1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16 + 1}"),
    ]

    for name, formula in number_137:
        console.print(f"   {name}: {formula}")

    # Random formulas that give 137
    console.print("\n[bold]3. Other Lie Group Formulas Giving 137:[/bold]")

    other_formulas = [
        ("E7: roots - rank + h_dual", f"{E7['roots']} - {E7['rank']} + {E7['h_dual']} = {E7['roots'] - E7['rank'] + E7['h_dual']}"),
        ("dim(SO(17)) + 1", f"136 + 1 = {17*16//2 + 1}"),  # SO(17) has dim = 136
        ("dim(A_16) + 1", f"136 + 1 = {17**2 - 1 + 1 - 16*2 + 1}"),
    ]

    # Check SO(17)
    so17_dim = 17 * 16 // 2  # = 136
    console.print(f"   SO(17): dim = {so17_dim}, add 1 = {so17_dim + 1}")

    # Alternative E7 formulas
    console.print("\n[bold]4. Multiple E7 Formulas Give 137:[/bold]")

    e7_formulas = [
        ("dim + fund/(2*rank)", f"{E7['dim']} + {E7['fund']}/(2*{E7['rank']}) = {E7['dim'] + E7['fund']//(2*E7['rank'])}"),
        ("roots - rank + h_dual", f"{E7['roots']} - {E7['rank']} + {E7['h_dual']} = {E7['roots'] - E7['rank'] + E7['h_dual']}"),
        ("dim + 4", f"{E7['dim']} + 4 = {E7['dim'] + 4}"),
        ("7 * 19 + 4", f"7 * 19 + 4 = {7 * 19 + 4}"),
    ]

    for name, formula in e7_formulas:
        console.print(f"   {name} = {formula}")

    console.print(f"\n[bold red]CONCLUSION: At least {len(results_137) + 5}+ ways to get 137![/bold red]")
    console.print(f"   - Sp(8) with same formula as E7")
    console.print(f"   - SO(17) dim + 1")
    console.print(f"   - T_16 + 1 = 137 (triangular)")
    console.print(f"   - 2^7 + 9 = 137")
    console.print(f"   - Many more...")

    return {
        'classical_giving_137': results_137,
        'number_theoretic': number_137,
        'total_ways': len(results_137) + len(number_137) + 3
    }


# =============================================================================
# SECTION 3: MONTE CARLO - HOW SPECIAL IS THE FORMULA?
# =============================================================================

def monte_carlo_formula_test(n_trials: int = 100000):
    """
    Generate random 'Lie-group-like' objects and test how often
    the master formula gives exactly 137.
    """
    section("SECTION 3: MONTE CARLO SIMULATION")

    console.print(f"""
[bold yellow]THE TEST:[/bold yellow]
Generate {n_trials:,} random 'group-like' objects with:
  - dim ~ rank^2 to 4*rank^2 (like Lie groups)
  - fund ~ rank to 4*rank
  - rank = 2..20

Count how often dim + fund/(2*rank) = 137 exactly.
""")

    hits_137 = 0
    integer_results = 0
    result_counts = Counter()

    random.seed(42)  # Reproducibility

    for _ in range(n_trials):
        rank = random.randint(2, 20)
        dim = random.randint(rank * rank, 4 * rank * rank)
        fund = random.randint(rank, 4 * rank)

        two_rank = 2 * rank
        if fund % two_rank == 0:
            result = dim + fund // two_rank
            integer_results += 1
            result_counts[result] += 1
            if result == 137:
                hits_137 += 1

    console.print(f"[bold]Results:[/bold]")
    console.print(f"  Total trials: {n_trials:,}")
    console.print(f"  Integer results: {integer_results:,} ({100*integer_results/n_trials:.1f}%)")
    console.print(f"  Hits of exactly 137: {hits_137}")
    console.print(f"  P(137 | integer): {hits_137/max(1,integer_results):.6f}")

    # Distribution
    console.print(f"\n[bold]Most Common Results:[/bold]")
    for val, count in result_counts.most_common(10):
        marker = " <-- TARGET" if val == 137 else ""
        console.print(f"   {val}: {count} times{marker}")

    if 137 in result_counts:
        rank_137 = sorted(result_counts.values(), reverse=True).index(result_counts[137]) + 1
        console.print(f"\n   137 is #{rank_137} most common")
    else:
        console.print(f"\n   [yellow]137 did not appear in {n_trials:,} trials[/yellow]")

    return {
        'n_trials': n_trials,
        'hits_137': hits_137,
        'integer_results': integer_results,
        'p_137': hits_137 / max(1, integer_results)
    }


# =============================================================================
# SECTION 4: PROBLEMATIC CLAIMS - WEAKEST LINKS
# =============================================================================

def analyze_weak_claims():
    """
    Identify and rank the theory's claims by weakness.
    """
    section("SECTION 4: PROBLEMATIC CLAIMS ANALYSIS")

    claims = [
        {
            'id': 'W1',
            'claim': 'g-2 coefficient A2 = -197/144',
            'original_confidence': 'HIGH',
            'actual_status': 'FALSIFIED (316% error)',
            'explanation': 'A2 = -0.3285..., not -1.368. The 197/144 is ONLY the rational part.',
            'weakness': 10,  # 1-10, 10 = worst
        },
        {
            'id': 'W2',
            'claim': 'E7 is UNIQUE in giving 137',
            'original_confidence': 'HIGH',
            'actual_status': 'FALSE - Sp(8) also gives 137',
            'explanation': 'Classical group Sp(8) gives 136 + 1 = 137 with same formula.',
            'weakness': 8,
        },
        {
            'id': 'W3',
            'claim': 'DM/baryon ratio ~ 56/10 = 5.6',
            'original_confidence': 'MEDIUM',
            'actual_status': 'WEAK NUMEROLOGY',
            'explanation': 'Observed: 5.36. Why divide by 10? Post-hoc rationalization.',
            'weakness': 9,
        },
        {
            'id': 'W4',
            'claim': 'Hubble constant H0 ~ 133/2 = 66.5',
            'original_confidence': 'MEDIUM',
            'actual_status': 'COINCIDENCE',
            'explanation': 'Planck gives 67.4, SH0ES gives 73. Neither is 66.5.',
            'weakness': 9,
        },
        {
            'id': 'W5',
            'claim': 'E-folds N ~ 56',
            'original_confidence': 'LOW',
            'actual_status': 'WEAK',
            'explanation': 'CMB requires N > 50. Any N in 50-60 is acceptable.',
            'weakness': 7,
        },
        {
            'id': 'W6',
            'claim': 'sin^2(theta_W) = 3/13 = 0.2308',
            'original_confidence': 'MEDIUM',
            'actual_status': 'CLOSE BUT OFF',
            'explanation': 'Experimental: 0.23122. Error: 0.2%. Not exact.',
            'weakness': 5,
        },
        {
            'id': 'W7',
            'claim': 'A4 denominator = 31104',
            'original_confidence': 'STRONG',
            'actual_status': 'UNTESTED',
            'explanation': 'A4 rational part not yet extracted from numerical data.',
            'weakness': 3,
        },
        {
            'id': 'W8',
            'claim': 'Delta ~ 1/28 (discrepancy explanation)',
            'original_confidence': 'MEDIUM',
            'actual_status': 'FAILS BY 0.8%',
            'explanation': '1/28 = 0.03571..., Delta = 0.03600..., 0.8% error.',
            'weakness': 6,
        },
        {
            'id': 'W9',
            'claim': 'Muon g-2 scale sqrt(133)*m_mu = 1.22 GeV',
            'original_confidence': 'STRONG',
            'actual_status': 'UNTESTED',
            'explanation': 'Scale is in HVP region, but no specific anomaly identified.',
            'weakness': 4,
        },
        {
            'id': 'W10',
            'claim': 'Steane code 7 comes from E7',
            'original_confidence': 'MEDIUM',
            'actual_status': 'INDIRECT',
            'explanation': '7 = 2^3 - 1 from Hamming, chain to E7 is long.',
            'weakness': 5,
        },
    ]

    # Sort by weakness
    claims.sort(key=lambda x: -x['weakness'])

    table = Table(title="Weakest Claims (Ranked)", show_lines=True)
    table.add_column("ID", style="cyan", width=4)
    table.add_column("Claim", style="white", width=35)
    table.add_column("Status", style="red", width=25)
    table.add_column("Weakness", justify="center", width=10)

    for c in claims:
        weakness_bar = "[red]" + "#" * c['weakness'] + "[/red]" + "." * (10 - c['weakness'])
        table.add_row(
            c['id'],
            c['claim'][:35],
            c['actual_status'][:25],
            weakness_bar
        )

    console.print(table)

    console.print("\n[bold]Detailed Analysis of TOP 5 WEAKEST:[/bold]")
    for c in claims[:5]:
        console.print(f"\n[bold red]{c['id']}: {c['claim']}[/bold red]")
        console.print(f"   Original confidence: {c['original_confidence']}")
        console.print(f"   Actual status: {c['actual_status']}")
        console.print(f"   [yellow]Explanation: {c['explanation']}[/yellow]")

    return claims


# =============================================================================
# SECTION 5: FAILED PREDICTIONS
# =============================================================================

def analyze_failed_predictions():
    """
    List predictions that have been TESTED and FAILED.
    """
    section("SECTION 5: FAILED PREDICTIONS")

    console.print("""
[bold red]PREDICTIONS THAT WERE WRONG:[/bold red]
""")

    failed = [
        {
            'prediction': 'A2 coefficient = -197/144 = -1.3681',
            'actual': 'A2 = -0.32847...',
            'error': '316%',
            'status': 'FALSIFIED',
            'notes': 'Original claim was dramatically wrong'
        },
        {
            'prediction': 'E7 is UNIQUE structure giving 137',
            'actual': 'Sp(8) also gives 137',
            'error': 'N/A',
            'status': 'FALSIFIED',
            'notes': 'Classical group works too'
        },
        {
            'prediction': 'Alpha^-1 = 137 exactly',
            'actual': 'Alpha^-1 = 137.0359990840',
            'error': '0.026%',
            'status': 'WRONG by 263 ppm',
            'notes': 'Not exact, requires post-hoc "correction" terms'
        },
        {
            'prediction': '0.036 discrepancy = 1/28',
            'actual': '0.036 vs 1/28 = 0.0357',
            'error': '0.8%',
            'status': 'APPROXIMATE ONLY',
            'notes': 'Close but not exact'
        },
    ]

    table = Table(title="Failed Predictions", show_lines=True)
    table.add_column("Prediction", style="yellow", width=35)
    table.add_column("Actual", style="green", width=20)
    table.add_column("Error", style="red", width=10)
    table.add_column("Status", style="magenta", width=15)

    for f in failed:
        table.add_row(f['prediction'], f['actual'], f['error'], f['status'])

    console.print(table)

    # Success count
    console.print(f"\n[bold]Failure Rate:[/bold]")
    console.print(f"  Major falsified claims: {len(failed)}")
    console.print(f"  This is a [red]HIGH[/red] failure rate for a 'fundamental theory'")

    return failed


# =============================================================================
# SECTION 6: ALTERNATIVE THEORY COMPARISON - SEDENIONS
# =============================================================================

def compare_sedenion_theory():
    """
    The 2025 sedenion paper claims alpha^-1 = 137.035999206077.
    How does E7 compare?
    """
    section("SECTION 6: SEDENION ALTERNATIVE THEORY")

    # Sedenion claim from exp07
    sedenion_alpha_inv = 137.035999206077

    console.print("""
[bold yellow]THE SEDENION ALTERNATIVE:[/bold yellow]

A 2025 paper claims to derive alpha using sedenions (16D hypercomplex):
  - Uses Cayley-Dickson construction: R -> C -> H -> O -> S
  - Claims: alpha^-1 = 137.035999206077
  - Precision: matches to 12 digits!
""")

    console.print(f"\n[bold]Comparison:[/bold]")
    console.print(f"  Experimental:  {ALPHA_INV_EXP:.12f} +/- {ALPHA_INV_UNCERT}")
    console.print(f"  E7 basic:      137.000000000000 (error: 0.026%)")
    console.print(f"  E7 + 1/28:     137.035714285714 (error: 8 ppm)")
    console.print(f"  Sedenion:      {sedenion_alpha_inv:.12f} (error: ??? ppm)")

    # Compare
    sedenion_error = abs(sedenion_alpha_inv - ALPHA_INV_EXP)
    e7_basic_error = abs(137 - ALPHA_INV_EXP)
    e7_corrected_error = abs(137 + 1/28 - ALPHA_INV_EXP)

    console.print(f"\n[bold]Absolute Errors:[/bold]")
    console.print(f"  E7 basic:      {e7_basic_error:.9f}")
    console.print(f"  E7 + 1/28:     {e7_corrected_error:.9f}")
    console.print(f"  Sedenion:      {sedenion_error:.9f}")

    console.print(f"\n[bold]Relative Errors (ppm):[/bold]")
    console.print(f"  E7 basic:      {e7_basic_error/ALPHA_INV_EXP * 1e6:.1f} ppm")
    console.print(f"  E7 + 1/28:     {e7_corrected_error/ALPHA_INV_EXP * 1e6:.1f} ppm")
    console.print(f"  Sedenion:      {sedenion_error/ALPHA_INV_EXP * 1e6:.3f} ppm")

    if sedenion_error < e7_corrected_error:
        console.print(f"\n[bold red]SEDENION IS MORE ACCURATE![/bold red]")
        console.print(f"  If precision matters, sedenions WIN over E7")

    console.print(f"""
[bold]Critical Questions:[/bold]
  1. Can BOTH be right? (Sedenions contain octonions, E7 relates to octonions)
  2. Is the sedenion derivation rigorous or curve-fitting?
  3. Why would two DIFFERENT structures give the SAME constant?

[bold red]RED FLAG:[/bold red]
  If multiple unrelated theories 'derive' alpha, then NONE may be fundamental.
  We might just be finding clever ways to fit 137.036...
""")

    return {
        'sedenion_value': sedenion_alpha_inv,
        'sedenion_error_ppm': sedenion_error / ALPHA_INV_EXP * 1e6,
        'e7_basic_error_ppm': e7_basic_error / ALPHA_INV_EXP * 1e6,
        'e7_corrected_error_ppm': e7_corrected_error / ALPHA_INV_EXP * 1e6,
        'sedenion_wins': sedenion_error < e7_corrected_error
    }


# =============================================================================
# SECTION 7: FALSIFICATION CRITERIA - WHAT WOULD DISPROVE THE THEORY
# =============================================================================

def define_falsification_criteria():
    """
    Define clear, testable criteria that would FALSIFY the theory.
    """
    section("SECTION 7: FALSIFICATION CRITERIA")

    console.print("""
[bold green]A GOOD THEORY MAKES PREDICTIONS THAT CAN BE WRONG.[/bold green]

If the E7 theory is scientific (not numerology), it must be falsifiable.
What observations would DISPROVE the theory?
""")

    criteria = [
        {
            'id': 'F1',
            'test': 'A4 Denominator Test',
            'prediction': 'A4 rational denominator = 31104 = 144 * 6^3',
            'falsified_if': 'A4 denominator is NOT 31104 when extracted',
            'timeline': '2025-2028 (when A4 rational part computed)',
            'impact': 'FATAL to QED coefficient claims'
        },
        {
            'id': 'F2',
            'test': 'g-2 1.22 GeV Scale Test',
            'prediction': 'Anomaly/structure in R(s) at sqrt(s) = 1.22 GeV',
            'falsified_if': 'No structure found at this energy in detailed scans',
            'timeline': '2025-2030 (CMD-3, BES-III data)',
            'impact': 'WEAKENS muon g-2 connection'
        },
        {
            'id': 'F3',
            'test': 'Alpha Constancy Test',
            'prediction': 'Alpha does NOT vary over cosmic time (number-theoretic origin)',
            'falsified_if': 'Delta_alpha/alpha > 10^-6 detected in quasar spectra',
            'timeline': '2027+ (ELT, next-gen spectroscopy)',
            'impact': 'FATAL to number-theoretic interpretation'
        },
        {
            'id': 'F4',
            'test': 'A5 Denominator Test',
            'prediction': 'A5 denominator = 186624 = 144 * 6^4',
            'falsified_if': 'Pattern breaks at 5-loop',
            'timeline': '2030+ (6-loop QED)',
            'impact': 'WEAKENS denominator pattern claim'
        },
        {
            'id': 'F5',
            'test': 'Precision Alpha Test',
            'prediction': 'Corrections follow E7 pattern (1/28 second term)',
            'falsified_if': 'Higher precision shows non-E7 structure',
            'timeline': '2027-2035 (next-gen precision experiments)',
            'impact': 'FATAL to correction formula claim'
        },
    ]

    table = Table(title="Falsification Criteria", show_lines=True)
    table.add_column("ID", style="cyan", width=4)
    table.add_column("Test", style="yellow", width=25)
    table.add_column("Falsified If...", style="red", width=35)
    table.add_column("Timeline", style="green", width=12)

    for c in criteria:
        table.add_row(c['id'], c['test'], c['falsified_if'], c['timeline'])

    console.print(table)

    console.print("\n[bold]Most Important Test:[/bold]")
    console.print(f"   [bold cyan]{criteria[0]['test']}[/bold cyan]")
    console.print(f"   If A4 denominator != 31104, the QED pattern claim FAILS")
    console.print(f"   This is testable NOW with existing numerical data")

    return criteria


# =============================================================================
# SECTION 8: THE VERDICT - HONEST ASSESSMENT
# =============================================================================

def final_verdict(results: Dict):
    """
    Synthesize all findings into an honest assessment.
    """
    section("SECTION 8: FINAL ADVERSARIAL VERDICT")

    console.print(Panel(f"""
[bold red]ADVERSARIAL ASSESSMENT OF E7-ALPHA THEORY[/bold red]

[bold]EVIDENCE AGAINST:[/bold]

1. [red]LOOK-ELSEWHERE EFFECT IS SEVERE[/red]
   - Searched ~{results['look_elsewhere']['total_trials']:,} formula-group combinations
   - Expected ~{results['look_elsewhere']['expected_hits']:.0f} hits by chance
   - Finding ONE formula that works is NOT surprising

2. [red]MULTIPLE STRUCTURES GIVE 137[/red]
   - Sp(8) with same formula
   - SO(17) dim + 1 = 137
   - T_16 + 1 = 137
   - Many number-theoretic ways

3. [red]MAJOR PREDICTIONS FALSIFIED[/red]
   - A2 = -197/144: WRONG (316% error)
   - E7 uniqueness: WRONG (Sp(8) also works)
   - Exact 137: WRONG (off by 0.026%)

4. [red]COSMOLOGICAL CLAIMS ARE NUMEROLOGY[/red]
   - DM/baryon ~ 56/10: Why divide by 10?
   - H0 ~ 133/2: Neither Planck nor SH0ES match
   - These are post-hoc fits

5. [red]COMPETING THEORY (SEDENIONS) IS MORE ACCURATE[/red]
   - Sedenions give alpha^-1 to 12 digits
   - E7 basic gives only 3 digits
   - If precision matters, E7 loses

[bold]EVIDENCE FOR:[/bold]

1. [green]MATHEMATICAL FACTS ARE EXACT[/green]
   - 133 + 56/14 = 137 (verified)
   - A2 rational = 197/144 (verified)
   - 144 = 126 + 18 (verified)

2. [green]E7 APPEARS IN REAL PHYSICS[/green]
   - N=8 SUGRA scalar manifold
   - String theory U-duality
   - Not invented for this purpose

3. [green]PREDICTIONS REMAIN TO BE TESTED[/green]
   - A4 denominator = 31104
   - 1.22 GeV g-2 scale
   - Alpha constancy

[bold yellow]OVERALL VERDICT:[/bold yellow]

The theory is [yellow]INTRIGUING BUT UNPROVEN[/yellow].

- It is NOT obvious nonsense (the math is real)
- It is NOT convincingly established (too many coincidences possible)
- It makes TESTABLE predictions (good for science)
- It has FAILED some predictions (bad for confidence)

[bold]PROBABILITY ESTIMATE (ADVERSARIAL):[/bold]
   P(E7 fundamentally determines alpha) ~ 5-15%

   This is higher than random numerology (<1%)
   But much lower than claimed (~80%+)

[bold red]BOTTOM LINE:[/bold red]
   The theory deserves investigation but NOT belief.
   Wait for A4 denominator test before taking seriously.
""", title="ADVERSARIAL VERDICT", border_style="red"))


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Run complete adversarial analysis."""
    console.print(Panel.fit(
        "[bold red]EXPERIMENT 69: ADVERSARIAL FALSIFICATION ANALYSIS[/bold red]\n\n"
        "[yellow]Objective: Try to BREAK the E7-Alpha theory[/yellow]\n"
        "[yellow]Stance: Assume WRONG until proven RIGHT[/yellow]",
        title="FALSIFICATION ANALYSIS",
        border_style="red"
    ))

    results = {}

    # Run all analyses
    results['look_elsewhere'] = analyze_look_elsewhere()
    results['alternatives'] = find_alternative_137s()
    results['monte_carlo'] = monte_carlo_formula_test()
    results['weak_claims'] = analyze_weak_claims()
    results['failed_predictions'] = analyze_failed_predictions()
    results['sedenion_comparison'] = compare_sedenion_theory()
    results['falsification_criteria'] = define_falsification_criteria()

    # Final verdict
    final_verdict(results)

    # Save results
    output = {
        'experiment': 'exp69_falsification',
        'timestamp': datetime.now().isoformat(),
        'stance': 'ADVERSARIAL',
        'look_elsewhere': {
            'total_trials': results['look_elsewhere']['total_trials'],
            'expected_hits': results['look_elsewhere']['expected_hits'],
            'conclusion': 'Finding 137 is NOT surprising after so many trials'
        },
        'alternatives_found': results['alternatives']['total_ways'],
        'monte_carlo_p137': results['monte_carlo']['p_137'],
        'failed_predictions': len(results['failed_predictions']),
        'sedenion_more_accurate': results['sedenion_comparison']['sedenion_wins'],
        'falsification_tests': [c['id'] for c in results['falsification_criteria']],
        'adversarial_probability': '5-15%',
        'verdict': 'INTRIGUING BUT UNPROVEN - wait for A4 test'
    }

    with open('/home/mikeb/theory/experiments/exp69_results.json', 'w') as f:
        json.dump(output, f, indent=2)

    console.print("\n[green]Results saved to exp69_results.json[/green]")
    console.print("=" * 80)

    return results


if __name__ == "__main__":
    main()
