import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import sys,json,hashlib,importlib.util,functools
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent; ROOT=P.parent
sys.path.insert(0,str(ROOT/'adjoint-radial-pole-convergence-gate/vendor'))
import mpmath as mp
mp.mp.dps=60

def load(p,n):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
S=load(ROOT/'adjoint-radial-pole-gate/calculation.py','scalar_rxi')
M=load(ROOT/'shifted-vacuum-gate/calculation.py','action_rxi')
HP=load(ROOT/'adjoint-radial-pole-convergence-gate/verify.py','hp_rxi')
x,B,c,R,_,_,_=M.setup(); _,grad,H,J,f=M.tree(x,B,c)
h=np.zeros(188);h[108:186]=x[108:186]/np.linalg.norm(x[108:186])
T,U=S.tree_tensors(M,x,B,c,h);K=R@x;L=R@h
mv,V=np.linalg.eigh(K@K.T); mv[np.abs(mv)<1e-8]=0
D=V.T@(L@K.T+K@L.T)@V; Q=V.T@(2*L@L.T)@V; Z=V.T@(K@L.T)@V
s=mp.mpf(4320);fac=32*mp.pi**2
@functools.lru_cache(None)
def I(a,b):return HP.integral(a,b)
def A(a):return mp.mpf(a)*(mp.log(a)-1) if a else mp.mpf(0)
def r(a):return round(float(a),8) if abs(a)>1e-8 else 0.
def moments(a,b):
 a,b=map(mp.mpf,(a,b)); z=I(a,b)
 return z,A(b)+a*z,A(a)+b*z,(b+s+a)*A(b)+a*a*z,(a+s+b)*A(a)+b*b*z,a*A(a)+b*A(b)+a*b*z
@functools.lru_cache(None)
def vv(a,b,xi):
 a,b,xi=map(mp.mpf,(a,b,xi));z,u,v,u2,v2,uv=moments(a,b)
 def j(c,d):
  z,u,v,u2,v2,uv=moments(c,d);return (u2+v2+2*uv-2*s*(u+v)+s*s*z)/4
 return 4*z+2-(u-moments(xi*a,b)[1])/a-(v-moments(a,xi*b)[2])/b+(j(a,b)-j(xi*a,b)-j(a,xi*b)+j(xi*a,xi*b))/(a*b)
@functools.lru_cache(None)
def sv(a,b,xi):
 a,b,xi=map(mp.mpf,(a,b,xi)) # vector, scalar
 z,u,v,u2,v2,uv=moments(a,b)
 def j(a):
  z,u,v,u2,v2,uv=moments(a,b);return s*s*z-2*s*v+v2
 # d-dimensional evanescent finite term is independent of xi and included by Landau matching.
 return (2*s*z+2*v-u)-(j(a)-j(xi*a))/a

def weighted(ms,E,xi):
 t=E.T@T@E;C=V.T@L@E
 bins={}; binsv={}
 for i,a in enumerate(ms):
  for j,b in enumerate(ms):
   w=float(t[i,j]**2)
   if w>1e-18: bins[r(a),r(b)]=bins.get((r(a),r(b)),0)+w
 for a,v in enumerate(mv):
  for i,b in enumerate(ms):
   w=float(C[a,i]**2)
   if w>1e-18:
    assert v>1e-8
    binsv[r(v),r(b)]=binsv.get((r(v),r(b)),0)+w
 scalar=sum(mp.mpf(w)*I(a,b) for (a,b),w in bins.items())/fac
 mixed=-2*sum(mp.mpf(w)*sv(a,b,xi) for (a,b),w in binsv.items())/fac
 return scalar,mixed

