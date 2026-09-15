prelude
universe u
inductive lcAny : Type
inductive lcErased : Type
noncomputable section
namespace WilsonMass
inductive E {A : Sort u} (a : A) : A → Prop where | refl : E a a
inductive N where | z : N | s : N → N
def congr {A B : Sort u} (f : A → B) {a b : A} (h : E a b) : E (f a) (f b) :=
 E.rec (a := a) (motive := fun b _ => E (f a) (f b)) E.refl h
def trans {A : Sort u} {a b c : A} (h : E a b) (k : E b c) : E a c :=
 E.rec (a := b) (motive := fun c _ => E a c) h k
def symm {A : Sort u} {a b : A} (h : E a b) : E b a :=
 E.rec (a := a) (motive := fun b _ => E b a) E.refl h
def add (a b : N) : N := N.rec (motive := fun _ => N) a (fun _ x => N.s x) b
def pred : N → N := N.rec (motive := fun _ => N) N.z (fun n _ => n)
theorem add_succ_left (a : N) : ∀ b : N, E (add (N.s a) b) (N.s (add a b)) :=
 N.rec (motive := fun b => E (add (N.s a) b) (N.s (add a b))) E.refl
  (fun _ ih => congr N.s ih)
-- Universal exchange of the two removed/retained natural counts.
theorem right_swap (a p : N) : ∀ k : N, E (add (add a p) k) (add (add a k) p) :=
 N.rec (motive := fun k => E (add (add a p) k) (add (add a k) p)) E.refl
  (fun k ih => trans (congr N.s ih) (symm (add_succ_left (add a k) p)))
theorem right_cancel (a b : N) : ∀ p : N, E (add a p) (add b p) → E a b :=
 N.rec (motive := fun p => E (add a p) (add b p) → E a b)
  (fun h => h) (fun _ ih h => ih (congr pred h))
-- Physical premises remain external: n=m+k in one corresponding irrep,
-- and an ordinary gauge-invariant mass removes p fields on BOTH sides.
-- The conclusion is not assumed, nor are mass rank or topology asserted.
theorem paired_mass_preserves_net (n m nleft mleft p k : N)
 (net : E n (add m k)) (left_removal : E n (add nleft p))
 (right_removal : E m (add mleft p)) : E nleft (add mleft k) :=
 right_cancel nleft (add mleft k) p
  (trans (symm left_removal)
   (trans net
    (trans (congr (fun x => add x k) right_removal) (right_swap mleft p k))))
def one : N := N.s N.z
def three : N := N.s (N.s one)
def four : N := N.s three
def seven : N := add four three
-- Nonzero witness: four vectorlike pairs removed, not erased by an index.
theorem four_pairs_witness : E three (add N.z three) :=
 paired_mass_preserves_net seven four three N.z four three
  E.refl E.refl E.refl
end WilsonMass
#print axioms WilsonMass.add_succ_left
#print axioms WilsonMass.right_swap
#print axioms WilsonMass.right_cancel
#print axioms WilsonMass.paired_mass_preserves_net
#print axioms WilsonMass.four_pairs_witness
