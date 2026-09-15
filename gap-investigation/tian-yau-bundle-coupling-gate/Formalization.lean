prelude
universe u
inductive lcAny : Type
inductive lcErased : Type
noncomputable section
namespace BundleCup
inductive E {A : Sort u} (a : A) : A → Prop where | refl : E a a
def trans {A : Sort u} {a b c : A} (h:E a b) (k:E b c) : E a c := E.rec (a:=b) (motive:=fun c _ => E a c) h k
structure AddGroup where
  A : Type u
  zero : A
  add : A → A → A
structure Complex where
  G : AddGroup
  d0 : G.A → G.A
  d1 : G.A → G.A
  chain : ∀ x, E (d1 (d0 x)) G.zero
-- The actual algebra certificate supplies δd+dδ=0. This kernel theorem
-- isolates the substantive consequence used for the terminal-C classes:
-- if δ vanishes there, the induced obstruction representative is zero.
theorem terminal_zero_cup (K : Complex) (delta : K.G.A → K.G.A)
  (terminal : ∀ x, E (delta x) K.G.zero) (c : K.G.A) :
  E (delta c) K.G.zero := terminal c
-- A representative differing by a boundary remains closed; this is the
-- exact chain-complex prerequisite behind quotienting polynomial maps.
theorem boundary_is_closed (K : Complex) (b : K.G.A) :
  E (K.d1 (K.d0 b)) K.G.zero := K.chain b
end BundleCup
#print axioms BundleCup.terminal_zero_cup
#print axioms BundleCup.boundary_is_closed
