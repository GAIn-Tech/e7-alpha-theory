prelude
/- Kernel-only conditional inverse-problem composition.
   No real-number arithmetic, EFT, spectrum, or atomic physics is formalized. -/
universe u v w
namespace ClockMatching
inductive Same {A : Sort u} (a : A) : A → Prop where
  | refl : Same a a

theorem symm {A : Sort u} {a b : A} (h : Same a b) : Same b a :=
  Same.rec (motive := fun b _ => Same b a) Same.refl h

theorem trans {A : Sort u} {a b c : A}
    (h : Same a b) (k : Same b c) : Same a c :=
  Same.rec (motive := fun c _ => Same a c) h k

theorem congr {A : Sort u} {B : Sort v} (f : A → B)
    {a b : A} (h : Same a b) : Same (f a) (f b) :=
  Same.rec (motive := fun b _ => Same (f a) (f b)) Same.refl h

/-- A supplied left inverse makes observations identify the matched state. -/
theorem left_inverse_identifies {A : Sort u} {B : Sort v}
    (obs : A → B) (recover : B → A)
    (left : ∀ a, Same (recover (obs a)) a)
    {a b : A} (equal_obs : Same (obs a) (obs b)) : Same a b :=
  trans (symm (left a)) (trans (congr recover equal_obs) (left b))

/-- Clock inversion and threshold-fixed matching inversion are distinct
    hypotheses. Both must be independently available to identify a UV jet. -/
theorem two_stage_identification
    {UV : Sort u} {Matched : Sort v} {Data : Sort w}
    (matching : UV → Matched) (unmatch : Matched → UV)
    (clock : Matched → Data) (recover : Data → Matched)
    (matching_left : ∀ p, Same (unmatch (matching p)) p)
    (clock_left : ∀ h, Same (recover (clock h)) h)
    {p q : UV}
    (equal_data : Same (clock (matching p)) (clock (matching q))) : Same p q :=
  left_inverse_identifies matching unmatch matching_left
    (left_inverse_identifies clock recover clock_left equal_data)
end ClockMatching
#print axioms ClockMatching.left_inverse_identifies
#print axioms ClockMatching.two_stage_identification
