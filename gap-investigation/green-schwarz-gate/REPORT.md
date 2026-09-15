# Boundary Green–Schwarz/Stückelberg gate

## Outcome

**There is an exact conditional local perturbative repair of the I/P model:** add one shifting axion on its breaking wall. Its two anomaly-determined Wess–Zumino couplings cancel both mixed anomalies, no cubic-X coupling is needed, X loses its massless gauge boson, and n chiral E6 27s remain without mirror 27s. This is new boundary action data, not a consequence of E7 alone and not a physical alpha solution.

The construction below is explicitly the **non-SUSY 5D bulk-Dirac-56 variant**. It does not supply an axion supermultiplet, supersymmetric boundary action, FI analysis or supersymmetric vacuum. Calling the same bosonic terms a completed full-hypermultiplet model would be unsupported.

## 1. Conventions and complete perturbative polynomial

Take all fermions left-handed, n positive copies of S=27(+1)+1(-3), and an oriented spin four-dimensional wall. Negative n in the exact tests denotes virtual conjugate chirality, not negative particle multiplicities. A is the real connection multiplying primitive integer X charges in D=d-iqA; delta A=d lambda, lambda has period 2pi. For the anti-Hermitian E6 curvature F6 set f6=iF6/(2pi), and x=dA/(2pi). Products of forms mean wedge products. tr27 is the literal 27-dimensional matrix trace. For the real tangent connection curvature R, p1(TM)=-tr_vector(R wedge R)/(8pi²). Define the chirality sign by I6=[Ahat(TM) ch(E)]6 with Ahat=1-p1/24+...; reversing chirality/orientation changes every anomaly and WZ sign together.

For a Weyl representation R of dimension d and charge q,

I6(R,q) = (1/6)tr_R f6³ + (q/2)x tr_R f6²
           + (q²/2)x² tr_R f6 + (d q³/6)x³
           - (p1/24)(tr_R f6+d q x).

E6 has no invariant degree-three adjoint polynomial, so tr_R f6³=0; its generators are traceless. The 27 matter cubic invariant does not contradict that statement. Therefore the FULL perturbative four-dimensional polynomial of nS is

I6 = n x Q4,                 Q4 = (1/2)tr27 f6² - p1.

The cubic sum is 27*1³+1*(-3)³=0. The linear sum is 27-3=24. Thus A(E6²X)=n T27, A(gravity²X)=24n, A(X³)=0, and E6 X² and E6³ vanish. There is no pure gravitational six-form for four-dimensional Weyl fermions. These are consistent-anomaly data, not a covariant-current formula imported with a different factor of three.

Exact predecessor weights give tr27(H_i H_j)=6 A_E6,ij. With long-root length squared two, define the basic E6 class u=tr27 f6²/12; on liftable simply connected E6 bundles u has integral periods (orientation can reverse the instanton sign). Thus Q4=6u-p1. This uses integral index 6, not the physics index T27=3: Bphys=2B0. The independent primary normalization table gives lambda_E6=6 [3].

## 2. Descent and Bardeen convention—preserve E6 and gravity

Set a=A/(2pi). Choose the consistent descent

I5^(0)=n a Q4;     delta I5^(0)=d I4^(1);
I4^(1)=n (lambda/(2pi)) Q4.

Fix the determinant phase convention delta log Z_fermion=2pi i integral I4^(1)=i n integral lambda Q4. This scheme preserves E6 gauge and local Lorentz/diffeomorphism Ward identities; all mixed anomaly is assigned to X. It is legitimate locally, not an assertion that the mixed anomaly has disappeared.

For an explicit change-of-scheme formula let q3=(1/2)CS3(f6)-CS3(p1), normalized by dq3=Q4. The descent n x q3 instead assigns variations to the nonabelian/gravitational connections. Their difference is

n a Q4 - n x q3 = -n d(a q3).

The associated local four-dimensional Bardeen counterterm (with sign following the chosen determinant convention) implements this change of representative. General distributions are obtained by linear combinations of these representatives. This exact transgression is the reason the E6 and gravitational anomalies can both be moved to X; merely using a covariant anomaly instead of a consistent one would not supply this argument. The gravitational counterterm A times the gravitational CS current and the resulting shift into diffeomorphism violation are displayed explicitly in [2], PDF p.8, equation (2.15). Its coefficients are in that paper's conventions; the above normalized characteristic forms fix ours without copying them.

