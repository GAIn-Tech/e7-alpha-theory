# Adjoint-radial finite transverse vector bubble gate

## Result and boundary

From `L = -F^2/4 + A_mu^a M^2_ab(phi) A^{b mu}/2`, expansion along the normalized adjoint radial coordinate gives

`D_A = d_A M^2 = (Rv_A)(Rx)^T + (Rx)(Rv_A)^T`,
`Q_AA = d_A^2 M^2 = 2(Rv_A)(Rv_A)^T`.

Thus the Feynman rules are `i D_A,ab g_mu_nu` and `i Q_AA,ab g_mu_nu`. The two-trilinear bubble carries symmetry factor `1/2`. In strict Landau gauge each unequal-mass vector propagator is proportional to

`P_mu_nu(k)/(k^2-m_a^2+i0)`,  `P_mu_nu=g_mu_nu-k_mu k_nu/k^2`,

and `P(k):P(k+p)=d-2+[k.(k+p)]^2/[k^2(k+p)^2]` in `d=4-2 eps`.

At `p^2=4320 epsilon M^2`, `Q^2=epsilon M^2`, the finite MSbar transverse result, in units of `epsilon^2 M^2`, is

- vector-vector bubble: **`76.7356082103 - 31.9290185806 i`**;
- momentum-independent vector seagull: **`15.0356670883`**;
- their sum: **`91.7712752985 - 31.9290185806 i`**.

This is the actual finite transverse VV subset, not a zero-momentum determinant substitution. Mixed scalar-vector derivative bubbles, external scalar/vector mixing, and general-xi longitudinal/Goldstone/ghost cancellation remain open. No full-pole, physical-width, or gauge-independent claim is made.

## Scalar-integral reduction and subtraction

Write `I_ab(s)=int_0^1 dx log[x a+(1-x)b-s x(1-x)-i0]` and `A(a)=a(log a-1)`. Partial fractions reduce the longitudinal-projector numerator to

`X=[A(b)+a I_ab-a I_a0]/b`, `Y=[A(a)+b I_ab-b I_0b]/a`,
`U=(I_ab-I_0b)/a`, `V=(I_ab-I_a0)/b`,
`W=(I_ab-I_0b-I_a0+I_00)/(ab)`.

The locally MSbar-subtracted kernel is

`K_ab(s)=2 I_ab + [X+Y+2 I_ab-2s(U+V)+s^2 W]/4 + 2`.

The last `+2` is essential: it is the finite evanescent contribution from the `-2 eps` in the d-dimensional projector multiplying the UV pole. The bubble is `sum_ab D_ab^2 K_ab/(32 pi^2)`; the denominator includes the `1/2` diagram symmetry factor while the sum is over ordered eigenstates. The removed local UV coefficient is `3 Tr(D_A^2)/(64 pi^2)=5.12938492189`.

The seagull is separate and momentum independent: `3 sum_a Q_AA,aa m_a^2(2 log m_a^2-2/3)/(64 pi^2)`. It is not folded into the finite bubble.

## Enumeration and controls

All 79 vectors are instantiated: 67 massive and 12 massless. Ten mass shells are recorded in `receipt.json`; all 62 ordered nonzero-D channels are above threshold at the requested shell. The radial D rows/columns touching the unbroken massless block have norm `1.19e-30`, so massless propagator limits never enter an active bubble term.

- `p -> 0`: direct kernel gives `39.9662886317`, exactly matching the vector Coleman-Weinberg Hessian **bubble component**. Adding the separate seagull reproduces the prior total vector CW Hessian `55.0019557199`.
- Random rotations within every degenerate vector shell change the finite result by `1.5e-14`.
- An independently coded threshold-split 512-point integration agrees within the disclosed cancellation-limited numerical bound in `verification.json`.
- Strict-Landau ghost boundary: background-Rxi radial ghost vertices are proportional to xi and vanish at `xi -> 0`; this is not a general-xi cancellation proof.

## Sources and provenance

The source hashes in `receipt.json` bind this calculation to the prior gauge gate, scalar/fermion pole source, Goldstone pole source notes, and canonical shifted-vacuum generator implementation. Conventions are consistent with the retained S. P. Martin, hep-ph/0111209, and M. Goodsell, S. Paßehr et al., arXiv:1910.02094 references; the finite tensor contraction above is independently derived from the displayed canonical action rather than copied from the zero-momentum determinant.

