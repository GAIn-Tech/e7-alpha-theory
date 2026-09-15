# Background Rxi radial pole-difference gate

## Outcome and boundary

The actual 188-real-scalar, 79-vector covariant action now gives a numerical cancellation of the one-loop gauge-dependent radial pole difference, including stationary displacement, at xi=0.1,1,3,100. All seven contributions are computed separately; no cancellation, Nielsen identity, or counterterm is substituted into the sum. This advances the general-gauge gate but is NOT an all-xi symbolic proof, a full physical pole, a width, UV matching, or compactification result.

At s0=4320 epsilon M^2 the differences in units epsilon^2 M^2 are:

|xi|Pi_xi-Pi_0 (real)|stationary tree shift difference|remaining real|remaining imaginary|
|---|---:|---:|---:|---:|
|0.1|-15.3669276606|15.3669276609|2.75e-10|-2.21e-10|
|1|980.171868101|-980.171868101|6.47e-10|-3.50e-10|
|3|4563.454733151|-4563.454733150|4.36e-10|-2.47e-10|
|100|324785.415751765|-324785.415751764|9.99e-10|-3.16e-10|

The imaginary part of Pi difference is the last column because displacement is real. The receipt contains each channel. At xi=1 the ghost is -10.7651546920+5.3048443553i; omitting it leaves +10.7651546927-5.3048443557i. Omitting displacement leaves +980.171868101. These negative controls reject a diagrams-only cancellation and a missing-ghost calculation. No action repair or finite-counterterm fitting was needed.

## Action and gauge fixing (fixed reference background)

Use the predecessor canonical action L=-F^2/4+1/2(D phi)^T(D phi)-epsilon sum_r( phi^T B_r phi/2+c_r)^2, with D phi=partial phi+g A_a R_a phi and real antisymmetric R_a. The script strips g=sqrt(epsilon), M, and the loop-order powers exactly as the predecessors. Define phi=x+eta, K_a=R_a x, L_a=R_a h, h=v_A. The reference x in gauge fixing is held FIXED when differentiating quantum radial insertions. This is background Rxi, not a field-dependent nonlinear gauge that replaces x by x+h in F.

F_a=partial.A_a-xi g K_a.eta; L_gf=-F_a^2/(2xi).
The cross term integrates to -g A_a K_a.partial eta and cancels the kinetic mixing. The scalar inverse mass matrix is H+xi K^T K. Its 67 gauge tangents have masses xi m_a^2, while the 121 physical scalars, including 11 extra soft modes, are retained. No physical quotient is used as the loop spectrum.

For delta eta=g R_b(x+eta) alpha_b and delta A_a=-partial alpha_a+nonabelian terms, variation of F gives the FP operator with mass xi g^2 K_a.R_b x and scalar vertex N_ab(h)=xi g^2 K_a.R_b h. The sign convention is chosen so the free ghost denominator is k^2-xi m_a^2+i0; the Grassmann loop contributes minus twice a real-scalar determinant. Thus N=xi Z, Z=K L^T in the vector mass basis, and the ghost bubble is -2 sum_ab N_ab N_ba I(xi a,xi b)/(32pi^2). It is NOT generally N_ab squared. The FP operator is linear in eta: no hh-ghost seagull exists in this fixed-reference gauge. Ghost-vector interactions exist but do not enter this one-loop two-external-scalar topology.

The hVV and hhVV vertices remain D=L K^T+K L^T and Q=2L L^T; scalar T=d_h H and U=d_h^2 H come from the actual B tensors. Scalar-vector coupling is C_ai=E_i^T R_a h. Gauge fixing adds masses but no new radial cubic/quartic at fixed x.

## Independent tensor reduction and MSbar conventions

I(a,b;s)=int_0^1 log[ta+(1-t)b-s t(1-t)-i0]dt and A(a)=a(log a-1), Q^2=epsilon M^2. The inverse propagator is s-m_tree^2-Pi. All tensor reduction retains dimensional regularization; the VV +2 evanescent finite term is inherited and cancels in its xi difference. SV's gauge-independent evanescent constant cancels in its difference because sum C^2 is basis invariant. This code is a DIFFERENCE calculator; its unsubtracted absolute SV kernel must not replace the predecessor absolute finite SV coefficient.

Writing u=k^2, v=(k-p)^2, the vector propagator tensor without its common -i is
 g/(u-a)-k k/a [1/(u-a)-1/(u-xi a)].
Contracting k yields xi k/(u-xi a), checked exactly in symbolic_checks.py. The VV numerator uses (k.l)^2=(u+v-s)^2/4; the mixed vertex has w=2p-k, w^2=2s+2v-u and (w.k)^2=(s-v)^2. The code reduces these independently rather than using an expected zero.

