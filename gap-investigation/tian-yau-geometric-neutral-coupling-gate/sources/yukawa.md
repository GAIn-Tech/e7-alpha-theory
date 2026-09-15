##### Report GitHub Issue

Content selection saved. Describe the issue below:

![](/static/base/1.0.1/images/icons/smileybones-small.svg)
![arXiv logo](/static/base/1.0.1/images/arxiv-logo-primary-light.svg)

# Physical Yukawa Couplings in Heterotic String Compactifications

###### Abstract

One of the challenges of heterotic compactification on a Calabi–Yau threefold is to determine the physical (𝟐𝟕)3(\mathbf{27})^{3} Yukawa couplings of the resulting four-dimensional 𝒩=1\mathcal{N}=1 theory.
In general, the calculation necessitates knowledge of the Ricci-flat metric.
However, in the standard embedding, which references the tangent bundle, we can compute normalized Yukawa couplings from the Weil–Petersson metric on the moduli space of complex structure deformations of the Calabi–Yau manifold.
In various examples (the Fermat quintic, the intersection of two cubics in ℙ5\mathbb{P}^{5}, and the Tian–Yau manifold), we calculate the normalized Yukawa couplings for (2,1)(2,1)-forms using the Weil–Petersson metric obtained from the Kodaira–Spencer map.
In cases where h1,1=1h^{1,1}=1, this is compared to a complementary calculation based on performing period integrals.
A third expression for the normalized Yukawa couplings is obtained from a machine learned approximate Ricci-flat metric making use of explicit harmonic representatives.
The excellent agreement between the different approaches opens the door to precision string phenomenology.

## 1 Introduction