## 3. Boundary distribution and explicit cancellation

Use unit-integrated endpoint distributions delta_0 and delta_L. The previously saved full-56 parity-weighted trace calculation is replayed, not regenerated. For n I/P bulk Dirac copies with positive breaking parity it gives

I6(y)=n delta_L(y) x_L Q4,L,   I6 at the identity wall = 0.

This includes the massive tower's localized anomaly, not just the anomaly of constant zero modes. It applies to arbitrary allowed gauge parameters lambda(x,y): the X variation is i n integral_wall L lambda_L Q4,L. The full-E7 identity wall is anomaly-free in these parity traces. Boundary E7 coset parameters vanish at the breaking wall, so the new boundary action needs only the actual boundary subgroup symmetry. Orbifold anomalies need not vanish when their integral vanishes; [1], equation (10) and its discussion, explicitly demonstrate this. Covering-circle coefficients in that paper are not our unit-integrated endpoint coefficients.

Add ONLY at L a dimensionless theta with period 2pi and transformation

delta theta=k lambda_L,       k nonzero,
S_kin,E=(f_a²/2) integral_L (dtheta-k A_L) wedge *(dtheta-k A_L), f_a²>0,
exp(i S_WZ)=exp[-i (n/k) integral_L theta ((1/2)tr27 f6,L²-p1)].

Equivalently the theta couplings to (tr27 f6²,p1,x²) are (-n/(2k),+n/k,0). Their variation is -i n integral_L lambda_L Q4,L and cancels the determinant pointwise at the correct wall. The kinetic term is exactly gauge invariant and positive Euclidean quadratic energy; its Lorentzian continuation has a healthy scalar sign. No ghost or mirror fermion is used. There is no independent theta x² term: with nonzero k it would introduce an uncancelled X³ variation. Boundary Bardeen terms are to be chosen in the same localized scheme as the determinant, rather than silently assuming a different anomaly distribution.

The construction cancels all cohomologically nontrivial *local perturbative* anomalies listed above; existence of the full regulated 5D determinant/global phase is not thereby proved. A P/P model has anomaly on both walls. Placing a single ordinary axion on L to cancel its integrated 2n coefficient leaves (n,-n) locally. Independent endpoint gauge parameters forbid treating one boundary scalar as shifting under the other wall without extra nonlocal/bulk structure. Our negative controls reject exactly that error. Periodic bulk CS redistribution is neither needed nor claimed here.

## 4. Gauge generators, spectrum, and mass scales

The shift covector has components (0 on e6,k on X). With f_a²>0 and k nonzero its gauge mass matrix has rank one in the 79-dimensional zero-mode gauge sector, so its kernel is exactly e6 (dimension 78). In a four-dimensional truncation normalized as -F_X²/(4g_X,4²),

m_X²=k² f_a² g_X,4² > 0.

This expression assumes the light-mode approximation and separation from the compactification scale. A localized mass changes the exact 5D wavefunctions and boundary condition to a Robin condition; it is not an exact all-KK eigenvalue formula for arbitrary f_a. Positivity of the bulk and boundary quadratic forms removes the constant X zero mode for every nonzero boundary coefficient. E6 modes have unchanged boundary mass zero. The theta phase is eaten, not an additional physical massless axion in this minimal Stückelberg sector. Gauge redundancy survives even for massive X; calling X simply absent would not cure its anomaly.

At zero background the left-handed massless matter remains n*27+n*1 under E6; the original X charges still constrain gauge-invariant operators with theta dressings. No mirror 27 is introduced. No fermion mass operator is chosen here: Stückelberg terms alone do not provide such masses. Under the standard chain each 27 is (10+5bar+1)+(5+5bar)+1, so there are n net standard families plus vectorlike exotics and singlets, not an already realistic SM spectrum. Three copies remain three chosen bulk Dirac fields, not derived multiplicity. A Higgs sector, exotic decoupling and vacuum remain missing.

