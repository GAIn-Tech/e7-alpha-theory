##### Report GitHub Issue

Content selection saved. Describe the issue below:

![](/static/base/1.0.1/images/icons/smileybones-small.svg)
![arXiv logo](/static/base/1.0.1/images/arxiv-logo-primary-light.svg)

The decoupling of moduli about the standard embedding
  
Beatrice Chisamanga† 1, Jock McOrist♯ 2, Sebastien Picard$ 3, and Eirik Eik Svanes† 4

† Department of Mathematics and Physics
  
Faculty of Science and Technology
  
University of Stavanger
  
N-4036, Stavanger, Norway

♯Department of Mathematics2
  
School of Science and Technology
  
University of New England
  
Armidale, 2351, Australia

$ Department of Mathematics
  
University of British Columbia
  
1984 Mathematics Road
  
Vancouver, BC, Canada

Abstract

We study the cohomology of an elliptic differential complex arising from the infinitesimal moduli of heterotic string theory in the supergravity approximation. We compute these cohomology groups at the standard embedding, and show that they decompose into a direct sum of cohomologies. While this is often assumed in the literature, it had not been explicitly demonstrated. Given a stable gauge bundle over a complex threefold with trivial canonical bundle and no holomorphic vector fields, we also show that the Euler characteristic of this differential complex is zero. This points towards a perfect obstruction theory for the heterotic moduli problem, at least for the most physically relevant compactifications.

## 1 Introduction