String theory on Calabi–Yau manifolds has offered the promise of deriving the complete structure of the Standard Model of particle physics from the compactification geometry [[1](#bib.bib1)].
We focus here on the case of the “standard embedding” [[1](#bib.bib1), [2](#bib.bib2), [3](#bib.bib3), [4](#bib.bib4), [5](#bib.bib5), [6](#bib.bib6)] of heterotic E8×E8E\_{8}\times E\_{8} superstring theory on Calabi–Yau threefolds for which there are 12​|χ|\frac{1}{2}|\chi| generations of particles in the low-energy spectrum.
A modern approach to model building, which invokes bundle structures, does not insist that the Euler characteristic χ=±6\chi=\pm 6 and is perhaps physically more appealing for string phenomenology as we can work with manifolds with a small number of moduli [[7](#bib.bib7), [8](#bib.bib8), [9](#bib.bib9), [10](#bib.bib10), [11](#bib.bib11)]. For reviews on the matter see, e.g., [[12](#bib.bib12), [13](#bib.bib13)].

Viewed in this more general framework, the standard embedding is the case in which the vector bundle VV is taken to be the tangent bundle of the Calabi–Yau compatification TXT\_{X}, i.e., the holomorphic sheaf of vector fields on XX whose connection solves the Hermitian Yang–Mills equations.
The standard embedding provides fertile ground for study and is particularly amenable to numerical analysis.
We start here as an initial step.

By virtue of the Calabi–Yau manifold admitting a Ricci-flat metric in each Kähler class, compactification of the heterotic theory on such a geometry preserves 𝒩=1\mathcal{N}=1 supersymmetry in the four-dimensional effective field theory. The Calabi–Yau threefold XX is as well an S​U​(3)SU(3) holonomy manifold.
The commutant of S​U​(3)SU(3) in E8E\_{8} is E6E\_{6}, which embeds generations of the particle spectrum of the Standard Model in its 𝟐𝟕\mathbf{27} and 𝟐𝟕¯\overline{\mathbf{27}} representations.
An important question then is to determine the Yukawa couplings that describe how strongly the low-energy fields interact.
The (𝟐𝟕¯)3(\overline{\mathbf{27}})^{3} couplings are topological (without the worldsheet instantons included), whereas the (𝟐𝟕)3(\mathbf{27})^{3} couplings require knowledge of the complex geometry of the Calabi–Yau space [[14](#bib.bib14), [15](#bib.bib15), [16](#bib.bib16)].
In this paper, we focus on the latter set of couplings, expressed in terms of forms resident in H2,1​(X)H^{2,1}(X), to which we now turn. (For more details, see [[3](#bib.bib3)].)

The Calabi–Yau condition is also equivalent to the existence of a nowhere vanishing holomorphic top form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ω(3,0)=13!​Ωμ​ν​ρ​d​zμ∧d​zν∧d​zρ,\Omega^{(3,0)}=\frac{1}{3!}\Omega\_{\mu\nu\rho}\,{\mathrm{d}}z^{\mu}\wedge{\mathrm{d}}z^{\nu}\wedge{\mathrm{d}}z^{\rho}\,, |  | (1.1) |

which provides for the isomorphism H2,1​(X)​≈Ω¯​H1​(X,TX)H^{2,1}(X)\overset{\scriptscriptstyle\overline{\Omega}}{\approx}H^{1}(X,T\_{X}).
For a given (2,1)(2,1)-form, we can write an equivalent (0,1)(0,1) TXT\_{X}-valued form as

|  |  |  |  |
| --- | --- | --- | --- |
|  | 12!ωμ​ν​σ¯dzμ∧dzν∧dzσ¯⟷dzσ¯(ωσ¯=μΩ¯μ​ν​ρων​ρ​σ¯)∂μ.\frac{1}{2!}\omega\_{\mu\nu\overline{\sigma}}\,{\mathrm{d}}z^{\mu}\wedge{\mathrm{d}}z^{\nu}\wedge{\mathrm{d}}z^{\overline{\sigma}}\quad\longleftrightarrow\quad{\mathrm{d}}z^{\overline{\sigma}}(\omega\_{\overline{\sigma}}{}^{\mu}=\overline{\Omega}^{\mu\nu\rho}\omega\_{\nu\rho\overline{\sigma}})\partial\_{\mu}\,. |  | (1.2) |

Schematically, the (𝟐𝟕)3(\mathbf{27})^{3} couplings are

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ=∫XΩ∧ωμ∧ων∧ωρ​Ωμ​ν​ρ.\kappa=\int\_{X}\Omega\wedge\omega^{\mu}\wedge\omega^{\nu}\wedge\omega^{\rho}\,\Omega\_{\mu\nu\rho}\,. |  | (1.3) |

These are the unnormalized Yukawa couplings:
the integral depends only on the cohomology class of ω\omega and not the actual representative.
The normalized Yukawa couplings, corresponding to the physical couplings of the model, demand a diagonalization of the kinetic terms.
In general, calculating the normalized couplings requires using the Ricci-flat Calabi–Yau metric in order to choose particular harmonic representatives.

This complication is circumvented in the standard embedding V≅TXV\cong T\_{X}.
In this case, the deformations of VV correspond one-to-one to the complex structure deformations of the base Calabi–Yau manifold, and the metric on the h2,1h^{2,1}-dimensional space of deformations is the Weil–Petersson metric.
The crucial fact is that the Weil–Petersson metric on the moduli space can be calculated without recourse to the Ricci-flat Calabi–Yau metric [[17](#bib.bib17)].
This is sufficient to calculate the normalized Yukawa couplings.

This effort is part of a program to improve numerical results in string phenomenology.
These developments have been revived because machine learning provides good approximations for Ricci-flat Calabi–Yau metrics [[18](#bib.bib18), [19](#bib.bib19), [20](#bib.bib20), [21](#bib.bib21), [22](#bib.bib22), [23](#bib.bib23), [24](#bib.bib24), [25](#bib.bib25)]
and more recently facilitates the computation of the spectrum of harmonic forms [[26](#bib.bib26), [27](#bib.bib27), [28](#bib.bib28), [29](#bib.bib29)] that enter into the calculation of Yukawa couplings.
In this work, we use numerical integration techniques to compute the field normalizations and the normalized Yukawa couplings for various heterotic compactifications in the standard embedding.
Furthermore, we use a similar implementation as the one underlying the spectral neural network construction [[24](#bib.bib24)] in order to obtain harmonic, tangent bundle valued (0,1)(0,1)-forms.
The explicit computation of the normalization for those objects requires the Ricci-flat Calabi–Yau metric.
Our aim is to demonstrate that those normalization agree with the Weil–Petersson results.

We consider two one-parameter Calabi–Yau threefolds, the intersection of two cubics in ℙ5\mathbb{P}^{5}, the quintic hypersurface in ℙ4\mathbb{P}^{4} (and their mirrors) as well as the complete intersection Tian–Yau manifold.
We shall compute the Weil–Petersson metric in two different ways: (i) via a Kodaira–Spencer map for all cases considered, and (ii) via the calculation of period integrals for Calabi–Yau spaces with h2,1=1h^{2,1}=1 only.11
1
When h2,1>1h^{2,1}>1, the analogous calculation requires solving Picard–Fuchs partial differential equations and is more complicated than the h2,1=1h^{2,1}=1 case, where we essentially have an ordinary differential equation [[30](#bib.bib30)].
In particular, we check that for the examples with h2,1=1h^{2,1}=1 the Kodaira–Spencer and the period computations agree.
This validates the Kodaira–Spencer algorithms implemented.
These calculations are compared to each other and found to match the canonical computation, using the Ricci-flat Calabi–Yau metric that is calculated numerically using machine learning.

Our work presents the first calculation of physically normalized Yukawa couplings for several complete intersection Calabi–Yau (CICY) manifolds with standard embedding, as well as a versatile extension of the Kodaira–Spencer method advanced by Keller–Lukic [[31](#bib.bib31)].
The techniques are: firstly, more efficient than machine learning based methods, and secondly, more general than existing methods for computing analytically continued periods, which are anyway only feasible for a small number of moduli.

The organization of the paper is as follows.
In Section [2](#S2 "2 Heterotic Yukawa couplings ‣ Physical Yukawa Couplings in Heterotic String Compactifications"), we sketch the general computation of Yukawa couplings associated to H2,1​(X)H^{2,1}(X).
Recalling that tangent bundle valued (0,1)(0,1)-forms are dual to (2,1)(2,1)-forms and that these span the massless degrees of freedom transforming as 𝟐𝟕\mathbf{27} under E6E\_{6}, we construct polynomial representatives for the (0,1)(0,1)-forms.
In Section [3](#S3 "3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications"), we discuss the Kodaira–Spencer map and its use in the computation of the field normalizations (see Section [3.1](#S3.SS1 "3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")).
In Section [4](#S4 "4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications"), we present numerical results.
For the mirror of the intersection of two cubics in ℙ5\mathbb{P}^{5}, we compare the period integral result with the numerical integration that produces the Weil–Petersson metric and demonstrate the agreement of both methods.
We also compute the Yukawa coupling for this example and show that it agrees with the period result for any value of the modular deformation.
In addition, we consider a ℤ5×ℤ5\mathbb{Z}\_{5}\times\mathbb{Z}\_{5} quotient of the Fermat quintic and the ℤ3\mathbb{Z}\_{3} quotient of the Tian–Yau manifold.
For the Fermat quotient, we compare the normalized Yukawa couplings to the conformal field theory computations [[32](#bib.bib32)] and show that the Kodaira–Spencer normalization produces the correct results.
Similarly, for the Tian–Yau quotient, we contrast our computation with the unnormalized Yukawa couplings of [[33](#bib.bib33)].
For this case, we obtain the normalized couplings as well as their behavior along a modulus direction.
Our methods are general and can be readily applied to the standard embedding of any complete intersection Calabi–Yau manifold.
In Section [5](#S5 "5 Machine learning harmonic representatives ‣ Physical Yukawa Couplings in Heterotic String Compactifications"), we discuss the method employed to search for the harmonic representatives and the direct computation of the normalizations which makes use of machine learned Ricci-flat metric. We discuss our implementation for the quintic and the bicubic.
Finally, in Section [6](#S6 "6 Discussion and outlook ‣ Physical Yukawa Couplings in Heterotic String Compactifications"), we present conclusions and prospects for future work.

The numerical implementation of the Weil–Petersson metric as well as the calculation of approximate Ricci-flat Calabi–Yau metrics are part of a JAX [[34](#bib.bib34)] library called cymyc (Calabi–Yau Metrics, Yukawas, and Curvature) [[35](#bib.bib35)], to be released soon.

Note added:
One week after the first version of this preprint appeared on arXiv, the preprint [[36](#bib.bib36)] considered machine learning based calculation of physical Yukawa couplings in non-standard embeddings.

## 2 Heterotic Yukawa couplings

Let us begin by considering the E8×E8E\_{8}\times E\_{8} heterotic string compactified on a Calabi–Yau threefold XX.
The compactification breaks E8×E8E\_{8}\times E\_{8} to a smaller subgroup.
In order for 𝒩=1\mathcal{N}=1 supersymmetry to be preserved in the resulting four-dimensional effective theory, the structure group HH of a principal bundle VV over XX must be embedded into E8×E8E\_{8}\times E\_{8}.
The matter in four dimensions can be obtained from the corresponding decomposition of the E8×E8E\_{8}\times E\_{8} adjoint representation.

For simplicity, consider a subgroup GG in a single E8E\_{8} with GG the commutant of HH in E8E\_{8}, so that the effective gauge symmetry in four dimensions is G×E8G\times E\_{8}.
The matter in the visible sector is then supplied by the decomposition of the 248248-dimensional adjoint representation of E8E\_{8},

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟐𝟒𝟖=𝐀𝐝𝐣E8→(𝐀𝐝𝐣H,𝟏)⊕(𝟏,𝐀𝐝𝐣G)​⨁i(𝐑H(i),𝐑G(i)),\mathbf{248}=\mathbf{Adj}\_{E\_{8}}\rightarrow(\mathbf{Adj}\_{H},\mathbf{1})\penalty\ \oplus\penalty\ (\mathbf{1},\mathbf{Adj}\_{G})\penalty\ \bigoplus\_{i}(\mathbf{R}\_{H}^{(i)},\mathbf{R}\_{G}^{(i)})\,, |  | (2.1) |

where 𝐑H(i)\mathbf{R}\_{H}^{(i)} and 𝐑G(i)\mathbf{R}\_{G}^{(i)} are suitable representations of HH and GG.
More specifically, matter in the representation 𝐑G(i)\mathbf{R}\_{G}^{(i)} of the effective gauge group is represented by harmonic (0,1)(0,1)-forms a(i)a^{(i)} that take values in a vector bundle ViV\_{i},22
2
The index ii denotes different bundles, such as VV, V∗V^{\*}, and V⊗V∗V\otimes V^{\*}. i.e., a(i)∈H1​(X,Vi)a^{(i)}\in H^{1}(X,V\_{i}).

We discuss computation of the trilinear interaction terms.
The holomorphic Yukawa couplings λ⁡(a(i),b(j),c(k))\lambda(a^{(i)},b^{(j)},c^{(k)}) may be nonzero provided the tensor product 𝐑G(i)⊗𝐑G(j)⊗𝐑G(k)\mathbf{R}\_{G}^{(i)}{\otimes}\mathbf{R}\_{G}^{(j)}{\otimes}\mathbf{R}\_{G}^{(k)} contains a GG-invariant, and may be computed, generalizing ([1.3](#S1.E3 "In 1 Introduction ‣ Physical Yukawa Couplings in Heterotic String Compactifications")), as

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ⁡(a(i),b(j),c(k))=∫XΩ∧Ω~​(a(i),b(j),c(k)),\kappa(a^{(i)},b^{(j)},c^{(k)})=\int\_{X}\Omega\wedge\widetilde{\Omega}\big(a^{(i)},b^{(j)},c^{(k)}\big)\,, |  | (2.2) |

where Ω\Omega is the holomorphic (3,0)(3,0) form and Ω~​(a(i),b(j),c(k))\widetilde{\Omega}(a^{(i)},b^{(j)},c^{(k)}) is the appropriate contraction with the (0,1)​V(0,1)\,V-valued forms, with Ω~\widetilde{\Omega} a suitable deformation of the standard Ω\Omega as long as ViV\_{i} is a rank-33 deformation of TXT\_{X}.
The couplings ([2.2](#S2.E2 "In 2 Heterotic Yukawa couplings ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) only become the physical ones once we know the Kähler potential for the matter fields, which yields the corresponding kinetic terms.

The low-energy effective action of an 𝒩=1\mathcal{N}=1 theory is written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Seff=∫d4x[∫d4θK(Φa,Φ¯)b¯+14​g2(∫d2θtr𝒲α𝒲α+∫d2θW(Φa))+h.c.],S\_{\text{eff}}=\int{\mathrm{d}}^{4}x\ \left[\int{\mathrm{d}}^{4}\theta\ K\big(\Phi^{a},\overline{\Phi}{}^{\overline{b}}\big)+\frac{1}{4g^{2}}\left(\int{\mathrm{d}}^{2}\theta\ \text{tr}\,\mathcal{W}\_{\alpha}\mathcal{W}^{\alpha}+\int{\mathrm{d}}^{2}\theta\ W(\Phi^{a})\right)+\text{h.c.}\right], |  | (2.3) |

where Φa\Phi^{a} are chiral superfields and 𝒲α\mathcal{W}\_{\alpha} is the gauge field strength associated to the vector superfield.
The superpotential W⁡(Φa)W(\Phi^{a}) is a holomorphic function of the superfields and is gauge invariant with RR-charge 22.
The Yukawa couplings originate from this term in the effective action.
The Kähler potential, which is explicitly not holomorphic, contains the kinetic terms:33
3
From the underlying worldsheet quantum field theory, this kinetic term normalization metric emerges as a two-point correlation function defining (the appropriate generalization of) the Zamolodchikov metric [[37](#bib.bib37)]. In the special case when Vi=TXV\_{i}=T\_{X}, this equals the Weil–Petersson metric [[38](#bib.bib38)].

|  |  |  |  |
| --- | --- | --- | --- |
|  | K(Φa,Φ¯)b¯⊃Na​b¯ΦaΦ¯+b¯….K\big(\Phi^{a},\overline{\Phi}{}^{\overline{b}}\big)\supset N\_{a\overline{b}}\;\Phi^{a}\overline{\Phi}{}^{\overline{b}}+\ldots\,. |  | (2.4) |

The entries of the normalization matrix Na​b¯N\_{a\overline{b}} are proportional to the inner product

|  |  |  |  |
| --- | --- | --- | --- |
|  | Na​b¯∼(a,b)=∫Xa∧⋆¯V​b,N\_{a\overline{b}}\sim(a,b)=\int\_{X}a\wedge\bar{\star}\_{V}b\,, |  | (2.5) |

between the harmonic representatives a,ba,b of their respective classes in H1​(X,Vi)H^{1}(X,V\_{i}).
Equipped with this inner product, starting from a given basis {ak(i)}k=1h1​(Vi)\{a\_{k}^{(i)}\}\_{k=1}^{h^{1}(V\_{i})}, we may obtain an orthonormal basis {ak(i)′}k=1h1​(Vi)\{a\_{k}^{(i)\prime}\}\_{k=1}^{h^{1}(V\_{i})} via diagonalization of the normalization matrix induced by ([2.5](#S2.E5 "In 2 Heterotic Yukawa couplings ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) and rescaling by the square root of the eigenvalues, i.e., the normalizations Nak′N\_{a^{\prime}\_{k}} of each eigenform ak(i)′a\_{k}^{(i)\prime}. This change of basis converts the holomorphic Yukawa couplings into the physical Yukawa couplings, computed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y(a(i)′,b(j)′,c(k)′)=∫XΩ∧Ω~(a(i)′,b(j)′,c(k)′)∫XΩ∧Ω¯.Y\big(a^{(i)\,\prime},b^{(j)\,\prime},c^{(k)\,\prime}\big)=\frac{\int\_{X}\Omega\wedge\widetilde{\Omega}\big(a^{(i)\,\prime},b^{(j)\,\prime},c^{(k)\,\prime}\big)}{\int\_{X}\Omega\wedge\overline{\Omega}}\,. |  | (2.6) |

Reflecting on what we have discussed so far, we emphasize the following two points.

The computation of the holomorphic Yukawa couplings in ([2.2](#S2.E2 "In 2 Heterotic Yukawa couplings ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) does not require knowledge of the harmonic representatives in H1​(X,Vi)H^{1}(X,V\_{i}), i.e., the unnormalized couplings are the same when computed using elements in the cohomology classes [a(i)][a^{(i)}], [b(j)][b^{(j)}], and [c(k)][c^{(k)}].
The calculation of λ\lambda is quasi-topological [[39](#bib.bib39), [40](#bib.bib40)].

This is not the case for the normalization ([2.5](#S2.E5 "In 2 Heterotic Yukawa couplings ‣ Physical Yukawa Couplings in Heterotic String Compactifications")), since the Hodge star ⋆V\star\_{V} between harmonic bundle-valued forms requires knowledge of the Ricci-flat metric on XX and the Hermitian structure on VV.
The calculation of κ\kappa requires geometric input.

Here we briefly note that one requires geometric computations involving the metric to utilize the Ricci-flat representative for the Kähler class being considered in order for the metric on the Calabi–Yau complex structure moduli space to be Kähler, an argument we will make more precise in the discussion after Lemma [2](#Thmlemma2 "Lemma 2. ‣ 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications").

Let us now specialize to the case where H=S​U​(3)H=SU(3), for which the adjoint decomposition takes the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝟐𝟒𝟖→(𝟕𝟖,𝟏)⊕(𝟏,𝟖)⊕(𝟐𝟕¯,𝟑¯)⊕(𝟐𝟕,𝟑).\mathbf{248}\rightarrow(\mathbf{78},\mathbf{1})\oplus(\mathbf{1},\mathbf{8})\oplus(\overline{\mathbf{27}},\overline{\mathbf{3}})\oplus(\mathbf{27},\mathbf{3})\,. |  | (2.7) |

As E6×S​U​(3)E\_{6}\times SU(3) is a maximal subgroup of E8E\_{8}, we identify E6E\_{6} as the GUT gauge group GG.
The number of 𝟐𝟕\mathbf{27} multiplets are counted by h1​(V)h^{1}(V) while the number of 𝟐𝟕¯\overline{\mathbf{27}} multiplets are counted by h1​(V∗)=h2​(V)h^{1}(V^{\*})=h^{2}(V).
There might also be additional singlet fields corresponding to bundle moduli; these are counted by h1​(V⊗V∗)h^{1}(V\otimes V^{\*}).
In the standard embedding, the role of the holomorphic vector bundle VV is played by the tangent sheaf TXT\_{X}, whose structure group is indeed S​U​(3)SU(3).
Setting V=TXV=T\_{X} implies that the difference between the number of massless 𝟐𝟕\mathbf{27} and 𝟐𝟕¯\overline{\mathbf{27}} representations is an index, half of the Euler characteristic. It also motivates the following lemma (see Appendix [A](#A1 "Appendix A Proofs of lemmas ‣ Physical Yukawa Couplings in Heterotic String Compactifications") for a detailed proof):

###### Lemma 1.

Let XX be a Calabi–Yau manifold, then: H1​(X,TX)≃H∂¯n−1,1​(X)H^{1}(X,T\_{X})\simeq H^{n-1,1}\_{\overline{\partial}}(X) and the isomorphism is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | [α]⟼[Ω⁡(α)],\displaystyle[\alpha]\longmapsto[\Omega(\alpha)]\,, |  | (2.8) |

where Ω∈H∂¯n,0​(X)\Omega\in H^{n,0}\_{\overline{\partial}}(X) is nowhere zero.

For the particular case of Calabi–Yau threefolds, this implies the well-known isomorphism H1​(X,TX)≃H2,1​(X)H^{1}(X,T\_{X})\simeq H^{2,1}(X). Recall further that for this particular case, the pairing ([2.5](#S2.E5 "In 2 Heterotic Yukawa couplings ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) becomes the Weil–Petersson metric on the Calabi–Yau complex structure moduli space (see also Definition [1](#Thmdefinition1 "Definition 1. ‣ 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications") below),

|  |  |  |  |
| --- | --- | --- | --- |
|  | (a,b)=∫Xa∧⋆¯g​b=def⟨a,b⟩WP.(a,b)=\int\_{X}a\wedge\bar{\star}\_{g}b\mathrel{\overset{\scriptscriptstyle\rm def}{=}}\langle a,b\rangle\_{\rm WP}\,. |  | (2.9) |

This may be computed by exploiting the existence of the Ricci-flat metric without its direct invocation, owing to special geometry, as we shall see in the sequel.

We are interested in the computation of Yukawa couplings of the form (𝟐𝟕)3(\mathbf{27})^{3} which involve only elements in H1​(X,TX)H^{1}(X,T\_{X}). In this case, the pairing introduced in ([2.2](#S2.E2 "In 2 Heterotic Yukawa couplings ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) can be written as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ω~​(a,b,c)=defaμ∧bν∧cρ​Ωμ​ν​ρ,\widetilde{\Omega}(a,b,c)\mathrel{\overset{\scriptscriptstyle\rm def}{=}}a^{\mu}\wedge b^{\nu}\wedge c^{\rho}\,\Omega\_{\mu\nu\rho}\,, |  | (2.10) |

where the (3,0)(3,0)-form Ω\Omega acts by contraction on the ⋀3TX\bigwedge^{3}T\_{X}-valued (0,3)(0,3)-form to give an ordinary, ℂ\mathbb{C}-valued (0,3)(0,3)-form. If we take an orthogonal basis {ak}k=1h1​(TX)\{a\_{k}\}\_{k=1}^{h^{1}(T\_{X})} the corresponding normalized Yukawa couplings take the form

|  |  |  |  |
| --- | --- | --- | --- |
|  | Yi​j​k=∫XΩ∧Ω~​(ai,aj,ak)Ni​Nj​Nk​∫XΩ∧Ω¯.\displaystyle Y\_{ijk}=\frac{\displaystyle\int\_{X}\Omega\wedge\widetilde{\Omega}(a\_{i},a\_{j},a\_{k})}{\displaystyle\sqrt{N\_{i}N\_{j}N\_{k}}\int\_{X}\Omega\wedge\overline{\Omega}}\,. |  | (2.11) |

## 3 Physical Yukawa couplings via the Kodaira–Spencer map

### 3.1 Computing normalizations

In order to discuss the computation of the canonical normalization matrix via the Weil–Petersson metric ([2.9](#S2.E9 "In 2 Heterotic Yukawa couplings ‣ Physical Yukawa Couplings in Heterotic String Compactifications")), we briefly recall some facts on the metric on the complex structure moduli of a Calabi–Yau manifold XX with Kähler class [ω]∈H∂¯1,1​(X)[\omega]\in H\_{\overline{\partial}}^{1,1}(X). We shall mostly follow the notation of [[41](#bib.bib41)]. Let us start by considering a complex analytic family (in the sense of Kodaira and Spencer [[42](#bib.bib42)], for more details see: [[43](#bib.bib43)]) (𝒳,B,ϖ)(\mathcal{X},B,\varpi) of Calabi–Yau manifolds over a base BB such that 0∈B⊆ℂdimH1​(X,TX)0\in B\subseteq\mathbb{C}^{\dim H^{1}(X,T\_{X})} with projection map ϖ:𝒳→B\varpi\colon\mathcal{X}\rightarrow B and Xt:=ϖ−1​(t)X\_{t}:=\varpi^{-1}(t) with X:=X0X:=X\_{0}. Recall that the Weil–Petersson metric ⟨−,−⟩WP\langle-,-\rangle\_{\mathrm{WP}} on the moduli space T0​BT\_{0}B of complex deformations of XX can be written as a Kähler metric such that X0=XX\_{0}=X and [ωt]=[ω][\omega\_{t}]=[\omega]. We shall refer to this family as a polarized complex analytic family, with polarization induced by [ω][\omega].

###### Definition 1.

Let gt∈[ω]g\_{t}\in[\omega] denote the unique Ricci-flat metric on Xt∈𝒳X\_{t}\in\mathcal{X} in the polarized complex analytic family (𝒳,B,ϖ)(\mathcal{X},B,\varpi). The Weil–Petersson metric is then defined as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨a,b⟩WP=∫Xtρ⁡(a)∧⋆gt¯​ℋ​ρ​(b),\displaystyle\langle a,b\rangle\_{\mathrm{WP}}=\int\_{X\_{t}}\rho(a)\wedge\overline{\star\_{g\_{t}}}\mathcal{H}\rho(b)\,, |  | (3.1) |

where ρ:Tt​B→H1​(X,TX)\rho\colon T\_{t}B\rightarrow H^{1}(X,T\_{X}) is the Kodaira–Spencer map [[42](#bib.bib42), [43](#bib.bib43)]
and ℋ:H∂¯p,q​(X)→ℋ∂¯p,q​(X)\mathcal{H}\colon H^{p,q}\_{\overline{\partial}}(X)\rightarrow\mathcal{H}^{p,q}\_{\overline{\partial}}(X) is the harmonic projection.

The Kodaira–Spencer map can be defined in the following manner: Let {Uj}\{U\_{j}\} be a finite cover of XtX\_{t} with local coordinates {zj1,…,zjn}\{z\_{j}^{1},\dots,z\_{j}^{n}\} such that for every Uj∩Uk≠∅U\_{j}\cap U\_{k}\neq\emptyset the gluing maps are given by fj​k:B×Uk→Ujf\_{jk}\colon B\times U\_{k}\rightarrow U\_{j}. Then, the Kodaira–Spencer map is defined as follows:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ⁡(∂∂t)=[{∂fj​kμ​(zk,t)∂t​∂∂zjμ}],where​zk=fk​j​(zj,t).\displaystyle\rho\left(\frac{\partial}{\partial t}\right)=\left[\left\{\frac{\partial f\_{jk}^{\mu}(z\_{k},t)}{\partial t}\frac{\partial}{\partial z^{\mu}\_{j}}\right\}\right],\quad\text{where}\penalty\ z\_{k}=f\_{kj}(z\_{j},t)\,. |  | (3.2) |

Note that from [[41](#bib.bib41)] we have im​ρ⊆H1​(X,TX)ω\mathrm{im}\,{\rho}\subseteq H^{1}(X,T\_{X})\_{\omega} where H1​(X,TX)ωH^{1}(X,T\_{X})\_{\omega} is the subspace of polarization preserving deformations: [ϕ]∈H1​(X,TX)ω[\phi]\in H^{1}(X,T\_{X})\_{\omega} if [ω⁡(ϕ)]=0[\omega(\phi)]=0. It can be shown that if ϕ∈[ϕ]\phi\in[\phi] is harmonic, then gt​(ϕ)=0g\_{t}(\phi)=0 identically [[44](#bib.bib44)]. This leads to the following lemma:

###### Lemma 2.

Let Ω∈H∂¯n,0​(Xt)\Omega\in H\_{\overline{\partial}}^{n,0}(X\_{t}) where n=dimXtn=\dim{X\_{t}}, be non-zero, then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨a,b⟩WP=−∫XtΩ⁡(ℋ​ρ​(a))∧Ω⁡(ℋ​ρ​(b))¯∫XtΩ∧Ω¯∫Xt𝗏𝗈𝗅gt.\displaystyle\langle a,b\rangle\_{\mathrm{WP}}=-\frac{\displaystyle\int\_{X\_{t}}\Omega(\mathcal{H}\rho(a))\wedge\overline{\Omega(\mathcal{H}\rho(b))}}{\displaystyle\int\_{X\_{t}}\Omega\wedge\overline{\Omega}}\int\_{X\_{t}}\mathsf{vol}\_{g\_{t}}\,. |  | (3.3) |

###### Proof.

See Appendix [A](#A1 "Appendix A Proofs of lemmas ‣ Physical Yukawa Couplings in Heterotic String Compactifications") or Refs. [[45](#bib.bib45), [41](#bib.bib41)]. ∎

At first glance, it may seem that evaluation
of ([3.1](#S3.E1 "In Definition 1. ‣ 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) requires the metric gtg\_{t} on XtX\_{t}, which also induces a metric on Ω0,1​(TXt)\Omega^{0,1}(T\_{X\_{t}}). However, the Ricci-flatness consequence volgt∝Ωt∧Ωt¯\textsf{vol}\_{g\_{t}}\propto\Omega\_{t}\wedge\overline{\Omega\_{t}} ensures ([2.5](#S2.E5 "In 2 Heterotic Yukawa couplings ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) may be expressed in terms of the standard cup product on H∂¯p,q​(Xt)H^{p,q}\_{\bar{\partial}}(X\_{t}) with p+q=np+q=n.

Since our numerical methods use representatives of the Kodaira–Spencer classes ρ⁡(a)∈H1​(X,TX)\rho(a)\in H^{1}(X,T\_{X}) which are not necessarily harmonic, the polarization-preserving condition gt​(ϕ)=0g\_{t}(\phi)=0 is not necessarily guaranteed to hold. We therefore show explicitly, at the level of forms, that the Weil–Petersson metric may be computed with arbitrary representatives. We shall first briefly recall the explicit construction of the Kodaira–Spencer class:

Recall that for any t,t′∈Bt,t^{\prime}\in B, we have Xt≃Xt′X\_{t}\simeq X\_{t^{\prime}} diffeomorphic as real manifolds. For simplicity, let t′=0t^{\prime}=0, and denote the diffeomorphism by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ζt:X⟶≃Xt.\displaystyle\zeta\_{t}\colon X\stackrel{{\scriptstyle\simeq}}{{\longrightarrow}}X\_{t}\,. |  | (3.4) |

Then, the corresponding infinitesimal deformation ξ\xi to ζt\zeta\_{t} at t=0t=0 is a set of non-holomorphic vector fields: ξ={ξj}j\xi=\{\xi\_{j}\}\_{j} defined on a finite open cover {Uj}j\{U\_{j}\}\_{j} of XX. Then, we may construct Kodaira–Spencer class corresponding to ξ\xi using Čech co-cycle defined by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | [{∂¯​ξj}j]∈Hˇ1​(X,TX)≃H1​(X,TX).\displaystyle[\{\overline{\partial}\xi\_{j}\}\_{j}]\in\check{H}^{1}(X,T\_{X})\simeq H^{1}(X,T\_{X})\,. |  | (3.5) |

From the results of [[41](#bib.bib41), [45](#bib.bib45)], the ⟨−,−⟩WP\langle-,-\rangle\_{\mathrm{WP}} is shown to be a Kähler metric with the local Kähler potential given by the canonical intersection pairing on H∂¯n,0​(X)H^{n,0}\_{\overline{\partial}}(X). We shall show that such identification can also be computed with arbitrary representatives without application of harmonic projections. In particular, let Ω⁡(t)\Omega(t) be a holomorphic nn-form on the total space which is smoothly varying with respect to the deformation parameter t∈Bt\in B of the polarized complex analytic family (𝒳,B,ϖ)(\mathcal{X},B,\varpi) and restricts to a non-zero holomorphic (n,0)(n,0) form Ωt∈H∂¯n,0​(Xt)\Omega\_{t}\in H^{n,0}\_{\overline{\partial}}(X\_{t}) on each fibre. Then one has the following decomposition:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Ωtd​t|t=0=Ω′+Ω⁡(ϕ)∈Γ⁡(X,Ωn,0)⊕Γ⁡(X,Ωn−1,1),respectively,\displaystyle\frac{{\mathrm{d}}\Omega\_{t}}{{\mathrm{d}}t}\bigg|\_{t=0}=\Omega^{\prime}+\Omega(\phi)\penalty\ \in\penalty\ \Gamma(X,\Omega^{n,0})\oplus\Gamma(X,\Omega^{n-1,1}),\penalty\ \penalty\ \text{respectively}, |  | (3.6) |

where ϕ∈H1​(TX)\phi\in H^{1}(T\_{X}) is a representative of the Kodaira–Spencer class. The arguments of [[41](#bib.bib41), [45](#bib.bib45), [44](#bib.bib44)] apply the harmonic projection to ϕ\phi to show that Ω′\Omega^{\prime} is holomorphic. Since the general numerical methods that we consider do not compute harmonic representatives, we show that the result holds true for an arbitrary choice of the representatives, when the (n,0)(n,0) part Ω′\Omega^{\prime} of the variation in the canonical holomorphic form is not necessarily holomorphic.

###### Theorem 1.

The identification of ⟨−,−⟩WP\langle-,-\rangle\_{\mathrm{WP}} with the Kähler metric using ([3.6](#S3.E6 "In 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) is true for an arbitrary choice of representatives of the Kodaira–Spencer class.

###### Proof.

Let (−,−)(-,-) denote the intersection pairing on H∂¯p,q​(X)H^{p,q}\_{\overline{\partial}}(X) with p+q=np+q=n:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (α,β)=∫Xα∧β¯.\displaystyle(\alpha,\beta)=\int\_{X}\alpha\wedge\overline{\beta}\,. |  | (3.7) |

Then, without loss of generality, we shall show that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨a,a⟩WP∫X𝗏𝗈𝗅g=(d​Ωtd​t|t=0,d​Ωtd​t|t=0)(Ω,Ω)+|(Ω,d​Ωtd​t|t=0)|2(Ω,Ω)2,\displaystyle\frac{\displaystyle\langle a,a\rangle\_{\mathrm{WP}}}{\displaystyle\int\_{X}\mathsf{vol}\_{g}}\penalty\ =\penalty\ \frac{\displaystyle\left(\frac{{\mathrm{d}}\Omega\_{t}}{{\mathrm{d}}t}\bigg|\_{t=0},\frac{{\mathrm{d}}\Omega\_{t}}{{\mathrm{d}}t}\bigg|\_{t=0}\right)}{(\Omega,\Omega)}+\frac{\displaystyle\left|\left(\Omega,\frac{{\mathrm{d}}\Omega\_{t}}{{\mathrm{d}}t}\bigg|\_{t=0}\right)\right|^{2}}{(\Omega,\Omega)^{2}}\,, |  | (3.8) |

where the decomposition ([3.6](#S3.E6 "In 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) is arbitrary and a∈T0​Ba\in T\_{0}B such that ρ⁡(a)=[ϕ]\rho(a)=[\phi]. This implies that the terms in ([3.8](#S3.E8 "In Proof. ‣ 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) due to the Γ⁡(X,Ωn,0)\Gamma(X,\Omega^{n,0}) component of the decomposition ([3.6](#S3.E6 "In 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) are not necessarily zero. Recall that closure is a topological condition; we have: d​Ωt=0d\Omega\_{t}=0 for all tt, which implies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂Ω′+∂¯​Ω′+∂(Ω⁡(ϕ))=0.\displaystyle\partial\Omega^{\prime}+\overline{\partial}\Omega^{\prime}+\partial(\Omega(\phi))=0\,. |  | (3.9) |

Note that deg∂Ω′=(n+1,0)\deg{\partial\Omega^{\prime}}=(n+1,0) whereas deg∂¯Ω′=deg∂(Ω(ϕ))=(n,1)\deg{\overline{\partial}\Omega^{\prime}}=\deg\partial(\Omega(\phi))=(n,1), thus ∂Ω′=0\partial\Omega^{\prime}=0 due to the Hodge decomposition. Let ψ∈Γ⁡(X,Ωn−1,0)\psi\in\Gamma(X,\Omega^{n-1,0}) be such that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ω⁡(ϕ)+∂¯​ψ=ℋ​Ω​(ϕ),\displaystyle\Omega(\phi)+\overline{\partial}\psi=\mathcal{H}\Omega(\phi)\,, |  | (3.10) |

whose existence is guaranteed by the Hodge theorem. Then, by combining ([3.9](#S3.E9 "In Proof. ‣ 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) and ([3.10](#S3.E10 "In Proof. ‣ 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂¯​Ω′+∂(Ω⁡(ϕ))+∂∂¯​ψ−∂¯​∂ψ=∂¯​(Ω′+∂ψ)+∂ℋ⁡(Ω⁡(ϕ))=0.\displaystyle\overline{\partial}\Omega^{\prime}+\partial(\Omega(\phi))+\partial\overline{\partial}\psi-\overline{\partial}\partial\psi=\overline{\partial}(\Omega^{\prime}+\partial\psi)+\partial\mathcal{H}(\Omega(\phi))=0\,. |  | (3.11) |

However, using Kähler identities, we have: ∂ℋ⁡(Ω⁡(ϕ))=0\partial\mathcal{H}(\Omega(\phi))=0, thus Ω′+∂ψ=c​Ω\Omega^{\prime}+\partial\psi=c\Omega for some constant c∈ℂc\in\mathbb{C} by compactness. Thus, to show that ([3.8](#S3.E8 "In Proof. ‣ 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) is true, it remains to compute the intersection products. In particular, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (d​Ωtd​t|t=0,d​Ωtd​t|t=0)=(Ω′,Ω′)+(Ω⁡(ϕ),Ω⁡(ϕ)),\displaystyle\left(\frac{{\mathrm{d}}\Omega\_{t}}{{\mathrm{d}}t}\bigg|\_{t=0},\frac{{\mathrm{d}}\Omega\_{t}}{{\mathrm{d}}t}\bigg|\_{t=0}\right)=(\Omega^{\prime},\Omega^{\prime})+(\Omega(\phi),\Omega(\phi))\,, |  | (3.12) |

where the (Ω′,Ω′)(\Omega^{\prime},\Omega^{\prime}) can be decomposed as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Ω′,Ω′)=(c​Ω−∂ψ,c​Ω−∂ψ)=|c|2​(Ω,Ω)+(∂ψ,∂ψ),\displaystyle(\Omega^{\prime},\Omega^{\prime})=(c\Omega-\partial\psi,c\Omega-\partial\psi)=|c|^{2}(\Omega,\Omega)+(\partial\psi,\partial\psi)\,, |  | (3.13) |

where we have used ∂Ω=0\partial\Omega=0. Note that (∂ψ,∂ψ)(\partial\psi,\partial\psi) is not necessarily zero. Similarly, we may decompose (Ω⁡(ϕ),Ω⁡(ϕ))(\Omega(\phi),\Omega(\phi)) as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Ω⁡(ϕ),Ω⁡(ϕ))=(ℋ​Ω​(ϕ)−∂¯​ψ,ℋ​Ω​(ϕ)−∂¯​ψ)=(ℋ​Ω​(ϕ),ℋ​Ω​(ϕ))+(∂¯​ψ,∂¯​ψ),\displaystyle(\Omega(\phi),\Omega(\phi))=(\mathcal{H}\Omega(\phi)-\overline{\partial}\psi,\mathcal{H}\Omega(\phi)-\overline{\partial}\psi)=(\mathcal{H}\Omega(\phi),\mathcal{H}\Omega(\phi))+(\overline{\partial}\psi,\overline{\partial}\psi)\,, |  | (3.14) |

where we have used the harmonicity condition. A simple integration by parts argument and application of Stokes’ theorem gives: (∂¯​ψ,∂¯​ψ)=−(ψ,∂∂¯​ψ)(\overline{\partial}\psi,\overline{\partial}\psi)=-(\psi,\partial\overline{\partial}\psi) and (∂ψ,∂ψ)=−(ψ,∂¯​∂ψ)=(ψ,∂∂¯​ψ)(\partial\psi,\partial\psi)=-(\psi,\overline{\partial}\partial\psi)=(\psi,\partial\overline{\partial}\psi), thus, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (d​Ωtd​t|t=0,d​Ωtd​t|t=0)=|c|2​(Ω,Ω)+(ℋ​Ω​(ϕ),ℋ​Ω​(ϕ)).\displaystyle\left(\frac{{\mathrm{d}}\Omega\_{t}}{{\mathrm{d}}t}\bigg|\_{t=0},\frac{{\mathrm{d}}\Omega\_{t}}{{\mathrm{d}}t}\bigg|\_{t=0}\right)=|c|^{2}(\Omega,\Omega)+\big(\mathcal{H}\Omega(\phi),\mathcal{H}\Omega(\phi)\big)\,. |  | (3.15) |

Finally, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (d​Ωtd​t|t=0,Ω)=(Ω′,Ω)=(c​Ω−∂ψ,Ω)=c⁡(Ω,Ω).\displaystyle\left(\frac{{\mathrm{d}}\Omega\_{t}}{{\mathrm{d}}t}\bigg|\_{t=0},\Omega\right)=(\Omega^{\prime},\Omega)=(c\Omega-\partial\psi,\Omega)=c(\Omega,\Omega)\,. |  | (3.16) |

From this, direct calculation shows that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | −(d​Ωtd​t|t=0,d​Ωtd​t|t=0)(Ω,Ω)+|(Ω,d​Ωtd​t|t=0)|2(Ω,Ω)2=−(ℋ​Ω​(ϕ),ℋ​Ω​(ϕ))(Ω,Ω).\displaystyle-\frac{\displaystyle\left(\frac{{\mathrm{d}}\Omega\_{t}}{{\mathrm{d}}t}\bigg|\_{t=0},\frac{{\mathrm{d}}\Omega\_{t}}{{\mathrm{d}}t}\bigg|\_{t=0}\right)}{(\Omega,\Omega)}+\frac{\displaystyle\left|\left(\Omega,\frac{{\mathrm{d}}\Omega\_{t}}{{\mathrm{d}}t}\bigg|\_{t=0}\right)\right|^{2}}{(\Omega,\Omega)^{2}}=-\frac{\big(\mathcal{H}\Omega(\phi),\mathcal{H}\Omega(\phi)\big)}{(\Omega,\Omega)}\,. |  | (3.17) |

The result then follows from the statement of Lemma [2](#Thmlemma2 "Lemma 2. ‣ 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications"), where we have used the fact that ℋ⁡(Ω⁡(ϕ))=Ω⁡(ℋ​ϕ)\mathcal{H}(\Omega(\phi))=\Omega(\mathcal{H}\phi), which follows from Ricci-flatness of XtX\_{t} [[45](#bib.bib45)]. ∎

### 3.2 Constructing the Kodaira–Spencer map

In this section we shall briefly review the method described in [[31](#bib.bib31)] and show that it naturally generalizes to Calabi–Yau complete intersections. The main idea described in [[31](#bib.bib31)] is to find explicit form of the decomposition: ([3.6](#S3.E6 "In 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) and then apply numerical integration techniques to compute the canonical intersection pairings ([3.17](#S3.E17 "In Proof. ‣ 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")). As described in Section [3.1](#S3.SS1 "3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications"), the (n,0)(n,0)-terms in the decomposition ([3.6](#S3.E6 "In 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) now contribute non-trivially to the Weil–Petersson metric and both components must be computed explicitly.

First, let us briefly set up the notation defining the complete intersection Calabi–Yau XX. Recall that the information defining XX can be given as a configuration matrix:

|  |  |  |  |
| --- | --- | --- | --- |
|  | X=[n1nmq11…qK1⋱q1N…qKN],\displaystyle X=\left[\begin{matrix}\begin{matrix}n\_{1}\\ \vdots\\ n\_{m}\end{matrix}\penalty\ \vline\penalty\ \begin{matrix}q\_{1}^{1}&\dots&q\_{K}^{1}\\ \vdots&\ddots&\vdots\\ q\_{1}^{N}&\dots&q\_{K}^{N}\end{matrix}\end{matrix}\right]\,, |  | (3.18) |

where, after fixing the point in the complex structure moduli, the defining equations are given by polynomials: {pj}j=1K\{p\_{j}\}\_{j=1}^{K} of appropriate degrees specified by ([3.18](#S3.E18 "In 3.2 Constructing the Kodaira–Spencer map ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")). To describe the deformations of XX, we may identify H1​(TX)H^{1}(T\_{X}) with a quotient [[46](#bib.bib46)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H1(TX)≃⨁l=1KH0(X,𝒪X(ql))/∼∋F.\displaystyle H^{1}(T\_{X})\simeq\bigoplus\_{l=1}^{K}H^{0}(X,\mathcal{O}\_{X}(q\_{l}))\bigg/\penalty\sim\qquad\ni F\,. |  | (3.19) |

Thus, suppose ζt:X⟶Xt\zeta\_{t}\colon X\longrightarrow X\_{t} denotes the diffeomorphism induced by the deformation FF in ([3.19](#S3.E19 "In 3.2 Constructing the Kodaira–Spencer map ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")), then we have pj​(ζt)+t​Fj​(ζt)=0p\_{j}(\zeta\_{t})+tF\_{j}(\zeta\_{t})=0 for all j∈{1,…,K}j\in\{1,\dots,K\}. Let {Zj}j=1M\{Z^{j}\}\_{j=1}^{M} for M=n1+⋯+nNM=n\_{1}+\dots+n\_{N} be the set of local coordinates on the ambient space: A=ℙn1×⋯×ℙnNA=\mathbb{P}^{n\_{1}}\times\cdots\times\mathbb{P}^{n\_{N}}. Let ξ∈TX\xi\in T\_{X} be the generator of the diffeomorphism corresponding to FF. Note that ξ\xi is a non-holomorphic section of TAT\_{A} that satisfies:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂pj∂Zk​ξk+Fj=0,for all​j∈{1,⋯,K}.\displaystyle\frac{\partial p\_{j}}{\partial Z^{k}}\xi^{k}+F\_{j}=0,\quad\text{for all}\penalty\ j\in\{1,\cdots,K\}\,. |  | (3.20) |

From above it follows that the solution for ξ\xi is not unique. In [[31](#bib.bib31), [15](#bib.bib15)] the authors give examples of particular solutions to ([3.20](#S3.E20 "In 3.2 Constructing the Kodaira–Spencer map ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")). We shall instead derive a general solution. Let Jac⁡(p)\mathrm{Jac}(p) denote the matrix {∂pj/∂Zk}j,k\{\partial p\_{j}/\partial Z^{k}\}\_{j,k}. Then, after fixing a metric gg on the ambient space, it suffices to compute Moore–Penrose pseudoinverse with respect to metric gg and kernel of Jac⁡(p)\mathrm{Jac}(p). Explicitly, the right pseudoinverse Jac​(p)+\mathrm{Jac}(p)^{+} with respect to gg is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Jac​(p)+=Jac⁡(p)¯⋅(Jac⁡(p)⋅Jac⁡(p)¯)−1,\displaystyle\mathrm{Jac}(p)^{+}=\overline{\mathrm{Jac}(p)}\cdot\big(\mathrm{Jac}(p)\cdot\overline{\mathrm{Jac}(p)}\big)^{-1}\,, |  | (3.21) |

where all inner products are induced by the metric gg. Thus, a general solution to ([3.20](#S3.E20 "In 3.2 Constructing the Kodaira–Spencer map ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ξk=(Jac​(p)+)k​j​Fj+∑ici​χik,for​ci∈ℂ,\displaystyle\xi^{k}=(\mathrm{Jac(p)}^{+})^{kj}F\_{j}+\sum\_{i}c\_{i}\chi^{k}\_{i},\quad\text{for}\penalty\ c\_{i}\in\mathbb{C}\,, |  | (3.22) |

where ℂ​{χi}i=ker⁡Jac⁡(p)\mathbb{C}\{\chi\_{i}\}\_{i}=\ker{\mathrm{Jac}(p)}. Note that the expressions given in [[31](#bib.bib31), [15](#bib.bib15)] correspond to the coefficients ci=0c\_{i}=0 ([3.22](#S3.E22 "In 3.2 Constructing the Kodaira–Spencer map ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")), but they differ by the choice of the metric gg on the ambient space.

From the non-holomorphic local vector field ξ\xi corresponding to the deformation FF, we may compute the Kodaira–Spencer class using the method described in Section [3.1](#S3.SS1 "3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications") as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ρ⁡(∂∂t)=[∂¯​ξ].\displaystyle\rho\left(\frac{\partial}{\partial t}\right)=\left[\overline{\partial}\xi\right]\,. |  | (3.23) |

Which allows us to compute unnormalized Yukawa coupling using the Kodaira–Spencer map in the following manner, let ξi\xi\_{i} be the vector field corresponding to ρ⁡(∂/∂ti)\rho(\partial/\partial t\_{i}), then, the unnormalized Yukawa coupling κi​j​k\kappa\_{ijk} is given by the following integral:

|  |  |  |  |
| --- | --- | --- | --- |
|  | κi​j​k=∫XΩα​β​γ​∂ξiα∂z¯μ​∂ξjβ∂z¯ν​∂ξkγ∂z¯δ​Ω∧d​z¯μ∧d​z¯ν∧d​z¯δ\displaystyle\kappa\_{ijk}=\int\_{X}\Omega\_{\alpha\beta\gamma}\frac{\partial\xi^{\alpha}\_{i}}{\partial\overline{z}^{\mu}}\frac{\partial\xi^{\beta}\_{j}}{\partial\overline{z}^{\nu}}\frac{\partial\xi^{\gamma}\_{k}}{\partial\overline{z}^{\delta}}\penalty\ \Omega\wedge d\overline{z}^{\mu}\wedge d\overline{z}^{\nu}\wedge d\overline{z}^{\delta} |  | (3.24) |

Thus, what remains to compute is the decomposition ([3.6](#S3.E6 "In 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")). In the case of hypersurfaces, this has been done in [[31](#bib.bib31)]. We show that this naturally generalizes to arbitrary complete intersections with codim>1\mathrm{codim}>1. This can be done by differentiating the Poincaré residue equation. First, note that for a sufficiently small t>0t>0, the vector field ξ\xi in TAT\_{A} induces an automorphism of the ambient space AA:

|  |  |  |  |
| --- | --- | --- | --- |
|  | A{\lx@inpgf@ignorespaces A}At{\lx@inpgf@ignorespaces A\_{t}}X{\lx@inpgf@ignorespaces X}Xt{\lx@inpgf@ignorespaces X\_{t}}ζˇt\scriptstyle{\lx@inpgf@ignorespaces\check{\zeta}\_{t}}ζt\scriptstyle{\lx@inpgf@ignorespaces\zeta\_{t}} |  | (3.25) |

Let Ut⊂AtU\_{t}\subset A\_{t} be some open set, and pick local coordinates (Zt1,…,ZtM)(Z\_{t}^{1},\dots,Z\_{t}^{M}) on UtU\_{t}, such that Z0j=ZjZ\_{0}^{j}=Z^{j} for all jj, where M=dimAtM=\dim{A\_{t}}. Using the adjunction formula, we may relate canonical bundles of XtX\_{t} and AtA\_{t} as: KXt=KAt⊗det⁡(𝒩Xt|At)|XtK\_{X\_{t}}=K\_{A\_{t}}\otimes\det{\mathcal{N}\_{X\_t|A\_t}}\big|\_{X\_{t}}, which leads to:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ωt∧d​pt1∧⋯∧d​ptK=d​Zt1∧⋯∧d​ZtM,\displaystyle\Omega\_{t}\wedge{\mathrm{d}}p^{1}\_{t}\wedge\cdots\wedge{\mathrm{d}}p^{K}\_{t}={\mathrm{d}}Z\_{t}^{1}\wedge\cdots\wedge{\mathrm{d}}Z\_{t}^{M}\,, |  | (3.26) |

where Ωt∈Γ⁡(Xt,KXt)\Omega\_{t}\in\Gamma(X\_{t},K\_{X\_{t}}). Following [[31](#bib.bib31)], we consider perturbation of ([3.26](#S3.E26 "In 3.2 Constructing the Kodaira–Spencer map ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) at t=0t=0 in the direction ξ∈TA\xi\in T\_{A}. In particular, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​t​(d​Zt1∧⋯∧d​ZtM)|t=0=dd​t​det⁡(δkj+t​∂ξj∂Zk)j,k|t=0​d​Z1∧⋯∧d​ZM+\displaystyle\frac{{\mathrm{d}}}{{\mathrm{d}}t}\left({\mathrm{d}}Z\_{t}^{1}\wedge\cdots\wedge{\mathrm{d}}Z\_{t}^{M}\right)\bigg|\_{t=0}=\frac{{\mathrm{d}}}{{\mathrm{d}}t}\det\left(\delta\_{k}^{j}+t\frac{\partial\xi^{j}}{\partial Z^{k}}\right)\_{j,k}\bigg|\_{t=0}{\mathrm{d}}Z^{1}\wedge\cdots\wedge{\mathrm{d}}Z^{M}+ |  | (3.27) |
|  |  |  |
| --- | --- | --- |
|  | +∑j,k=1M∂ξj∂Z¯kdZ1∧⋯∧d​Zj^∧dZ¯k∧⋯∧dZM.\displaystyle+\sum\_{j,k=1}^{M}\frac{\partial\xi^{j}}{\partial\overline{Z}^{k}}{\mathrm{d}}Z^{1}\wedge\cdots\wedge\widehat{{\mathrm{d}}Z^{j}}\wedge{\mathrm{d}}\overline{Z}^{k}\wedge\cdots\wedge{\mathrm{d}}Z^{M}\,. |  |

Furthermore, note that:

|  |  |  |  |
| --- | --- | --- | --- |
|  | dd​t​(d​ptj)|t=0=d⁡(∂pj∂Zk​ξk+Fj)=0,\displaystyle\frac{{\mathrm{d}}}{{\mathrm{d}}t}(dp\_{t}^{j})\bigg|\_{t=0}={\mathrm{d}}\left(\frac{\partial p^{j}}{\partial Z^{k}}\xi^{k}+F^{j}\right)=0\,, |  | (3.28) |

where we have used ([3.20](#S3.E20 "In 3.2 Constructing the Kodaira–Spencer map ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")). This implies that: d​pt1∧⋯∧d​ptK=d​p1∧⋯∧d​pK{\mathrm{d}}p\_{t}^{1}\wedge\dots\wedge{\mathrm{d}}p\_{t}^{K}={\mathrm{d}}p^{1}\wedge\dots\wedge{\mathrm{d}}p^{K}. Thus, the derivative ([3.6](#S3.E6 "In 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) satisfies the following relation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | d​Ωtd​t|t=0∧d​p1∧⋯∧d​pK|X=Tr​Jac​(ξ)​d​Z1∧⋯∧d​ZK|X+\displaystyle\frac{{\mathrm{d}}\Omega\_{t}}{{\mathrm{d}}t}\bigg|\_{t=0}\wedge{\mathrm{d}}p^{1}\wedge\cdots\wedge{\mathrm{d}}p^{K}\bigg|\_{X}=\mathrm{Tr}\penalty\ \mathrm{Jac}(\xi)\penalty\ {\mathrm{d}}Z^{1}\wedge\cdots\wedge{\mathrm{d}}Z^{K}\bigg|\_{X}+ |  | (3.29) |
|  |  |  |
| --- | --- | --- |
|  | +∑j,k=1M∂ξj∂Z¯kdZ1∧⋯∧d​Zj^∧dZ¯k∧⋯∧dZM|X.\displaystyle+\sum\_{j,k=1}^{M}\frac{\partial\xi^{j}}{\partial\overline{Z}^{k}}{\mathrm{d}}Z^{1}\wedge\cdots\wedge\widehat{{\mathrm{d}}Z^{j}}\wedge{\mathrm{d}}\overline{Z}^{k}\wedge\cdots\wedge{\mathrm{d}}Z^{M}\bigg|\_{X}\,. |  |

Let α∈Γ⁡(X,Ωn,0)\alpha\in\Gamma(X,\Omega^{n,0}) and β∈Γ⁡(X,Ωn−1,1)\beta\in\Gamma(X,\Omega^{n-1,1}) be the (n,0)(n,0) and (n−1,1)(n-1,1) terms in the decomposition ([3.6](#S3.E6 "In 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")), respectively. Then, the forms can be expanded as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | α=f⁡(Z)​d​Z1∧⋯∧d​Zn,β=∑j,k=1ngkj​(Z)​d​Z1∧⋯∧d​Zj^∧⋯∧d​Zn∧d​Z¯k.\displaystyle\alpha=f(Z){\mathrm{d}}Z^{1}\wedge\cdots\wedge{\mathrm{d}}Z^{n},\quad\beta=\sum\_{j,k=1}^{n}g\_{k}^{j}(Z){\mathrm{d}}Z^{1}\wedge\cdots\wedge\widehat{{\mathrm{d}}Z^{j}}\wedge\cdots\wedge{\mathrm{d}}Z^{n}\wedge{\mathrm{d}}\overline{Z}^{k}\,. |  | (3.30) |

Combining ([3.30](#S3.E30 "In 3.2 Constructing the Kodaira–Spencer map ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) and ([3.26](#S3.E26 "In 3.2 Constructing the Kodaira–Spencer map ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) and solving for f⁡(Z)f(Z) we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | f⁡(Z)=Tr​Jac​(ξ)/det⁡(∂pj∂Zn+k)j,k=1K.\displaystyle f(Z)=\mathrm{Tr}\penalty\ \mathrm{Jac}(\xi)\Big/\det\Big({\frac{\partial p^j}{\partial Z^{n+k}}}\Big)\_{j,k=1}^{K}\,. |  | (3.31) |

Similarly, solving for gkj​(Z)g\_{k}^{j}(Z), we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | gkj​(Z)=(−1)n−jdet⁡(∂pj′∂Zn+k′)j′,k′=1K​[∂ξj∂Z¯k+∑l=1K∂ξj∂Z¯n+l​∂Z¯n+l∂Z¯k],\displaystyle g\_{k}^{j}(Z)=\frac{\displaystyle(-1)^{n-j}}{\displaystyle\det\Big({\frac{\partial p^{j'}} {\partial Z^{n+{k'}}}}\Big)\_{j^{\prime},k^{\prime}=1}^{K}}\left[\frac{\partial\xi^{j}}{\partial\overline{Z}^{k}}+\sum\_{l=1}^{K}\frac{\partial\xi^{j}}{\partial\overline{Z}^{n+l}}\frac{\partial\overline{Z}^{n+l}}{\partial\overline{Z}^{k}}\right]\,, |  | (3.32) |

where we have applied pullback i:X↪Ai\colon X\hookrightarrow A as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | i∗​d​Z¯n+l=∑k=1n∂Z¯n+l∂Z¯k​d​Z¯k.\displaystyle i^{\*}{\mathrm{d}}\overline{Z}^{n+l}=\sum\_{k=1}^{n}\frac{\partial\overline{Z}^{n+l}}{\partial\overline{Z}^{k}}{\mathrm{d}}\overline{Z}^{k}\,. |  | (3.33) |

Combining the results, we see that ([3.31](#S3.E31 "In 3.2 Constructing the Kodaira–Spencer map ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) and ([3.32](#S3.E32 "In 3.2 Constructing the Kodaira–Spencer map ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) are natural generalizations of the results of [[31](#bib.bib31)] in the case of K>1K>1.

## 4 Numerical results

Here we compute the Weil–Petersson metric using the Kodaira–Spencer map, and thereby obtain the physical Yukawa couplings, for a range of different complete intersection Calabi–Yau manifolds. This requires the numerical evaluation of integrals over the Calabi–Yau fibres XtX\_{t}, which are approximated by Monte Carlo integration over XtX\_{t},

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫Xt𝗏𝗈𝗅gt​f≃1N​∑k=1Nf⁡(pk(t)),\int\_{X\_{t}}\mathsf{vol}\_{g\_{t}}f\simeq\frac{1}{N}\sum\_{k=1}^{N}f(p^{(t)}\_{k})\,, |  | (4.1) |

where the distribution of the random points {pk(t)}k=1N\{p^{(t)}\_{k}\}\_{k=1}^{N} is chosen to be uniform with respect to the Fubini–Study metric on the embedding space ℙn1×⋯×ℙnK⊃Xt\mathbb{P}^{n\_{1}}\times\cdots\times\mathbb{P}^{n\_{K}}\supset X\_{t} [[47](#bib.bib47), [48](#bib.bib48)]. Here N=250,000N=250,000 in all experiments unless stated otherwise. All computations are performed using our JAX library [[24](#bib.bib24)] and some make use of the point sampling package of cymetric [[23](#bib.bib23)].

### 4.1 Mirror of ℙ5​[3,3]\mathbb{P}^{5}[3,3]

Consider the Calabi–Yau threefold XX belonging to the deformation space ℙ5​[3,3]\mathbb{P}^{5}[3,3] via the following system of defining equations:

|  |  |  |  |
| --- | --- | --- | --- |
|  | x03+x13+x23−3​ψ​x3​x4​x5=0,x33+x43+x53−3​ψ​x0​x1​x2=0.x\_{0}^{3}+x\_{1}^{3}+x\_{2}^{3}-3\psi\,x\_{3}x\_{4}x\_{5}=0\,,\qquad x\_{3}^{3}+x\_{4}^{3}+x\_{5}^{3}-3\psi\,x\_{0}x\_{1}x\_{2}=0\,. |  | (4.2) |

This space has h2,1=73h^{2,1}=73 and h1,1=1h^{1,1}=1 and it is a member of the one parameter family of Calabi–Yau manifolds considered, e.g., in [[49](#bib.bib49)].
Its mirror, X~\widetilde{X} (with swapped Hodge numbers), is constructed as a blowup of a finite quotient of this same zero-locus. That way, the complex structure parameter ψ\psi in the description of XX one-to-one corresponds to the Kähler class of the mirror, X~\widetilde{X}. Note however that the limit ψ→0\psi\to 0 makes the intersection of the two quadrics ([4.2](#S4.E2 "In 4.1 Mirror of ℙ^5⁢[3,3] ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) (as well as their finite quotient) singular along a network of curves. This singularization of both XX and X~\widetilde{X} gives rise to the pole-singularity at ψ→0\psi\to 0 seen in the plots in Figure [1](#S4.F1 "Figure 1 ‣ 4.1 Mirror of ℙ^5⁢[3,3] ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications") and Figure [2](#S4.F2 "Figure 2 ‣ 4.1 Mirror of ℙ^5⁢[3,3] ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications").

The grid of points in Figure [1](#S4.F1 "Figure 1 ‣ 4.1 Mirror of ℙ^5⁢[3,3] ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications") corresponds to the Kodaira–Spencer computation, and we observe good agreement between the two methods. The modulus dependent Yukawa coupling is presented in Figure [1](#S4.F1 "Figure 1 ‣ 4.1 Mirror of ℙ^5⁢[3,3] ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications")(b) where we again obtain a matching of the results from both techniques.

### 4.2 Quintic and the Gepner model Y4;5Y\_{4;5}

One of the simplest exactly soluble models is given by a Gepner model Y4;5Y\_{4;5} [[50](#bib.bib50), [32](#bib.bib32), [51](#bib.bib51), [52](#bib.bib52)], which corresponds to a specific point in the moduli of the quintic threefold ℙ4​[5]\mathbb{P}^{4}[5]. It has been shown in [[32](#bib.bib32)] that the normalized Yukawa couplings can be expressed as powers of a constant κ\kappa given by a ratio of Γ\Gamma-functions:

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ=[Γ​(3/5)3​Γ​(1/5)Γ​(2/5)3​Γ​(4/5)]1/2≈1.09236.\displaystyle\kappa=\left[\frac{\Gamma(3/5)^{3}\Gamma(1/5)}{\Gamma(2/5)^{3}\Gamma(4/5)}\right]^{1/2}\approx 1.09236\,. |  | (4.3) |

In particular, in the model Y4;5Y\_{4;5}, we consider a quintic threefold XX defined as a zero locus of Fermat quintic Z05+⋯+Z45=0Z\_{0}^{5}+\dots+Z\_{4}^{5}=0 under quotient G=ℤ5×ℤ5′G=\mathbb{Z}\_{5}\times\mathbb{Z}\_{5}^{\prime}. The resulting Calabi–Yau manifold has h1,1​(X/G)=1h^{1,1}(X/G)=1 and h2,1​(X/G)=5h^{2,1}(X/G)=5 and Euler number −200/(5×5)=−8-200/(5\times 5)=-8 (see: [[53](#bib.bib53), [54](#bib.bib54)]) hence a heterotic string compactification with standard embedding will yield four chiral generations. One can show that the group GG is freely acting, with its generators being

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℤ5:\displaystyle\mathbb{Z}\_{5}\,: | zj→αj​zj,\displaystyle\quad z\_{j}\rightarrow\alpha^{j}z\_{j}\,, |  | (4.4) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℤ5′:\displaystyle\mathbb{Z}\_{5}^{\prime}\,: | zj→zj+1,\displaystyle\quad z\_{j}\rightarrow z\_{j+1}\,, |  | (4.5) |

The monomial representatives of the H2,1​(X/G)≃H1​(TX/G)H^{2,1}(X/G)\simeq H^{1}(T\_{X/G}) are shown in Table [1](#S4.T1 "Table 1 ‣ 4.2 Quintic and the Gepner model 𝑌_{4;5} ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications").

| Family | Monomial FF | Comment |
| --- | --- | --- |
| 11 | Zi2​Zj3Z\_{i}^{2}Z\_{j}^{3} | i≠ji\neq j |
| 22 | Zi​Zj​Zk3Z\_{i}Z\_{j}Z\_{k}^{3} | i≠j≠ki\neq j\neq k |
| 33 | Zi​Zj2​Zk2Z\_{i}Z\_{j}^{2}Z\_{k}^{2} | i≠j≠ki\neq j\neq k |
| 44 | Zi​Zj​Zk​Zl2Z\_{i}Z\_{j}Z\_{k}Z\_{l}^{2} | i≠j≠k≠li\neq j\neq k\neq l |
| 55 | Z0​Z1​Z2​Z3​Z4Z\_{0}Z\_{1}Z\_{2}Z\_{3}Z\_{4} | – |

The Yukawa couplings for the Gepner model Y4;5Y\_{4;5} were already computed in [[32](#bib.bib32)]. We want to employ the method described in Section [3.2](#S3.SS2 "3.2 Constructing the Kodaira–Spencer map ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications") in order to make a direct comparison. We first show that monomial families in Table [1](#S4.T1 "Table 1 ‣ 4.2 Quintic and the Gepner model 𝑌_{4;5} ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications") indeed form an orthogonal basis. In the basis of [1](#S4.T1 "Table 1 ‣ 4.2 Quintic and the Gepner model 𝑌_{4;5} ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications"), the Weil–Petersson metric entries are given in the grayscale grid of Figure [3](#S4.F3 "Figure 3 ‣ 4.2 Quintic and the Gepner model 𝑌_{4;5} ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications"). Evidently, the off-diagonal components vanish, wherefore the Yukawa couplings can be computed using ([2.11](#S2.E11 "In 2 Heterotic Yukawa couplings ‣ Physical Yukawa Couplings in Heterotic String Compactifications")).

![Refer to caption](2401.15078v2/wp.png)

Using numerical integration techniques, we compute the 95%95\% confidence intervals of the values for the normalized Yukawa couplings for the quintic quotient model. In Figure [4](#S4.F4 "Figure 4 ‣ 4.2 Quintic and the Gepner model 𝑌_{4;5} ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications") we contrast our results with those of [[32](#bib.bib32)].

As can be observed in Figure [4](#S4.F4 "Figure 4 ‣ 4.2 Quintic and the Gepner model 𝑌_{4;5} ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications"), the numerical values computed using the methods described in the Section [3.2](#S3.SS2 "3.2 Constructing the Kodaira–Spencer map ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications") are within the margin of the error of the exact results computed in the work [[32](#bib.bib32)].

Finally, note that the coupling corresponding to the family 55 in Table [1](#S4.T1 "Table 1 ‣ 4.2 Quintic and the Gepner model 𝑌_{4;5} ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications") matches the coupling of the mirror quintic X~\widetilde{X} which has h2,1​(X~)=1h^{2,1}(\widetilde{X})=1. In particular, recall that the invariant/normalized Yukawa coupling defined in [[55](#bib.bib55)] attains value of κ5\kappa^{5} at Landau–Ginzburg point in the complex structure moduli of X~\widetilde{X}. From Figure [4](#S4.F4 "Figure 4 ‣ 4.2 Quintic and the Gepner model 𝑌_{4;5} ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications"), the numerical value corresponding to this family is:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Y5,5,5=1.550±0.002,\displaystyle Y\_{5,5,5}=1.550\pm 0.002\,, |  | (4.6) |

which is close to the exact value of κ5≈1.555\kappa^{5}\approx 1.555.

### 4.3 Tian–Yau quotient

We start with a complete intersection in ℙ3×ℙ3\mathbb{P}^{3}\times\mathbb{P}^{3} given by the following configuration matrix

|  |  |  |  |
| --- | --- | --- | --- |
|  | X=[33310013].\displaystyle X=\left[\begin{matrix}\begin{matrix}3\\ 3\end{matrix}\penalty\ \vline\penalty\ \begin{matrix}3&1&0\\ 0&1&3\\ \end{matrix}\end{matrix}\right]\,. |  | (4.7) |

All manifolds in this deformation class have Hodge numbers h1,1=14h^{1,1}=14 and h1,2=23h^{1,2}=23, and so χ=−18\chi=-18.
To be specific, we choose the defining polynomials to be of the form

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | | | | |
|  | p1\displaystyle p^{1} | =13​(x03+x13+x23+x33)=0,\displaystyle=\tfrac{1}{3}\left(x\_{0}^{3}+x\_{1}^{3}+x\_{2}^{3}+x\_{3}^{3}\right)=0\,, |  | (4.8a) |
|  | p2\displaystyle p^{2} | =x0​y0+x1​y1+x2​y2+x3​y3=0,\displaystyle=x\_{0}y\_{0}+x\_{1}y\_{1}+x\_{2}y\_{2}+x\_{3}y\_{3}=0\,, |  | (4.8b) |
|  | p3\displaystyle p^{3} | =13​(y03+y13+y23+y33)=0,\displaystyle=\tfrac{1}{3}\left(y\_{0}^{3}+y\_{1}^{3}+y\_{2}^{3}+y\_{3}^{3}\right)=0\,, |  | (4.8c) |

where, following the notation of [[33](#bib.bib33)] we take xx and yy to denote coordinates in the first and second ℙ3\mathbb{P}^{3}s respectively. The manifold ([4.8](#S4.E8 "In 4.3 Tian–Yau quotient ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) has a freely acting ℤ3\mathbb{Z}\_{3} symmetry specified as follows

|  |  |  |  |
| --- | --- | --- | --- |
|  | {(x0,x1,x2,x3)→(x0,α2​x1,α​x2,α​x3),(y0,y1,y2,y3)→(y0,α​y1,α2​y2,α2​y3),\bigg\{\begin{array}[]{@{}rl}(x\_{0},x\_{1},x\_{2},x\_{3})&\rightarrow(x\_{0},\alpha^{2}x\_{1},\alpha x\_{2},\alpha x\_{3})\,,\\ (y\_{0},y\_{1},y\_{2},y\_{3})&\rightarrow(y\_{0},\alpha y\_{1},\alpha^{2}y\_{2},\alpha^{2}y\_{3})\,,\end{array} |  | (4.9) |

with α=e2​π​i/3\alpha=e^{2\pi{\rm i}/3}. The Tian–Yau manifold is constructed by quotienting out the freely acting ℤ3\mathbb{Z}\_{3} symmetry ([4.9](#S4.E9 "In 4.3 Tian–Yau quotient ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications")), yielding a quotient Calabi–Yau manifold with χ=−6\chi=-6 [[56](#bib.bib56), [4](#bib.bib4)].

Similarly as in the case of the quintic threefold discussed in Section [4.2](#S4.SS2 "4.2 Quintic and the Gepner model 𝑌_{4;5} ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications"), we consider the orthogonal basis of H1​(TX/ℤ3)H^{1}(T\_{X/\mathbb{Z}\_{3}}) specified by the corresponding monomial representatives shown in Table [2](#S4.T2 "Table 2 ‣ 4.3 Tian–Yau quotient ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications"), constructed by Gram–Schmidt orthogonalization using the inner product defined by the
Weil–Petersson metric.

| Family | Monomial FF |
| --- | --- |
| λ1\lambda\_{1} | x0​x1​x2​e1x\_{0}x\_{1}x\_{2}\,e\_{1} |
| λ2\lambda\_{2} | x0​x1​x3​e1x\_{0}x\_{1}x\_{3}\,e\_{1} |
| λ3\lambda\_{3} | y0​y1​y2​e3y\_{0}y\_{1}y\_{2}\,e\_{3} |
| λ4\lambda\_{4} | y0​y1​y3​e3y\_{0}y\_{1}y\_{3}\,e\_{3} |
| λ5\lambda\_{5} | x3​y3​e2x\_{3}y\_{3}\,e\_{2} |
| λ6\lambda\_{6} | 18​(x3​y3+3​x2​y2)​e2\displaystyle\frac{1}{\sqrt{8}}(x\_{3}y\_{3}+3x\_{2}y\_{2})\,e\_{2} |
| λ7\lambda\_{7} | 38​(x0​y0−x1​y1)​e2\displaystyle\sqrt{\frac{3}{8}}(x\_{0}y\_{0}-x\_{1}y\_{1})\,e\_{2} |
| λ8\lambda\_{8} | x2​y3​e2x\_{2}y\_{3}\,e\_{2} |
| λ9\lambda\_{9} | x3​y2​e2x\_{3}y\_{2}\,e\_{2} |

In Table [2](#S4.T2 "Table 2 ‣ 4.3 Tian–Yau quotient ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications") we have chosen {ej}j\{e\_{j}\}\_{j} to be such that 𝒩X|ℙ3×ℙ3≃𝒪⁡(3,0)​e1⊕𝒪⁡(1,1)​e2⊕𝒪⁡(0,3)​e3\mathcal{N}\_{X|\mathbb{P}^{3}\times\mathbb{P}^{3}}\simeq\mathcal{O}(3,0)\,e\_{1}\oplus\mathcal{O}(1,1)\,e\_{2}\oplus\mathcal{O}(0,3)\,e\_{3}.
Using the numerical method discussed in Section [3.2](#S3.SS2 "3.2 Constructing the Kodaira–Spencer map ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications"), we compute the unnormalized Yukawa couplings:

|  |  |  |  |
| --- | --- | --- | --- |
|  | κi​j​k=∫X/ℤ3Ω∧Ω⁡(λi,λj,λk),\displaystyle\kappa\_{ijk}=\int\_{X/\mathbb{Z}\_{3}}\Omega\wedge\Omega(\lambda\_{i},\lambda\_{j},\lambda\_{k})\,, |  | (4.10) |

and verify the results by comparing the ratios to the Table 3 of [[33](#bib.bib33)]. In particular, the values of κ^i​j​k=defκi​j​k/κ111\widehat{\kappa}\_{ijk}\stackrel{{\scriptstyle\mathrm{def}}}{{=}}\kappa\_{ijk}/\kappa\_{111} computed numerically using ([4.10](#S4.E10 "In 4.3 Tian–Yau quotient ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) and compared to [[33](#bib.bib33)] are shown in Figure [5](#S4.F5 "Figure 5 ‣ 4.3 Tian–Yau quotient ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications"), where we observe an exact match of the results.44
4
Except for κ246\kappa\_{246}, which is incorrectly given in [[33](#bib.bib33)] to be 00, when it should equal 8​μ\sqrt{8}\,\mu in their notation.

Before computing the normalized Yukawa couplings, we first verify that the basis specified in Table [2](#S4.T2 "Table 2 ‣ 4.3 Tian–Yau quotient ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications") is indeed orthogonal. In particular, we plot the numerical values of the Weil–Petersson metric Ni​j:=⟨λi,λj⟩WPN\_{ij}:=\langle\lambda\_{i},\lambda\_{j}\rangle\_{\mathrm{WP}} in Figure [6](#S4.F6 "Figure 6 ‣ 4.3 Tian–Yau quotient ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications"). As can be observed in Figure [6](#S4.F6 "Figure 6 ‣ 4.3 Tian–Yau quotient ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications"), the basis {λj}j\{\lambda\_{j}\}\_{j} of H1​(TX/ℤ3)H^{1}(T\_{X/\mathbb{Z}\_{3}}) is indeed orthogonal. This then allows us to use ([2.11](#S2.E11 "In 2 Heterotic Yukawa couplings ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) to compute normalized Yukawa couplings. We show the numerical results in Figure [7](#S4.F7 "Figure 7 ‣ 4.3 Tian–Yau quotient ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications").

![Refer to caption](2401.15078v2/x1.png)

Further we compute the moduli dependent normalized and unnormalized Yukawa couplings. Consider the following deformation of p2p\_{2}
(cf., ([4.8b](#S4.E8.2 "In 4.8 ‣ 4.3 Tian–Yau quotient ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) above, following ([57](#bib.bib57), Eq. (1))):

|  |  |  |  |
| --- | --- | --- | --- |
|  | p2=x0​y0+x1​y1+(1+ϵ)​(x2​y2+x3​y3)=0,ϵ∈ℝ.p\_{2}=x\_{0}y\_{0}+x\_{1}y\_{1}+(1+\epsilon)(x\_{2}y\_{2}+x\_{3}y\_{3})=0\,,\quad\epsilon\in\mathbb{R}\,. |  | (4.11) |

In Figure [8](#S4.F8 "Figure 8 ‣ 4.3 Tian–Yau quotient ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications"), we present the ϵ\epsilon-dependent couplings κa​a​a\kappa\_{aaa}, using the basis of [[57](#bib.bib57)] and focusing on 0≤ϵ≤20\leq\epsilon\leq 2; note that this basis differs from the one shown in Table [2](#S4.T2 "Table 2 ‣ 4.3 Tian–Yau quotient ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications"). The couplings (κ111,κ222,κ333,κ444)(\kappa\_{111},\kappa\_{222},\kappa\_{333},\kappa\_{444}) and (κ777,κ888)(\kappa\_{777},\kappa\_{888}) are respectively degenerate while the others vanish, in agreement with the results in [[57](#bib.bib57)]. In Figure [9](#S4.F9 "Figure 9 ‣ 4.3 Tian–Yau quotient ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications"), we plot the absolute value of the normalized Yukawa couplings on a logarithmic scale.55
5
Plotting absolute values shows an artificial “crossover” near ϵ≈0.20\epsilon\approx 0.20: In fact, Y888Y\_{888} and Y555Y\_{555} have opposite signs and never coincide. In turn, the physical normalization moves the actual Y222/Y555Y\_{222}/Y\_{555} “crossover” coincidence from ϵ≈0.15\epsilon\approx 0.15 in Figure [8](#S4.F8 "Figure 8 ‣ 4.3 Tian–Yau quotient ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications") to ϵ≈0.05\epsilon\approx 0.05 in Figure [9](#S4.F9 "Figure 9 ‣ 4.3 Tian–Yau quotient ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications").

Post-normalization, we note that as ϵ\epsilon increases, a hierarchy between Y5=Y555Y\_{5}=Y\_{555} and the other couplings develops,66
6
Similar hierarchies appearing after normalization have been observed for toroidal orbifolds [[58](#bib.bib58)]. and they appear to converge to different values in the large-ϵ\epsilon regime. Looking at the logarithmic plot of the absolute values for the normalized Yukawa couplings we identify a hierarchy of 10210^{2} in the couplings. We defer a further analysis of the phenomenological implications of this large-ϵ\epsilon hierarchy, as well as the κ^222/κ^555\widehat{\kappa}\_{222}/\widehat{\kappa}\_{555}“crossover” near ϵ≈0.15\epsilon\approx 0.15 in Figure [8](#S4.F8 "Figure 8 ‣ 4.3 Tian–Yau quotient ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications") to a later effort; for an early phenomenological discussion at the level of the unnormalized Yukawa textures, see also [[57](#bib.bib57)].

## 5 Machine learning harmonic representatives

### 5.1 Preliminaries

Given a Calabi–Yau (X,g,ω)(X,g,\omega), we wish to obtain an expression for forms which are harmonic with respect to the unique Ricci-flat metric gtg\_{t} in each Kähler class. Consider the complex analytic family (𝒳,B,π)(\mathcal{X},B,\pi) such that π−1​(0)=defX0=X\pi^{-1}(0)\mathrel{\overset{\scriptscriptstyle\rm def}{=}}X\_{0}=X. Any two fibres in this family are diffeomorphic as real manifolds, X0≃XtX\_{0}\simeq X\_{t}. The corresponding generator ξ\xi, of the infinitesimal diffeomorphism is a non-holomorphic section of TX0T\_{X\_{0}}. In what follows we let (E,G)(E,G) denote a holomorphic vector bundle over XX equipped with a Hermitian structure, which may be considered the data of a smoothly varying Hermitian inner product GG on each fibre ExE\_{x}. Recall ∂¯E:Ωp,q​(E)→Ωp,q+1​(E)\bar{\partial}\_{E}:\Omega^{p,q}(E)\rightarrow\Omega^{p,q+1}(E) is the natural generalisation of the Dolbeault operator to holomorphic bundle-valued forms Ωp,q​(E)\Omega^{p,q}(E). For the case where EE is the holomorphic tangent bundle TXT\_{X}, the Kähler metric gg plays the role of the fibre metric GG. In what follows we identify EE with TXT\_{X}, although in principle our method may be reproduced for an arbitrary holomorphic vector bundle if the Hermitian inner product GG is known.

We may obtain a basis for Tt​B≃H1​(X,TX)T\_{t}B\simeq H^{1}(X,T\_{X}) by first computing ξ⁡(z,z¯)\xi(z,\bar{z}) in local holomorphic coordinates {zi}i=1n\{z^{i}\}\_{i=1}^{n} on U⊂X0U\subset X\_{0}. Then one obtains a representative of the corresponding Kodaira–Spencer class as
ϕ=ϕν¯μdz¯ν¯⊗∂∂zμ=def∂¯Eξ∈H1(X,TX)\phi=\phi^{\mu}\_{\overline{\nu}}\,{\mathrm{d}}\bar{z}^{\overline{\nu}}\otimes\partialderivative{z^{\mu}}\mathrel{\overset{\scriptscriptstyle\rm def}{=}}\bar{\partial}\_{E}\xi\in H^{1}(X,T\_{X}), where ϕν¯μ​d​z¯ν¯=∂¯​ξμ\phi^{\mu}\_{\overline{\nu}}\,{\mathrm{d}}\bar{z}^{\overline{\nu}}=\bar{\partial}\xi^{\mu}. Note [ϕ]≠0[\phi]\neq 0 as ξ\xi is not globally defined. By Hodge theory, every cohomology class contains a unique harmonic representative η\eta, related to ϕ\phi through an ∂¯E\bar{\partial}\_{E}-exact correction:

|  |  |  |  |
| --- | --- | --- | --- |
|  | η=ϕ+∂¯E​𝔰∈ℋ∂¯0,1​(X,TX),𝔰∈C∞​(TX),\eta=\phi+\bar{\partial}\_{E}\,\mathfrak{s}\in\mathcal{H}\_{\bar{\partial}}^{0,1}(X,T\_{X})\,,\quad\mathfrak{s}\in C^{\infty}(T\_{X})\,, |  | (5.1) |

where 𝔰\mathfrak{s} is a non-holomorphic section of TXT\_{X}. Note that ∂¯E​η=0\bar{\partial}\_{E}\,\eta=0 locally by construction and thus the harmonicity condition reduces to ∂¯E†​η=0\bar{\partial}\_{E}^{\dagger}\eta=0, which we encode numerically.

### 5.2 Harmonic objective

To recover the (0,1)(0,1) TXT\_{X}-valued forms which are harmonic with respect to gtg\_{t}, there are a range of possibilities to pursue, owing to the rich interplay between geometry, topology and analysis realized in Hodge theory. Here η\eta is obtained through a straightforward two-stage process. First, we approximate the Ricci-flat metric for a given choice of complex structure on XX. Secondly, we fix the learned metric on XtX\_{t} and parameterize the sections sθs\_{\theta} corresponding to the basis for Tt​BT\_{t}B using a neural network with parameters θ\theta. Noting that ∂¯E†​η∈C∞​(TX)\bar{\partial}\_{E}^{\dagger}\eta\in C^{\infty}(T\_{X}), we use the natural objective for training:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℓ⁡(θ)\displaystyle\ell(\theta) | :=(∂¯E†​ηθ,∂¯E†​ηθ)=∫Xt∂¯E†​ηθ∧⋆¯E​∂¯E†​ηθ,\displaystyle:=\left(\bar{\partial}\_{E}^{\dagger}\eta\_{\theta},\bar{\partial}\_{E}^{\dagger}\eta\_{\theta}\right)=\int\_{X\_{t}}\bar{\partial}\_{E}^{\dagger}\eta\_{\theta}\wedge\bar{\star}\_{E}\bar{\partial}\_{E}^{\dagger}\eta\_{\theta}\,, |  | (5.2) |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =∫Xt𝗏𝗈𝗅gt​gμ​ν¯​(∂¯E†​ηθ)μ​(∂¯E†​ηθ¯)ν¯.\displaystyle=\int\_{X\_{t}}\mathsf{vol}\_{g\_{t}}\,g\_{\mu\overline{\nu}}(\bar{\partial}\_{E}^{\dagger}\eta\_{\theta})^{\mu}(\overline{\bar{\partial}\_{E}^{\dagger}\eta\_{\theta}})^{\overline{\nu}}\,. |  | (5.3) |

Note the expression for the Weil–Petersson metric ([3.17](#S3.E17 "In Proof. ‣ 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) simplifies to the pairing between the interior product of the respective harmonic representatives with the holomorphic (n,0)(n,0) form if the Kodaira–Spencer representative is chosen to be harmonic. For the case of a general gauge bundle where a representative of the H1​(X,E)H^{1}(X,E) cohomology may not be available, one would have to enforce the closure condition ∂¯E​η=0\bar{\partial}\_{E}\eta=0 in addition to the co-closure condition.

Note that the Ricci-flat metric gtg\_{t} does double duty in the case of the standard embedding as it naturally induces a metric on Ω0,1​(TXt)\Omega^{0,1}(T\_{X\_{t}}). To find harmonic bundle-valued representatives for a general holomorphic vector bundle VV using the objective ([5.2](#S5.E2 "In 5.2 Harmonic objective ‣ 5 Machine learning harmonic representatives ‣ Physical Yukawa Couplings in Heterotic String Compactifications")), one must compute the Hermitian metric on the fibres of VV in addition to the metric gtg\_{t}.

As an example, we consider the mirror X~\widetilde{X} of X=ℙ5​[3,3]X=\mathbb{P}^{5}[3,3], described in Section [4.1](#S4.SS1 "4.1 Mirror of ℙ^5⁢[3,3] ‣ 4 Numerical results ‣ Physical Yukawa Couplings in Heterotic String Compactifications"), parametrized by the complex structure parameter ψ\psi. We first find explicit harmonic representatives of the Kodaira–Spencer class [∂¯​ξ][\overline{\partial}\xi] via the objective ([5.2](#S5.E2 "In 5.2 Harmonic objective ‣ 5 Machine learning harmonic representatives ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) using a standard fully connected neural network with four layers with intermediate dimensions [64,32,32,48][64,32,32,48] and the Gaussian error linear unit activation function. We used the Adam optimization algorithm with a learning rate of 10−410^{-4} in all experiments. We empirically observed that the results were insensitive to the choice of hyperparameters considered. We subsequently compute the Weil–Petersson metric gψ​ψ¯g\_{\psi\overline{\psi}} on an independent validation set consisting of 250,000 fibre points for each point in moduli space. In Figure [10](#S5.F10 "Figure 10 ‣ 5.2 Harmonic objective ‣ 5 Machine learning harmonic representatives ‣ Physical Yukawa Couplings in Heterotic String Compactifications"), we plot gψ​ψ¯g\_{\psi\overline{\psi}} obtained using the intersection pairing valid for harmonic representatives ([3.17](#S3.E17 "In Proof. ‣ 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")), together with the numerical values obtained for general representatives by the Kodaira–Spencer approach, as well as the exact period computation across discrete points in complex moduli space. The evolution of the loss function ([5.2](#S5.E2 "In 5.2 Harmonic objective ‣ 5 Machine learning harmonic representatives ‣ Physical Yukawa Couplings in Heterotic String Compactifications")) throughout the training is shown on Figure [11](#S5.F11 "Figure 11 ‣ 5.2 Harmonic objective ‣ 5 Machine learning harmonic representatives ‣ Physical Yukawa Couplings in Heterotic String Compactifications") for the benchmark points ψ=0.2,0.45,1.05\psi=0.2\,,0.45\,,1.05.

We observe that the harmonic forms computed using the approximate Ricci-flat metric as input are able to recover the value of the Weil–Petersson metric away from the singularities in moduli space. This supplies an additional reassurance similar in spirit to the topological computations from local geometry in [[59](#bib.bib59)] — that numerical approximations to the Ricci-flat metric are able to yield physically meaningful data. While we have restricted our attention to the standard embedding, these results are an encouraging step towards conducting similar computations for more general gauge bundles to extract relevant effective field theory parameters. Our method provides an improved approximation to the Weil–Petersson metric over the non-harmonic representatives even near points in moduli space of the mirror ℙ5​[3,3]~\widetilde{\mathbb{P}^{5}[3,3]} close to the singularity at ψ=0\psi=0, and continues to yield the expected result near logarithmic singularities such as ψ=1\psi=1. However, the fidelity of approximation degrades as one approaches the ψ=0\psi=0 singularity; we aim to address this issue in ongoing work.

Finally, we also consider the Weil–Petersson metric of the mirror quintic ℙ4​[5]~\widetilde{\mathbb{P}^{4}[5]} at Fermat point (ψ=0\psi=0). From the machine learned harmonic representative, we obtain the value: gψ​ψ¯=0.1906g\_{\psi\overline{\psi}}=0.1906, which is well within the typical 95%95\% confidence interval of the numerical integration of the exact value [[55](#bib.bib55)]:

|  |  |  |  |
| --- | --- | --- | --- |
|  | 25​Γ​(4/5)5​Γ​(2/5)5Γ​(1/5)5​Γ​(3/5)5≈0.1922.\displaystyle 25\frac{\Gamma(4/5)^{5}\Gamma(2/5)^{5}}{\Gamma(1/5)^{5}\Gamma(3/5)^{5}}\approx 0.1922\,. |  | (5.4) |

## 6 Discussion and outlook

The as yet unrealized dream of string phenomenology is to start from a construction involving higher dimensional geometry and objects such as strings and branes to obtain an effective four-dimensional theory satisfying all known particle physics and cosmological constraints from real world experiments and observations.
Plausibly, we must look for Standard Model or beyond the Standard Model physics as an 𝒩=0\mathcal{N}=0 (non-supersymmetric) quantum field theory in a de Sitter background.
With our current understanding of string theory, there is no obvious direct attack for achieving this goal in one fell swoop.
A more tractable initial step is to obtain a four-dimensional 𝒩=1\mathcal{N}=1 theory that includes the Standard Model spectrum and interactions and has Yukawa couplings commensurate with observed mass hierarchies in a three generation model.
In order to perform this set of calculations within a heterotic compactification on a Calabi–Yau threefold, we require knowledge of the Ricci-flat metric in a given Kähler class as a function of the complex structure moduli.
This is necessary ab initio for normalizing the kinetic terms in the Kähler potential and ultimately for addressing more complicated issues such as moduli stabilization, incorporating α′\alpha^{\prime}-corrections, and breaking supersymmetry.
Perhaps the most straightforward laboratory for studying the problem invokes the “standard embedding,” wherein the holomorphic vector bundle is the tangent bundle on the Calabi–Yau manifold.
The important technical simplification that occurs within this setting is that the normalized Yukawa couplings can be computed directly using the Weil–Petersson metric on the complex structure moduli space.
In this work, we have performed the analysis for several Calabi–Yau geometries and calculated the normalized Yukawa couplings.

The Kodaira–Spencer approach [[31](#bib.bib31)] we have used applies to Calabi–Yau geometries with arbitrary h2,1​(X)h^{2,1}(X).
Moreover, we can generalize these techniques to Calabi–Yau threefolds realized as hypersurfaces in toric varieties, namely those geometries obtained from applying Batyrev’s procedure [[60](#bib.bib60)] to the Kreuzer–Skarke list [[61](#bib.bib61)] of four-dimensional reflexive polytopes.

In particular, we are performing analogous computations of Yukawa couplings in multi-parameter families and for various three generation models such as [[62](#bib.bib62), [63](#bib.bib63), [64](#bib.bib64), [65](#bib.bib65), [4](#bib.bib4)].
The results are compared to Yukawa coupling calculations reliant on machine learned harmonic representatives using the Ricci-flat Calabi–Yau metric.
This work is forthcoming [[66](#bib.bib66)].
We as well intend to adapt these methods to non-standard embeddings, for which the number of generations of particles in the low-energy spectrum need not be given by the Euler characteristic of the Calabi–Yau base space.

Accompanying this work and our earlier paper [[24](#bib.bib24)], we aim to release our code base, the software library cymyc [[35](#bib.bib35)], written in JAX, to compute Calabi–Yau Metrics, Yukawas, and Curvature.
On complete intersection Calabi–Yau manifolds, the spectral networks we employ supply, to date, the most efficient tool for numerically approximating the Ricci-flat metric using ∼105\sim 10^{5} or ∼106\sim 10^{6} points.77
7
The point selection follows the prescription of Shiffman–Zelditch [[47](#bib.bib47)].
Preliminary experiments indicate that computational performance may be improved with different point selection schemes.

The numerical calculation of the Weil–Petersson metric for arbitrary number of complex structure moduli will also be useful for studying the swampland distance conjecture [[67](#bib.bib67)]. Recently there has been some progress in this direction, by employing the Kodaira–Spencer method [[31](#bib.bib31)] for studying the moduli metric on Fermat quintic [[27](#bib.bib27)].

A synoptic view of this research places it in the broader context of a Big Data approach to string phenomenology and the vacuum selection problem.
We envision a systematic search through the estimated mole of Standard Model-like string constructions [[11](#bib.bib11)] arising from complete intersection Calabi–Yau geometries and the heptagoogol moles (10700+2310^{700+23}) of toric ones so as to find “the needle in the haystack,” which is us, living in our Universe.
To make progress, we must incorporate some combination of the algebro-geometric and analytic methods into the mechanized algorithm.
Each configuration is an entire (continuous) deformation space of models, so it seems important to obtain the physically normalized Yukawa couplings as functions of the complex structure deformation parameters and the Kähler class of the metric.
Ideally, we would input a Calabi–Yau geometry and ask whether there exists a point in its moduli space that recovers a quantum field theory with desired phenomenological properties and if so to deduce its low-energy effective action upon compactification.
We suspect that string Standard Models with hierarchies in the Yukawa couplings are extremely rare, as at a generic point in moduli space, most of the couplings will be of 𝒪⁡(1)\mathcal{O}(1).
Finding special points in moduli space where this expectation is dashed poses a central challenge for obtaining realistic models of particle physics.
Given the vastness of potential compactification geometries, it must be the case that if we find one model with the correct physics, there will be hugely many.

More ambitiously, the question of whether Calabi–Yau compactifications (a priori, with Minkowski spacetime) can be *uplifted* to accommodate our asymptotically de Sitter spacetime may well depend “Goldilocks” style, delicately on
*nearly-but-not-quite/almost-conifold-singular* Calabi–Yau manifolds [[68](#bib.bib68), [59](#bib.bib59)].
Our earlier machine learning investigations scanning for curvature clumping on singular K3 surfaces [[24](#bib.bib24)] (generalized to Calabi–Yau threefolds), should provide a solid stepping stone in searching for such models.

## Acknowledgements

We thank Nana Cabo Bizet and Fernando Quevedo as well as the organizers and participants at String Data 2023 at Caltech for comments on this work.
PB and GB are supported in part by the Department of Energy grant DE-SC0020220.
TH is grateful to the Department of Mathematics, University of Maryland, College Park MD,
and the Physics Department of the Faculty of Natural Sciences of the University of Novi Sad, Serbia, for the recurring hospitality and resources.
VJ is supported by the South African Research Chairs Initiative of the Department of Science and Innovation and the National Research Foundation. DM is supported
by FCT/Portugal through CAMGSD, IST-ID, projects UIDB/04459/2020 and UIDP/04459/2020.
CM is supported by a Fellowship with the Accelerate Science program at the Computer Laboratory, University
of Cambridge.
JT is supported by a studentship with the Accelerate Science Program.
The authors would like to thank the Isaac Newton Institute for Mathematical Sciences for support and hospitality during the program “Black holes: bridges between number theory and holographic quantum information” when work on this paper was undertaken; this work was supported by EPSRC grant number EP/R014604/1.

## Appendix A Proofs of lemmas

For completeness, we provide proofs of Lemma [1](#Thmlemma1 "Lemma 1. ‣ 2 Heterotic Yukawa couplings ‣ Physical Yukawa Couplings in Heterotic String Compactifications") and Lemma [2](#Thmlemma2 "Lemma 2. ‣ 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications").
We recall that we have used Lemma [1](#Thmlemma1 "Lemma 1. ‣ 2 Heterotic Yukawa couplings ‣ Physical Yukawa Couplings in Heterotic String Compactifications") to establish that H1​(X,TX)≃H2,1​(X)H^{1}(X,T\_{X})\simeq H^{2,1}(X) and Lemma [2](#Thmlemma2 "Lemma 2. ‣ 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications") to describe the Weil–Petersson metric.

Lemma [1](#Thmlemma1 "Lemma 1. ‣ 2 Heterotic Yukawa couplings ‣ Physical Yukawa Couplings in Heterotic String Compactifications")
Let XX be a Calabi–Yau manifold, then: H1​(X,TX)≃H∂¯n−1,1​(X)H^{1}(X,T\_{X})\simeq H^{n-1,1}\_{\overline{\partial}}(X) and the isomorphism is given by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | [α]⟼[Ω⁡(α)],\displaystyle[\alpha]\longmapsto[\Omega(\alpha)]\,, |  | ([2.8](#S2.E8 "In Lemma 1. ‣ 2 Heterotic Yukawa couplings ‣ Physical Yukawa Couplings in Heterotic String Compactifications")′) |

where Ω∈H∂¯n,0​(X)\Omega\in H^{n,0}\_{\overline{\partial}}(X) is non-zero.

###### Proof.

We shall first show the isomorphism is a consequence of Serre duality. For brevity we shall suppress the reference to the manifold XX. Then, by multiple applications of Serre duality, we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | H1​(TX)≃H0,1​(TX)≃Hn,n−1​(TX∗)∗≃Hn−1​(Ωn⊗TX∗)∗.\displaystyle H^{1}(T\_{X})\simeq H^{0,1}(T\_{X})\simeq H^{n,n-1}(T\_{X}^{\*})^{\*}\simeq H^{n-1}(\Omega^{n}\otimes T\_{X}^{\*})^{\*}\,. |  | (A.1) |

However, since Ωn=KX≃𝒪X\Omega^{n}=K\_{X}\simeq\mathcal{O}\_{X} and TX∗≃ΩT\_{X}^{\*}\simeq\Omega, we have:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Hn−1​(Ωn⊗TX∗)∗≃H1,n−1​(𝒪X)∗≃Hn−1,1​(𝒪X∗)≃Hn−1,1​(𝒪X),\displaystyle H^{n-1}(\Omega^{n}\otimes T\_{X}^{\*})^{\*}\simeq H^{1,n-1}(\mathcal{O}\_{X})^{\*}\simeq H^{n-1,1}(\mathcal{O}\_{X}^{\*})\simeq H^{n-1,1}(\mathcal{O}\_{X})\,, |  | (A.2) |

thus proving the claim H1​(TX)≃H∂¯n−1,1​(X)H^{1}(T\_{X})\simeq H^{n-1,1}\_{\overline{\partial}}(X). We shall now show that the isomorphism is given by the interior product. It is trivial to see that the interior product gives an isomorphism on the sections: Γ⁡(X,Ωn−1,1)≃Γ⁡(X,Ω0,1​(TX))\Gamma(X,\Omega^{n-1,1})\simeq\Gamma(X,\Omega^{0,1}(T\_{X})) [[41](#bib.bib41)], thus what remains to show is that the map preserves kernels and images of ∂¯{\overline{\partial}}. Let p∈Xp\in X and pick local coordinates (z1,…,zn)(z^{1},\dots,z^{n}) centered at point pp. Suppose that [α]=0[\alpha]=0 in H1​(TX)H^{1}(T\_{X}), then, α=∂¯​ϕ\alpha=\overline{\partial}\phi for some non-holomorphic vector field ϕ∈Γ⁡(X,TX)\phi\in\Gamma(X,T\_{X}). Let Ω=f⁡(z)​d​z1∧⋯∧d​zn\Omega=f(z){\mathrm{d}}z^{1}\wedge\cdots\wedge{\mathrm{d}}z^{n} in the local coordinates defined above, where f⁡(z)f(z) is holomorphic. Then, the interior product is given explicitly by:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ω⁡(∂¯​ϕ)=∑μ=1n(−1)μ−1​f​αν¯μ​d​z¯ν∧μ^=∑μ=1n(−1)μ−1​f​∂ϕ∂z¯ν​d​z¯ν∧μ^,\displaystyle\Omega(\overline{\partial}\phi)=\sum\_{\mu=1}^{n}(-1)^{\mu-1}f\,\alpha^{\mu}\_{\overline{\nu}}\,{\mathrm{d}}\overline{z}^{\nu}\wedge\widehat{\mu}=\sum\_{\mu=1}^{n}(-1)^{\mu-1}f\,\frac{\partial\phi}{\partial\overline{z}^{\nu}}{\mathrm{d}}\overline{z}^{\nu}\wedge\widehat{\mu}\,, |  | (A.3) |

where we abbreviated
μ^​=def​d​z1∧⋯∧d​zμ^∧⋯∧d​zn\widehat{\mu}\overset{\scriptscriptstyle\mathrm{def}}{=}dz^{1}\wedge\cdots\wedge\widehat{dz^{\mu}}\wedge\cdots\wedge dz^{n}.
That above is exact follows immediately from the fact that ff is holomorphic, thus ∂¯​f=0\overline{\partial}f=0. Similarly, let α\alpha be ∂¯\overline{\partial}-closed, then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∂¯​Ω​(α)=∑μ=1n(−1)μ−1​f​∂αν¯μ∂z¯σ​d​z¯σ∧d​z¯ν∧μ^=0.\displaystyle\overline{\partial}\Omega(\alpha)=\sum\_{\mu=1}^{n}(-1)^{\mu-1}f\,\frac{\partial\alpha\_{\overline{\nu}}^{\mu}}{\partial\overline{z}^{\sigma}}{\mathrm{d}}\overline{z}^{\sigma}\wedge{\mathrm{d}}\overline{z}^{\nu}\wedge\widehat{\mu}=0\,. |  | (A.4) |

∎

Lemma [2](#Thmlemma2 "Lemma 2. ‣ 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications") Let Ω∈H∂¯n,0​(Xt)\Omega\in H\_{\overline{\partial}}^{n,0}(X\_{t}) where n=dimXtn=\dim{X\_{t}}, be non-zero, then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ⟨a,b⟩WP=−∫XtΩ⁡(ℋ​ρ​(a))∧Ω⁡(ℋ​ρ​(b))¯∫XtΩ∧Ω¯∫Xt𝗏𝗈𝗅gt.\displaystyle\langle a,b\rangle\_{\mathrm{WP}}=-\frac{\displaystyle\int\_{X\_{t}}\Omega(\mathcal{H}\rho(a))\wedge\overline{\Omega(\mathcal{H}\rho(b))}}{\displaystyle\int\_{X\_{t}}\Omega\wedge\overline{\Omega}}\int\_{X\_{t}}\mathsf{vol}\_{g\_{t}}\,. |  | ([3.3](#S3.E3 "In Lemma 2. ‣ 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications")′) |

###### Proof.

The result follows from direct calculation in local coordinates. Let p∈Xtp\in X\_{t} and consider local coordinates (z1,…,zn)(z^{1},\dots,z^{n}) centered at pp. Let α=ℋ​ρ​(a)\alpha=\mathcal{H}\rho(a) and β=ℋ​ρ​(b)\beta=\mathcal{H}\rho(b), then:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ω⁡(α)=∑μ,ν=1n(−1)μ−1​αν¯μ​f​d​z¯ν∧μ^,\displaystyle\Omega(\alpha)=\sum\_{\mu,\nu=1}^{n}(-1)^{\mu-1}\alpha\_{\overline{\nu}}^{\mu}\,f\,{\mathrm{d}}\overline{z}^{\nu}\wedge\widehat{\mu}\,, |  | (A.5) |

where α=αμν¯dz¯ν⊗∂μ\alpha=\alpha^{\mu}\_{\overline{\nu}}\,{\mathrm{d}}\overline{z}^{\nu}\otimes\partial\_{\mu} and Ω=f⁡(z)​d​z1∧⋯∧d​zn\Omega=f(z)\,dz^{1}\wedge\cdots\wedge dz^{n}. Combining the results for both deformations yields the following:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ω⁡(α)∧Ω⁡(β)¯=∑μ,μ′,ν,ν′=1n(−1)μ+μ′​|f|2​αν¯μ​βν′¯μ′¯​d​z¯ν∧μ^∧d​zν′∧μ′^¯.\displaystyle\Omega(\alpha)\wedge\overline{\Omega(\beta)}=\sum\_{\mu,\mu^{\prime},\nu,\nu^{\prime}=1}^{n}(-1)^{\mu+\mu^{\prime}}|f|^{2}\,\alpha\_{\overline{\nu}}^{\mu}\,\overline{\beta\_{\overline{\nu^{\prime}}}^{\mu^{\prime}}}\,{\mathrm{d}}\overline{z}^{\nu}\wedge\widehat{\mu}\wedge{\mathrm{d}}z^{\nu^{\prime}}\wedge\overline{\widehat{\mu^{\prime}}}\,. |  | (A.6) |

It is easy to see that the only non-vanishing terms have indices μ=ν′\mu=\nu^{\prime} and μ′=ν\mu^{\prime}=\nu, which leads to the following expression:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ω⁡(α)∧Ω⁡(β)¯=(∑μ,ν=1n(−1)μ+ν​αν¯μ​βμ¯ν¯​(−1)μ+ν−1)​Ω∧Ω¯=−αν¯μ​βμ¯ν¯​Ω∧Ω¯.\displaystyle\Omega(\alpha)\wedge\overline{\Omega(\beta)}=\left(\sum\_{\mu,\nu=1}^{n}(-1)^{\mu+\nu}\alpha\_{\overline{\nu}}^{\mu}\,\overline{\beta\_{\overline{\mu}}^{\nu}}\,(-1)^{\mu+\nu-1}\right)\Omega\wedge\overline{\Omega}=-\alpha\_{\overline{\nu}}^{\mu}\,\overline{\beta\_{\overline{\mu}}^{\nu}}\,\Omega\wedge\overline{\Omega}\,. |  | (A.7) |

Finally, since α\alpha and β\beta are both chosen to be harmonic, using the results of [[44](#bib.bib44)]
(or Lemma [3](#Thmlemma3 "Lemma 3. ‣ Appendix A Proofs of lemmas ‣ Physical Yukawa Couplings in Heterotic String Compactifications")), it is immediate that αν¯μ​βμν¯=gμ​ν¯​gσ​δ¯​αδ¯μ​βσ¯ν¯\alpha\_{\overline{\nu}}^{\mu}\,\overline{\beta\_{\mu}^{\nu}}=g\_{\mu\overline{\nu}}\,g^{\sigma\overline{\delta}}\,\alpha^{\mu}\_{\overline{\delta}}\,\overline{\beta\_{\overline{\sigma}}^{\nu}} where (see Definition [1](#Thmdefinition1 "Definition 1. ‣ 3.1 Computing normalizations ‣ 3 Physical Yukawa couplings via the Kodaira–Spencer map ‣ Physical Yukawa Couplings in Heterotic String Compactifications"))
gt=gμ​ν¯​d​zμ∧d​z¯νg\_{t}=g\_{\mu\overline{\nu}}\,{\mathrm{d}}z^{\mu}\wedge{\mathrm{d}}\overline{z}^{\nu}. Furthermore, noting that the flat metric on compact XtX\_{t} solves the Monge–Ampère equation: 𝗏𝗈𝗅gt=κ​Ω∧Ω¯\mathsf{vol}\_{g\_{t}}=\kappa\,\Omega\wedge\overline{\Omega} for some constant κ∈ℂ\kappa\in\mathbb{C}, we obtain:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ∫XtΩ(α)∧Ω⁡(β)¯=−1κ∫Xtα∧⋆gt¯β.\displaystyle\int\_{X\_{t}}\Omega(\alpha)\wedge\overline{\Omega(\beta)}=-\frac{1}{\kappa}\int\_{X\_{t}}\alpha\wedge\overline{\star\_{g\_{t}}}\beta\,. |  | (A.8) |

After identifying κ\kappa with ∫Xt𝗏𝗈𝗅gt/∫XtΩ∧Ω¯\int\_{X\_{t}}\mathsf{vol}\_{g\_{t}}\big/\int\_{X\_{t}}\Omega\wedge\overline{\Omega}, the result follows.
∎

We also note that there exists a method of computation of the harmonic representative which avoids the use of the computationally expensive derivatives of the Ricci-flat metric. The result follows from the following lemma.

###### Lemma 3.

Let XX be Calabi–Yau with Kähler class [ω]∈H1,1​(X)∩H2​(X)[\omega]\in H^{1,1}(X)\cap H^{2}(X) and α∈Ω0,1​(TX)\alpha\in\Omega^{0,1}(T\_{X}) is closed, then the following are equivalent:

α\alpha is harmonic with respect to Ricci-flat metric in the Kähler class [ω][\omega].

α\alpha is polarization preserving with respect to [ω][\omega] and ∂Ω⁡(α)=0\partial\Omega(\alpha)=0.

In statement 2, polarization preserving is in the sense of [[41](#bib.bib41), [44](#bib.bib44)].

###### Proof.

That 1⇒21\Rightarrow 2 is proved in [[44](#bib.bib44)] and depends on Ricci-flatness of the metric. Conversely, to show that 2⇒12\Rightarrow 1, pick an open set U⊂XU\subset X and local coordinates (z1,…,zn)(z^{1},\dots,z^{n}) on UU such that Ω=f⁡(z)​d​z1∧⋯∧d​zn\Omega=f(z){\mathrm{d}}z^{1}\wedge\dots\wedge{\mathrm{d}}z^{n}. Locally, we may expand ∂Ω⁡(α)\partial\Omega(\alpha) as:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂Ω⁡(α)\displaystyle\partial\Omega(\alpha) | =∂(∑μ=1n(−1)μ−1​f​(z)​αν¯μ​d​z¯ν∧μ^),\displaystyle=\partial\left(\sum\_{\mu=1}^{n}(-1)^{\mu-1}f(z)\,\alpha\_{\overline{\nu}}^{\mu}\,{\mathrm{d}}\overline{z}^{\nu}\wedge\widehat{\mu}\right)\,, |  | (A.9) |
|  |  | =∑μ=1n∂∂zμ​(f⁡(z)​αν¯μ)​d​z¯ν∧d​z1∧⋯∧d​zn=0,\displaystyle=\sum\_{\mu=1}^{n}\frac{\partial}{\partial z^{\mu}}\big(f(z)\,\alpha^{\mu}\_{\overline{\nu}}\big){\mathrm{d}}\overline{z}^{\nu}\wedge{\mathrm{d}}z^{1}\wedge\dots\wedge{\mathrm{d}}z^{n}=0\,, |  |

where μ^:=d​z1∧⋯∧d​zμ^∧⋯∧d​zn\widehat{\mu}:={\mathrm{d}}z^{1}\wedge\dots\wedge\widehat{{\mathrm{d}}z^{\mu}}\wedge\dots\wedge{\mathrm{d}}z^{n}. Similarly, the polarization preserving condition, at the level of forms, can be written as:

|  |  |  |  |
| --- | --- | --- | --- |
|  | gμ​ρ¯​gσ​ν¯​αν¯μ=αρ¯σ.\displaystyle g\_{\mu\overline{\rho}}\,g^{\sigma\overline{\nu}}\,\alpha\_{\overline{\nu}}^{\mu}=\alpha\_{\overline{\rho}}^{\sigma}\,. |  | (A.10) |

Finally, using the local Monge–Ampère equation, det⁡g=κ​|f⁡(z)|2\det g=\kappa|f(z)|^{2}, we obtain:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ∂∂zμ​(gσ​ν¯​gμ​ρ¯​αρ¯σ​det⁡g)​d​z¯ν\displaystyle\frac{\partial}{\partial z^{\mu}}\big(g\_{\sigma\overline{\nu}}\,g^{\mu\overline{\rho}}\,\alpha^{\sigma}\_{\overline{\rho}}\,\det g\big){\mathrm{d}}\overline{z}^{\nu} | =κ​∂∂zμ​(|f⁡(z)|2​gσ​ν¯​gμ​ρ¯​αρ¯σ)​d​z¯ν,\displaystyle=\kappa\frac{\partial}{\partial z^{\mu}}\big(|f(z)|^{2}g\_{\sigma\overline{\nu}}\,g^{\mu\overline{\rho}}\,\alpha^{\sigma}\_{\overline{\rho}}\big){\mathrm{d}}\overline{z}^{\nu}\,, |  | (A.11) |
|  |  | =κ​f⁡(z)¯​∂∂zμ​(f⁡(z)​αν¯μ)​d​z¯ν=0.\displaystyle=\kappa\overline{f(z)}\frac{\partial}{\partial z^{\mu}}\big(f(z)\,\alpha^{\mu}\_{\overline{\nu}}\big){\mathrm{d}}\overline{z}^{\nu}=0\,. |  |

Equivalently, extending the results globally to XX, we have: ∂¯†​α=0\overline{\partial}^{\dagger}\alpha=0 and since ∂¯​α=0\overline{\partial}\alpha=0 by definition, we see that α\alpha is indeed harmonic.
∎

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