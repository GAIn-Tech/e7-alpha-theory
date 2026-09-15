"""Leading physical-soft Gaussian tadpole; not missing hard two-loop matching."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import json,sys,hashlib,importlib.util
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent

def run():
 p=HERE.parent/'shifted-vacuum-gate/calculation.py';s=importlib.util.spec_from_file_location('shifted_soft_tadpole',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
 x,B,c,R,T,si,a=m.setup();_,g,H,J,f=m.tree(x,B,c)
 data=json.loads((HERE/'projected-tensors.json').read_text());F=np.array(data['basis_F']);FF=np.array(data['sum_over_epsilon_squared'])[67:,67:];z,U=np.linalg.eigh(FF)
 pred=json.loads((HERE.parent/'shifted-vacuum-gate/receipt.json').read_text());mass=np.array([pred['leading_angular_margins']['octet']]*8+[pred['leading_angular_margins']['triplet']]*3)
 assert np.max(abs(z-mass))<1e-7
 modes=F@U;Z,inv,_=m.exact_singlet_inverse(x,B,c,T,si,a)
 results=[]
 for eps in (1e-7,5e-8,2.5e-8):
  weights=mass*(np.log(eps*mass)-1);W=(modes*weights)@modes.T
  coeff=(4*np.einsum('rij,rj->i',B,J@W)+2*J.T@np.einsum('ij,rji->r',W,B))/(32*np.pi**2)
  singlet_coordinates=-eps**2*inv@Z.T@coeff
  dx=Z@singlet_coordinates
  remainder=eps*H@dx+eps**3*coeff
  error=float(np.linalg.norm(remainder)/np.linalg.norm(eps**3*coeff));assert error<1e-9
  assert np.linalg.norm(F.T@coeff)<1e-7
  results.append({'epsilon':eps,'leading_physical_soft_tadpole_norm':float(eps**3*np.linalg.norm(coeff)),'log_soft_singlet_shift_coordinates':singlet_coordinates.tolist(),'canonical_soft_shift_norm':float(np.linalg.norm(dx)),'linear_tadpole_cancellation_relative_error':error,'soft_gradient_canonical':(eps**3*coeff).tolist()})
 return {'passed':True,'claim_boundary':'Calculated leading physical-soft Gaussian epsilon^3 log(epsilon) tadpole and linear compensating epsilon^2 log(epsilon) singlet displacement only. Missing hard two-loop tadpoles and soft Ward reclosure prevent a full stationary-solution claim.','mass_input':'High-precision predecessor m8,m3; eigenvectors independently computed full 11x11 block.','results':results,'source_hashes':{str(q):hashlib.sha256(q.read_bytes()).hexdigest() for q in (Path(__file__),p,HERE/'projected-tensors.json',HERE.parent/'shifted-vacuum-gate/receipt.json')}}
if __name__=='__main__':
 p=HERE/'soft-tadpole-receipt.json'
 if '--create' not in sys.argv:
  old=json.loads(p.read_text())
  for q,h in old['source_hashes'].items():assert hashlib.sha256(Path(q).read_bytes()).hexdigest()==h
 out=run()
 if '--create' in sys.argv:
  with p.open('x') as f:json.dump(out,f,indent=2)
 else:assert old==out
 print(json.dumps({**out,'results':[{k:v for k,v in r.items() if k!='soft_gradient_canonical'} for r in out['results']]},indent=2))
