# Scalar-to-electromagnetic matching and multi-clock null-test gate

## Outcome

A concrete **conditional** EFT now connects an E7 kinetic function to a low-energy optical ratio. With the independently fixed standard SU(5) hypercharge embedding,

\[
 H(u)\equiv e_{\rm atom}^{-2}(u)=\frac83 f_7(u)+\Delta(u),\qquad
 d_\alpha\equiv\left.\partial_u\ln\alpha_{\rm atom}\right|_0
 =-\frac{(8/3)f'_7(0)+\Delta'(0)}{(8/3)f_7(0)+\Delta(0)}.
\]

Consequently a clean optical ratio has the first-order signal
\[
 y_{ij}(t)\equiv\ln\frac{[\nu_i/\nu_j](t)}{[\nu_i/\nu_j](t_0)}
 =(K_i-K_j)d_\alpha[u(t)-u(t_0)]+O(u^2)+\epsilon_{ij}(t).
\]

This is a genuine matching/response map, **not a numerical prediction**. Neither E7 nor the previous unbroken/vectorlike actions supplies its boundary, scalar coupling, broken spectrum or scalar history. The result distinguishes four previously conflated inputs: the absolute boundary, its scalar derivative, threshold values/slopes, and the canonically normalized scalar history. No CODATA number or observed time series is used.

Three optical ratios to a common fourth reference clock give two independent alpha-only null tests when their sensitivities are known and nonzero. These are **generic varying-alpha EFT tests, not E7 signatures**. Thresholds can exactly hide a nonzero UV scalar coupling even if every alpha-only clock ratio is constant. Independently fixed threshold data, an identifiable atomic response, and independent scalar history are distinct prerequisites for recovering a UV slope.

The local exact checks were executed with Z3; the minimal Lean kernel accepted the separate abstract two-stage identification theorem with no axioms. Preserved SMT inputs, original receipt replay and rejected receipt negative controls are provided below. These prove conditional mathematics, not the assumed breaking, QFT matching coefficients, scalar solution or atomic sensitivities.

## 1. A positive kinetic EFT with an actual normalization convention

Use four-dimensional natural units, signature (-+++), a real gauge-singlet scalar phi with mass dimension one, and connection convention (couplings not inserted inside the connection). Define

\[
 F\equiv(4\pi G)^{-1/2}=\sqrt2\,\overline M_{\rm Pl},\quad
 u=(\phi-\phi_*)/F,\quad
 {\cal L}/\sqrt{-g}=\frac{\overline M_{\rm Pl}^2}{2}R
 -\frac12(\partial\phi)^2-V(\phi)
 -\frac14 f_7(u)B_{\rm phys}({\cal F},{\cal F})+{\cal L}_{\rm break,matter}.
\]

F is fixed, not an adjustable field amplitude. The scalar's kinetic term is canonical; the kinetic term in u is **-F^2(du)^2/2**, not - (du)^2/2. If a future compactification begins with a nontrivial modulus metric, it must supply the canonical map before using this action. We choose the same inverse-gravitational normalization as kappa^-1 in Damour--Donoghue; their (+---) scalar sign is the equivalent healthy convention.[1, Sec. 2.1, Eqs. (4)--(6)]

An explicit positive family, sufficient for this conditional gate, is

\[
 f_7(u)=f_0\exp(bu),\qquad f_0>0,\quad b\in\mathbb R.
\]

At fixed reference renormalization scale M above the heavy thresholds, g7^-2(M,0)=f0. Here f7'(0)=f0 b. Positivity alone does not constrain b or determine f0; b=0, either sign of b, and every positive f0 are permitted. This is an **added model family**, not a function derived from E7 invariants. A positive invariant kinetic coefficient is allowed by the symmetry. Replacing phi by an arbitrary multiple while holding its kinetic term canonical would change the theory, not create a normalization-free prediction. A local gauge-field rescaling at phi* does not remove the scalar-photon interaction from the action.