For the global quotient and k=3 described next, the stabilizer of theta is isomorphic to E6: the apparent Z3 subset of U1 is already identified with the E6 center. For k=3r its component group is Z_|r|; the group extension need not be called a direct product. No extra independent Z3 is claimed for k=3. These group statements do not prove absence of discrete anomalies.

## 5. Global quantization: progress and a real remaining condition

Because the bulk 56 is faithful, the natural compact gauge group used here is simply connected E7 (not E7/Z2). Choose z in the E6 center acting on our 27 by omega=exp(2pi i/3). The kernel of E6_sc times U1 on 56 is generated by (z,omega^-1): it acts trivially on 27_1, conjugate27_-1 and both charge-three singlets. Conversely the singlets restrict the kernel to these three elements. Hence the boundary group is H=(E6_sc times U1)/Z3, confirmed explicitly in [4], equation (3.42).

An ordinary E6-singlet phase e^(i theta) transforming with charge k is a character of H iff k is a multiple of 3. Thus k=1 is a valid *Lie algebra* calculation but not an ordinary compact singlet axion for this global group. The group fixes a lattice of charges, not a unique axion charge or decay constant.

Bare WZ periodicity requires (n/k) integral_M Q4 to be an integer on every admitted closed spin four-manifold with bundle. On liftable E6 times U1 bundles, integral u is an integer and integral p1 is in 48Z (signature theorem plus Rokhlin). Therefore k=3 passes this necessary period check for all integer n. This is not sufficient on unrestricted quotient bundles: [5] explains why fractional instantons and correlated quantization matter.

We explicitly compute the E6 generating central coweight mu from the inverse Cartan matrix: (mu,mu)=4/3 and 3mu is a coroot. Choose the sign of its paired U1 component ±1/3 so (mu,±1/3) is a cocharacter of H. On spin S2 times S2 use flux c=a+b, integral c²=2; p1 integrates to zero. The induced torus bundle has

integral u=(1/2)(mu,mu) integral c²=4/3,
integral Q4=8.

For k=3 the bare WZ phase under theta->theta+2pi is exp[-2pi i*(8n/3)]. Thus n not divisible by three FAILS this unrestricted-bundle period test. n=3 passes this example; it is not a proved full global solution and does not derive three families. Every H bundle induces an E7 bundle by extension of structure group; whether a proposed compactification/topological sector admits it must be specified rather than presumed excluded.

Crucially, a smooth fixed-modulus charged Stückelberg phase is itself a nowhere-vanishing section of its charge-k associated line bundle. It restricts allowed bundles by trivializing that line. The flux example has nontrivial charge-three line and is NOT a configuration with such a globally smooth phase. Consequently it is an obstruction to claiming the *bare WZ expression on all quotient bundles*, not an automatic inconsistency of the local smooth-patch EFT. A globally defined theory must specify restricted bundles, defects/radial completion or further topological data, and define the fermion determinant plus WZ action by appropriate differential/global anomaly data. Torsion bundles, large gauge transformations, large diffeomorphisms, boundary/corner terms and bulk regulator/parity/global anomalies are not settled by these rational checks. No globally quantized E7 completion is claimed.

## 6. Couplings and hypercharge

Anomaly cancellation constrains n/k times the WZ coefficient only. It does not constrain the positive gauge kinetic terms, f_a, L, cutoff, or boundary thresholds. With the predecessor's connection convention,

1/g6,4²=L/g7,5²+tau6,0+tau6,L,
1/gX,integer,4²=12*(L/g7,5²+tauX,0+tauX,L).

The identity wall relates normalized E7 coefficients; the breaking wall permits independent E6 and X coefficients. Even all tau=0 leaves continuous L/g7,5². Positivity and anomaly matching permit distinct positive gauge couplings. X is now massive; its coupling is not an electromagnetic coupling and cannot be substituted for alpha. Integrating out its tower and boundary sector adds matching information rather than selecting that information.

