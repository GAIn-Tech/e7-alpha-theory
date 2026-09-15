prelude
universe u
inductive lcAny : Type
inductive lcErased : Type
noncomputable section
namespace CoverIndex
inductive E {A : Sort u} (a : A) : A → Prop where | refl : E a a
inductive N where | z : N | s : N → N
def congr {A B : Sort u} (f : A → B) {a b : A} (h : E a b) : E (f a) (f b) :=
 E.rec (a := a) (motive := fun b _ => E (f a) (f b)) E.refl h
def trans {A : Sort u} {a b c : A} (h : E a b) (k : E b c) : E a c :=
 E.rec (a := b) (motive := fun c _ => E a c) h k
def symm {A : Sort u} {a b : A} (h : E a b) : E b a :=
 E.rec (a := a) (motive := fun b _ => E b a) E.refl h
def triple : N → N := N.rec (motive := fun _ => N) N.z (fun _ n => N.s (N.s (N.s n)))
def pred : N → N := N.rec (motive := fun _ => N) N.z (fun n _ => n)
-- A direct recursor proof of triple injectivity avoids any division library.
def succ_inj {a b : N} (h : E (N.s a) (N.s b)) : E a b := congr pred h
inductive Empty : Prop
inductive TrueP : Prop where | intro : TrueP
def zeroTest : N → Prop := N.rec (motive := fun _ => Prop) TrueP (fun _ _ => Empty)
def zero_not_succ {n : N} (h : E N.z (N.s n)) : Empty :=
 E.rec (a := N.z) (motive := fun b _ => zeroTest b) TrueP.intro h

theorem triple_injective : ∀ a b : N, E (triple a) (triple b) → E a b :=
 N.rec (motive := fun a => ∀ b : N, E (triple a) (triple b) → E a b)
  (N.rec (motive := fun b => E (triple N.z) (triple b) → E N.z b)
   (fun _ => E.refl)
   (fun b _ h => Empty.rec (motive := fun _ => E N.z (N.s b)) (zero_not_succ h)))
  (fun a ih => N.rec (motive := fun b => E (triple (N.s a)) (triple b) → E (N.s a) b)
   (fun h => Empty.rec (motive := fun _ => E (N.s a) N.z) (zero_not_succ (symm h)))
   (fun b _ h => congr N.s (ih b (succ_inj (succ_inj (succ_inj h))))))

def three : N := N.s (N.s (N.s N.z))
def nine : N := triple three
-- External topology premise: absolute cover index is triple quotient index.
-- External geometric input: this cover index magnitude is nine.
theorem degree_three_cover_net_three (q cover : N)
 (cover_law : E (triple q) cover) (cover_value : E cover nine) : E q three :=
 triple_injective q three (trans cover_law cover_value)
-- If the cover has zero index, a degree-three descent cannot create chirality.
theorem degree_three_zero_index (q : N) (cover_law : E (triple q) N.z) : E q N.z :=
 triple_injective q N.z cover_law
-- Explicit nonzero example exercising the conditional theorem.
theorem three_family_witness : E three three :=
 degree_three_cover_net_three three nine E.refl E.refl
end CoverIndex
#print axioms CoverIndex.triple_injective
#print axioms CoverIndex.degree_three_cover_net_three
#print axioms CoverIndex.degree_three_zero_index
#print axioms CoverIndex.three_family_witness
