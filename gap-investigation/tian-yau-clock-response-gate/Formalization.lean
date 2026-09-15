prelude
universe u v w
namespace TianYauClock
inductive Same {A : Sort u} (a : A) : A → Prop where
 | refl : Same a a
inductive Empty : Prop

theorem symm {A : Sort u} {a b : A} (h : Same a b) : Same b a :=
 Same.rec (motive := fun b _ => Same b a) Same.refl h

theorem trans {A : Sort u} {a b c : A} (h : Same a b) (k : Same b c) : Same a c :=
 Same.rec (motive := fun c _ => Same a c) h k

theorem congr {A : Sort u} {B : Sort v} (f : A → B) {a b : A}
 (h : Same a b) : Same (f a) (f b) :=
 Same.rec (motive := fun b _ => Same (f a) (f b)) Same.refl h

/-- A recoverable projection, not the full state, is identifiable. -/
theorem projected_identification {State : Sort u} {Data : Sort v} {Target : Sort w}
 (obs : State → Data) (projection : State → Target) (recover : Data → Target)
 (calibrated : ∀ x, Same (recover (obs x)) (projection x))
 {x y : State} (h : Same (obs x) (obs y)) : Same (projection x) (projection y) :=
 trans (symm (calibrated x)) (trans (congr recover h) (calibrated y))

/-- An explicit nontrivial fiber prevents every full-state left inverse. -/
theorem fiber_obstructs_inverse {State : Sort u} {Data : Sort v}
 (obs : State → Data) (x y : State) (different : Same x y → Empty)
 (fiber : Same (obs x) (obs y))
 (recover : Data → State) (left : ∀ z, Same (recover (obs z)) z) : Empty :=
 different (projected_identification obs (fun z => z) recover left fiber)

inductive Bit where
 | zero : Bit
 | one : Bit
inductive Unit where
 | star : Unit
inductive True : Prop where
 | intro : True
noncomputable def distinguish : Bit → Prop := Bit.rec True Empty

theorem different_bits (h : Same Bit.zero Bit.one) : Empty :=
 Same.rec (a := Bit.zero) (motive := fun b _ => distinguish b) True.intro h

noncomputable def erase : Bit → Unit := fun _ => Unit.star

theorem concrete_nonidentifiability (r : Unit → Bit)
 (left : ∀ b, Same (r (erase b)) b) : Empty :=
 fiber_obstructs_inverse erase Bit.zero Bit.one different_bits Same.refl r left

theorem concrete_projection (x y : Bit) : Same (erase x) (erase y) := Same.refl
end TianYauClock
#print axioms TianYauClock.projected_identification
#print axioms TianYauClock.fiber_obstructs_inverse
#print axioms TianYauClock.concrete_nonidentifiability
#print axioms TianYauClock.concrete_projection
