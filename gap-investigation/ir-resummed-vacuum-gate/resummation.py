"""Order-one matched Gaussian soft functional, plus exact Phi-sector IR test.
No claim that this partial resummation is the complete two-loop effective action.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import sys,json,hashlib,importlib.util
from pathlib import Path
from fractions import Fraction
from decimal import Decimal,localcontext
import numpy as np
HERE=Path(__file__).resolve().parent

def gaussian_soft(mass_squared,mu_squared):
 """The hard+soft matching formula already cancels the original soft trace.
 Evaluating its separate subtraction at negative tree G is neither necessary
 nor permissible here. Exactly zero eigenvalues use the analytic f(0)=0 limit.
 """
 vals=np.asarray(mass_squared,dtype=float)
 if mu_squared<=0 or np.any(vals<0):raise ValueError('outside real Gaussian domain; not clipped')
 nz=vals!=0
 return float(np.sum(vals[nz]**2*(np.log(vals[nz]/mu_squared)-1.5))/(64*np.pi**2))

def run():
 p=HERE.parent/'shifted-vacuum-gate/calculation.py'
 spec=importlib.util.spec_from_file_location('shifted_obstruction',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 x,B,c,R,T,si,a=m.setup();ug,s,vg=np.linalg.svd((R@x).T,full_matrices=False);G=ug[:,:67]
 radial=np.eye(188)[:,186];phase=np.eye(188)[:,187]
 gauge_error=float(np.linalg.norm(G@G.T@phase-phase));assert gauge_error<1e-12
 J=B@x;dJ=B@radial;dH=2*(dJ.T@J+J.T@dJ+np.einsum('r,rij->ij',J@radial,B))
 dg=G.T@dH@G
 trace_square=float(np.trace(dg@dg));assert abs(trace_square-8)<1e-10
 # Exact algebra: Vphi/epsilon=(rho^2+chi^2-2)^2/4,
 # H_chichi(rho,0)=rho^2-2 and rho0^2=2, so (dH/drho)^2=4*rho0^2=8.
 exact_square=Fraction(4)*Fraction(2);assert exact_square==8
 # The Phi-phase tadpole follows a Ward identity; it is not a physical soft scalar.
 # F(rho)=(rho^2-2) is a mass-squared eigenvalue; the one-sided second
 # derivative of F^2(log(F/mu^2)-3/2)/(64pi^2) has coefficient
 # F'^2/(32pi^2) multiplying log(F/mu^2), while F F'' log F -> 0.
 eps=1e-7;r=json.loads((HERE.parent/'shifted-vacuum-gate/receipt.json').read_text());ms=r['leading_angular_margins']
 mass=np.array([0.]*67+[eps**2*ms['octet']]*8+[eps**2*ms['triplet']]*3)
 value=gaussian_soft(mass,eps)
 failed=False
 try:gaussian_soft([-eps**2],eps)
 except ValueError:failed=True
 assert failed
 positive_fake=value+gaussian_soft([eps**2]*67,eps)
 assert abs(positive_fake-value)>abs(value)
 with localcontext() as ctx:
  ctx.prec=70;d=Decimal;pi=d('3.141592653589793238462643383279502884197169399375105820974944592307816406286')
  coeff=d(1)/(4*pi*pi)
  logs=[{'eta':v,'log_curvature_over_epsilon_squared':str(coeff*d(v).ln())} for v in ('1e-4','1e-8','1e-16','1e-32')]
 return {'passed':True,'claim_boundary':'Explicit Phi-phase non-C2 Gaussian ring obstruction and correctly subtracted one-loop matched soft value, not full resummed vacuum.','pure_Phi_phase_gauge_projector_error':gauge_error,'Phi_radial_Goldstone_derivative_trace_square':trace_square,'exact_trace_square':str(exact_square),'coefficient_of_epsilon_squared_log_eta':'1/(4*pi^2)','regulator_scan':logs,'one_loop_matched_soft_value':value,'negative_mass_rejected':failed,'spurious_67_positive_Goldstones_value':positive_fake,'spurious_Goldstones_change':positive_fake-value,'source_hashes':{str(q):hashlib.sha256(q.read_bytes()).hexdigest() for q in (Path(__file__),p,HERE.parent/'shifted-vacuum-gate/receipt.json')}}
if __name__=='__main__':
 p=HERE/'resummation-receipt.json'
 if '--create' not in sys.argv:
  old=json.loads(p.read_text())
  for q,h in old['source_hashes'].items():assert hashlib.sha256(Path(q).read_bytes()).hexdigest()==h
 out=run()
 if '--create' in sys.argv:
  with p.open('x') as f:json.dump(out,f,indent=2)
 else:assert old==out
 print(json.dumps(out,indent=2))
