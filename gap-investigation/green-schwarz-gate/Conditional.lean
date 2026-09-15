prelude
universe u
namespace BoundaryGS
inductive Same {A : Sort u} (a : A) : A → Prop where
 | refl : Same a a

theorem trans {A : Sort u} {a b c : A} (h : Same a b) (j : Same b c) : Same a c :=
 Same.rec (motive := fun c _ => Same a c) h j

theorem map {A B : Sort u} (f : A → B) {a b : A} (h : Same a b) : Same (f a) (f b) :=
 Same.rec (motive := fun b _ => Same (f a) (f b)) Same.refl h

/-- One shifting field cancels a factorized anomaly when its descent image is
    the additive inverse. No coefficient, topology, or descent premise is hidden. -/
theorem factorized_cancellation {A : Type u}
 (add : A → A → A) (neg : A → A) (zero : A)
 (inverse : ∀ a, Same (add a (neg a)) zero)
 (descent : A → A) (anomaly coupling : A)
 (matching : Same (descent coupling) (neg anomaly)) :
 Same (add anomaly (descent coupling)) zero :=
 trans (map (add anomaly) matching) (inverse anomaly)

/-- A counterterm supported at L cannot affect an independent wall-0 anomaly.
    Even if the integrated anomaly vanishes, local cancellation forces wall 0 zero. -/
theorem uncancelled_other_wall {A : Type u} (zero : A)
 (add : A → A → A) (right_zero : ∀ a, Same (add a zero) a)
 (wall0 : A) (local_cancel : Same (add wall0 zero) zero) : Same wall0 zero :=
 Same.rec (motive := fun b _ => Same b zero) local_cancel (right_zero wall0)
end BoundaryGS
#print axioms BoundaryGS.factorized_cancellation
#print axioms BoundaryGS.uncancelled_other_wall
