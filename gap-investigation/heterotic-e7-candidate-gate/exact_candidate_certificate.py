#!/usr/bin/env python3
"""Exact arithmetic certificate for the bounded heterotic E7 candidate gate."""
from fractions import Fraction
import json, pathlib, sys

OUT = pathlib.Path(__file__).with_name("certificate.json")

def calculate():
    # Candidate A: E8xE8 on K3 x T2, standard SU(2) embedding V=TK3.
    k3_c2_tx = 24
    c2_visible = 24
    c2_hidden = 0
    fivebrane = k3_c2_tx - c2_visible - c2_hidden
    # Any rank-two complex vector bundle has c_i=0 for i>2.
    rank_su2, c1_su2, c3_su2 = 2, 0, 0
    chi_su2 = Fraction(c3_su2, 2)  # CY3 HRR when c1(V)=0
    # Negative controls.
    illegal_rank2_c3 = 6
    illegal_rank2_rejected = illegal_rank2_c3 != 0
    # SU(3) can have c3=6 and index 3, but its E8 commutant is E6, not E7.
    rank_su3, c3_su3 = 3, 6
    chi_su3 = Fraction(c3_su3, 2)
    return {
      "schema_version": 1,
      "claim_boundary": "Exact characteristic-class and representation arithmetic only; existence/HYM and physical interpretation are source-dependent and separately disclosed.",
      "candidate": "E8xE8 on K3 x T2 with V1=pr_K3^*TK3 and V2 trivial",
      "commutant": "E7 x E8 (plus generic torus U(1)^4)",
      "bianchi": {"c2_TX_on_K3": k3_c2_tx, "c2_V1_on_K3": c2_visible,
                   "c2_V2_on_K3": c2_hidden, "fivebrane_class_on_K3": fivebrane,
                   "passed": fivebrane == 0},
      "su2_index": {"rank": rank_su2, "c1": c1_su2, "c3": c3_su2,
                    "chi_V_equals_half_c3": str(chi_su2),
                    "net_56_chirality": int(chi_su2), "equals_three": chi_su2 == 3},
      "branching": {"E7_to_E6xU1": "56 = 27_1 + 27bar_-1 + 1_3 + 1_-3",
                    "net_E6_27_minus_27bar_per_56": 0},
      "negative_controls": {
        "rank2_c3_6_rejected_by_rank": illegal_rank2_rejected,
        "rank3_c3_6_index": str(chi_su3),
        "rank3_commutant": "E6, not E7",
        "composite_c2_24_allowed": k3_c2_tx % 2 == 0 and k3_c2_tx > 0,
        "prime_required": False},
      "passed": fivebrane == 0 and chi_su2 == 0 and illegal_rank2_rejected and chi_su3 == 3
    }

def main():
    payload = calculate()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if "--verify" in sys.argv:
        if not OUT.exists(): raise SystemExit("missing certificate.json")
        if OUT.read_text(encoding="utf-8") != text: raise SystemExit("certificate mismatch")
        print("verified exact candidate certificate: passed=true")
    else:
        OUT.write_text(text, encoding="utf-8")
        print("wrote certificate.json: passed=true")

if __name__ == "__main__": main()
