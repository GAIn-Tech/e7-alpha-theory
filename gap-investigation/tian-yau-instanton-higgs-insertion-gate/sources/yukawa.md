##### Report GitHub Issue

Content selection saved. Describe the issue below:

![](/static/base/1.0.1/images/icons/smileybones-small.svg)
![arXiv logo](/static/base/1.0.1/images/arxiv-logo-primary-light.svg)

# Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications

###### Abstract

We study the modular symmetry in heterotic string theory on Calabi-Yau threefolds.
In particular, we examine whether moduli-dependent holomorphic Yukawa couplings are described by modular forms
in the context of heterotic string theory with standard embedding.
We find that S​L​(2,ℤ)SL(2,\mathbb{Z}) modular symmetry emerges in asymptotic regions of the Calabi-Yau moduli
space.
The instanton-corrected holomorphic Yukawa couplings are then given by modular forms under S​L​(2,ℤ)SL(2,\mathbb{Z}) or
its congruence subgroups such as Γ0​(3)\Gamma\_{0}(3) and Γ0​(4)\Gamma\_{0}(4).
In addition to the modular symmetry, it turns out that another coupling selection rule controls the structure of holomorphic Yukawa couplings.
Furthermore, the coexistence of both the positive and negative modular weights for matter fields
leads to a hierarchical structure of matter field Kähler metric.
Thus, these holomorphic modular forms and the matter field Kähler metric play an important role in realizing a hierarchical
structure of physical Yukawa couplings.

## 1 Introduction

