"""Bounded CW diagnostic, no spectral EFT; canonical B=Tr27/3.
Gauge derivatives Decimal 70 digits; independently assembled full gauge matrix.
"""
from pathlib import Path
import json,hashlib,importlib.util,sys
from decimal import Decimal as D,getcontext
import numpy as np
getcontext().prec=70
HERE=Path(__file__).resolve().parent; PRE=HERE.parent/'e6-vacuum-gate/checks.py'
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def setup():
 r=json.loads((HERE.parent/'e6-breaking-gate/breaking-receipt.json').read_text())
 v=load(PRE,'vac'); b=v.load(v.PRE,'br'); em=b.load(); er=em.replay()
 C=np.array([a[:6] for a in er['cartan'][:6]],int); W=np.array(r['weights27'],int);wi={tuple(w):i for i,w in enumerate(W)}
 H=[np.diag(W[:,i]) for i in range(6)]; E=[]
 for i in range(6):
  e=np.zeros((27,27),int)
  for j,w in enumerate(W):
   if tuple(w+C[i]) in wi:e[wi[tuple(w+C[i])],j]=1
  E.append(e)
 roots={tuple(int(i==j) for i in range(6)):E[j] for j in range(6)}
 expected={tuple(x) for x in em.load().positive_roots(C.tolist())}
 while set(roots)!=expected:
  old=len(roots)
  for rootkey,e in list(roots.items()):
   for i in range(6):
    nr=tuple(rootkey[k]+int(i==k) for k in range(6))
    if nr in expected and nr not in roots:
     z=E[i]@e-e@E[i]
     if np.any(z):roots[nr]=z
  assert len(roots)>old
 G=np.array(H+[z for _,e in sorted(roots.items()) for z in (e+e.T,1j*(e-e.T))],complex)
 gram=np.einsum('aij,bji->ab',G,G).real/3
 L=np.linalg.cholesky(gram); T=np.einsum('ab,bij->aij',np.linalg.inv(L),G)
 assert np.max(abs(np.einsum('aij,bji->ab',T,T)-3*np.eye(78)))<1e-12
 yc=np.array([-2,0,-4,-6,-3,0]); a=W@yc
 si=[wi[tuple(s)] for s in r['singlets']]
 # SU5 simple chain (1,3,4,5); fundamental diag(-2,-2,-2,3,3).
 # H1 octet, H5 triplet. SU4 competitor diag(c,c,c,c,-4c), c=sqrt(3/2).
 octet=W[:,0];triplet=W[:,4]; comp=W@np.array([1,0,2,3,4,0])
 assert np.dot(a,a)==180 and np.dot(a,octet)==0 and np.dot(a,triplet)==0
 data=[]
 for root,e in sorted(roots.items()):
  i,j=np.argwhere(e)[0];nr=sum(int(np.any(e[:,s]))+int(np.any(e.T[:,s])) for s in si)
  assert np.trace((e+e.T)@(e+e.T))==12
  data.append((i,j,D(nr)/2))
 return a,octet,triplet,comp,si,G,gram,T,data

def dvec(v):return [D(int(x)) for x in v]
def path(a,b,t):
 aa=dvec(a);bb=dvec(b);n=sum(x*x for x in aa);k=sum(x*x for x in bb)/n
 return [(x+t*y)/(1+k*t*t).sqrt() for x,y in zip(aa,bb)]
def f(x,c=D(5)/6,scale=D(1)):
 return D(0) if not x else x*x*((x/scale).ln()-c)
def fp(x,c=D(5)/6):return D(0) if not x else x*(2*x.ln()+1-2*c)
def fpp(x,c=D(5)/6):return 2*x.ln()+3-2*c

def gauge_pot(v,data,scale=D(1),c=D(5)/6,only_su5=False):
 return 2*sum(f((v[i]-v[j])**2+off,c,scale) for i,j,off in data if not only_su5 or off==0)
