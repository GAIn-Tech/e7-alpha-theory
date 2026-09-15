import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.LinearCombination
import Mathlib.Data.Fintype.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

-- Generated from immutable saved channel coefficient tables; no zero-sum premise.
namespace Rxi
variable {K : Type*} [Field K] [CharZero K]

inductive PhysicalMaster where
  | m0 -- A(a*xi)
  | m1 -- I(0, t)
  | m2 -- I(t, a*xi)
  deriving DecidableEq, Fintype

def physicalScalarBubble (a t s rho xi : K) : PhysicalMaster → K
  | .m0 => 0
  | .m1 => (((-2) * (((-rho) + t) ^ 2)) / a)
  | .m2 => ((2 * (((-rho) + t) ^ 2)) / a)

def physicalMixed (a t s rho xi : K) : PhysicalMaster → K
  | .m0 => ((2 * ((((-a) * xi) + s) - t)) / a)
  | .m1 => ((2 * ((s - t) ^ 2)) / a)
  | .m2 => (((-2) * ((s - t) ^ 2)) / a)

def physicalVectorSeagull (a t s rho xi : K) : PhysicalMaster → K
  | .m0 => (2 * xi)
  | .m1 => 0
  | .m2 => 0

def physicalStationary (a t s rho xi : K) : PhysicalMaster → K
  | .m0 => ((2 * (t - rho)) / a)
  | .m1 => 0
  | .m2 => 0

def physicalCoefficient (a t s rho xi : K) (m : PhysicalMaster) : K :=
  physicalScalarBubble a t s rho xi m + physicalMixed a t s rho xi m + physicalVectorSeagull a t s rho xi m + physicalStationary a t s rho xi m

def physicalFactor (a t s rho xi : K) : PhysicalMaster → K
  | .m0 => (2 / a)
  | .m1 => ((((2 * rho) + (2 * s)) - (4 * t)) / a)
  | .m2 => (((((-2) * rho) - (2 * s)) + (4 * t)) / a)

theorem physical_factorization (a t s rho xi : K) (ha : a ≠ 0) (m : PhysicalMaster) :
    physicalCoefficient a t s rho xi m = (s-rho) * physicalFactor a t s rho xi m := by
  cases m <;> simp only [physicalCoefficient, physicalFactor, physicalScalarBubble, physicalMixed, physicalVectorSeagull, physicalStationary] <;>
    field_simp [ha] <;> ring

theorem physical_on_shell (a t s rho xi : K) (ha : a ≠ 0) (hs : s = rho) (m : PhysicalMaster) :
    physicalCoefficient a t s rho xi m = 0 := by
  rw [physical_factorization a t s rho xi ha m, hs]
  simp

def physicalAmplitude (a t s rho xi : K) (master : PhysicalMaster → K) : K :=
  ∑ m, physicalCoefficient a t s rho xi m * master m

theorem physical_amplitude_on_shell (a t s rho xi : K) (ha : a ≠ 0) (hs : s = rho) (master : PhysicalMaster → K) :
    physicalAmplitude a t s rho xi master = 0 := by
  simp [physicalAmplitude, physical_on_shell a t s rho xi ha hs]

theorem off_shell_nonzero : physicalCoefficient (2:ℚ) 3 7 5 1 .m0 = 2 := by
  norm_num [physicalCoefficient, physicalScalarBubble, physicalMixed, physicalVectorSeagull, physicalStationary]

inductive PairMaster where
  | m0 -- A(a)
  | m1 -- A(a*xi)
  | m2 -- A(b)
  | m3 -- A(b*xi)
  | m4 -- I(0, 0)
  | m5 -- I(0, a)
  | m6 -- I(0, b)
  | m7 -- I(a*xi, b*xi)
  | m8 -- I(a, b*xi)
  | m9 -- I(b, a*xi)
  deriving DecidableEq, Fintype

def pairScalarBubble (a b s rho xi : K) : PairMaster → K
  | .m0 => 0
  | .m1 => 0
  | .m2 => 0
  | .m3 => 0
  | .m4 => ((-(rho ^ 2)) / (a * b))
  | .m5 => 0
  | .m6 => 0
  | .m7 => ((rho ^ 2) / (a * b))
  | .m8 => 0
  | .m9 => 0

