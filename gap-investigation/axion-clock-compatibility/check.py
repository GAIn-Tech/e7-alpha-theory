"""Local Ward-identity gate, not a derivation of an E7 completion.
Assume delta a=q*lambda and a gauge-invariant coefficient f(a) of F^2,
with no other shifting fields or compensating CP-even variations.
Then infinitesimal invariance requires q*f'(a)=0. Contrast a two-field
invariant combination and a topological Wess-Zumino variation.
"""
import json
from z3 import Real, Solver, sat, unsat

def check(name, constraints, expected):
    s = Solver(); s.add(*constraints)
    actual = s.check()
    if actual != expected:
        raise AssertionError((name, str(actual), str(expected)))
    return {"name": name, "result": str(actual), "smt2": s.to_smt2()}

q, slope, r, fa, fb, anomaly, wz = [Real(x) for x in ('q','slope','r','fa','fb','anomaly','wz')]
checks = [
    check('one_shifting_field_no_nonconstant_invariant_kinetic_coefficient',
          [q != 0, q*slope == 0, slope != 0], unsat),
    check('neutral_scalar_can_have_kinetic_slope',
          [q == 0, q*slope == 0, slope != 0], sat),
    check('two_shifting_fields_allow_invariant_direction',
          [q == 1, r == 1, fa == 1, fb == -1, q*fa+r*fb == 0], sat),
    check('WZ_anomaly_cancellation_does_not_require_kinetic_slope',
          [q == 1, anomaly != 0, anomaly+q*wz == 0, q*slope == 0], sat),
]
print(json.dumps({"passed": True, "checks": checks,
    "scope": "Z3 exact local algebra only. Ward-identity translation, gauge transformations, operator independence and physical degrees of freedom are external assumptions. No Lean, global gauge completion, measured clock signal or all-scalar no-go claimed."}, indent=2))