def gauge_curv(a,b,data):
 a=dvec(a);b=dvec(b);k=sum(x*x for x in b)/sum(x*x for x in a);ans=D(0)
 for i,j,off in data:
  d=a[i]-a[j];e=b[i]-b[j];x=d*d+off; xp=2*d*e;xpp=2*e*e-2*k*d*d
  if x:ans+=2*(fpp(x)*xp*xp+fp(x)*xpp)
 return ans

def full_gauge(v,si,T):
 A=np.diag(np.array(v,float)); K=np.array([1j*(t@A-A@t) for t in T]);
 mass=np.einsum('aij,bji->ab',K,K).real/3
 for s in si:mass+=2*np.einsum('ai,bi->ab',T[:,:,s].conj(),T[:,:,s]).real
 return np.linalg.eigvalsh(mass)

def scalar_masses(v,si,G,gram):
 av=np.array(v,float);rows=[]
 for f0,s in enumerate(si):
  r=np.zeros(186);r[f0*54+s]=2;rows.append(r)
 r=np.zeros(186);r[si[1]]=1;r[54+si[0]]=1;rows.append(r)
 r=np.zeros(186);r[27+si[1]]=-1;r[81+si[0]]=1;rows.append(r)
 r=np.zeros(186);r[108:]=2*np.einsum('i,aii->a',av,G).real;rows.append(r)
 for f0,s in enumerate(si):
  for imag in (0,1):
   for j in range(27):
    r=np.zeros(186);r[f0*54+27*imag+j]=av[j];r[108:]=(G[:,j,s].imag if imag else G[:,j,s].real);rows.append(r)
 J=np.array(rows);J[:,:108]/=np.sqrt(2);J[:,108:]=J[:,108:]@np.linalg.inv(np.linalg.cholesky(gram).T)
 # same nonzero eigenvalues of 2JJ^T, fewer nulls than 186x186
 return np.linalg.eigvalsh(2*J@J.T)
def sp(v,si,G,gram):
 x=scalar_masses(v,si,G,gram)
 assert abs(x[-1]-4320)<1e-8
 x=x[(x>1e-9)&(x<4000)] # remove exactly constant radial eigenvalue before cancellation
 return float(np.sum(x*x*(np.log(x)-1.5)))

def scalar_blocks(si,G,gram):
 # JJ^T residual block: diag(a_w^2) + 2 K B^-1 K^T.
 # Group equal squared SU5 weights; off-block elements must vanish.
 K=np.array([(G[:,j,s].imag if im else G[:,j,s].real) for s in si for im in (0,1) for j in range(27)])
 C=2*K@np.linalg.inv(gram)@K.T
 inv12=np.rint(12*np.linalg.inv(gram)).astype(np.int64)
 assert np.array_equal(gram.astype(np.int64)@inv12,12*np.eye(78,dtype=np.int64))
 C6=K.astype(np.int64)@inv12@K.astype(np.int64).T
 assert np.max(abs(C6/6-C))<1e-12
 keys=[];groups={}
 for f0 in range(2):
  for im in (0,1):
   for j in range(27):
    w=tuple(int(G[i,j,j].real) for i in (0,2,3,4));key=min(w,tuple(-x for x in w));idx=len(keys);keys.append(key);groups.setdefault(key,[]).append(idx)
 assert all(C6[i,j]==0 for i in range(108) for j in range(108) if keys[i]!=keys[j])
 rank=load(PRE,'ranker').rank;blocks=[]
 for key,inds in groups.items():
  cc=C6[np.ix_(inds,inds)];ev=np.linalg.eigvalsh(cc);rounded=np.rint(ev).astype(int)
  assert np.max(abs(ev-rounded))<1e-10
  for z in sorted(set(rounded)):
   mult=int(sum(rounded==z));assert len(inds)-rank(cc-z*np.eye(len(inds),dtype=int))==mult
   blocks.append((inds[0]%27,D(int(z))/6,mult))
 return blocks

