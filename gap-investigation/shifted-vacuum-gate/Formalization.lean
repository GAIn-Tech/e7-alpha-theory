prelude
universe u v
inductive lcAny : Type
inductive lcErased : Type
noncomputable section
namespace ShiftedVacuum
inductive Eqv {A : Sort u} (a : A) : A → Prop where | refl : Eqv a a
inductive Ex {A : Sort u} (P : A → Prop) : Prop where | intro (a : A) : P a → Ex P
inductive AndP (P Q : Prop) : Prop where | intro : P → Q → AndP P Q
inductive Void : Prop
inductive N where | zero : N | succ : N → N

theorem symm {A : Sort u} {a b : A} (h : Eqv a b) : Eqv b a :=
 Eqv.rec (a := a) (motive := fun b _ => Eqv b a) Eqv.refl h

theorem trans {A : Sort u} {a b c : A} (h : Eqv a b) (k : Eqv b c) : Eqv a c :=
 Eqv.rec (a := b) (motive := fun c _ => Eqv a c) h k

theorem congr {A : Sort u} {B : Sort v} (f : A → B) {a b : A} (h : Eqv a b) : Eqv (f a) (f b) :=
 Eqv.rec (a := a) (motive := fun b _ => Eqv (f a) (f b)) Eqv.refl h

def iterate {X : Type u} (T : X → X) (x : X) : N → X := N.rec x (fun _ a => T a)

def Cauchy {X : Type u} {E : Type v} (dist : X → X → E)
 (small : E → E → Prop) (positive : E → Prop) (later : N → N → Prop) (s : N → X) : Prop :=
 ∀ e, positive e → Ex (fun k => ∀ n m, later k n → later k m → small (dist (s n) (s m)) e)

-- A constructive contraction-tail theorem. No analytic premise is silently asserted:
-- the tail bound/modulus are supplied by a contraction estimate, completeness and
-- continuity are explicit, and closed-ball membership is proved by induction.
theorem local_stationary_from_contraction_tail
 {X : Type u} {E : Type v} (T : X → X) (seed : X)
 (ball : X → Prop) (stationary : X → Prop)
 (dist : X → X → E) (small : E → E → Prop) (positive : E → Prop)
 (later : N → N → Prop) (bound : N → E)
 (converges : (N → X) → X → Prop)
 (seed_in : ball seed)
 (invariant : ∀ x, ball x → ball (T x))
 (decay : ∀ e, positive e → Ex (fun k => small (bound k) e))
 (tail : ∀ k e, small (bound k) e → ∀ n m, later k n → later k m →
    small (dist (iterate T seed n) (iterate T seed m)) e)
 (complete : ∀ s, Cauchy dist small positive later s → Ex (fun x => converges s x))
 (closed : ∀ s x, (∀ n, ball (s n)) → converges s x → ball x)
 (continuous : ∀ s x, converges s x → converges (fun n => T (s n)) (T x))
 (shift : ∀ s x, converges s x → converges (fun n => s (N.succ n)) x)
 (unique_limit : ∀ s x y, converges s x → converges s y → Eqv x y)
 (fixed_stationary : ∀ x, ball x → Eqv (T x) x → stationary x) :
 Ex (fun x => AndP (ball x) (stationary x)) :=
 let s := iterate T seed
 let cin : Cauchy dist small positive later s := fun e he =>
   Ex.rec (motive := fun _ => Ex (fun k => ∀ n m, later k n → later k m → small (dist (s n) (s m)) e))
    (fun k hk => Ex.intro k (tail k e hk)) (decay e he)
 let allin : ∀ n, ball (s n) := N.rec seed_in (fun n hn => invariant (s n) hn)
 Ex.rec (motive := fun _ => Ex (fun x => AndP (ball x) (stationary x)))
  (fun x hx =>
   let bx := closed s x allin hx
   let fx : Eqv (T x) x := unique_limit (fun n => s (N.succ n)) (T x) x (continuous s x hx) (shift s x hx)
   Ex.intro x (AndP.intro bx (fixed_stationary x bx fx))) (complete s cin)