The modular symmetry plays a crucial role in string theory.
It was known that the one-loop closed bosonic string amplitude defined over the quotient of
the upper half-plane of S​L​(2,ℤ)SL(2,\mathbb{Z}) is free of ultra-violet divergence.
This discussion can be extended to higher-loop orders.11
1
For more details, see, e.g., Ref. [[1](#bib.bib1)]. For genus hh Riemann surfaces, the S​L​(2,ℤ)SL(2,\mathbb{Z})
modular group is replaced by the S​p​(2​h,ℤ)Sp(2h,\mathbb{Z}) modular group.
The modular symmetry in the string worldsheet can also be seen in the target space of string theory.

In toroidal compactifications, the modular symmetry can be regarded as a geometric symmetry of torus,
which puts strong constraints on the four-dimensional (4D) low-energy effective field theory.
Indeed, the modulus τ\tau parametrizing the S​L​(2,ℤ)SL(2,\mathbb{Z}) modular symmetry appears in couplings of matter fields,
as known in heterotic orbifold models [[2](#bib.bib2), [3](#bib.bib3), [4](#bib.bib4), [5](#bib.bib5)] and magnetized D-brane models [[6](#bib.bib6), [7](#bib.bib7), [8](#bib.bib8), [9](#bib.bib9), [10](#bib.bib10), [11](#bib.bib11), [12](#bib.bib12), [13](#bib.bib13)].
In these models, chiral zero-modes have certain representations of the congruence subgroup of S​L​(2,ℤ)SL(2,\mathbb{Z}) with
a modular weight, and these holomorphic Yukawa couplings are described by a certain modular form under the congruence
subgroup. It is remarkable that the inhomogeneous modular group Γ¯=P​S​L​(2,ℤ)\bar{\Gamma}=PSL(2,\mathbb{Z}) has several
finite subgroups such as S3,A4,S4,A5S\_{3},A\_{4},S\_{4},A\_{5} [[14](#bib.bib14)].
These modular groups will be important to understand the flavor structure of
quarks and leptons [[15](#bib.bib15), [16](#bib.bib16), [17](#bib.bib17), [18](#bib.bib18), [19](#bib.bib19)].

In Calabi-Yau (CY) compactifications as an extension of toroidal backgrounds22
2
See, Ref. [[20](#bib.bib20)], for a construction of
modular symmetric models from higher-dimensional theory on general grounds.,
the modular symmetry is enhanced to S​p​(2​h+2,ℤ)Sp(2h+2,\mathbb{Z}) with hh being the number of moduli fields [[21](#bib.bib21), [22](#bib.bib22)].
Such a symplectic modular symmetry will constrain the 4D low-energy effective action [[23](#bib.bib23), [24](#bib.bib24)].
It was pointed out in Ref. [[23](#bib.bib23)] that the flavor symmetry of matter fields can be embedded into the
symplectic modular symmetry in the context of heterotic string theory with standard embedding.
However, it is still unclear whether holomorphic Yukawa couplings are described by modular forms.
The derivation of holomorphic Yukawa couplings is also important to understand the hierarchical structure of
quark and lepton masses.33
3
See for the derivation of holomorphic Yukawa couplings
for heterotic line bundle models [[25](#bib.bib25)].
The purpose of this paper is to derive explicit forms of holomorphic Yukawa couplings in heterotic
string theory on concrete CY threefolds.
We find that the S​L​(2,ℤ)SL(2,\mathbb{Z}) modular symmetry emerges in asymptotic regions of the complex structure and
Kähler moduli spaces. The instanton-corrected holomorphic Yukawa couplings are then described by modular forms
of S​L​(2,ℤ)SL(2,\mathbb{Z}) or its congruence subgroups such as Γ0​(3)\Gamma\_{0}(3) and Γ0​(4)\Gamma\_{0}(4).
Furthermore, it turns out that these holomorphic modular forms as well as Kähler metric of matter fields can
lead to the hierarchical structure of physical Yukawa couplings.

This paper is organized as follows.
In Sec. [2](#S2 "2 Modular invariant effective action ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications"), we review the 4D low-energy effective field theory of heterotic string theory with standard
embedding, focusing on the role of modular symmetry.
In Sec. [3](#S3 "3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications"), we study instanton-corrected holomorphic Yukawa couplings on several CY threefolds.
The structure of instanton numbers determines the modular form of holomorphic Yukawa couplings such as modular forms of S​L​(2,ℤ)SL(2,\mathbb{Z}) in Sec. [3.1](#S3.SS1 "3.1 𝑆⁢𝐿⁢(2,ℤ) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications"),
Γ0​(3)\Gamma\_{0}(3) in Sec. [3.2](#S3.SS2 "3.2 Γ_0⁢(3) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications") and Γ0​(4)\Gamma\_{0}(4) in Sec. [3.3](#S3.SS3 "3.3 Γ_0⁢(4) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications").
As an application of modular forms, we investigate whether one can realize the hierarchical structure of physical Yukawa couplings
in Sec. [4](#S4 "4 Hierarchical structure of physical Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications").
Sec. [5](#S5 "5 Conclusions and discussions ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications") is devoted to conclusions.
In Appendix [A](#A1 "Appendix A Γ_0⁢(𝑁) modular forms ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications"), we summarize several holomorphic modular forms under the Γ0​(N)\Gamma\_{0}(N) modular group.

## 2 Modular invariant effective action

In this section, we briefly review the 4D low-energy effective field theory action derived from E8×E8′E\_{8}\times E\_{8}^{\prime} heterotic string theory on smooth Calabi-Yau threefolds with standard embedding.44
4
The discussion is the same for S​O​(32)SO(32) heterotic string theory.
In particular, we emphasize the role of symplectic modular symmetry in the effective action of matter fields which are in one-to-one correspondence with the moduli fields.

##### Kähler potential

It is known that the low-energy group is described by E6×E8′E\_{6}\times E\_{8}^{\prime} due to the identification of background S​U​(3)⊂E8SU(3)\subset E\_{8}
gauge field with the spin connection of CY threefolds.
There are h1,1h^{1,1} number of chiral superfields AaA^{a} in the 𝟐𝟕{\bf 27} representation of E6E\_{6} and h2,1h^{2,1} number of chiral superfields AiA^{i} in the \macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​𝟐𝟕\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{{\bf 27}} representation of E6E\_{6}.
Here, h1,1h^{1,1} and h2,1h^{2,1} denote the hodge numbers of CY threefolds.
Thanks to the one-to-one correspondence between moduli and chiral matter fields, the matter field Kähler metrics are written by the following form [[26](#bib.bib26)]55
5
Note that the overall factor e±13​(Kcs−Kks)e^{\pm\frac{1}{3}(K\_{\rm cs}-K\_{\rm ks})}
is different in toroidal orbifolds due to the enlarged symmetry [[26](#bib.bib26)].:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ka​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​b(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{a\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{b}} | =e13​(Kcs−Kks)​(Kks)a​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​b,\displaystyle=e^{\frac{1}{3}(K\_{\rm cs}-K\_{\rm ks})}(K\_{\rm ks})\_{a\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{b}}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ki​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​j(\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​𝟐𝟕)\displaystyle K^{(\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{{\bf 27}})}\_{i\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{j}} | =e−13​(Kcs−Kks)​(Kcs)i​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​j,\displaystyle=e^{-\frac{1}{3}(K\_{\rm cs}-K\_{\rm ks})}(K\_{\rm cs})\_{i\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{j}}, |  | (2.1) |

where (Kks)a​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​b=∂a∂b¯Kks(K\_{\rm ks})\_{a\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{b}}=\partial\_{a}\partial\_{\bar{b}}K\_{\rm ks} and (Kcs)i​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​j=∂i∂j¯Kcs(K\_{\rm cs})\_{i\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{j}}=\partial\_{i}\partial\_{\bar{j}}K\_{\rm cs} are the metric of the Kähler moduli and the complex structure moduli, respectively.
To see an explicit form of the matter field Kähler metric, let us focus on the Kähler moduli sector for concreteness.
The Kähler potential of the Kähler moduli is well controlled in the large volume regime 𝒱≫ls6{\cal V}\gg l\_{s}^{6}

|  |  |  |  |
| --- | --- | --- | --- |
|  | Kks=−ln⁡(𝒱)=−ln[iκa​b​c6(ta−\macc@depthΔ\macc@set@skewchar\macc@nested@a111ta)(tb−\macc@depthΔ\macc@set@skewchar\macc@nested@a111tb)(tc−\macc@depthΔ\macc@set@skewchar\macc@nested@a111tc)].\displaystyle K\_{\rm ks}=-\ln{\cal V}=-\ln\biggl[i\frac{\kappa\_{abc}}{6}(t^{a}-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}^{a})(t^{b}-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}^{b})(t^{c}-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}^{c})\biggl]. |  | (2.2) |

Here, κa​b​c\kappa\_{abc} denotes a triple intersection number of CY threefolds.
It results in the Kähler metric of 𝟐𝟕{\bf 27} matters:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ka​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​b(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{a\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{b}} | =e13​Kcs​𝒱1/3​(Kks)a​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​b\displaystyle=e^{\frac{1}{3}K\_{\rm cs}}{\cal V}^{1/3}(K\_{\rm ks})\_{a\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{b}} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =eKcs3[1𝒱5/3(κa​d​e2(td−\macc@depthΔ\macc@set@skewchar\macc@nested@a111td)(te−\macc@depthΔ\macc@set@skewchar\macc@nested@a111te))(κb​f​g2(tf−\macc@depthΔ\macc@set@skewchar\macc@nested@a111tf)(tg−\macc@depthΔ\macc@set@skewchar\macc@nested@a111tg))+i𝒱2/3κa​b​h(th−\macc@depthΔ\macc@set@skewchar\macc@nested@a111th)],\displaystyle=e^{\frac{K\_{\rm cs}}{3}}\biggl[\frac{1}{{\cal V}^{5/3}}\left(\frac{\kappa\_{ade}}{2}(t^{d}-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}^{d})(t^{e}-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}^{e})\right)\left(\frac{\kappa\_{bfg}}{2}(t^{f}-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}^{f})(t^{g}-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}^{g})\right)+\frac{i}{{\cal V}^{2/3}}\kappa\_{abh}(t^{h}-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}^{h})\biggl], |  | (2.3) |

where we use

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Kks)a​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​b\displaystyle(K\_{\rm ks})\_{a\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{b}} | =1𝒱​(∂a𝒱​∂b¯𝒱𝒱−∂a∂b¯𝒱)\displaystyle=\frac{1}{{\cal V}}\left(\frac{\partial\_{a}{\cal V}\partial\_{\bar{b}}{\cal V}}{{\cal V}}-\partial\_{a}\partial\_{\bar{b}}{\cal V}\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =1𝒱2​(κa​d​e2​(td−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​td)​(te−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​te))​(κb​f​g2​(tf−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​tf)​(tg−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​tg))+i𝒱​κa​b​h​(th−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​th).\displaystyle=\frac{1}{{\cal V}^{2}}\left(\frac{\kappa\_{ade}}{2}(t^{d}-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}^{d})(t^{e}-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}^{e})\right)\left(\frac{\kappa\_{bfg}}{2}(t^{f}-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}^{f})(t^{g}-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}^{g})\right)+\frac{i}{{\cal V}}\kappa\_{abh}(t^{h}-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}^{h}). |  | (2.4) |

The Kähler metric of \macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​𝟐𝟕\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{{\bf 27}} matters is written by the same expression,
where the large volume regime corresponds to the large complex structure moduli.
If we restrict Kähler moduli to the universal value, that is, t:=tit:=t^{i} for all ii, the matter field Kähler metric is proportional to

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ka​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​b(𝟐𝟕)∝e13​Kcs​1i⁡(t¯−t).\displaystyle K^{({\bf 27})}\_{a\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{b}}\propto e^{\frac{1}{3}K\_{\rm cs}}\frac{1}{i(\bar{t}-t)}. |  | (2.5) |

In the following, we focus on the effective action of 𝟐𝟕{\bf 27} matter fields, but a similar analysis can be done for the \macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​𝟐𝟕\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{{\bf 27}} matters.

##### Yukawa couplings

The 3-point coupling of moduli fields is given by the third derivative of the prepotential with respect to corresponding moduli fields.
In the large volume regime, this 3-point coupling is nothing but the triple intersection numbers κa​b​c\kappa\_{abc} classically.
However, it will be corrected by instanton contributions.
It is known that instanton-corrected Yukawa couplings ere obtained in the following form [[27](#bib.bib27), [28](#bib.bib28)]

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ya​b​c\displaystyle y\_{abc} | =κa​b​c+∑d1,d2,…,dm=0∞(da​db​dc)​nd1,d2,…,dm1−Πl=1m​qldl​Πl=1m​qldl,\displaystyle=\kappa\_{abc}+\sum\_{d\_{1},d\_{2},...,d\_{m}=0}^{\infty}\frac{(d\_{a}d\_{b}d\_{c})n\_{d\_{1},d\_{2},...,d\_{m}}}{1-\Pi\_{l=1}^{m}q\_{l}^{d\_{l}}}\Pi\_{l=1}^{m}q\_{l}^{d\_{l}}, |  | (2.6) |

with ql=e2​π​i​tlq\_{l}=e^{2\pi it\_{l}}, where the instanton numbers nd1,d2,…,dmn\_{d\_{1},d\_{2},...,d\_{m}} are determined once the background CY geometry is fixed.
The 𝟐𝟕{\bf 27} matter superpotential is then written by

|  |  |  |  |
| --- | --- | --- | --- |
|  | W=ya​b​c​Aa​Ab​Ac.\displaystyle W=y\_{abc}A^{a}A^{b}A^{c}. |  | (2.7) |

##### Modular symmetry

In the large volume regime, the effective action is controlled by a certain subgroup of symplectic modular group S​p​(2​h1,1+2,ℤ)Sp(2h^{1,1}+2,\mathbb{Z}), which depends on the structure of the intersection numbers κa​b​c\kappa\_{abc}. The full modular group can be described in projective coordinates YAY^{A} with A=1,2,…,h1,1+1A=1,2,...,h^{1,1}+1. Here, the Kähler moduli correspond to

|  |  |  |  |
| --- | --- | --- | --- |
|  | ta=YaY0,\displaystyle t^{a}=\frac{Y^{a}}{Y^{0}}, |  | (2.8) |

with a=1,2,…,h1,1a=1,2,...,h^{1,1}.
As discussed in Ref. [[24](#bib.bib24)], the symplectic modular transformations of matter fields and their Kähler metric

|  |  |  |  |
| --- | --- | --- | --- |
|  | Aa\displaystyle A^{a} | →A~a=(Y~0)−1/3∂t~a∂tbAb,\displaystyle\rightarrow\tilde{A}^{a}=(\tilde{Y}^{0})^{-1/3}\frac{\partial\tilde{t}^{a}}{\partial t^{b}}A^{b}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ka​b¯(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{a\bar{b}} | →K~a​b¯(𝟐𝟕)=|Y~0|2/3​∂tc∂t~a​∂t¯d¯∂t¯~b¯​Kc​d¯(𝟐𝟕),\displaystyle\rightarrow\tilde{K}^{({\bf 27})}\_{a\bar{b}}=|\tilde{Y}^{0}|^{2/3}\frac{\partial t^{c}}{\partial\tilde{t}^{a}}\frac{\partial\bar{t}^{\bar{d}}}{\partial\tilde{\bar{t}}^{\bar{b}}}K^{({\bf 27})}\_{c\bar{d}}, |  | (2.9) |

are consistent with the modular symmetry of the Kähler moduli: ta→t~at^{a}\rightarrow\tilde{t}^{a}.
Furthermore, Yukawa couplings are expected to be transformed as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ya​b​c→y~a​b​c=Y~0​∂td∂t~a​∂te∂t~b​∂tf∂t~c​yd​e​f.\displaystyle y\_{abc}\rightarrow\tilde{y}\_{abc}=\tilde{Y}^{0}\frac{\partial t^{d}}{\partial\tilde{t}^{a}}\frac{\partial t^{e}}{\partial\tilde{t}^{b}}\frac{\partial t^{f}}{\partial\tilde{t}^{c}}y\_{def}. |  | (2.10) |

Thus, the symplectic modular symmetry will determine the flavor symmetry of matter fields.

Note that instanton effects may further break the remained modular group into a smaller one.
The tree-level Yukawa couplings κa​b​c\kappa\_{abc} are moduli-independent constants and correspond to trivial modular forms of weight zero.
On the other hand, moduli-dependent holomorphic Yukawa coupling terms induced by instanton effects can be non-trivial modular forms.
That is interesting from both theoretical and phenomenological viewpoints.
In the following section, we study explicitly several CY threefolds in order to
reveal unbroken modular symmetries and concrete forms of
non-trivial modular forms.

## 3 Holomorphic Yukawa couplings

In this section, we study a modular invariance of the effective action for matter fields.
In Sec. [3.1](#S3.SS1 "3.1 𝑆⁢𝐿⁢(2,ℤ) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications"), we first derive a S​L​(2,ℤ)SL(2,\mathbb{Z}) modular form for holomorphic
Yukawa couplings of matter fields, which are realized in specific CY threefolds with two moduli in Sec. [3.1.1](#S3.SS1.SSS1 "3.1.1 Two moduli ‣ 3.1 𝑆⁢𝐿⁢(2,ℤ) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications") and
three moduli in Sec. [3.1.2](#S3.SS1.SSS2 "3.1.2 Three moduli ‣ 3.1 𝑆⁢𝐿⁢(2,ℤ) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications").
In both examples, holomorphic Yukawa couplings are described by an Eisenstein series with weight 4 which transforms as a singlet representation under S​L​(2,ℤ)SL(2,\mathbb{Z}).
In Sec. [3.2](#S3.SS2 "3.2 Γ_0⁢(3) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications"), we next show that the holomorphic Yukawa couplings are described by a modular form under Γ0​(3)\Gamma\_{0}(3) as a subgroup of S​L​(2,ℤ)SL(2,\mathbb{Z}), which are realized in specific CY threefolds with two moduli in Sec. [3.2.1](#S3.SS2.SSS1 "3.2.1 Two moduli ‣ 3.2 Γ_0⁢(3) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications") and three moduli in Sec. [3.2.2](#S3.SS2.SSS2 "3.2.2 Three moduli ‣ 3.2 Γ_0⁢(3) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications").
Finally, we present the holomorphic Yukawa couplings controlled by Γ0​(4)\Gamma\_{0}(4) modular group in Sec. [3.3](#S3.SS3 "3.3 Γ_0⁢(4) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications").

### 3.1 S​L​(2,ℤ)SL(2,\mathbb{Z}) modular forms

In this section, we focus on specific CY threefolds with two moduli in Sec. [3.1.1](#S3.SS1.SSS1 "3.1.1 Two moduli ‣ 3.1 𝑆⁢𝐿⁢(2,ℤ) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications") and three moduli
in Sec. [3.1.2](#S3.SS1.SSS2 "3.1.2 Three moduli ‣ 3.1 𝑆⁢𝐿⁢(2,ℤ) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications"), leading to a S​L​(2,ℤ)SL(2,\mathbb{Z}) modular form for holomorphic Yukawa couplings.

#### 3.1.1 Two moduli

We first study a CY threefold defined by the degree 18 hypersurface in weighted projective space ℂ​ℙ1,1,1,6,9​[18]\mathbb{CP}^{1,1,1,6,9}[18],
where the number of Kähler moduli is h1,1=2h^{1,1}=2.
We revisit the work of Ref. [[29](#bib.bib29)] from the viewpoint of effective action of matter fields.
By solving the corresponding Picard-Fuchs equation, the prepotential for two Kähler moduli was known to be

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℱ\displaystyle{\cal F} | =−16​(9​t13+9​t12​t2+3​t1​t22),\displaystyle=-\frac{1}{6}\left(9t\_{1}^{3}+9t\_{1}^{2}t\_{2}+3t\_{1}t\_{2}^{2}\right), |  | (3.1) |

where we omit the higher-order corrections including instanton effects, and the triple intersection numbers are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ111=9,κ112=3,κ122=1,\displaystyle\kappa\_{111}=9,\quad\kappa\_{112}=3,\quad\kappa\_{122}=1, |  | (3.2) |

and otherwise 0.
Instanton-corrected holomorphic Yukawa couplings are of the form:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ya​b​c\displaystyle y\_{abc} | =κa​b​c+∑d1,d2=0∞ca​b​c​(d1,d2)​nd1,d2​q1d1​q2d21−q1d1​q2d2,\displaystyle=\kappa\_{abc}+\sum\_{d\_{1},d\_{2}=0}^{\infty}\frac{c\_{abc}(d\_{1},d\_{2})n\_{d\_{1},d\_{2}}q\_{1}^{d\_{1}}q\_{2}^{d\_{2}}}{1-q\_{1}^{d\_{1}}q\_{2}^{d\_{2}}}, |  | (3.3) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | c111=(d1)3,c112=(d1)2​d2,c122=d1​(d2)2,c112=(d2)3.\displaystyle c\_{111}=(d\_{1})^{3},\quad c\_{112}=(d\_{1})^{2}d\_{2},\quad c\_{122}=d\_{1}(d\_{2})^{2},\quad c\_{112}=(d\_{2})^{3}. |  | (3.4) |

Here, the instanton numbers nd1,d2n\_{d\_{1},d\_{2}} are given in Table [1](#S3.T1 "Table 1 ‣ 3.1.1 Two moduli ‣ 3.1 𝑆⁢𝐿⁢(2,ℤ) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications").

| d1d\_{1} ∖\setminus d2d\_{2} | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| 0 |  | 3 | -6 | 27 |
| 1 | 540 | -1080 | 2700 | -17280 |
| 2 | 540 | 143370 | -574560 | 5051970 |
| 3 | 540 | 204071184 | 74810520 | -913383000 |

Remarkably, instanton numbers nd1,0n\_{d\_{1},0} are the same number 540 for all d1d\_{1}.
When we restrict ourselves to the regime q2≪q1q\_{2}\ll q\_{1} with q1=e2​π​i​t1q\_{1}=e^{2\pi it\_{1}} and q2=e2​π​i​t2q\_{2}=e^{2\pi it\_{2}} such that the t2t\_{2}-dependent instanton corrections are suppressed, only the sector with d2=0d\_{2}=0 contributes to the holomorphic Yukawa couplings.
In this regime, holomorphic Yukawa couplings are described by an Eisenstein series with weight 4:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y111\displaystyle y\_{111} | =9+540​∑k=0∞k3​q1k1−q1k=274+94​E4​(t1),\displaystyle=9+540\sum\_{k=0}^{\infty}\frac{k^{3}q\_{1}^{k}}{1-q\_{1}^{k}}=\frac{27}{4}+\frac{9}{4}E\_{4}(t\_{1}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y112\displaystyle y\_{112} | =3,\displaystyle=3, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y122\displaystyle y\_{122} | =1,\displaystyle=1, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | y222\displaystyle y\_{222} | =0,\displaystyle=0, |  | (3.5) |

where

|  |  |  |  |
| --- | --- | --- | --- |
|  | E4​(t)=1+240​∑k=0∞k3​qk1−qk.\displaystyle E\_{4}(t)=1+240\sum\_{k=0}^{\infty}\frac{k^{3}q^{k}}{1-q^{k}}. |  | (3.6) |

It indicates an existence of S​L​(2,ℤ)SL(2,\mathbb{Z}) modular symmetry, as confirmed at the level of period integrals [[29](#bib.bib29)].
When we move to the following basis:

|  |  |  |  |
| --- | --- | --- | --- |
|  | t:=t1,s:=32​t1+t2,\displaystyle t:=t^{1},\qquad s:=\frac{3}{2}t^{1}+t^{2}, |  | (3.7) |

the S​L​(2,ℤ)SL(2,\mathbb{Z}) symmetry can appear manifest in the regime qs≪qtq\_{s}\ll q\_{t} with qt:=q1q\_{t}:=q\_{1} and qs:=e2​π​i​s=q13/2​q2q\_{s}:=e^{2\pi is}=q\_{1}^{3/2}q\_{2}.
In this basis, the prepotential is rewritten in terms of the redefined moduli as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℱ\displaystyle{\cal F} | =−16​(94​t3+3​t​s2).\displaystyle=-\frac{1}{6}\left(\frac{9}{4}t^{3}+3ts^{2}\right). |  | (3.8) |

To see the modular invariance of the effective action, let us consider the modular weights of matter fields,
which can be read off from the moduli Kähler potential:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Kks\displaystyle K\_{\rm ks} | =−ln[i(38(t−\macc@depthΔ\macc@set@skewchar\macc@nested@a111t)3+12(t−\macc@depthΔ\macc@set@skewchar\macc@nested@a111t)(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s)2)].\displaystyle=-\ln\biggl[i\left(\frac{3}{8}(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})^{3}+\frac{1}{2}(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})^{2}\right)\biggl]. |  | (3.9) |

Since the corresponding moduli Kähler metric is given in the regime Im⁡(t)≪Im⁡(s){\rm Im}(t)\ll{\rm Im}(s):

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Kks)t​t¯≃−1(t−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t)2,(Kks)s​s¯≃−2(s−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s)2,(Kks)t​s¯=Ks​t¯≃0,\displaystyle(K\_{\rm ks})\_{t\bar{t}}\simeq-\frac{1}{(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})^{2}},\qquad(K\_{\rm ks})\_{s\bar{s}}\simeq-\frac{2}{(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})^{2}},\qquad(K\_{\rm ks})\_{t\bar{s}}=K\_{s\bar{t}}\simeq 0, |  | (3.10) |

one can determine the matter modular weights from tt-dependent part of the moduli Kähler metric by using Eq. ([2.1](#S2.E1 "In Kähler potential ‣ 2 Modular invariant effective action ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | Kt​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{t\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}} | ∼e13​(−Kks)​(Kks)t​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t≃1(t−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t)5/3,\displaystyle\sim e^{\frac{1}{3}(-K\_{\rm ks})}(K\_{\rm ks})\_{t\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}}\simeq\frac{1}{(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})^{5/3}}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ks​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{s\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s}} | ∼e13​(−Kks)​(Kks)s​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s≃(t−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t)1/3.\displaystyle\sim e^{\frac{1}{3}(-K\_{\rm ks})}(K\_{\rm ks})\_{s\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s}}\simeq(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})^{1/3}. |  | (3.11) |

It leads to the modular weights −53-\frac{5}{3} for At(𝟐𝟕)A^{({\bf 27})}\_{t} and 13\frac{1}{3} for As(𝟐𝟕)A^{({\bf 27})}\_{s}.
Then, the modular weights of holomorphic Yukawa couplings are determined, and their explicit forms are rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt​t​t\displaystyle y\_{ttt} | =94E4(t)(weight 4),\displaystyle=\frac{9}{4}E\_{4}(t)\qquad({\rm weight}\,4), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | yt​t​s\displaystyle y\_{tts} | =0(weight 2),\displaystyle=0\hskip 48.0pt({\rm weight}\,2), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | yt​s​s\displaystyle y\_{tss} | =1(weight 0),\displaystyle=1\hskip 48.0pt({\rm weight}\,0), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ys​s​s\displaystyle y\_{sss} | =0(weight−2).\displaystyle=0\hskip 48.0pt({\rm weight}\,-2). |  | (3.12) |

In this basis, they are described by modular forms of weights 4, 2, 0, -2, respectively.
Since there are no modular forms of weights 2 and -2 under S​L​(2,ℤ)SL(2,\mathbb{Z}), they are forced to be zero.
By definition, the modular form of weight 0 is just a modulus-independent constant.
Thus, this result is consistent with the modular invariance of 4D effective action.
Indeed, under the S​L​(2,ℤ)tSL(2,\mathbb{Z})\_{t} modular transformation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | t→a​t+bc​t+d\displaystyle t\rightarrow\frac{at+b}{ct+d} |  | (3.13) |

with a​d−b​c=1ad-bc=1, the Kähler potential and superpotential

|  |  |  |  |
| --- | --- | --- | --- |
|  | K\displaystyle K | =−ln[i2(t−\macc@depthΔ\macc@set@skewchar\macc@nested@a111t)(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s)2]+Kt​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t(𝟐𝟕)|At(𝟐𝟕)|2+Ks​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s(𝟐𝟕)|As(𝟐𝟕)|2,\displaystyle=-\ln\biggl[\frac{i}{2}(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})^{2}\biggl]+K^{({\bf 27})}\_{t\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}}|A^{({\bf 27})}\_{t}|^{2}+K^{({\bf 27})}\_{s\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s}}|A^{({\bf 27})}\_{s}|^{2}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | W\displaystyle W | =yt​t​t​At(𝟐𝟕)​At(𝟐𝟕)​At(𝟐𝟕)+yt​s​s​At(𝟐𝟕)​As(𝟐𝟕)​As(𝟐𝟕)\displaystyle=y\_{ttt}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{t}+y\_{tss}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{s}A^{({\bf 27})}\_{s} |  | (3.14) |

transform as

|  |  |  |  |
| --- | --- | --- | --- |
|  | K→K+ln⁡|c​t+d|2,W→(c​t+d)−1​W,\displaystyle K\rightarrow K+\ln|ct+d|^{2},\qquad W\rightarrow(ct+d)^{-1}W, |  | (3.15) |

and the Kähler invariant quantity eK​|W|2e^{K}|W|^{2} is modular invariant.

#### 3.1.2 Three moduli

We move to a CY threefold with a K3 fibration structure embedded in weighted projective spaces:

|  |  |  |
| --- | --- | --- |
|  | ℂ​ℙ​(641010640101)​[1212].\displaystyle\mathbb{CP}\begin{pmatrix}6&4&1&0&1&0\\ 6&4&0&1&0&1\end{pmatrix}\left[\begin{array}[]{c}12\\ 12\end{array}\right]. |  |

As studied in Ref. [[30](#bib.bib30)], the leading part of the prepotential for three Kähler moduli is described by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℱ\displaystyle{\cal F} | =−43​t13−t12​t2−t12​t3−t1​t2​t3,\displaystyle=-\frac{4}{3}t\_{1}^{3}-t\_{1}^{2}t\_{2}-t\_{1}^{2}t\_{3}-t\_{1}t\_{2}t\_{3}, |  | (3.18) |

where the triple intersection numbers are

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ111=8,κ112=2,κ113=2,κ123=1,\displaystyle\kappa\_{111}=8,\quad\kappa\_{112}=2,\quad\kappa\_{113}=2,\quad\kappa\_{123}=1, |  | (3.19) |

and otherwise 0. The holomorphic Yukawa couplings of matter fields are determined by the classical part and instanton
contribution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ya​b​c=κa​b​c+∑d1,d2,d3=0∞ca​b​c​(d1,d2,d3)​nd1,d2,d3​q1d1​q2d2​q3d31−q1d1​q2d2​q3d3,\displaystyle y\_{abc}=\kappa\_{abc}+\sum\_{d\_{1},d\_{2},d\_{3}=0}^{\infty}\frac{c\_{abc}(d\_{1},d\_{2},d\_{3})n\_{d\_{1},d\_{2},d\_{3}}q\_{1}^{d\_{1}}q\_{2}^{d\_{2}}q\_{3}^{d\_{3}}}{1-q\_{1}^{d\_{1}}q\_{2}^{d\_{2}}q\_{3}^{d\_{3}}}, |  | (3.20) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | ca​b​c​(d1,d2,d3)=da​db​dc,q1=e2​π​i​t1,q2=e2​π​i​t2,q3=e2​π​i​t3.\displaystyle c\_{abc}(d\_{1},d\_{2},d\_{3})=d\_{a}d\_{b}d\_{c},\quad q\_{1}=e^{2\pi it\_{1}},\quad q\_{2}=e^{2\pi it\_{2}},\quad q\_{3}=e^{2\pi it\_{3}}. |  | (3.21) |

Let us consider the regime q1,q2≪q3q\_{1},q\_{2}\ll q\_{3}; one can approximate the instanton expansion by focusing on d3=0d\_{3}=0.
The nonvanishing instanton numbers nd1,d2,0n\_{d\_{1},d\_{2},0} are given in Table [2](#S3.T2 "Table 2 ‣ 3.1.2 Three moduli ‣ 3.1 𝑆⁢𝐿⁢(2,ℤ) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications").

| d1d\_{1} ∖\setminus d2d\_{2} | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| 0 |  | -2 |  |  |
| 1 | 480 | 480 |  |  |
| 2 | 480 | 282888 | 480 |  |
| 3 | 480 | 17058560 | 17058560 | 480 |

As seen in the previous section, instanton numbers nd1,0n\_{d\_{1},0} and nd1,d1n\_{d\_{1},d\_{1}} are the same number 480 for all d1d\_{1}.
When we restrict ourselves to the regime q2≪q1q\_{2}\ll q\_{1} such that the t2t\_{2}-dependent instanton corrections are suppressed, the sector with d2=0d\_{2}=0 is relevant for holomorphic Yukawa couplings:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y111\displaystyle y\_{111} | =8+480​∑k=0∞k3​q1k1−q1k=6+2​E4​(t1),\displaystyle=8+480\sum\_{k=0}^{\infty}\frac{k^{3}q^{k}\_{1}}{1-q^{k}\_{1}}=6+2E\_{4}(t\_{1}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y112\displaystyle y\_{112} | =2,\displaystyle=2, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y113\displaystyle y\_{113} | =2,\displaystyle=2, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | y123\displaystyle y\_{123} | =1.\displaystyle=1. |  | (3.22) |

Since an Eisenstein function with weight 4 is a modular function under S​L​(2,ℤ)SL(2,\mathbb{Z}),
it indicates the S​L​(2,ℤ)SL(2,\mathbb{Z}) modular symmetry for the effective action of matter fields.
To check the modular invariance of the effective action, let us redefine the moduli as

|  |  |  |  |
| --- | --- | --- | --- |
|  | t:=t1,u:=t1+t2,s:=t1+t3.\displaystyle t:=t\_{1},\qquad u:=t\_{1}+t\_{2},\qquad s:=t\_{1}+t\_{3}. |  | (3.23) |

In this basis, the prepotential becomes

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℱ\displaystyle{\cal F} | =−43​t13−t12​t2−t12​t3−t1​t2​t3\displaystyle=-\frac{4}{3}t\_{1}^{3}-t\_{1}^{2}t\_{2}-t\_{1}^{2}t\_{3}-t\_{1}t\_{2}t\_{3} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =−16​(2​t3+6​t​u​s).\displaystyle=-\frac{1}{6}\left(2t^{3}+6tus\right). |  | (3.24) |

The limit q2→0q\_{2}\rightarrow 0 and q3→0q\_{3}\rightarrow 0 correspond to qu=e2​π​i​u=q2​qt→0q\_{u}=e^{2\pi iu}=q\_{2}q\_{t}\rightarrow 0 and qs=e2​π​i​t3=q3→0q^{s}=e^{2\pi it\_{3}}=q\_{3}\rightarrow 0, respectively.
The moduli Kähler potential is also given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Kks\displaystyle K\_{\rm ks} | =−ln[i(13(t−\macc@depthΔ\macc@set@skewchar\macc@nested@a111t)3+(t−\macc@depthΔ\macc@set@skewchar\macc@nested@a111t)(u−\macc@depthΔ\macc@set@skewchar\macc@nested@a111u)(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s))],\displaystyle=-\ln\biggl[i\left(\frac{1}{3}(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})^{3}+(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})(u-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u})(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})\right)\biggl], |  | (3.25) |

and the corresponding moduli Kähler metric in the regime Im⁡(t)≪Im⁡(s),Im⁡(u){\rm Im}(t)\ll{\rm Im}(s),{\rm Im}(u):

|  |  |  |  |
| --- | --- | --- | --- |
|  | (Kks)t​t¯\displaystyle(K\_{\rm ks})\_{t\bar{t}} | ≃−1(t−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t)2,(Kks)s​s¯≃−1(s−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s)2,\displaystyle\simeq-\frac{1}{(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})^{2}},\qquad(K\_{\rm ks})\_{s\bar{s}}\simeq-\frac{1}{(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})^{2}}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | (Kks)u​u¯\displaystyle(K\_{\rm ks})\_{u\bar{u}} | ≃−1(u−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​u)2,\displaystyle\simeq-\frac{1}{(u-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u})^{2}}, |  | (3.26) |

and otherwise 0.
By using Eq. ([2.1](#S2.E1 "In Kähler potential ‣ 2 Modular invariant effective action ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications")), one can determine the matter modular weights from tt-dependent part of the moduli Kähler metric:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Kt​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{t\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}} | ∼e13​(−Kks)​(Kks)t​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t≃1(t−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t)5/3,\displaystyle\sim e^{\frac{1}{3}(-K\_{\rm ks})}(K\_{\rm ks})\_{t\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}}\simeq\frac{1}{(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})^{5/3}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ku​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​u(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{u\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u}} | ∼e13​(−Kks)​(Kks)u​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​u≃(t−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t)1/3,\displaystyle\sim e^{\frac{1}{3}(-K\_{\rm ks})}(K\_{\rm ks})\_{u\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u}}\simeq(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})^{1/3}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ks​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{s\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s}} | ∼e13​(−Kks)​(Kks)s​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s≃(t−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t)1/3,\displaystyle\sim e^{\frac{1}{3}(-K\_{\rm ks})}(K\_{\rm ks})\_{s\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s}}\simeq(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})^{1/3}, |  | (3.27) |

that is, modular weight −53-\frac{5}{3} for At(𝟐𝟕)A^{({\bf 27})}\_{t} and 13\frac{1}{3} for As(𝟐𝟕)A^{({\bf 27})}\_{s} and Au(𝟐𝟕)A^{({\bf 27})}\_{u}.
Then, the modular weights of holomorphic Yukawa couplings are determined, and their explicit forms are rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt​t​t\displaystyle y\_{ttt} | =2E4(t)(weight 4),\displaystyle=2E\_{4}(t)\qquad({\rm weight}\,4), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ys​t​u\displaystyle y\_{stu} | =1(weight 0),\displaystyle=1\hskip 48.0pt({\rm weight}\,0), |  | (3.28) |

and otherwise 0.
In this basis, they are described by modular forms of weights 4, 0, respectively.
Thus, this result is consistent with the modular invariance of 4D effective action.
Indeed, under the S​L​(2,ℤ)tSL(2,\mathbb{Z})\_{t} modular transformation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | t→a​t+bc​t+d\displaystyle t\rightarrow\frac{at+b}{ct+d} |  | (3.29) |

with a​d−b​c=1ad-bc=1, the Kähler potential and superpotential

|  |  |  |  |
| --- | --- | --- | --- |
|  | K\displaystyle K | =−ln[i((t−\macc@depthΔ\macc@set@skewchar\macc@nested@a111t)(u−\macc@depthΔ\macc@set@skewchar\macc@nested@a111u)2+(t−\macc@depthΔ\macc@set@skewchar\macc@nested@a111t)(u−\macc@depthΔ\macc@set@skewchar\macc@nested@a111u)(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s))]+∑a,bKa​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​b(𝟐𝟕)Aa(𝟐𝟕)\macc@depthΔ\macc@set@skewchar\macc@nested@a111Ab(𝟐𝟕),\displaystyle=-\ln\biggl[i\left((t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})(u-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u})^{2}+(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})(u-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u})(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})\right)\biggl]+\sum\_{a,b}K^{({\bf 27})}\_{a\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{b}}A^{({\bf 27})}\_{a}\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{A^{({\bf 27})}\_{b}}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | W\displaystyle W | =yt​t​t​At(𝟐𝟕)​At(𝟐𝟕)​At(𝟐𝟕)+ys​t​u​As(𝟐𝟕)​At(𝟐𝟕)​Au(𝟐𝟕)\displaystyle=y\_{ttt}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{t}+y\_{stu}A^{({\bf 27})}\_{s}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{u} |  | (3.30) |

transform as

|  |  |  |  |
| --- | --- | --- | --- |
|  | K→K+ln⁡|c​t+d|2,W→(c​t+d)−1​W,\displaystyle K\rightarrow K+\ln|ct+d|^{2},\qquad W\rightarrow(ct+d)^{-1}W, |  | (3.31) |

and the Kähler invariant quantity eK​|W|2e^{K}|W|^{2} is modular invariant.

Note that this effective theory also seems to have another coupling selection rule.
The matter fields As(𝟐𝟕)A^{({\bf 27})}\_{s} and Au(𝟐𝟕)A^{({\bf 27})}\_{u} have the same modular weight.
The modular invariance allows ys​s​t​As(𝟐𝟕)​As(𝟐𝟕)​At(𝟐𝟕)y\_{sst}A^{({\bf 27})}\_{s}A^{({\bf 27})}\_{s}A^{({\bf 27})}\_{t} and
yt​u​u​At(𝟐𝟕)​Au(𝟐𝟕)​Au(𝟐𝟕)y\_{tuu}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{u}A^{({\bf 27})}\_{u} couplings.
For example, if As(𝟐𝟕)A^{({\bf 27})}\_{s} and Au(𝟐𝟕)A^{({\bf 27})}\_{u} are S4S\_{4} doublet and
At(𝟐𝟕)A^{({\bf 27})}\_{t} is a S4S\_{4} singlet, ys​s​t​As(𝟐𝟕)​As(𝟐𝟕)​At(𝟐𝟕)y\_{sst}A^{({\bf 27})}\_{s}A^{({\bf 27})}\_{s}A^{({\bf 27})}\_{t} and
yt​u​u​At(𝟐𝟕)​Au(𝟐𝟕)​Au(𝟐𝟕)y\_{tuu}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{u}A^{({\bf 27})}\_{u} couplings are forbidden, but
yt​t​t​At(𝟐𝟕)​At(𝟐𝟕)​At(𝟐𝟕)y\_{ttt}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{t} and ys​t​u​As(𝟐𝟕)​At(𝟐𝟕)​Au(𝟐𝟕)y\_{stu}A^{({\bf 27})}\_{s}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{u}
are allowed [[17](#bib.bib17)].
One can replace S4S\_{4} by S3S\_{3}.
The S4S\_{4} group as well as the S3S\_{3} group is originated from S​p​(8,ℤ)Sp(8,\mathbb{Z}).

### 3.2 Γ0​(3)\Gamma\_{0}(3) modular forms

In this section, we focus on specific CY threefolds with two moduli in Sec. [3.2.1](#S3.SS2.SSS1 "3.2.1 Two moduli ‣ 3.2 Γ_0⁢(3) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications") and three moduli
in Sec. [3.2.2](#S3.SS2.SSS2 "3.2.2 Three moduli ‣ 3.2 Γ_0⁢(3) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications"), leading to Γ0​(3)\Gamma\_{0}(3) modular form for holomorphic Yukawa couplings.
The Γ0​(N)\Gamma\_{0}(N) modular forms are summarized in Appendix [A](#A1 "Appendix A Γ_0⁢(𝑁) modular forms ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications").

#### 3.2.1 Two moduli

We start with a CY threefold defined by a hypersurface in a product of two projective spaces:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℂ​ℙ2ℂ​ℙ2​[33],\displaystyle\begin{matrix}\mathbb{CP}^{2}\\ \mathbb{CP}^{2}\\ \end{matrix}\begin{bmatrix}3\\ 3\\ \end{bmatrix}, |  | (3.32) |

where the number of Kähler moduli is h1,1=2h^{1,1}=2.
The moduli effective action was studied in Ref. [[31](#bib.bib31)] by using the mirror symmetry technique.
Here, we study whether the effective action of matter fields enjoys the modular symmetry.
By solving the corresponding Picard-Fuchs equation, the leading part of the prepotential for two Kähler moduli was known to be

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℱ\displaystyle{\cal F} | =−16​(9​t12​t2+9​t1​t22),\displaystyle=-\frac{1}{6}\left(9t\_{1}^{2}t\_{2}+9t\_{1}t\_{2}^{2}\right), |  | (3.33) |

where the triple intersection numbers are given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ111=κ222=0,κ112=κ122=3.\displaystyle\kappa\_{111}=\kappa\_{222}=0,\quad\kappa\_{112}=\kappa\_{122}=3. |  | (3.34) |

Instanton-corrected holomorphic Yukawa couplings are of the form:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ya​b​c\displaystyle y\_{abc} | =κa​b​c+∑d1,d2=0∞ca​b​c​(d1,d2)​nd1,d2​q1d1​q2d21−q1d1​q2d2,\displaystyle=\kappa\_{abc}+\sum\_{d\_{1},d\_{2}=0}^{\infty}\frac{c\_{abc}(d\_{1},d\_{2})n\_{d\_{1},d\_{2}}q\_{1}^{d\_{1}}q\_{2}^{d\_{2}}}{1-q\_{1}^{d\_{1}}q\_{2}^{d\_{2}}}, |  | (3.35) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | c111=(d1)3,c112=(d1)2​d2,c122=d1​(d2)2,c112=(d2)3.\displaystyle c\_{111}=(d\_{1})^{3},\quad c\_{112}=(d\_{1})^{2}d\_{2},\quad c\_{122}=d\_{1}(d\_{2})^{2},\quad c\_{112}=(d\_{2})^{3}. |  | (3.36) |

Here, the instanton numbers nd1,d2n\_{d\_{1},d\_{2}} are given in Table. [3](#S3.T3 "Table 3 ‣ 3.2.1 Two moduli ‣ 3.2 Γ_0⁢(3) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications").

| d1d\_{1} ∖\setminus d2d\_{2} | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 |  | 189 | 189 | 162 | 189 | 189 | 162 |
| 1 | 189 | 8262 | 142884 | 1492290 | 11375073 | 69962130 |  |
| 2 | 189 | 142884 | 13108392 | 516953097 | 12289326723 |  |  |
| 3 | 162 | 1492290 | 516953097 | 55962304650 |  |  |  |
| 4 | 189 | 11375073 | 12289326723 |  |  |  |  |
| 5 | 189 | 69962130 |  |  |  |  |  |
| 6 | 162 |  |  |  |  |  |  |

Remarkably, instanton numbers nd1,0n\_{d\_{1},0} have an interesting structure such as
nd1,0=162n\_{d\_{1},0}=162 for d1=3​ℤ+d\_{1}=3\mathbb{Z}\_{+} and otherwise 189.
Thus, when we restrict ourselves to the regime q2≪q1q\_{2}\ll q\_{1} such that the t2t\_{2}-dependent instanton corrections are suppressed, only t1t\_{1}-dependent instantons contribute to the holomorphic Yukawa couplings.
In particular, one of the holomorphic Yukawa couplings is described by an Eisenstein series with weight 4:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y111\displaystyle y\_{111} | =189​∑k=0∞k3​q1k1−q1k−27​∑m=0∞(3​m)3​q13​m1−q13​m\displaystyle=189\sum\_{k=0}^{\infty}\frac{k^{3}q^{k}\_{1}}{1-q^{k}\_{1}}-27\sum\_{m=0}^{\infty}\frac{(3m)^{3}q^{3m}\_{1}}{1-q^{3m}\_{1}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =189240​(1+240​∑k=0∞k3​q1k1−q1k)−272240​(1+240​∑m=0∞(m)3​q3​m1−q13​m)+94\displaystyle=\frac{189}{240}\left(1+240\sum\_{k=0}^{\infty}\frac{k^{3}q^{k}\_{1}}{1-q^{k}\_{1}}\right)-\frac{27^{2}}{240}\left(1+240\sum\_{m=0}^{\infty}\frac{(m)^{3}q^{3m}}{1-q^{3m}\_{1}}\right)+\frac{9}{4} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =94+6380​E4​(t1)−24380​E4​(3​t1),\displaystyle=\frac{9}{4}+\frac{63}{80}E\_{4}(t\_{1})-\frac{243}{80}E\_{4}(3t\_{1}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y112\displaystyle y\_{112} | =3,\displaystyle=3, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y122\displaystyle y\_{122} | =3,\displaystyle=3, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | y222\displaystyle y\_{222} | =0.\displaystyle=0. |  | (3.37) |

Since E4​(3​τ)E\_{4}(3\tau) is not a modular form under S​L​(2,ℤ)SL(2,\mathbb{Z}), the effective action does not have the full S​L​(2,ℤ)SL(2,\mathbb{Z}) modular symmetry.
However, as shown in Appendix [A.2](#A1.SS2 "A.2 Weight 4 ‣ Appendix A Γ_0⁢(𝑁) modular forms ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications"), both E4​(τ)E\_{4}(\tau) and E4​(3​τ)E\_{4}(3\tau) are modular forms of weight 4 under Γ0​(3)\Gamma\_{0}(3).
To see the modular invariance of the effective action, we move to the following basis:

|  |  |  |  |
| --- | --- | --- | --- |
|  | t:=t1,s:=12​t1+t2,\displaystyle t:=t\_{1},\qquad s:=\frac{1}{2}t\_{1}+t\_{2}, |  | (3.38) |

where q2≪q1q\_{2}\ll q\_{1} corresponds to qs≪qtq\_{s}\ll q\_{t} with qs:=q11/2​q2q\_{s}:=q\_{1}^{1/2}q\_{2} and qt:=q1q\_{t}:=q\_{1}.
In this basis, the prepotential is rewritten in terms of the redefined moduli as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℱ\displaystyle{\cal F} | =−16​(−94​t3+9​t​s2).\displaystyle=-\frac{1}{6}\left(-\frac{9}{4}t^{3}+9ts^{2}\right). |  | (3.39) |

Since the moduli Kähler potential is approximately given in the regime Im⁡(t)≪Im⁡(s){\rm Im}(t)\ll{\rm Im}(s):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Kks\displaystyle K\_{\rm ks} | =−ln[3​i2(t−\macc@depthΔ\macc@set@skewchar\macc@nested@a111t)(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s)2],\displaystyle=-\ln\biggl[\frac{3i}{2}(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})^{2}\biggl], |  | (3.40) |

the corresponding moduli Kähler metric is found as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | (Kks)t​t¯≃−1(t−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t)2,(Kks)s​s¯≃−2(s−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s)2,(Kks)t​s¯=(Kks)s​t¯≃0.\displaystyle(K\_{\rm ks})\_{t\bar{t}}\simeq-\frac{1}{(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})^{2}},\qquad(K\_{\rm ks})\_{s\bar{s}}\simeq-\frac{2}{(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})^{2}},\qquad(K\_{\rm ks})\_{t\bar{s}}=(K\_{\rm ks})\_{s\bar{t}}\simeq 0. |  | (3.41) |

Thus, one can read off the matter modular weights from a tt-dependent part of the moduli Kähler metric by using Eq. ([2.1](#S2.E1 "In Kähler potential ‣ 2 Modular invariant effective action ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | Kt​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{t\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}} | ∼e13​(−Kks)(Kks)t​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t∝(t−\macc@depthΔ\macc@set@skewchar\macc@nested@a111t)−5/3,\displaystyle\sim e^{\frac{1}{3}(-K\_{\rm ks})}(K\_{\rm ks})\_{t\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}}\propto(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})^{-5/3}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ks​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{s\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s}} | ∼e13​(−Kks)​(Kks)s​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s∝(t−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t)1/3.\displaystyle\sim e^{\frac{1}{3}(-K\_{\rm ks})}(K\_{\rm ks})\_{s\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s}}\propto(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})^{1/3}. |  | (3.42) |

It leads to the modular weight −53-\frac{5}{3} for At(𝟐𝟕)A^{({\bf 27})}\_{t} and 13\frac{1}{3} for As(𝟐𝟕)A^{({\bf 27})}\_{s}.
In this basis, the nonvanishing holomorphic Yukawa couplings are also rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt​t​t\displaystyle y\_{ttt} | =6380E4(t)−24380E4(3t)(weight 4),\displaystyle=\frac{63}{80}E\_{4}(t)-\frac{243}{80}E\_{4}(3t)\qquad({\rm weight}\,4), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | yt​s​s\displaystyle y\_{tss} | =9(weight 0),\displaystyle=9\hskip 118.0pt({\rm weight}\,0), |  | (3.43) |

which correspond to the modular forms of weight 4 and 0 under Γ0​(3)\Gamma\_{0}(3), respectively.
Note that yt​t​sy\_{tts} vanishes, although the modular weight of yt​t​sy\_{tts} must be 2 and
there exists a modular form of weight 2 under Γ0​(3)\Gamma\_{0}(3).
(See Appendix [A](#A1 "Appendix A Γ_0⁢(𝑁) modular forms ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications").)
It suggests that the low-energy effective field theory derived from this CY compactification
has another coupling selection rule in addition to the Γ0​(3)\Gamma\_{0}(3) modular symmetry.
If At(𝟐𝟕)A^{({\bf 27})}\_{t} has even Z2Z\_{2} charge and As(𝟐𝟕)A^{({\bf 27})}\_{s} has odd Z2Z\_{2} charge,
the yt​t​t​At(𝟐𝟕)​At(𝟐𝟕)​At(𝟐𝟕)y\_{ttt}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{t} coupling and the yt​s​s​At(𝟐𝟕)​As(𝟐𝟕)​As(𝟐𝟕)y\_{tss}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{s}A^{({\bf 27})}\_{s} coupling are allowed, but the yt​t​s​At(𝟐𝟕)​At(𝟐𝟕)​As(𝟐𝟕)y\_{tts}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{s}
coupling is forbidden.
Such Z2Z\_{2} charges can be originated from S​p​(6,ℤ)Sp(6,\mathbb{Z}).
At any rate, the above result is consistent with the modular invariance of 4D effective action.

To check the modular invariance of the effective action, let us consider the Γ0​(3)\Gamma\_{0}(3) modular transformation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | t→a​t+bc​t+d\displaystyle t\rightarrow\frac{at+b}{ct+d} |  | (3.44) |

with a​d−b​c=1ad-bc=1 and c≡0c\equiv 0 (mod 33), the Kähler potential and superpotential

|  |  |  |  |
| --- | --- | --- | --- |
|  | K\displaystyle K | =−ln[i2(t−\macc@depthΔ\macc@set@skewchar\macc@nested@a111t)(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s)2]+Kt​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t(𝟐𝟕)|At(𝟐𝟕)|2+Ks​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s(𝟐𝟕)|As(𝟐𝟕)|2,\displaystyle=-\ln\biggl[\frac{i}{2}(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})^{2}\biggl]+K^{({\bf 27})}\_{t\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}}|A^{({\bf 27})}\_{t}|^{2}+K^{({\bf 27})}\_{s\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s}}|A^{({\bf 27})}\_{s}|^{2}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | W\displaystyle W | =yt​t​t​At(𝟐𝟕)​At(𝟐𝟕)​At(𝟐𝟕)+yt​s​s​At(𝟐𝟕)​As(𝟐𝟕)​As(𝟐𝟕)\displaystyle=y\_{ttt}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{t}+y\_{tss}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{s}A^{({\bf 27})}\_{s} |  | (3.45) |

transform as

|  |  |  |  |
| --- | --- | --- | --- |
|  | K→K+ln⁡|c​t+d|2,W→(c​t+d)−1​W,\displaystyle K\rightarrow K+\ln|ct+d|^{2},\qquad W\rightarrow(ct+d)^{-1}W, |  | (3.46) |

and the Kähler invariant quantity eK​|W|2e^{K}|W|^{2} is modular invariant.

Note that instanton numbers n0,d2n\_{0,d\_{2}} have the same behavior as nd1,0n\_{d\_{1},0}.
Similarly, we can discuss the regime q1≪q2q\_{1}\ll q\_{2}.
Then, we can find the Γ0​(3)\Gamma\_{0}(3) modular symmetry and its modular forms.

#### 3.2.2 Three moduli

We move to a favorable complete intersection CY threefold:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℂ​ℙ1ℂ​ℙ1ℂ​ℙ3​[022031],\displaystyle\begin{matrix}\mathbb{CP}^{1}\\ \mathbb{CP}^{1}\\ \mathbb{CP}^{3}\\ \end{matrix}\begin{bmatrix}0&2\\ 2&0\\ 3&1\\ \end{bmatrix}, |  | (3.47) |

where the number of Kähler moduli is h1,1=3h^{1,1}=3.
As studied in Ref. [[30](#bib.bib30)], the leading part of the prepotential for three Kähler moduli is calculated as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℱ\displaystyle{\cal F} | =−16​(18​t12​t2+18​t12​t3+18​t1​t2​t3),\displaystyle=-\frac{1}{6}\left(18t\_{1}^{2}t\_{2}+18t\_{1}^{2}t\_{3}+18t\_{1}t\_{2}t\_{3}\right), |  | (3.48) |

where the triple intersection numbers are

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ112=6,κ113=6,κ123=3,\displaystyle\kappa\_{112}=6,\quad\kappa\_{113}=6,\quad\kappa\_{123}=3, |  | (3.49) |

and otherwise 0. The holomorphic Yukawa couplings of matter fields are determined by the classical part and instanton
contribution as in Eq. ([3.20](#S3.E20 "In 3.1.2 Three moduli ‣ 3.1 𝑆⁢𝐿⁢(2,ℤ) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications")).
Let us consider the regime q2≪q1,q3q\_{2}\ll q\_{1},q\_{3} such that only q1,3q\_{1,3} are relevant for the instanton expansion.
The nonvanishing instanton numbers nd1,0,d3n\_{d\_{1},0,d\_{3}} are given in Table [4](#S3.T4 "Table 4 ‣ 3.2.2 Three moduli ‣ 3.2 Γ_0⁢(3) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications").

| d1d\_{1} ∖\setminus d3d\_{3} | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| 0 |  | 18 |  |  |  |
| 1 | 216 | 216 |  |  |  |
| 2 | 216 | 2106 | 216 |  |  |
| 3 | 48 | 17856 | 17856 | 48 |  |
| 4 | 216 | 95094 | 414720 | 95094 | 216 |

As seen in the previous section, instanton numbers nd1,0,0n\_{d\_{1},0,0} and nd1,0,d1n\_{d\_{1},0,d\_{1}} have an interesting structure such as
nd1,0,0=nd1,0,d1=48n\_{d\_{1},0,0}=n\_{d\_{1},0,d\_{1}}=48 for d1=3​ℤ+d\_{1}=3\mathbb{Z}\_{+} and otherwise 216.
Thus, when we restrict ourselves to the regime q3≪q1q\_{3}\ll q\_{1} such that the t3t\_{3}-dependent instanton corrections are suppressed, only
the modulus t1t\_{1} contributes to the holomorphic Yukawa couplings.66
6
We can realize the same structure in the regime q1=q3q\_{1}=q\_{3}.
In particular, one of the holomorphic Yukawa couplings is described by an Eisenstein series with weight 4.
We list the nonvanishing holomorphic Yukawa couplings:

|  |  |  |  |
| --- | --- | --- | --- |
|  | y111\displaystyle y\_{111} | =216​∑k=0∞k3​q1k1−q1k−168​∑m=0∞(3​m)3​q13​m1−q13​m\displaystyle=216\sum\_{k=0}^{\infty}\frac{k^{3}q\_{1}^{k}}{1-q\_{1}^{k}}-168\sum\_{m=0}^{\infty}\frac{(3m)^{3}q\_{1}^{3m}}{1-q\_{1}^{3m}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =216240​(1+240​∑k=0∞k3​q1k1−q1k)−168×27240​(1+240​∑m=0∞(m)3​q13​m1−q13​m)+18\displaystyle=\frac{216}{240}\left(1+240\sum\_{k=0}^{\infty}\frac{k^{3}q\_{1}^{k}}{1-q\_{1}^{k}}\right)-\frac{168\times 27}{240}\left(1+240\sum\_{m=0}^{\infty}\frac{(m)^{3}q\_{1}^{3m}}{1-q\_{1}^{3m}}\right)+18 |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =18+910​E4​(t1)−18910​E4​(3​t1),\displaystyle=18+\frac{9}{10}E\_{4}(t\_{1})-\frac{189}{10}E\_{4}(3t\_{1}), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y112\displaystyle y\_{112} | =6,\displaystyle=6, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y113\displaystyle y\_{113} | =6,\displaystyle=6, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | y123\displaystyle y\_{123} | =3.\displaystyle=3. |  | (3.50) |

Thus, we observe the Γ0​(3)\Gamma\_{0}(3) modular form in the same manner as in the previous example.
To see the modular invariance of the effective action, we move to the following basis:

|  |  |  |  |
| --- | --- | --- | --- |
|  | t:=t1,s:=t1+t2,u:=t1+t3,\displaystyle t:=t\_{1},\qquad s:=t\_{1}+t\_{2},\qquad u:=t\_{1}+t\_{3}, |  | (3.51) |

where the regime q2,q3≪q1q\_{2},q\_{3}\ll q\_{1} correspond to qs,qu≪qtq\_{s},q\_{u}\ll q\_{t} with qu:=e2​π​i​uq\_{u}:=e^{2\pi iu}, qs:=e2​π​i​sq\_{s}:=e^{2\pi is} and qt:=e2​π​i​tq\_{t}:=e^{2\pi it}.
In this basis, the prepotential is rewritten in terms of the redefined moduli as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℱ\displaystyle{\cal F} | =−16​(−18​t3+18​s​t​u).\displaystyle=-\frac{1}{6}\left(-18t^{3}+18stu\right). |  | (3.52) |

Since the moduli Kähler potential is approximately given in the regime Im⁡(t)≪Im⁡(s),Im⁡(u){\rm Im}(t)\ll{\rm Im}(s),{\rm Im}(u):

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Kks\displaystyle K\_{\rm ks} | =−ln[3i(t−\macc@depthΔ\macc@set@skewchar\macc@nested@a111t)(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s)(u−\macc@depthΔ\macc@set@skewchar\macc@nested@a111u)],\displaystyle=-\ln\biggl[3i(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})(u-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u})\biggl], |  | (3.53) |

the corresponding moduli Kähler metric is found as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | (Kks)t​t¯≃−1(t−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t)2,(Kks)s​s¯≃−1(s−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s)2,(Kks)u​u¯≃−1(u−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​u)2,\displaystyle(K\_{\rm ks})\_{t\bar{t}}\simeq-\frac{1}{(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})^{2}},\qquad(K\_{\rm ks})\_{s\bar{s}}\simeq-\frac{1}{(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})^{2}},\qquad(K\_{\rm ks})\_{u\bar{u}}\simeq-\frac{1}{(u-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u})^{2}}, |  | (3.54) |

and otherwise 0.
Thus, one can read off the matter modular weights from a tt-dependent part of the moduli Kähler metric by using Eq. ([2.1](#S2.E1 "In Kähler potential ‣ 2 Modular invariant effective action ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | Kt​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{t\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}} | ∼e13​(−Kks)(Kks)t​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t∝(t−\macc@depthΔ\macc@set@skewchar\macc@nested@a111t)−5/3,\displaystyle\sim e^{\frac{1}{3}(-K\_{\rm ks})}(K\_{\rm ks})\_{t\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}}\propto(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})^{-5/3}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ks​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{s\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s}} | ∼e13​(−Kks)​(Kks)s​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s∝(t−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t)1/3,\displaystyle\sim e^{\frac{1}{3}(-K\_{\rm ks})}(K\_{\rm ks})\_{s\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s}}\propto(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})^{1/3}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Ku​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​u(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{u\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u}} | ∼e13​(−Kks)​(Kks)u​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​u∝(t−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t)1/3.\displaystyle\sim e^{\frac{1}{3}(-K\_{\rm ks})}(K\_{\rm ks})\_{u\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u}}\propto(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})^{1/3}. |  | (3.55) |

It leads to the modular weight −53-\frac{5}{3} for At(𝟐𝟕)A^{({\bf 27})}\_{t} and 13\frac{1}{3} for As(𝟐𝟕)A^{({\bf 27})}\_{s} and Au(𝟐𝟕)A^{({\bf 27})}\_{u}.
The holomorphic Yukawa couplings are also rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | yt​t​t\displaystyle y\_{ttt} | =910E4(t)−18910E4(3t)(weight 4),\displaystyle=\frac{9}{10}E\_{4}(t)-\frac{189}{10}E\_{4}(3t)\qquad({\rm weight}\,4), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | yt​s​u\displaystyle y\_{tsu} | =3(weight 0),\displaystyle=3\hskip 118.0pt({\rm weight}\,0), |  | (3.56) |

and otherwise 0.
In this basis, they are described by modular forms of weights 4 and 0 under Γ0​(3)\Gamma\_{0}(3), respectively.
Thus, this result is consistent with the modular invariance of 4D effective action. Note that the effective theory has the same coupling selection rule, as shown in Sec. [3.1.2](#S3.SS1.SSS2 "3.1.2 Three moduli ‣ 3.1 𝑆⁢𝐿⁢(2,ℤ) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications").

To check the modular invariance of the effective action, let us consider the Γ0​(3)\Gamma\_{0}(3) modular transformation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | t→a​t+bc​t+d\displaystyle t\rightarrow\frac{at+b}{ct+d} |  | (3.57) |

with a​d−b​c=1ad-bc=1 and c≡0c\equiv 0 (mod 33), under which the Kähler potential and superpotential

|  |  |  |  |
| --- | --- | --- | --- |
|  | K\displaystyle K | =−ln[i(t−\macc@depthΔ\macc@set@skewchar\macc@nested@a111t)(u−\macc@depthΔ\macc@set@skewchar\macc@nested@a111u)(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s)]+∑a,bKa​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​b(𝟐𝟕)Aa(𝟐𝟕)\macc@depthΔ\macc@set@skewchar\macc@nested@a111Ab(𝟐𝟕),\displaystyle=-\ln\biggl[i(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})(u-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u})(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})\biggl]+\sum\_{a,b}K^{({\bf 27})}\_{a\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{b}}A^{({\bf 27})}\_{a}\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{A^{({\bf 27})}\_{b}}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | W\displaystyle W | =yt​t​t​At(𝟐𝟕)​At(𝟐𝟕)​At(𝟐𝟕)+ys​t​u​As(𝟐𝟕)​At(𝟐𝟕)​Au(𝟐𝟕)\displaystyle=y\_{ttt}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{t}+y\_{stu}A^{({\bf 27})}\_{s}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{u} |  | (3.58) |

transform as

|  |  |  |  |
| --- | --- | --- | --- |
|  | K→K+ln⁡|c​t+d|2,W→(c​t+d)−1​W.\displaystyle K\rightarrow K+\ln|ct+d|^{2},\qquad W\rightarrow(ct+d)^{-1}W. |  | (3.59) |

Thus, the Kähler invariant quantity eK​|W|2e^{K}|W|^{2} is modular invariant.

### 3.3 Γ0​(4)\Gamma\_{0}(4) modular forms

In this section, we focus on specific CY threefolds with three moduli in Sec. [3.3.1](#S3.SS3.SSS1 "3.3.1 Three moduli ‣ 3.3 Γ_0⁢(4) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications") and four moduli
in Sec. [3.3.2](#S3.SS3.SSS2 "3.3.2 Four moduli ‣ 3.3 Γ_0⁢(4) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications"), leading to Γ0​(4)\Gamma\_{0}(4) modular forms for holomorphic Yukawa couplings.
The Γ0​(N)\Gamma\_{0}(N) modular forms are summarized in Appendix [A](#A1 "Appendix A Γ_0⁢(𝑁) modular forms ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications").

#### 3.3.1 Three moduli

We start with a CY threefold defined by a single polynomial in three projective spaces:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℂ​ℙ1ℂ​ℙ1ℂ​ℙ3​[223],\displaystyle\begin{matrix}\mathbb{CP}^{1}\\ \mathbb{CP}^{1}\\ \mathbb{CP}^{3}\\ \end{matrix}\begin{bmatrix}2\\ 2\\ 3\\ \end{bmatrix}, |  | (3.60) |

where the number of Kähler moduli is h1,1=3h^{1,1}=3.
As studied in Ref. [[32](#bib.bib32)], the leading part of the prepotential for three Kähler moduli is calculated as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℱ\displaystyle{\cal F} | =−16​(6​t1​t32+6​t2​t32+18​t1​t2​t3),\displaystyle=-\frac{1}{6}\left(6t\_{1}t\_{3}^{2}+6t\_{2}t\_{3}^{2}+18t\_{1}t\_{2}t\_{3}\right), |  | (3.61) |

where the triple intersection numbers are

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ233=2,κ133=2,κ123=3,\displaystyle\kappa\_{233}=2,\quad\kappa\_{133}=2,\quad\kappa\_{123}=3, |  | (3.62) |

and otherwise 0. The holomorphic Yukawa couplings of matter fields are determined by the classical part and instanton
contribution as in Eq. ([3.20](#S3.E20 "In 3.1.2 Three moduli ‣ 3.1 𝑆⁢𝐿⁢(2,ℤ) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications")).
Let us consider the regime q3≪q1,q2q\_{3}\ll q\_{1},q\_{2}; only q1,2q\_{1,2} contribute to the instanton expansion.
The nonvanishing instanton numbers nd1,d2,0n\_{d\_{1},d\_{2},0} are given in Table [5](#S3.T5 "Table 5 ‣ 3.3.1 Three moduli ‣ 3.3 Γ_0⁢(4) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications").

| d1d\_{1} ∖\setminus d2d\_{2} | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| 0 |  | 54 |  |  |  |
| 1 | 54 | 180 | 54 |  |  |
| 2 |  | 54 | 144 | 54 |  |
| 3 |  |  | 54 | 180 | 54 |
| 4 |  |  |  | 54 | 144 |

Remarkably, instanton numbers nd1,0,0n\_{d\_{1},0,0} and nd1,d2,0n\_{d\_{1},d\_{2},0} have an interesting structure, i.e.,
nd1+1,d1,0=nd1,d1+1,0=54n\_{d\_{1}+1,d\_{1},0}=n\_{d\_{1},d\_{1}+1,0}=54 for all d1d\_{1}, and nd1,d1=144n\_{d\_{1},d\_{1}}=144 for d1=2​ℤ+d\_{1}=2\mathbb{Z}\_{+} and otherwise 180.
Specifically, nonvanishing holomorphic Yukawa couplings are described by

|  |  |  |  |
| --- | --- | --- | --- |
|  | y111\displaystyle y\_{111} | =∑d1,d2=0∞(d1)3​nd1,d2,0​q1d1​q2d21−q1d1​q2d2\displaystyle=\sum\_{d\_{1},d\_{2}=0}^{\infty}\frac{(d\_{1})^{3}n\_{d\_{1},d\_{2},0}q\_{1}^{d\_{1}}q\_{2}^{d\_{2}}}{1-q\_{1}^{d\_{1}}q\_{2}^{d\_{2}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑d1=0∞[(d1)3​nd1,d1,0​q1d1​q2d11−q1d1​q2d1+(d1)3​nd1,d1+1,0​q1d1​q2d1+11−q1d1​q2d1+1+(d1+1)3​nd1+1,d1,0​q1d1+1​q2d11−q1d1+1​q2d1],\displaystyle=\sum\_{d\_{1}=0}^{\infty}\biggl[\frac{(d\_{1})^{3}n\_{d\_{1},d\_{1},0}q\_{1}^{d\_{1}}q\_{2}^{d\_{1}}}{1-q\_{1}^{d\_{1}}q\_{2}^{d\_{1}}}+\frac{(d\_{1})^{3}n\_{d\_{1},d\_{1}+1,0}q\_{1}^{d\_{1}}q\_{2}^{d\_{1}+1}}{1-q\_{1}^{d\_{1}}q\_{2}^{d\_{1}+1}}+\frac{(d\_{1}+1)^{3}n\_{d\_{1}+1,d\_{1},0}q\_{1}^{d\_{1}+1}q\_{2}^{d\_{1}}}{1-q\_{1}^{d\_{1}+1}q\_{2}^{d\_{1}}}\biggl], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y112\displaystyle y\_{112} | =∑d1,d2=0∞(d1)2​d2​nd1,d2,0​q1d1​q2d21−q1d1​q2d2\displaystyle=\sum\_{d\_{1},d\_{2}=0}^{\infty}\frac{(d\_{1})^{2}d\_{2}n\_{d\_{1},d\_{2},0}q\_{1}^{d\_{1}}q\_{2}^{d\_{2}}}{1-q\_{1}^{d\_{1}}q\_{2}^{d\_{2}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑d1=0∞[(d1)3​nd1,d1,0​q1d1​q2d11−q1d1​q2d1+(d1)2​(d1+1)​nd1,d1+1,0​q1d1​q2d1+11−q1d1​q2d1+1+(d1+1)2​d1​nd1+1,d1,0​q1d1+1​q2d11−q1d1+1​q2d1],\displaystyle=\sum\_{d\_{1}=0}^{\infty}\biggl[\frac{(d\_{1})^{3}n\_{d\_{1},d\_{1},0}q\_{1}^{d\_{1}}q\_{2}^{d\_{1}}}{1-q\_{1}^{d\_{1}}q\_{2}^{d\_{1}}}+\frac{(d\_{1})^{2}(d\_{1}+1)n\_{d\_{1},d\_{1}+1,0}q\_{1}^{d\_{1}}q\_{2}^{d\_{1}+1}}{1-q\_{1}^{d\_{1}}q\_{2}^{d\_{1}+1}}+\frac{(d\_{1}+1)^{2}d\_{1}n\_{d\_{1}+1,d\_{1},0}q\_{1}^{d\_{1}+1}q\_{2}^{d\_{1}}}{1-q\_{1}^{d\_{1}+1}q\_{2}^{d\_{1}}}\biggl], |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y122\displaystyle y\_{122} | =∑d1,d2=0∞d1​(d2)2​nd1,d2,0​q1d1​q2d21−q1d1​q2d2\displaystyle=\sum\_{d\_{1},d\_{2}=0}^{\infty}\frac{d\_{1}(d\_{2})^{2}n\_{d\_{1},d\_{2},0}q\_{1}^{d\_{1}}q\_{2}^{d\_{2}}}{1-q\_{1}^{d\_{1}}q\_{2}^{d\_{2}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑d1=0∞[(d1)3​nd1,d1,0​q1d1​q2d11−q1d1​q2d1+d1​(d1+1)2​nd1,d1+1,0​q1d1​q2d1+11−q1d1​q2d1+1+(d1+1)​(d1)2​nd1+1,d1,0​q1d1+1​q2d11−q1d1+1​q2d1]\displaystyle=\sum\_{d\_{1}=0}^{\infty}\biggl[\frac{(d\_{1})^{3}n\_{d\_{1},d\_{1},0}q\_{1}^{d\_{1}}q\_{2}^{d\_{1}}}{1-q\_{1}^{d\_{1}}q\_{2}^{d\_{1}}}+\frac{d\_{1}(d\_{1}+1)^{2}n\_{d\_{1},d\_{1}+1,0}q\_{1}^{d\_{1}}q\_{2}^{d\_{1}+1}}{1-q\_{1}^{d\_{1}}q\_{2}^{d\_{1}+1}}+\frac{(d\_{1}+1)(d\_{1})^{2}n\_{d\_{1}+1,d\_{1},0}q\_{1}^{d\_{1}+1}q\_{2}^{d\_{1}}}{1-q\_{1}^{d\_{1}+1}q\_{2}^{d\_{1}}}\biggl] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =y112,\displaystyle=y\_{112}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y222\displaystyle y\_{222} | =∑d1,d2=0∞(d2)3​nd1,d2,0​q1d1​q2d21−q1d1​q2d2\displaystyle=\sum\_{d\_{1},d\_{2}=0}^{\infty}\frac{(d\_{2})^{3}n\_{d\_{1},d\_{2},0}q\_{1}^{d\_{1}}q\_{2}^{d\_{2}}}{1-q\_{1}^{d\_{1}}q\_{2}^{d\_{2}}} |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑d1=0∞[(d1)3​nd1,d1,0​q1d1​q2d11−q1d1​q2d1+(d1+1)3​nd1,d1+1,0​q1d1​q2d1+11−q1d1​q2d1+1+(d1)3​nd1+1,d1,0​q1d1+1​q2d11−q1d1+1​q2d1]\displaystyle=\sum\_{d\_{1}=0}^{\infty}\biggl[\frac{(d\_{1})^{3}n\_{d\_{1},d\_{1},0}q\_{1}^{d\_{1}}q\_{2}^{d\_{1}}}{1-q\_{1}^{d\_{1}}q\_{2}^{d\_{1}}}+\frac{(d\_{1}+1)^{3}n\_{d\_{1},d\_{1}+1,0}q\_{1}^{d\_{1}}q\_{2}^{d\_{1}+1}}{1-q\_{1}^{d\_{1}}q\_{2}^{d\_{1}+1}}+\frac{(d\_{1})^{3}n\_{d\_{1}+1,d\_{1},0}q\_{1}^{d\_{1}+1}q\_{2}^{d\_{1}}}{1-q\_{1}^{d\_{1}+1}q\_{2}^{d\_{1}}}\biggl] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =y111,\displaystyle=y\_{111}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | y123\displaystyle y\_{123} | =3,y233=y133=2.\displaystyle=3,\qquad y\_{233}=y\_{133}=2. |  | (3.63) |

When we restrict ourselves to the regime t1=t2t\_{1}=t\_{2},
they are rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | y111\displaystyle y\_{111} | =∑d1=0∞[(d1)3​nd1,d1,0​q12​d11−q12​d1+54(d1)3​q12​d1+11−q12​d1+1+54(d1+1)3​q12​d1+11−q12​d1+1]\displaystyle=\sum\_{d\_{1}=0}^{\infty}\biggl[\frac{(d\_{1})^{3}n\_{d\_{1},d\_{1},0}q\_{1}^{2d\_{1}}}{1-q\_{1}^{2d\_{1}}}+54\frac{(d\_{1})^{3}q\_{1}^{2d\_{1}+1}}{1-q\_{1}^{2d\_{1}+1}}+54\frac{(d\_{1}+1)^{3}q\_{1}^{2d\_{1}+1}}{1-q\_{1}^{2d\_{1}+1}}\biggl] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑d1=0∞[180(d1)3​q12​d11−q12​d1−36(2​d1)3​q12​(2​d1)1−q12​(2​d1)+544((2​d1+1)3​q12​d1+11−q12​d1+1+3(2​d1+1)​q12​d1+11−q12​d1+1)]\displaystyle=\sum\_{d\_{1}=0}^{\infty}\biggl[180\frac{(d\_{1})^{3}q\_{1}^{2d\_{1}}}{1-q\_{1}^{2d\_{1}}}-36\frac{(2d\_{1})^{3}q\_{1}^{2(2d\_{1})}}{1-q\_{1}^{2(2d\_{1})}}+\frac{54}{4}\left(\frac{(2d\_{1}+1)^{3}q\_{1}^{2d\_{1}+1}}{1-q\_{1}^{2d\_{1}+1}}+3\frac{(2d\_{1}+1)q\_{1}^{2d\_{1}+1}}{1-q\_{1}^{2d\_{1}+1}}\right)\biggl] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =180​(E4​(2​t1)−1240)−288​(E4​(4​t1)−1240)\displaystyle=180\left(\frac{E\_{4}(2t\_{1})-1}{240}\right)-288\left(\frac{E\_{4}(4t\_{1})-1}{240}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +544∑d1=0∞[((d1)3​q1d11−q1d1−(2​d1)3​q12​d11−q12​d1)+3((d1)​q1d11−q1d1−(2​d1)​q12​d11−q12​d1)]\displaystyle+\frac{54}{4}\sum\_{d\_{1}=0}^{\infty}\Biggl[\left(\frac{(d\_{1})^{3}q\_{1}^{d\_{1}}}{1-q\_{1}^{d\_{1}}}-\frac{(2d\_{1})^{3}q\_{1}^{2d\_{1}}}{1-q\_{1}^{2d\_{1}}}\right)+3\left(\frac{(d\_{1})q\_{1}^{d\_{1}}}{1-q\_{1}^{d\_{1}}}-\frac{(2d\_{1})q\_{1}^{2d\_{1}}}{1-q\_{1}^{2d\_{1}}}\right)\Biggl] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−2732+3160​(3​E4​(t1)+16​(E4​(2​t1)−4​E4​(4​t1))−2716​(E2​(t1)−2​E2​(2​t1))CLOSE,\displaystyle=-\frac{27}{32}+\frac{3}{160}(3E\_{4}(t\_{1})+16\left(E\_{4}(2t\_{1})-4E\_{4}(4t\_{1})\right)-\frac{27}{16}\left(E\_{2}(t\_{1})-2E\_{2}(2t\_{1})\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y112\displaystyle y\_{112} | =∑d1=0∞[(d1)3​nd1,d1,0​q12​d11−q12​d1+54(d1)2​(d1+1)​q12​d1+11−q12​d1+1+54d1​(d1+1)2​q12​d1+11−q12​d1+1]\displaystyle=\sum\_{d\_{1}=0}^{\infty}\biggl[\frac{(d\_{1})^{3}n\_{d\_{1},d\_{1},0}q\_{1}^{2d\_{1}}}{1-q\_{1}^{2d\_{1}}}+54\frac{(d\_{1})^{2}(d\_{1}+1)q\_{1}^{2d\_{1}+1}}{1-q\_{1}^{2d\_{1}+1}}+54\frac{d\_{1}(d\_{1}+1)^{2}q\_{1}^{2d\_{1}+1}}{1-q\_{1}^{2d\_{1}+1}}\biggl] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =180(E4​(2​t1)−1240)−288(E4​(4​t1)−1240)+272∑d1=0∞[((2​d1+1)3​q12​d1+11−q12​d1+1−(2​d1+1)​q12​d1+11−q12​d1+1)]\displaystyle=180\left(\frac{E\_{4}(2t\_{1})-1}{240}\right)-288\left(\frac{E\_{4}(4t\_{1})-1}{240}\right)+\frac{27}{2}\sum\_{d\_{1}=0}^{\infty}\Biggl[\left(\frac{(2d\_{1}+1)^{3}q\_{1}^{2d\_{1}+1}}{1-q\_{1}^{2d\_{1}+1}}-\frac{(2d\_{1}+1)q\_{1}^{2d\_{1}+1}}{1-q\_{1}^{2d\_{1}+1}}\right)\Biggl] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =4532+3160​(3​E4​(t1)+16​(E4​(2​t1)−4​E4​(4​t1))+916​(E2​(t1)−2​E2​(2​t1))CLOSE,\displaystyle=\frac{45}{32}+\frac{3}{160}(3E\_{4}(t\_{1})+16\left(E\_{4}(2t\_{1})-4E\_{4}(4t\_{1})\right)+\frac{9}{16}\left(E\_{2}(t\_{1})-2E\_{2}(2t\_{1})\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y122\displaystyle y\_{122} | =y112,\displaystyle=y\_{112}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y222\displaystyle y\_{222} | =y111,\displaystyle=y\_{111}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | y123\displaystyle y\_{123} | =3,y233=y133=2.\displaystyle=3,\qquad y\_{233}=y\_{133}=2. |  | (3.64) |

Note that E2​(t1)−2​E2​(2​t1)E\_{2}(t\_{1})-2E\_{2}(2t\_{1}) and E4​(n​t1)E\_{4}(nt\_{1}) for n|Nn|N are modular forms of weight 2 and 4 under Γ0​(4)\Gamma\_{0}(4),
respectively. See Appendix [A](#A1 "Appendix A Γ_0⁢(𝑁) modular forms ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications"), for more details about the modular form of Γ0​(N)\Gamma\_{0}(N).
To see the modular invariance of the effective action, we move to the following basis:

|  |  |  |  |
| --- | --- | --- | --- |
|  | t:=t1−t22,s:=t1+t22,u:=2​t3+34​(t1+t2).\displaystyle t:=\frac{t^{1}-t^{2}}{2},\qquad s:=\frac{t^{1}+t^{2}}{2},\qquad u:=2t\_{3}+\frac{3}{4}(t^{1}+t^{2}). |  | (3.65) |

In this basis, the prepotential is rewritten in terms of the redefined moduli as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℱ\displaystyle{\cal F} | =−16​(−274​s3+272​s​t2−9​t2​u+3​s​u2).\displaystyle=-\frac{1}{6}\left(-\frac{27}{4}s^{3}+\frac{27}{2}st^{2}-9t^{2}u+3su^{2}\right). |  | (3.66) |

The corresponding moduli Kähler potential is given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Kks\displaystyle K\_{\rm ks} | =−ln[i2(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s)(u−\macc@depthΔ\macc@set@skewchar\macc@nested@a111u)2−9​i8(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s)3+9​i4(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s)(t−\macc@depthΔ\macc@set@skewchar\macc@nested@a111t)2−3​i2(t−\macc@depthΔ\macc@set@skewchar\macc@nested@a111t)2(u−\macc@depthΔ\macc@set@skewchar\macc@nested@a111u)].\displaystyle=-\ln\biggl[\frac{i}{2}(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})(u-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u})^{2}-\frac{9i}{8}(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})^{3}+\frac{9i}{4}(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})^{2}-\frac{3i}{2}(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})^{2}(u-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u})\biggl]. |  | (3.67) |

In an asymptotic regime qu≪qs≪qtq\_{u}\ll q\_{s}\ll q\_{t} with qt:=e2​π​i​tq\_{t}:=e^{2\pi it}, qu:=e2​π​i​uq\_{u}:=e^{2\pi iu} and qs:=e2​π​i​sq\_{s}:=e^{2\pi is},
corresponding to q3≪q1,q2q\_{3}\ll q\_{1},q\_{2} and q2→q1q\_{2}\rightarrow q\_{1},
the moduli Kähler metric is obtained as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | (Kks)s​s¯≃−1(s−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s)2,(Kks)u​u¯≃−2(u−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​u)2,(Kks)t​t¯≃−32​(s−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s)​(u−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​u),\displaystyle(K\_{\rm ks})\_{s\bar{s}}\simeq-\frac{1}{(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})^{2}},\qquad(K\_{\rm ks})\_{u\bar{u}}\simeq-\frac{2}{(u-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u})^{2}},\qquad(K\_{\rm ks})\_{t\bar{t}}\simeq-\frac{3}{2(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})(u-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u})}, |  | (3.68) |

and otherwise 0.
Thus, one can read off the matter modular weights from a ss-dependent part of the moduli Kähler metric by using Eq. ([2.1](#S2.E1 "In Kähler potential ‣ 2 Modular invariant effective action ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ks​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{s\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s}} | ∼e13​(−Kks)(Kks)s​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s∝(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s)−5/3,\displaystyle\sim e^{\frac{1}{3}(-K\_{\rm ks})}(K\_{\rm ks})\_{s\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s}}\propto(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})^{-5/3}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ku​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​u(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{u\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u}} | ∼e13​(−Kks)​(Kks)u​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​u∝(s−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s)1/3,\displaystyle\sim e^{\frac{1}{3}(-K\_{\rm ks})}(K\_{\rm ks})\_{u\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u}}\propto(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})^{1/3}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Kt​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{t\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}} | ∼e13​(−Kks)(Kks)t​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t∝(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s)−2/3.\displaystyle\sim e^{\frac{1}{3}(-K\_{\rm ks})}(K\_{\rm ks})\_{t\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}}\propto(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})^{-2/3}. |  | (3.69) |

It leads to the modular weight −53-\frac{5}{3} for As(𝟐𝟕)A^{({\bf 27})}\_{s}, 13\frac{1}{3} for Au(𝟐𝟕)A^{({\bf 27})}\_{u} and −23-\frac{2}{3} for At(𝟐𝟕)A^{({\bf 27})}\_{t}. Then, the modular weights of holomorphic Yukawa couplings are determined, and their explicit forms are rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ys​s​s\displaystyle y\_{sss} | =920E4(s)+125(E4(2s)−4E4(4s))(weight 4),\displaystyle=\frac{9}{20}E\_{4}(s)+\frac{12}{5}\left(E\_{4}(2s)-4E\_{4}(4s)\right)\quad({\rm weight}\,4), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ys​t​t\displaystyle y\_{stt} | =−92(E2(s)−2E2(2s))(weight 2),\displaystyle=-\frac{9}{2}\left(E\_{2}(s)-2E\_{2}(2s)\right)\hskip 65.0pt({\rm weight}\,2), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ys​u​u\displaystyle y\_{suu} | =1(weight 0),\displaystyle=1\hskip 165.0pt({\rm weight}\,0), |  | (3.70) |

and otherwise 0.
Note that modular forms of the weight 2 under Γ0​(4)\Gamma\_{0}(4) are given by a linear combination: E2​(s)−2​E2​(2​s)E\_{2}(s)-2E\_{2}(2s) and E2​(2​s)−2​E2​(4​s)E\_{2}(2s)-2E\_{2}(4s), as shown in Appendix [A.1](#A1.SS1 "A.1 Weight 2 ‣ Appendix A Γ_0⁢(𝑁) modular forms ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications").

To check the modular invariance of the effective action, let us consider the Γ0​(4)\Gamma\_{0}(4) modular transformation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | s→a​s+bc​s+d\displaystyle s\rightarrow\frac{as+b}{cs+d} |  | (3.71) |

with a​d−b​c=1ad-bc=1 and c≡0c\equiv 0 (mod 44), under which the Kähler potential and superpotential

|  |  |  |  |
| --- | --- | --- | --- |
|  | K\displaystyle K | =−ln[i2(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s)(u−\macc@depthΔ\macc@set@skewchar\macc@nested@a111u)2]+∑a,bKa​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​b(𝟐𝟕)Aa(𝟐𝟕)\macc@depthΔ\macc@set@skewchar\macc@nested@a111Ab(𝟐𝟕),\displaystyle=-\ln\biggl[\frac{i}{2}(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})(u-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u})^{2}\biggl]+\sum\_{a,b}K^{({\bf 27})}\_{a\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{b}}A^{({\bf 27})}\_{a}\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{A^{({\bf 27})}\_{b}}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | W\displaystyle W | =ys​s​s​As(𝟐𝟕)​As(𝟐𝟕)​As(𝟐𝟕)+ys​t​t​As(𝟐𝟕)​At(𝟐𝟕)​At(𝟐𝟕)+ys​u​u​As(𝟐𝟕)​Au(𝟐𝟕)​Au(𝟐𝟕)+yt​t​u​At(𝟐𝟕)​At(𝟐𝟕)​Au(𝟐𝟕)\displaystyle=y\_{sss}A^{({\bf 27})}\_{s}A^{({\bf 27})}\_{s}A^{({\bf 27})}\_{s}+y\_{stt}A^{({\bf 27})}\_{s}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{t}+y\_{suu}A^{({\bf 27})}\_{s}A^{({\bf 27})}\_{u}A^{({\bf 27})}\_{u}+y\_{ttu}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{u} |  | (3.72) |

transform as

|  |  |  |  |
| --- | --- | --- | --- |
|  | K→K+ln⁡|c​s+d|2,W→(c​s+d)−1​W.\displaystyle K\rightarrow K+\ln|cs+d|^{2},\qquad W\rightarrow(cs+d)^{-1}W. |  | (3.73) |

Thus, the Kähler invariant quantity eK​|W|2e^{K}|W|^{2} is modular invariant.

#### 3.3.2 Four moduli

We next discuss a CY threefold defined by a single polynomial in four projective spaces:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ℂ​ℙ1ℂ​ℙ1ℂ​ℙ1ℂ​ℙ1​[2222],\displaystyle\begin{matrix}\mathbb{CP}^{1}\\ \mathbb{CP}^{1}\\ \mathbb{CP}^{1}\\ \mathbb{CP}^{1}\\ \end{matrix}\begin{bmatrix}2\\ 2\\ 2\\ 2\\ \end{bmatrix}, |  | (3.74) |

where the number of Kähler moduli is h1,1=4h^{1,1}=4.
As studied in heterotic string theory with line bundles [[33](#bib.bib33)], the leading part of the prepotential for four Kähler moduli is calculated as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℱ\displaystyle{\cal F} | =−16​(12​t1​t2​t3+12​t1​t2​t4+12​t1​t3​t4+12​t2​t3​t4),\displaystyle=-\frac{1}{6}\left(12t\_{1}t\_{2}t\_{3}+12t\_{1}t\_{2}t\_{4}+12t\_{1}t\_{3}t\_{4}+12t\_{2}t\_{3}t\_{4}\right), |  | (3.75) |

where the triple intersection numbers are

|  |  |  |  |
| --- | --- | --- | --- |
|  | κ123=κ124=κ134=κ234=2,\displaystyle\kappa\_{123}=\kappa\_{124}=\kappa\_{134}=\kappa\_{234}=2, |  | (3.76) |

and otherwise 0. The holomorphic Yukawa couplings of matter fields are determined by the classical part and instanton
contribution:

|  |  |  |  |
| --- | --- | --- | --- |
|  | ya​b​c=κa​b​c+∑d1,d2,d3,d4=0∞ca​b​c​(d1,d2,d3,d4)​nd1,d2,d3,d4​q1d1​q2d2​q3d3​q4d41−q1d1​q2d2​q3d3​q4d4\displaystyle y\_{abc}=\kappa\_{abc}+\sum\_{d\_{1},d\_{2},d\_{3},d\_{4}=0}^{\infty}\frac{c\_{abc}(d\_{1},d\_{2},d\_{3},d\_{4})n\_{d\_{1},d\_{2},d\_{3},d\_{4}}q\_{1}^{d\_{1}}q\_{2}^{d\_{2}}q\_{3}^{d\_{3}}q\_{4}^{d\_{4}}}{1-q\_{1}^{d\_{1}}q\_{2}^{d\_{2}}q\_{3}^{d\_{3}}q\_{4}^{d\_{4}}} |  | (3.77) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | ca​b​c​(d1,d2,d3)=da​db​dc,q1=e2​π​i​t1,q2=e2​π​i​t2,q3=e2​π​i​t3,q4=e2​π​i​t4.\displaystyle c\_{abc}(d\_{1},d\_{2},d\_{3})=d\_{a}d\_{b}d\_{c},\quad q\_{1}=e^{2\pi it\_{1}},\quad q\_{2}=e^{2\pi it\_{2}},\quad q\_{3}=e^{2\pi it\_{3}},\quad q\_{4}=e^{2\pi it\_{4}}. |  | (3.78) |

To simplify our analysis, let us focus on the regime q3,q4≪q1,q2q\_{3},q\_{4}\ll q\_{1},q\_{2}; only q1,2q\_{1,2} contribute to the instanton expansion.
The nonvanishing instanton numbers nd1,d2,0,0n\_{d\_{1},d\_{2},0,0} are given in Table [6](#S3.T6 "Table 6 ‣ 3.3.2 Four moduli ‣ 3.3 Γ_0⁢(4) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications").

| d1d\_{1} ∖\setminus d2d\_{2} | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| 0 |  | 48 |  |  |  |
| 1 | 48 | 160 | 48 |  |  |
| 2 |  | 48 | 128 | 48 |  |
| 3 |  |  | 48 | 160 | 48 |
| 4 |  |  |  | 48 | 128 |

As shown in the previous example, instanton numbers have an interesting structure, i.e.,
nd1+1,d1,0,0=nd1,d1+1,0,0=48n\_{d\_{1}+1,d\_{1},0,0}=n\_{d\_{1},d\_{1}+1,0,0}=48 for all d1d\_{1}, and nd1,d1,0,0=128n\_{d\_{1},d\_{1},0,0}=128 for d1=2​ℤ+d\_{1}=2\mathbb{Z}\_{+} and otherwise 160.
In a similar manner as in Sec. [3.3.1](#S3.SS3.SSS1 "3.3.1 Three moduli ‣ 3.3 Γ_0⁢(4) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications"), we restrict ourselves to the regime t1=t2t\_{1}=t\_{2} in which nonvanishing holomorphic Yukawa couplings are described by

|  |  |  |  |
| --- | --- | --- | --- |
|  | y111\displaystyle y\_{111} | =∑d1=0∞[(d1)3​nd1,d1,0,0​q12​d11−q12​d1+48(d1)3​q12​d1+11−q12​d1+1+48(d1+1)3​q12​d1+11−q12​d1+1]\displaystyle=\sum\_{d\_{1}=0}^{\infty}\biggl[\frac{(d\_{1})^{3}n\_{d\_{1},d\_{1},0,0}q\_{1}^{2d\_{1}}}{1-q\_{1}^{2d\_{1}}}+48\frac{(d\_{1})^{3}q\_{1}^{2d\_{1}+1}}{1-q\_{1}^{2d\_{1}+1}}+48\frac{(d\_{1}+1)^{3}q\_{1}^{2d\_{1}+1}}{1-q\_{1}^{2d\_{1}+1}}\biggl] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =∑d1=0∞[160(d1)3​q12​d11−q12​d1−32(2​d1)3​q12​(2​d1)1−q12​(2​d1)+484((2​d1+1)3​q12​d1+11−q12​d1+1+3(2​d1+1)​q12​d1+11−q12​d1+1)]\displaystyle=\sum\_{d\_{1}=0}^{\infty}\biggl[160\frac{(d\_{1})^{3}q\_{1}^{2d\_{1}}}{1-q\_{1}^{2d\_{1}}}-32\frac{(2d\_{1})^{3}q\_{1}^{2(2d\_{1})}}{1-q\_{1}^{2(2d\_{1})}}+\frac{48}{4}\left(\frac{(2d\_{1}+1)^{3}q\_{1}^{2d\_{1}+1}}{1-q\_{1}^{2d\_{1}+1}}+3\frac{(2d\_{1}+1)q\_{1}^{2d\_{1}+1}}{1-q\_{1}^{2d\_{1}+1}}\right)\biggl] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =160​(E4​(2​t1)−1240)−256​(E4​(4​t1)−1240)\displaystyle=160\left(\frac{E\_{4}(2t\_{1})-1}{240}\right)-256\left(\frac{E\_{4}(4t\_{1})-1}{240}\right) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | +484∑d1=0∞[((d1)3​q1d11−q1d1−(2​d1)3​q12​d11−q12​d1)+3((d1)​q1d11−q1d1−(2​d1)​q12​d11−q12​d1)]\displaystyle+\frac{48}{4}\sum\_{d\_{1}=0}^{\infty}\Biggl[\left(\frac{(d\_{1})^{3}q\_{1}^{d\_{1}}}{1-q\_{1}^{d\_{1}}}-\frac{(2d\_{1})^{3}q\_{1}^{2d\_{1}}}{1-q\_{1}^{2d\_{1}}}\right)+3\left(\frac{(d\_{1})q\_{1}^{d\_{1}}}{1-q\_{1}^{d\_{1}}}-\frac{(2d\_{1})q\_{1}^{2d\_{1}}}{1-q\_{1}^{2d\_{1}}}\right)\Biggl] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =−34+160​(3​E4​(t1)+16​(E4​(2​t1)−4​E4​(4​t1))−32​(E2​(t1)−2​E2​(2​t1))CLOSE,\displaystyle=-\frac{3}{4}+\frac{1}{60}(3E\_{4}(t\_{1})+16\left(E\_{4}(2t\_{1})-4E\_{4}(4t\_{1})\right)-\frac{3}{2}\left(E\_{2}(t\_{1})-2E\_{2}(2t\_{1})\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y112\displaystyle y\_{112} | =∑d1=0∞[(d1)3​nd1,d1,0​q12​d11−q12​d1+54(d1)2​(d1+1)​q12​d1+11−q12​d1+1+54d1​(d1+1)2​q12​d1+11−q12​d1+1]\displaystyle=\sum\_{d\_{1}=0}^{\infty}\biggl[\frac{(d\_{1})^{3}n\_{d\_{1},d\_{1},0}q\_{1}^{2d\_{1}}}{1-q\_{1}^{2d\_{1}}}+54\frac{(d\_{1})^{2}(d\_{1}+1)q\_{1}^{2d\_{1}+1}}{1-q\_{1}^{2d\_{1}+1}}+54\frac{d\_{1}(d\_{1}+1)^{2}q\_{1}^{2d\_{1}+1}}{1-q\_{1}^{2d\_{1}+1}}\biggl] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =160(E4​(2​t1)−1240)−256(E4​(4​t1)−1240)+12∑d1=0∞[((2​d1+1)3​q12​d1+11−q12​d1+1−(2​d1+1)​q12​d1+11−q12​d1+1)]\displaystyle=160\left(\frac{E\_{4}(2t\_{1})-1}{240}\right)-256\left(\frac{E\_{4}(4t\_{1})-1}{240}\right)+12\sum\_{d\_{1}=0}^{\infty}\Biggl[\left(\frac{(2d\_{1}+1)^{3}q\_{1}^{2d\_{1}+1}}{1-q\_{1}^{2d\_{1}+1}}-\frac{(2d\_{1}+1)q\_{1}^{2d\_{1}+1}}{1-q\_{1}^{2d\_{1}+1}}\right)\Biggl] |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =54+160​(3​E4​(t1)+16​(E4​(2​t1)−4​E4​(4​t1))+12​(E2​(t1)−2​E2​(2​t1))CLOSE,\displaystyle=\frac{5}{4}+\frac{1}{60}(3E\_{4}(t\_{1})+16\left(E\_{4}(2t\_{1})-4E\_{4}(4t\_{1})\right)+\frac{1}{2}\left(E\_{2}(t\_{1})-2E\_{2}(2t\_{1})\right), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y122\displaystyle y\_{122} | =y112,\displaystyle=y\_{112}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | y222\displaystyle y\_{222} | =y111,\displaystyle=y\_{111}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | y123\displaystyle y\_{123} | =y124=y133=y234=2.\displaystyle=y\_{124}=y\_{133}=y\_{234}=2. |  | (3.79) |

Note that E2​(t1)−2​E2​(2​t1)E\_{2}(t\_{1})-2E\_{2}(2t\_{1}) and E4​(n​t1)E\_{4}(nt\_{1}) for n|Nn|N are modular forms of weight 2 and 4 under Γ0​(4)\Gamma\_{0}(4),
respectively.
To see the modular invariance of the effective action, we move to the following basis:

|  |  |  |  |
| --- | --- | --- | --- |
|  | t:=t1−t22,s:=t1+t22,u:=t3+14​(t1+t2),r:=t4+14​(t1+t2).\displaystyle t:=\frac{t^{1}-t^{2}}{2},\qquad s:=\frac{t^{1}+t^{2}}{2},\qquad u:=t\_{3}+\frac{1}{4}(t^{1}+t^{2}),\qquad r:=t\_{4}+\frac{1}{4}(t^{1}+t^{2}). |  | (3.80) |

In this basis, the prepotential is rewritten in terms of the redefined moduli as

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ℱ\displaystyle{\cal F} | =−16​(24​s​u​r−6​s3−12​t2​u−12​t2​r+12​t2​s).\displaystyle=-\frac{1}{6}\left(24sur-6s^{3}-12t^{2}u-12t^{2}r+12t^{2}s\right). |  | (3.81) |

The corresponding moduli Kähler potential is approximately given by

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Kks\displaystyle K\_{\rm ks} | =−ln[i{4(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s)(u−\macc@depthΔ\macc@set@skewchar\macc@nested@a111u)(r−\macc@depthΔ\macc@set@skewchar\macc@nested@a111r)−(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s)3−2(t−\macc@depthΔ\macc@set@skewchar\macc@nested@a111t)2((r−\macc@depthΔ\macc@set@skewchar\macc@nested@a111r)+(t−\macc@depthΔ\macc@set@skewchar\macc@nested@a111t))−(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s)}].\displaystyle=-\ln\biggl[i\left\{4(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})(u-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u})(r-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{r})-(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})^{3}-2(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})^{2}\left((r-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{r})+(t-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t})\right)-(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})\right\}\biggl]. |  | (3.82) |

Note that we consider an asymptotic regime q3,q4≪q1,q2q\_{3},q\_{4}\ll q\_{1},q\_{2} with q1=q2q\_{1}=q\_{2},
corresponding to qu,qr≪qs≪qtq\_{u},q\_{r}\ll q\_{s}\ll q\_{t} with qt:=e2​π​i​t=1q\_{t}:=e^{2\pi it}=1, qs:=e2​π​i​sq\_{s}:=e^{2\pi is}, qu:=e2​π​i​uq\_{u}:=e^{2\pi iu} and qr:=e2​π​i​rq\_{r}:=e^{2\pi ir},
the corresponding moduli Kähler metric is found as

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | (Kks)s​s¯≃−1(s−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s)2,(Kks)t​t¯≃−1(s−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s)​(1u−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​u+1r−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​r),\displaystyle(K\_{\rm ks})\_{s\bar{s}}\simeq-\frac{1}{(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})^{2}},\qquad(K\_{\rm ks})\_{t\bar{t}}\simeq-\frac{1}{(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})}\left(\frac{1}{u-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u}}+\frac{1}{r-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{r}}\right), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | (Kks)u​u¯≃−1(u−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​u)2,(Kks)r​r¯≃−1(r−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​r)2,\displaystyle(K\_{\rm ks})\_{u\bar{u}}\simeq-\frac{1}{(u-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u})^{2}},\qquad(K\_{\rm ks})\_{r\bar{r}}\simeq-\frac{1}{(r-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{r})^{2}}, |  | (3.83) |

and otherwise 0.
Thus, one can read off the matter modular weights from a ss-dependent part of the moduli Kähler metric by using Eq. ([2.1](#S2.E1 "In Kähler potential ‣ 2 Modular invariant effective action ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications")),

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ks​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{s\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s}} | ∼e13​(−Kks)(Kks)s​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s∝(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s)−5/3,\displaystyle\sim e^{\frac{1}{3}(-K\_{\rm ks})}(K\_{\rm ks})\_{s\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s}}\propto(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})^{-5/3}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Kt​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{t\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}} | ∼e13​(−Kks)(Kks)t​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​t∝(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s)−2/3,\displaystyle\sim e^{\frac{1}{3}(-K\_{\rm ks})}(K\_{\rm ks})\_{t\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{t}}\propto(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})^{-2/3}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | Ku​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​u(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{u\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u}} | ∼e13​(−Kks)​(Kks)u​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​u∝(s−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s)1/3,\displaystyle\sim e^{\frac{1}{3}(-K\_{\rm ks})}(K\_{\rm ks})\_{u\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u}}\propto(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})^{1/3}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | Kr​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​r(𝟐𝟕)\displaystyle K^{({\bf 27})}\_{r\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{r}} | ∼e13​(−Kks)​(Kks)r​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​r∝(s−\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​s)1/3.\displaystyle\sim e^{\frac{1}{3}(-K\_{\rm ks})}(K\_{\rm ks})\_{r\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{r}}\propto(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})^{1/3}. |  | (3.84) |

It leads to the modular weight −53-\frac{5}{3} for As(𝟐𝟕)A^{({\bf 27})}\_{s}, −23-\frac{2}{3} for At(𝟐𝟕)A^{({\bf 27})}\_{t}, and 13\frac{1}{3} for Au(𝟐𝟕)A^{({\bf 27})}\_{u} and Ar(𝟐𝟕)A^{({\bf 27})}\_{r}. Then, the modular weights of holomorphic Yukawa couplings are determined, and their explicit forms are rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | ys​s​s\displaystyle y\_{sss} | =615E4(s)+3215(E4(2s)−4E4(4s))(weight 4),\displaystyle=\frac{6}{15}E\_{4}(s)+\frac{32}{15}\left(E\_{4}(2s)-4E\_{4}(4s)\right)\quad({\rm weight}\,4), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | ys​t​t\displaystyle y\_{stt} | =−4(E2(s)−2E2(2s))(weight 2),\displaystyle=-4\left(E\_{2}(s)-2E\_{2}(2s)\right)\hskip 69.0pt({\rm weight}\,2), |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | yt​t​u\displaystyle y\_{ttu} | =yt​t​r=−4(weight 0),\displaystyle=y\_{ttr}=-4\hskip 127.0pt({\rm weight}\,0), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | ys​u​r\displaystyle y\_{sur} | =4(weight 0),\displaystyle=4\hskip 165.0pt({\rm weight}\,0), |  | (3.85) |

and otherwise 0. Note that modular forms of the weight 2 under Γ0​(4)\Gamma\_{0}(4) are given by a linear combination: E2​(s)−2​E2​(2​s)E\_{2}(s)-2E\_{2}(2s) and E2​(2​s)−2​E2​(4​s)E\_{2}(2s)-2E\_{2}(4s), as shown in Appendix [A.1](#A1.SS1 "A.1 Weight 2 ‣ Appendix A Γ_0⁢(𝑁) modular forms ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications").

To check the modular invariance of the effective action, let us consider the Γ0​(4)\Gamma\_{0}(4) modular transformation:

|  |  |  |  |
| --- | --- | --- | --- |
|  | s→a​s+bc​s+d\displaystyle s\rightarrow\frac{as+b}{cs+d} |  | (3.86) |

with a​d−b​c=1ad-bc=1 and c≡0c\equiv 0 (mod 44), under which the Kähler potential and superpotential

|  |  |  |  |
| --- | --- | --- | --- |
|  | K\displaystyle K | =−ln[4i(s−\macc@depthΔ\macc@set@skewchar\macc@nested@a111s)(u−\macc@depthΔ\macc@set@skewchar\macc@nested@a111u)(r−\macc@depthΔ\macc@set@skewchar\macc@nested@a111r)]+∑a,bKa​\macc@depth​Δ​\macc@set@skewchar​\macc@nested@a​111​b(𝟐𝟕)Aa(𝟐𝟕)\macc@depthΔ\macc@set@skewchar\macc@nested@a111Ab(𝟐𝟕),\displaystyle=-\ln\biggl[4i(s-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{s})(u-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{u})(r-\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{r})\biggl]+\sum\_{a,b}K^{({\bf 27})}\_{a\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{b}}A^{({\bf 27})}\_{a}\macc@depth\char 1\relax\macc@set@skewchar\macc@nested@a 111{A^{({\bf 27})}\_{b}}, |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  | W\displaystyle W | =ys​s​s​As(𝟐𝟕)​As(𝟐𝟕)​As(𝟐𝟕)+ys​t​t​As(𝟐𝟕)​At(𝟐𝟕)​At(𝟐𝟕)\displaystyle=y\_{sss}A^{({\bf 27})}\_{s}A^{({\bf 27})}\_{s}A^{({\bf 27})}\_{s}+y\_{stt}A^{({\bf 27})}\_{s}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{t} |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | +ys​u​r​As(𝟐𝟕)​Au(𝟐𝟕)​Ar(𝟐𝟕)+yt​t​r​At(𝟐𝟕)​At(𝟐𝟕)​Ar(𝟐𝟕)+yt​t​u​At(𝟐𝟕)​At(𝟐𝟕)​Au(𝟐𝟕)\displaystyle+y\_{sur}A^{({\bf 27})}\_{s}A^{({\bf 27})}\_{u}A^{({\bf 27})}\_{r}+y\_{ttr}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{r}+y\_{ttu}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{t}A^{({\bf 27})}\_{u} |  | (3.87) |

transform as

|  |  |  |  |
| --- | --- | --- | --- |
|  | K→K+ln⁡|c​s+d|2,W→(c​s+d)−1​W.\displaystyle K\rightarrow K+\ln|cs+d|^{2},\qquad W\rightarrow(cs+d)^{-1}W. |  | (3.88) |

Thus, the Kähler invariant quantity eK​|W|2e^{K}|W|^{2} is modular invariant.

Note that the 4D low-energy effective theory has the permutation symmetry between
Ar(𝟐𝟕)A^{({\bf 27})}\_{r} and Au(𝟐𝟕)A^{({\bf 27})}\_{u}.
Such a Z2Z\_{2} permutation symmetry is originated from S​p​(10,ℤ)Sp(10,\mathbb{Z}).

## 4 Hierarchical structure of physical Yukawa couplings

In this section, we discuss the flavor structure of physical Yukawa couplings in more details.
Specifically, we focus on the CY threefold in Sec. [3.1.2](#S3.SS1.SSS2 "3.1.2 Three moduli ‣ 3.1 𝑆⁢𝐿⁢(2,ℤ) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications").

To see the flavor structure of 𝟐𝟕{\bf 27} matters, let us consider the physical Yukawa couplings
by diagonalizing the kinetic terms of 𝟐𝟕{\bf 27} matter fields:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Aa​Ka​b¯(𝟐𝟕)​A¯b¯=Aa​(L†)ac^¯​Λc^¯​c^​Lb¯c^​A¯b¯=:𝒜a^​𝒜¯a^¯\displaystyle A^{a}K\_{a\bar{b}}^{({\bf 27})}\bar{A}^{\bar{b}}=A^{a}(L^{\dagger})^{\bar{\hat{c}}}\_{a}\Lambda\_{\bar{\hat{c}}\hat{c}}L^{\hat{c}}\_{\bar{b}}\bar{A}^{\bar{b}}=:{\cal A}^{\hat{a}}\bar{{\cal A}}^{\bar{\hat{a}}} |  | (4.1) |

with

|  |  |  |  |
| --- | --- | --- | --- |
|  | 𝒜a^=Ad​(L†)da^¯​(Λ)a^¯​a^,\displaystyle{\cal A}^{\hat{a}}=A^{d}(L^{\dagger})^{\bar{\hat{a}}}\_{d}(\sqrt{\Lambda})\_{\bar{\hat{a}}\hat{a}}, |  | (4.2) |

where Lb¯c^L^{\hat{c}}\_{\bar{b}} is an unitary matrix to diagonalize the matter field Kähler metric Ka​b¯(𝟐𝟕)K\_{a\bar{b}}^{({\bf 27})}, and Λa^¯​a^\Lambda\_{\bar{\hat{a}}\hat{a}} denotes its eigenvalue matrix, that is,
(L​K​L†)a^¯​a^=Λa^¯​a^(LKL^{\dagger})\_{\bar{\hat{a}}\hat{a}}=\Lambda\_{\bar{\hat{a}}\hat{a}}.
Then, the physical Yukawa couplings are expressed by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Ya^​b^​c^=eK/2(Λ−1/2L)a^d(Λ−1/2L)b^e(Λ−1/2L)c^fyd​e​f,\displaystyle Y\_{\hat{a}\hat{b}\hat{c}}=e^{K/2}(\Lambda^{-1/2}L)^{d}\_{\hat{a}}(\Lambda^{-1/2}L)^{e}\_{\hat{b}}(\Lambda^{-1/2}L)^{f}\_{\hat{c}}y\_{def}, |  | (4.3) |

where we use

|  |  |  |  |
| --- | --- | --- | --- |
|  | eK/2yd​e​fAdAeAf=eK/2yd​e​f(Λ−1/2L)a^d(Λ−1/2L)b^e(Λ−1/2L)c^f𝒜a^𝒜b^𝒜c^=Ya^​b^​c^𝒜a^𝒜b^𝒜c^.\displaystyle e^{K/2}y\_{def}A^{d}A^{e}A^{f}=e^{K/2}y\_{def}(\Lambda^{-1/2}L)^{d}\_{\hat{a}}(\Lambda^{-1/2}L)^{e}\_{\hat{b}}(\Lambda^{-1/2}L)^{f}\_{\hat{c}}{\cal A}^{\hat{a}}{\cal A}^{\hat{b}}{\cal A}^{\hat{c}}=Y\_{\hat{a}\hat{b}\hat{c}}{\cal A}^{\hat{a}}{\cal A}^{\hat{b}}{\cal A}^{\hat{c}}. |  | (4.4) |

We can estimate the physical Yukawa couplings in the regime Im⁡(t1)≪Im⁡(t2)=Im⁡(t3){\rm Im}(t\_{1})\ll{\rm Im}(t\_{2})={\rm Im}(t\_{3}) by
using the nonvanishing holomorphic Yukawa couplings ([3.22](#S3.E22 "In 3.1.2 Three moduli ‣ 3.1 𝑆⁢𝐿⁢(2,ℤ) modular forms ‣ 3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications")) and the matter field Kähler metric:

|  |  |  |  |
| --- | --- | --- | --- |
|  | (K1​1¯K1​2¯K1​3¯K2​1¯K2​2¯K2​3¯K3​1¯K3​2¯K3​3¯)=eKcs32​(Im​(t3)2/3Im​(t1)5/3Im​(t1)1/3Im​(t3)4/3Im​(t1)1/3Im​(t3)4/3Im​(t1)1/3Im​(t3)4/3Im​(t1)1/3Im​(t3)4/30Im​(t1)1/3Im​(t3)4/30Im​(t1)1/3Im​(t3)4/3).\displaystyle\begin{pmatrix}K\_{1\bar{1}}&K\_{1\bar{2}}&K\_{1\bar{3}}\\ K\_{2\bar{1}}&K\_{2\bar{2}}&K\_{2\bar{3}}\\ K\_{3\bar{1}}&K\_{3\bar{2}}&K\_{3\bar{3}}\end{pmatrix}=\frac{e^{\frac{K\_{\rm cs}}{3}}}{2}\begin{pmatrix}\frac{{\rm Im}(t\_{3})^{2/3}}{{\rm Im}(t\_{1})^{5/3}}&\frac{{\rm Im}(t\_{1})^{1/3}}{{\rm Im}(t\_{3})^{4/3}}&\frac{{\rm Im}(t\_{1})^{1/3}}{{\rm Im}(t\_{3})^{4/3}}\\ \frac{{\rm Im}(t\_{1})^{1/3}}{{\rm Im}(t\_{3})^{4/3}}&\frac{{\rm Im}(t\_{1})^{1/3}}{{\rm Im}(t\_{3})^{4/3}}&0\\ \frac{{\rm Im}(t\_{1})^{1/3}}{{\rm Im}(t\_{3})^{4/3}}&0&\frac{{\rm Im}(t\_{1})^{1/3}}{{\rm Im}(t\_{3})^{4/3}}\\ \end{pmatrix}. |  | (4.5) |

Since the eigenvalues of the matter field Kähler metric

|  |  |  |  |
| --- | --- | --- | --- |
|  | Λc^¯​c^=eKcs32​diag​(Im​(t1)1/3Im​(t3)4/3,Im​(t1)1/3Im​(t3)4/3,Im​(t3)2/3Im​(t1)5/3)\displaystyle\Lambda\_{\bar{\hat{c}}\hat{c}}=\frac{e^{\frac{K\_{\rm cs}}{3}}}{2}{\rm diag}\left(\frac{{\rm Im}(t\_{1})^{1/3}}{{\rm Im}(t\_{3})^{4/3}},\,\,\frac{{\rm Im}(t\_{1})^{1/3}}{{\rm Im}(t\_{3})^{4/3}},\,\,\frac{{\rm Im}(t\_{3})^{2/3}}{{\rm Im}(t\_{1})^{5/3}}\right) |  | (4.6) |

are hierarchical in the regime Im⁡(t1)≪Im⁡(t3){\rm Im}(t\_{1})\ll{\rm Im}(t\_{3}), it will be accessible to the hierarchical physical Yukawa couplings from the hierarchical structure of matter field Kähler metric [[34](#bib.bib34)].
Such a hierarchical structure arises from the coexistence of both the positive and negative modular weights for matter fields.
Indeed, if the matter fields share the same modular weights, the matter field Kähler metric takes a moduli-independent form whose
value is of 𝒪⁡(1){\cal O}(1). See, Ref. [[35](#bib.bib35)], for a theoretical study about a lepton model building by utilizing the positive and negative modular weights.

Let us study the flavor structure of matter fields.
For simplicity, suppose that the Higgs field belongs to 𝒜3^{\cal A}^{\hat{3}}, and three generations of
quarks and leptons are originated from the elements of {𝒜1^,𝒜2^,𝒜3^}\{{\cal A}^{\hat{1}},{\cal A}^{\hat{2}},{\cal A}^{\hat{3}}\}.
In this case, the eigenvalues of physical Yukawa couplings Y3^​a^​b^Y\_{\hat{3}\hat{a}\hat{b}} are found as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Eigen⁡(Y3^​a^​b^)=2​d​i​a​g​(−(Im⁡(t3)Im⁡(t1))2,(3+E4​(t1))​(Im⁡(t3)Im⁡(t1))4,−1+E4​(t1)3+E4​(t1)​(Im⁡(t3)Im⁡(t1))2),\displaystyle{\rm Eigen}(Y\_{\hat{3}\hat{a}\hat{b}})=2{\rm diag}\left(-\left(\frac{{\rm Im}(t\_{3})}{{\rm Im}(t\_{1})}\right)^{2},\,\,(3+E\_{4}(t\_{1}))\left(\frac{{\rm Im}(t\_{3})}{{\rm Im}(t\_{1})}\right)^{4},\,\,\frac{-1+E\_{4}(t\_{1})}{3+E\_{4}(t\_{1})}\left(\frac{{\rm Im}(t\_{3})}{{\rm Im}(t\_{1})}\right)^{2}\right), |  | (4.7) |

up to the contribution from the complex structure moduli.
By using the explicit form of the Eisenstein function, the ratios of these eigenvalues r1r\_{1} and r2r\_{2} are
evaluated as

|  |  |  |  |
| --- | --- | --- | --- |
|  | r1\displaystyle r\_{1} | ≃−14​(Im⁡(t1)Im⁡(t3))2,\displaystyle\simeq-\frac{1}{4}\left(\frac{{\rm Im}(t\_{1})}{{\rm Im}(t\_{3})}\right)^{2}, |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  | r2\displaystyle r\_{2} | ≃15​(Im⁡(t1)Im⁡(t3))2​∑k=0∞k3​qk1−qk.\displaystyle\simeq 15\left(\frac{{\rm Im}(t\_{1})}{{\rm Im}(t\_{3})}\right)^{2}\sum\_{k=0}^{\infty}\frac{k^{3}q^{k}}{1-q^{k}}. |  | (4.8) |

Thus, we can obtain the hierarchical physical Yukawa couplings due to the instanton effects as well as the hierarchical moduli values Im⁡(t1)≪Im⁡(t3){\rm Im}(t\_{1})\ll{\rm Im}(t\_{3}). In this region, the determinant of physical Yukawa couplings is also proportional to qq-expansion ∑k=0∞k3​qk1−qk\sum\_{k=0}^{\infty}\frac{k^{3}q^{k}}{1-q^{k}}.
Since the axion Re⁡(t1){\rm Re}(t\_{1}) controls the size of CP violation, it would be accessible to the small value of Jarlskog invariant, which is beyond the scope of this paper and will be the subject of future investigation.

Just for simple illustration, we have assumed that the Higgs field belongs to 𝒜3^{\cal A}^{\hat{3}}.
In general, the Higgs fields may correspond to linear combinations of {𝒜1^,𝒜2^,𝒜3^}\{{\cal A}^{\hat{1}},{\cal A}^{\hat{2}},{\cal A}^{\hat{3}}\}, and coefficients of linear combinations
may be different between the up and down sectors of the Higgs fields.
That may lead to more realistic mass matrices including mixing angles.
At any rate, a direction of light Higgs pair is fixed by mass terms of the Higgs sector,
which may be generated by vacuum expectation values of singlets and/or non-perturbative effects.
Such a study is beyond our scope, but it would be interesting to study it in
realistic CY compactifications in future.

## 5 Conclusions and discussions

In this paper, we studied heterotic string theory with standard embedding
from the viewpoint of the modular symmetry.
We found that the 4D low-energy effective action is controlled by
the S​L​(2,ℤ)SL(2,\mathbb{Z}) and its subgroups in the asymptotic regions
of Calabi-Yau moduli space.
In asymptotic limits, the holomorphic Yukawa couplings are described by
holomorphic modular forms, as shown in Sec. [3](#S3 "3 Holomorphic Yukawa couplings ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications").
To extract a modular form, we focused on a novel structure
of instanton numbers, e.g., the same instanton number for a particular modulus
for the S​L​(2,ℤ)SL(2,\mathbb{Z}) modular form.
In the orbifold limit of the moduli space, the moduli are decomposed to
untwisted moduli and twisted ones.
Among the full S​p​(2​h+2,ℤ)Sp(2h+2,\mathbb{Z}) symmetry, only the modular symmetries
corresponding to the untwisted (bulk) moduli become manifest, although some symmetries such as permutation symmetries of twisted moduli remain among
the S​p​(2​h+2,ℤ)Sp(2h+2,\mathbb{Z}) modular symmetry.
The regime of the moduli space, which we studied in this paper, may be another
limit, where some subgroups of the S​p​(2​h+2,ℤ)Sp(2h+2,\mathbb{Z}) modular symmetry
become manifest.

We also evaluated the physical Yukawa couplings of matter fields in a specific
CY compactification.
So far, it was pointed out in Refs. [[36](#bib.bib36), [34](#bib.bib34)] that the matter field Kähler metric plays
an important role in understanding a hierarchical structure of physical Yukawa couplings.
We found the coexistence of both the positive and negative modular weights for matter fields.
Such a sign difference of the modular weights leads to the hierarchical structure of matter field Kähler metric.
It was also argued in Ref. [[35](#bib.bib35)] that the coexistence of both the positive and negative modular weights
for matter fields provides a new direction for lepton model building.
Our finding results reproduce these observations.
Furthermore, we showed that the instanton corrections also give rise to
a hierarchical structure thanks to the nature of modular forms.77
7
Such an exponential suppression was also seen in holomorphic Yukawa couplings of twisted modes in heterotic orbifold models [[37](#bib.bib37), [38](#bib.bib38), [39](#bib.bib39)].

In this paper, we examined the holomorphic Yukawa couplings in the 4D low-energy effective action,
and they transform under the modular symmetry.
However, there are several unsolved problems:

The origin of Γ0​(N)\Gamma\_{0}(N) structure

We have seen the non-trivial structure of instanton numbers, determining the remaining modular symmetry in the low-energy
effective action. However, our analysis was constrained as a limited class of CY threefolds.
It would be important to perform a comprehensive study about the modular symmetry in the asymptotic region of CY moduli space.
It will provide a better understanding of Γ0​(N)\Gamma\_{0}(N) symmetry for underlying CY threefolds.88
8
Similar subgroups Γ0​(N)\Gamma\_{0}(N) were found in specific orbifold limits [[40](#bib.bib40), [41](#bib.bib41)].
In the bottom-up approach, moduli-dependent Yukawa couplings was widely used in the so-called
modular flavor models.
(See Refs. [[42](#bib.bib42), [43](#bib.bib43)] and references therein.)
It would also be fascinating to apply our finding Γ0​(N)\Gamma\_{0}(N) structure to
the flavor structure of matter fields. We hope to report on this bottom-up direction in the future.

Stringy selection rule

The 4D low-energy effective field theory derived in this paper seems to have additional coupling selection rules.
Some of them can be originated from the original S​p​(2​h+2,ℤ)Sp(2h+2,\mathbb{Z}) symplectic modular symmetry.
Also, the doublet structure was found.
It would be important to study more on stringy selection rules.

Siegel modular forms

We have studied the regime, where instanton effects of a single modulus are finite, but
the other vanish.
In this regime, S​L​(2,ℤ)SL(2,\mathbb{Z}) or its subgroup becomes manifest and their
modular forms appear.
CY threefolds have larger S​p​(2​h+2,ℤ)Sp(2h+2,\mathbb{Z}) modular symmetry and many moduli.
It would be interesting to study modular symmetries larger than S​L​(2,ℤ)SL(2,\mathbb{Z}) including
multi-moduli and their Siegel modular forms.99
9
Some Siegel forms were studied
explicitly in magnetized D-brane models on T6T^{6} compactification [[44](#bib.bib44)]. See also for heterotic orbifold models Refs. [[45](#bib.bib45), [46](#bib.bib46)].
We would study it elsewhere.

The modular symmetry controls not only 3-point couplings of matter fields, but
also higher order couplings [[47](#bib.bib47), [48](#bib.bib48)].
Furthermore, the gauge threshold corrections are constrained by the modular symmetry anomalies [[49](#bib.bib49)], although explicit calculations were done in heterotic orbifold models [[50](#bib.bib50)].
Moreover, moduli-dependence of the species scale was also constrained by
the modular symmetry [[51](#bib.bib51), [52](#bib.bib52)].
The modular symmetry is relevant to other aspects.
Hence, the modular symmetry is quite important in most of aspects
of 4D low-energy effective field theory derived from string theory.
Our analysis has opened various interesting directions to study the modular symmetry
in CY compactifications.

###### Acknowledgements.

## Appendix A Γ0​(N)\Gamma\_{0}(N) modular forms

In this Appendix, we briefly summarize the modular forms of Γ0​(N)\Gamma\_{0}(N) rather than S​L​(2,ℤ)SL(2,\mathbb{Z}).
For more details, see, e.g., Ref. [[53](#bib.bib53)].
As discussed before, Γ0​(3)\Gamma\_{0}(3) modular forms can be realized on specific CY threefolds.
Γ0​(N)\Gamma\_{0}(N) is a congruence subgroup of level NN, which is defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Γ0(N)={(abcd),c≡0(modN)}.\displaystyle\Gamma\_{0}(N)=\left\{\begin{pmatrix}a&b\\ c&d\\ \end{pmatrix},\quad c\equiv 0\,({\rm mod}\,N)\,\right\}. |  | (A.1) |

Before discussing the modular form of Γ0​(N)\Gamma\_{0}(N), let us remark the modular forms of S​L​(2,ℤ)SL(2,\mathbb{Z}).
It was known that the Eisenstein series EkE\_{k} for k≥4k\geq 4 are holomorphic modular forms of weight kk,
but there are no holomorphic modular forms of weight 2. The Eisenstein series E2E\_{2} is a holomorphic function, but not a modular form.1010
10
A non-holomorphic but modular function of weight 2 is given by E2∗​(τ):=E2​(τ)−3π​Im​(τ)E\_{2}^{\ast}(\tau):=E\_{2}(\tau)-\frac{3}{\pi{\rm Im}(\tau)} introduced by Siegel.
Indeed, the modular transformation of E2E\_{2} is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | E2​(γ​τ)=(c​τ+d)2​E2​(τ)+122​π​i​c​(c​τ+d)\displaystyle E\_{2}(\gamma\tau)=(c\tau+d)^{2}E\_{2}(\tau)+\frac{12}{2\pi i}c(c\tau+d) |  | (A.2) |

with γ\gamma being the element of S​L​(2,ℤ)SL(2,\mathbb{Z}).
Note that a modular covariant differential operator DkD\_{k} acting on modular forms of weight kk is
defined as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Dk=12​π​i​dd​τ−k12​E2​(τ),\displaystyle D\_{k}=\frac{1}{2\pi i}\frac{d}{d\tau}-\frac{k}{12}E\_{2}(\tau), |  | (A.3) |

which maps a modular form of weight kk to a modular form of weight k+2k+2.
Thus, E2​(τ)E\_{2}(\tau) is regarded as a modular connection rather than a modular form, and it can be rewritten as

|  |  |  |  |
| --- | --- | --- | --- |
|  | E2​(τ)=12​π​i​∂τln⁡Δ⁡(τ)\displaystyle E\_{2}(\tau)=\frac{1}{2\pi i}\partial\_{\tau}\ln\Delta(\tau) |  | (A.4) |

where Δ\Delta is a weight 12 modular (cusp) form of S​L​(2,ℤ)SL(2,\mathbb{Z}).
Specifically, Δ\Delta is the discriminant of Weierstrass equation, which is
defined by using the Dedekind η\eta-function:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ⁡(τ)=(2​π)12​η​(τ)24.\displaystyle\Delta(\tau)=(2\pi)^{12}\eta(\tau)^{24}. |  | (A.5) |

This modular function Δ\Delta is convenient to define the holomorphic Eisenstein series for Γ0​(N)\Gamma\_{0}(N).

Let us consider the following modular transformation of Γ0​(N)\Gamma\_{0}(N):

|  |  |  |  |
| --- | --- | --- | --- |
|  | τ→τ′=τN​τ+1\displaystyle\tau\rightarrow\tau^{\prime}=\frac{\tau}{N\tau+1} |  | (A.6) |

under which Δ⁡(n​τ)\Delta(n\tau) with n∈ℕn\in\mathbb{N} transforms as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ⁡(n​τ)→Δ⁡(n​τ′)=(−N​τ+1n​τ)12​Δ​(−Nn−1n​τ).\displaystyle\Delta(n\tau)\rightarrow\Delta(n\tau^{\prime})=\left(-\frac{N\tau+1}{n\tau}\right)^{12}\Delta\left(-\frac{N}{n}-\frac{1}{n\tau}\right). |  | (A.7) |

Recalling that the modular transformation of Δ⁡(τ)\Delta(\tau) is given by

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ⁡(τ)→Δ⁡(γ​τ)=(c​τ+d)12​Δ​(τ),\displaystyle\Delta(\tau)\rightarrow\Delta(\gamma\tau)=(c\tau+d)^{12}\Delta(\tau), |  | (A.8) |

Eq. ([A.7](#A1.E7 "In Appendix A Γ_0⁢(𝑁) modular forms ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications")) is simplified as

|  |  |  |  |
| --- | --- | --- | --- |
|  | Δ⁡(n​τ′)=(N​τ+1)12​Δ​(n​τ),\displaystyle\Delta(n\tau^{\prime})=(N\tau+1)^{12}\Delta(n\tau), |  | (A.9) |

for n|Nn|N. It indicates that Δ⁡(n​τ)\Delta(n\tau) with n|Nn|N is regarded as a weight 12 modular form of Γ0​(N)\Gamma\_{0}(N).

### A.1 Weight 2

By using the modular transformation of Δ⁡(n​τ)\Delta(n\tau) ([A.9](#A1.E9 "In Appendix A Γ_0⁢(𝑁) modular forms ‣ Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications")),
one can construct a modular form of weight 2 under Γ0​(N)\Gamma\_{0}(N).
Let us consider the modular transformation of E2​(n1​τ)E\_{2}(n\_{1}\tau) with n1|Nn\_{1}|N:

|  |  |  |  |
| --- | --- | --- | --- |
|  | E2​(n1​τ′)\displaystyle E\_{2}(n\_{1}\tau^{\prime}) | =1(2​π​i)​n1​∂τ′ln⁡Δ⁡(n1​τ′)\displaystyle=\frac{1}{(2\pi i)n\_{1}}\partial\_{\tau^{\prime}}\ln\Delta(n\_{1}\tau^{\prime}) |  |
|  |  |  |  |
| --- | --- | --- | --- |
|  |  | =1(2​π​i)​n1​∂τ∂τ′​∂τ(12​ln⁡(N​τ+1)+ln⁡Δ⁡(n1​τ))\displaystyle=\frac{1}{(2\pi i)n\_{1}}\frac{\partial\tau}{\partial\tau^{\prime}}\partial\_{\tau}\left(12\ln(N\tau+1)+\ln\Delta(n\_{1}\tau)\right) |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | =(N​τ+1)2​E2​(n1​τ)+Nn1​122​π​i​(N​τ+1).\displaystyle=(N\tau+1)^{2}E\_{2}(n\_{1}\tau)+\frac{N}{n\_{1}}\frac{12}{2\pi i}(N\tau+1). |  | (A.10) |

It indicates that a linear combination of E2​(τ)E\_{2}(\tau) and E2​(n1​τ)E\_{2}(n\_{1}\tau) transforms as

|  |  |  |  |
| --- | --- | --- | --- |
|  | E2​(τ′)−c1​E2​(n1​τ′)=(N​τ+1)2​(E2​(τ)−c1​E2​(n1​τ))+12​N2​π​i​(N​τ+1)​(1−c1n1).\displaystyle E\_{2}(\tau^{\prime})-c\_{1}E\_{2}(n\_{1}\tau^{\prime})=(N\tau+1)^{2}\left(E\_{2}(\tau)-c\_{1}E\_{2}(n\_{1}\tau)\right)+\frac{12N}{2\pi i}(N\tau+1)\left(1-\frac{c\_{1}}{n\_{1}}\right). |  | (A.11) |

Thus, when the constant c1c\_{1} is chosen as c1=n1c\_{1}=n\_{1} with n1|Nn\_{1}|N,
E2​(τ)−n1​E2​(n1​τ)E\_{2}(\tau)-n\_{1}E\_{2}(n\_{1}\tau) is a modular form under Γ0​(N)\Gamma\_{0}(N) of weight 2.
Furthermore, the modular transformation of E2​(n2​τ)−c2​E2​(n3​τ)E\_{2}(n\_{2}\tau)-c\_{2}E\_{2}(n\_{3}\tau)
with n2,3|Nn\_{2,3}|N and c2c\_{2} being a constant

|  |  |  |  |
| --- | --- | --- | --- |
|  | E2​(n2​τ′)−c2​E2​(n3​τ′)=(N​τ+1)2​(E2​(n2​τ)−c2​E2​(n3​τ))+12​N2​π​i​(N​τ+1)​(1n2−c2n3)\displaystyle E\_{2}(n\_{2}\tau^{\prime})-c\_{2}E\_{2}(n\_{3}\tau^{\prime})=(N\tau+1)^{2}\left(E\_{2}(n\_{2}\tau)-c\_{2}E\_{2}(n\_{3}\tau)\right)+\frac{12N}{2\pi i}(N\tau+1)\left(\frac{1}{n\_{2}}-\frac{c\_{2}}{n\_{3}}\right) |  | (A.12) |

indicates that E2​(n2​τ)−n2n3​E2​(n3​τ)E\_{2}(n\_{2}\tau)-\frac{n\_{2}}{n\_{3}}E\_{2}(n\_{3}\tau) is a modular form under Γ0​(N)\Gamma\_{0}(N) of weight 2.

For instance, there are two linearly independent modular forms of weight 2 under Γ0​(4)\Gamma\_{0}(4):

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | E2​(τ)−2​E2​(2​τ),\displaystyle E\_{2}(\tau)-2E\_{2}(2\tau), |  |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
|  |  | E2​(2​τ)−2​E2​(4​τ).\displaystyle E\_{2}(2\tau)-2E\_{2}(4\tau). |  | (A.13) |

### A.2 Weight 4

The Eisenstein series E4​(τ)E\_{4}(\tau) is a modular form of weight 4 under S​L​(2,ℤ)SL(2,\mathbb{Z}).
Since E4​(τ)E\_{4}(\tau) is written by E2​(τ)E\_{2}(\tau)

|  |  |  |  |
| --- | --- | --- | --- |
|  | E4​(τ)=−122​π​i​dd​τ​E2​(τ)+E2​(τ)2,\displaystyle E\_{4}(\tau)=-\frac{12}{2\pi i}\frac{d}{d\tau}E\_{2}(\tau)+E\_{2}(\tau)^{2}, |  | (A.14) |

the modular transformation of E4​(n​τ)E\_{4}(n\tau) under Γ0​(N)\Gamma\_{0}(N) is obtained by using that of E2​(n​τ)E\_{2}(n\tau).
It results in

|  |  |  |  |
| --- | --- | --- | --- |
|  | E4​(n​τ′)=(N​τ+1)4​E4​(n​τ),\displaystyle E\_{4}(n\tau^{\prime})=(N\tau+1)^{4}E\_{4}(n\tau), |  | (A.15) |

for n|Nn|N. Thus, E4​(n​τ)E\_{4}(n\tau) is a modular form of weight 4 under Γ0​(N)\Gamma\_{0}(N) for n|Nn|N.

### A.3 Weight 6

The Eisenstein series E6​(τ)E\_{6}(\tau) is a modular form of weight 6 under S​L​(2,ℤ)SL(2,\mathbb{Z}).
Since E6​(τ)E\_{6}(\tau) is written by E4​(τ)E\_{4}(\tau)

|  |  |  |  |
| --- | --- | --- | --- |
|  | E6​(τ)=−3​D4​E4​(τ)=−32​π​i​dd​τ​E4​(τ)+E2​(τ)​E4​(τ),\displaystyle E\_{6}(\tau)=-3D\_{4}E\_{4}(\tau)=-\frac{3}{2\pi i}\frac{d}{d\tau}E\_{4}(\tau)+E\_{2}(\tau)E\_{4}(\tau), |  | (A.16) |

the modular transformation of E6​(n​τ)E\_{6}(n\tau) under Γ0​(N)\Gamma\_{0}(N) is obtained by using that of E2​(n​τ)E\_{2}(n\tau) and E4​(n​τ)E\_{4}(n\tau).
It results in

|  |  |  |  |
| --- | --- | --- | --- |
|  | E6​(n​τ′)=(N​τ+1)6​E6​(n​τ),\displaystyle E\_{6}(n\tau^{\prime})=(N\tau+1)^{6}E\_{6}(n\tau), |  | (A.17) |

for n|Nn|N. Thus, E6​(n​τ)E\_{6}(n\tau) is a modular form of weight 6 under Γ0​(N)\Gamma\_{0}(N) for n|Nn|N.
In a similar way, higher modular forms can be constructed by acting the modular covariant differential operator
on modular forms of lower modular forms.

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