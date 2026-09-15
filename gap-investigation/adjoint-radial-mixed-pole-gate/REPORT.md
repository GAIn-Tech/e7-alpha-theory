# Recovered adjoint-radial mixed scalar–vector gate

## Result and claim boundary

At `s = 4320 epsilon M²`, `Q² = epsilon M²`, strict Landau gauge and MSbar,

**Pi_SV / (epsilon² M²) = -6901.51071046 + 3077.65019492 i.**

This is the complete derivative-bubble subset with all **188 real internal scalars** and **79 vectors**, not a gauge-independent pole or a decay width. There are 67 gauge Goldstones plus 121 quotient scalars; the full tree scalar soft space has dimension 78. The kernel calculation uses the tree action at the tree stationary background, appropriate for a one-loop contribution; mass/vertex changes from the one-loop displacement would enter this bubble at the next loop order. Couplings and masses inherit the declared EFT normalization, not a compactification derivation.

The 67 Goldstones alone contribute `-6669.26283161 + 2973.93850915 i`; the quotient scalars contribute `-232.24787886 + 103.71168576 i`. Their coupling-squared sums are respectively `11.596820257368204` and `0.40317974263179734`, totaling 12. No positive Goldstone mass, absolute-mass logarithm, or IR clipping is introduced. Eigenvalues below `1e-8` in absolute value are recognized as numerical representations of the independently verified Ward kernel, not made massive. Massive eigenvalues are grouped to nine decimal places; this is a floating numerical certificate, not exact arithmetic or interval proof.

## Recovery

Read the native original transcript `deleg_030c2c73/task-0.log`; it contains three timeout returns and no completed receipt. The only pre-existing lane artifact was `calculation.py`. Native process inspection found no identifiable running calculation process (two inaccessible Python command lines remained unidentified and were not terminated). Original source is preserved unchanged. No original receipt was overwritten.

The interrupted source was not ready to promote:

* It projected internal scalars onto the 121-dimensional physical quotient, dropping nonzero Goldstone derivative couplings.
* Its overall `-C² BSV` sign contradicted the canonical scalar–vector diagram and the retained primary source, whose scalar potential bubble has `-lambda² B` while the derivative bubble has `+g² BSV` in the same convention.
* Its UV expression omitted both A-function residues and the B(X,0) residue.
* Its unpivoted QR was not a reliable Goldstone frame when gauge columns are dependent. Recovery uses the rank-67 SVD image.
* `M.setup()` was recomputed inside a 79-entry comprehension, with no cached tensors. The interruption was not evidence of a physics failure.
* The inherited positive-s analytic B routine takes real parts of complex roots below threshold. A diagnostic found disagreement there; the new master routine rejects negative discriminant and is used only in its valid above-threshold domain. Near-zero tests use the independent parameter integral instead.

`recovery-audit.json` is an additive certificate of the failed completeness assertion. `finite-momentum-receipt.json` supersedes it scientifically without erasing that provenance.

## Canonical action and vertices

Take real antisymmetric generators `R_a` (including the declared coupling normalization), `D phi = d phi + A_a R_a phi`, and `phi=x+eta`. Expansion gives

`Lkin = (d eta)²/2 + A_a (R_a x).d eta + A_a (R_a eta).d eta + A_a A_b [R_a(x+eta)].[R_b(x+eta)]/2`.

Writing `eta = h v_A + S_i E_i`, the derivative cross term is

`C_ai A_a.[h dS_i - S_i dh]`, with `C_ai = E_i^T R_a v_A`.

The all-incoming momentum vertex is proportional to `C_ai(p_h-p_i)_mu`; the overall vertex phase depends on the Fourier/Feynman convention and is fixed together with the propagator phases. There is no identical-line factor for the distinct S,V lines. With loop vector momentum k, contraction gives

`(2p-k)_mu P^{mu nu}(k)(2p-k)_nu = 4[p²-(p.k)²/k²]`.

This fixes the numerator, sign relative to the scalar master, and its exact p=0 zero. The actual coefficient is `+sum C_ai² BSV/(16 pi²)` in `s-m_tree²-Pi(s)`. Merely noticing `I=-B` in the scalar predecessor does NOT justify changing the derivative diagram's sign.

For this D convention the gauge fixing may be chosen `F_a = d.A_a + xi (R_a x).eta`, `Lgf=-F_a²/(2xi)`, cancelling the background bilinear after integration by parts. Goldstone masses are `xi mV²` and remain zero at strict xi=0; ghosts have scalar-background vertices proportional to xi. Gauge fixing does not remove internal Goldstone fields. A simultaneous opposite sign convention for R and F changes no squared coupling.

## Integral, UV and cuts

Using `A(X)=X(log(X/Q²)-1)` and `B(X,V;s)=-int_0^1 log[tX+(1-t)V-st(1-t)-i0] dt`, the reduced kernel is

