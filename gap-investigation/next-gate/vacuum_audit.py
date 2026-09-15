#!/usr/bin/env python3
"""Exact additive exp47 audit. Default replays saved receipt; --create writes once.
Standard library only. No imports or execution of legacy module/main; selected
arithmetic AST expressions are checked and evaluated with exact division.
"""
import argparse
import ast
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations_with_replacement, product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


class Exact(ast.NodeTransformer):
    def visit_Constant(self, node):
        if isinstance(node.value, float):
            return ast.Call(func=ast.Name(id='F', ctx=ast.Load()),
                            args=[ast.Constant(str(node.value))], keywords=[])
        return node

    def visit_BinOp(self, node):
        node = self.generic_visit(node)
        if isinstance(node.op, ast.Div):
            return ast.Call(func=ast.Name(id='F', ctx=ast.Load()),
                            args=[node.left, node.right], keywords=[])
        return node


def calc(node, env):
    expr = Exact().visit(ast.parse(ast.unparse(node), mode='eval'))
    return eval(compile(ast.fix_missing_locations(expr), '<legacy-exact-AST>', 'eval'),
                {'F': F, 'sum': sum, 'abs': abs}, env)


def distribution(n, cap):
    """Counts ordered tuples by (sum, strictly-positive-entry count)."""
    d = Counter({(0, 0): 1})
    for _ in range(n):
        out = Counter()
        for (s, p), count in d.items():
            for x in range(cap + 1):
                out[s + x, p + (x > 0)] += count
        d = out
    return d


