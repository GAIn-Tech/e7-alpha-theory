# Survivor Yoneda gate: the four proposed inputs do not exist as Ext1 classes

## Correction requiring parent integration

**Reject the predecessor's invariant-neutral count 16 and its proposed four-source Yoneda problem.** With the supplied monad A in degree -1, B in degree 0, C in degree 1, End degree is target minus source. Thus H2(Hom(C,A)) is bidegree (-2,2), total degree 0. Its d3 target (1,0) has total degree 1. A d3 kernel could only contribute to Ext0, not be added to the Ext1 target. Simultaneously shifting the tangent monad cancels inside End; shifting End itself would also shift the polynomial deformation classes out of Ext1. There is no convention rescue preserving both identifications.

The new computation is stronger than this degree objection: **E2^(-2,2)=0 in all three characters.** Therefore the predecessor's twelve purported E3 sources, including the four invariant labels, do not survive the full first End differential. They cannot be supplied as neutral-modulus cocycles to a charged Yoneda calculation.

## Actual exact matrices, not an assigned endpoint

`exact_audit.py` calculates all line-bundle cohomologies occurring in End(K) using QQ Laurent-monomial Koszul matrices on P3 x P3. Ambient rows are 0,3,6 and Koszul length is three; a higher row-jumping differential would require r=4 and cannot fit. The saved certificate lists every End E1 entry and every Ext1-diagonal summand.

`q1_differential.py` constructs actual monomial Koszul representatives and computes both End d1 arrows on H1, including the minus sign in D(phi)=d phi-(-1)^p phi d. It verifies their product is zero and source-boundary changes project to zero. Its saved full sparse matrices give:

| Character | H1 End^0 -> H1 End^1 -> H1 End^2 dimensions | d1 ranks | E2 row |
|---|---|---|---|
| 0 | 4 -> 80 -> 16 | 4,16 | 0,60,0 |
| 1 | 4 -> 72 -> 12 | 4,12 | 0,56,0 |
| 2 | 4 -> 72 -> 12 | 4,12 | 0,56,0 |

`verification.json` retains exact right inverses of the last maps. Their products are identity. Equivariant Serre duality (the residue phase is zero) identifies H2 End with the opposite-character, reversed H1 row. The surjective last H1 arrow therefore proves the first H2 arrow is injective: E2^(-2,2)=0. This is not a generic-rank argument.

## Correct Ext1 diagonal and outstanding work

Replaying the polynomial constraint and gauge matrices, and using the new H1 row and Serre duality, gives the complete E2 diagonal for Ext1:

| Bidegree | Character 0 | Character 1 | Character 2 |
|---|---:|---:|---:|
| (1,0) | 12 | 14 | 14 |
| (0,1) | 0 | 0 | 0 |
| (-1,2) | 60 | 56 | 56 |
| (-2,3) | 4 | 2 | 2 |

The four invariant E2^(-2,3) classes are **not** the predecessor's four E3^(-2,2) labels. They are dual to the polynomial H0 End^2 cokernel. Their identity and higher-page fate must be established independently.

Only the polynomial (1,0) slot is now known to equal its E-infinity value: all possible incoming sources vanish and it has no outgoing arrows. The unresolved differentials are d2: (-1,2)->(1,1), d3: (-2,3)->(1,1), d3: (-1,2)->(2,0), and d4: (-2,3)->(2,0), interpreted on their proper pages. Consequently

    dim Ext1_0 = 12 + dim E_inf^(-1,2)_0 + dim E_inf^(-2,3)_0,
    12 <= dim Ext1_0 <= 76.

This is a filtration statement, not a claim that E2 already equals E-infinity. Vector-space extensions cannot move total degrees or change the sum of associated-graded dimensions. The full neutral count remains unknown.

## Yoneda and Higgs boundary

The requested action has total degrees 1+1=2. A hypothetical total-degree-zero source instead acts into H1, not H2. Since the proposed four inputs already fail class identification, no charged cocycles, two geometric primitives, H2 projection, tensor components, or new e32/e33 neutral F contractions are asserted. The tensor fields are explicitly null, not invented zero arrays. The predecessor's terminal-C argument continues to give the zero tensor on the now-established polynomial image only. No full-moduli, neutral F-flatness, unobstructed deformation, exotic mass-rank, or stabilized-vacuum claim follows.

A future chain-level calculation must start with representatives of the actual (-1,2) and (-2,3) sectors after their higher-page tests, and use the Leibniz rule for the total differential. For a closed degree-one a and charged c, replacing c by c+D b changes a c by -D(a b); replacing a by a+D eta changes a c by D(eta c). These identities do not supply missing geometric lifts.

## Predecessor evidence audit

The predecessor completion replay does exit successfully and prints zero blocks of shapes 12x4,14x4,14x4 and count 16. Inspection of `exact_d3.py` shows `endpoint=s.zeros(target_dim,4)` is assigned directly; the two primitive fields are prose strings, not executable total-complex solutions. Its projector tests and byte replay do not establish a geometric d3 or representative independence. Keep its historical artifacts unchanged, but do not promote that receipt to a computed higher differential. The older boundary script already explicitly asserted source total degree zero.

## Replay and controls

From this canonical directory:

    C:/Python313/python.exe -B exact_audit.py
    C:/Python313/python.exe -B q1_differential.py
    C:/Python313/python.exe -B verify.py

Default commands compare complete saved deterministic payloads before claiming success; creation is exclusive. Controls cover wrong total degree, incompatible shifts, wrong End sign, d1 squared zero, Koszul-boundary representative changes, exact right inverses, rank-destroying row mutations, missing artifacts and tampered payloads. The geometric Yoneda representative control remains unexecuted because there is no constructed new Yoneda map. Local SymPy exact arithmetic only; no Lean-kernel or hosted-CI claim. Initial receipts are retained as `.initial` provenance, not current replay targets.

All new artifacts belong exclusively to `gap-investigation/tian-yau-survivor-yoneda-gate`. A shadow-file delivery issue was repaired by copying verified source text in bounded native-Python chunks into the canonical tree. A SymPy empty-RHS solve corner case was handled by explicitly skipping the vacuous zero-boundary-column solve; no nonempty solve or mathematical condition was skipped.

