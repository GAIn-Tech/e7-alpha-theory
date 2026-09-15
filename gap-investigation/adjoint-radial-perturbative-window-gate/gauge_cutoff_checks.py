"""Supplementary gauge-domain and genuinely conditional EFT cutoff tests."""
import sys,json,hashlib,importlib.util
from pathlib import Path
P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('window',P/'calculate.py');W=importlib.util.module_from_spec(spec);spec.loader.exec_module(W)
mp,np=W.mp,W.np

def compute():
 r=json.loads((P/'receipt.json').read_text());assert r['passed']
 assert W.sha(P/'calculate.py')==r['verifier_sha256']
 for p,h in r['source_hashes'].items():assert W.sha(Path(p))==h,p
 rho=W.rho;fac=32*mp.pi**2
 # Physical scalar/Goldstone identity coefficient uses physical quotient only.
 pg=[v for v in r['SV_channels'] if v['scalar_type']!='Goldstone']
 # VV vertex D_ab=2 Z_ab on this invariant radial direction; hence Z^2 = D^2/4.
 gg=r['VV_channels'];rows=[]
 land=mp.mpc(r['derivative']['total_Landau']['real'],r['derivative']['total_Landau']['imag'])
 for xi in (0,1,10,100):
  shift=mp.mpc(0)
  for c in pg:
   t,a,w=map(mp.mpf,(c['a'],c['b'],c['weight']))
   shift+=w*2/a*(W.A(xi*a)-(2*rho-2*t)*(W.I(t,xi*a,rho)-W.I(t,0,rho)))/fac
  for c in gg:
   a,b,w=map(mp.mpf,(c['a'],c['b'],c['weight']))
   shift+=w/4/(a*b)*(W.A(xi*a)+W.A(xi*b)-2*rho*(W.I(xi*a,xi*b,rho)-W.I(0,0,rho)))/fac
  thresholds=[]
  for c in pg:
   a,b=c['a'],xi*c['b'];thresholds.append({'type':'physical_G','t':a,'xi_a':b,'threshold':W.threshold(a,b),'distance':abs(4320-W.threshold(a,b))})
  for c in gg:
   a,b=xi*c['a'],xi*c['b'];thresholds.append({'type':'GG_ghost_longitudinal','xi_a':a,'xi_b':b,'threshold':W.threshold(a,b),'distance':abs(4320-W.threshold(a,b))})
  poles=[{'a':s['m2'],'xi_a':xi*s['m2'],'distance':abs(4320-xi*s['m2'])} for s in r['vector_shells'] if s['m2']>0]
  cp=land+shift
  rows.append({'xi':xi,'Pi_prime_over_epsilon_conditional':W.pack(cp),'change_from_Landau':W.pack(shift),'wavefunction_abs':float(abs(cp)),'epsilon_wavefunction_upper_tolerance_0p1':float(mp.mpf('.1')/abs(cp)),'unphysical_thresholds':thresholds,'unphysical_poles':poles,'minimum_threshold_distance':min(t['distance'] for t in thresholds),'minimum_pole_distance':min(p['distance'] for p in poles)})
 assert rows[0]['change_from_Landau']=={'real':0.,'imag':0.}
 assert abs(rows[1]['change_from_Landau']['real'])>1e-5
 # Algebraic dimension-six counterfamily, not an operator added to the action.
 # r0^2=60 M^2, V=epsilon(3r^2-180M^2)^2+c6 r^6/Lambda^2.
 from fractions import Fraction as F
 r2=F(60);rho0=F(4320)
 shift_r=-6*r2*r2/rho0
 direct=30*r2*r2/rho0
 stationary=216*r2*shift_r/rho0
 complete=direct+stationary
 assert (shift_r,direct,stationary,complete)==(F(-5),F(25),F(-15),F(10))
 tol=mp.mpf('.1');upper=mp.mpf(r['conditional_bounds'][0]['necessary_joint_upper'])
 # Requiring |delta m2_dim6|/m_tree2<tol needs epsilon>10|c6|/(tol L^2).
 cutoff_ratio_for_unit_c6=mp.sqrt(10/(tol*upper))
 negatives={
  'wrong_epsilon_order_ratio_at_1e_minus_7':float(mp.mpf('1e-7')/mp.mpf('1e-7')**2),
  'omit_stationary_shift_dimension6_relative_coefficient':float(direct),
  'correct_stationary_dimension6_relative_coefficient':float(complete),
  'xi_independent_wavefunction_rejected':rows[1]['change_from_Landau']!={'real':0.,'imag':0.},
  'epsilon1_fails_shift_tolerance':r['epsilon_diagnostic_coefficients']['relative_complex_shift']>float(tol),
  'Lambda_equals_M_unit_c6_has_no_0p1_joint_window':float(10/tol)>float(upper)
 }
 assert all(negatives[k] for k in ('xi_independent_wavefunction_rejected','epsilon1_fails_shift_tolerance','Lambda_equals_M_unit_c6_has_no_0p1_joint_window'))
 # Compare complete raw sums against quotient plus Goldstone decomposition, meaningful FP tolerance.
 th=r['support_classification']['radial_radial_soft_structural_identity_residual'];assert th<1e-8
 return {'passed':True,'claim_boundary':'Rxi derivative transfer conditional on exact master identity and floating action Ward/kernel hypotheses; dimension-six example is a counterfamily, not declared matching data.','base_receipt_sha256':W.sha(P/'receipt.json'),'verifier_sha256':W.sha(Path(__file__)),'gauge_scan':rows,'dimension6_counterfamily':{'potential':'epsilon(3 r^2-180 M^2)^2+c6 r^6/Lambda^2','delta_r_over_r':'-5(c6/epsilon)(M/Lambda)^2','relative_mass_shift_at_shifted_vacuum':'10(c6/epsilon)(M/Lambda)^2','epsilon_lower_bound_tolerance_0p1':'100 abs(c6) (M/Lambda)^2','unit_c6_minimum_Lambda_over_M_for_nonempty_0p1_window':float(cutoff_ratio_for_unit_c6),'scope':'first order in c6 M2/(epsilon Lambda2), sign-indefinite unknown c6; no c6 value asserted for actual model'},'negative_controls':negatives}
if __name__=='__main__':
 out=compute();q=P/'gauge-cutoff-receipt.json'
 if '--create' in sys.argv:
  with q.open('x') as f:json.dump(out,f,indent=2)
 else:assert out==json.loads(q.read_text()),'supplement receipt mismatch'
 print(json.dumps({k:v for k,v in out.items() if k!='gauge_scan'},indent=2))
 print(json.dumps([{k:v for k,v in r.items() if k not in ('unphysical_thresholds','unphysical_poles')} for r in out['gauge_scan']],indent=2))