def run():
    src = ROOT / 'exp47_unique_vacuum.py'
    tree = ast.parse(src.read_text(encoding='utf-8'))
    search = next(x for x in tree.body if isinstance(x, ast.FunctionDef) and x.name == 'search_unique_vacuum')
    result_class = next(x for x in tree.body if isinstance(x, ast.ClassDef) and x.name == 'VacuumSearchResult')
    prop = next(x for x in result_class.body if isinstance(x, ast.FunctionDef) and x.name == 'is_candidate')
    ret = next(x.value for x in prop.body if isinstance(x, ast.Return))
    assignments = {}
    for x in ast.walk(search):
        if isinstance(x, ast.Assign) and len(x.targets) == 1 and isinstance(x.targets[0], ast.Name):
            assignments[x.targets[0].id] = x.value
    required = {
        'flux': 'tuple(np.random.randint(0, 11, size=4).tolist())',
        'e7_preserved': 'sum(flux) % 7 == 0',
        'moduli_stabilized': 'sum((1 for f in flux if f > 0)) >= 3',
        'flux_correction': 'sum(flux) / (2 * rank_e7)',
        'alpha_inv': 'dim_e7 + flux_correction',
        'swampland_ok': '120 < alpha_inv < 150',
    }
    for name, expected in required.items():
        assert ast.dump(assignments[name]) == ast.dump(ast.parse(expected, mode='eval').body), name
    expected_ret = 'abs(self.alpha_inv - 137) < 0.1 and self.e7_preserved and self.moduli_stabilized and self.swampland_ok'
    assert ast.dump(ret) == ast.dump(ast.parse(expected_ret, mode='eval').body)

    def evaluate(flux):
        env = {'flux': tuple(flux), 'rank_e7': 7, 'dim_e7': 133}
        for name in ('e7_preserved', 'moduli_stabilized', 'flux_correction', 'alpha_inv', 'swampland_ok'):
            env[name] = calc(assignments[name], env)
        obj = type('Result', (), {k: env[k] for k in ('alpha_inv', 'e7_preserved', 'moduli_stabilized', 'swampland_ok')})()
        return {
            'flux': list(flux), 'sum': sum(flux),
            'alpha_inv': str(env['alpha_inv']),
            'sum_divisible_by_7': env['e7_preserved'],
            'positive_count_at_least_3': env['moduli_stabilized'],
            'range_120_150': env['swampland_ok'],
            'target_selected': calc(ret, {'self': obj}),
            'in_original_domain': len(flux) == 4 and all(type(x) is int and 0 <= x <= 10 for x in flux),
        }

    # Verify DP independently against direct enumeration on small domains.
    dp_tests = []
    for n, cap in ((1, 2), (3, 3), (4, 2)):
        brute = Counter((sum(t), sum(x > 0 for x in t)) for t in product(range(cap + 1), repeat=n))
        assert distribution(n, cap) == brute
        dp_tests.append({'n': n, 'cap': cap, 'tuples': (cap + 1) ** n, 'passed': True})

    # Deliberate *diagnostic* extension to printed arity, not a repaired theory.
    n, cap = 8, 10
    d = distribution(n, cap)
    assert sum(d.values()) == (cap + 1) ** n
    pre = Counter()
    for (s, p), count in d.items():
        a = F(133) + F(s, 14)
        if s % 7 == 0 and p >= 3 and 120 < a < 150:
            pre[s] += count
    # Independent permutation-orbit enumeration; no gauge equivalence asserted.
    orbits = Counter()
    for t in combinations_with_replacement(range(cap + 1), n):
        if sum(t) % 7 == 0 and sum(x > 0 for x in t) >= 3 and 120 < F(133) + F(sum(t), 14) < 150:
            orbits[sum(t)] += 1
    selected = [s for s in pre if abs(F(133) + F(s, 14) - 137) < F(1, 10)]
    assert selected == [56]
    # For integer sum and divisibility, target-window iff sum=56, in all
    # residue-allowed values in this bounded diagnostic (not FP arithmetic).
    assert all((abs(F(133) + F(s, 14) - 137) < F(1, 10)) == (s == 56)
               for s in range(0, n * cap + 1, 7))
    witnesses = [evaluate(t) for t in (
        (7,) * 8, (6, 8, 7, 7, 7, 7, 7, 7),
        (0, 0, 7, 7, 7, 7, 14, 14), (0, 0, 0, 0, 0, 7, 7, 7),
        (1, 1, 1, 4), (0, 0, 0, 0, 0, 7, 7, 14))]
    assert witnesses[0]['target_selected'] and not witnesses[0]['in_original_domain']
    assert witnesses[1]['target_selected'] and sorted(witnesses[0]['flux']) != sorted(witnesses[1]['flux'])
    assert witnesses[2]['target_selected']
    assert all(w['sum_divisible_by_7'] and w['positive_count_at_least_3'] and w['range_120_150'] for w in witnesses)
    assert len({w['alpha_inv'] for w in witnesses}) > 1
    # The summary adds per-entry quantization, absent from the search.
    unit7 = [t for t in product((0, 7), repeat=8) if sum(t) == 56 and sum(x > 0 for x in t) >= 3]
    assert unit7 == [(7,) * 8]
    for w in witnesses[:3]:
        w['all_entries_multiple_of_7'] = all(x % 7 == 0 for x in w['flux'])

    # Cross-route formula discrepancy, checked exactly without interpreting
    # these toy formulas as geometry or integrating a superpotential.
    g2 = next(x for x in tree.body if isinstance(x, ast.ClassDef) and x.name == 'G2Compactification')
    stab = next(x for x in g2.body if isinstance(x, ast.FunctionDef) and x.name == 'analyze_moduli_stabilization')
    g2_assign = {x.targets[0].id: ast.unparse(x.value) for x in stab.body if isinstance(x, ast.Assign)}
    assert g2_assign['n_moduli'] == '43'
    assert g2_assign['n_stabilized'] == 'min(len(self.g_flux_quanta), n_moduli)'
    cross_route = {'G2_flux_4_alpha_inv': str(F(133) + F(sum([4]), len([4]))),
                   'G2_flux_4_claimed_stabilized_count': min(len([4]), 43),
                   'G2_n_moduli': 43,
                   'G2_eight_sevens_alpha_inv': str(F(133) + F(56, 8)),
                   'part8_eight_sevens_alpha_inv': witnesses[0]['alpha_inv']}
    # Static inventory is auditable source evidence, not a proof by keyword absence.
    inventory = [{'name': x.name, 'line': x.lineno, 'end_line': x.end_lineno}
                 for x in ast.walk(tree) if isinstance(x, (ast.FunctionDef, ast.AsyncFunctionDef))]
    sources = ['exp47_unique_vacuum.py', 'EXP47_UNIQUE_VACUUM_SUMMARY.md', 'gap-investigation/REPORT.md']
    return {
        'schema': 'exp47-next-gate-v1', 'passed': True,
        'claim_boundary': 'Exact finite arithmetic and source audit only; no vacuum equations solved, no stability or E7-invariance certification, no physical no-go, no alpha fit, no Lean proof.',
        'source_sha256': {name: digest(ROOT / name) for name in sources},
        'artifact_sha256': {'vacuum_audit.py': digest(Path(__file__)), 'vacuum-report.md': digest(HERE / 'vacuum-report.md')},
        'source_expression_checks': {name: ast.unparse(assignments[name]) for name in required},
        'candidate_property': ast.unparse(ret),
        'dp_crosschecks': dp_tests,
        'diagnostic_domain': {'arity': n, 'entry_min': 0, 'entry_max': cap, 'ordered_total': sum(d.values()),
                              'not_original_search': True, 'not_physical_vacua': True},
        'pretarget_distribution': [{'sum': s, 'alpha_inv': str(F(133) + F(s, 14)), 'ordered_count': pre[s],
                                    'permutation_orbit_count': orbits[s]} for s in sorted(pre)],
        'pretarget_ordered_total': sum(pre.values()),
        'target_selected_sums': selected,
        'target_selected_ordered_count': sum(pre[s] for s in selected),
        'target_selected_permutation_orbit_count': sum(orbits[s] for s in selected),
        'witnesses': witnesses,
        'extra_per_entry_units7_with_cap10_target_count': len(unit7),
        'cross_route': cross_route,
        'function_inventory': inventory,
        'missing_physical_input_scope': 'Manual inspection of exp47 and its summary: no specified finite action/metric/gauge-kinetic function with derived vacuum equations and mass spectrum; boolean/count proxies cannot certify them.',
        'next_physical_gate': {'status': 'BLOCKED_MISSING_ACTION',
            'required_before_execution': ['One independently specified finite action and field domain',
                'Flux basis, true singlet/commutator constraints and tadpole bounds',
                'Gauge equivalence and charge/trace conventions',
                'Stationarity equations and kinetic metric',
                'Complete isolated solutions plus flat-direction and physical mass/stability checks',
                'Gauge-kinetic function evaluated without target selection'],
            'stop_rule': 'No target-informed parameter, domain, constraint or correction adjustment; report missing data or continuous freedom and stop.'}
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--create', action='store_true', help='Create receipt exclusively; fails if it exists.')
    args = ap.parse_args()
    path = HERE / 'vacuum-receipt.json'
    if args.create:
        actual = run()
        with path.open('x', encoding='utf-8', newline='\n') as f:
            json.dump(actual, f, indent=2, sort_keys=True)
            f.write('\n')
        mode = 'created'
    else:
        # Read first; never regenerate a missing/stale receipt before comparing.
        saved = json.loads(path.read_text(encoding='utf-8'))
        actual = run()
        assert actual == saved, 'Saved receipt differs from exact recomputation or source/artifact hashes'
        mode = 'replayed'
    print(json.dumps({'mode': mode, 'passed': actual['passed'],
        'ordered_total': actual['diagnostic_domain']['ordered_total'],
        'pretarget_ordered_total': actual['pretarget_ordered_total'],
        'pretarget_distribution': actual['pretarget_distribution'],
        'selected_ordered': actual['target_selected_ordered_count'],
        'selected_permutation_orbits': actual['target_selected_permutation_orbit_count'],
        'cross_route': actual['cross_route'],
        'physical_gate': actual['next_physical_gate']['status']}, indent=2))


if __name__ == '__main__':
    main()