For an illustrative dynamical completion of the scalar sector only, take V= m_phi^2(phi-phi*)^2/2 with m_phi>0. This still leaves its mass, initial/boundary conditions and abundance unspecified. Its coupling to the gauge sector can source its equation of motion: in these conventions, neglecting other scalar-dependent terms,

\[
 \Box\phi-V_{,\phi}-\frac{f'_{7}(u)}{4F}B_{\rm phys}({\cal F},{\cal F})=0.
\]

A free harmonic field is therefore an approximation requiring negligible sources/backreaction and quadratic-dominated dynamics, not an automatic solution of every E7 theory. No viable breaking/matter Lagrangian is supplied here. In particular, the conventional embedding and photon are conditional on a vacuum/construction with the requisite gauge breaking and chiral low-energy content; the earlier vectorlike 56 models do not become viable by adding this scalar.

## 2. Fixed Y and the inverse electromagnetic coupling

Use the preceding embedding gate's fixed generators in the SU(5) fundamental,

\[
Y={\rm diag}(-1/3,-1/3,-1/3,1/2,1/2),\quad
T_3={\rm diag}(0,0,0,1/2,-1/2),\quad Q=T_3+Y,
\]
with Bphys=2 Tr5, kY=5/3, k2=1 and Bphys(Y,T3)=0. The generator X commuting with E6 is **not** the photon or hypercharge. In the conditional index-one chain, with extra abelian groups removed and their mixing properly accounted for, restriction of the common gauge kinetic form gives

\[
 g_2^{-2}=f_7+\Delta_2,\qquad
 g_Y^{-2}=\tfrac53 f_7+\Delta_Y.
\]

At ideal common tree matching, a conventional neutral Higgs VEV yields 1/e^2=1/g2^2+1/gY^2, so e^2=3/(8 f7). This is not a low-energy relation without running and thresholds. Defining the electromagnetic coupling in the same low-energy convention used by the atomic calculation gives instead

\[
 H(u)=\tfrac83 f_7(u)+\Delta(u),\quad
 \Delta=\Delta_2+\Delta_Y+\Delta_{\rm EW,QED,conversion},\quad H>0.
\]

The last term includes electroweak matching, QED running/decoupling and conversion to the atomic alpha convention (normally the low-energy/Thomson fine-structure constant). One must not insert an arbitrary MS-bar alpha at a high renormalization scale directly into an optical sensitivity coefficient. If surviving U(1) mixing is present, matching begins with the kinetic matrix and its photon projection; it cannot simply be ignored. Delta in this report is the resulting scalar-dependent matching remainder once that problem is solved, **not a calculated E7 correction**. At higher loops Delta can depend on the boundary coupling itself.

### Running and moving physical thresholds

Declare beta sign and RG time:

\[
 t=\ln\mu,\quad \frac{dg_a}{dt}=\frac{b_a}{16\pi^2}g_a^3+\cdots,
 \quad\frac{d g_a^{-2}}{dt}=-\frac{b_a}{8\pi^2}+\cdots.
\]

Here positive b is the screening sign. In a fixed-spectrum one-loop interval, the inverse-coupling contribution from M down to mu is +(b_a/8pi^2)ln(M/mu). With one physical heavy mass m_h(u), fixed endpoint scales M,mu and fixed beta coefficients bH above and bL below, it is

\[
 R_a(u)=\frac1{8\pi^2}\left[b_H\ln\frac{M}{m_h(u)}+b_L\ln\frac{m_h(u)}{\mu}\right],\qquad
 R_a'(u)=\frac{b_L-b_H}{8\pi^2}\partial_u\ln m_h.
\]

Finite matching terms add their own derivatives. This formula is derived by differentiating the specified piecewise one-loop running, not asserted as a complete E7 threshold. With an arbitrary moving matching scale lambda(u), its spurious derivative (bL-bH) partial_u ln lambda is canceled by the corresponding threshold matching derivative to the retained order; it is **not** a physical scalar signal. Physical mass derivatives remain. Martens explicitly describes the mass-dependent matching coefficient and its dependence on integrated-out heavy masses; his restricted two-loop GUT calculation is not a general E7 threshold result.[3, Sec. 2.3, Eq. (26), footnote 5]

Thus even if f7 is the only fundamental gauge kinetic function, scalar-dependent heavy masses, Higgs scales, compactification radii or localized kinetic terms can induce Delta'. The actual matter spectrum determines bH,bL. The earlier unbroken N=8 RG example does not supply the beta functions of an unspecified chiral, broken theory.

## 3. Derivative matching and the distinction between boundary and history

Write f0=f7(0), f1=f7'(0), Delta0=Delta(0), Delta1=Delta'(0), and H0=(8/3)f0+Delta0. Since alpha_atom=1/(4pi H), ordinary calculus gives

\[
 d_\alpha=-H'_0/H_0=-[(8/3)f_1+\Delta_1]/H_0,
 \qquad \frac{d\ln\alpha}{dt}=d_\alpha\dot\phi/F+O(u\dot u).
\]

For the exponential family, replace f1 by f0 b. If Delta is independent of f7 and u, d_alpha=-(8/3)f0 b/H0; only at clean tree boundary Delta0=Delta1=0 does it reduce to **-b**, independent of f0. Hence a nonzero fractional drift can determine b times the scalar drift while leaving the absolute coupling completely undetermined. Conversely b need not vanish when d_alpha=0: a threshold slope can cancel it.

At higher loop order, writing Delta=Delta(f7(u),u) at fixed other independent model parameters means

\[
 H'_0=[8/3+\partial_f\Delta]f_1+\partial_u\Delta.
\]

All equations using Delta1 mean the **total** derivative. Treating it as only an explicit mass derivative while omitting its coupling dependence would be inconsistent. These total derivatives also include any specified implicit scalar dependence of vevs and matching inputs.

The sign is physical: increasing H decreases alpha. The low-energy interaction in Damour--Donoghue is -(1-d_e kappa phi)F_EM^2/(4e0^2), yielding positive delta ln alpha=d_e kappa phi to first order.[1, Sec. 3, Eqs. (15)--(16)] With the fixed F=kappa^-1 and the origin shift absorbed, this gate's d_alpha corresponds to their d_e. It is **minus** the fractional slope of the inverse kinetic coefficient.

A static alpha fixes H0 only if independently measured or extracted using an accurate absolute atomic theory with known intercepts. A clock drift fixes a time derivative or a product, not H0. Integrating a drift needs an integration boundary. None of the four independent inputs below is supplied by the SI second:

| Input | Physical role | What it does not establish |
|---|---|---|
| f0 | absolute high-scale inverse coupling | f1 or scalar evolution |
| f1 (or b with f0 fixed) | UV scalar sensitivity | threshold slope or field amplitude |
| Delta0, Delta1 | broken-spectrum matching value and response | scalar history |
| phi(t), or its stochastic law | converts coupling response to a time signal | absolute gauge boundary |

## 4. Optical ratios and substantive null tests

For corrected, co-located/appropriately redshift-corrected optical clocks, let nu_i=S C_i F_i(alpha) in the leading frozen-nuisance model, with K_i=partial ln F_i/partial ln alpha evaluated at the reference. Ratios cancel the common S. Arvanitaki--Huang--Van Tilburg give precisely the optical difference of sensitivity coefficients multiplying the scalar-induced fractional alpha change.[4, Sec. III, Eqs. (9)--(11)] The coefficients must come from independent atomic calculations; no numerical K is selected here. Finite nuclear-size, recoil, other dimensionless couplings and residual experimental effects must be restored when relevant.

For four clocks 0,1,2,3 define three ratio changes to clock 0, s_i=K_i-K_0 and a(t)=delta ln alpha(t). At first order and with nuisances frozen,

\[
 \mathbf y(t)=\mathbf s\,a(t),\qquad
 s_j y_i-s_i y_j=0.
\]

If s1 is nonzero, s2 y1-s1 y2=0 and s3 y1-s1 y3=0 are two independent constraints; the third pairwise minor is redundant. This is target-independent: it needs theoretical sensitivities, not a numerical alpha target, f0, b, Delta or a chosen scalar amplitude. Over multiple epochs it also implies y_i(t)y_j(t')-y_j(t)y_i(t')=0, the rank-one temporal minor, provided sensitivities stay fixed to the expansion's accuracy.

**Three clocks are different from three independent ratios.** The cyclic three ratios A/B, B/C, C/A always obey yAB+yBC+yCA=0, even if arbitrary unrelated physics shifts each clock. This exact log closure is a bookkeeping/measurement-consistency identity, not a varying-alpha or E7 test. Among two independent ratios of three clocks, the alpha-only model supplies one additional sensitivity-weighted null. A three-ratio/four-clock setup makes the two independent physical nulls transparent. Shared reference noise induces covariance between ratios; it must be included in an actual null-test statistic.

These relations are **not E7-specific**. The factor 8/3 cancels with all of d_alpha in the weighted null. Any low-energy theory producing alpha-only changes obeys them, including a generic scalar-photon EFT. Any single scalar varying several constants can produce temporal rank one with a different fixed response vector, so temporal rank one alone does not identify alpha. Higher-order atomic response produces curvature and higher-order scalar dynamics can spoil linear rank one without falsifying E7. The exact clean nonlinear statement is a one-dimensional atomic-response curve parameterized by alpha, not a straight line unless the sensitivities are constant.

## 5. Threshold and nuisance degeneracy; real identification conditions

### Exact functional threshold degeneracy

For an arbitrary smooth h(u), make the replacement

\[
 f_7(u)\longrightarrow f_7(u)+h(u),\qquad
 \Delta(u)\longrightarrow\Delta(u)-\tfrac83h(u).
\]

H(u), alpha(u) and **every alpha-only clock observable** remain unchanged. Small enough h preserves f7>0 on any compact neighborhood with a positive lower bound; H positivity is unchanged exactly. The jet version independently shifts f0 by h0 and f1 by h1 and compensates Delta0 and Delta1. Within the unrestricted positive exponential family, different positive f0 and b can similarly be compensated by changing Delta. This is a nonidentifiability of the incomplete matching model, not a claim that every shifted Delta can be realized by an arbitrary fixed UV spectrum. Once a spectrum/action is independently fixed, its calculable thresholds need not admit the transformation.

An alpha-null observation cannot bound f1 alone when Delta1 is arbitrary: Delta1=-(8/3)f1 hides it. The idealized absence of a drift likewise says nothing about f0. Even clean known d_alpha=-f1/f0 leaves infinitely many positive (f0,f1) pairs. Positivity is not an extra measurement.

### Atomic nuisance directions

For a general local response let

\[
 \mathbf y=\mathbf s\,a+P\mathbf n+\boldsymbol\epsilon.
\]

A null vector w must satisfy w^T s=0 **and** w^T P=0. Thus the alpha-only nulls are not protected from nuclear/mass responses or clock systematics. For three ratios and one known nuisance direction p, the single projected null is (s cross p) dot y=0. Its coefficients vanish if s,p are collinear, in which case the two effects are not separately identifiable. Conversely a nonzero minor s_i p_j-s_j p_i allows a and the single nuisance amplitude to be recovered from the two corresponding responses. With two independent nuisances giving a full-rank three-column matrix there is no nontrivial three-ratio null, although three parameters can be estimated in an ideal noiseless model. Free differential systematic offsets/drifts can mask any alpha signal; priors or independently calibrated systematics are necessary.

More generally a is identifiable after nuisance marginalization precisely when s is outside the column space of P. A scalar may drive both alpha and nuisance constants; calling an optical comparison 'alpha-only' is a controlled approximation, not an E7 consequence. Failure of an alpha-only null diagnoses the response assumptions or data, not uniquely a failure of a gauge group.

### What actually restores identification

1. A calibrated atomic sensitivity/intercept model and response matrix with the needed rank, with experimental residuals and covariance constrained, can identify a(t). A time difference removes a constant intercept but not an unknown drifting systematic.
2. Independently specified **nonzero** u(t)-u(t0), or a statistical scalar field law with independently fixed amplitude distribution, can identify d_alpha rather than only d_alpha delta u. A null field excursion provides no such inverse. Phase/sign ambiguities remain if only oscillation power is observed.
3. Independently known H0 and Delta0 recover f0=(3/8)(H0-Delta0). Independently known Delta1 and d_alpha recover f1=-(3/8)(H0 d_alpha+Delta1). A prediction reverses this direction: it must specify f0,f1 and thresholds before using alpha/clock data. Extracting them from that data is an inference, not an independent prediction.
4. At higher loops a known Delta functional gives a nonlinear inverse map. Local recovery additionally requires nonzero matching derivative (8/3)+partial_f Delta; global uniqueness requires the actual map to be injective on the allowed domain. Knowing the name of a threshold function does not establish either property.

`Matching.lean` kernel-checks the abstract statement that **two supplied left inverses** (clock-to-matched-state and matched-state-to-UV-parameters) compose to give unique UV parameters from equal data. The actual real-arithmetic rank and matching statements are the separate Z3 checks. The Lean theorem does not pretend to prove those physical inverse hypotheses.

## 6. An actionable independent model package and a conditional signal

The next input that would permit a physical calculation is a target-independent, canonically normalized modulus/scalar model with:

- a viable broken/chiral construction and fixed Y photon; its complete light/heavy charged spectrum, masses m_h(phi), Higgs/compactification scales and surviving/localized kinetic terms;
- an independently determined f7(phi), including f0 and f1 (e.g. from a stabilized modulus vacuum and its canonical metric), not a coefficient chosen to reproduce alpha;
- specified renormalization/matching scheme and scale hierarchy, loop order and controlled truncation uncertainty, enabling Delta0 and Delta1 to be calculated;
- a scalar potential, couplings and cosmological/environmental initial conditions or an independently constrained local density fraction and velocity distribution;
- atomic response coefficients, nuisance priors and the chosen ratio/time-domain observable fixed before comparison with data.

As an explicitly conditional harmonic example, under a quadratic-dominated, nonrelativistic coherent scalar with weak backreaction,

\[
 \phi(t)-\phi_*\simeq\frac{\sqrt{2\rho_\phi}}{m_\phi}\cos(m_\phi t+\theta),
 \quad \rho_\phi=\eta\rho_{\rm DM},\quad
 A_{ij}=|K_i-K_j|\,|d_\alpha|\frac{\sqrt{2\rho_\phi}}{m_\phi F}.
\]

A_ij is the peak first-order sinusoidal fractional ratio amplitude; subtracting the reference epoch adds the corresponding constant offset, not another predicted oscillation. The formula is supported by the canonical scalar energy density and clock-coupling derivation.[2, Eqs. (1)--(3); 4, Sec. II, Eqs. (6)--(8), Sec. VII A] It uses the scalar's own density, not automatically all dark matter. Velocity dispersion limits coherence; a statistical signal model is needed outside a coherence interval. An arbitrary amplitude cannot be called a prediction. If rho_phi is unknown, an oscillation constrains a coupling-density product; if theta is unknown, it is a nuisance phase. No numerical m_phi, eta, rho_phi, f0 or b has been invented here.

The cited dysprosium experiment is a **radio-frequency transition search**, not a mislabeled optical-optical clock measurement.[2] The direct optical theory is [4]. The user's HyperPhysics page remains retained in `../atomic-clock-gate/hyperphysics.html`: its Cs-133/SI-second account motivates clocks but supplies none of the independent model inputs above. Its mass number 133 is not a gauge kinetic coefficient.

## 7. Executed artifacts and reproducibility

`check_matching.py` defines and executes 23 new exact real-arithmetic checks. They comprise inverse-Y matching and response/chain-rule signs; moving-threshold and arbitrary-scale cancellation; matching-boundary/slope reallocation; positive nonidentifiable states and threshold cancellation; threshold-prior inversion versus clean-drift boundary freedom; three-ratio/temporal/triangle nulls; nuisance-breaking and nuisance-projected nulls; independent versus collinear nuisance identification; unconstrained systematics; harmonic coupling-density degeneracy; and scalar-history inversion. This advances the previous gate's local two-ratio checks by supplying the EFT-to-clock map, threshold derivative and multi-ratio geometry.

Z3 SAT witnesses are mathematical assignments, not data, parameter estimates or finite-perturbation physical benchmarks. UNSAT checks negate each claimed identity or conditional identification result. The exponential positivity and differential calculus are analytic derivations in this report; the SMT files check their local polynomial consequences, not transcendental differential calculus. `Matching.lean` passed the existing Lean 4.32.1 kernel and printed no axiom dependencies for both named identification theorems. No Init/Mathlib import or full QFT formalization is claimed.

Artifacts:

- `smt/*.smt2`, `gate-receipt.json`: retained solver problems, exact SAT witnesses, actual status, complete claim boundary and source/code hashes.
- `check_matching.py`: default mode replays the **existing** receipt, checks saved SMT against mathematical definitions, re-solves it and compares the full deterministic payload without overwriting evidence. `--create` is exclusive initial creation only.
- `verification.json`: actual commands, outputs, exit codes, immutable receipt hash, kernel result, and five receipt negative controls (missing receipt, altered solver result, forged physical claim, missing check, altered source hash).
- `sources/`: four complete primary PDFs, full text extractions, precise page/equation evidence, nine exact-quotation checks and URL/hash provenance. Parent verification independently rechecks the retained source manifest, not merely the delegated success summary.
- `formalization.yaml` and `RELEASE_DISCLOSURE.md`: exact scope and trust boundary. No hosted CI or independent expert review was run.

From native Windows Bash:

```bash
C:/Users/mikeb/e7-alpha-theory/gap-investigation/.venv/Scripts/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/clock-matching-gate/check_matching.py
C:/Users/mikeb/e7-alpha-theory/gap-investigation/.venv/Scripts/python.exe -B C:/Users/mikeb/e7-alpha-theory/gap-investigation/clock-matching-gate/check_matching.py --negative-controls
C:/Users/mikeb/e7-alpha-theory/gap-investigation/lean-4.32.1-windows/bin/lean.exe C:/Users/mikeb/e7-alpha-theory/gap-investigation/clock-matching-gate/Matching.lean
```

The known file-tool/Cygwin shadow mapping was handled by copying new lane-owned files byte-for-byte into the native canonical directory before execution. No pre-existing source, sibling lane, profile, memory or skill was edited; no publishing occurred. There is a usable conditional prediction formula and a concrete independent-input stopping rule, **not a numerical E7 clock prediction**.

## Primary references

1. T. Damour and J. F. Donoghue, *Equivalence Principle Violations and Couplings of a Light Dilaton*, https://arxiv.org/abs/1007.2792v2, especially Secs. 2.1 and 3. Canonical normalization, inverse kinetic coefficient and sign of the alpha response.
2. K. Van Tilburg, N. Leefer, L. Bougas and D. Budker, *Search for ultralight scalar dark matter with atomic spectroscopy*, https://arxiv.org/abs/1503.06886v2, Eqs. (1)--(3). Scalar-photon action, oscillation amplitude, coherence and actual Dy search.
3. W. Martens, *Towards a Two-Loop Matching of Gauge Couplings in Grand Unified Theories*, https://arxiv.org/abs/1011.2927v2, Sec. 2.3, Eq. (26), footnote 5. Heavy-mass matching dependence; restricted two-loop calculation, not an E7 calculation.
4. A. Arvanitaki, J. Huang and K. Van Tilburg, *Searching for dilaton dark matter with atomic clocks*, https://arxiv.org/abs/1405.2925v2, Secs. II--III and VII A. Density/amplitude assumptions and direct optical-ratio sensitivity theory.

The fixed hypercharge traces and conditional photon matching are the executed antecedent in `../embedding-gate/REPORT.md`; the basic ratio conventions and full HyperPhysics/NIST/BIPM source captures are in `../atomic-clock-gate/REPORT.md`. Neither is used as evidence for an already viable chiral E7 completion.