def pairMixed (a b s rho xi : K) : PairMaster → K
  | .m0 => (xi / a)
  | .m1 => ((((((-a) * xi) - (b * xi)) + b) + s) / (a * b))
  | .m2 => (xi / b)
  | .m3 => ((((((-a) * xi) + a) - (b * xi)) + s) / (a * b))
  | .m4 => ((2 * (s ^ 2)) / (a * b))
  | .m5 => ((-(((-a) + s) ^ 2)) / (a * b))
  | .m6 => ((-(((-b) + s) ^ 2)) / (a * b))
  | .m7 => ((-((((((a ^ 2) * (xi ^ 2)) - (((2 * a) * s) * xi)) + ((b ^ 2) * (xi ^ 2))) - (((2 * b) * s) * xi)) + (2 * (s ^ 2)))) / (a * b))
  | .m8 => (((((((a ^ 2) - (((2 * a) * b) * xi)) - ((2 * a) * s)) + ((b ^ 2) * (xi ^ 2))) - (((2 * b) * s) * xi)) + (s ^ 2)) / (a * b))
  | .m9 => ((((((((a ^ 2) * (xi ^ 2)) - (((2 * a) * b) * xi)) - (((2 * a) * s) * xi)) + (b ^ 2)) - ((2 * b) * s)) + (s ^ 2)) / (a * b))

def pairVectorBubble (a b s rho xi : K) : PairMaster → K
  | .m0 => ((-xi) / a)
  | .m1 => ((xi - 1) / a)
  | .m2 => ((-xi) / b)
  | .m3 => ((xi - 1) / b)
  | .m4 => ((-(s ^ 2)) / (a * b))
  | .m5 => ((((-a) + s) ^ 2) / (a * b))
  | .m6 => ((((-b) + s) ^ 2) / (a * b))
  | .m7 => ((((((-a) * xi) - (b * xi)) + s) ^ 2) / (a * b))
  | .m8 => ((-((((((a ^ 2) - (((2 * a) * b) * xi)) - ((2 * a) * s)) + ((b ^ 2) * (xi ^ 2))) - (((2 * b) * s) * xi)) + (s ^ 2))) / (a * b))
  | .m9 => ((-(((((((a ^ 2) * (xi ^ 2)) - (((2 * a) * b) * xi)) - (((2 * a) * s) * xi)) + (b ^ 2)) - ((2 * b) * s)) + (s ^ 2))) / (a * b))

def pairGhost (a b s rho xi : K) : PairMaster → K
  | .m0 => 0
  | .m1 => 0
  | .m2 => 0
  | .m3 => 0
  | .m4 => 0
  | .m5 => 0
  | .m6 => 0
  | .m7 => ((-2) * (xi ^ 2))
  | .m8 => 0
  | .m9 => 0

def pairVectorSeagull (a b s rho xi : K) : PairMaster → K
  | .m0 => 0
  | .m1 => (xi / b)
  | .m2 => 0
  | .m3 => (xi / a)
  | .m4 => 0
  | .m5 => 0
  | .m6 => 0
  | .m7 => 0
  | .m8 => 0
  | .m9 => 0

def pairStationary (a b s rho xi : K) : PairMaster → K
  | .m0 => 0
  | .m1 => ((-rho) / (a * b))
  | .m2 => 0
  | .m3 => ((-rho) / (a * b))
  | .m4 => 0
  | .m5 => 0
  | .m6 => 0
  | .m7 => 0
  | .m8 => 0
  | .m9 => 0

def pairCoefficient (a b s rho xi : K) (m : PairMaster) : K :=
  pairScalarBubble a b s rho xi m + pairMixed a b s rho xi m + pairVectorBubble a b s rho xi m + pairGhost a b s rho xi m + pairVectorSeagull a b s rho xi m + pairStationary a b s rho xi m

def pairFactor (a b s rho xi : K) : PairMaster → K
  | .m0 => 0
  | .m1 => (1 / (a * b))
  | .m2 => 0
  | .m3 => (1 / (a * b))
  | .m4 => ((rho + s) / (a * b))
  | .m5 => 0
  | .m6 => 0
  | .m7 => (((-rho) - s) / (a * b))
  | .m8 => 0
  | .m9 => 0

theorem pair_factorization (a b s rho xi : K) (ha : a ≠ 0) (hb : b ≠ 0) (m : PairMaster) :
    pairCoefficient a b s rho xi m = (s-rho) * pairFactor a b s rho xi m := by
  cases m <;> simp only [pairCoefficient, pairFactor, pairScalarBubble, pairMixed, pairVectorBubble, pairGhost, pairVectorSeagull, pairStationary] <;>
    field_simp [ha, hb] <;> ring

theorem pair_on_shell (a b s rho xi : K) (ha : a ≠ 0) (hb : b ≠ 0) (hs : s = rho) (m : PairMaster) :
    pairCoefficient a b s rho xi m = 0 := by
  rw [pair_factorization a b s rho xi ha hb m, hs]
  simp

