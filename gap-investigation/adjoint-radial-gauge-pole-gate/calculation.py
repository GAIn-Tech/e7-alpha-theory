"""Gauge-sector data and zero-momentum Landau-gauge gate for adjoint radial v_A.
This deliberately does not label the finite-p result complete: the transverse VV and
mixed scalar-vector bubbles are left explicit. M=1, Q^2=epsilon M^2.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'; os.environ['OMP_NUM_THREADS']='1'
import json,hashlib,importlib.util,sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent; ROOT=HERE.parent

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def divided_fp(m):
 """Divided difference of f'(z), f=z^2(log z-5/6), with exact zero limits."""
 fp=np.zeros_like(m); pos=m>1e-10; fp[pos]=m[pos]*(2*np.log(m[pos])-2/3)
 out=np.zeros((len(m),len(m)))
 for i,a in enumerate(m):
  for j,b in enumerate(m):
   if a>1e-10 and b>1e-10:
    out[i,j]=2*np.log(a)+4/3 if abs(a-b)<1e-8*max(1,a,b) else (fp[i]-fp[j])/(a-b)
   elif a>1e-10: out[i,j]=fp[i]/a
   elif b>1e-10: out[i,j]=fp[j]/b
   else: out[i,j]=0.0
 return fp,out

def compute():
 M=load(ROOT/'shifted-vacuum-gate/calculation.py','shift_gauge'); IR=load(ROOT/'ir-resummed-vacuum-gate/calculation.py','ir_gauge');IR.M=M
 x,B,c,R,T,si,a=M.setup();_,grad,H,J,f=M.tree(x,B,c)
 assert np.linalg.norm(f)<1e-10 and np.linalg.norm(grad)<1e-8
 v=np.zeros(188);v[108:186]=x[108:186]/np.linalg.norm(x[108:186])
 assert np.linalg.norm(H@v-4320*v)<1e-8
 K=R@x; dK=R@v; MV=K@K.T; D=dK@K.T+K@dK.T; Q=2*dK@dK.T
 mass,U=np.linalg.eigh((MV+MV.T)/2); De=U.T@D@U; Qe=U.T@Q@U
 mass[np.abs(mass)<1e-10]=0
 assert sum(mass>1e-8)==67 and sum(mass==0)==12
 # Unbroken vectors remain identically massless along this gauge-singlet radial line.
 iz=np.where(mass==0)[0]; zero_D=float(np.linalg.norm(De[np.ix_(iz,iz)])); zero_Q=float(np.linalg.norm(Qe[np.ix_(iz,iz)]))
 assert zero_D<1e-9 and zero_Q<1e-9
 fp,L=divided_fp(mass)
 hess_cw=3*(float(fp@np.diag(Qe))+float(np.sum(L*De*De)))/(64*np.pi**2)
 # Analytic directional finite difference of the full vector CW determinant.
 def vcw(t):
  Ky=R@(x+t*v); z=np.linalg.eigvalsh(Ky@Ky.T); z=z[z>1e-10]
  return 3*np.sum(z*z*(np.log(z)-5/6))/(64*np.pi**2)
 fd=[]
 for h in (2e-4,1e-4,5e-5): fd.append({'h':h,'second':float((vcw(h)-2*vcw(0)+vcw(-h))/h**2)})
 assert abs(fd[-1]['second']-hess_cw)/max(1,abs(hess_cw))<2e-5
 # Vector tadpole and induced tree shift, exactly predecessor convention.
 _,Wv,_=M.spectral(MV,5/6); gv=2*np.einsum('ai,aij->j',Wv@K,R); gvec=3*gv/(64*np.pi**2)
 stab=M.null((R@x).T);smR=np.einsum('ak,aij->kij',stab,R);Sphys=M.null(np.concatenate((smR.reshape(-1,188),R@x),axis=0))
 delta=-Sphys@np.linalg.solve(Sphys.T@H@Sphys,Sphys.T@gvec)
 shift=float(v@IR.tree_dH(x,delta,B)@v); total0=shift+hess_cw
 # Dimensional UV local coefficient of the transverse determinant Hessian.
 uv=3*(float(np.diag(Qe)@mass)+float(np.sum(De*De)))/(64*np.pi**2)
 # Basis rotation test within every degenerate vector shell.
 rng=np.random.default_rng(914);Ur=U.copy()
 for val in np.unique(np.round(mass,7)):
  ids=np.where(abs(mass-val)<1e-7)[0]
  if len(ids)>1: Ur[:,ids]=U[:,ids]@np.linalg.qr(rng.normal(size=(len(ids),len(ids))))[0]
 Dr=Ur.T@D@Ur;Qr=Ur.T@Q@Ur; fpr,Lr=divided_fp(mass)
 hr=3*(float(fpr@np.diag(Qr))+float(np.sum(Lr*Dr*Dr)))/(64*np.pi**2)
 # Landau FP scalar vertices are proportional to xi and vanish at xi=0.
 out={'passed':True,'claim_boundary':'Derived all 79 vector masses and vA-vector-vector/seagull couplings from the canonical covariant kinetic term and completed the Landau-gauge zero-momentum transverse-vector determinant, vector tadpole shift, and vanishing xi=0 ghost vertex. Finite-p transverse VV, mixed scalar-vector bubbles, external mixing, and xi cancellation remain; this is not a pole contribution or gauge-independent mass.',
 'tree_shell_over_epsilonM2':4320.0,'dimensions':{'vectors':79,'massive':67,'massless_unbroken':12},
 'couplings':{'mass_matrix_definition':'M_V^2=(R x)(R x)^T','D_v_definition':'(R v)(R x)^T+(R x)(R v)^T','Q_vv_definition':'2(R v)(R v)^T','D_frobenius_squared':float(np.sum(De*De)),'Q_mass_contraction':float(np.diag(Qe)@mass),'nonzero_D_entries_abs_gt_1e-10':int(np.sum(abs(De)>1e-10)),'unbroken_D_block_norm':zero_D,'unbroken_Q_block_norm':zero_Q},
 'zero_momentum':{'vector_CW_Hessian':hess_cw,'vector_stationary_shift':shift,'sum':total0,'finite_difference':fd,'MSbar_vector_UV_local_coefficient_removed':uv},
 'ghost':{'xi':0,'direct_vA_ghost_antighost_vertex':0.0,'reason':'background-Rxi FP scalar vertex is proportional to xi; strict Landau limit'},
 'checks':{'degenerate_basis_rotation_abs_difference':abs(hr-hess_cw),'negative_omit_stationary_shift_change':abs(shift),'negative_drop_seagull_change':abs(3*float(fp@np.diag(Qe))/(64*np.pi**2))},
 'remaining':['finite-p transverse vector-vector bubble at p2=4320 epsilon M2','scalar-vector mixed derivative bubbles from canonical kinetic term','external scalar-vector pole determinant mixing','general-xi Goldstone/ghost/longitudinal cancellation'],'source_hashes':{}}
 return out
if __name__=='__main__':
 out=compute(); src=[Path(__file__),ROOT/'shifted-vacuum-gate/calculation.py',ROOT/'shifted-vacuum-gate/receipt.json',ROOT/'ir-resummed-vacuum-gate/calculation.py',ROOT/'goldstone-pole-matching-gate/calculation.py',ROOT/'adjoint-radial-pole-gate/calculation.py']
 out['source_hashes']={str(p):sha(p) for p in src}; p=HERE/'receipt.json'
 if '--create' in sys.argv:
  with p.open('x') as f:json.dump(out,f,indent=2)
 else: assert json.loads(p.read_text())==out
 print(json.dumps(out,indent=2))

