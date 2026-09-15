# Adjoint-radial gauge pole gate — bounded zero-momentum result

## Outcome

From the action's canonical scalar kinetic term and its actual 79 real antisymmetric generators, the vector mass matrix and adjoint-radial derivatives are

`M_V^2=(R x)(R x)^T`,  `D_A=(R v_A)(R x)^T+(R x)(R v_A)^T`,  `Q_AA=2(R v_A)(R v_A)^T`.

The spectrum has 67 massive and 12 massless unbroken vectors. The unbroken blocks of both radial derivatives vanish (`||D_00||=1.19e-30`, `||Q_00||=1.49e-31`), so no artificial IR mass or logarithm is assigned to them.

In strict Landau gauge and MSbar at `Q^2=epsilon M^2`, the **zero-momentum transverse-vector determinant Hessian** is `55.00195572 epsilon^2 M^2`. The vector tadpole displacement, solved in the predecessor's invariant physical-singlet space, adds `-45.10700126 epsilon^2 M^2`, giving the bounded zero-momentum sum `9.894954455 epsilon^2 M^2`. This is a CW-Hessian crosscheck, **not the requested finite-momentum pole contribution**.

The strict-Landau background-Rxi Faddeev–Popov scalar vertex is proportional to xi and vanishes at xi=0. This statement does not replace a general-xi cancellation calculation.

## Checks

- All 79 vector eigenstates are retained. `Tr D_A^2=1080.000000000001`; `Tr(Q_AA M_V^2)=548.0000000000005`.
- Analytic spectral divided differences reproduce direct second finite differences: `55.00195357` at step `5e-5` versus `55.00195572` analytically.
- Random orthogonal rotations in every degenerate vector eigenspace change the result by zero at stored precision.
- The removed local MSbar UV coefficient in the declared transverse determinant convention is `7.7320728267`.
- Negative controls: omitting the stationary shift changes the answer by `45.10700126`; dropping the seagull part changes it by `15.03566709`.

## Unclosed pole work

The finite `p^2=4320 epsilon M^2` transverse vector-vector bubble was **not completed**. Scalar-vector derivative bubbles, external scalar/vector mixing, and general-xi longitudinal/Goldstone/ghost cancellation also remain. Therefore this lane does not combine its number with the predecessor scalar/fermion pole coefficient and makes no physical or gauge-independent pole claim.

The retained primary source is M. Goodsell, S. Paßehr et al., *All two-loop scalar self-energies and tadpoles in general renormalisable field theories*, arXiv:1910.02094, whose notation explicitly includes `SVV`, `SSVV`, and general-Rxi ghost vertices. The implementation here uses only the zero-momentum one-loop determinant consequence that was independently checked against the canonical mass matrix; it does not claim that paper's finite-momentum formulas were fully instantiated.