`BSV = (2X-V+2s)B(X,V)+A(X)-A(V)+[(X-s)A(V)-(X-s)²(B(X,V)-B(X,0))]/V`.

Source: retained primary text from Elias-Miro, Espinosa, Konstandin, arXiv:1406.2652, Appendix A, (A.1)–(A.5); its hash is in the receipt. Massless-vector couplings of this radial field vanish to numerical tolerance, so no active channel needs V=0 division.

An independent tensor-first Feynman-parameter reduction gives

`BSV = 6s/V int_0^1 [A(Delta_0)-A(Delta_V)] dt - 2s`,

`Delta_V=tX+(1-t)V-st(1-t)-i0`.

The `-2s` is the finite evanescent product from the `d=4-2e` transverse tensor average and UV pole. The integral is evaluated by split quadrature across real threshold roots, whereas the first reduction uses analytic scalar-master logarithms. `A(0)=0` is implemented as its exact continuous limit.

Before subtraction the master residues are `A(X): -X DeltaUV`, `B: +DeltaUV`. They give exactly `3s DeltaUV` per squared coupling, not a mass-dependent residue; total residue is `984.841905003524 epsilon² M²`. UV cancellation is a local wavefunction counterterm in the subset. Finite counterterms are zero by the stated MSbar prescription; finite scheme changes are not ruled out.

Both the massive-vector/scalar cut and the massless denominator introduced by the Landau projector are retained. The latter is a gauge artifact, not an additional physical particle or partial width. Direct phase-space interval evaluation gives imaginary coefficient `3077.650194916984`, agreeing with the master expression. At this s all active shell channels are open.

## Tadpoles and external mixing

The derivative SV term vanishes for constant external background and contributes no one-loop potential tadpole. The momentum-independent vector seagull is already counted in the predecessor, not in SV. Independently differentiating the vector determinant and solving the positive tree-Hessian block gives the vector stationary tree shift **-45.10700126487947**, agreeing with its original gauge-sector receipt. It must be included once when sectors are added.

`(R x) v_A = 0`, `G^T H v_A = 0`, and `H v_A=4320 v_A`; the nearest other scalar pole is separated by 4283.5 in tree units. For the full block inverse propagator, `D_eff = D_hh - D_hq D_qq^{-1} D_qh`. Tree off-diagonal blocks vanish; evaluated at this nonzero isolated tree pole, the complementary scalar/longitudinal-Goldstone blocks have no pole there. Thus one-loop off-diagonal insertions first contribute quadratically at two-loop order. A scalar–vector amplitude must be proportional to p_mu by Lorentz invariance and cannot mix into transverse vector polarizations. This establishes the order without claiming that the one-loop hA/hG amplitudes vanish or have been computed. It is a perturbative loop-counting statement; general-xi cancellation and possible higher-order enhancements remain separate.

## Executed tests and limitations

* Ward `max|H(Rx)^T| = 6.1431e-12`; external tree mixing exactly zero numerically.
* Analytic p=0 SV residual `5.7131e-18`; independent near-zero values vanish linearly.
* Independent split-parameter integral: 256-node `-6901.51074617`, 512-node `-6901.51071274`; 512-node absolute difference from analytic result `2.2739e-6`.
* Full equal-mass scalar/vector basis rotations, including the complete soft scalar block: difference `2.8761e-12`.
* Exact polynomial UV residue test and independent cut identity asserted in executable code.
* Negative controls: omit Goldstones; reverse overall sign; drop transverse subtraction (nonzero p=0); omit evanescent term; omit vector stationary shift. These change the answer or violate a required identity. They are algebraic/numerical controls, not independent expert review.

A conditional bookkeeping sum using the retained scalar/fermion and transverse-vector receipts, the recovered vector stationary shift, and SV is

`505145.4645135748 - 235147.46524822008 i`.

**This is not certified as a full pole.** Predecessor receipts were read and their integrity checked where available, not recomputed end-to-end here. In particular their scalar 256-vs-512 discrepancy is about **1.0908189794**, much larger than this lane's integration difference. Do not report all digits of the conditional sum as physical precision. No general-xi Nielsen cancellation, gauge-independent/full-pole result, physical width, hard two-loop tadpoles, or complete one-loop mixing amplitudes are claimed. No Lean proof, interval-certified enclosure, hosted CI, or external peer review was performed.

## Replay

Use the explicit native interpreter:

`C:/Users/mikeb/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe .../adjoint-radial-mixed-pole-gate/run_checks.py`

The checker validates the checkpoint against a fresh native construction without overwriting it, checks saved source hashes and the receipt, and replays the finite calculation without `--create`. `calculation.py` and `integral_probe.py` are historical/diagnostic, not release entry points. Scope is this lane only; nothing was published.
