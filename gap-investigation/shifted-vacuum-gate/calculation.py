"""Full 188-real-scalar/79-vector CW transverse calculation. M=1, mu^2=epsilon.
Real-part MSbar Landau potential; unresummed Goldstone limitations disclosed.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
import numpy as np
import json,sys,hashlib,importlib.util
HERE=Path(__file__).resolve().parent
PRE=HERE.parent/'radiative-vacuum-gate/diagnostic.py'
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p); m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def setup():
 d=load(PRE,'radiative');a,o,t,comp,si,G,gram,T,data=d.setup(); n=188
 x=np.zeros(n);x[si[0]]=2**.5;x[54+si[1]]=2**.5;x[108:186]=np.einsum('aii,i->a',T,a).real/3;x[186]=2**.5
 Bs=[];cs=[]
 def add(B,c=0):Bs.append(B);cs.append(c)
 for start in (0,54,186):
  B=np.zeros((n,n));end=start+54 if start<108 else 188;B[start:end,start:end]=np.eye(end-start);add(B,-1)
 for im in (False,True):
  B=np.zeros((n,n))
  if not im:
   for j in range(54):B[j,54+j]=B[54+j,j]=.5
  else:
   for j in range(27):
    B[j,81+j]=B[81+j,j]=.5;B[27+j,54+j]=B[54+j,27+j]=-.5
  add(B)
 B=np.zeros((n,n));B[108:186,108:186]=6*np.eye(78);add(B,-180)
 for start in (0,54):
  for im in (False,True):
   for j in range(27):
    B=np.zeros((n,n)); vals=np.concatenate((T[:,j,:].imag,T[:,j,:].real),axis=1) if im else np.concatenate((T[:,j,:].real,-T[:,j,:].imag),axis=1)
    B[108:186,start:start+54]=vals/2**.5;B[start:start+54,108:186]=vals.T/2**.5;add(B)
 B=np.array(Bs); c=np.array(cs)
 R=np.zeros((79,n,n))
 for k,Tk in enumerate(T):
  D=1j*Tk;rr=np.block([[D.real,-D.imag],[D.imag,D.real]])
  R[k,:54,:54]=rr;R[k,54:108,54:108]=rr
  comm=1j*(Tk@T-T@Tk)
  R[k,108:186,108:186]=np.einsum('aij,bji->ab',T,comm).real/3
 for start,end,q in ((0,54,-2),(54,108,-2),(186,188,3)):
  h=(end-start)//2;R[78,start:start+h,start+h:end]=-q*np.eye(h);R[78,start+h:end,start:start+h]=q*np.eye(h)
 assert np.max(abs(R+R.transpose(0,2,1)))<1e-12
 return x,B,c,R,T,si,a

def tree(x,B,c):
 J=B@x;f=.5*(J@x)+c;H=2*(J.T@J+np.einsum('r,rij->ij',f,B));return f@f,2*J.T@f,H,J,f

def spectral(H,c,hard=False):
 z,U=np.linalg.eigh(H); mask=(z>.5) if hard else (abs(z)>1e-9);fp=np.zeros_like(z);f=np.zeros_like(z)
 f[mask]=z[mask]**2*(np.log(abs(z[mask]))-c)
 fp[mask]=z[mask]*(2*np.log(abs(z[mask]))+1-2*c)
 return sum(f),(U*fp)@U.T,z

def loop(x,B,c,R,fermions=True,hard=False):
 _,_,H,J,_=tree(x,B,c);Vs,W,sz=spectral(H,1.5,hard)
 # dH=2(dJ^t J+J^t dJ)+2 sum dF B. All 188 scalar modes.
 gs=4*np.einsum('rij,rj->i',B,J@W)+2*J.T@np.einsum('ij,rji->r',W,B)
 K=R@x;Vv,Wv,vz=spectral(K@K.T,5/6)
 gv=2*np.einsum('ai,aij->j',Wv@K,R)
 # 27 + 1 + 1 + 1 Dirac blocks; y/sqrt(epsilon)=(1,1,2,3).
 u=(x[186]**2+x[187]**2)/2;vf=0.;gf=np.zeros(188)
 if fermions:
  for mult,y in ((27,1),(1,1),(1,2),(1,3)):
   z=y*y*u;vf-=4*mult*z*z*(np.log(z)-1.5)
   gf[186:]-=4*mult*y*y*z*(2*np.log(z)-2)*x[186:]
 return (Vs+3*Vv+vf)/(64*np.pi**2),(gs+3*gv+gf)/(64*np.pi**2),{'scalar_min':float(sz[0]),'scalar_max':float(sz[-1]),'vector_max':float(vz[-1]),'fermion_tadpole_phi':float(gf[186]/(64*np.pi**2))}

def null(A,tol=1e-8):
 _,s,V=np.linalg.svd(A,full_matrices=True);return V[int(sum(s>tol)):].T

def exact_singlet_inverse(x,B,c,T,si,a):
 from fractions import Fraction as Fq
 d=load(PRE,'rad_exact');_,_,_,_,_,G,gram,_,_=d.setup()
 # Solve three simple-root commutator constraints on the six original Cartans.
 W=np.array([np.diag(g).real for g in G[:6]]).T
 br=json.loads((HERE.parent/'e6-breaking-gate/breaking-receipt.json').read_text())
 vac=d.load(d.PRE,'vac_exact');breaking=vac.load(vac.PRE,'breaking_exact');em=breaking.load();cart=em.replay()['cartan']
 C=np.array([r[:6] for r in cart[:6]],int)
 mat=[[Fq(int(v)) for v in C[k]] for k in (0,2,4)]
 piv=[];row=0
 for col in range(6):
  z=next((j for j in range(row,3) if mat[j][col]),None)
  if z is None:continue
  mat[row],mat[z]=mat[z],mat[row];v=mat[row][col];mat[row]=[q/v for q in mat[row]]
  for j in range(3):
   if j!=row:
    v=mat[j][col];mat[j]=[q-v*t for q,t in zip(mat[j],mat[row])]
  piv.append(col);row+=1
  if row==3:break
 Z=[]
 def vec():return [Fq(0)]*188
 for idx in (si[0],54+si[1],186):
  z=vec();z[idx]=1;Z.append(z)
 for im in (False,True):
  z=vec();z[si[1]+27*im]=1;z[54+si[0]+27*im]=-1 if im else 1;Z.append(z)
 for j in set(range(6))-set(piv):
  z=vec();z[108+j]=1
  for i,k in enumerate(piv):z[108+k]=-mat[i][j]
  Z.append(z)
 for k in (76,77):
  z=vec();z[108+k]=1;Z.append(z)
 Z=np.array(Z,dtype=object).T
 # Direct integer residual Jacobian in original Re/Im h and G coordinates.
 rows=[]
 for start,ss in ((0,si[0]),(54,si[1]),(186,0)):
  r=np.zeros(188,int);r[start+ss]=2;rows.append(r)
 r=np.zeros(188,int);r[si[1]]=r[54+si[0]]=1;rows.append(r)
 r=np.zeros(188,int);r[27+si[1]]=-1;r[81+si[0]]=1;rows.append(r)
 r=np.zeros(188,int);r[108:186]=np.rint(2*np.einsum('i,aii->a',a,G).real).astype(int);rows.append(r)
 for start,ss in ((0,si[0]),(54,si[1])):
  for im in (False,True):
   for j in range(27):
    r=np.zeros(188,int);r[start+27*im+j]=a[j];r[108:186]=(G[:,j,ss].imag if im else G[:,j,ss].real).astype(int);rows.append(r)
 Jz=np.array(rows,dtype=object)@Z;K=2*Jz.T@Jz
 n=10; aug=[[Fq(K[i,j]) for j in range(n)]+[Fq(int(i==j)) for j in range(n)] for i in range(n)]
 for i in range(n):
  j=next(j for j in range(i,n) if aug[j][i]);aug[i],aug[j]=aug[j],aug[i];v=aug[i][i];aug[i]=[q/v for q in aug[i]]
  for j in range(n):
   if i!=j:
    v=aug[j][i];aug[j]=[q-v*t for q,t in zip(aug[j],aug[i])]
 inv=np.array([r[n:] for r in aug],object);assert np.array_equal(K@inv,np.eye(n,dtype=int))
 D=np.array(Z,float);D[:108]*=2**.5;D[186:]*=2**.5;D[108:186]=np.linalg.cholesky(gram).T@D[108:186]
 assert np.max(abs(D.T@tree(x,B,c)[2]@D-np.array(K,float)))<1e-7
 return D,np.array(inv,float),{'basis_original':[[str(v) for v in row] for row in Z.T],'Hessian':[[str(v) for v in row] for row in K],'inverse':[[str(v) for v in row] for row in inv],'exact_identity_K_times_inverse':True}

def compute():
 x,B,c,R,T,si,a=setup();V,g,H,J,f=tree(x,B,c);assert np.max(abs(f))<1e-10
 z,U=np.linalg.eigh(H);P=U[:,z>1e-7];F=null(np.concatenate((H,(R@x)),axis=0));Q=null(R@x)
 assert P.shape[1]==110 and F.shape[1]==11 and Q.shape[1]==121
 # All SM generators are kernel of tangent map; select their full linear action,
 # then invariant singlet field space as simultaneous kernel, not a guessed radial slice.
 stab=null((R@x).T);smR=np.einsum('ak,aij->kij',stab,R)
 S=null(smR.reshape(-1,188));Sphys=null(np.concatenate((smR.reshape(-1,188),R@x),axis=0))
 assert np.max(abs(Sphys.T@F))<1e-8
 vl,tad,info=loop(x,B,c,R);assert np.linalg.norm(tad-S@S.T@tad)<1e-7
 Hs=Sphys.T@H@Sphys;delta=-Sphys@np.linalg.solve(Hs,Sphys.T@tad)
 D,inv,exact=exact_singlet_inverse(x,B,c,T,si,a)
 assert np.max(abs(smR@D))<1e-9 and np.max(abs((R@x)@D))<1e-9
 exact_delta=-D@inv@D.T@tad
 assert np.linalg.norm(delta-exact_delta)<1e-7
 delta=exact_delta
 assert np.linalg.norm(H@delta+tad)/np.linalg.norm(tad)<1e-10
 # Exact rational inverse on a nonorthogonal rational singlet transverse basis is
 # generated separately below: no claim that floating inverse is exact.
 # Independent directional FD checks (full scalar/vector+fermion determinant).
 checks=[]
 for v in (x/np.linalg.norm(x),delta/np.linalg.norm(delta)):
  h=1e-5;fd=(loop(x+h*v,B,c,R)[0]-loop(x-h*v,B,c,R)[0])/(2*h)
  checks.append({'analytic':float(tad@v),'fd':float(fd),'relative_error':float(abs(fd-tad@v)/max(1,abs(tad@v)))})
 assert max(k['relative_error'] for k in checks)<1e-6
 # Pure angular leading block includes transverse displacement, not just straight V1 Hessian.
 rad=json.loads((PRE.parent/'receipt.json').read_text());margins={k:float(v)/(64*np.pi**2) for k,v in rad['combined_r1'].items()}
 residuals=[]
 for eps in (1e-7,5e-8,2.5e-8):
  xp=x+eps*delta;_,gt,Ht,_,_=tree(xp,B,c);_,gl,inf=loop(xp,B,c,R)
  residual=eps*gt+eps**2*gl
  # Directional CW Hessian on entire physical quotient, finite differences.
  qp=null(R@xp);h=2e-5
  HL=np.column_stack([(loop(xp+h*v,B,c,R)[1]-loop(xp-h*v,B,c,R)[1])/(2*h) for v in qp.T]);HL=qp.T@HL;HL=(HL+HL.T)/2
  phys=eps*(qp.T@Ht@qp)+eps**2*HL; eig=np.linalg.eigvalsh(phys)
  # block Schur complement in fixed tree positive/flat frame (close to quotient)
  pp=qp.T@P;ff=qp.T@F;A=pp.T@phys@pp;Dflat=ff.T@phys@ff;C=pp.T@phys@ff
  schur=Dflat-C.T@np.linalg.solve(A,C)
  residuals.append({'epsilon':eps,'gradient_norm':float(np.linalg.norm(residual)),'norm_over_epsilon_cubed':float(np.linalg.norm(residual)/eps**3),'min_physical_eigenvalue_over_epsilon_squared':float(eig[0]/eps**2),'schur_min_over_epsilon_squared':float(np.linalg.eigvalsh(schur)[0]/eps**2),'tree_scalar_min_at_shift':inf['scalar_min']*eps,'relative_shift':float(eps*np.linalg.norm(delta)/np.linalg.norm(x))})
 assert all(r['schur_min_over_epsilon_squared']>0 for r in residuals)
 noferm=loop(x,B,c,R,False)[1];dd=-P@((P.T@noferm)/z[z>1e-7]);ferm_control=float(np.linalg.norm(dd-delta))
 assert ferm_control>1e-3
 # Construct a stationary point of the analytic hard-scalar one-loop action.
 # The omitted 78 soft scalar modes are not declared absent from the full action.
 eps=1e-7;coords=eps*(-inv@D.T@tad);newton=[]
 for iteration in range(5):
  xp=x+D@coords;_,gt,Ht,_,_=tree(xp,B,c);_,gl,_=loop(xp,B,c,R,hard=True)
  grad=D.T@(gt+eps*gl);newton.append(float(np.linalg.norm(grad)))
  h=1e-6;L=np.column_stack([(loop(xp+h*v,B,c,R,hard=True)[1]-loop(xp-h*v,B,c,R,hard=True)[1])/(2*h) for v in D.T])
  K=D.T@Ht@D+eps*D.T@L;step=np.linalg.solve(K,grad);coords-=step
 xp=x+D@coords;_,gt,Ht,_,_=tree(xp,B,c);_,gl,_=loop(xp,B,c,R,hard=True)
 full_stationarity=float(np.linalg.norm(eps*gt+eps**2*gl));assert full_stationarity<1e-15
 qp=null(R@xp);hard_checks=[]
 for h in (2e-5,1e-5):
  L=np.column_stack([(loop(xp+h*v,B,c,R,hard=True)[1]-loop(xp-h*v,B,c,R,hard=True)[1])/(2*h) for v in qp.T])
  PH=eps*(qp.T@Ht@qp)+eps**2*((qp.T@L+L.T@qp)/2)
  pp=qp.T@P;ff=qp.T@F;AA=pp.T@PH@pp;CC=pp.T@PH@ff;DD=ff.T@PH@ff
  sc=DD-CC.T@np.linalg.solve(AA,CC)
  hard_checks.append({'fd_step':h,'min_physical_over_epsilon_squared':float(np.linalg.eigvalsh(PH)[0]/eps**2),'Schur_min_over_epsilon_squared':float(np.linalg.eigvalsh(sc)[0]/eps**2),'massive_min_over_epsilon':float(np.linalg.eigvalsh(AA)[0]/eps)})
 assert all(k['Schur_min_over_epsilon_squared']>1.17 for k in hard_checks)
 hard_result={'epsilon':eps,'singlet_coordinates':coords.tolist(),'newton_projected_residuals_divided_by_epsilon':newton,'full_gradient_norm':full_stationarity,'physical_Hessian':hard_checks,'scalar_hard_spectral_count':int(sum(np.linalg.eigvalsh(Ht)>.5)),'scope':'110 massive scalar spectral subbundle; 78 soft scalars retained as omitted IR remainder, not a full resummed theory'}
 # Tree gauge invariance Ward identity, including off-shell H R x = R grad V.
 y=x+1e-5*delta;_,gy,Hy,_,_=tree(y,B,c);ward=float(np.max(abs((Hy@(R@y).T).T-R@gy)))
 assert ward<1e-7
 return {'passed':True,'claim_boundary':'Executed full one-loop real-part leading shift and numerical Schur diagnostics; conditional hard-mode continuation only, not IR-resummed/pole/global vacuum proof.','hard_mode_stationary_solution':hard_result,'dimensions':{'scalar':188,'vector':79,'gauge':67,'tree_positive':110,'physical_flats':11,'SM_fixed_space':S.shape[1],'SM_fixed_physical':Sphys.shape[1]},'tree_gap':float(z[z>1e-7][0]),'exact_singlet_inverse':exact,'singlet_covector_tadpole':(D.T@tad).tolist(),'singlet_coordinate_shift':(-inv@D.T@tad).tolist(),'tadpole_norm':float(np.linalg.norm(tad)),'delta_norm':float(np.linalg.norm(delta)),'h1_radial_delta':float(delta[si[0]]/2**.5),'h2_radial_delta':float(delta[54+si[1]]/2**.5),'Phi_radial_delta':float(delta[186]/2**.5),'A_radial_fraction_delta':float(x[108:186]@delta[108:186]/60),'tadpole_canonical':tad.tolist(),'leading_delta_canonical':delta.tolist(),'loop_info':info,'derivative_checks':checks,'residual_scaling':residuals,'leading_angular_margins':margins,'negative_controls':{'omit_fermions_changes_shift_norm':ferm_control,'r3_angular_eigenvalues':[float(v)/(64*np.pi**2) for v in rad['combined_r3'].values()],'off_shell_Ward_residual':ward},'source_hashes':{str(p):sha(p) for p in [Path(__file__),PRE,PRE.parent/'REPORT.md',PRE.parent/'receipt.json',PRE.parent/'verification.json',HERE.parent/'e6-vacuum-gate/checks.py',HERE.parent/'anomaly-uv-completion-gate/REPORT.md']}}
if __name__=='__main__':
 out=compute();p=HERE/'receipt.json'
 if '--create' in sys.argv:
  with p.open('x') as f:json.dump(out,f,indent=2)
 else:
  old=json.loads(p.read_text());assert old==out,'receipt mismatch'
 print(json.dumps({k:v for k,v in out.items() if k not in ['tadpole_canonical','leading_delta_canonical']},indent=2))