String compactification is a process which embeds a four-dimensional spacetime into a ten-dimensional string theory. The string theory studied in 1986 by [[1](#bib.bib1)] is the heterotic string, whose spacetime has an ansatz of the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | M10−n×Xnc​o​m​p​a​c​t,M\_{10-n}\times X\_{n}^{compact}~, |  | (1.1) |

where M10−nM\_{10-n} is non–compact and the vector bundle is identified with the tangent bundle – this setup is known as the standard embedding. More general heterotic string compactifications, of interest due to their ability to embed chiral gauge theories close to the minimally supersymmetric standard model, for example [[2](#bib.bib2)], and their tractability in computing quantum corrections which may be phrased in terms of geometric conditions on Xnc​o​m​p​a​c​tX\_{n}^{compact}. The most physically relevant case is n=6n=6 described in [[3](#bib.bib3), [4](#bib.bib4)]. As the string compactification at a fundamental level is described by a two-dimensional conformal field theory, it is possible to replace the geometry of XX by an abstract CFT with an appropriate collection of symmetries such as a Gepner model. Nonetheless, theories defined by Calabi-Yau manifolds with stable vector bundles are still the most widely studied due to their well established mathematics and being amenable to both worldsheet and supergravity methods.

We focus here on heterotic compactifications that realise four-dimensional Minkowski spacetime with N=1N=1 supersymmetry, meaning that XX is a compact complex 3-fold with vanishing first Chern class. There is a vector bundle VV that is holomorphic which admits a connection that is hermitian Yang-Mills. The Green-Schwarz anomaly relates the hermitian form on XX to topological constraints on VV. Over the years many authors have established solutions of the 10-dimensional heterotic supergravity, and realized a 4-dimensional Minkowski space via the standard embedding and other ways. These geometries define a conformal field theory with (0,2)(0,2) supersymmetry, and little is known about these theories at a fundamental level. There is a limit in which this enhances to (2,2)(2,2) supersymmetry, with many more calculation tools available, and this limit is known as the standard embedding. It is in this limit that mirror symmetry and special geometry exists with which the complete couplings of the theory can be determined. A simple problem going beyond this limit is to study deformations of the standard embedding that do not necessarily preserve (2,2)(2,2) supersymmetry. Geometrically, this amounts to studying deformations of the Calabi-Yau manifold together with deformations of the tangent bundle that are not connected to the underlying Calabi-Yau such that the spacetime supersymmetry conditions are satisfied.

From the point of view of spacetime, the deformations are coupled via the supersymmetry variations and the Bianchi identity. When written in terms of spinor bilinears, and related to the differential geometric structures of the internal manifold XX, some of these can also be written as the variation of a functional called the superpotential [[5](#bib.bib5), [6](#bib.bib6), [7](#bib.bib7), [8](#bib.bib8)], so we call them F-terms in analogy with N=1N=1 d=4d=4 supersymmetry. These were extended in [[9](#bib.bib9)] to a study of finite deformations. The remaining supersymmetry variations we would like to refer to as D-terms, continuing the analogy, and evidence for this was presented in [[10](#bib.bib10)], and further studied in [[11](#bib.bib11)] in which using the string theory moduli space metric, calculated in [[12](#bib.bib12), [13](#bib.bib13)] by a dimensional reduction to first order in α‵{\alpha^{\backprime}\,}, it was demonstrated that the F-terms correspond to the kernel of a certain D¯\overline{D}-operator and the D-terms lie in the kernel of its adjoint D¯†{\overline{D}}^{\dagger} with respect to the metric on moduli. In [[14](#bib.bib14), [15](#bib.bib15)] the D-terms were presented in terms of a moment map construction, all of this consistent with the usual N=1N=1 d=4d=4 supersymmetry lore. All this being said, and unlike the case of the moduli space of Calabi-Yau manifolds (e.g. see the classic work [[16](#bib.bib16)]), it is certainly not obvious the deformations decouple into a direct sum of cohomologies related to complex structure of the manifold, the hermitian structure, and endomorphisms of the tangent bundle. A toy example which we return to later is that, as noted by Atiyah [[17](#bib.bib17)], as the bundle is holomorphic it requires a field strength F(0,2)=0F^{(0,2)}=0 with respect to the complex structure of XX. For a generic deformation of complex structure, one might worry we generate some F(0,2)F^{(0,2)} that violates this condition; indeed, this is the case if such a deformation is not ∂¯𝒜{\overline{\partial}}\_{\mathcal{A}}–exact, in which case the corresponding complex structure deformation of the manifold XX is not a deformation or parameter of the heterotic theory. See [[18](#bib.bib18), [19](#bib.bib19), [20](#bib.bib20)] for applications of this mechanism to the heterotic moduli problem.

From the point of view of the worldsheet theory, when studied via a gauged linear sigma model the deformations of the bundle and the traditional deformations of the CY appear on the same footing at least when computing worldsheet instanton corrections to Yukawa couplings [[21](#bib.bib21), [22](#bib.bib22)]. The same conclusion holds when the semi-classical non–linear sigma model is studied [[23](#bib.bib23)]. Thence, it is not obvious what the action of mirror symmetry is on the parameter space. That being said, this question has been answered to some extent for CY manifolds that are complex intersections in toric varieties satisfying a certain combinatorial condition [[24](#bib.bib24), [25](#bib.bib25)], but the connection to the spacetime description of the moduli space, via the Hull-Strominger system, is an open question. What happens when this condition is not satisfied is also an open question, even for deformations of the standard embedding.

The goal of this paper is to demonstrate that the parameter space of heterotic theories about the standard embedding decomposes into a sum of cohomologies utilising results derived in [[26](#bib.bib26), [13](#bib.bib13)] and later in [[10](#bib.bib10)]. We also draw inspiration from Atiyah’s work [[17](#bib.bib17)], and later applications in physics and mathematics [[18](#bib.bib18), [19](#bib.bib19), [20](#bib.bib20), [27](#bib.bib27), [28](#bib.bib28), [29](#bib.bib29), [15](#bib.bib15), [30](#bib.bib30), [31](#bib.bib31)], where the simultaneous deformations of the geometry and the bundle were considered at the level of α‵{\alpha^{\backprime}\,}-correct supergravity.

More specifically, we are interested in the total moduli that result from the simultaneous deformations of the metric, complex structure, and gauge connection. The infinitesimal moduli are computed by a cohomology HD¯0,1​(Q)H^{0,1}\_{\bar{D}}(Q) [[10](#bib.bib10)], which can be computed using homological algebra techniques and long exact sequences. We show that these sequences split at the standard embedding, leading to an infinitesimal spectrum

|  |  |  |  |
| --- | --- | --- | --- |
|  | HD¯0,1​(Q)≅H1,1​(X)⊕H2,1​(X)⊕H0,1​(End0​(V)).H\_{\bar{D}}^{0,1}(Q)~\cong~H^{1,1}(X)\oplus H^{2,1}(X)\oplus H^{0,1}({\rm End}\_{0}(V))~. |  | (1.2) |

Note, there is a substantial swath of literature that implicitly use this result, without having actually verified it is true. We do that here.

Finally, given physically motivated assumptions about the holomorphic bundles involved, i.e. a stable gauge bundle over a complex threefold with trivial canonical bundle and no holomorphic vector fields, we also show that the associated heterotic moduli complex has vanishing Euler characteristic. This is a simplified version of a more general proof of vanishing index for the moduli problem of heterotic S​U​(3)SU(3) solutions found in [[32](#bib.bib32)]. This points towards a perfect obstruction theory for heterotic moduli, at least for the most physically relevant compactifications, which may also have implications for the heterotic string theory moduli problem, and for understanding geometric invariants in this setting.

## 2 An elliptic complex

We begin by showing that the differential complex governing the six-dimensional heterotic moduli problem is elliptic, and so the corresponding cohomologies are finite-dimensional. Let (X,ω)(X,\omega) be a complex hermitian manifold. Let V→XV\rightarrow X be a holomorphic vector bundle with connection and denote its curvature 2-form by FF. Let Q=T∗(1,0)​X⊕End0​(V)⊕T1,0​XQ=T^{\*(1,0)}X\oplus{\rm End}\_{0}(V)\oplus T^{1,0}X. We equip the smooth complex vector bundle Q→XQ\rightarrow X with a differential operator

|  |  |  |  |
| --- | --- | --- | --- |
|  | D¯:Ω0,p​(Q)→Ω0,p+1​(Q),D¯=[∂¯α′​ℱ∗𝒯+α′ℛ⋅∇0∂¯Aℱ00∂¯].\bar{D}:\Omega^{0,p}(Q)\rightarrow\Omega^{0,p+1}(Q),\quad\bar{D}=\begin{bmatrix}\bar{\partial}&\alpha^{\prime}\mathcal{F}^{\*}&\mathcal{T}+\alpha^{\prime}\mathcal{R}\cdot\nabla\\ 0&\bar{\partial}\_{A}&\mathcal{F}\\ 0&0&\bar{\partial}\end{bmatrix}. |  | (2.1) |

The definitions are as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℱ⁡(Δ)\displaystyle\mathcal{F}(\Delta) | =Fμ​ν¯​d​xν¯∧Δμ\displaystyle=F\_{\mu\bar{\nu}}{\text{d}}x^{\bar{\nu}}\wedge\Delta^{\mu} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℱ∗​(𝔞)\displaystyle\mathcal{F}^{\*}(\mathfrak{a}) | =Tr​Fμ​ν¯​d​xμ⊗d​xν¯∧𝔞\displaystyle={\rm Tr}\,F\_{\mu\bar{\nu}}{\text{d}}x^{\mu}\otimes{\text{d}}x^{\bar{\nu}}\wedge\mathfrak{a} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒯⁡(Δ)\displaystyle\mathcal{T}(\Delta) | =Hρ​ν¯​μ​d​xρ⊗d​xν¯∧Δμ\displaystyle=H\_{\rho\bar{\nu}\mu}{\text{d}}x^{\rho}\otimes{\text{d}}x^{\bar{\nu}}\wedge\Delta^{\mu} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ℛ⋅∇(Δ)\displaystyle\mathcal{R}\cdot\nabla(\Delta) | =−1p!Rρ​μ¯σλ∇^σΔλκ¯1⋯κ¯pdxρ⊗dxμ¯κ¯1⋯κ¯p,\displaystyle=-\frac{1}{p!}R\_{\rho\bar{\mu}}{}^{\sigma}{}\_{\lambda}\hat{\nabla}\_{\sigma}\Delta^{\lambda}{}\_{\bar{\kappa}\_{1}\cdots\bar{\kappa}\_{p}}\,{\text{d}}x^{\rho}\otimes{\text{d}}x^{\bar{\mu}\bar{\kappa}\_{1}\cdots\bar{\kappa}\_{p}}\>, |  |

where Δ∈Ω0,p​(T1,0​X)\Delta\in\Omega^{0,p}(T^{1,0}X), 𝔞∈Ω0,p​(End0​(V)CLOSE\mathfrak{a}\in\Omega^{0,p}({\rm End}\_{0}(V), H=i(∂−∂¯)ωH=i(\partial-\bar{\partial})\omega and ∇^\hat{\nabla} is the Bismut connection when acting on holomorphic “free" indices, and the Chern connection when acting on form indices. The mathematical origins of this operator can be found in [[33](#bib.bib33), [34](#bib.bib34)] and its relevance in heterotic string theory was discovered in [[28](#bib.bib28), [27](#bib.bib27)]; see [[10](#bib.bib10)] for the setup without spurious modes. The significance of the operator D¯\bar{D} is that its nilpotency is related to the heterotic Bianchi identity.

The calculation of [[11](#bib.bib11)] shows that the equation D¯2=0\bar{D}^{2}=0 is equivalent to

|  |  |  |  |
| --- | --- | --- | --- |
|  | i​∂∂¯​ω=α′2​Tr​F∧F−α′2​Tr​R∧R,i\partial\bar{\partial}\omega=\frac{\alpha^{\prime}}{2}{\rm Tr}\,F\wedge F-\frac{\alpha^{\prime}}{2}{\rm Tr}\,R\wedge R\>, |  | (2.2) |

where RR is the Chern curvature of the hermitian metric ω\omega. We note that this is not the usual Bianchi identity from string theory since there RR is computed with respect to the Hull connection [[3](#bib.bib3)], however ([2.2](#S2.E2 "In 2 An elliptic complex")) agrees with the physical system up to O⁡(α′2)O(\alpha^{\prime 2}) in the regime where H=O⁡(α′)H=O(\alpha^{\prime}), and so ([2.2](#S2.E2 "In 2 An elliptic complex")) is a good mathematical approximation to the physical system at order O⁡(α′2)O(\alpha^{\prime 2}) in the action when H=O⁡(α′)H=O(\alpha^{\prime}). The advantage of ([2.2](#S2.E2 "In 2 An elliptic complex")) is that the exact equality D¯2=0\bar{D}^{2}=0 allows us to use methods from homological algebra to compute the cohomology of the complex defined by D¯\bar{D}.

In summary, we have interpreted equation ([2.2](#S2.E2 "In 2 An elliptic complex")) as a sort of holomorphic structure (Q,D¯)(Q,\bar{D}) on the smooth bundle QQ. However, we note that

|  |  |  |
| --- | --- | --- |
|  | D¯​(f​q)≠(∂¯​f)​q+f​D¯​q,f∈C∞​(X),q∈Γ⁡(Q),\bar{D}(fq)\neq(\bar{\partial}f)q+f\bar{D}q,\quad f\in C^{\infty}(X),\ q\in\Gamma(Q), |  |

due to the α′ℛ∇\alpha^{\prime}\mathcal{R}\nabla off-diagonal corrections. Thus (Q,D¯)(Q,\bar{D}) is not a holomorphic structure in the traditional sense and the discrepancy occurs at order α′\alpha^{\prime}.

Provided ([2.2](#S2.E2 "In 2 An elliptic complex")) holds, we have D¯2=0\bar{D}^{2}=0 and the differential operator D¯\bar{D} defined in ([2.1](#S2.E1 "In 2 An elliptic complex")) defines a differential complex

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0⟶Γ⁡(Q)​⟶D¯​Ω0,1​(Q)​⟶D¯​Ω0,2​(Q)→⋯.0\longrightarrow\Gamma(Q)\overset{\bar{D}}{\longrightarrow}\Omega^{0,1}(Q)\overset{\bar{D}}{\longrightarrow}\Omega^{0,2}(Q)\rightarrow\cdots\>. |  | (2.3) |

The current paper initiates the study of the cohomology of this complex. In this section, we will show that this complex is elliptic. For this, we must show that for all p∈Xp\in X, then for all ξ∈Tp∗​X\{0}\xi\in T^{\*}\_{p}X\backslash\{0\} then the symbols

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ⁡(D¯,ξ)|p:Ω0,k​(Q)|p→Ω0,k+1​(Q)|p\sigma(\bar{D},\xi)|\_{p}:\Omega^{0,k}(Q)|\_{p}\rightarrow\Omega^{0,k+1}(Q)|\_{p} |  | (2.4) |

have the property

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ker​σ​(D¯,ξ)|p=Im​σ​(D¯,ξ)|p.{\rm Ker}\,\sigma(\bar{D},\xi)|\_{p}={\rm Im}\,\sigma(\bar{D},\xi)|\_{p}\>. |  | (2.5) |

The vector ξ\xi is real, which we write in complex coordinates as ξ=ξμ​d​xμ+ξμ¯​d​xμ¯\xi=\xi\_{\mu}dx^{\mu}+\xi\_{\bar{\mu}}dx^{\bar{\mu}} with ξμ¯=ξμ¯\xi\_{\bar{\mu}}=\overline{\xi\_{\mu}}. The symbol σ⁡(D¯,ξ)\sigma(\bar{D},\xi) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ⁡(D¯,ξ)=[σ⁡(∂¯,ξ)0A⁡(ξ)0σ⁡(∂¯,ξ)000σ⁡(∂¯,ξ)],\sigma(\bar{D},\xi)=\begin{bmatrix}\sigma(\bar{\partial},\xi)&0&A(\xi)\\ 0&\sigma(\bar{\partial},\xi)&0\\ 0&0&\sigma(\bar{\partial},\xi)\end{bmatrix}, |  | (2.6) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ(∂¯,ξ)𝒵=ξμ¯𝒵α​𝒦¯𝓀!d𝓍α⊗d𝓍μ¯∧d𝓍𝒦¯,𝒜(ξ)Δ=−ℛα​μ¯ξσσλΔλ𝒦¯𝓀!d𝓍α⊗d𝓍μ¯∧d𝓍𝒦¯.\sigma(\bar{\partial},\xi)\mathpzc Z=\xi\_{\bar{\mu}}\frac{\mathpzc Z\_{\alpha\bar{K}}}{k!}{\text{d}}x^{\alpha}\otimes{\text{d}}x^{\bar{\mu}}\wedge{\text{d}}x^{\bar{K}},\quad A(\xi)\Delta=-R\_{\alpha\bar{\mu}}{}^{\sigma}{}\_{\lambda}\xi\_{\sigma}\frac{\Delta^{\lambda}{}\_{\bar{K}}}{k!}{\text{d}}x^{\alpha}\otimes{\text{d}}x^{\bar{\mu}}\wedge{\text{d}}x^{\bar{K}}. |  | (2.7) |

Since σ⁡(D¯,ξ)​σ​(D¯,ξ)=0\sigma(\bar{D},\xi)\sigma(\bar{D},\xi)=0, we have Im​σ​(D¯,ξ)|p⊆Ker​σ​(D¯,ξ)|p{\rm Im}\,\sigma(\bar{D},\xi)|\_{p}\subseteq{\rm Ker}\,\sigma(\bar{D},\xi)|\_{p}. To show ellipticity we take q∈Ω0,k​(Q)q\in\Omega^{0,k}(Q) with

|  |  |  |  |
| --- | --- | --- | --- |
|  | q=[𝒵𝔞Δ]∈ker​σ​(D¯,ξ)q=\begin{bmatrix}\mathpzc Z\\ \mathfrak{a}\\ \Delta\end{bmatrix}\in{\rm ker~}\sigma(\bar{D},\xi) |  | (2.8) |

and show q∈Im​σ​(D¯,ξ)|pq\in{\rm Im}\,\sigma(\bar{D},\xi)|\_{p}. Since σ⁡(∂¯,ξ)\sigma(\bar{\partial},\xi) is elliptic, then

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Δ\displaystyle\Delta | =\displaystyle= | σ⁡(∂¯,ξ)​Δ^,Δ^∈Ω0,k−1​(Q)\displaystyle\sigma(\bar{\partial},\xi)\hat{\Delta},\quad\hat{\Delta}\in\Omega^{0,k-1}(Q) |  | (2.9) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | 𝔞\displaystyle\mathfrak{a} | =\displaystyle= | σ⁡(∂¯,ξ)​𝔞^,𝔞^∈Ω0,k−1​(Q).\displaystyle\sigma(\bar{\partial},\xi)\hat{\mathfrak{a}},\quad\hat{\mathfrak{a}}\in\Omega^{0,k-1}(Q). |  | (2.10) |

The constraint σ⁡(D¯,ξ)​q=0\sigma(\bar{D},\xi)q=0 implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | σ⁡(∂¯,ξ)​𝒵+𝒜⁡(ξ)​Δ=0.\sigma(\bar{\partial},\xi)\mathpzc Z+A(\xi)\Delta=0. |  | (2.11) |

This is

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0=σ⁡(∂¯,ξ)​𝒵+𝒜⁡(ξ)​σ​(∂¯,ξ)​Δ^=σ⁡(∂¯,ξ)​(𝒵−𝒜⁡(ξ)​Δ^)0=\sigma(\bar{\partial},\xi)\mathpzc Z+A(\xi)\sigma(\bar{\partial},\xi)\hat{\Delta}=\sigma(\bar{\partial},\xi)(\mathpzc Z-A(\xi)\hat{\Delta}) |  | (2.12) |

since A⁡(ξ)​σ​(∂¯,ξ)=−σ⁡(∂¯,ξ)​A​(ξ)A(\xi)\sigma(\bar{\partial},\xi)=-\sigma(\bar{\partial},\xi)A(\xi). Ellipticity of σ⁡(∂¯,ξ)\sigma(\bar{\partial},\xi) implies

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒵−𝒜⁡(ξ)​Δ^=σ​𝒵^.\mathpzc Z-A(\xi)\hat{\Delta}=\sigma\hat{\mathpzc Z}. |  | (2.13) |

Altogether,

|  |  |  |  |
| --- | --- | --- | --- |
|  | [σ⁡(∂¯,ξ)0A⁡(ξ)0σ⁡(∂¯,ξ)000σ⁡(∂¯,ξ)]​[𝒵^𝔞^Δ^]=[𝒵𝔞Δ]\begin{bmatrix}\sigma(\bar{\partial},\xi)&0&A(\xi)\\ 0&\sigma(\bar{\partial},\xi)&0\\ 0&0&\sigma(\bar{\partial},\xi)\end{bmatrix}\begin{bmatrix}\hat{\mathpzc Z}\\ \hat{\mathfrak{a}}\\ \hat{\Delta}\end{bmatrix}=\begin{bmatrix}\mathpzc Z\\ \mathfrak{a}\\ \Delta\end{bmatrix} |  | (2.14) |

as desired.

From the elliptic complex ([2.3](#S2.E3 "In 2 An elliptic complex")), we can define the cohomology groups

|  |  |  |  |
| --- | --- | --- | --- |
|  | HD¯0,q(Q)=Ker(D¯:Ω0,q(Q)→Ω0,q+1(Q))Im(D¯:Ω0,q−1(Q)→Ωq,0(Q)).H^{0,q}\_{\bar{D}}(Q)=\frac{{\rm Ker}\,(\bar{D}:\Omega^{0,q}(Q)\rightarrow\Omega^{0,q+1}(Q))}{{\rm Im}\,(\bar{D}:\Omega^{0,q-1}(Q)\rightarrow\Omega^{q,0}(Q))}. |  | (2.15) |

On the space Ω0,q​(Q)\Omega^{0,q}(Q), we may introduce the L2L^{2} inner product:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | g⁡(q1,q2)\displaystyle g(q\_{1},q\_{2}) | =\displaystyle= | ∫X14​gμ​ν¯​(𝒵1)μ⋆(𝒵2)ν¯−α‵4​Tr​(𝔞1⋆𝔞2†)+ℊμ​ν¯​Δ1μ⋆Δ2ν¯\displaystyle\int\_{X}\frac{1}{4}g^{\mu\bar{\nu}}(\mathpzc Z\_{1})\_{\mu}\star\overline{(\mathpzc Z\_{2})\_{\nu}}-\frac{{\alpha^{\backprime}\,}}{4}{\rm Tr}\,(\mathfrak{a}\_{1}\star\mathfrak{a}\_{2}^{\dagger})+g\_{\mu\bar{\nu}}\Delta\_{1}^{\mu}\star\overline{\Delta\_{2}^{\nu}} |  | (2.16) |
|  |  |  | +α′2∫XRμ¯​ρ​σ​ν¯((−1)q+114(𝒵1)ρ​μ¯⋆(𝒵2)¯σ​ν¯+(−1)𝓆(Δ1)μ¯​ν¯(Δ2)¯ρ​σ),\displaystyle+\frac{\alpha^{\prime}}{2}\int\_{X}R^{\bar{\mu}\rho\sigma\bar{\nu}}\bigg((-1)^{q+1}\frac{1}{4}(\mathpzc Z\_{1})\_{\rho\bar{\mu}}\star\overline{(\mathpzc Z\_{2})}\_{\sigma\bar{\nu}}+(-1)^{q}(\Delta\_{1})\_{\bar{\mu}\bar{\nu}}\overline{(\Delta\_{2})}\_{\rho\sigma}\bigg)\>, |  |

where, to correct to first order in α′\alpha^{\prime} the curvature RR in the last line is the Riemann curvature. When q=0q=0, the inner product does not include the last line. These α′\alpha^{\prime}-corrections on the last line are derived from the moduli space metric on the heterotic moduli space and are due to [[12](#bib.bib12), [26](#bib.bib26), [10](#bib.bib10)]. For α′\alpha^{\prime} small enough, the expression defines a positive-definite L2L^{2} inner product.

This inner product allows us to define the adjoint operator

|  |  |  |  |
| --- | --- | --- | --- |
|  | D¯†:Ω0,q​(Q)→Ω0,q−1​(Q),\bar{D}^{\dagger}:\Omega^{0,q}(Q)\rightarrow\Omega^{0,q-1}(Q)\>, |  | (2.17) |

and form the Laplacian

|  |  |  |  |
| --- | --- | --- | --- |
|  | □=D¯†​D¯+D¯​D¯†.\Box=\bar{D}^{\dagger}\bar{D}+\bar{D}\bar{D}^{\dagger}\>. |  | (2.18) |

Since the complex is elliptic, we obtain finite dimensional spaces of harmonic forms.

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℋq(Q)=Ker(□:Ω0,q(Q)→Ω0,q+1(Q)).\mathcal{H}^{q}(Q)={\rm Ker}\,(\Box:\Omega^{0,q}(Q)\rightarrow\Omega^{0,q+1}(Q))\>. |  | (2.19) |

The significance of these spaces is that the analysis in [[10](#bib.bib10)] shows that ℋ1​(Q)\mathcal{H}^{1}(Q) parametrizes the heterotic moduli. By the Hodge theorem for elliptic complexes (see e.g. [[35](#bib.bib35)]), we conclude

|  |  |  |  |
| --- | --- | --- | --- |
|  | dimℋ1​(Q)=dimHD¯0,1​(Q),\dim\mathcal{H}^{1}(Q)=\dim H\_{\bar{D}}^{0,1}(Q)\>, |  | (2.20) |

and this space is finite dimensional by ellipticity of the complex. This correspondence allows us to use methods from homological algebra to compute dimℋ1​(Q)\dim\mathcal{H}^{1}(Q). We give an application of this method to the standard embedding in the following section.

## 3 The standard embedding

We now compute the cohomology HD¯0,1​(Q)H\_{\bar{D}}^{0,1}(Q) for the particular example of the standard embedding. The standard embedding [[1](#bib.bib1)], was the first consistent string compactification. It was constructed with a view to building a theory that incorporated the standard model and gravity. It is defined by taking XX to be a CY manifold and embedding the spin connection, an S​U​(3)SU(3) connection, in the E8×E8E\_{8}\times E\_{8} gauge bundle. The E8×E8E\_{8}\times E\_{8} is Higgsed to E6×E8E\_{6}\times E\_{8} and so as the connection takes values in the adjoint representation 𝟐𝟒𝟖{{\boldsymbol{248}}} of E8E\_{8}, it decomposes under S​U​(3)×E6⊂E8SU(3)\times E\_{6}\subset E\_{8} as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟐𝟒𝟖=(𝟑,𝟐𝟕)⊕(𝟑¯,𝟐𝟕¯)⊕(𝟏,𝟕𝟖)⊕(𝟖,𝟏),{{\boldsymbol{248}}}\;=\;({{\boldsymbol{3}}},{{\boldsymbol{27}}})\oplus({{\overline{\boldsymbol{3}}}},{{\overline{\boldsymbol{27}}}})\oplus({{\boldsymbol{1}}},{{\boldsymbol{78}}})\oplus({{\boldsymbol{8}}},{{\boldsymbol{1}}})~, |  | (3.1) |

where the 𝟕𝟖{{\boldsymbol{78}}} and 𝟖{{\boldsymbol{8}}} are the adjoint representation of E6E\_{6} and S​U​(3)SU(3) respectively, and 𝟐𝟕{{\boldsymbol{27}}} and 𝟑{{\boldsymbol{3}}} are their respective fundamental representation with their respective conjugates 𝟑¯{{\overline{\boldsymbol{3}}}} and 𝟐𝟕¯{{\overline{\boldsymbol{27}}}}. See any of the canonical texts such as [[36](#bib.bib36)] for more details. For the moduli analysis we are only interested in the S​U​(3)SU(3) adjoint representation, which are singlets under the external E6×E8E\_{6}\times E\_{8} gauge symmetry.

Analysing simultaneous deformations of the gauge connection and the complex structure leads to potential obstructions of the complex structure moduli. This is because not all complex structure deformations need preserve the bundle remains holomorphic, as required by supersymmetry. This was first observed by Atiyah [[17](#bib.bib17)], and applied to the study of heterotic moduli in [[18](#bib.bib18), [19](#bib.bib19), [20](#bib.bib20)]. Specifically, the deformations should satisfy the equation

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δμ​Fμ​ν¯​d​xν¯=∂¯𝒜​𝔞,\Delta^{\mu}F\_{\mu{\overline{\nu}}}{\text{d}}x^{\overline{\nu}}\;=\;{\overline{\partial}}\_{\mathcal{A}}\mathfrak{a}~, |  | (3.2) |

where F=d​A+A2F={\text{d}}A+A^{2}, 𝒜=A(0,1)\mathcal{A}=A^{(0,1)}, Δ∈H0,1​(T(1,0))\Delta\in H^{0,1}(T^{(1,0)}) is the complex structure deformation, 𝔞=δ​𝒜∈Ω0,1​(End0​(V))\mathfrak{a}=\delta\mathcal{A}\in\Omega^{0,1}({\rm End}\_{0}(V)) is the deformation of the gauge connection. This can be rephrased as requiring that the simultaneous deformations (𝔞,Δ)(\mathfrak{a},\Delta) be in the kernel of

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂¯1=(∂¯𝒜ℱ0∂¯),ℱ⁡(Δ)=Fμ​ν¯​d​xν¯∧Δμ{\overline{\partial}}\_{1}=\begin{pmatrix}{\overline{\partial}}\_{\mathcal{A}}&\mathcal{F}\\ 0&{\overline{\partial}}\end{pmatrix}~,\quad\quad\mathcal{F}(\Delta)=F\_{\mu\bar{\nu}}{\text{d}}x^{\bar{\nu}}\wedge\Delta^{\mu} |  | (3.3) |

acting on sections of the complex vector bundle Q1=End0​(V)⊕T(1,0)​XQ\_{1}={\rm End}\_{0}(V)\oplus T^{(1,0)}X. Here ℱ\mathcal{F} is the extension map given by the curvature FF, often called the Atiyah map. The operator ∂¯1\bar{\partial}\_{1} defines a holomorphic structure (Q1,∂¯1)(Q\_{1},\bar{\partial}\_{1}) and forms the differential of the central complex of the Atiyah sequence

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0→Ω0,q​(End0​(V))→𝜄Ω∂¯10,q​(Q1)→𝑝Ω0,q​(T(1,0)​X)→0.0\rightarrow\Omega^{0,q}({\rm End}\_{0}(V))\xrightarrow{\iota}\Omega\_{{\overline{\partial}}\_{1}}^{0,q}(Q\_{1})\xrightarrow{p}\Omega^{0,q}(T^{(1,0)}X)\rightarrow 0~. |  | (3.4) |

The short exact sequence gives a long exact sequence in cohomology

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0→H0,1​(End0​(V))→H0,1​(Q1)→H0,1​(T(1,0)​X)→ℱH0,2​(End0​(V))→⋯,0\rightarrow\>H^{0,1}({\rm End}\_{0}(V))\rightarrow H^{0,1}(Q\_{1})\rightarrow H^{0,1}(T^{(1,0)}X)\xrightarrow{\mathcal{F}}H^{0,2}({\rm End}\_{0}(V))\rightarrow\cdots~, |  | (3.5) |

where the sequence begins at level one as the holomorphic tangent bundle of a simply connected Kähler Calabi-Yau manifold has no holomorphic sections. The snake lemma gives us that the connecting homomorphism ℱ\mathcal{F} is the induced map on cohomology coming from ℱ:Ω0,q​(T(1,0)​X)→Ω0,q+1​(End0​(V))\mathcal{F}:\Omega^{0,q}(T^{(1,0)}X)\rightarrow\Omega^{0,q+1}({\rm End}\_{0}(V)) in the ∂¯1\bar{\partial}\_{1} operator given above.

Using the properties of exact sequences, one gets:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H0,1​(Q1)≅H0,1​(End0​(V))⊕ker​ℱ,H^{0,1}(Q\_{1})\cong H^{0,1}({\rm End}\_{0}(V))\oplus{\rm ker~}\mathcal{F}~, |  | (3.6) |

where ker​ℱ⊆H1​(T(1,0)​X){\rm ker~}\mathcal{F}\subseteq H^{1}(T^{(1,0)}X), but does not span this space in general, reflecting the fact that some complex structure moduli are obstructed.

However, in the case of the standard embedding, the extension map ℱ\mathcal{F} is trivial and the long exact sequence splits. To see this, note that the curvature FF is in this case given by the Riemann curvature RR of the Calabi-Yau. Equation ([3.2](#S3.E2 "In 3 The standard embedding")) then takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | dxμ¯Rμ¯​νστ∧Δν=∂¯𝒜𝔞στ.{\text{d}}x^{\overline{\mu}}R\_{{\overline{\mu}}\nu}{}^{\sigma}{}\_{\tau}{\,\wedge\,}\Delta^{\nu}\;=\;{\overline{\partial}}\_{\mathcal{A}}\mathfrak{a}^{\sigma}{}\_{\tau}~. |  | (3.7) |

Let us postulate the following form of α\alpha

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝔞στ=∇τΔσ+𝔞0στ,\mathfrak{a}^{\sigma}{}\_{\tau}\;=\;\nabla\_{\tau}\Delta^{\sigma}+\mathfrak{a}\_{0}^{\sigma}{}\_{\tau}~, |  | (3.8) |

where we take ∂¯𝒜𝔞0στ=0{\overline{\partial}}\_{\mathcal{A}}\mathfrak{a}\_{0}^{\sigma}{}\_{\tau}=0, so that [𝔞]∈H0,1​(End0​(V))[\mathfrak{a}]\in H^{0,1}({\rm End}\_{0}(V)) corresponds to a bundle modulus. These are deformations of the gauge bundle which can deform the geometry away from the standard embedding. Using the expression for 𝔞στ\mathfrak{a}^{\sigma}{}\_{\tau}, we see that

|  |  |  |
| --- | --- | --- |
|  | ∂¯𝒜𝔞στ=∂¯𝒜(∇σΔτ+𝔞0στ)=[∂¯𝒜,∇τ]​Δσ=dxμ¯Rμ¯​τσρ∧Δρ=dxμ¯Rμ¯​ρστ∧Δρ,\begin{split}{\overline{\partial}}\_{\mathcal{A}}\mathfrak{a}^{\sigma}{}\_{\tau}&\;=\;{\overline{\partial}}\_{\mathcal{A}}(\nabla\_{\sigma}\Delta^{\tau}+{\mathfrak{a}\_{0}}^{\sigma}{}\_{\tau})\\ &\;=\;[{\overline{\partial}}\_{\mathcal{A}},\nabla\_{\tau}]\Delta^{\sigma}\\ &\;=\;{\text{d}}x^{\overline{\mu}}R\_{{\overline{\mu}}\tau}{}^{\sigma}{}\_{\rho}\wedge\Delta^{\rho}\;=\;{\text{d}}x^{\overline{\mu}}R\_{{\overline{\mu}}\rho}{}^{\sigma}{}\_{\tau}\wedge\Delta^{\rho}~,\\ \end{split} |  |

where we used symmetries of the Riemann curvature on Kähler manifold. This demonstrates that ([3.2](#S3.E2 "In 3 The standard embedding")) can always be solved about the standard embedding. Moreover, we have an explicit expression for 𝔞\mathfrak{a} which we will use below. It follows that the Atiyah extension map ℱ{\cal F} is trivial, so that ker​ℱ=H0,1​(T(1,0)​X){\rm ker~}\mathcal{F}=H^{0,1}(T^{(1,0)}X) and

|  |  |  |
| --- | --- | --- |
|  | H0,1​(Q1)≅H0,1​(End0​(V))⊕H0,1​(T(1,0)​X),H^{0,1}(Q\_{1})\cong H^{0,1}({\rm End}\_{0}(V))\oplus H^{0,1}(T^{(1,0)}X)~, |  |

which counts the simultaneous deformations of the complex structure and bundle at the standard embedding.

Solutions of heterotic supergravity are also requred to satisfy the heterotic anomaly cancellation condition

|  |  |  |  |
| --- | --- | --- | --- |
|  | i(∂−∂¯)ω=dB−α′4(CS(A)−CS(∇)),i({\partial}-{\overline{\partial}})\omega={\text{d}}B-\frac{\alpha^{\prime}}{4}\left({\text{CS}}(A)-{\text{CS}}(\nabla)\right)~,\\ |  | (3.9) |

where ω\omega is the hermitian two-form on XX, and ∇\nabla is a connection on the tangent bundle. This connection is the Levi-Civita connection at the standard embedding, where it is identified with AA. With ω\omega being Kähler, and d​B=0{\text{d}}B=0, ([3.9](#S3.E9 "In 3 The standard embedding")) is trivially satisfied at this locus. In [[10](#bib.bib10)] it was shown that for simultaneous deformations of the geometry and bundle (𝒵,𝔞,Δ)(\mathpzc Z,\mathfrak{a},\Delta), where 𝒵\mathpzc Z denotes complexified hermitian deformations, to also satisfy anomaly cancellation, they must be in the kernel of the differential ([2.1](#S2.E1 "In 2 An elliptic complex")) given above, which we can also write as

|  |  |  |
| --- | --- | --- |
|  | D¯=(∂¯ℋ0∂¯1).\bar{D}=\begin{pmatrix}{\overline{\partial}}&\mathcal{H}\\ 0&{\overline{\partial}}\_{1}\end{pmatrix}~. |  |

Here the extension map ℋ\cal H is determined by the anomaly cancellation. At the standard embedding, the expression ([2.1](#S2.E1 "In 2 An elliptic complex")) becomes

|  |  |  |
| --- | --- | --- |
|  | D¯=(∂¯ℱ∗R⋅∇0∂¯𝒜ℱ00∂¯),\bar{D}=\begin{pmatrix}{\overline{\partial}}&\mathcal{F}^{\*}&\>R\cdot\nabla\\ 0&{\overline{\partial}}\_{\mathcal{A}}&\mathcal{F}\\ 0&0&{\overline{\partial}}\end{pmatrix}~, |  |

acting on Q=T∗(1,0)​X⊕Q1Q=T^{\*(1,0)}X\oplus Q\_{1}. This time (Q,D¯)(Q,\bar{D}) is not a holomorphic structure, however this operator is still the differential of the middle part of a short exact sequence of differential modules

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0→Ω0,p​(T∗(1,0)​X)→𝜄ΩD¯0,p​(Q)→𝑝Ω0,p​(Q1)→0.0\rightarrow\Omega^{0,p}(T^{\*(1,0)}X)\xrightarrow{\iota}\Omega^{0,p}\_{\bar{D}}(Q)\xrightarrow{p}\Omega^{0,p}(Q\_{1})\rightarrow 0~. |  | (3.10) |

As mentioned above, the infinitesimal deformations of the system are counted by HD¯0,1​(Q)H^{0,1}\_{\bar{D}}(Q). The short exact sequence creates a long exact sequence in cohomology

|  |  |  |  |
| --- | --- | --- | --- |
|  | 0→H0,1​(T∗(1,0)​X)→H0,1​(Q)→H0,1​(Q1)→ℋH0,2​(T∗(1,0)​X)→⋯.0\rightarrow H^{0,1}(T^{\*(1,0)}X)\rightarrow H^{0,1}(Q)\rightarrow H^{0,1}(Q\_{1})\xrightarrow{\mathcal{H}}H^{0,2}(T^{\*(1,0)}X)\rightarrow\cdots~. |  | (3.11) |

Again, the snake lemma identifies the connecting homomorphism ℋ\mathcal{H} as induced by D¯\bar{D} and the sequence begins at level one as at the standard embedding H0​(End0​(V))=H0​(End0​(T​X))=0H^{0}({\rm End}\_{0}(V))=H^{0}({\rm End}\_{0}(TX))=0, which also implies H0​(Q1)=0H^{0}(Q\_{1})=0. Using exactness, we can deduce that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H0,1​(Q)≅H0,1​(T∗(1,0)​X)⊕ker⁡(ℋ),H^{0,1}(Q)\cong H^{0,1}(T^{\*(1,0)}X)\oplus{\rm ker~}(\mathcal{H})~, |  | (3.12) |

where ker⁡(ℋ)⊆H1,0​(Q1){\rm ker~}(\mathcal{H})\subseteq H^{1,0}(Q\_{1}) are the complex structure and bundle deformations satisfying anomaly cancellation.

We want to show that the extension map ℋ\cal H is trivial at the standard embedding. To do so, note again that F=RF=R in this case. For (𝒵,𝔞,Δ)(\mathpzc Z,\mathfrak{a},\Delta) to be in the kernel of D¯\bar{D} implies the following schematic equations

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂¯​𝒵+ℋ⁡(Δ,𝔞)=∂¯​𝒵+ℛ∗​𝔞+ℛ⋅∇Δ\displaystyle{\overline{\partial}}\mathpzc Z+\mathcal{H}(\Delta,\mathfrak{a})={\overline{\partial}}\mathpzc Z+R^{\*}\mathfrak{a}+R\cdot\nabla\Delta | =0\displaystyle=0 |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂¯𝒜​𝔞+R​Δ\displaystyle{\overline{\partial}}\_{\mathcal{A}}\mathfrak{a}+R\Delta | =0\displaystyle=0 |  | (3.13) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂¯​Δ\displaystyle{\overline{\partial}}\Delta | =0.\displaystyle=0~. |  | (3.14) |

The last two equations are the conditions to be in the kernel of ∂¯1{\overline{\partial}}\_{1}, while the first equation written out is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂¯𝒵+ℋ(Δ,𝔞)=∂¯𝒵−α‵2Tr(ℱ∧𝔞)+α‵2ℛσ∇στΔτ= 0.{\overline{\partial}}\mathpzc Z+\mathcal{H}(\Delta,\mathfrak{a})={\overline{\partial}}\mathpzc Z-\frac{{\alpha^{\backprime}\,}}{2}\text{Tr}\thinspace(F\wedge\mathfrak{a})+\frac{{\alpha^{\backprime}\,}}{2}R^{\sigma}{}\_{\tau}\nabla\_{\sigma}\Delta^{\tau}\;=\;0~. |  | (3.15) |

For ℋ\cal H to be trivial, we must show that any pair (𝔞,Δ)(\mathfrak{a},\Delta) in the kernel of ∂¯1{\overline{\partial}}\_{1} satisfies this equation. Consider 𝔞\mathfrak{a} as in ([3.8](#S3.E8 "In 3 The standard embedding")). Taking R=FR=F, the above equation can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂¯​𝒵=α‵2Rστ(∇σΔτ+𝔞0τσ)−α‵2Rστ∇σΔτ=α‵2Rστ∇σΔτ+α‵2Rστ𝔞0τσ−α‵2Rστ∇σΔτ=α‵2Rστ𝔞0τσ.\begin{split}{\overline{\partial}}\mathpzc Z&\;=\;\frac{{\alpha^{\backprime}\,}}{2}R^{\sigma}{}\_{\tau}(\nabla\_{\sigma}\Delta^{\tau}+{\mathfrak{a}\_{0}}^{\tau}{}\_{\sigma})-\frac{{\alpha^{\backprime}\,}}{2}R^{\sigma}{}\_{\tau}\nabla\_{\sigma}\Delta^{\tau}\\ &\;=\;\frac{{\alpha^{\backprime}\,}}{2}R^{\sigma}{}\_{\tau}\>\nabla\_{\sigma}\Delta^{\tau}+\frac{{\alpha^{\backprime}\,}}{2}R^{\sigma}{}\_{\tau}\>{\mathfrak{a}\_{0}}^{\tau}{}\_{\sigma}-\frac{{\alpha^{\backprime}\,}}{2}R^{\sigma}{}\_{\tau}\nabla\_{\sigma}\Delta^{\tau}\;=\;\frac{{\alpha^{\backprime}\,}}{2}R^{\sigma}\_{\tau}\>{\mathfrak{a}\_{0}}^{\tau}{}\_{\sigma}~.\end{split} |  | (3.16) |

What this shows is that we need to demonstrate the last term is trivial in cohomology for any [𝔞0]∈H0,1​(End0​(V))[\mathfrak{a}\_{0}]\in H^{0,1}({\rm End}\_{0}(V)). We do this now.

Our strategy is to take the inner product with a generic harmonic form χ¯∈ℋ(1,2)\bar{\chi}\in\mathcal{H}^{(1,2)}. If the inner product is zero then Rστ𝔞0τσR^{\sigma}{}\_{\tau}{\mathfrak{a}\_{0}}^{\tau}{}\_{\sigma} is ∂¯{\overline{\partial}} exact which follows from the orthogonal decomposition of forms in the Hodge decomposition theorem. Consider

|  |  |  |
| --- | --- | --- |
|  | ⟨Rσ𝔞0ττ,σχ¯⟩=∫Rσ𝔞0ττ∧σ⋆χ,\langle R^{\sigma}{}\_{\tau}{\mathfrak{a}\_{0}}^{\tau}{}\_{\sigma},\bar{\chi}\rangle=\int R^{\sigma}{}\_{\tau}\,\mathfrak{a}\_{0}^{\tau}\>{}\_{\sigma}\wedge\star\chi~, |  |

where ∗χ\*\chi is a harmonic (2,1)(2,1)-form, which can be written as

|  |  |  |
| --- | --- | --- |
|  | ⋆χ=12​Δ~μ​Ωμ​ν​λ​d​xν​λ,\star\chi=\frac{1}{2}\widetilde{\Delta}^{\mu}\>\Omega\_{\mu\nu\lambda}{\text{d}}x^{\nu\lambda}~, |  |

where Δ~∈ℋ(0,1)​(T(1,0))\widetilde{\Delta}\in\mathcal{H}^{(0,1)}(T^{(1,0)}). The inner product becomes

|  |  |  |
| --- | --- | --- |
|  | ⟨Rσ𝔞0ττ,σχ¯⟩=12∫Tr(R∧𝔞0)∧Δ~μ∧Ωμ​ν​λdxν​λ.\langle R^{\sigma}{}\_{\tau}\,{\mathfrak{a}\_{0}}^{\tau}{}\_{\sigma},\bar{\chi}\rangle=\frac{1}{2}\int\text{Tr}\thinspace(R\wedge\mathfrak{a}\_{0})\>\wedge\>\widetilde{\Delta}^{\mu}\>\wedge\>\Omega\_{\mu\nu\lambda}{\text{d}}x^{\nu\lambda}\>. |  |

Next, note that the total anti-symmetrisation of four holomorphic indecies vanishes, so that

|  |  |  |
| --- | --- | --- |
|  | 0=R[ξΩμνλ]dzν​λ​ξ=14(3RξΩμ​ν​λ−RμΩξ​ν​λ)dxν​λ​ξ.0=R\_{[\xi}\Omega\_{\mu\nu\lambda]}dz^{\nu\lambda\xi}=\frac{1}{4}(3\>R\_{\xi}\Omega\_{\mu\nu\lambda}-R\_{\mu}\Omega\_{\xi\nu\lambda}){\text{d}}x^{\nu\lambda\xi}~. |  |

Using this, we find

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨Rσ𝔞0ττ,σχ¯⟩=∫tr(Rμ∧𝔞0)∧Δ~μ∧Ω.\langle R^{\sigma}{}\_{\tau}\,{\mathfrak{a}\_{0}}^{\tau}{}\_{\sigma},\bar{\chi}\rangle=\int tr(R\_{\mu}\wedge\mathfrak{a}\_{0})\wedge\widetilde{\Delta}^{\mu}\wedge\Omega\>. |  | (3.17) |

But we already know that Rμ​Δ~μ=∂¯𝒜R\_{\mu}\widetilde{\Delta}^{\mu}={\overline{\partial}}\_{\mathcal{A}}-exact, as Δ~μ\widetilde{\Delta}^{\mu} corresponds to a complex structure deformation. It follows that the inner product vanishes. We therefore conclude that ℋ\mathcal{H} is trivial as a map in cohomology, that is

|  |  |  |  |
| --- | --- | --- | --- |
|  | ker​ℋ=H0,1​(Q1)≅H0,1​(T(1,0))⊕H0,1​(End0​(V)).{\rm ker~}{\mathcal{H}}=H^{0,1}(Q\_{1})\cong H^{0,1}(T^{(1,0)})\oplus H^{0,1}({\rm End}\_{0}(V))~. |  | (3.18) |

Therefore,

|  |  |  |  |
| --- | --- | --- | --- |
|  | H0,1​(Q)≅H0,1​(T∗(1,0)​X)⊕H0,1​(End0​(V))⊕H0,1​(T(1,0)​X).H^{0,1}(Q)\cong H^{0,1}(T^{\*(1,0)}X)\oplus H^{0,1}({\rm End}\_{0}(V))\oplus H^{0,1}(T^{(1,0)}X)~. |  | (3.19) |

This proves that in the standard embedding, the total heterotic moduli are given by, Kähler moduli H1,1H^{1,1}, complex structure moduli H2,1H^{2,1}, and bundle moduli H0,1​(End0​(V))H^{0,1}({\rm End}\_{0}(V)), as claimed in the literature.

## 4 The index of the complex and obstructions

As mentioned above, it was shown in [[10](#bib.bib10)] that, to first order in α′\alpha^{\prime}, HD¯(0,1)​(Q)H^{(0,1)}\_{\bar{D}}(Q) computes the infinitesimal spectrum of six-dimensional heterotic solutions. Though not yet demonstrated, it is expected that HD¯(0,2)​(Q)H^{(0,2)}\_{\bar{D}}(Q) will parameterise the obstruction space for the given deformations. If this space has the same dimension as the infinitesimal moduli space the deformation problem is said to have expected or "virtual" dimension zero, meaning the expected moduli space is a set of points. This is interesting not only from the point of view of physics and the string theory moduli problem, but also mathematically in the context of enumerative geometry, invariant theory, and perfect obstruction theories [[37](#bib.bib37), [38](#bib.bib38)]. In this section we demonstrate that, given some physically motivated assumptions, HD¯(0,1)​(Q)≅HD¯(0,2)​(Q)H^{(0,1)}\_{\bar{D}}(Q)\cong H^{(0,2)}\_{\bar{D}}(Q) and so in the case at hand the space of deformations does have virtual dimension zero. The argument is the "simplified case" version of a more general argument found in [[32](#bib.bib32)], where the physically motivated assumptions are omitted.

We let XX be a compact complex manifold of dimension 3 with nowhere vanishing holomorphic volume form Ω\Omega satisfying

|  |  |  |  |
| --- | --- | --- | --- |
|  | H0​(T(1,0)​X)=0.H^{0}(T^{(1,0)}X)=0\>. |  | (4.1) |

Let V→XV\rightarrow X be a holomorphic vector bundle with

|  |  |  |  |
| --- | --- | --- | --- |
|  | H0​(End0​(V))=0.H^{0}({\rm End}\_{0}(V))=0\>. |  | (4.2) |

For example, we may take VV to be a stable bundle since these do not admit holomorphic endomorphisms. In this section we will show that in this setup, then

|  |  |  |  |
| --- | --- | --- | --- |
|  | dimHD¯0,1​(Q)=dimHD¯0,2​(Q),\dim H^{0,1}\_{\bar{D}}(Q)=\dim H^{0,2}\_{\bar{D}}(Q)\>, |  | (4.3) |

where HD¯0,q​(Q)H^{0,q}\_{\bar{D}}(Q) refers to the cohomology of the complex ([2.3](#S2.E3 "In 2 An elliptic complex")). By comparing the zeroth and third order cohomology, we will also see that

|  |  |  |  |
| --- | --- | --- | --- |
|  | χ⁡(X,D¯):=∑k=03(−1)k​dimHD¯0,k​(Q)=0,\chi(X,\bar{D}):=\sum\_{k=0}^{3}(-1)^{k}\dim H^{0,k}\_{\bar{D}}(Q)=0\>, |  | (4.4) |

and so the Euler characteristic of the complex vanishes.

Remark: We make a few remarks about the assumption ([4.1](#S4.E1 "In 4 The index of the complex and obstructions")). First, we note that the standard isomorphisms

|  |  |  |  |
| --- | --- | --- | --- |
|  | H0​(T(1,0)​X)≅H3,0​(T(1,0)​X)≅H0,3​(T∗(1,0)​X)∗H^{0}(T^{(1,0)}X)\cong H^{3,0}(T^{(1,0)}X)\cong H^{0,3}(T^{\*(1,0)}X)^{\*} |  | (4.5) |

hold in the non-Kähler setting by the existence of a holomorphic top form Ω\Omega and Serre duality. If XX is a Kähler Calabi-Yau threefold with dimH1​(X,R)=0\dim H^{1}(X,\mathbb{R})=0, then

|  |  |  |
| --- | --- | --- |
|  | dimH0​(T(1,0)​X)=h1,3​(X)=h3,1​(X)=h0,1​(X)=0,\dim H^{0}(T^{(1,0)}X)=h^{1,3}(X)=h^{3,1}(X)=h^{0,1}(X)=0\>, |  |

and so assumption ([4.1](#S4.E1 "In 4 The index of the complex and obstructions")) is valid for Kähler threefolds. The argument above does not go through for non-Kähler manifolds, as it uses the Kähler properties h1,3=h3,1h^{1,3}=h^{3,1} and h0,1≤dimH1​(X,R)h^{0,1}\leq\dim H^{1}(X,\mathbb{R}).

Nevertheless, we note that ([4.1](#S4.E1 "In 4 The index of the complex and obstructions")) is a natural assumption in the context of non-Kähler conifold transitions. If one considers the web of all complex manifolds connected to Kähler Calabi-Yau threefolds by conifold transition, then some of these objects may not support any Kähler metric, however the condition ([4.1](#S4.E1 "In 4 The index of the complex and obstructions")) still holds through conifold transitions. This is because after a contraction and smoothing X→X0↝XtX\rightarrow X\_{0}\rightsquigarrow X\_{t}, if infinitely many XtX\_{t} have H0​(T(1,0)​Xt)≠0H^{0}(T^{(1,0)}X\_{t})\neq 0 then after normalization one can take a limit of these holomorphic vector fields and obtain a non-zero vector field W∈H0​(T(1,0)​X0,reg)W\in H^{0}(T^{(1,0)}X\_{0,{\rm reg}}) which extends by Hartog’s theorem to a holomorphic vector field W∈H0​(T(1,0)​X)W\in H^{0}(T^{(1,0)}X). But since XX is a simply connected Kähler threefold, such a WW does not exist. It follows that for small tt, the deformed non-Kähler object XtX\_{t} still satisfies ([4.1](#S4.E1 "In 4 The index of the complex and obstructions")). For further discussion on conifold transitions, see e.g. [[39](#bib.bib39), [40](#bib.bib40), [41](#bib.bib41), [42](#bib.bib42), [43](#bib.bib43), [44](#bib.bib44), [45](#bib.bib45), [46](#bib.bib46), [47](#bib.bib47), [48](#bib.bib48), [49](#bib.bib49)] and references therein.

We now prove ([4.3](#S4.E3 "In 4 The index of the complex and obstructions")). To shorten the notation a bit, let us write T=T(1,0)​XT=T^{(1,0)}X and H1​(Q)=HD¯0,1​(Q)H^{1}(Q)=H^{0,1}\_{\bar{D}}(Q). The long exact sequence ([3.11](#S3.E11 "In 3 The standard embedding")) gives

|  |  |  |
| --- | --- | --- |
|  | 0→H1​(T∗)→H1​(Q)→H1​(Q1)→ℋH2​(T∗)→H2​(Q)→H2​(Q1)→0.0\rightarrow H^{1}(T^{\*})\rightarrow H^{1}(Q)\rightarrow H^{1}(Q\_{1})\xrightarrow{\mathcal{H}}H^{2}(T^{\*})\rightarrow H^{2}(Q)\rightarrow H^{2}(Q\_{1})\rightarrow 0\>. |  |

since ([4.5](#S4.E5 "In 4 The index of the complex and obstructions")) and ([4.1](#S4.E1 "In 4 The index of the complex and obstructions")) imply H0,3​(T∗(1,0)​X)=0H^{0,3}(T^{\*(1,0)}X)=0, and H0​(Q1)=0H^{0}(Q\_{1})=0 holds by ([4.1](#S4.E1 "In 4 The index of the complex and obstructions")), ([4.2](#S4.E2 "In 4 The index of the complex and obstructions")). We conclude

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | h1​(Q)\displaystyle h^{1}(Q) | =\displaystyle= | h1​(T∗)+dimker​ℋ,\displaystyle h^{1}(T^{\*})+\dim{\rm ker~}\mathcal{H}\>, |  | (4.6) |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | h2​(Q)\displaystyle h^{2}(Q) | =\displaystyle= | h2​(Q1)+h2​(T∗)−dimIm ​ℋ.\displaystyle h^{2}(Q\_{1})+h^{2}(T^{\*})-\dim\text{Im~}\mathcal{H}\>. |  | (4.7) |

where h1​(Q)=dimH1​(Q)h^{1}(Q)=\dim H^{1}(Q). We can apply the same analysis to the long exact sequence ([3.5](#S3.E5 "In 3 The standard embedding")) for Q1Q\_{1}, which gives

|  |  |  |
| --- | --- | --- |
|  | 0→H1​(End0​(V))→H1​(Q1)→H1​(T)→ℱH2​(End0​(V))→H2​(Q1)→H1​(T)→00\rightarrow\>H^{1}({\rm End}\_{0}(V))\rightarrow H^{1}(Q\_{1})\rightarrow H^{1}(T)\xrightarrow{\mathcal{F}}H^{2}({\rm End}\_{0}(V))\rightarrow H^{2}(Q\_{1})\rightarrow H^{1}(T)\rightarrow 0 |  |

since H0,3​(End0​(V))=0H^{0,3}({\rm End}\_{0}(V))=0 by ([4.2](#S4.E2 "In 4 The index of the complex and obstructions")) and Serre duality, and so we can conclude

|  |  |  |  |
| --- | --- | --- | --- |
|  | h2​(Q1)=h2​(T)+h2​(End0​(V))−dimIm ​ℱ.h^{2}(Q\_{1})=h^{2}(T)+h^{2}({\rm End}\_{0}(V))-\dim\text{Im~}\mathcal{F}\>. |  | (4.8) |

Combining ([4.7](#S4.E7 "In 4 The index of the complex and obstructions")) and ([4.8](#S4.E8 "In 4 The index of the complex and obstructions")) gives

|  |  |  |
| --- | --- | --- |
|  | h2​(Q)=h2​(T)+h2​(End0​(V))+h2​(T∗)−dimIm ​ℱ−dimIm ​ℋ.h^{2}(Q)=h^{2}(T)+h^{2}({\rm End}\_{0}(V))+h^{2}(T^{\*})-\dim\text{Im~}\mathcal{F}-\dim\text{Im~}\mathcal{H}\>. |  |

Using the holomorphic volume form and Serre duality gives

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h2​(T)\displaystyle h^{2}(T) | =\displaystyle= | h2,2=h1,1=h1​(T∗),\displaystyle h^{2,2}=h^{1,1}=h^{1}(T^{\*})\>, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | h2​(T∗)\displaystyle h^{2}(T^{\*}) | =\displaystyle= | h1,2=h2,1=h1​(T),\displaystyle h^{1,2}=h^{2,1}=h^{1}(T)\>, |  |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | h2​(End0​(V))\displaystyle h^{2}({\rm End}\_{0}(V)) | =\displaystyle= | h1​(End0​(V)).\displaystyle h^{1}({\rm End}\_{0}(V))\>. |  | (4.9) |

Thus

|  |  |  |
| --- | --- | --- |
|  | h2​(Q)=h1​(T∗)+h1​(End0​(V))+h1​(T)−dimIm ​ℱ−dimIm ​ℋ.h^{2}(Q)=h^{1}(T^{\*})+h^{1}({\rm End}\_{0}(V))+h^{1}(T)-\dim\text{Im~}\mathcal{F}-\dim\text{Im~}\mathcal{H}\>. |  |

We can now substitute

|  |  |  |
| --- | --- | --- |
|  | h1​(End0​(V))+h1​(T)−dimIm ​ℱ=h1​(End0​(V))+dimker​ℱ=h1​(Q1)h^{1}({\rm End}\_{0}(V))+h^{1}(T)-\dim\text{Im~}\mathcal{F}=h^{1}({\rm End}\_{0}(V))+\dim{\rm ker~}\mathcal{F}=h^{1}(Q\_{1}) |  |

to conclude

|  |  |  |
| --- | --- | --- |
|  | h2​(Q)=h1​(T∗)+h1​(Q1)−dimIm ​ℋ,h^{2}(Q)=h^{1}(T^{\*})+h^{1}(Q\_{1})-\dim\text{Im~}\mathcal{H}\>, |  |

which agrees with the expression for h1​(Q)h^{1}(Q) given in ([4.6](#S4.E6 "In 4 The index of the complex and obstructions")). This completes the proof of ([4.3](#S4.E3 "In 4 The index of the complex and obstructions")).

It should be noted that the above proof does not rely on the details of the extension map ℋ\mathcal{H}, so it is also true for the moduli problems of [[28](#bib.bib28), [27](#bib.bib27)], where extra spurious modes are included, corresponding to deformations of a connection on the tangent bundle.

The vanishing of the index, or Euler characteristic ([4.4](#S4.E4 "In 4 The index of the complex and obstructions")), then also follows. Indeed, as H0​(Q1)=0H^{0}(Q\_{1})=0, we have

|  |  |  |
| --- | --- | --- |
|  | h0​(Q)=h0​(T∗)=h3​(T)=h3​(Q),h^{0}(Q)=h^{0}(T^{\*})=h^{3}(T)=h^{3}(Q)\>, |  |

where the middle equality again uses the holomorphic volume form and Serre duality. It follows that the alternating sum in ([4.4](#S4.E4 "In 4 The index of the complex and obstructions")) vanishes.

## 5 Conclusion

We have shown that, at the level of supergravity, correct to first order in α‵{\alpha^{\backprime}\,}, the dimension of the parameter space for a point on the standard embedding is

|  |  |  |  |
| --- | --- | --- | --- |
|  | h1,1​(X)+h2,1​(X)+h0,1​(End0​(T​X)).h^{1,1}(X)\>+\>h^{2,1}(X)\>+\>h^{0,1}({\rm End}\_{0}(TX))\>. |  | (5.1) |

There is the question of extending this infinitesimal analysis to all orders in the deformation theory; namely to rigorously construct coordinates on the moduli space nearby the standard embedding. Progress in this direction in the mathematics literature can be found in [[50](#bib.bib50), [51](#bib.bib51)]. While it is often assumed that the parameter space of heterotic string theory decomposes into a sum of cohomologies, we have actually demonstrated this here in the particular situation of the standard embedding (the more general situation is much harder and beyond the scope of our current tools).

This calculation might be interesting in trying to understand the meaning of (0,2)(0,2) mirror symmetry. As we are considering theories at the standard embedding there is (2,2)(2,2)–mirror symmetry. This is a symmetry of the full string theory and so the dimension of the moduli space of the mirror should at least match that of the original theory. While this is true for the deformations that preserve the (2,2)(2,2) locus via

|  |  |  |
| --- | --- | --- |
|  | h1,1​(X)=h2,1​(X~),andh2,1​(X)=h1,1​(X~),h^{1,1}(X)=h^{2,1}(\widetilde{X})~,\qquad{\rm and}\qquad h^{2,1}(X)=h^{1,1}(\widetilde{X})~, |  |

we haven’t had a complete expression at the level of supergravity, even for theories that are deformations of the standard embedding, until now. This is of interest for two reasons. First, mathematically speaking it is certainly not obvious that h0,1​(X,End0​(T​X))=h0,1​(X~,End0​(T​X~))h^{0,1}(X,{\rm End}\_{0}(TX))=h^{0,1}(\widetilde{X},{\rm End}\_{0}(T\widetilde{X})). So the expression ([5.1](#S5.E1 "In 5 Conclusion")) for XX and its mirror X~\widetilde{X} are not necessarily the same. Secondly, analogous calculations at the level of the worldsheet indicate that the dimension of the moduli space, and its purported mirror, do not agree [[24](#bib.bib24)]. This non-agreement is reflected here. What do we make of this?

The moduli we computed in ([5.1](#S5.E1 "In 5 Conclusion")) are massless singlet fields of a supergravity theory correct to first order in α‵{\alpha^{\backprime}\,}. It could be the case that the true dimension of the string theory moduli space differs, modified by worldsheet instantons or gsg\_{s} corrections. For this reason one might study a sigma model description of the same background, and count the corresponding parameter space. Indeed, this was done in [[24](#bib.bib24)] for CY manifolds that are complete intersections in toric varieties. Unless, XX satisfied a certain combinatorial condition (the Newton polytope and its dual both have no facets with interior points) the dimension of the entire (0,2)(0,2) parameter space for XX is not the same as its mirror X~\widetilde{X}. In the situation where XX does satisfy this combinatorial condition, then the parameter spaces of both XX and X~\widetilde{X} are the same and [[23](#bib.bib23)] constructed a mirror map on the parameters. It would be interesting, even if this restricted case, to compare the expressions for the parameter space of the GLSM to what is computed in ([5.1](#S5.E1 "In 5 Conclusion")). They do not necessarily have to agree as, for example the GLSM misses moduli that are “non-polynomial” or “non-toric" but the moduli it does counts are true at least in the sense they are not lifted by quantum corrections at least in α‵{\alpha^{\backprime}\,}.

It would also be interesting to calculate a similar splitting of cohomologies for more generic heterotic theories. Indeed, the crux of our calculation used the fact that deformations of the gauge connection could be expressed in terms of the moduli Δ\Delta and 𝒵\mathpzc Z as per the calculation in [[13](#bib.bib13)]. We do not have this freedom in more generic situations.

The computation above also suggests that the Hull-Strominger system has a zero-dimensional virtual moduli space, i.e. the expected moduli space is a set of points. This is the scenario where techniques of enumerative geometry, or counting topological invariants, naturally applies. In this setting, it is tempting to speculate whether analogs of Donaldson-Thomas invariants [[52](#bib.bib52), [53](#bib.bib53)] may be defined for heterotic geometries. Note that in [[32](#bib.bib32)], the index computation was extended to other dimensions and to more generic scenarios where our assumption ([4.1](#S4.E1 "In 4 The index of the complex and obstructions")) of no holomorphic vector fields and stable gauge bundles does not hold, such as for example principal T2T^{2} fibrations over K​3K3 manifolds, see for example [[54](#bib.bib54), [55](#bib.bib55), [56](#bib.bib56), [57](#bib.bib57), [58](#bib.bib58), [59](#bib.bib59)] and references therein. These geometries are far from Kähler Calabi-Yau and it would be interesting to see how the vanishing of the Euler characteristic connects to the physics of these vacua.

Finally, there has been a lot of recent developments in understanding higher order Yukawa couplings of moduli and matter fields in heterotic compactifications [[60](#bib.bib60), [8](#bib.bib8), [9](#bib.bib9), [61](#bib.bib61), [62](#bib.bib62), [63](#bib.bib63), [64](#bib.bib64), [65](#bib.bib65), [66](#bib.bib66), [67](#bib.bib67)]. Given its topological nature, it is natural to wonder if the vanishing Euler characteristic has something to say about the true nature of the heterotic moduli problem (massless spectrum), once all higher order and non-perturbative corrections have been included.

### Acknowledgements

We would like to thank Xenia de la Ossa, Hannah de Lazari, Mario Garcia-Fernandez, Raul Gonzalez Molina, Jason Lotay, Javier José Murgas Ibarra, Henrique Sa Earp, and Markus Upmeier for interesting conversations. JM is partially supported by a ARC Discovery Grant DP240101409. SP is supported by an NSERC Discovery Grant. JM and ES would like to thank the mathematical research institute MATRIX in Australia where part of this research was performed.

## References

![[LOGO]][IMAGE]

## Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile
support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the
methods listed below:

**Tip:** You can select the relevant text first, to include it in your report.

Our team has already identified [the following issues](https://github.com/arXiv/html_feedback/issues). We appreciate your time reviewing and reporting rendering errors we
may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability
should not be a barrier to accessing research. Thank you for your continued support in championing open access for
all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a [list of packages that need conversion](https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML), and welcome [developer contributions](https://github.com/brucemiller/LaTeXML/issues).

![Simons Foundation](/static/base/1.0.1/images/funders/simons-foundation.png)
![Simons Foundation International](/static/base/1.0.1/images/funders/simons-foundation-international.png)
![Schmidt Sciences](/static/base/1.0.1/images/funders/schmidt-sciences.png)