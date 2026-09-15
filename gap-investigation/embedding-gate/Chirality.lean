prelude
/- Conditional kernel bridge only. Representation restriction, mass-matrix
   rank pairing, and physical interpretation are NOT kernel-proved here. -/
universe u v
namespace Embedding
inductive Same {A : Sort u} (a : A) : A → Prop where
  | refl : Same a a

theorem map2 {A : Sort u} {B : Sort v} (f : A → A → B)
    {a b c d : A} (h : Same a b) (k : Same c d) : Same (f a c) (f b d) :=
  Same.rec (motive := fun b _ => Same (f a c) (f b d))
    (Same.rec (motive := fun d _ => Same (f a c) (f a d)) Same.refl k) h

/-- Equal conjugate multiplicities remain equal after removing equal mass ranks.
    Instantiate remove with natural-number subtraction and rank with the rank
    of an H-invariant R-by-conjugate(R) mass matrix. Those inputs are explicit. -/
theorem paired_mass_removal_preserves_balance
    {Rep : Type u} {Count : Type v}
    (bar : Rep → Rep) (count rank : Rep → Count) (remove : Count → Count → Count)
    (balanced : ∀ r, Same (count r) (count (bar r)))
    (paired : ∀ r, Same (rank r) (rank (bar r))) :
    ∀ r, Same (remove (count r) (rank r)) (remove (count (bar r)) (rank (bar r))) :=
  fun r => map2 remove (balanced r) (paired r)
end Embedding
#print axioms Embedding.paired_mass_removal_preserves_balance
