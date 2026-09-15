"""Leading hard/soft matching for the declared shifted E6 action; no IR clipping.
Replay compares saved receipt before any write. Run with native Python -B.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import sys,json,hashlib,importlib.util
from pathlib import Path
import numpy as np
from decimal import Decimal,localcontext
HERE=Path(__file__).resolve().parent
PRE=HERE.parent/'shifted-vacuum-gate'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):
 s=importlib.util.spec_from_file_location('shifted_ir_input',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def spectral_data(H,c,cut):
 z,U=np.linalg.eigh(H); keep=z>cut
 # The cut labels a gapped analytic spectral bundle, not positive-mass clipping.
 f=np.zeros_like(z);p=np.zeros_like(z);pp=np.zeros_like(z)
 f[keep]=z[keep]**2*(np.log(z[keep])-c)
 p[keep]=z[keep]*(2*np.log(z[keep])+1-2*c)
 pp[keep]=2*np.log(z[keep])+3-2*c
 dz=z[:,None]-z[None,:];dp=p[:,None]-p[None,:]
 near=abs(dz)<1e-8*np.maximum(1,np.maximum(abs(z[:,None]),abs(z[None,:])))
 K=np.zeros_like(dz);np.divide(dp,dz,out=K,where=~near)
 K[near]=np.broadcast_to((pp[:,None]+pp[None,:])/2,dz.shape)[near]
 return float(sum(f)),(U*p)@U.T,(z,U,K)
def frechet(data,dH):
 z,U,K=data;return U@(K*(U.T@dH@U))@U.T

def hard(x,B,c,R,frame=None):
 V,g,H,J,f=M.tree(x,B,c);Vs,W,ds=spectral_data(H,1.5,.5)
 assert sum(ds[0]>.5)==110
 gs=4*np.einsum('rij,rj->i',B,J@W)+2*J.T@np.einsum('ij,rji->r',W,B)
 K=R@x;Vv,Wv,dv=spectral_data(K@K.T,5/6,1e-8)
 gv=2*np.einsum('ai,aij->j',Wv@K,R)
 u=(x[186:]@x[186:])/2;vf=0.;gf=np.zeros(188);HF=np.zeros((188,188))
 for n,y in ((27,1),(1,1),(1,2),(1,3)):
  z=y*y*u;p=z*(2*np.log(z)-2);pp=2*np.log(z)
  vf-=4*n*z*z*(np.log(z)-1.5);gf[186:]-=4*n*y*y*p*x[186:]
  HF[186:,186:]-=4*n*(y*y*p*np.eye(2)+y**4*pp*np.outer(x[186:],x[186:]))
 L=(Vs+3*Vv+vf)/(64*np.pi**2);grad=(gs+3*gv+gf)/(64*np.pi**2)
 if frame is None:return L,grad
 cols=[]
 for v in frame.T:
  dJ=B@v;df=J@v
  dH=2*(dJ.T@J+J.T@dJ+np.einsum('r,rij->ij',df,B))
  dW=frechet(ds,dH)
  dgs=4*np.einsum('rij,rj->i',B,dJ@W+J@dW)+2*dJ.T@np.einsum('ij,rji->r',W,B)+2*J.T@np.einsum('ij,rji->r',dW,B)
  dK=R@v;dWv=frechet(dv,dK@K.T+K@dK.T)
  dgv=2*np.einsum('ai,aij->j',dWv@K+Wv@dK,R)
  cols.append((dgs+3*dgv+HF@v)/(64*np.pi**2))
 return L,grad,np.column_stack(cols)

def tree_dH(x,v,B):
 J=B@x;dJ=B@v
 return 2*(dJ.T@J+J.T@dJ+np.einsum('r,rij->ij',J@v,B))
def eig(A):return np.linalg.eigvalsh((A+A.T)/2).tolist()
def decimal_soft(m8,m3,eps,precision):
 with localcontext() as ctx:
  ctx.prec=precision;d=Decimal;e=d(str(eps));a=d(str(m8));b=d(str(m3));pi=d('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
  val=e**4*(8*a*a*((e*a).ln()-d('1.5'))+3*b*b*((e*b).ln()-d('1.5')))/(64*pi*pi)
  # Rigorous algebraic envelope provided only for these positive mass values.
  cap=d('1.5');bound=11*cap**2*(abs(e.ln())+d('1.5')+cap.ln())*e**4/(64*pi*pi)
  assert 1<a<cap and 1<b<cap and abs(val)<bound
  return str(val),str(bound)

def subtraction_controls():
 # A matrix need not commute with Delta: subtract the directional Taylor series
 # of Tr f(G+t Delta). Check linear term by finite differences at positive G.
 G=np.diag([.7,1.2]);D=np.array([[.2,.07],[.07,-.1]])
 def trf(A):
  z=np.linalg.eigvalsh(A);assert min(z)>0;return sum(z*z*(np.log(z)-1.5))
 fp=np.diag(G)*(2*np.log(np.diag(G))-2);linear=float(np.diag(D)@fp)
 rows=[]
 for t in (1e-3,5e-4,2.5e-4):
  full=trf(G+t*D);good=full-trf(G)-t*linear;wrong=full-trf(G)+t*linear
  rows.append({'t':t,'correct_remainder_over_t2':good/t**2,'wrong_sign_remainder_over_t':wrong/t})
 assert abs(rows[-1]['wrong_sign_remainder_over_t'])>.01
 assert abs(rows[0]['correct_remainder_over_t2']-rows[-1]['correct_remainder_over_t2'])<1e-4
 return rows

def compute():
 global M
 M=load(PRE/'calculation.py')
 old=json.loads((PRE/'receipt.json').read_text())
 for p,h in old['source_hashes'].items():assert sha(Path(p))==h,(p,'predecessor source changed')
 x,B,c,R,T,si,a=M.setup();_,gt,H,J,f=M.tree(x,B,c)
 z,U=np.linalg.eigh(H);P=U[:,z>1e-7];F=M.null(np.concatenate((H,R@x),axis=0))
 ug,sg,vg=np.linalg.svd((R@x).T,full_matrices=False);G=ug[:,:67];S=np.column_stack((G,F))
 assert F.shape==(188,11) and np.max(abs(S.T@S-np.eye(78)))<1e-9
 L,g,HL=hard(x,B,c,R,np.eye(188));asym=float(np.max(abs(HL-HL.T)));HL=(HL+HL.T)/2
 delta=np.array(old['leading_delta_canonical']);leading=tree_dH(x,delta,B)
 Pi=S.T@HL@S;TS=S.T@leading@S;res=Pi+TS
 # Goldstone Ward cancellation, including all 67 and mixed soft matrix elements.
 ward=float(np.linalg.norm(res[:,:67],2));assert ward<1e-7
 ff=eig(res[67:,67:]);assert min(ff)>1.18 and max(ff)<1.41
 margins=old['leading_angular_margins'];target=sorted([margins['octet']]*8+[margins['triplet']]*3)
 assert max(abs(np.array(ff)-target))<1e-7
 # Full one-loop Ward identity, not a manually zeroed diagonal.
 ward_full=float(np.max(abs((HL@(R@x).T).T-R@g)))
 assert ward_full<1e-6
 derivatives=[]
 for name,v in [('octet_rep',F[:,0]),('Goldstone_rep',G[:,0]),('shift',delta/np.linalg.norm(delta))]:
  exact=HL@v
  for h in (4e-5,2e-5,1e-5):
   fd=(hard(x+h*v,B,c,R)[1]-hard(x-h*v,B,c,R)[1])/(2*h)
   err=float(np.linalg.norm(fd-exact)/max(1,np.linalg.norm(exact)))
   derivatives.append({'direction':name,'step':h,'relative_error':err})
 assert max(q['relative_error'] for q in derivatives if q['step']==1e-5)<1e-6,derivatives
 shift_errors=[q['relative_error'] for q in derivatives if q['direction']=='shift']
 assert 3.9<shift_errors[0]/shift_errors[1]<4.1 and 3.9<shift_errors[1]/shift_errors[2]<4.1
 # Read-back canonical shifted sample, without rerunning or rewriting its receipt.
 Z,inv,exact=M.exact_singlet_inverse(x,B,c,T,si,a)
 xp=x+Z@np.array(old['hard_mode_stationary_solution']['singlet_coordinates']);eps=1e-7
 _,gp,Hp,_,_=M.tree(xp,B,c);lp,glp,HLp=hard(xp,B,c,R,np.eye(188));HLp=(HLp+HLp.T)/2
 PH=eps*Hp+eps**2*HLp;gradp=eps*gp+eps**2*glp
 Q=M.null(R@xp);pp=Q@(Q.T@P);fframe=Q@(Q.T@F)
 AA=pp.T@PH@pp;CC=pp.T@PH@fframe;DD=fframe.T@PH@fframe
 sc=DD-CC.T@np.linalg.solve(AA,CC)
 schur=float(min(eig(sc))/eps**2);assert schur>1.18
 # This is an IR obstruction diagnostic, not a claimed full resummed Hessian.
 # Along the canonical radial direction, tree Goldstone eigenvalues turn on
 # linearly; their squared derivative controls the log(eta) term in V''.
 v=x/np.linalg.norm(x);Dg=G.T@tree_dH(x,v,B)@G
 log_coefficient=float(np.trace(Dg@Dg)/(32*np.pi**2))
 assert log_coefficient>0
 soft=[]
 for e in (1e-7,5e-8,2.5e-8):
  v50,b50=decimal_soft(margins['octet'],margins['triplet'],e,50)
  v80,b80=decimal_soft(margins['octet'],margins['triplet'],e,80)
  assert abs(Decimal(v50)-Decimal(v80))<Decimal('1e-70')
  soft.append({'epsilon':e,'physical_soft_ring_V_50_digits':v50,'physical_soft_ring_V_80_digits':v80,'absolute_value_envelope':b80})
 regulator=[]
 for eta in (1e-4,1e-8,1e-16,1e-32):
  regulator.append({'eta_dimensionless':eta,'radial_log_term_over_epsilon_squared':log_coefficient*np.log(eta)})
 wrong=float(np.linalg.norm((TS-Pi)[:,:67],2));retained=float(np.linalg.norm(TS[:67,:67],2))
 assert wrong>1 and retained>1
 # Save full projected tensors as deterministic JSON (not an opaque npz archive).
 tensors={'basis_G':G.tolist(),'basis_F':F.tolist(),'Pi_hard_over_epsilon_squared':Pi.tolist(),'tree_shift_over_epsilon_squared':TS.tolist(),'sum_over_epsilon_squared':res.tolist()}
 source_paths=[Path(__file__),PRE/'REPORT.md',PRE/'calculation.py',PRE/'receipt.json',PRE.parent/'radiative-vacuum-gate/diagnostic.py',PRE.parent/'radiative-vacuum-gate/REPORT.md',PRE.parent/'radiative-vacuum-gate/receipt.json']+sorted((HERE/'sources').glob('*'))
 out={'claim_boundary':'Leading 78x78 hard zero-momentum matching and ring potential value. No full resummed stationary branch, C2 remainder or pole mass proof.','passed':True,'dimensions':{'Goldstone':67,'physical_soft':11,'hard_scalar':110},'hard_Hessian_antisymmetry':asym,'hard_Ward_max_abs':ward_full,'leading_soft_Goldstone_column_operator_norm':ward,'hard_Pi_GG_eigenvalues':eig(Pi[:67,:67]),'tree_shift_GG_eigenvalues':eig(TS[:67,:67]),'hard_Pi_FF_eigenvalues':eig(Pi[67:,67:]),'tree_shift_FF_eigenvalues':eig(TS[67:,67:]),'resummed_leading_FF_eigenvalues':ff,'matched_hard_stationary_sample':{'epsilon':eps,'gradient_norm':float(np.linalg.norm(gradp)),'hard_Schur_min_over_epsilon_squared':schur,'massive_min_over_epsilon':float(min(eig(AA))/eps),'full_gauge_Ward_residual':float(np.max(abs((PH@(R@xp).T).T-R@gradp)))},'step_controls':derivatives,'physical_soft_ring':soft,'radial_Goldstone_log_obstruction':{'unit_direction':'x0 / norm(x0)','coefficient_of_epsilon_squared_log_eta':log_coefficient,'regulator_scan':regulator,'scope':'Analytic coefficient of the Gaussian Goldstone ring curvature singularity. Higher hard matching and pole-momentum terms not included.'},'negative_controls':{'opposite_self_energy_sign_Goldstone_norm':wrong,'retain_tree_Goldstone_mass_norm':retained,'noncommuting_double_count_subtraction':subtraction_controls()},'source_hashes':{str(p):sha(p) for p in source_paths}}
 return out,tensors
if __name__=='__main__':
 receipt=HERE/'receipt.json';tensor=HERE/'projected-tensors.json'
 if '--create' not in sys.argv:
  saved=json.loads(receipt.read_text());saved_t=json.loads(tensor.read_text())
  for p,h in saved['source_hashes'].items():assert sha(Path(p))==h
 out,mat=compute()
 if '--create' in sys.argv:
  with receipt.open('x') as f:json.dump(out,f,indent=2)
  with tensor.open('x') as f:json.dump(mat,f,indent=2)
 else:assert saved==out and saved_t==mat,'replay mismatch'
 print(json.dumps({k:v for k,v in out.items() if not k.endswith('eigenvalues')},indent=2))
