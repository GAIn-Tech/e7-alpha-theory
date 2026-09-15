import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "release" / "openai-style" / "numerical_certificate.py"
CERT = ROOT / "release" / "openai-style" / "certificate-fresh.json"


def load_fresh():
    raw = subprocess.check_output([sys.executable, str(SCRIPT)], cwd=ROOT, text=True)
    return json.loads(raw)


def test_certificate_is_exact_and_fail_closed():
    cert = load_fresh()
    assert cert["schema"] == "e7-alpha-openai-style-certificate-v1"
    assert cert["e7_identity_exact"] is True
    assert Fraction(cert["e7_identity_value"]) == Fraction(137, 1)
    assert cert["physical_alpha_equal_137"] is False
    assert cert["literal_prediction_verdict"] == "excluded_at_codata_scale"


def test_gap_is_large_relative_to_codata_sigma():
    cert = load_fresh()
    codata = Fraction(*cert["inputs"]["codata_2022_alpha_inverse_fraction"])
    sigma = Fraction(*cert["inputs"]["codata_2022_sigma_fraction"])
    gap_sigma = (codata - Fraction(137, 1)) / sigma
    assert gap_sigma > 1_714_000


def test_committed_certificate_matches_generator_if_present():
    generated = load_fresh()
    if CERT.exists():
        committed = json.loads(CERT.read_text())
        # Source hashes may change when README/docs are edited; core verdicts must not drift.
        for key in [
            "schema",
            "e7_identity_exact",
            "e7_identity_value",
            "physical_alpha_equal_137",
            "literal_prediction_verdict",
            "gap_alpha_inverse_minus_e7_decimal",
        ]:
            assert committed[key] == generated[key]
