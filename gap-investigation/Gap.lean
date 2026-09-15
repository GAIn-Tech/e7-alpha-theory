prelude
/- Kernel-only bridge; no Mathlib required. E7 adjoint invariance and the
   coefficient domain are explicit inputs, NOT derived physical facts.
   SMT companion separately constructs E7 Weyl invariance over real matrices. -/
universe u v w
namespace E7Gap

inductive Same {A : Sort u} (a : A) : A → Prop where
  | refl : Same a a

theorem map_same {A : Sort u} {B : Sort v} (f : A → B)
    {a b : A} (h : Same a b) : Same (f a) (f b) :=
  Same.rec (motive := fun b _ => Same (f a) (f b)) (Same.refl) h

def Invariant {X : Type u} {V : Type v}
    (transform : X → X) (functional : X → V) : Prop :=
  ∀ x, Same (functional (transform x)) (functional x)

/-- Any coefficient postcomposition preserves an invariant functional.
    For L_c = c * B(F,F), choose scale c v = c*v. This is not an axiom
    asserting a numerical value for c. -/
theorem every_coefficient_preserves_invariance
    {X : Type u} {V : Type v} {C : Type w}
    (transform : X → X) (functional : X → V)
    (scale : C → V → V) (h : Invariant transform functional) :
    ∀ c, Invariant transform (fun x => scale c (functional x)) :=
  fun c x => map_same (scale c) (h x)

def Injective {A : Type u} {B : Type v} (f : A → B) : Prop :=
  ∀ a b, Same (f a) (f b) → Same a b

inductive Empty : Prop

def Different {A : Type u} (a b : A) : Prop := Same a b → Empty

/-- Distinct boundary coefficients remain distinct under an injective
    matching map. The SMT companion proves injectivity for k*x+d, k>0. -/
theorem matching_preserves_boundary_freedom
    {A : Type u} {B : Type v} (matching : A → B)
    (h : Injective matching) (a b : A) (hne : Different a b) :
    Different (matching a) (matching b) :=
  fun hab => hne (h a b hab)

/-- Conversely, equal independently fixed boundary data give equal outputs. -/
theorem fixed_boundary_restores_matching_uniqueness
    {A : Type u} {B : Type v} (matching : A → B)
    {a b : A} (h : Same a b) : Same (matching a) (matching b) :=
  map_same matching h

end E7Gap
#print axioms E7Gap.every_coefficient_preserves_invariance
#print axioms E7Gap.matching_preserves_boundary_freedom
#print axioms E7Gap.fixed_boundary_restores_matching_uniqueness
