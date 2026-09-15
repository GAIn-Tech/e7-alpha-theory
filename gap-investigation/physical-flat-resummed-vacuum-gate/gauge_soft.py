"""Source-derived finite soft scalar/massless-vector on-shell matrix, Landau MSbar."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import ast,json,sys,hashlib
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'adjoint-radial-mixed-pole-gate/finite_momentum.py'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def compute():
 # Import only the actual source master definitions, not radial data or its totals.
 tree=ast.parse(SOURCE.read_text());keep=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ['A','B','K']]
 env={'np':np};exec(compile(ast.Module(body=keep,type_ignores=[]),str(SOURCE),'exec'),env)
 d=json.loads((HERE/'matrices.json').read_text());M=np.array(d['M1']);C=np.array(d['unbroken_Casimir']);lam,U=np.linalg.eigh(M);c=np.diag(U.T@C@U)
 assert np.max(abs(C@M-M@C))<1e-9
 assert max(abs(c[:8]-3))<1e-8 and max(abs(c[8:]-2))<1e-8
 rows=[];mats=[]
 for eps in [1e-7,1e-5,1e-3]:
  coeff=c*lam*(7-3*np.log(eps*lam))/(16*np.pi**2)
  vals=[]
  for mass in [lam[0],lam[-1]]:
   x=eps*mass;s=x
   inherited=env['K'](x,0.,s)
   # Tensor-first integral t=exp(-u); omitted u>60 tail < 1e-21 in bracket.
   nodes,w=np.polynomial.legendre.leggauss(256);u=30*(nodes+1)
   independent=-6*x*30*np.sum(w*(1-np.exp(-u))*(np.log(x)-2*u)*np.exp(-u))-2*x
   closed=x*(7-3*np.log(x))
   assert abs(inherited-closed)<1e-12 and abs(float(independent)-closed)<1e-12
   vals.append({'mass2_over_epsilonM2':x,'source_kernel':inherited.real,'transformed_Gauss_kernel':float(independent),'imaginary':inherited.imag})
  mat=(U*coeff)@U.T
  mats.append({'epsilon':eps,'matrix_over_epsilon3M2':mat.tolist()})
  rows.append({'epsilon':eps,'octet_coefficient_over_epsilon3M2':float(np.mean(coeff[:8])),'triplet_coefficient_over_epsilon3M2':float(np.mean(coeff[8:])),'relative_octet_correction':float(eps*coeff[0]/lam[0]),'relative_triplet_correction':float(eps*coeff[-1]/lam[-1]),'checks':vals,'drop_evanescent_coefficient_change_norm':float(np.linalg.norm(2*c*lam/(16*np.pi**2)))})
 # Its zero-momentum potential contribution vanishes: K(x,0,0)=0.
 assert abs(env['K'](0.25,0.,0.))<1e-14
 logmatrix=-3*C@M/(16*np.pi**2)
 out={'passed':True,'claim_boundary':'Finite resummed physical-soft/massless-unbroken-vector derivative bubble matrix at each octet/triplet leading shell; not complete NLO pole or full quantum vacuum.','prescription':'inverse propagator s-m2-Pi; Q2=epsilon M2; strict Landau; internal physical scalar mass epsilon2 lambda M2, never a Goldstone regulator','rows':rows,'log_epsilon_coefficient_eigenvalues':np.linalg.eigvalsh(logmatrix).tolist(),'source_hashes':{str(p):sha(p) for p in [Path(__file__),SOURCE,HERE/'matrices.json',HERE/'receipt.json']}}
 return out,mats
if __name__=='__main__':
 p=HERE/'gauge-soft-receipt.json';q=HERE/'gauge-soft-matrices.json'
 if '--create' not in sys.argv:
  old=json.loads(p.read_text());oldm=json.loads(q.read_text())
  for f,h in old['source_hashes'].items():assert sha(Path(f))==h
 out,m=compute()
 if '--create' in sys.argv:
  with p.open('x') as f:json.dump(out,f,indent=2)
  with q.open('x') as f:json.dump(m,f)
 else:assert old==out and oldm==m
 print(json.dumps(out,indent=2))
