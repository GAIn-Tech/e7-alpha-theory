# Finite-flow attraction gate: slow convergence and transient amplification

## Verdict

The restricted N=8 massless non-SUSY E7 model has exact two-loop asymptotic attraction, but does not generically erase finite-scale boundary uncertainty. In particular, over any IR log interval **L <= 100** (up to about 43.43 decades of scale ratio), neither fractional distance to the fixed point nor infinitesimal boundary sensitivity can be reduced by more than about **15.3%**. Some AF trajectories instead amplify infinitesimal boundary uncertainty. This is a conditional quantitative obstruction, not a general no-go for other actions or mechanisms.

There is no supplied physical massless interval, breaking scale, or independently specified tolerance from which to establish a realistic finite-hierarchy prediction. Even the most favorable infinitesimal halving requires more than 181.52 decades. No threshold was chosen to fit alpha; no measured coupling, electromagnetic identification, or experimental scale enters this gate.

## Inputs and conventions

Inherited from `../rg-fixed-point-gate/REPORT.md` and `check_rg.py`: N=8 Dirac 56 fermions; CA=18, TF=6, CF=57/4; no scalars/Yukawas; exactly zero fermion masses; a=g^2/(16 pi^2); t=ln(mu); beta=-4a^2+9648a^3, a*=1/2412. These are conditional action and perturbative inputs, not newly derived physical facts. The predecessor's sourced approximately 3% three-loop root shift is not an all-orders error bound. This gate does not improve that truncation uncertainty.

Declare L=ln(mu0/mu)>=0, s=L/603, x=a/a*, and d=1-x. The AF basin is 0<x<1. The exact two-loop equation becomes

    dx/ds = f(x) = x^2(1-x),      dd/ds = -(1-d)^2 d.

Scenario grid, chosen as dimensionless coarse diagnostic inputs, **not observations**:

- Initial fractional deficits d0 = 0.01, 0.1, 0.5, 0.9, 0.99 (x0=0.99,0.9,0.5,0.1,0.01).
- L = 0, 1, 10, 100, 603, 1000, 10000.
- Optional diagnostic remaining-deficit fractions 1/2, 1/10, 1/100, not acceptance thresholds or fitted precision targets.

## Exact implicit solution and boundary sensitivity

Define H(x)=ln[x/(1-x)]-1/x. Differentiation gives H'(x)=1/[x^2(1-x)]>0. Hence

    H(x(L)) - H(x0) = L/603.

H ranges from minus infinity to plus infinity across the open AF basin, so this equation has one solution there for every finite real L. In the IR x0<x(L)<1; the IR limit is 1. These existence/uniqueness and calculus steps are analytic arguments, not a claimed Lean theorem.

Differentiating the implicit relation with respect to the initial boundary value gives the exact Jacobian

    J = dx(L)/dx0 = da(L)/da0 = f(x(L))/f(x0) > 0.

It is not generally equal to the remaining-deficit fraction d(L)/d0. It can exceed one while x<2/3 because f increases there. The flow therefore retains finite-time injectivity and can initially *increase* uncertainty despite monotonic motion toward the fixed point. H(x)-L/603=H(x0) is the surviving integration constant; AF alone does not fix it.

## Uniform rigorous analytic bounds

Because x0<=x(s)<1,

    exp(-s) <= d(s)/d0 <= exp(-x0^2 s).

Because -1 <= f'(x)=2x-3x^2 <= 1/3 throughout the AF basin,

    exp(-s) <= J(s) <= exp(s/3).

These bounds follow by integrating the scalar deficit and variational equations; their polynomial hypotheses are solver-checked. The exponential integration is not machine-formalized here. Strict lower inequalities hold at positive finite s for interior initial data. Thus the fixed-point linearized factor exp(-L/603) is an optimistic lower bound for both quantities, not a global equality. The mean-value theorem transfers the Jacobian lower bound to every finite pair of AF initial conditions. No interval with L<=100 can halve their separation: J>=0.8471839079. Likewise halving a deficit requires L>603 ln(2)=417.96775, or more than 181.52109 decades, independent of x0.

There is also no uniform contraction strictly below one across the *whole* open AF basin at fixed finite L: as x0 tends to zero, x(L)/x0 tends to one and d(L)/d0 and J both tend to one. Requiring a lower basin cutoff is extra boundary information. The grid is not a proof that all possible inputs lie within its endpoints.

## Certified nonlinear results

Values rounded for readability; `receipt.json` stores rational enclosures for x and J. R=d(L)/d0, J=boundary Jacobian.

