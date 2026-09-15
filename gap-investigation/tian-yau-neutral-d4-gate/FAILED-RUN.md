# Failed-run forensic record

Process `proc_34c5ee2e337f`, PID 10872, native `verify.py --create`, exited 1 after 657 seconds. Its source was loaded before subsequent edits. The tool returned this traceback, whose displayed file text was read from the later on-disk version:

```text
derive source 0
derive source 1
derive source 2
derive source 3
Traceback (most recent call last):
  File "C:\Users\mikeb\e7-alpha-theory\gap-investigation\tian-yau-neutral-d4-gate\verify.py", line 122, in <module>
    assert M.rank()==0 and len(kernel)==4
                           ^^^^^^
  File "C:\Users\mikeb\e7-alpha-theory\gap-investigation\tian-yau-neutral-d4-gate\verify.py", line 105, in main
    for i in range(len(c.terms)):
        ^^^^^^^^^^^
  File "C:\Users\mikeb\e7-alpha-theory\gap-investigation\tian-yau-neutral-d4-gate\verify.py", line 91, in calculate
    # Full survivors are data for later Yoneda, not an assigned tensor.
AssertionError
```

A separate direct `verify.calculate()` execution of the original code, before those edits, exited 1 with line 91 correctly rendered as:

```python
assert counts['source_boundary']>0 and counts['target_d1_boundary']>0
```

Thus the failure was a missing nontrivial source-boundary test, not an observed nonzero d4 or failed rank check. The harmonic-normalized source support contracts to zero; it is unsuitable for generating such a test. The repair creates an admissible same-character Laurent perturbation outside that support, contracts it, explicitly requires its vertical boundary to be nonzero, then checks the full total-boundary extension. The mathematical rank assertion was not removed or weakened to obtain success. The independently computed endpoint cochains were already zero in `computed-chains.json` before this verifier existed.

`failed-run-source-reconstructed.py` is a reconstruction by reversing recorded patches, not a falsely claimed contemporaneous process dump. It is 8170 bytes and has SHA-256 `f2fa446e6107603bae85b4b1aec2bdaf4ad85431ad1147d188767363d6322f80`. `verify-pre-release-snapshot.py` freezes the subsequent passing-calculation source at 9493 bytes, SHA-256 `4e5d5a5aa270c75c75ddbe952cd736676e90d6d623813dacb7d2def69bf103d3`. No release receipt existed at the time of the failure or snapshot; no existing receipt was overwritten.

A later fresh native calculation exited zero and reported four source-boundary changes, six vertical target-boundary changes, 64 target d1-boundary generators, four wrong-curvature detections, ten wrong-primitive-sign detections, four wrong-End-sign detections, and 6470 keywise nilpotence/contraction checks. Immutable release replay remains a separate gate.

## Reusable lessons for the parent skill maintainer

- Freeze source before starting a long verifier; Python can render traceback line text from a newer on-disk file than the running bytecode. Preserve both versions before interpreting a mathematical failure.
- A contracting homotopy vanishes on normalized harmonic representatives. Generate nontrivial exact-representative tests outside the harmonic support, preserving line degree and character, and assert the perturbation is nonzero.
- A consistently changed supercommutator sign can retain square-zero identities. Test a sign mutation against the fixed chain lift/product convention, not only nilpotence.
- On this host filesystem tools wrote into `C:/cygwin64/c/Users/...` despite reporting a canonical Windows path. Native Python located the actual source; explicit native copy repaired delivery. Do not infer delivery from reported resolved paths.
- The finite Čech-to-Koszul perturbation series supplies reusable executable vertical primitives. Check every returned primitive against the original differential, not only its transferred cohomology coordinates.

No global skill file was modified because this worker owns only the d4 lane.
