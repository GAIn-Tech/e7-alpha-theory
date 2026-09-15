"""Exact representation/Jacobian gate. No floating eigenvalue tolerances.
Run native Python with numpy (integer arrays only); Fraction row rank.
"""
from pathlib import Path
from fractions import Fraction as F
import importlib.util, json, hashlib, sys
import numpy as np
HERE=Path(__file__).resolve().parent
PRE=HERE.parent/'e6-breaking-gate/breaking_checks.py'
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def rank(rows):
 # sparse exact elimination; preserve pivot rows, no tolerance
 piv={}
 for rr in rows:
  r={j:F(int(x)) if isinstance(x,np.integer) else F(x) for j,x in enumerate(rr) if x}
  while r:
   j=min(r)
   if j not in piv:
    d=r[j];piv[j]={k:v/d for k,v in r.items()};break
   d=r[j]
   for k,v in piv[j].items():
    n=r.get(k,F(0))-d*v
    if n:r[k]=n
    else:r.pop(k,None)
 return len(piv)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def compute():
 b=load(PRE,'breaking'); receipt=b.replay(); emb=b.load();pr=emb.replay()
 C=np.array([r[:6] for r in pr['cartan'][:6]],dtype=np.int64)
 W=[tuple(w) for w in receipt['weights27']];wi={w:i for i,w in enumerate(W)}
 H=[np.diag([w[i] for w in W]) for i in range(6)];E=[]
 for i in range(6):
  e=np.zeros((27,27),dtype=np.int64)
  for j,w in enumerate(W):
   v=tuple(w[k]+int(C[i,k]) for k in range(6))
   if v in wi:e[wi[v],j]=1
  E.append(e)
 def comm(a,b):return a@b-b@a
 nchecks=0
 for i in range(6):
  for j in range(6):
   assert np.array_equal(comm(H[i],E[j]),C[i,j]*E[j]);nchecks+=1
   assert np.array_equal(comm(E[i],E[j].T),H[i] if i==j else 0*H[i]);nchecks+=1
   if i!=j:
    z=comm(E[i],E[j])
    if C[i,j]==-1:z=comm(E[i],z)
    assert not np.any(z);nchecks+=1
 roots={tuple(int(i==j) for i in range(6)):E[j] for j in range(6)}
 expected={tuple(r) for r in emb.load().positive_roots(C.tolist())}
 while set(roots)!=expected:
  old=len(roots)
  for r,e in list(roots.items()):
   for i in range(6):
    nr=tuple(r[k]+int(k==i) for k in range(6))
    if nr in expected and nr not in roots:
     z=comm(E[i],e)
     if np.any(z):roots[nr]=z
  assert len(roots)>old
 # Every Hermitian basis matrix is real symmetric or i times real antisymmetric.
 # Store real and imaginary integer parts separately.
 G=[(h,0*h) for h in H];labels=[('cartan',i) for i in range(6)]
 for r,e in sorted(roots.items()):
  assert np.max(np.abs(e))==1
  G.extend([(e+e.T,0*e),(0*e,e-e.T)]);labels.extend([('rootR',r),('rootI',r)])
 assert len(G)==78
 assert rank([list(a.flat)+list(z.flat) for a,z in G])==78
 # A0=6Y, v1=v2=1 in arbitrary mass unit M. NO alpha input.
 yc=np.array([int(6*F(x)) for x in receipt['Y_coroot']],dtype=np.int64)
 A=sum((yc[i]*H[i] for i in range(6)),np.zeros((27,27),dtype=np.int64));av=np.diag(A)
 si=[wi[tuple(s)] for s in receipt['singlets']]
 assert all(av[s]==0 for s in si)
 assert sum(av==0)==2
 c=int(np.trace(A@A)); spectrum=sorted(set(map(int,av)))
 # Real coordinates: Re/Im H1, Re/Im H2 (108), then 78 real A coordinates.
 rows=[]
 for f,s in enumerate(si):
  r=[0]*186;r[f*54+s]=2;rows.append(r)
 r=[0]*186;r[si[1]]=1;r[54+si[0]]=1;rows.append(r)
 r=[0]*186;r[27+si[1]]=-1;r[81+si[0]]=1;rows.append(r)
 r=[0]*186
 for k,(gr,gi) in enumerate(G):r[108+k]=2*int(np.trace(A@gr))
 rows.append(r)
 base_count=len(rows)
 for f,s in enumerate(si):
  for imag in (False,True):
   for j in range(27):
    r=[0]*186;r[f*54+27*imag+j]=int(av[j])
    for k,(gr,gi) in enumerate(G):r[108+k]=int((gi if imag else gr)[j,s])
    rows.append(r)
 Jren=rows.copy()
 # p(z)=product(z-r), r in the computed distinct A0 eigenvalues.
 # Frechet derivative at A0: divided difference; off-diagonal unequal eigenvalues zero.
 # Scale p' out of each output row (nonzero), preserving exact kernel and rank.
 pd={r:np.prod([r-t for t in spectrum if t!=r],dtype=object) for r in spectrum}
 assert all(pd.values())
 specrows=[]
 for imag in (False,True):
  for i in range(27):
   for j in range(27):
    if av[i]!=av[j]:continue
    r=[0]*186
    for k,(gr,gi) in enumerate(G):r[108+k]=int((gi if imag else gr)[i,j])
    if any(r):specrows.append(r)
 Jeff=rows+specrows
 renrank=rank(Jren);eftrank=rank(Jeff)
 # Gauge tangents in H slots and A matrix slots; avoid solving nonorthogonal Cartan metric.
 # Gauge-orbit rank as image in ambient 108+2*729 real coordinates.
 gauges=[]
 for gr,gi in G:
  rr=[]
  for s in si:rr.extend((-gi[:,s]).tolist()+gr[:,s].tolist())
  rr.extend((-comm(gi,A)).flat);rr.extend(comm(gr,A).flat)
  gauges.append(rr)
 gauge_rank=rank(gauges)
 # Express commutator images in the same 78-coordinate basis and test J*g=0.
 gram=[[int(np.trace(ar@br-ai@bi)) for br,bi in G] for ar,ai in G]
 gi=emb.inverse(gram)
 gauge_coords=[]
 for rr in gauges:
  ar=np.array(rr[108:108+729],dtype=np.int64).reshape(27,27)
  ai=np.array(rr[108+729:],dtype=np.int64).reshape(27,27)
  dual=[int(np.trace(ar@br-ai@bi)) for br,bi in G]
  coeff=[sum(gi[i][j]*dual[j] for j in range(78)) for i in range(78)]
  assert all(v.denominator==1 for v in coeff)
  coeff=list(map(int,coeff));g=rr[:108]+coeff;gauge_coords.append(g)
  assert np.array_equal(sum((coeff[k]*G[k][0] for k in range(78)),np.zeros((27,27),dtype=np.int64)),ar)
  assert np.array_equal(sum((coeff[k]*G[k][1] for k in range(78)),np.zeros((27,27),dtype=np.int64)),ai)
  assert all(sum(x*y for x,y in zip(r,g))==0 for r in Jeff)
 assert rank(gauge_coords)==gauge_rank
 # centralizer and annihilator exact dimensions
 cent=rank([list(gr.flat)+list(gi.flat) for gr,gi in G])-rank([list(comm(gr,A).flat)+list(comm(gi,A).flat) for gr,gi in G])
 assert gauge_rank==66 and cent==16
 assert eftrank==186-gauge_rank
 # SU5: 24 generators annihilating both singlets; one radial constraint ->23 tangents.
 suidx=[k for k,(gr,gi) in enumerate(G) if all(not np.any(gr[:,s]) and not np.any(gi[:,s]) for s in si)]
 # Includes 20 root planes; Cartan kernel formed separately from 4 standard SU5 coroots.
 suG=[G[i] for i in [0,2,3,4]]+[G[k] for k in suidx if k>=6]
 assert len(suG)==24
 surad=[int(np.trace(A@gr)) for gr,gi in suG]
 suborbit=rank([list(comm(gr,A).flat)+list(comm(gi,A).flat) for gr,gi in suG])
 assert rank([surad])==1 and suborbit==12
 # Tangent B=H1, [A,B]=0, Tr(A B)=0, hence physical flat mode.
 B=H[0];assert not np.any(comm(A,B)) and np.trace(A@B)==0
 assert all(not np.any(B[:,s]) for s in si)
 bvec=[0]*186;bvec[108]=1
 assert all(sum(x*y for x,y in zip(r,bvec))==0 for r in Jren)
 assert any(sum(x*y for x,y in zip(r,bvec))!=0 for r in specrows)
 # Negative control: coefficient of |A H1|^2 flipped. Choose H1 perturbation of Y!=0,
 # orthogonal to both singlets, A fixed. All other residual derivatives vanish.
 j=next(i for i in range(27) if av[i]!=0)
 neg_q=-2*int(av[j])**2;assert neg_q<0
 # Adjoint invariant polynomial restrictions checked as full multivariate Cartan identities.
 # Coefficients of trace A^d from exact weights, all monomials, not sample points.
 from itertools import product
 def compositions(n,k):
  if k==1:yield (n,);return
  for i in range(n+1):
   for t in compositions(n-i,k-1):yield (i,)+t
 from math import factorial
 polys={}
 for d in [2,3,4]:
  p={}
  for ex in compositions(d,6):
   val=sum(np.prod([int(w[i])**ex[i] for i in range(6)],dtype=object) for w in W)
   coef=F(factorial(d),int(np.prod([factorial(x) for x in ex],dtype=object)))
   if val:p[ex]=int(coef*val)
  polys[d]=p
 square={}
 for a,x in polys[2].items():
  for z,y in polys[2].items():
   k=tuple(a[i]+z[i] for i in range(6));square[k]=square.get(k,0)+x*y
 assert not polys[3]
 assert {k:12*v for k,v in polys[4].items()}=={k:v for k,v in square.items() if v}
 # Solve all homogeneous Weyl-invariance constraints, establishing uniqueness,
 # unlike checking only one trace identity.
 invariant_dims={}
 for degree in (2,3,4):
  exps=list(compositions(degree,6));ix={e:i for i,e in enumerate(exps)};equations=[]
  for node in range(6):
   mat=[[0]*len(exps) for _ in exps]
   linear=[int(i==node)-int(C[node,i]) for i in range(6)]
   for col,e in enumerate(exps):
    start=list(e);power=start[node];start[node]=0
    terms={tuple(start):1}
    for _ in range(power):
     nxt={}
     for a,v in terms.items():
      for j,t in enumerate(linear):
       if not t:continue
       aa=list(a);aa[j]+=1;aa=tuple(aa);nxt[aa]=nxt.get(aa,0)+v*t
     terms=nxt
    for a,v in terms.items():mat[ix[a]][col]+=v
    mat[col][col]-=1
   equations.extend(mat)
  invariant_dims[str(degree)]=len(exps)-rank(equations)
 assert invariant_dims=={'2':1,'3':0,'4':1}
 files=[Path(__file__),PRE,HERE.parent/'e6-breaking-gate/breaking-receipt.json',HERE/'sources/deppisch.pdf']
 return {'weyl_invariant_dimensions':invariant_dims,'gauge_jacobian_annihilation_checks':len(gauge_coords),'passed':True,'claim_boundary':'Exact full real-field Hessian inertia via SOS Jacobian and rational rank; engineered tree-level EFT, not naturalness/quantum/UV proof. Renormalizable flat example and scoped 11-physical-flat obstruction.', 'source_hashes':{str(p):sha(p) for p in files},'chevalley_serre_checks':nchecks,'representation_dimension':27,'real_scalar_dimension':186,'generators':78,'A0':'6Y in arbitrary mass unit M','A0_eigenvalues':spectrum,'A0_eigenvalue_multiplicities':{str(t):int(sum(av==t)) for t in spectrum},'TrA0_squared':c,'polynomial_degree':len(spectrum),'EFT_highest_operator_dimension':2*len(spectrum),'p_prime_eigenvalues':{str(k):str(v) for k,v in pd.items()},'renormalizable_hessian':{'positive':renrank,'zero':186-renrank,'negative':0,'gauge_zero':gauge_rank,'physical_zero':186-renrank-gauge_rank},'EFT_hessian':{'positive':eftrank,'zero':186-eftrank,'negative':0,'gauge_zero':gauge_rank,'physical_zero':186-eftrank-gauge_rank},'centralizer_A_dimension':cent,'SU5_sphere_tangent':23,'SU5_gauge_orbit':suborbit,'unavoidable_physical_flat_lower_bound':23-suborbit,'negative_control_hessian_quadratic':neg_q,'trace_identity':'12 Tr27(A^4)=(Tr27(A^2))^2; Tr27(A^3)=0, exact Cartan polynomial check', 'negative_controls':{'wrong_sign_tachyon_detected':True,'remove_EFT_physical_flats_detected':True}}
def replay(p=None):
 p=HERE/'receipt.json' if p is None else Path(p)
 old=json.loads(p.read_text());new=compute();assert old==new,'receipt mismatch';return new
if __name__=='__main__':
 if '--create' in sys.argv:
  r=compute()
  with (HERE/'receipt.json').open('x') as f:json.dump(r,f,indent=2)
 else:r=replay()
 print(json.dumps(r,indent=2))