-- First-order tadpole cancellation from a right inverse; delta is constructed,
-- not an assumed solution. Negation compatibility is an explicit linear premise.
theorem leading_displacement_cancels
 {X : Type u} (H inv neg : X → X) (t : X)
 (right_inverse : ∀ x, Eqv (H (inv x)) x)
 (linear_neg : ∀ x, Eqv (H (neg x)) (neg (H x))) :
 Eqv (H (neg (inv t))) (neg t) :=
 trans (linear_neg (inv t)) (congr neg (right_inverse t))

inductive OrP (P Q : Prop) : Prop where | left : P → OrP P Q | right : Q → OrP P Q

-- Completion-of-square positivity derived from both blocks, not a claim that
-- the singlet restriction alone is positive. Split is the invertible triangular
-- change (x,y) -> (x+H^{-1}Cy,y); identity is Schur completion of squares.
theorem schur_transfer
 {X : Type u} {Y : Type v} {E : Type}
 (Q : X → Y → E) (qa : X → E) (qs : Y → E)
 (shift : X → Y → X) (add : E → E → E)
 (positive nonnegative : E → Prop)
 (nx : X → Prop) (ny : Y → Prop) (nxy : X → Y → Prop)
 (identity : ∀ x y, Eqv (add (qa (shift x y)) (qs y)) (Q x y))
 (split : ∀ x y, nxy x y → OrP (nx (shift x y)) (ny y))
 (a_nonneg : ∀ x, nonnegative (qa x)) (s_nonneg : ∀ y, nonnegative (qs y))
 (a_pos : ∀ x, nx x → positive (qa x)) (s_pos : ∀ y, ny y → positive (qs y))
 (add_left : ∀ a b, positive a → nonnegative b → positive (add a b))
 (add_right : ∀ a b, nonnegative a → positive b → positive (add a b)) :
 ∀ x y, nxy x y → positive (Q x y) :=
 fun x y h =>
  let pos : positive (add (qa (shift x y)) (qs y)) :=
   OrP.rec (motive := fun _ => positive (add (qa (shift x y)) (qs y)))
    (fun hx => add_left (qa (shift x y)) (qs y) (a_pos (shift x y) hx) (s_nonneg y))
    (fun hy => add_right (qa (shift x y)) (qs y) (a_nonneg (shift x y)) (s_pos y hy))
    (split x y h)
  Eqv.rec (a := add (qa (shift x y)) (qs y)) (motive := fun z _ => positive z) pos (identity x y)

inductive Z3 where | zero : Z3 | one : Z3 | two : Z3
inductive TrueP : Prop where | intro : TrueP
def neg3 : Z3 → Z3 := Z3.rec Z3.zero Z3.two Z3.one
def isTwo : Z3 → Prop := Z3.rec Void Void TrueP

theorem nonvacuous_displacement : Eqv ((fun z : Z3 => z) (neg3 ((fun z : Z3 => z) Z3.one))) (neg3 Z3.one) :=
 leading_displacement_cancels (fun z => z) (fun z => z) neg3 Z3.one (fun _ => Eqv.refl) (fun _ => Eqv.refl)

theorem wrong_sign_control (h : Eqv (neg3 Z3.one) Z3.one) : Void :=
 Eqv.rec (a := Z3.two) (motive := fun z _ => isTwo z) TrueP.intro h
end ShiftedVacuum
#print axioms ShiftedVacuum.local_stationary_from_contraction_tail
#print axioms ShiftedVacuum.leading_displacement_cancels
#print axioms ShiftedVacuum.schur_transfer

#print axioms ShiftedVacuum.nonvacuous_displacement
#print axioms ShiftedVacuum.wrong_sign_control
