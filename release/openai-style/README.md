# E7 alpha audit — OpenAI-style release package

This package mirrors the rigorous parts of OpenAI's recent math-release style without erasing the original research record:

- plain-language result page,
- machine-checkable artifacts,
- explicit disclosure of what is proved vs conjectured,
- reproducible numerical certificates,
- independent-tool parity via the Theory2 conventions,
- fail-closed CI checks.

## Result status

**Physical derivation of the fine-structure constant from E7: not proved.**

What is proved is narrower:

1. the arithmetic identity `133 + 56/(2*7) = 137` is exact;
2. the identity is an E7 invariant-table coincidence under a chosen formula family;
3. current experimental `alpha^-1` is not exactly `137`;
4. the gap from the CODATA-scale value is about `0.035999177`, so integer equality is excluded as a literal physical prediction;
5. later experiments in this repository remain exploratory unless promoted by this release contract.

## OpenAI-style mapping

OpenAI's public style elements used as precedent:

- result announcement plus manuscript-style explanation;
- formal Lean certificates where available;
- transparent authorship/process disclosure;
- released artifacts that readers can run, not trust;
- explicit community-review invitation and limitations.

We adopt the verification structure, not the substance or branding.

## Artifacts

- `DISCLOSURE.md` — authorship, AI/tooling, limitations, non-claims.
- `REPRODUCE.md` — exact local commands and expected gates.
- `formalization.yaml` — machine-readable proof/reproduction manifest.
- `numerical_certificate.py` — exact arithmetic + decimal certificate generator.
- `certificate-fresh.json` — generated certificate from this run.
- `tests/test_release_certificate.py` — fail-closed certificate tests.

## Trust boundary

This release does **not** ask readers to trust an LLM or a narrative. It asks them to run:

```bash
python release/openai-style/numerical_certificate.py > release/openai-style/certificate-fresh.json
python -m pytest tests/test_release_certificate.py -q
```

If a Lean toolchain is installed, readers should additionally check the existing Lean proof file:

```bash
lake env lean E7Alpha.lean
```

The current repository-level Lean setup is lightweight and may require installing Lean/Lake locally; absence of that toolchain is disclosed, not hidden.