def pack(z):return {'real':float(mp.re(z)),'imag':float(mp.im(z))}
def compute():
 base_m,base_E=np.linalg.eigh(H);base_m=np.array([r(a) for a in base_m]);base=weighted(base_m,base_E,0)
 stab=M.null(K.T);smR=np.einsum('ak,aij->kij',stab,R);SP=M.null(np.concatenate((smR.reshape(-1,188),K),axis=0))
 t_hh=np.array([h@S.tree_tensors(M,x,B,c,np.eye(188)[j])[0]@h for j in range(188)])
 ward=float(np.linalg.norm(T@K.T+H@L.T-s*L.T))
 rows=[]
 assert ward<1e-7
 assert np.linalg.norm(H@K.T)<1e-7
 assert np.linalg.norm(D-Z-Z.T)<1e-10
 gap=float(min(abs(v-4320) for v in base_m if abs(v-4320)>1e-6))
 for xi in (.1,1.,3.,100.):
  ms,E=np.linalg.eigh(H+xi*K.T@K);ms=np.array([r(a) for a in ms]);sc,mix=weighted(ms,E,xi)
  Aval=np.array([float(A(a)) for a in ms]);Abase=np.array([float(A(a)) for a in base_m]); W=(E*Aval)@E.T-(base_E*Abase)@base_E.T
  scalar_tad=mp.mpf(float(np.sum(U*W.T)))/fac
  tad=(4*np.einsum('rij,rj->i',B,J@W)+2*J.T@np.einsum('ij,rji->r',W,B))/(32*np.pi**2)
  delta=-SP@np.linalg.solve(SP.T@H@SP,SP.T@tad);shift=float(t_hh@delta)
  vvb=mp.mpc(0);gh=mp.mpc(0);vs=mp.mpf(0)
  for a,ma in enumerate(mv):
   if ma<1e-8:continue
   aa=r(ma);vs+=mp.mpf(float(Q[a,a]))*xi*A(xi*mp.mpf(aa))/fac
   for b,mb in enumerate(mv):
    if mb<1e-8:continue
    bb=r(mb)
    if abs(D[a,b])>1e-10:vvb+=mp.mpf(float(D[a,b]**2))*(vv(aa,bb,xi)-vv(aa,bb,0))/fac
    if abs(Z[a,b]*Z[b,a])>1e-15:gh-=2*mp.mpf(float(Z[a,b]*Z[b,a]))*xi*xi*I(mp.mpf(xi)*aa,mp.mpf(xi)*bb)/fac
  channels={'scalar_bubble':sc-base[0],'scalar_seagull':scalar_tad,'mixed':mix-base[1],'vector_bubble':vvb,'vector_seagull':vs,'ghost':gh,'stationary_shift':shift}
  total=sum(channels.values());rows.append({'xi':xi,'channels':{k:pack(v) for k,v in channels.items()},'sum':pack(total),'Pi_difference_without_shift':pack(total-shift),'unphysical_pole_gap':float(min(abs(4320-xi*v) for v in mv)),'omit_ghost':pack(total-gh),'omit_shift':pack(total-shift),'stationary_equation_residual':float(np.linalg.norm(H@delta+tad))})
 errors=[]
 for a,b in [(0,0),(.1,3),(4320,4320),(1000,1000)]:errors.append(float(abs(I(a,b)-HP.integral(a,b,adaptive=True))))
 assert max(errors)<1e-40
 assert all(abs(complex(z['sum']['real'],z['sum']['imag']))<1e-5 for z in rows)
 assert all(abs(complex(z['omit_ghost']['real'],z['omit_ghost']['imag']))>1e-3 for z in rows)
 inputs=[f for d in ROOT.glob('adjoint-radial-*') if d!=P for f in d.iterdir() if f.suffix in ('.py','.json','.md','.npz')]+[ROOT/'shifted-vacuum-gate/calculation.py']
 return {'input_hashes':{str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest() for f in inputs},'isolated_physical_tree_gap':gap,'claim_boundary':'Action-derived Rxi diagram evaluation; cancellation status computed, not assumed; floating tensors and rounded mass shells, not a formal proof or full pole.','ward_differentiated_residual':ward,'master_adaptive_max_error':max(errors),'rows':rows,'cancellation_passed':all(abs(complex(z['sum']['real'],z['sum']['imag']))<1e-5 for z in rows),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
 out=compute();p=P/'receipt.json'
 if '--create' in sys.argv:
  with p.open('x') as f:json.dump(out,f,indent=2)
 else:assert json.loads(p.read_text())==out
 print(json.dumps(out,indent=2))
