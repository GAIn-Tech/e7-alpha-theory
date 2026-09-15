"""Finite-momentum strict-Landau transverse VV bubble for the adjoint radial mode.
Units: M=1, Q^2=epsilon M^2; masses and s are divided by epsilon M^2.
Only the canonical 1/2 A M^2(phi) A interactions are used.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'; os.environ['OMP_NUM_THREADS']='1'
import json, hashlib, importlib.util, sys
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent; ROOT=HERE.parent

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

_GL={}
def logB(a,b,s,n=512):
 """I(a,b;s)=int_0^1 log[x a+(1-x)b-s*x(1-x)-i0] dx."""
 if a==0 and b==0 and s>0: return complex(np.log(s)-2,-np.pi)
 if s>0:
  rr=np.sort(np.roots([s,a-b-s,b]).real)
  def F(r):
   t=0.0
   if abs(1-r)>0: t+=(1-r)*np.log(abs(1-r))
   if abs(r)>0: t+=r*np.log(abs(r))
   return t-1.0
  neg=max(0.0,min(1.0,rr[1])-max(0.0,rr[0]))
  return complex(np.log(s)+F(rr[0])+F(rr[1]),-np.pi*neg)
 if n not in _GL:
  z,w=np.polynomial.legendre.leggauss(n); _GL[n]=((z+1)/2,w/2)
 u,w=_GL[n]
 roots=np.roots([s,a-b-s,b]) if s else []
 cuts=[0.0]+sorted(float(r.real) for r in roots if abs(r.imag)<1e-11 and 0<r.real<1)+[1.0]
 ans=0j
 for lo,hi in zip(cuts,cuts[1:]):
  x=lo+(hi-lo)*u
  # long-double evaluation avoids an accidental exact zero from cancellation when a
  # Gauss node lies extremely close to a threshold root (the logarithm is integrable).
  xl=x.astype(np.longdouble)
  if a==0: d=(1-xl)*(np.longdouble(b)-np.longdouble(s)*xl)
  elif b==0: d=xl*(np.longdouble(a)-np.longdouble(s)*(1-xl))
  else: d=xl*np.longdouble(a)+(1-xl)*np.longdouble(b)-np.longdouble(s)*xl*(1-xl)
  ad=abs(d); ad=np.where(ad==0,np.longdouble(max(a,b,s,1.0)*(hi-lo)/(n*n)),ad)
  ans += (hi-lo)*np.sum(w*np.log(ad).astype(float))
  mid=(lo+hi)/2
  if mid*a+(1-mid)*b-s*mid*(1-mid)<0: ans -= 1j*np.pi*(hi-lo)
 return complex(ans)

def Avec(a): return 0.0 if a==0 else a*(np.log(a)-1)

def kernel(a,b,s,n=512,cache=None):
 """MSbar finite contraction of two d-dimensional Landau projectors.
 P(k):P(k+p)=d-2+(k.(k+p))^2/[k^2(k+p)^2].
 The +2 is the evanescent (-2 eps) times the UV pole in our I=+int log convention.
 Formula is used only for a,b>0; the canonical radial D has no massless rows/columns.
 """
 def B(x,y):
  key=(round(x,12),round(y,12),round(s,12),n)
  if cache is not None and key in cache:return cache[key]
  v=logB(x,y,s,n)
  if cache is not None:cache[key]=v
  return v
 Bab,Ba0,B0b,B00=B(a,b),B(a,0.0),B(0.0,b),B(0.0,0.0)
 X=(Avec(b)+a*Bab-a*Ba0)/b
 Y=(Avec(a)+b*Bab-b*B0b)/a
 U=(Bab-B0b)/a; V=(Bab-Ba0)/b
 W=(Bab-B0b-Ba0+B00)/(a*b)
 return 2*Bab+0.25*(X+Y+2*Bab-2*s*(U+V)+s*s*W)+2.0

def compute(n=512):
 M=load(ROOT/'shifted-vacuum-gate/calculation.py','shift_vv')
 x,B,c,R,T,si,aa=M.setup(); _,grad,H,J,f=M.tree(x,B,c)
 assert np.linalg.norm(f)<1e-10 and np.linalg.norm(grad)<1e-8
 v=np.zeros(188); v[108:186]=x[108:186]/np.linalg.norm(x[108:186]); s=4320.0
 assert np.linalg.norm(H@v-s*v)<1e-8
 K=R@x; dK=R@v; MV=K@K.T
 D=dK@K.T+K@dK.T; Q=2*dK@dK.T
 mass,U=np.linalg.eigh((MV+MV.T)/2); mass[np.abs(mass)<1e-10]=0
 De=U.T@D@U; Qe=U.T@Q@U; iz=np.where(mass==0)[0]
 touch=np.zeros_like(De,dtype=bool); touch[iz,:]=True; touch[:,iz]=True
 massless_touch=float(np.linalg.norm(De[touch])); assert massless_touch<1e-9
 cache={}; total=0j; active=[]; open_channels=0
 for i,a in enumerate(mass):
  if a<=0: continue
  for j,b in enumerate(mass):
   if b<=0 or abs(De[i,j])<=1e-12: continue
   kval=kernel(float(a),float(b),s,n,cache); total += De[i,j]**2*kval
   disc=(s-a-b)**2-4*a*b
   isopen=s>(np.sqrt(a)+np.sqrt(b))**2
   open_channels += int(isopen)
   active.append((i,j,float(a),float(b),float(De[i,j]),kval,isopen,disc))
 bubble=total/(32*np.pi**2) # 1/2 identical-vertex symmetry factor; ordered eigenstate sum
 # p=0 analytic kernel: 3 I(a,b;0)+2 = (3/2)[f'(a)-f'(b)]/(a-b).
 zero=0.0
 for i,a in enumerate(mass):
  if a<=0: continue
  for j,b in enumerate(mass):
   if b<=0: continue
   zero += De[i,j]**2*(3*logB(float(a),float(b),0.0,n).real+2)
 zero/=32*np.pi**2
 fp=np.zeros_like(mass); pos=mass>0; fp[pos]=mass[pos]*(2*np.log(mass[pos])-2/3)
 L=np.zeros((79,79))
 for i,a in enumerate(mass):
  for j,b in enumerate(mass):
   if a>0 and b>0:L[i,j]=2*np.log(a)+4/3 if abs(a-b)<1e-8*max(1,a,b) else (fp[i]-fp[j])/(a-b)
 cw_bubble=3*np.sum(L*De*De)/(64*np.pi**2)
 seagull=3*float(fp@np.diag(Qe))/(64*np.pi**2)
 uv=3*float(np.sum(De*De))/(64*np.pi**2)
 # rotate each degenerate shell, recompute contraction from shell-invariant kernel matrix
 rng=np.random.default_rng(1901); Ur=U.copy()
 for val in np.unique(np.round(mass,7)):
  ids=np.where(abs(mass-val)<1e-7)[0]
  if len(ids)>1: Ur[:,ids]=U[:,ids]@np.linalg.qr(rng.normal(size=(len(ids),len(ids))))[0]
 Dr=Ur.T@D@Ur; rotated=0j
 for i,a in enumerate(mass):
  if a>0:
   for j,b in enumerate(mass):
    if b>0 and abs(Dr[i,j])>1e-12: rotated += Dr[i,j]**2*kernel(float(a),float(b),s,n,cache)
 rotated/=32*np.pi**2
 shells=[]
 for val in np.unique(np.round(mass,8)):
  ids=np.where(abs(mass-val)<1e-7)[0]; shells.append({'m2':float(np.mean(mass[ids])),'multiplicity':int(len(ids)),'D_block_frobenius2':float(np.sum(De[np.ix_(ids,ids)]**2))})
 return {'passed':True,'claim_boundary':'Finite-momentum transverse vector-vector bubble and momentum-independent vector seagull from the canonical mass term in strict Landau gauge. Mixed scalar-vector derivative bubbles, external mixing, and general-xi cancellation remain; this is not a full, physical, or gauge-independent pole.',
 'kinematics':{'p2_over_epsilonM2':s,'Q2_over_epsilonM2':1.0,'feynman_prescription':'-i0','inverse_propagator':'s-m_tree^2-Pi(s)'},
 'enumeration':{'vectors':79,'massive':int(sum(mass>0)),'massless':int(sum(mass==0)),'mass_shells':shells,'active_ordered_D_pairs':len(active),'open_ordered_threshold_channels':open_channels,'massless_D_row_column_norm':massless_touch},
 'vertices':{'D_A':'(R v_A)(R x)^T+(R x)(R v_A)^T','Q_AA':'2(R v_A)(R v_A)^T','hAA_feynman_rule':'i D_A,ab g_mn','hhAA_feynman_rule':'i Q_AA,ab g_mn','bubble_symmetry_factor':0.5},
 'result':{'transverse_VV_bubble_real':float(bubble.real),'transverse_VV_bubble_imag':float(bubble.imag),'vector_seagull_momentum_independent':seagull,'bubble_plus_seagull_real':float(bubble.real+seagull),'bubble_plus_seagull_imag':float(bubble.imag)},
 'renormalization':{'scheme':'MSbar','finite_kernel':'K=2Iab+[X+Y+2Iab-2s(U+V)+s^2W]/4+2','UV_local_bubble_coefficient_removed':uv,'note':'The +2 is the d=4-2eps evanescent projector contribution; no finite local mass counterterm is added.'},
 'checks':{'quadrature_n':n,'p0_direct_bubble':zero,'p0_vector_CW_Hessian_bubble':float(cw_bubble),'p0_abs_difference':abs(zero-cw_bubble),'degenerate_basis_rotation_abs_difference':abs(rotated-bubble)},
 'ghost':{'xi':0,'direct_radial_ghost_vertex':0.0,'boundary':'Background-Rxi FP scalar vertices are proportional to xi and vanish only in the strict xi->0 boundary; no general-xi cancellation is claimed.'},
 'remaining':['mixed scalar-vector derivative bubbles','external scalar-vector pole determinant mixing','general-xi longitudinal/Goldstone/ghost cancellation'],'source_hashes':{}}

if __name__=='__main__':
 out=compute(512); low=compute(256)
 out['checks']['independent_256_vs_512_abs_difference']=abs(complex(out['result']['transverse_VV_bubble_real'],out['result']['transverse_VV_bubble_imag'])-complex(low['result']['transverse_VV_bubble_real'],low['result']['transverse_VV_bubble_imag']))
 src=[Path(__file__),ROOT/'adjoint-radial-gauge-pole-gate/calculation.py',ROOT/'adjoint-radial-gauge-pole-gate/REPORT.md',ROOT/'adjoint-radial-pole-gate/calculation.py',ROOT/'goldstone-pole-matching-gate/SOURCE_NOTES.md',ROOT/'shifted-vacuum-gate/calculation.py']
 out['source_hashes']={str(p):sha(p) for p in src}; p=HERE/'receipt.json'
 if '--create' in sys.argv:
  with p.open('x') as f: json.dump(out,f,indent=2)
 else: assert json.loads(p.read_text())==out
 print(json.dumps(out,indent=2))