The six finite moments for denominator (u-a)(v-b) are:
 J(1)=I; J(u)=A(b)+aI; J(v)=A(a)+bI;
 J(u^2)=(b+s+a)A(b)+a^2 I;
 J(v^2)=(a+s+b)A(a)+b^2 I;
 J(uv)=aA(a)+bA(b)+abI.
Scaleless integrals vanish. The resulting VV uses its ordered-state factor 1/(32pi^2), SV uses -2 C^2/(32pi^2), scalar T bubbles use 1/(32pi^2), and ghost bubbles use the Grassmann -2. These signs reproduce cancellation without changing any predecessor.

Vector longitudinal seagull is xi sum_a Q_aa A(xi a)/(32pi^2). Scalar seagull difference is Tr[U W]/(32pi^2), where W=A(H+xi K^T K)-A(H). Longitudinal-vector and ghost tadpoles cancel each other: xi Tr[D_j A]/32 minus 2xi Tr[Z_j A]/32=0 since D_j=Z_j+Z_j^T and A is diagonal. The remaining tadpole difference is Tr[T_j W]/(32pi^2). Solve H delta=-delta tad in the actual invariant physical-singlet space, not merely along h. The radial displacement term is (dH[delta])_hh. Its stationary-equation residual is below 1.5e-10.

## Ward/BRST checks and proof layers

The potential identity H R_a x=R_a grad V differentiates at the stationary background to T_h K_a+H L_a=s0 L_a. The actual full matrices satisfy this with norm 8.18e-12. In eigencomponents this is T_iG_a sqrt(a)=(s0-X_i) C_ai. D=Z+Z^T and H K^T=0 are independently asserted. These are tree Ward and FP/longitudinal checks implied by the BRST gauge fixing, NOT a computed full quantum Slavnov-Taylor functional or a Lean proof of BRST invariance.

symbolic_checks.py checks exact rational propagator, contracted Ward-polynomial, FP tadpole, and numerator identities with SymPy; their physical action premises remain numerical/derived on paper. No Lean kernel theorem, interval enclosure, hosted CI, or independent expert review is claimed.

Master integrals use the predecessor analytic root primitive with the exact signed negative-Delta interval cut. Four independent 60-digit adaptive tanh-sinh checks cover massless, open, and closed thresholds; maximum discrepancy 1.25e-60. xi=100 changes which unphysical cuts are open. It does not use log(abs mass squared), drop imaginary parts, floor denominators, or fit a regulator. Actual action tensors remain double precision; scalar masses are grouped by 8-decimal shell rounding. The ~1e-9 cancellation residual therefore is numerical evidence, not 60-digit action accuracy. Not every weighted master was independently adaptively checked in this lane; the convergence predecessor remains a separate stronger master audit.

## Power counting and isolated pole

With fixed dimensionless xi, g^2~lambda~epsilon, m^2~epsilon M^2, trilinears~epsilon M, each one-loop diagonal and tadpole shift is epsilon^2 M^2 times its displayed coefficient. Pi'(s0)~epsilon times a coefficient, so delta s Pi' is next order. Off-diagonal self-energies ~epsilon^2 M^2 enter an isolated eigenvalue via their square divided by a tree gap ~epsilon M^2: epsilon^3 M^2, not the present epsilon^2 order. The physical tree gap from the radial shell is 4283.5 epsilon M^2. At sampled gauges the closest unphysical pole gaps are 4316.35,4283.5,4210.5,670 in those units.

Require epsilon times loop coefficients small relative to tree eigenvalue/gaps; require epsilon ||delta||/||x|| small; require |Pi'|<<1 and no threshold or xi m_a^2 tuned within the loop displacement of s0. xi growing as 1/epsilon, unphysical pole degeneracy, a threshold collision, or a nearly degenerate physical mode invalidates this simple counting and requires the appropriate mixed/resummed determinant. xi=100 is a fixed-xi algebraic stress test, not proof perturbation theory is reliable at any chosen epsilon. No numerical bound on the omitted higher-order remainder has been established.

## Reproduction

Native NumPy Python, -B:
`C:/Users/mikeb/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/adjoint-radial-rxi-pole-gate/calculation.py`

SymPy Python:
`C:/Python313/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/adjoint-radial-rxi-pole-gate/symbolic_checks.py`

Saved receipts are mandatory and compared exactly. --create uses exclusive creation only. Initial calculation and receipt remain as provenance. All work is additive in this directory. Input hashes bind the radial predecessor action/calculations/disclosures and convergence source 60510b3b00dbd70bc2aa3217cf90b6f2c9f10b7c5fe8527c1f9078a6ed9cc006. Legacy README overclaims are not adopted. Missing gates: analytic all-xi sum proof, full quantum identities, higher-order mixing/tadpoles, finite EFT matching, and physical interpretation of any absolute pole.
