prelude
universe u v w t
inductive lcAny : Type
inductive lcErased : Type
noncomputable section
set_option linter.unusedVariables false
set_option linter.defProp false
namespace CubicGate
inductive Eqv {A : Sort u} (a : A) : A → Prop where
 | refl : Eqv a a
 theorem sym {A : Sort u} {a b : A} (h : Eqv a b) : Eqv b a :=
 Eqv.rec (motive := fun b _ => Eqv b a) Eqv.refl h
 theorem trans {A : Sort u} {a b c : A} (h : Eqv a b) (k : Eqv b c) : Eqv a c :=
 Eqv.rec (motive := fun c _ => Eqv a c) h k
 theorem cong {A : Sort u} {B : Sort v} (f : A → B) {a b : A} (h : Eqv a b) : Eqv (f a) (f b) :=
 Eqv.rec (motive := fun b _ => Eqv (f a) (f b)) Eqv.refl h
inductive Void : Prop
inductive UnitP : Prop where | intro : UnitP
/-- Explicit fragment of additive-group laws. Every additive group supplies it.
Associativity/commutativity are not needed by the proof. -/
inductive AddCore (A : Type u) where
 | mk (zero : A) (add : A → A → A) (neg : A → A) (right_zero : ∀ x, Eqv (add x zero) x) (add_neg : ∀ x, Eqv (add x (neg x)) zero) (neg_add : ∀ x, Eqv (add (neg x) x) zero) (cancel : ∀ a b c, Eqv (add a b) (add a c) → Eqv b c) : AddCore A
namespace AddCore
noncomputable def zero {A : Type u} (d : AddCore A) : A :=
 AddCore.rec (motive := fun d => A) (fun zero add neg right_zero add_neg neg_add cancel => zero) d
noncomputable def add {A : Type u} (d : AddCore A) : A → A → A :=
 AddCore.rec (motive := fun d => A → A → A) (fun zero add neg right_zero add_neg neg_add cancel => add) d
noncomputable def neg {A : Type u} (d : AddCore A) : A → A :=
 AddCore.rec (motive := fun d => A → A) (fun zero add neg right_zero add_neg neg_add cancel => neg) d
noncomputable def right_zero {A : Type u} (d : AddCore A) : ∀ x, Eqv ((add d) x (zero d)) x :=
 AddCore.rec (motive := fun d => ∀ x, Eqv ((add d) x (zero d)) x) (fun zero add neg right_zero add_neg neg_add cancel => right_zero) d
noncomputable def add_neg {A : Type u} (d : AddCore A) : ∀ x, Eqv ((add d) x ((neg d) x)) (zero d) :=
 AddCore.rec (motive := fun d => ∀ x, Eqv ((add d) x ((neg d) x)) (zero d)) (fun zero add neg right_zero add_neg neg_add cancel => add_neg) d
noncomputable def neg_add {A : Type u} (d : AddCore A) : ∀ x, Eqv ((add d) ((neg d) x) x) (zero d) :=
 AddCore.rec (motive := fun d => ∀ x, Eqv ((add d) ((neg d) x) x) (zero d)) (fun zero add neg right_zero add_neg neg_add cancel => neg_add) d
noncomputable def cancel {A : Type u} (d : AddCore A) : ∀ a b c, Eqv ((add d) a b) ((add d) a c) → Eqv b c :=
 AddCore.rec (motive := fun d => ∀ a b c, Eqv ((add d) a b) ((add d) a c) → Eqv b c) (fun zero add neg right_zero add_neg neg_add cancel => cancel) d
end AddCore

def Additive {A : Type u} {B : Type v} (a : AddCore A) (b : AddCore B) (f : A → B) : Prop :=
 ∀ x y, Eqv (f (a.add x y)) (b.add (f x) (f y))

theorem additive_zero {A : Type u} {B : Type v} (a : AddCore A) (b : AddCore B)
 (f : A → B) (h : Additive a b f) : Eqv (f a.zero) b.zero :=
 b.cancel (f a.zero) (f a.zero) b.zero
 (trans (sym (h a.zero a.zero))
 (trans (cong f (a.right_zero a.zero)) (sym (b.right_zero (f a.zero)))))

