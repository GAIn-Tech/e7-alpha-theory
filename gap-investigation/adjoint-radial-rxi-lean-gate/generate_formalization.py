"""Translate the saved source coefficient table, without changing its receipts."""
from pathlib import Path
import json, ast, hashlib
import sympy as S
P=Path(__file__).resolve().parent
SOURCE=P.parent/'adjoint-radial-rxi-identity-gate'

def lean(expr):
 def go(n):
  if isinstance(n,ast.Expression):return go(n.body)
  if isinstance(n,ast.Name):return n.id
  if isinstance(n,ast.Constant):return str(n.value)
  if isinstance(n,ast.UnaryOp):return '(-'+go(n.operand)+')'
  if isinstance(n,ast.BinOp):return '('+go(n.left)+' '+{ast.Add:'+',ast.Sub:'-',ast.Mult:'*',ast.Div:'/',ast.Pow:'^'}[type(n.op)]+' '+go(n.right)+')'
  raise ValueError(ast.dump(n))
 return go(ast.parse(str(expr),mode='eval'))

def generate():
 r=json.loads((SOURCE/'symbolic_receipt.json').read_text())
 text=['import Mathlib.Tactic.FieldSimp','import Mathlib.Tactic.Ring','import Mathlib.Tactic.NormNum','import Mathlib.Tactic.LinearCombination','import Mathlib.Data.Fintype.Basic','import Mathlib.Algebra.BigOperators.Group.Finset.Basic','', '-- Generated from immutable saved channel coefficient tables; no zero-sum premise.', 'namespace Rxi','variable {K : Type*} [Field K] [CharZero K]','']
 names=[]
 for label,key,off,params in [('Physical','physical_channels','physical_off_shell','a t s rho xi'),('Pair','pair_channels','pair_off_shell','a b s rho xi')]:
  masters=sorted({m for d in r[key].values() for m in d})
  enum=label+'Master'; enum_names={m:'m'+str(i) for i,m in enumerate(masters)}
  text += ['inductive '+enum+' where']+['  | '+enum_names[m]+' -- '+m for m in masters]+['  deriving DecidableEq, Fintype','']
  ds=[]
  for channel,co in r[key].items():
   name=label.lower()+''.join(x.title() for x in channel.split('_'));ds.append(name)
   text+=['def '+name+' ('+params+' : K) : '+enum+' → K']+['  | .'+enum_names[m]+' => '+lean(co.get(m,'0')) for m in masters]+['']
  stat={'A(a*xi)':'2*(t-rho)/a'} if label=='Physical' else {'A(a*xi)':'-rho/(a*b)','A(b*xi)':'-rho/(a*b)'}
  name=label.lower()+'Stationary';ds.append(name)
  text+=['def '+name+' ('+params+' : K) : '+enum+' → K']+['  | .'+enum_names[m]+' => '+lean(stat.get(m,'0')) for m in masters]+['']
  total=label.lower()+'Coefficient';factor=label.lower()+'Factor'
  text+=['def '+total+' ('+params+' : K) (m : '+enum+') : K :=','  '+' + '.join(n+' '+params+' m' for n in ds),'']
  text+=['def '+factor+' ('+params+' : K) : '+enum+' → K']+['  | .'+enum_names[m]+' => '+lean(S.cancel(S.sympify(r[off].get(m,'0'))/(S.Symbol('s')-S.Symbol('rho')))) for m in masters]+['']
  theorem=label.lower()+'_factorization';names.append(theorem)
  hypotheses='(ha : a ≠ 0)'+(' (hb : b ≠ 0)' if label=='Pair' else '')
  hz='ha, hb' if label=='Pair' else 'ha'
  text+=['theorem '+theorem+' ('+params+' : K) '+hypotheses+' (m : '+enum+') :', '    '+total+' '+params+' m = (s-rho) * '+factor+' '+params+' m := by', '  cases m <;> simp only ['+', '.join([total,factor]+ds)+'] <;>', '    field_simp ['+hz+'] <;> ring','']
  theorem=label.lower()+'_on_shell';names.append(theorem)
  text+=['theorem '+theorem+' ('+params+' : K) '+hypotheses+' (hs : s = rho) (m : '+enum+') :','    '+total+' '+params+' m = 0 := by','  rw ['+label.lower()+'_factorization '+params+' ha'+(' hb' if label=='Pair' else '')+' m, hs]','  simp','']
  ampl=label.lower()+'Amplitude'
  text+=['def '+ampl+' ('+params+' : K) (master : '+enum+' → K) : K :=','  ∑ m, '+total+' '+params+' m * master m','']
  theorem=label.lower()+'_amplitude_on_shell';names.append(theorem)
  text+=['theorem '+theorem+' ('+params+' : K) '+hypotheses+' (hs : s = rho) (master : '+enum+' → K) :','    '+ampl+' '+params+' master = 0 := by','  simp ['+ampl+', '+label.lower()+'_on_shell '+params+' ha'+(' hb' if label=='Pair' else '')+' hs]','']
  if label=='Pair':
   im=enum_names['I(a*xi, b*xi)']
   for name,mult in [('missing_ghost',1),('wrong_ghost_sign',2)]:
    names.append(name)
    text+=['theorem '+name+' ('+params+' : K) '+hypotheses+' (hs : s = rho) :','    '+total+' '+params+' .'+im+' - '+str(mult)+' * pairGhost '+params+' .'+im+' = '+str(2*mult)+'*xi^2 := by','  rw [pair_on_shell '+params+' ha hb hs]','  simp [pairGhost] <;> ring','']
   text+=['theorem missing_ghost_nonzero :','    pairCoefficient (2:ℚ) 3 5 5 1 .'+im+' - pairGhost 2 3 5 5 1 .'+im+' ≠ 0 := by','  norm_num [pairCoefficient, '+', '.join(ds)+']','']
   names.append('missing_ghost_nonzero')
  if label=='Physical':
   am=enum_names['A(a*xi)']
   text+=['theorem off_shell_nonzero : physicalCoefficient (2:ℚ) 3 7 5 1 .'+am+' = 2 := by','  norm_num [physicalCoefficient, '+', '.join(ds)+']','']
   names.append('off_shell_nonzero')
 text+=['-- Ward and projected-stationarity relations are physical hypotheses, not Lean action theorems.',
 'theorem stationary_residual (a ell r k q sigma : K) (ha : a ≠ 0)',
 '    (hq : a*q - 2*ell = -r) (hsigma : a*sigma = r-k) :',
 '    q + sigma - 2*ell/a = -k/a := by',
 '  field_simp [ha]',
 '  linear_combination hq + hsigma','',
 'def compatibilityResidual (kappa master pi : K) : K := -kappa * master / (32*pi^2)','',
 'theorem unnormalized_compatibility (a ell r k q sigma master : K) (ha : a ≠ 0)',
 '    (hq : a*q - 2*ell = -r) (hsigma : a*sigma = r-k) :',
 '    (q + sigma - 2*ell/a) * master = -(k/a) * master := by',
 '  rw [stationary_residual a ell r k q sigma ha hq hsigma]',
 '  ring','',
 'theorem normalized_compatibility (a ell r k q sigma master pi : K) (ha : a ≠ 0)',
 '    (hq : a*q - 2*ell = -r) (hsigma : a*sigma = r-k) :',
 '    (q + sigma - 2*ell/a)*master/(32*pi^2) = compatibilityResidual (k/a) master pi := by',
 '  rw [unnormalized_compatibility a ell r k q sigma master ha hq hsigma]',
 '  rfl','',
 'theorem compatibility_nonzero (kappa master pi : K) (hk : kappa ≠ 0)',
 '    (hm : master ≠ 0) (hp : pi ≠ 0) : compatibilityResidual kappa master pi ≠ 0 := by',
 '  exact div_ne_zero (mul_ne_zero (neg_ne_zero.mpr hk) hm) (mul_ne_zero (by norm_num) (pow_ne_zero 2 hp))','',
 'theorem compatibility_witness : compatibilityResidual (1:ℚ) 1 1 = -1/32 := by',
 '  norm_num [compatibilityResidual]','',
 'theorem finite_compatibility_sum {ι : Type*} (indices : Finset ι)',
 '    (kappa master : ι → K) (pi : K) :',
 '    (∑ i ∈ indices, compatibilityResidual (kappa i) (master i) pi) =',
 '      -(∑ i ∈ indices, kappa i * master i) / (32*pi^2) := by',
 '  simp only [compatibilityResidual, neg_mul, Finset.sum_div, Finset.sum_neg_distrib]','',
 'end Rxi','']
 names+=['stationary_residual','unnormalized_compatibility','normalized_compatibility','compatibility_nonzero','compatibility_witness','finite_compatibility_sum']
 text+=['#print axioms Rxi.'+n for n in names]
 (P/'Formalization.lean').write_text('\n'.join(text)+'\n',encoding='utf-8')
 (P/'Challenge.lean').write_text('import Formalization\n\n'+'\n'.join('#check Rxi.'+n for n in names)+'\n',encoding='utf-8')
 (P/'coefficient_translation.json').write_text(json.dumps({'input_sha256':hashlib.sha256((SOURCE/'symbolic_receipt.json').read_bytes()).hexdigest(),'declarations':names,'translation':'All channel coefficients are syntactic arithmetic translations; factor targets are separately reduced with SymPy. Lean proves equality from unreduced channel sums.'},indent=2))
if __name__=='__main__':generate()
