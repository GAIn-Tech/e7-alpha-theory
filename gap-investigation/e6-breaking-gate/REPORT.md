# Bounded E6-to-SM breaking and exotic-mass gate

## Outcome
**27 directions alone cannot break the conventional SU(5) to the SM. Two independent 27 singlet VEVs plus an independently assigned adjoint Y VEV do have exactly the SM stabilizer inside E6. This is an algebraic configuration, not a demonstrated stable vacuum.** In the conventional renormalizable supersymmetric sector with massive adjoint(s), its required SU(5)-24 adjoint VEV is F-term obstructed. A primary explicit SUSY escape uses 351prime+conjugate as additional model input.

Existing actions were inspected through canonical embedding/chiral reports and the actual embedding code/receipt: the earlier nonsupersymmetric Dirac-56 action has no elementary breaking scalars; the earlier singlet SUSY vacuum leaves E7 unbroken. The I/P full-hyper projection supplies chiral matter but no demonstrated breaking potential. Nothing in this report derives scalar content, family number or an absolute coupling. The independent Green-Schwarz lane is not assumed successful.

## Exact root-action calculation
Reuse the predecessor's complete minuscule orbit and its Cartan/root routines, preserving Bourbaki E6 nodes 1..6. Take the conventional D5 on nodes 1..5 and A4=SU5 on nodes (1,3,4,5). The full orbit has 27 weights; 72 E6 roots give 432 nonzero directed weight transitions. The only SM-invariant weight directions are also SU5-invariant:

```
s0 = (0,-1,0,0,0,1), s1 = (0,0,0,0,0,1).
Y = -H1/3 -2 H3/3 -H4 -H5/2.
Y|5 = diag(-1/3,-1/3,-1/3,1/2,1/2).
Bphys=2 B0; B0(Hi,Hj)=Aij; Bphys(Y,Y)=5/3.
```

Weight coordinates are Dynkin labels, not simple-root coefficients. For each independent scalar field assigned a weight vector, compact infinitesimal invariance is tested with BOTH raising and lowering actions: a root plane survives iff w+alpha AND w-alpha are absent from the minuscule orbit for every VEV. Nonzero minuscule string maps are guaranteed by the standard representation theorem, not invented coefficients. Different roots have different output weights, so on these separate weight-basis VEVs there are no missed cancellations between root generators or Cartan outputs. This calculates the **compact** stabilizer; the complex holomorphic annihilator of one highest-weight vector would instead contain nilpotent generators and is not the compact gauge stabilizer.

| Configuration inside E6 | Surviving roots | Cartan | Lie dimension |
|---|---:|---:|---:|
| One s0 or s1 VEV | 40 | 5 | 45 (D5) |
| Two separate fields with VEVs s0 and s1 | 20 | 4 | 24 (A4=su5) |
| One such direction plus A proportional to Y | 8 | 5 | 13 (SM plus extra u1) |
| Two independent directions plus A proportional to Y | 8 | 4 | 12 (SM) |

The two-direction root set is explicitly matched to the regular A4 subsystem, and the last set to its Y-neutral A2+A1 roots; identification is not based only on dimensions. Conjugate fields with conjugate VEVs do not reduce these compact stabilizers further and can cancel D terms, but F terms must also vanish. Any number of 27/bar27 VEVs preserving this fixed SM lies in their SU5-singlet subspaces. Thus all such alignments preserve SU5, including arbitrary linear combinations: this scoped obstruction does not require classifying the stabilizer of each generic combination. Non-SM-singlet VEVs cannot preserve the specified SM embedding.

The table is inside E6. With gauged external X, two equally charged scalar directions leave a further linear combination of X and E6 Cartans; the same-charge two-VEV constraints lower rank by two, from seven to five. A separately consistent Stueckelberg mass for X could remove that remaining abelian direction, but neither gauge redundancy nor anomaly consistency can be discarded. No global gauge-group quotient is established by this Lie-algebra calculation.

## Potential gate: an actual scoped obstruction, not a stability label
Primary [1], section 3.1, equations (14)-(20), analyzes arbitrary copies of 27,bar27,78. On their SM-singlet locus the renormalizable cubic superpotential contains no SU5-24 VEV: 1*24*1 is not invariant, E6 has no symmetric adjoint cubic, and antisymmetric multi-adjoint cubics vanish on these singlet directions. For one adjoint define its quadratic convention as W24=(m/2) a^2; for several use W24=(1/2) a^T M a. Then

```
F24 = M a.
det M != 0 and F24=0 => a=0.
```

This is the precise SUSY lock relevant here. In one real component with canonical metric and real m, V24=m^2 a^2, derivative 2m^2 a and Hessian 2m^2: for m nonzero its minimum is a=0, the wrong symmetry. The Z3 test excludes m!=0, m*a=0, a!=0, and admits a!=0 when m=0. A zero/singular mass evades the implication but supplies no isolated stabilized SU5-breaking vacuum; on this restricted superpotential locus it is flat. We have not computed the complete scalar Hessian, soft-breaking effects, nonrenormalizable terms or a nonsupersymmetric potential. [1] reports the one-pair 27+bar27+78 SUSY model actually stops at SO10; extra copies do not remove the SU5 lock for generic massive adjoints.