A separate clock EFT may have a neutral canonical scalar phi and a CP-even gauge kinetic function f7=f0 exp(bu). It cannot silently identify that scalar with the eaten theta here. If delta theta=k lambda with k nonzero and there are no other shifting fields or CP-even compensations, gauge invariance of f(theta) F² requires k f'(theta)=0, hence f'=0. The anomalous CP-odd theta F-tilde-F WZ variation is different and cancels a fermion determinant anomaly; it does not authorize CP-even theta-dependent gauge kinetics. An independent neutral scalar or a gauge-invariant combination of multiple fields may still support clock variations. This is a scoped compatibility condition, not a universal scalar no-go; the parent reports four independent Z3 checks in its separate lane, not checked by this lane's runner.

The conventional Y=diag(-1/3,-1/3,-1/3,1/2,1/2) lies inside SU5 inside E6, so delta_Y theta=0 and the new mass term leaves Y massless. WZ terms restrict to theta times the appropriate E6-descended gauge Pontryagin forms, but do not give Y a Stückelberg mass. With later breaking, possible kinetic mixing can change canonical fields but not the dimension/generator kernel of this single shift. No alternate hypercharge involving X is assumed. Under the earlier idealized common tree matching assumptions, kY=5/3, gY²=(3/5)g6², and after an independently supplied neutral Higgs VEV e²=(3/8)g6² still hold as conditional relations, not low-energy predictions. Reusing unbroken eight-Dirac-56 RG coefficients is invalid for this projected/new-boundary spectrum.

## 7. Evidence and reproduction

`checks.py` replays both predecessor receipts without modifying them, derives the full polynomial coefficients, checks 35 exact (n,k) coefficient cases, derives the 27 trace matrix and central coweight, and tests local support, quantization negatives and positive mass/coupling freedom. `receipt.json` is exclusive-created, then full-payload replayed; missing or tampered receipts fail. `--test` runs 13 tests. No symbolic assertions of global topology are mistaken for a theorem about all bundles.

`Conditional.lean` has two kernel-checked axiom-free conditional theorems: additive factorized cancellation and the necessity of cancelling an independently supported other-wall anomaly. These are deliberately small bridges, not representation theory, index theorem, topology, general rational-algebra or quantum-consistency formalizations. No Mathlib build is claimed.

Run native Windows commands:

C:/Users/mikeb/e7-alpha-theory/gap-investigation/.venv/Scripts/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/green-schwarz-gate/run_checks.py

`verification.json` retains real exits/output and hashes. Sources are downloaded original PDFs with extracted page-labelled text, SHA256 and excerpt ledger. No hosted CI or expert review. File tools resolved to a shadow Cygwin tree despite printed canonical paths; files were explicitly copied to the native canonical directory before real execution. Only this new lane was written; no publication.

## Primary sources

[1] Scrucca, Serone, Silvestrini, Zwirner, Anomalies in orbifold field theories, https://arxiv.org/pdf/hep-th/0110073 — PDF p.5 equation (10), local anomalies despite integrated zero; p.2 footnote covers their normalization.

[2] Landsteiner, Megias, Melgar, Pena-Benitez, Holographic Gravitational Anomaly and Chiral Vortical Effect, https://arxiv.org/pdf/1107.0368 — PDF p.8 equation (2.15), gravitational Bardeen counterterm, and p.15 nonabelian counterterm discussion. This is a primary calculation, not the original historical Bardeen article; no historical-priority claim is made.

[3] Kumar, Morrison, Taylor, Global aspects of the space of 6D N=1 supergravities, https://arxiv.org/pdf/1008.1062 — PDF p.4 equation (2.2)/Table 1, minimal-instanton trace normalization lambda_E6=6. Only this group normalization is used, not their six-dimensional matter anomaly equations.

[4] Cacciatori, Dalla Piazza, Scotti, E7 groups from octonionic magic square, https://arxiv.org/pdf/1007.4758 — PDF p.7 equation (3.42), central intersection; p.11 faithful 56.

[5] Choi, Forslund, Lam, Shao, Quantization of Axion-Gauge Couplings and Non-Invertible Higher Symmetries, https://arxiv.org/pdf/2309.03937 — section 2.2, periodicity and fractional-instanton tests. Their SM-specific coefficient table is not applied to E6; the E6 counterexample above is independently constructed and exact-checked.
