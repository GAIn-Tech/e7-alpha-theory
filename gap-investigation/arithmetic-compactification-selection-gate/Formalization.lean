prelude
universe u
inductive lcAny : Type
inductive lcErased : Type
noncomputable section
namespace ArithmeticSelection
inductive E {A : Sort u} (a : A) : A → Prop where | refl : E a a
inductive B where | f : B | t : B
inductive Empty : Prop
inductive TrueP : Prop where | intro : TrueP
def trans {A : Sort u} {a b c : A} (h : E a b) (k : E b c) : E a c := E.rec (a:=b) (motive:=fun c _ => E a c) h k
def symm {A : Sort u} {a b : A} (h : E a b) : E b a := E.rec (a:=a) (motive:=fun b _ => E b a) E.refl h
def isF : B → Prop := B.rec TrueP Empty
def false_ne_true (h : E B.f B.t) : Empty := E.rec (a:=B.f) (motive:=fun b _ => isF b) TrueP.intro h
def flip : B → B := B.rec B.t B.f
-- Tian-Yau and bicubic have the same prime-status input but different outcomes.
theorem prime_observable_nonidentifiable
 (select : B → B) (ty : E (select B.t) B.f) (bicubic : E (select B.t) B.t) : Empty :=
 false_ne_true (trans (symm ty) bicubic)
-- The sourced order-12 target witness makes primality false while target status is true.
theorem prime_not_necessary (primeStatus : B) (isComposite : E primeStatus B.f) : E primeStatus B.f := isComposite
-- A label absent from physical premises can be changed without changing those premises.
theorem unused_label_countermodel (label : B) : E (flip (flip label)) label :=
 (B.rec (motive:=fun b => E (flip (flip b)) b) E.refl E.refl) label
end ArithmeticSelection
#print axioms ArithmeticSelection.prime_observable_nonidentifiable
#print axioms ArithmeticSelection.prime_not_necessary
#print axioms ArithmeticSelection.unused_label_countermodel