| d0 | R at L=100 | J at L=100 | R at L=603 | J at L=603 | R at L=10000 | J at L=10000 |
|---|---:|---:|---:|---:|---:|---:|
| .01 | .849769 | .852350 | .372573 | .377311 | 6.40503e-8 | 6.53508e-8 |
| .1 | .872604 | .897483 | .418931 | .474772 | 7.79439e-8 | 9.62271e-8 |
| .5 | .957695 | 1.040440 | .723793 | 1.178845 | 3.41267e-7 | 1.36507e-6 |
| .9 | .998318 | 1.028773 | .989075 | 1.193139 | .00504042 | .499479 |
| .99 | .999983 | 1.003275 | .999899 | 1.019994 | .998018 | 1.428081 |

At L=603 the linearized factor is exp(-1), but a boundary starting at 1% of a* scarcely moves. At L=10000 this boundary still has J>1. The near-fixed-point approximation cannot be extrapolated indiscriminately across the AF basin.

Exact implicit required intervals for diagnostic reductions, converted to approximate decades L/ln(10):

| d0 | halve deficit | reduce to 1/10 | reduce to 1/100 |
|---|---:|---:|---:|
| .01 | 184.17 | 607.75 | 1211.22 |
| .1 | 210.99 | 654.41 | 1262.17 |
| .5 | 462.29 | 1019.18 | 1646.77 |
| .9 | 2770.61 | 3512.32 | 4161.17 |
| .99 | 26877.99 | 27679.00 | 28332.85 |

These are *deficit reduction* times, not automatically Jacobian contraction times. L and its rational enclosure are the principal certificate; displayed decimal/decade conversions are numerical summaries.

## Numerical certificate and proof boundary

`flow.py` uses high-precision Decimal bisection only to propose endpoints. Every nonzero-time x enclosure is then independently accepted or rejected using exact Fraction arithmetic on H endpoint signs. Logarithms use power-of-two range reduction and

    ln(r)=2 sum(j=0..n-1) z^(2j+1)/(2j+1) + remainder,
    z=(r-1)/(r+1), 1<=r<=2,
    0<=remainder<=2 z^(2n+1)/[(2n+1)(1-z^2)].

Here n=55. Negative power-of-two exponents reverse the ln(2) interval contribution as required. The proposed enclosure radius is 10^-32; its validity follows from exact residual signs, not Decimal precision. J is enclosed conservatively by xlo^2(1-xhi)/f(x0) and xhi^2(1-xlo)/f(x0). The target-time intervals use the same exact log bounds. The series remainder derivation and analytic ODE identity are mathematical exposition; no full formal analysis library is installed or claimed.

Seven saved SMT-LIB obligations return **unsat**: normalization to IR vector field; cleared implicit-derivative identity; positive AF vector field; deficit-rate bounds; global Jacobian-rate bounds; strict sensitivity amplification for y<x<=2/3; separation factorization. Z3 proves these real algebra statements conditional on the encoded coefficients. No new Lean artifact or full ODE/QFT theorem is claimed. Using Z3 rather than minimal Lean is deliberate: these inequalities directly support the finite-flow gate.

Ten local tests pass: log normalization, reciprocal bounds, high-precision log cross-check, zero interval, invalid-domain rejection, semigroup enclosure overlap, finite-difference Jacobian, amplification, linear lower bound, positive finite sensitivity. Saved receipt replay recomputes the deterministic certificate, hashes the Python and SMT sources, and reads existing obligations without regenerating them. `verification.json` records actual subprocess outputs and artifact hashes. Hosted CI and independent expert review were not run. Research, implementation and prose are AI-assisted.

Reproduce from the canonical directory with `C:/Users/mikeb/e7-alpha-theory/gap-investigation/.venv/Scripts/python.exe -B flow.py` and the same command plus `--test`. `--write` is deliberate certificate initialization only. The known file-tool shadow-path issue required copying initial authored files from the Cygwin shadow to native Windows paths; all execution and receipts use canonical paths.

## What remains physically open

A justified finite prediction needs independently fixed trajectory information or an independently motivated, sufficiently long unbroken massless hierarchy; protected fermion masses; a breaking action and spectrum; higher-loop/nonperturbative control; and actual low-energy matching. The current weak slope makes ordinary finite hierarchies ineffective at removing generic boundary information, but cannot exclude a separate mechanism imposing the conformal trajectory. Adding such a mechanism must not be a target-fitted boundary/threshold choice. No other lane was edited and nothing was published.
