prelude
universe u
inductive lcAny : Type
inductive lcErased : Type
noncomputable section
namespace ModularGate
inductive Eqv {A : Sort u} (a : A) : A → Prop where
 | refl : Eqv a a
inductive Void : Prop
inductive UnitP : Prop where | intro : UnitP
inductive Bit where | b0 : Bit | b1 : Bit
inductive Z4 where | z0 : Z4 | z1 : Z4 | z2 : Z4 | z3 : Z4
def plus4 : Z4 → Z4 → Z4 := (Z4.rec (motive := fun _ => Z4 → Z4) ((Z4.rec (motive := fun _ => Z4) (Z4.z0) (Z4.z1) (Z4.z2) (Z4.z3))) ((Z4.rec (motive := fun _ => Z4) (Z4.z1) (Z4.z2) (Z4.z3) (Z4.z0))) ((Z4.rec (motive := fun _ => Z4) (Z4.z2) (Z4.z3) (Z4.z0) (Z4.z1))) ((Z4.rec (motive := fun _ => Z4) (Z4.z3) (Z4.z0) (Z4.z1) (Z4.z2))))
def xor : Bit → Bit → Bit := (Bit.rec (motive := fun _ => Bit → Bit) ((Bit.rec (motive := fun _ => Bit) (Bit.b0) (Bit.b1))) ((Bit.rec (motive := fun _ => Bit) (Bit.b1) (Bit.b0))))
def q7 : Bit → Z4 := (Bit.rec (motive := fun _ => Z4) (Z4.z0) (Z4.z3))
def qA : Bit → Z4 := (Bit.rec (motive := fun _ => Z4) (Z4.z0) (Z4.z1))
def pairing : Bit → Bit → Z4 := (Bit.rec (motive := fun _ => Bit → Z4) ((Bit.rec (motive := fun _ => Z4) (Z4.z0) (Z4.z0))) ((Bit.rec (motive := fun _ => Z4) (Z4.z0) (Z4.z2))))
def gluedQ (x y : Bit) : Z4 := plus4 (q7 x) (qA y)
def isZero : Z4 → Prop := (Z4.rec (motive := fun _ => Prop) (UnitP) (Void) (Void) (Void))
theorem z1_ne_z0 (h : Eqv Z4.z0 Z4.z1) : Void := Eqv.rec (a := Z4.z0) (motive := fun q _ => isZero q) UnitP.intro h
theorem z3_ne_z0 (h : Eqv Z4.z0 Z4.z3) : Void := Eqv.rec (a := Z4.z0) (motive := fun q _ => isZero q) UnitP.intro h
theorem polarization_E7 : ∀ x y : Bit, Eqv (q7 (xor x y)) (plus4 (plus4 (q7 x) (q7 y)) (pairing x y)) := (Bit.rec (motive := fun x => ∀ y : Bit, Eqv (q7 (xor x y)) (plus4 (plus4 (q7 x) (q7 y)) (pairing x y))) ((Bit.rec (motive := fun y => Eqv (q7 (xor Bit.b0 y)) (plus4 (plus4 (q7 Bit.b0) (q7 y)) (pairing Bit.b0 y))) (Eqv.refl) (Eqv.refl))) ((Bit.rec (motive := fun y => Eqv (q7 (xor Bit.b1 y)) (plus4 (plus4 (q7 Bit.b1) (q7 y)) (pairing Bit.b1 y))) (Eqv.refl) (Eqv.refl))))
theorem polarization_A1 : ∀ x y : Bit, Eqv (qA (xor x y)) (plus4 (plus4 (qA x) (qA y)) (pairing x y)) := (Bit.rec (motive := fun x => ∀ y : Bit, Eqv (qA (xor x y)) (plus4 (plus4 (qA x) (qA y)) (pairing x y))) ((Bit.rec (motive := fun y => Eqv (qA (xor Bit.b0 y)) (plus4 (plus4 (qA Bit.b0) (qA y)) (pairing Bit.b0 y))) (Eqv.refl) (Eqv.refl))) ((Bit.rec (motive := fun y => Eqv (qA (xor Bit.b1 y)) (plus4 (plus4 (qA Bit.b1) (qA y)) (pairing Bit.b1 y))) (Eqv.refl) (Eqv.refl))))
theorem diagonal_glue_isotropic : ∀ x : Bit, Eqv (gluedQ x x) Z4.z0 := (Bit.rec (motive := fun x => Eqv (gluedQ x x) Z4.z0) (Eqv.refl) (Eqv.refl))
theorem isotropic_implies_diagonal : ∀ x y : Bit, Eqv Z4.z0 (gluedQ x y) → Eqv x y := (Bit.rec (motive := fun x => ∀ y : Bit, Eqv Z4.z0 (gluedQ x y) → Eqv x y) ((Bit.rec (motive := fun y => Eqv Z4.z0 (gluedQ Bit.b0 y) → Eqv Bit.b0 y) (fun _ => Eqv.refl) (fun h => Void.rec (motive := fun _ => Eqv Bit.b0 Bit.b1) (z1_ne_z0 h)))) ((Bit.rec (motive := fun y => Eqv Z4.z0 (gluedQ Bit.b1 y) → Eqv Bit.b1 y) (fun h => Void.rec (motive := fun _ => Eqv Bit.b1 Bit.b0) (z3_ne_z0 h)) (fun _ => Eqv.refl))))
theorem E7_nonzero_not_isotropic (h : Eqv Z4.z0 (q7 Bit.b1)) : Void := z3_ne_z0 h
end ModularGate
#print axioms ModularGate.polarization_E7
#print axioms ModularGate.polarization_A1
#print axioms ModularGate.diagonal_glue_isotropic
#print axioms ModularGate.isotropic_implies_diagonal
#print axioms ModularGate.E7_nonzero_not_isotropic
