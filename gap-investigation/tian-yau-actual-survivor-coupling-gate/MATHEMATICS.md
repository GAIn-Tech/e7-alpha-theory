# Chain conventions and claim ledger

## Strict curved-module construction

Let L be the three-term ambient monad and K the exterior Koszul algebra on the three defining equations f_h. The ambient differential d_L obeys d_L^2=sum_h f_h H_h, where H_h:A->C is the explicit multidegree homotopy. On K tensor L use

D_internal = kappa + (-1)^k d_L - sum_h epsilon_h H_h.

The curvature term cancels d_L squared because {kappa,epsilon_h}=f_h. The mixed terms vanish by degree (d_L H_h=H_h d_L=0) and the H_h pairwise compositions vanish; exterior multiplication anticommutes. Tensor-standard-cover Cech differential is multiplied by (-1)^(p-k), where p is monad/End degree, k exterior degree, and q the sum of the two Cech degrees. Total degree is p+q-k. The predecessor's curved-End operator is the corresponding graded commutator on coefficients, extended across K and the cover. The dummy scalar O in the implementation is a disconnected degree-zero term used to identify tangent vectors as Hom(O,L), dual vectors as Hom(L,O), and evaluation as composition. It adds no geometric summand to L's cohomology.

For alpha=(I,phi,X,Y) with End degree p and Cech degree q, and v=(J,b,U,V) with monad degree p_b, the implemented product is zero unless exterior factors are disjoint and the Alexander-Whitney endpoints satisfy last(X)=first(U), last(Y)=first(V). Otherwise multiply monomials and matrices and concatenate charts, with sign exponent

p*|J| + q*(p_b-|J|) + (|Y|-1)(|U|-1) + #{(i,j) in I x J : i>j}.

These are respectively End/Koszul interchange, Cech/internal interchange, tensor-cover interchange, and exterior-order signs. This product is associative as the tensor DG product; the certificate executes its required Leibniz instances on every neutral support key, including nonclosed keys. No harmonic projection is inserted into the product.

## Actual reduction, not assigned endpoint coordinates

The inherited Cech homotopy is extended by finite Koszul perturbation, and all rational solves are checked back on full cochains. In H2(TX), first read the A H3 coordinates, subtract their explicitly lifted full cocycles, then eliminate p=-1 and p=0 vertical boundaries by genuine primitives. Project the remaining C H1 component into the actual quotient by the B H1 Jacobian map. Lift that image boundary, and solve its residual vertical boundary. For every product v, the saved certificate contains h (its H2 representative) and b with the verified exact equation v=h+D b.

The dual four nonpolynomial classes similarly start in the actual kernel of the C* H2 -> B* H2 map and solve both later vertical lift equations. Together with the two terminal A* global classes they give six D-closed degree-one dual cocycles.

Evaluation beta(v) is a scalar total-degree-three cocycle. Transfer to the actual ambient H6/Koszul-degree-three representative of H3(O_X), and read its rational coordinate. The displayed generator fixes the algebraic residue convention. A nondegenerate computed pairing (determinant one) verifies all six dual modes against the six independently built tangent H2 modes. This does not compute a harmonic metric or physical holomorphic-volume normalization.

## Quotient and invariant controls

All Laurent terms obey the two line-bundle degrees, localization support, exterior ordering, actual Z3 phase and total degree. The invariant tangent and dual E1/E2 matrices are constructed from the same geometry. For the three-column tangent/dual strip, the only potentially relevant r=2 arrows have zero targets (or zero sources) in the listed rows, and r>=3 leaves the strip. H1=9 and H2=6 therefore follow from the displayed actual quotients rather than a guessed tensor shape.

Exact source, charged and dual changes obey their proper signed Leibniz boundary identities. The certificate checks nonzero such perturbations; counting a zero contracting homotopy as a representative test is prohibited. The first attempt at an auxiliary dual fixture was rejected for precisely this reason and preserved.

## Claim ledger

Established by exact local computations: four accepted neutral D-cocycles reused with pinned hash; invariant charged and dual domains; explicit action; all product lifts and boundary decompositions; invertible Serre pairing; complete 4x9x6 algebraic tensor; flavor-dependent neutral F contractions of the predecessor's gauge-matrix pattern.

Inherited, not recomputed as a new contribution here: accepted d2/d4 abutment Ext1_0=16, consisting of four actual survivors and twelve polynomial classes; vanishing of the polynomial-neutral tensor; geometry smoothness/freeness and standard-embedding model assumptions.

Not established: identification of the predecessor's unspecified geometric flavors (none was supplied), canonical field metrics, the complete compactification superpotential, quadratic Kuranishi unobstructedness, a higher-order simultaneous F/D solution, stability, exotic removal, moduli fixation, threshold matching, or alpha/clock/knot/partition predictions. The explicit first-two-flavor embedding is a new algebraic witness, not a retrospective identification or a complete vacuum.

Evidence class: exact computational certificate over QQ with immutable native replay; no Lean proof, CI run, independent expert review, external publication or other-lane edits.
