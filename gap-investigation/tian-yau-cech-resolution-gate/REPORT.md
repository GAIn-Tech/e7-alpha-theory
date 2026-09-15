# Tian–Yau Čech resolution gate

## Result

This lane adds the concrete 16-chart standard affine cover `U_i × V_j` and exact rational monomial-sector Čech contractions for each negative-support type on `P3`. The certificate verifies `δ²=0` and `δh+hδ=1-π` in every sector, and serializes every differential, projector, and contracting-homotopy matrix. External products give canonical Laurent normal forms on `P3×P3`.

The Bott/Künneth checks reproduce, among others, `H³(P3×P3,O(2,-4))=10`, its exchanged case, and `H⁰(O)=1`. The twelve Serre-dual mixed-quadratic source labels and their exact `Z3` characters `(4,4,4)` are reconstructed from the actual action. The first End-complex sign is fixed as `(+Eφ,-φJ)`.

## Remaining boundary

The actual `d3` endpoint matrix is **not computed**. The ambient Čech contraction is now explicit, but a chain-level Koszul/Tate comparison embedding the twelve `H²(O_X(-3,0)) ⊕ H²(O_X(0,-3))` classes into the complete-intersection total complex and carrying `E,J` through both vertical solves remains absent. Therefore endpoint representative invariance is not claimed, and no rank or survivor dimension is inferred. This is concrete infrastructure and a narrowed boundary, not closure of the gate.

Lean was not available on PATH; the finite chain identities are instead checked exhaustively over `QQ` by SymPy and stored as sparse exact matrices.

## Replay

```text
C:/Python313/python.exe -B exact_cech.py
C:/Python313/python.exe -B verify.py
```
