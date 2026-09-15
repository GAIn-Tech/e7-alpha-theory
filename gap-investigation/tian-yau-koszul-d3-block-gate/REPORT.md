# Tian–Yau Koszul–Čech `d3` character-block gate

## Result

For the exact Fermat/bilinear complete intersection and Euler/Jacobian tangent monad, the character-zero block

`d3 : QQ^4 -> QQ^12`

is the zero matrix (rank `0`). The ordered source is `Cx_to_Ay_01, Cx_to_Ay_23, Cy_to_Ax_01, Cy_to_Ax_23`. No conclusion is drawn for characters 1 or 2.

`exact_d3.py` records the three Koszul wedge differentials with signs, the signed first End differential `(+Ephi,-phiJ)`, both monomial Čech/HPL solve traces, the deterministic 12-dimensional target quotient, and the sparse/dense endpoint matrix. It checks Koszul syzygies, `J E=0` modulo the actual ideal, total-square zero, representative invariance, and convention-sign similarity. A negative control shows that deleting the Jacobian square factors leaves a top Čech projector and therefore changes the computation.

## Replay

```text
C:/Python313/python.exe -B exact_d3.py
C:/Python313/python.exe -B verify.py
```

The result is an exact calculation for this member and convention, not an equivariance argument for the other two blocks and not a claim that polynomial monad deformations exhaust `H1(End TX)`.