The nonsupersymmetric two27+78 configuration passes only the algebraic table. [2] cites Kalashnikov-Konshtein, Nucl.Phys.B166(1980)507, DOI 10.1016/0550-3213(80)90210-2, for such renormalizable-potential analysis. The original article was blocked; no parameter inequalities or stability result from it is asserted.

### Source-backed bounded next scalar requirement
[1] explicitly solves an SM-breaking F/D-flat sector H+barH+E+barE, H=27 and E=351prime in the authors' upper-index convention (conjugate naming differs from Slansky). Equation (29):

```
W = m_E E barE + m_H H barH
  + lambda1 E^3 + lambda2 barE^3
  + lambda3 H^2 barE + lambda4 barH^2 E
  + lambda5 H^3 + lambda6 barH^3.
I_E^3 = 3(e3 e4^2 + e1 e5^2 - sqrt(2)e2 e4 e5).  [eq32]
I_H^2barE = c2^2 f1 + sqrt(2)c1 c2 f2 + c1^2 f3. [eq34]
f5 = m_E/[3 sqrt(2)lambda1^(1/3)lambda2^(2/3)]. [eq72]
```

The e4/e5 and f4/f5 directions carry SU5-24 content, explaining how the lock is bypassed. Equation (73) imposes the associated D-flat relation; f5 cannot be selected independently. This report does not rerun that paper's complete nonlinear solution. Its original sector has a doublet-triplet splitting problem; [2] adds 78 and gives a fuller model. These are **new scalar/action choices**, not scalar fields derived from the projection. In particular their E6-only superpotential is not automatically invariant under this project's X: nonzero X charges can prohibit the displayed cubic terms and require a fresh charged/compensated action. This is an existence source for E6 breaking, not a transferred solution of E6 x X.

## E6 cubic and exotic mass channel
Do not confuse the preceding E7 56-cubic obstruction with E6's symmetric d tensor. [1] equations (12)-(13) fixes

```
(1/6)d_abc 27^a27^b27^c = -det L + det M - det N - tr(LMN),
d_abc d^{bce} = 10 delta_a^e.
```

The receipt counts zero-weight triples as a necessary selection-rule check; it does not construct d or prove invariance from zero weights alone. Use the sourced invariant above. With internal SO10 x U1psi convention 27=16_(1)+10_(-2)+1_(4), its channels include 16*16*10 and 10*10*1. Therefore a newly added scalar H in 27 with its SO10-singlet component acquiring VEV gives 10_F 10_F <1_H>. The vectorlike 5+bar5 in each SO10 10 can gain mass while the 16's chiral 10+bar5 remains. A second 16_H singlet VEV can mix the two bar5 types; a full-rank 5-to-bar5 matrix still leaves one net bar5 per 27. No desired rank follows automatically.

For three chosen families, an explicit diagonal Yukawa example diag(1,2,3) and nonzero singlet VEV has rank three. It pairs three 5s against six bar5s, leaving three bar5s and the three chiral 10s; this is an input/example, not a mass prediction or observed flavor fit. Singlet masses, light Higgs doublets, triplet constraints and realistic flavor remain unproved.

The separate external charge condition is essential:

```
qX(F)=+1; qX(F F H)=2+qX(H).
Renormalizable invariant FFH requires qX(H)=-2.
Three 27(+1) factors have total X=+3, not zero.
```

A scalar 27(-2) is an explicit possible new boundary-sector representation, not the projected 27(+1) relabeled. In SUSY a bar27(+2) partner may aid D-flatness; its anomaly contribution and full action need checking. Alternatively a charge -3 compensator for a 27(+1) scalar yields a higher-dimensional operator, or an axion-dressed operator must obey its genuine transformation law. A massive Stueckelberg X still has gauge redundancy and does not legalize a forbidden polynomial. No independent anomaly repair is assumed.

## Verification / files / limitations
`breaking_checks.py` replays the canonical predecessor receipt before computing. `breaking-receipt.json` stores all 27 weights, full surviving root sets, exact normalization, source hashes and scope. Default mode reads and compares the saved receipt; `--create` is exclusive. `test_breaking.py` has six executed passing tests, including missing receipt, tampered payload, tampered source hash, rank/charge example and Z3 massive-adjoint obstruction/zero-mass countercase. `verification.json` records real subprocess outputs/hashes. An early receipt before the one-VEV-plus-adjoint assertion was preserved as `development-receipt-superseded.json`, not silently accepted as current evidence.

Only this lane was written. File tools reported canonical paths but wrote to C:/cygwin64/c shadow paths; files were copied to canonical native Windows paths before execution. The source worker's missing helper is not a deliverable; actual saved source HTML/text and evidence notes exist. No Lean theorem, hosted CI, expert review, full stable vacuum, quantum consistency, absolute alpha, or publication is claimed. Exact finite Python/Z3 plus external minuscule representation theory and cited primary formulas is the trust boundary.

Sources: [1] https://arxiv.org/html/1311.0775v2 (Bajc-Susic); [2] https://arxiv.org/abs/1504.00904 (Babu-Bajc-Susic); [3] https://arxiv.org/html/1607.06900v3 (component exotic Yukawa example). See `sources/evidence-notes.md`, `citations.json`, and saved primary HTML/text for equation provenance and blocked-source boundaries.