theorem additive_neg {A : Type u} {B : Type v} (a : AddCore A) (b : AddCore B)
 (f : A → B) (h : Additive a b f) (x : A) : Eqv (f (a.neg x)) (b.neg (f x)) :=
 b.cancel (f x) (f (a.neg x)) (b.neg (f x))
 (trans (sym (h x (a.neg x)))
 (trans (cong f (a.add_neg x))
 (trans (additive_zero a b f h) (sym (b.add_neg (f x))))))

def NoTwoTorsion {K : Type u} (k : AddCore K) : Prop :=
 ∀ q, Eqv (k.add q q) k.zero → Eqv q k.zero

theorem fixed_neg_zero {K : Type u} (k : AddCore K) (h2 : NoTwoTorsion k)
 (q : K) (h : Eqv q (k.neg q)) : Eqv q k.zero :=
 h2 q (trans (cong (k.add q) h) (k.add_neg q))

/-- Additivity in each slot derives the odd sign: no sign law for T is assumed. -/
theorem three_neg_sign {A : Type u} {B : Type v} {C : Type w} {K : Type t}
 (a : AddCore A) (b : AddCore B) (c : AddCore C) (k : AddCore K)
 (T : A → B → C → K)
 (hA : ∀ y z, Additive a k (fun x => T x y z))
 (hB : ∀ x z, Additive b k (fun y => T x y z))
 (hC : ∀ x y, Additive c k (fun z => T x y z))
 (x : A) (y : B) (z : C) :
 Eqv (T (a.neg x) (b.neg y) (c.neg z)) (k.neg (T x y z)) :=
 let doubleNeg : ∀ q, Eqv (k.neg (k.neg q)) q := fun q =>
   k.cancel (k.neg q) (k.neg (k.neg q)) q
    (trans (k.add_neg (k.neg q)) (sym (k.neg_add q)))
 trans (additive_neg a k (fun x => T x (b.neg y) (c.neg z)) (hA (b.neg y) (c.neg z)) x)
 (trans (cong k.neg (additive_neg b k (fun y => T x y (c.neg z)) (hB x (c.neg z)) y))
 (trans (doubleNeg (T x y (c.neg z)))
 (additive_neg c k (fun z => T x y z) (hC x y) z)))

/-- Simultaneous central action on three odd slots; trivial action on the target.
Only the indicated transformation is required, not an entire group formalization. -/
theorem invariant_odd_trilinear_vanishes
 {A : Type u} {B : Type v} {C : Type w} {K : Type t}
 (a : AddCore A) (b : AddCore B) (c : AddCore C) (k : AddCore K)
 (h2 : NoTwoTorsion k) (T : A → B → C → K)
 (hA : ∀ y z, Additive a k (fun x => T x y z))
 (hB : ∀ x z, Additive b k (fun y => T x y z))
 (hC : ∀ x y, Additive c k (fun z => T x y z))
 (sA : A → A) (sB : B → B) (sC : C → C)
 (oddA : ∀ x, Eqv (sA x) (a.neg x))
 (oddB : ∀ y, Eqv (sB y) (b.neg y))
 (oddC : ∀ z, Eqv (sC z) (c.neg z))
 (invariant : ∀ x y z, Eqv (T (sA x) (sB y) (sC z)) (T x y z)) :
 ∀ x y z, Eqv (T x y z) k.zero :=
 fun x y z => fixed_neg_zero k h2 (T x y z)
 (trans (sym (invariant x y z))
 (trans (cong (fun q => T q (sB y) (sC z)) (oddA x))
 (trans (cong (fun q => T (a.neg x) q (sC z)) (oddB y))
 (trans (cong (fun q => T (a.neg x) (b.neg y) q) (oddC z))
 (three_neg_sign a b c k T hA hB hC x y z)))))
end CubicGate
#print axioms CubicGate.additive_zero
#print axioms CubicGate.additive_neg
#print axioms CubicGate.fixed_neg_zero
#print axioms CubicGate.three_neg_sign
#print axioms CubicGate.invariant_odd_trilinear_vanishes
