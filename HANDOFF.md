# HANDOFF: E7/E6 Heterotic Research

## Read this first

The previous session overstated completion. The charged E8 computation is **NOT COMPUTED**: its directory contains documentation, but no calculation, verifier or certificate. The later invented E7 "NS/Narita-Sato" proof claims are **RETRACTED**. An empty certificate hash and an exit-zero worker summary are not proof evidence.

Use [STORAGE.md](STORAGE.md) for clone/chunk/toolchain recovery and `python scripts/verify_handoff.py` for file-integrity verification. Consult individual saved reports and verifiers for scientific results; this handoff does not certify all historical results. The original remote history is preserved; unpublished commits are consolidated to remove installer-cache bloat.

This project investigates E7/E6 heterotic string compactifications. Existing sources, frozen predecessors and certificates are retained; missing calculations remain open.

## 1. Current Goal

Continue the E7/E6 physical-research investigation using source-backed mathematics, exact certificates and explicitly scoped formal verification. This is not the KaufmanNetwork training project. The current delivery task is a complete, byte-verifiable Git/chunk research handoff; publication does not imply scientific completion.

## 2. Standing Goals

- **E7/E6 Heterotic Research:** Rigorous physical solution for gaps using Lean/auto provers iteratively. Additional criteria: (1) investigate atomic clock connection to hyperphysics.phy-astr.gsu.edu/hbase/acloc.html; (2) Kauffman/HOMFLY, Ramanujan, nimbers, Dirac numbers, Dedekind numbers as missing pieces for partition/prime quantization 133→4.
- **Charged E8 Bracket:** Compute the genuine E8 current-algebra bracket `[[a1,a1]] → a2` for the charged Higgs direction `(3,27)+(3̅,27̅)` under E6⊂E8.
- **Cross-Domain Hypotheses:** Named concepts (Kauffman/HOMFLY, Ramanujan quantities, nimbers, Dirac numbers, Dedekind numbers, partition/prime scales → 4D from 133) with explicitly unproven transfer status.

## 3. Cross-Domain Hypotheses (All Explicitly Unproven)

| User Term | Precise Candidate | Transfer Status |
|-----------|------------------|-----------------|
| Kauffman/HOMFLY (kaufman) | Knot polynomial invariants, charge-refined modular data | knot-modular-threshold-gate exists; **no map to coupling** |
| Ramanujan quantities | Partition congruences `p(5n+4)≡0 mod 5`, tau function, mock theta | Distinct from nimbers; **no action map** |
| Nimbers | Sprague–Grundy/Conway arithmetic | **No canonical map** to Chern classes/indices |
| Dirac numbers | Monopole quantization, large-numbers hypothesis, Dirac operator eigenvalues | Three distinct concepts; internal Dirac index ≡ net chirality only |
| Dedekind numbers | Monotone Boolean function counts | **Not Dedekind η** (modular form); shared name ≠ map |
| Partitions + prime scales → 4D from 133 | `dim E7 = 133`, Cs-133 mass number | **Arithmetic-compactification-selection-gate** rejects prime-order necessity/sufficiency via 4-model catalog |

**No cross-domain arrow has been derived.** The term ledger in `arithmetic-compactification-selection-gate/REPORT.md` classifies each as theorem / model assumption / analogy / numerical coincidence / unsupported.

## 4. Unresolved calculations and release boundary

- **Charged E8 bracket:** not computed. Construct the actual charged cocycles, justified embedding and current-algebra structure constants before evaluating the Maurer–Cartan equation. Check Jacobi, graded Leibniz, representative changes and the obstruction projection. A bracket alone does not produce a solved `a2` or a quartic superpotential.
- **Instanton divisor-charge test:** `cross-domain-instanton-selection-gate/PREREGISTRATION.md` states the finite curve-pairing test. Frozen inputs exist, but no completed calculation or certificate is delivered there.
- **Atomic clocks:** preserve `tian-yau-clock-response-gate/` and its sources. Reconcile the actual canonical-scalar, coupling and frequency-ratio conventions, including the retained Lorini sign issue; no new clock prediction is claimed here.
- **Reference release:** the exact OpenAI release meant by "NS" remains unconfirmed. PrimeGaps186 was an inspected comparison, not confirmation of the user's intended paper. "Narita-Sato" was an unsupported assistant invention, not a derived concept or result.
- **Physical scope:** no completed compactification vacuum, full superpotential, moduli stabilization, electromagnetic-coupling prediction or independent empirical confirmation is asserted.
- **Formal scope:** existing Lean source is preserved. Source presence, installation and successful file transfer are not proof compilation, axiom auditing, hosted CI or peer review.

## 5. Repository Structure

- `gap-investigation/` — All gate investigations
  - `tian-yau-charged-E8-bracket-gate/` — Charged E8 bracket computation
  - `e7-ns-proof-gate/` — retraction notice for unsupported prior claims
  - `cross-domain-instanton-selection-gate/` — Cross-domain instanton selection
  - `arithmetic-compactification-selection-gate/` — Arithmetic compactification selection
  - `adjoint-radial-gauge-pole-gate/` — Adjoint radial gauge pole
  - `adjoint-radial-mixed-pole-gate/` — Adjoint radial mixed pole
  - `adjoint-radial-rxi-lean-gate/` — Adjoint radial RXI lean
  - See `handoff-artifacts/research-manifest.json` for the actual file inventory.

## 6. Git State

- **Branch:** `rigorous-openai-style-release`
- **Remote:** https://github.com/GAIn-Tech/e7-alpha-theory
- **Storage:** Ordinary Git holds large research data and eight checksummed toolchain chunks; LFS upload was rejected by the account budget. Installer caches are omitted, with exact inventory and recovery instructions in `STORAGE.md`.
- **Verification:** compare `git rev-parse HEAD` with `git ls-remote origin refs/heads/rigorous-openai-style-release`; run `python scripts/verify_handoff.py` to assemble the local archive cache and verify all bytes. Do not infer a successful push from this document alone.

## 7. Key Files and Their Status

- `HANDOFF.md` — This file (authoritative session standing)
- `gap-investigation/tian-yau-charged-E8-bracket-gate/RELEASE_DISCLOSURE.md` — Charged E8 release disclosure
- `gap-investigation/tian-yau-charged-E8-bracket-gate/REPORT.md` — Charged E8 gate outcome, boundary, controls
- `gap-investigation/tian-yau-charged-E8-bracket-gate/formalization.yaml` — Scope, axioms, automation, review status
- `gap-investigation/e7-ns-proof-gate/RELEASE_DISCLOSURE.md` — explicit retraction (no computation)
- `gap-investigation/cross-domain-instanton-selection-gate/PREREGISTRATION.md` — Preregistered instanton gate
- `handoff-artifacts/research-manifest.json` — exact retained/recovered research bytes
- `handoff-artifacts/toolchain-manifest.json` — exact selected Lean snapshot contents
