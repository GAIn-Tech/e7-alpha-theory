prelude
universe u v w
namespace KnotThreshold
inductive Same {A : Sort u} (a : A) : A → Prop where
 | refl : Same a a
inductive Empty : Prop
inductive True : Prop where
 | intro : True
inductive Bit where
 | zero : Bit
 | one : Bit
noncomputable def not : Bit → Bit := Bit.rec Bit.one Bit.zero
noncomputable def fusion : Bit → Bit → Bit := Bit.rec (fun b => b) not
noncomputable def separate : Bit → Prop := Bit.rec True Empty

theorem symm {A : Sort u} {a b : A} (h : Same a b) : Same b a :=
 Same.rec (motive := fun b _ => Same b a) Same.refl h
theorem trans {A : Sort u} {a b c : A} (h : Same a b) (k : Same b c) : Same a c :=
 Same.rec (motive := fun c _ => Same a c) h k
theorem congr {A : Sort u} {B : Sort v} (f : A → B) {a b : A} (h : Same a b) : Same (f a) (f b) :=
 Same.rec (motive := fun b _ => Same (f a) (f b)) Same.refl h

theorem zero_ne_one (h : Same Bit.zero Bit.one) : Empty :=
 Same.rec (a := Bit.zero) (motive := fun b _ => separate b) True.intro h

theorem two_nontrivial_fuse_vacuum : Same (fusion Bit.one Bit.one) Bit.zero := Same.refl
theorem three_nontrivial_not_vacuum
 (h : Same (fusion (fusion Bit.one Bit.one) Bit.one) Bit.zero) : Empty :=
 zero_ne_one (symm h)

/-- Any target varying inside an observation fiber cannot factor through the observation. -/
theorem fiber_target_obstruction {State : Sort u} {Data : Sort v} {Target : Sort w}
 (obs : State → Data) (target : State → Target) (x y : State)
 (fiber : Same (obs x) (obs y)) (different : Same (target x) (target y) → Empty)
 (recover : Data → Target) (matches : ∀ z, Same (recover (obs z)) (target z)) : Empty :=
 different (trans (symm (matches x)) (trans (congr recover fiber) (matches y)))

inductive State where
 | mk : Bit → Bit → State
noncomputable def obs : State → Bit := State.rec (fun b _ => b)
noncomputable def target : State → Bit := State.rec (fun _ m => m)

theorem nonconstant_observation : Same (obs (State.mk Bit.zero Bit.zero)) (obs (State.mk Bit.one Bit.zero)) → Empty := zero_ne_one

theorem concrete_target_obstruction (recover : Bit → Bit)
 (matches : ∀ s, Same (recover (obs s)) (target s)) : Empty :=
 fiber_target_obstruction obs target (State.mk Bit.zero Bit.zero) (State.mk Bit.zero Bit.one)
 Same.refl zero_ne_one recover matches

/-- Positive control: the visible coordinate, unlike the hidden target, is recoverable. -/
theorem visible_recovery (s : State) : Same ((fun b => b) (obs s)) (obs s) := Same.refl
end KnotThreshold
#print axioms KnotThreshold.two_nontrivial_fuse_vacuum
#print axioms KnotThreshold.three_nontrivial_not_vacuum
#print axioms KnotThreshold.fiber_target_obstruction
#print axioms KnotThreshold.nonconstant_observation
#print axioms KnotThreshold.concrete_target_obstruction
#print axioms KnotThreshold.visible_recovery
