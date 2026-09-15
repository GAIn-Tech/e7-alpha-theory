#!/usr/bin/env python3
from __future__ import annotations
from decimal import Decimal, getcontext
from fractions import Fraction
import hashlib
import json
from pathlib import Path

getcontext().prec = 50
DIM_E7 = 133
FUND_E7 = 56
RANK_E7 = 7
CODATA_2022_ALPHA_INV = Fraction(137035999177, 1_000_000_000)
CODATA_2022_SIGMA = Fraction(21, 1_000_000_000)

def dec(x: Fraction) -> str:
    return format(Decimal(x.numerator) / Decimal(x.denominator), "f")

def main() -> None:
    identity = Fraction(DIM_E7, 1) + Fraction(FUND_E7, 2 * RANK_E7)
    gap = CODATA_2022_ALPHA_INV - identity
    sigma_gap = gap / CODATA_2022_SIGMA
    root = Path(__file__).resolve().parents[2]
    payload = {
        "schema": "e7-alpha-openai-style-certificate-v1",
        "inputs": {
            "dim_e7": DIM_E7,
            "fund_e7": FUND_E7,
            "rank_e7": RANK_E7,
            "codata_2022_alpha_inverse_fraction": [CODATA_2022_ALPHA_INV.numerator, CODATA_2022_ALPHA_INV.denominator],
            "codata_2022_sigma_fraction": [CODATA_2022_SIGMA.numerator, CODATA_2022_SIGMA.denominator],
        },
        "e7_identity_exact": identity == 137,
        "e7_identity_value": str(identity),
        "e7_identity_formula": "133 + 56/(2*7)",
        "physical_alpha_equal_137": CODATA_2022_ALPHA_INV == identity,
        "literal_prediction_verdict": "excluded_at_codata_scale",
        "codata_2022_alpha_inverse_decimal": dec(CODATA_2022_ALPHA_INV),
        "codata_2022_sigma_decimal": dec(CODATA_2022_SIGMA),
        "gap_alpha_inverse_minus_e7_decimal": dec(gap),
        "gap_in_sigma_decimal": dec(sigma_gap),
        "source_files_sha256": {},
    }
    for rel in ["README.md", "E7Alpha.lean", "COMPREHENSIVE_VALIDATION_REPORT.md"]:
        p = root / rel
        if p.exists():
            payload["source_files_sha256"][rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
