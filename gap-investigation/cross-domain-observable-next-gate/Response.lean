prelude
universe u
namespace PairedThreshold
inductive Same {A : Sort u} (a : A) : A → Prop where
 | refl : Same a a

theorem symm {A : Sort u} {a b : A} (h : Same a b) : Same b a :=
 Same.rec (motive := fun b _ => Same b a) Same.refl h

theorem trans {A : Sort u} {a b c : A} (h : Same a b) (k : Same b c) : Same a c :=
 Same.rec (motive := fun c _ => Same a c) h k

theorem congr {A : Sort u} {B : Sort u} (f : A → B) {a b : A}
 (h : Same a b) : Same (f a) (f b) :=
 Same.rec (motive := fun b _ => Same (f a) (f b)) Same.refl h

/-- Opposite-sign threshold channels separate both infinitesimal components.
Algebraic hypotheses hold in the additive reals; they are not physical assumptions
about measurable hidden couplings or a completed heterotic threshold. -/
theorem paired_response_separates {A : Sort u}
 (add : A → A → A) (neg : A → A) (zero : A)
 (cancel : ∀ a b c, Same (add a b) (add a c) → Same b c)
 (addZero : ∀ a, Same (add a zero) a)
 (inverse : ∀ a, Same (add a (neg a)) zero)
 (noTwoTorsion : ∀ a, Same (add a a) zero → Same a zero)
 (ds dt : A) (visible : Same (add ds dt) zero)
 (hidden : Same (add ds (neg dt)) zero) : Same dt zero :=
 noTwoTorsion dt (trans
  (congr (add dt) (cancel ds dt (neg dt) (trans visible (symm hidden))))
  (inverse dt))

theorem paired_response_dilaton {A : Sort u}
 (add : A → A → A) (neg : A → A) (zero : A)
 (cancel : ∀ a b c, Same (add a b) (add a c) → Same b c)
 (addZero : ∀ a, Same (add a zero) a)
 (inverse : ∀ a, Same (add a (neg a)) zero)
 (noTwoTorsion : ∀ a, Same (add a a) zero → Same a zero)
 (ds dt : A) (visible : Same (add ds dt) zero)
 (hidden : Same (add ds (neg dt)) zero) : Same ds zero :=
 trans (symm (addZero ds)) (trans
  (symm (congr (add ds)
   (paired_response_separates add neg zero cancel addZero inverse noTwoTorsion ds dt visible hidden)))
  visible)
end PairedThreshold
#print axioms PairedThreshold.paired_response_separates
#print axioms PairedThreshold.paired_response_dilaton
