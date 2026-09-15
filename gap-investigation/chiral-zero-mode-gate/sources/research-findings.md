# Orbifold parity and anomaly research

## Outcome (derived for the stipulated zero modes)

For left-handed 2 x 27(+1) + 2 x 1(-3), pure E6 cubic anomaly is zero; E6^2 U1 is 2 T(27), U1^3 is zero, and mixed gravitational-U1 is 48. In the convention T(27)=3 the mixed nonabelian coefficient is 6. Arithmetic and phase eigenvalues were checked with Python. Thus the isolated spectrum fails the unbroken gauged E6 x U1 anomaly gate: the obstruction is NOT a pure E6 or U1^3 anomaly.

## Exact primary-source evidence

- Scrucca, Serone, Silvestrini and Zwirner, Anomalies in orbifold field theories, section 4, p.9: "Notice that this mechanism can work only when the integrated anomaly vanishes." This refers to the preceding Chern-Simons inflow construction.[1]
- Their Eq.(10), in covering-circle conventions, is d_M J^M = (1/8)[delta(y)-delta(y-pi R/2)+delta(y-pi R)-delta(y-3pi R/2)] Q(x,y), with Q=g5^2 F Ftilde/(16pi^2) from Eq.(2). This illustrates localized anomalies despite zero integrated anomaly.[1]
- Pilo and Riotto, On Anomalies in Orbifold Theories, Eqs.(3.4),(3.6),(3.8): S_CS = integral u(y) A wedge F wedge F; partial_y u(y) + g5^2 f(y)/(32pi^2)=0; integral_0^(2pi R) f(y) dy=0. Exact following statement: "As a result, there is no periodic u which solves Eq.(3.6) in the cases of fermions with parities (+, +) (-, -) where a chiral zero mode is present in the spectrum, the same result holds for the case of a single Z2." Signs here transcribed from PDF mathematical minus signs.[2]
- Pilo and Riotto Eqs.(2.4),(2.9): Psi(x,y')=epsilon gamma5 Psi(x,y), epsilon=+/-1; phi_R/L(-y)=+/-epsilon phi_R/L(y), phi_R/L(pi R-y)=+/-epsilon' phi_R/L(y). These are opposite parities for opposite four-dimensional fermion chiralities.[2]
- Arkani-Hamed, Cohen and Georgi, Anomalies on Orbifolds, Eq.(4.38): partial_C J^C=(1/2)[delta(x4)+delta(x4-L)] Q. Their endpoint delta functions integrate to 1/2 [Eqs.(4.36),(4.37)], and Q is the Dirac axial anomaly; do not silently interchange this normalization with a unit Weyl anomaly. Exact statement below Eq.(4.38): "Again this is independent of the shape of the chiral zero mode." Their Eq.(5.3) shows the induced bulk contribution proportional to -delta(x4)+delta(x4-L).[3]
- An Exceptional SSM from E6 Orbifold GUTs with intermediate LR symmetry, section 2.2: "5D matter hypermultiplets consist of two oppositely charged chiral superfields"; "In a" Z2 "orbifold, the two receive opposite boundary conditions". Equation (6): Phi^mu -> sigma exp[2pi i V dot mu] Phi^mu and Phi^mu -> sigma' exp[2pi i V' dot mu] Phi^mu. The quoted fragments are verbatim surrounding rendered mathematics. This is a primary E6 orbifold model, not the specific E7 phase-corrected model.[4]
- Goh et al., Dynamics of E6 chiral gauge theories, p.2: "E6 admits complex representations in which all of its representations are anomaly-free by construction." The same page has Eq.(2), S^(ijk)=d_(mu nu lambda) psi_i^mu psi_j^nu psi_k^lambda, explicitly identifying mu,nu,lambda as fundamental representation indices. This illustrates why the cubic invariant on 27 is NOT a cubic gauge-anomaly tensor with adjoint indices.[5]

## Application to the stipulated E7 construction (our derivation, not a paper quotation)

Assume 56=27(+1)+27bar(-1)+1(+3)+1(-3) and the full hypermultiplet H in 56, Hc in its dual, without a half-hyper reality reduction. For g=exp(i pi X/2), g^2=-1 on every listed weight. Taking P=-i g gives P^2=1 and eigenvalues +1,-1,-1,+1 on charges +1,-1,+3,-3. The full-hyper boundary action can be written H(-y)=P H(y), Hc(-y)=-Hc(y)P^{-1}, viewing Hc as a row in the dual. This is the opposite-parity rule underlying the primary constructions.[2][4]

Thus H retains 27(+1)+1(-3). Hc retains the duals of the P-odd H components, also 27(+1)+1(-3). It is incorrect to retain only H or count Hc's surviving fields as left-handed 27bar(-1)+1(+3). A second boundary condition must be compatible to retain these as zero modes; a single fixed-point parity alone does not prove a two-boundary spectrum.

For all-left-handed Weyl fields the reduced coefficients are A_E6^2X=sum q T(R)=2T(27), A_X^3=sum dim(R)q^3=2*27-2*27=0, and A_grav^2X=sum dim(R)q=54-6=48. A_E6 X^2=0 by tracelessness of every E6 generator. The pure E6 cubic anomaly is absent.[5]

The nonzero coefficients produce an integrated zero-mode anomaly. Ordinary compact 5D Chern-Simons inflow redistributes anomalies between fixed points and cannot cancel this nonzero sum, even when local counterterms are permitted.[1][2][3] Additional charged matter or a genuine Green-Schwarz/Stueckelberg sector would be a change of model, not a demonstration that the original spectrum is anomaly-free. The first paper notes that its proposed Green-Schwarz mechanism would spontaneously break the U1.[1]

## Limitations

No primary paper implementing exactly the stated E7 phase-corrected exp(i pi X/2) full-56 construction was located in bounded searches. The E7 branching/phase application is conditional algebra using the task's construction, not claimed as a sourced model. The arithmetic was executed rather than inferred from a paper.

## Sources

[1] https://arxiv.org/pdf/hep-th/0110073
[2] https://arxiv.org/pdf/hep-th/0202144
[3] https://arxiv.org/pdf/hep-th/0103135
[4] https://arxiv.org/html/1001.4074v3
[5] https://par.nsf.gov/servlets/purl/10635146