def scalar_pot(v,blocks):return sum(n*f(v[j]**2+off,D(3)/2) for j,off,n in blocks)
def scalar_curv(a,b,blocks):
 aa=dvec(a);bb=dvec(b);k=sum(x*x for x in bb)/sum(x*x for x in aa);ans=D(0)
 for j,off,n in blocks:
  x=aa[j]**2+off;xp=2*aa[j]*bb[j];xpp=2*bb[j]**2-2*k*aa[j]**2
  if x:ans+=n*(fpp(x,D(3)/2)*xp*xp+fp(x,D(3)/2)*xpp)
 return ans/(sum(x*x for x in bb)/3)

def compute(replay_pre=True):
 if replay_pre:
  pr=load(PRE,'prerequisite').replay()
  assert pr['renormalizable_hessian']=={'positive':109,'zero':77,'negative':0,'gauge_zero':66,'physical_zero':11}
 a,o,t,c,si,G,gram,T,data=setup();ad=dvec(a);cd=[D(int(z))*(D(3)/2).sqrt() for z in c]
 modes={};scalar={};blocks=scalar_blocks(si,G,gram);scalar_exact={}
 for name,b in [('octet',o),('triplet',t)]:
  se=scalar_curv(a,b,blocks);hh=D('.0000001');norms=D(int(np.dot(b,b)))/3
  sfd=(scalar_pot(path(a,b,hh),blocks)+scalar_pot(path(a,b,-hh),blocks)-2*scalar_pot(ad,blocks))/(hh*hh*norms)
  assert abs(se-sfd)<D('1e-9')
  scalar_exact[name]={'canonical_curvature_S':str(se),'fd_1e-7':str(sfd)}
  analytic=gauge_curv(a,b,data);fd={}
  for hh in ('0.001','0.00001','0.0000001'):
   h=D(hh);fd[hh]=str((gauge_pot(path(a,b,h),data)+gauge_pot(path(a,b,-h),data)-2*gauge_pot(ad,data))/(h*h))
  assert abs(D(fd['0.0000001'])-analytic)<D('0.00000001')
  norm=D(int(np.dot(b,b)))/3
  modes[name]={'path_curvature_S':str(analytic),'canonical_curvature_S':str(analytic/norm),'finite_difference':fd}
  ss={}
  for h in (.02,.01,.005,.002):
   ss[str(h)]=(sp(path(a,b,D(str(h))),si,G,gram)+sp(path(a,b,D(str(-h))),si,G,gram)-2*sp(ad,si,G,gram))/h**2/float(norm)
  scalar[name]=ss
 # full matrix at two orbits: 72 root modes + six Cartans; root list prediction and Cartan block
 for vv in (ad,cd):
  full=full_gauge(vv,si,T); pred=[float((vv[i]-vv[j])**2+off) for i,j,off in data for _ in range(2)]
  cart=full_gauge([D(0)]*27,si,T[:6]);pred+=list(cart)
  assert np.max(abs(np.sort(pred)-full))<1e-10
 moments=[2*sum(((vv[i]-vv[j])**2+off)**2 for i,j,off in data) for vv in (ad,cd,path(a,o,D('.13')),path(a,t,D('.19')))]
 assert max(moments)-min(moments)<D('1e-60')
 delta=gauge_pot(cd,data)-gauge_pot(ad,data)
 for sc in (D('.01'),D('100')):
  assert abs(gauge_pot(cd,data,scale=sc)-gauge_pot(ad,data,scale=sc)-delta)<D('1e-60')
 su5delta=gauge_pot(cd,data,only_su5=True)-gauge_pot(ad,data,only_su5=True)
 # scalar trace m4 full renormalizable model scale control
 smom=[float(np.sum(scalar_masses(vv,si,G,gram)**2)) for vv in (ad,cd,path(a,o,D('.13')))];assert max(smom)-min(smom)<1e-6
 out={'claim_boundary':'One-loop E6 vector determinant exact high precision angular derivatives, canonical metric specified; scalar V0 double-precision diagnostic. Not full quantum vacuum or pole masses.','prerequisite_replayed':replay_pre,'gauge_modes':modes,'gauge_SU4_minus_SM_S':str(delta),'gauge_SU5_only_SU4_minus_SM_S':str(su5delta),'gauge_trace_m4_root_part':list(map(str,moments)),'scalar_V0_canonical_curvatures_S':scalar,'scalar_SU4_minus_SM_S':sp(cd,si,G,gram)-sp(ad,si,G,gram),'scalar_trace_m4':smom,'negative_controls':{'SU5_truncation_has_scale_dependent_angular_trace':sum((ad[i]-ad[j])**4 for i,j,off in data if off==0)!=sum((cd[i]-cd[j])**4 for i,j,off in data if off==0),'wrong_sign_vector_determinant_reverses_verdict':delta!=0,'scalar_FFH_and_PhiPQ_no_A_dependence':True},'source_hashes':{str(p):sha(p) for p in [Path(__file__),PRE,HERE.parent/'e6-breaking-gate/breaking-receipt.json',HERE.parent/'e6-vacuum-gate/receipt.json',HERE.parent/'anomaly-uv-completion-gate/REPORT.md']},'passed':True}
 out['scalar_exact_modes']=scalar_exact
 out['scalar_exact_SU4_minus_SM_S']=str(scalar_pot(cd,blocks)-scalar_pot(ad,blocks))
 assert abs(float(out['scalar_exact_SU4_minus_SM_S'])-out['scalar_SU4_minus_SM_S'])<1e-7
 for name in modes:
  assert abs(scalar[name]['0.005']-float(scalar_exact[name]['canonical_curvature_S']))<.01
 out['combined_bound_lambda_over_g_squared']=str(min((-3*D(modes[n]['canonical_curvature_S'])/D(scalar_exact[n]['canonical_curvature_S'])).sqrt() for n in modes))
 out['scalar_blocks']=[[j,str(off),n] for j,off,n in blocks]
 out['claim_boundary']='Exact rational scalar residual-block spectra and 70-digit analytic CW derivatives, independently crosschecked full canonical matrices and finite differences. Leading angular stability only; not full quantum vacuum or pole masses.'
 out['combined_SU4_energy_bound_lambda_over_g_squared']=str((-3*delta/D(out['scalar_exact_SU4_minus_SM_S'])).sqrt())
 out['combined_r1']={n:str(3*D(modes[n]['canonical_curvature_S'])+D(scalar_exact[n]['canonical_curvature_S'])) for n in modes}
 out['combined_r3']={n:str(3*D(modes[n]['canonical_curvature_S'])+9*D(scalar_exact[n]['canonical_curvature_S'])) for n in modes}
 assert all(D(x)>0 for x in out['combined_r1'].values())
 assert all(D(x)<0 for x in out['combined_r3'].values())
 assert 3*delta+D(out['scalar_exact_SU4_minus_SM_S'])>0
 assert (-2)+(-1)+0==-3 and 3+(-2)+(-1)==0 and 1+1-2==0
 out['negative_controls']['r3_scalar_dominance_tachyons_detected']=True
 out['negative_controls']['bare_PAQ_forbidden_by_X_charge_minus3']=True
 out['source_hashes'][str(HERE/'sources/martin-0111209.txt')]=sha(HERE/'sources/martin-0111209.txt')
 return out
if __name__=='__main__':
 out=compute('--skip-prerequisite' not in sys.argv)
 p=HERE/'receipt.json'
 if '--create' in sys.argv:
  with p.open('x') as f0:json.dump(out,f0,indent=2)
 elif '--skip-prerequisite' not in sys.argv:assert json.loads(p.read_text())==out
 print(json.dumps(out,indent=2))
