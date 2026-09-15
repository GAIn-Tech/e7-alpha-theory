# Tian–Yau Koszul–Čech `d3` completion gate

## Exact result

For the fixed Fermat/bilinear Tian–Yau member and stated Euler/Jacobian monad, the three character blocks are explicit rational zero matrices:

- character 0: `QQ^4 -> QQ^12`, rank 0;
- character 1: `QQ^4 -> QQ^14`, rank 0;
- character 2: `QQ^4 -> QQ^14`, rank 0.

The certificate records every dense matrix, sparse endpoint, source ordering, Laurent-support trace, Koszul signs, `D_total^2=0`, representative-change invariance, and sign-convention similarity. Character preservation is derived directly; no conjugation relation between the nontrivial blocks is claimed.

All 12 incoming classes survive. Together with the prior 12 polynomial monad-map classes this gives 24 upstairs represented classes and 16 invariant descended neutral classes (12 prior invariant polynomial classes plus 4 character-zero incoming survivors).

## Charged action boundary

The prior `12 x 9 x 6` invariant neutral–`L`–`Lbar` tensor remains exactly zero. The four new invariant survivor actions are **not** determined by their zero `d3` endpoint. The missing map is

`QQ^4 x H1(TX)_0 (QQ^9) -> H2(TX)_0 (QQ^6)`.

The smallest missing data are chain-level Yoneda compositions of the four invariant `H2(Hom(C,A))` cocycles with the nine invariant charged cocycles, two total-complex primitives, and projection onto six invariant `H2(TX)` representatives. Consequently the e32/e33 witness has zero contractions for the prior 12 neutral classes, while its four new neutral F-contractions remain unresolved. No arbitrary tensor or generic rank is inserted.

## Replay

`C:/Python313/python.exe -B exact_d3.py`

`C:/Python313/python.exe -B verify.py`