def pairAmplitude (a b s rho xi : K) (master : PairMaster → K) : K :=
  ∑ m, pairCoefficient a b s rho xi m * master m

theorem pair_amplitude_on_shell (a b s rho xi : K) (ha : a ≠ 0) (hb : b ≠ 0) (hs : s = rho) (master : PairMaster → K) :
    pairAmplitude a b s rho xi master = 0 := by
  simp [pairAmplitude, pair_on_shell a b s rho xi ha hb hs]

theorem missing_ghost (a b s rho xi : K) (ha : a ≠ 0) (hb : b ≠ 0) (hs : s = rho) :
    pairCoefficient a b s rho xi .m7 - 1 * pairGhost a b s rho xi .m7 = 2*xi^2 := by
  rw [pair_on_shell a b s rho xi ha hb hs]
  simp [pairGhost] <;> ring

theorem wrong_ghost_sign (a b s rho xi : K) (ha : a ≠ 0) (hb : b ≠ 0) (hs : s = rho) :
    pairCoefficient a b s rho xi .m7 - 2 * pairGhost a b s rho xi .m7 = 4*xi^2 := by
  rw [pair_on_shell a b s rho xi ha hb hs]
  simp [pairGhost] <;> ring

theorem missing_ghost_nonzero :
    pairCoefficient (2:ℚ) 3 5 5 1 .m7 - pairGhost 2 3 5 5 1 .m7 ≠ 0 := by
  norm_num [pairCoefficient, pairScalarBubble, pairMixed, pairVectorBubble, pairGhost, pairVectorSeagull, pairStationary]

-- Ward and projected-stationarity relations are physical hypotheses, not Lean action theorems.
theorem stationary_residual (a ell r k q sigma : K) (ha : a ≠ 0)
    (hq : a*q - 2*ell = -r) (hsigma : a*sigma = r-k) :
    q + sigma - 2*ell/a = -k/a := by
  field_simp [ha]
  linear_combination hq + hsigma

def compatibilityResidual (kappa master pi : K) : K := -kappa * master / (32*pi^2)

theorem unnormalized_compatibility (a ell r k q sigma master : K) (ha : a ≠ 0)
    (hq : a*q - 2*ell = -r) (hsigma : a*sigma = r-k) :
    (q + sigma - 2*ell/a) * master = -(k/a) * master := by
  rw [stationary_residual a ell r k q sigma ha hq hsigma]
  ring

theorem normalized_compatibility (a ell r k q sigma master pi : K) (ha : a ≠ 0)
    (hq : a*q - 2*ell = -r) (hsigma : a*sigma = r-k) :
    (q + sigma - 2*ell/a)*master/(32*pi^2) = compatibilityResidual (k/a) master pi := by
  rw [unnormalized_compatibility a ell r k q sigma master ha hq hsigma]
  rfl

theorem compatibility_nonzero (kappa master pi : K) (hk : kappa ≠ 0)
    (hm : master ≠ 0) (hp : pi ≠ 0) : compatibilityResidual kappa master pi ≠ 0 := by
  exact div_ne_zero (mul_ne_zero (neg_ne_zero.mpr hk) hm) (mul_ne_zero (by norm_num) (pow_ne_zero 2 hp))

theorem compatibility_witness : compatibilityResidual (1:ℚ) 1 1 = -1/32 := by
  norm_num [compatibilityResidual]

theorem finite_compatibility_sum {ι : Type*} (indices : Finset ι)
    (kappa master : ι → K) (pi : K) :
    (∑ i ∈ indices, compatibilityResidual (kappa i) (master i) pi) =
      -(∑ i ∈ indices, kappa i * master i) / (32*pi^2) := by
  simp only [compatibilityResidual, neg_mul, Finset.sum_div, Finset.sum_neg_distrib]

end Rxi

#print axioms Rxi.physical_factorization
#print axioms Rxi.physical_on_shell
#print axioms Rxi.physical_amplitude_on_shell
#print axioms Rxi.off_shell_nonzero
#print axioms Rxi.pair_factorization
#print axioms Rxi.pair_on_shell
#print axioms Rxi.pair_amplitude_on_shell
#print axioms Rxi.missing_ghost
#print axioms Rxi.wrong_ghost_sign
#print axioms Rxi.missing_ghost_nonzero
#print axioms Rxi.stationary_residual
#print axioms Rxi.unnormalized_compatibility
#print axioms Rxi.normalized_compatibility
#print axioms Rxi.compatibility_nonzero
#print axioms Rxi.compatibility_witness
#print axioms Rxi.finite_compatibility_sum
