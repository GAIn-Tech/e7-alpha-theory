# Adjoint radial pole gate: complete scalar/fermion subset

## Result and boundary

For the isolated canonical adjoint radial mode `v_A=A0/sqrt(B(A0,A0))`, the tree shell is `p^2=4320 epsilon M^2`. In the declared shifted-vacuum EFT, MSbar at `Q^2=epsilon M^2` and Landau gauge, the complete **scalar plus fermion subset** of the one-loop pole coefficient is

`delta m_A^2/(epsilon^2 M^2) = 512000.31095 - 238193.18642 i`

at the regulator limit. This is not the full pole and is not gauge independent. Pure-vector, vector seagull, ghost, mixed scalar-vector bubbles, and scalar/vector external mixing in the pole determinant remain.

## Couplings derived from the action

The action is not augmented. With `V=epsilon sum_r f_r^2`, `f_r=x^T B_r x/2+c_r`, and canonical mass Hessian `H`, direct differentiation gives

`T_A = d_A H = 2[(Bv_A)^T J + J^T(Bv_A) + sum_r(Jv_A)_r B_r]`,

`U_AA = d_A^2 H = 4(Bv_A)^T(Bv_A)+2 sum_r(v_A^T B_r v_A)B_r`.

In a tree mass eigenbasis these are the actual vertices `lambda_Aij=epsilon M (E^T T_A E)_ij` and `lambda_AAij=epsilon (E^T U_AA E)_ij`. There are 12,325 trilinear matrix entries and 183 diagonal quartics above `1e-10`; `sum_ij lambda_hat_Aij^2=26750168.000000015` and `sum_i lambda_hat_AAii mhat_i^2=935976.0000000022`. Counts depend on the displayed eigenbasis inside degenerate spaces, while all contractions and the answer do not.

The declared Yukawa blocks are 27 Dirac fields with `y/sqrt(epsilon)=1` and three singlet Dirac blocks with ratios 1, 2, 3. Their masses depend only on `u=|Phi|^2/2`; since `d_A Phi=0`, every direct `v_A psi psi` and `v_A v_A psi psi` vertex vanishes. The direct fermion 1PI self-energy is therefore exactly zero. Its tadpole-induced stationary displacement contributes only `3.70e-32`, numerical zero.

## Renormalized expression and tadpoles

For `m_i^2=epsilon M^2 mhat_i^2`, define the finite MSbar function

`I_ij(shat)=int_0^1 dx log[x mhat_i^2+(1-x)mhat_j^2-shat x(1-x)-i0]`.

With inverse propagator `s-m_tree^2-Pi(s)`, the scalar result used is

`delta m_A,S^2/(epsilon^2 M^2) = v_A^T dH[delta_S] v_A`
` + (1/32pi^2) sum_i Uhat_AAii mhat_i^2(log mhat_i^2-1)`
` + (1/32pi^2) sum_ij That_Aij^2 I_ij(4320)`.

This is the quartic tadpole plus every scalar bubble, plus the scalar-sector stationary-vacuum shift. It is algebraically `H_CW,S(0)+Pi_S(s)-Pi_S(0)`, but evaluated in the displayed direct form so the zero-momentum bubble is not counted twice. Sector tadpoles are solved linearly in the same invariant physical singlet space as `shifted-vacuum-gate`. The scalar shift term is `-65350.0192170`; quartic tadpoles are `21783.2959900`; bubbles are `555567.034177-238193.186425 i`.

The local dimensional-regulator coefficient removed by MSbar is `87662.2775179`. A different finite radial mass counterterm shifts the reported real coefficient additively; declared MSbar sets it to zero. The Passarino-Veltman convention and branch follow Elias-Miro, Espinosa and Konstandin, arXiv:1406.2652, Appendix A eqs. (A.4)-(A.5), as already retained and hashed by `goldstone-pole-matching-gate/SOURCE_NOTES.md`. The general divided-difference/Coleman-Weinberg implementation follows the retained source S. P. Martin, hep-ph/0111209, used by the predecessor gates.

## Checks

Goldstone regulator scans from `eta=1e-4` to `1e-60` stabilize to the finite value; the last two values agree exactly at stored precision. A random orthogonal rotation in every degenerate mass eigenspace changes the real result by `1.16e-10`. Threshold-split 256/512-point quadratures differ by `1.09` in an answer of magnitude `5.6e5` (about `2e-6`); this bounds displayed practical precision to roughly six significant figures despite additional printed receipt digits. Negative controls show that omitting the stationary shift changes the real coefficient by `65350.0`, and dropping quartics by `21783.3`.

The imaginary part is the scalar-subset cut structure and must not be interpreted as a physical width before the omitted gauge-sector diagrams and full pole determinant are included.
