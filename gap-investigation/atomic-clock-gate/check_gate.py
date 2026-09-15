"""Conditional exact-rational SMT gate; not atomic-structure or E7 formalization."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,sys
import z3
P=Path(__file__).resolve().parent

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def numeric():
 obs=F('137.035999177'); u=F('0.000000021'); cand=F(137)+F(9,250)
 residual=cand-obs; delta_alpha=obs/cand-1
 return {'codata_inverse':str(obs),'quoted_u':str(u),'candidate_inverse':str(cand),'inverse_residual':str(residual),'residual_in_quoted_u':str(residual/u),'exact_fractional_alpha_difference':str(delta_alpha),'fractional_alpha_decimal':float(delta_alpha),'illustrative_Al_over_Hg_linear_shift':str(F(16,5)*delta_alpha),'linear_shift_decimal':float(F(16,5)*delta_alpha),'note':'Linear shift is conditional on rounded K difference 3.2 and frozen nuisances, not a predicted absolute ratio or exclusion significance.'}
def cases():
 a,m,g,b,d=z3.Reals('a m g b d'); aa,mm,gg,bb=z3.Reals('aa mm gg bb'); r,h=z3.Reals('r h'); k=z3.Real('k')
 # a=delta ln alpha, m=delta ln(me/mp), g=delta ln nuclear gCs.
 # Hg/Cs rounded source sensitivities: -3.2-(2+0.8)=-6.
 optical=z3.RealVal('3.2')*a; microwave=-6*a-m-g
 return [
 ('single_microwave_alpha_nonidentifiable',[microwave==0,a!=0],'sat'),
 ('same_microwave_two_alphas',[microwave==-6*aa-mm-gg,a!=aa],'sat'),
 ('optical_alpha_identifiable',[k!=0,k*a==k*aa,a!=aa],'unsat'),
 ('zero_sensitivity_not_identifiable',[k==0,k*a==k*aa,a!=aa],'sat'),
 ('two_ratios_alpha_identifiable',[optical==z3.RealVal('3.2')*aa,microwave==-6*aa-mm-gg,a!=aa],'unsat'),
 ('two_ratios_mass_nuclear_degenerate',[optical==z3.RealVal('3.2')*aa,microwave==-6*aa-mm-gg,m!=mm],'sat'),
 ('nuclear_prior_restores_mass_identifiability',[optical==z3.RealVal('3.2')*aa,microwave==-6*aa-mm-gg,g==gg,m!=mm],'unsat'),
 ('common_scale_cancels',[r+z3.RealVal('-3.2')*a-(r+z3.RealVal('2.8')*a+m+g)!=microwave],'unsat'),
 ('unknown_absolute_intercept_hides_alpha',[b+z3.RealVal('3.2')*a==bb+z3.RealVal('3.2')*aa,a!=aa],'sat'),
 ('fixed_absolute_intercept_restores_alpha',[b==bb,b+z3.RealVal('3.2')*a==bb+z3.RealVal('3.2')*aa,a!=aa],'unsat'),
 ('zero_drift_does_not_fix_boundary',[d==0,b>0,bb>0,b!=bb],'sat'),
 ('scalar_coupling_amplitude_degenerate',[a==k*d,aa==h*z3.RealVal('2')*d,k==2*h,d!=0,h!=0,a==aa,k!=h],'sat'),
 ('optical_ratio_orientation',[z3.RealVal('0')*a-z3.RealVal('-3.2')*a!=z3.RealVal('3.2')*a],'unsat')]
def build():
 rows=[]
 for name,terms,expected in cases():
  s=z3.Solver(); s.add(*terms); result=str(s.check()); assert result==expected,(name,result)
  p=P/(name+'.smt2'); p.write_text(s.to_smt2(),encoding='utf-8')
  rows.append({'name':name,'expected':expected,'result':result,'sha256':sha(p),'model':str(s.model()) if result=='sat' else None})
 sources=json.loads((P/'source-receipt.json').read_text())
 hashes={x.name:sha(x) for x in P.iterdir() if x.suffix in ('.html','.pdf','.txt','.py')}
 out={'claim_boundary':'Exact SMT identifiability checks of an explicitly assumed first-order clock response model. Not Lean-kernel proofs, not a QED or E7 derivation; rounded empirical sensitivity coefficients treated as exact within this toy response model.','z3_version':z3.get_version_string(),'cases':rows,'numeric':numeric(),'inputs':hashes,'all_passed':True}
 (P/'gate-receipt.json').write_text(json.dumps(out,indent=2),encoding='utf-8'); print(json.dumps(out,indent=2))
def verify():
 receipt=json.loads((P/'gate-receipt.json').read_text()); assert receipt['numeric']==numeric()
 for name,h in receipt['inputs'].items(): assert sha(P/name)==h,name
 replay=[]
 for c in receipt['cases']:
  p=P/(c['name']+'.smt2'); assert sha(p)==c['sha256']; s=z3.Solver(); s.from_file(str(p)); result=str(s.check()); assert result==c['expected']; replay.append({'name':c['name'],'result':result})
 assert len(replay)==len(cases())
 out={'saved_receipt_sha256':sha(P/'gate-receipt.json'),'source_hashes_verified':len(receipt['inputs']),'smt_replay':replay,'numeric_recomputed':numeric(),'passed':True}
 (P/'replay-receipt.json').write_text(json.dumps(out,indent=2),encoding='utf-8'); print(json.dumps(out,indent=2))
if __name__=='__main__': verify() if '--verify-existing' in sys.argv else build()
