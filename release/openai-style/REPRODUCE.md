# Reproduction commands

Run from repository root.

## Numerical certificate

```bash
python release/openai-style/numerical_certificate.py > release/openai-style/certificate-fresh.json
python -m pytest tests/test_release_certificate.py -q
```

Expected result: tests pass and the certificate reports:

- `e7_identity_exact: true`
- `e7_identity_value: "137"`
- `physical_alpha_equal_137: false`
- `literal_prediction_verdict: "excluded_at_codata_scale"`

## Lean certificate

If Lean/Lake is installed:

```bash
lake env lean E7Alpha.lean
```

Current disclosure: this repository's top-level Lean proof uses small arithmetic facts and may depend on local Lean/Lake availability. A stronger future release should vendor a pinned `lakefile.toml` / `lean-toolchain` and avoid `native_decide` for headline statements when possible.

## Theory2 parity path

A fuller verification environment exists in `GAIn-Tech/theory2`, whose formal module set contains Lean files for this E7 audit style:

- `formal/Formal/E7.lean`
- `formal/Formal/Alpha.lean`
- `docs/analysis/E7_ALPHA_ANALYSIS.md`
- `docs/analysis/VERIFICATION_LOG.md`

Use Theory2 as the checker/reference environment for future formal expansion, but do not copy its conclusions into this repository without running the gates locally.
