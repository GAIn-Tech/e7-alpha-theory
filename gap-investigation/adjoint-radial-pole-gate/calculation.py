"""MSbar/Landau scalar+fermion one-loop contribution to isolated adjoint radial pole.
M=1, Q^2=epsilon M^2; coefficients are divided by epsilon^2 M^2.
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

def log_integral_matrix(m,s,n=512):
 """I_ij(s), Gauss-Legendre per distinct mass pair with threshold splits."""
 z,w=np.polynomial.legendre.leggauss(n);u=(z+1)/2;w=w/2
 keys=np.where(m<1e-8,-1.0,np.round(m,8)); vals=np.unique(keys); cache={}; massval={k:(float(np.min(m)) if k==-1 else float(np.mean(m[keys==k]))) for k in vals}
 for ka in vals:
  for kb in vals:
   a,b=massval[ka],massval[kb]
   roots=np.roots([s,a-b-s,b]); points=sorted(float(r.real) for r in roots if abs(r.imag)<1e-10 and 0<r.real<1)
   cuts=[0.0]+points+[1.0]; re=im=0.0
   for lo,hi in zip(cuts,cuts[1:]):
    xx=lo+(hi-lo)*u; den=xx*a+(1-xx)*b-s*xx*(1-xx)
    re+=(hi-lo)*np.sum(w*np.log(abs(den)))
    if ((lo+hi)/2)*a+(1-(lo+hi)/2)*b-s*((lo+hi)/2)*(1-(lo+hi)/2)<0: im-=np.pi*(hi-lo)
   cache[(ka,kb)]=complex(re,im)
 return np.array([[cache[(a,b)] for b in keys] for a in keys])

def tree_tensors(M,x,B,c,v):
 J=B@x; dJ=B@v
 T=2*(dJ.T@J+J.T@dJ+np.einsum('r,rij->ij',J@v,B))
 U=4*dJ.T@dJ+2*np.einsum('r,rij->ij',np.einsum('ri,i->r',B@v,v),B)
 return (T+T.T)/2,(U+U.T)/2

def sector_tadpoles(M,x,B,c):
 _,_,H,J,_=M.tree(x,B,c); z,U=np.linalg.eigh(H); keep=z>1e-8
 fp=np.zeros_like(z);fp[keep]=z[keep]*(2*np.log(z[keep])-2);W=(U*fp)@U.T
 gs=(4*np.einsum('rij,rj->i',B,J@W)+2*J.T@np.einsum('ij,rji->r',W,B))/(64*np.pi**2)
 gf=np.zeros(188);u=x[186:]@x[186:]/2
 blocks=[]
 for mult,y in ((27,1),(1,1),(1,2),(1,3)):
  mf=y*y*u;p=mf*(2*np.log(mf)-2)
  gf[186:]-=4*mult*y*y*p*x[186:]
  blocks.append({'multiplicity_Dirac':mult,'y_over_sqrt_epsilon':y,'m2_over_epsilonM2':float(mf),'direct_vA_Yukawa':0.0})
 return gs,gf/(64*np.pi**2),blocks

def compute(n=512):
 M=load(ROOT/'shifted-vacuum-gate/calculation.py','shift_adj'); IR=load(ROOT/'ir-resummed-vacuum-gate/calculation.py','ir_adj');IR.M=M
 x,B,c,R,Trep,si,a=M.setup();_,grad,H,J,f=M.tree(x,B,c)
 assert np.linalg.norm(f)<1e-10 and np.linalg.norm(grad)<1e-8
 evals,E=np.linalg.eigh(H); v=np.zeros(188);v[108:186]=x[108:186]/np.linalg.norm(x[108:186])
 assert np.linalg.norm(H@v-4320*v)<1e-8 and sum(abs(evals-4320)<1e-7)==1
 Tv,Uv=tree_tensors(M,x,B,c,v); t=E.T@Tv@E; q=np.diag(E.T@Uv@E)
 gs,gf,fermions=sector_tadpoles(M,x,B,c)
 # Tadpole prescription: solve each sector's hard stationary displacement linearly
 # in the same invariant physical singlet space used by shifted-vacuum-gate.
 stab=M.null((R@x).T);smR=np.einsum('ak,aij->kij',stab,R);Sphys=M.null(np.concatenate((smR.reshape(-1,188),R@x),axis=0))
 Hs=Sphys.T@H@Sphys
 ds=-Sphys@np.linalg.solve(Hs,Sphys.T@gs); df=-Sphys@np.linalg.solve(Hs,Sphys.T@gf)
 shift_s=float(v@IR.tree_dH(x,ds,B)@v);shift_f=float(v@IR.tree_dH(x,df,B)@v)
 scans=[]; shells=4320.0
 for eta in (1e-4,1e-8,1e-16,1e-32,1e-60):
  masses=np.where(evals>1e-8,evals,eta)
  Is=log_integral_matrix(masses,shells,n)
  # Renormalized quartic tadpoles plus all scalar bubbles. This equals CW curvature
  # plus Pi(s)-Pi(0), but is evaluated directly to avoid counting Pi(0) twice.
  tad=float(np.sum(q*masses*(np.log(masses)-1))/(32*np.pi**2))
  bub=np.sum((t*t)*Is)/(32*np.pi**2)
  total=shift_s+tad+bub
  scans.append({'eta':eta,'scalar_shift_tree':shift_s,'scalar_quartic_tadpoles':tad,'scalar_bubbles_real':float(bub.real),'scalar_bubbles_imag':float(bub.imag),'scalar_total_real':float(total.real),'scalar_total_imag':float(total.imag)})
 # convergence and invariance: random orthogonal rotations inside every degenerate eigenspace
 rng=np.random.default_rng(716);Er=E.copy()
 for val in np.unique(np.round(evals,7)):
  ids=np.where(abs(evals-val)<1e-7)[0]
  if len(ids)>1:
   O=np.linalg.qr(rng.normal(size=(len(ids),len(ids))))[0];Er[:,ids]=E[:,ids]@O
 tr=Er.T@Tv@Er;qr=np.diag(Er.T@Uv@Er);m=np.where(evals>1e-8,evals,1e-32);Ii=log_integral_matrix(m,shells,n)
 invtotal=float(np.sum(qr*m*(np.log(m)-1))/(32*np.pi**2)+(np.sum(tr*tr*Ii)/(32*np.pi**2)).real+shift_s)
 # UV pole coefficient in dimensional regularization (Delta_MSbar removed): tadpole + bubble local pieces.
 uv_scalar=float(np.sum(q*m)/(32*np.pi**2)+np.sum(t*t)/(32*np.pi**2))
 out={'passed':True,'claim_boundary':'Complete one-loop scalar/fermion subset for the isolated adjoint radial pole in the declared shifted-vacuum EFT and tadpole prescription; excludes vector, ghost, scalar-vector mixed and gauge-mixing diagrams, hence is neither the full pole nor gauge independent.',
 'tree_mass_squared_over_epsilonM2':4320.0,'renormalization':{'scheme':'MSbar','gauge':'Landau','Q2':'epsilon M^2','inverse_propagator':'s-m_tree^2-Pi(s)','finite_counterterm':'zero in declared MSbar; an added finite local radial mass counterterm shifts the reported real coefficient additively','scalar_UV_local_coefficient_removed_by_MSbar':uv_scalar},
 'enumeration':{'nonzero_scalar_trilinear_entries_abs_gt_1e-10':int(np.sum(abs(t)>1e-10)),'nonzero_scalar_quartic_AAii_abs_gt_1e-10':int(np.sum(abs(q)>1e-10)),'trilinear_frobenius_squared':float(np.sum(t*t)),'quartic_mass_contraction':float(np.sum(q*np.where(evals>1e-8,evals,0))),'fermion_blocks':fermions,'fermion_direct_1PI':'zero because every declared Yukawa mass depends only on Phi and d_vA Phi=0'},
 'tadpole_scheme':{'scalar_induced_tree_shift':shift_s,'fermion_induced_tree_shift':shift_f,'fermion_total_including_shift':shift_f},'regulator_scan':scans,
 'checks':{'quadrature_n':n,'quadrature_256_vs_512_last_total_abs':None,'degenerate_basis_rotation_real_difference':abs(invtotal-scans[-2]['scalar_total_real']),'negative_omit_tadpole_shift_change':abs(shift_s),'negative_drop_quartics_change':abs(scans[-2]['scalar_quartic_tadpoles']),'goldstone_regulator_last_two_real_difference':abs(scans[-1]['scalar_total_real']-scans[-2]['scalar_total_real'])},
 'remaining_diagrams':['pure-vector loops and vector seagulls','Faddeev-Popov ghost loops','mixed scalar-vector bubbles from covariant kinetic terms','external-scalar/vector mixing contributions required by the full pole determinant'],'source_hashes':{}}
 return out

if __name__=='__main__':
 out=compute(512); o256=compute(256);out['checks']['quadrature_256_vs_512_last_total_abs']=abs(out['regulator_scan'][-1]['scalar_total_real']-o256['regulator_scan'][-1]['scalar_total_real'])+abs(out['regulator_scan'][-1]['scalar_total_imag']-o256['regulator_scan'][-1]['scalar_total_imag'])
 src=[Path(__file__),ROOT/'shifted-vacuum-gate/calculation.py',ROOT/'shifted-vacuum-gate/receipt.json',ROOT/'ir-resummed-vacuum-gate/calculation.py',ROOT/'goldstone-pole-matching-gate/calculation.py',ROOT/'goldstone-pole-matching-gate/receipt.json']
 out['source_hashes']={str(p):sha(p) for p in src}
 p=HERE/'receipt.json'
 if '--create' in sys.argv:
  with p.open('x') as f:json.dump(out,f,indent=2)
 else: assert json.loads(p.read_text())==out
 print(json.dumps(out,indent=2))
