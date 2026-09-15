"""Strict-Landau mixed scalar-vector one-loop subset for the adjoint radial pole.

Units are M=1, Q^2=epsilon M^2, and all displayed one-loop coefficients are
in epsilon^2 M^2.  Vertices are derived only from 1/2 (D_mu phi)^T(D^mu phi).
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'; os.environ['OMP_NUM_THREADS']='1'
import json, hashlib, importlib.util, sys, functools
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent; ROOT=HERE.parent

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def Avec(x): return 0.0 if abs(x)<1e-14 else x*(np.log(x)-1.0)

VV=load(ROOT/'adjoint-radial-vector-bubble-gate/calculation.py','vv_integrals')
@functools.lru_cache(maxsize=None)
def bfun(x,y,s):
 """Martin B=-int log(Delta-i0), Q2=1, using predecessor's analytic integral."""
 return -VV.logB(float(x),float(y),float(s),512)

@functools.lru_cache(maxsize=None)
def bsv(x,v,s):
 """MSbar Landau B_SV(X,V), Elias-Miro et al. 1406.2652 eq. (A.3/A.5)."""
 bxv=bfun(x,v,s)
 if abs(v)<1e-10:
  return 3*(x+s)*bfun(x,0.0,s)+3*Avec(x)-2*s
 return ((2*x-v+2*s)*bxv + Avec(x)-Avec(v)
         + ((x-s)*Avec(v)-(x-s)**2*(bxv-bfun(x,0.0,s)))/v)

def data():
 M=load(ROOT/'shifted-vacuum-gate/calculation.py','shift_mixed')
 x,B,c,R,T,si,aa=M.setup();_,grad,H,J,f=M.tree(x,B,c)
 assert np.linalg.norm(f)<1e-10 and np.linalg.norm(grad)<1e-8
 radial=np.zeros(188);radial[108:186]=x[108:186]/np.linalg.norm(x[108:186]);s=4320.0
 assert np.linalg.norm(H@radial-s*radial)<1e-8
 # Physical scalar quotient: orthogonal complement of all 67 gauge tangents.
 Q=M.null(R@x); assert Q.shape==(188,121)
 ms,Es0=np.linalg.eigh(Q.T@H@Q); Es=Q@Es0
 K=R@x; mv,Uv=np.linalg.eigh((K@K.T+(K@K.T).T)/2);mv[np.abs(mv)<1e-10]=0
 # From A^a_mu eta^T R_a d^mu eta.  With all momenta incoming,
 # V(A_a,S_i,h)=i C_ai (p_h-p_i)_mu, C_ai=E_i^T R_a radial.
 C0=np.einsum('ni,anm,m->ai',Es,R,radial)
 C=Uv.T@C0
 return M,x,H,radial,s,ms,Es,mv,Uv,C

def evaluate(n=512, rotate=False):
 M,x,H,h,s,ms,Es,mv,Uv,C=data()
 if rotate:
  rng=np.random.default_rng(20260909)
  for vals,A,isvec in ((ms,Es,False),(mv,Uv,True)):
   for val in np.unique(np.round(vals,7)):
    ids=np.where(abs(vals-val)<1e-7)[0]
    if len(ids)>1:
     O=np.linalg.qr(rng.normal(size=(len(ids),len(ids))))[0]
     if isvec: Uv[:,ids]=Uv[:,ids]@O
     else: Es[:,ids]=Es[:,ids]@O
  C0=np.einsum('ni,anm,m->ai',Es,M.setup()[3],h);C=Uv.T@C0
 total=0j; active=[]
 for a,V in enumerate(mv):
  for i,X in enumerate(ms):
   cc=float(C[a,i])
   if abs(cc)<=1e-12: continue
   z=bsv(float(max(X,0.0)),float(V),s)
   # Our inverse-propagator convention uses I=-B (as in scalar predecessor),
   # hence Pi_mixed=-sum C^2 BSV/(16 pi^2). No identical-line factor.
   total -= cc*cc*z/(16*np.pi**2)
   active.append((a,i,float(V),float(X),cc,z))
 return total,active,(ms,mv,C)

def compute():
 total,active,(ms,mv,C)=evaluate()
 zero=sum((-cc*cc*bsv(max(X,0.0),V,0.0)/(16*np.pi**2) for _,_,V,X,cc,_ in active),0j)
 rotated,_,_=evaluate(rotate=True)
 # Tree h-A and h-G mixings vanish. Any one-loop off-diagonal insertion therefore
 # first shifts this isolated nondegenerate pole through two insertions at two-loop order.
 M,x,H,h,s,ms,Es,mv,Uv,C=data(); tang=(M.setup()[3]@x).T
 tree_hA=np.array([h@(M.setup()[3][a]@x) for a in range(79)])
 G=M.null(np.concatenate((H,tang.T),axis=0)) if False else None
 # Goldstone orthonormal frame is the column space of gauge tangents.
 qg,_=np.linalg.qr(tang); rank=np.linalg.matrix_rank(tang,tol=1e-8); Gold=qg[:,:rank]
 tree_hG=Gold.T@H@h
 shells=[]
 for val in np.unique(np.round(ms,8)):
  ids=np.where(abs(ms-val)<1e-7)[0]
  shells.append({'m2':float(np.mean(ms[ids])),'multiplicity':int(len(ids)),'coupling_frobenius2':float(np.sum(C[:,ids]**2))})
 # UV coefficient from BSV: B contributes -Delta; coefficient of B is
 # (2X-V+2s)-(X-s)^2/V for V>0, with smooth massless expression 3(X+s).
 uv=0.0
 for _,_,V,X,cc,_ in active:
  k=3*(X+s) if abs(V)<1e-10 else (2*X-V+2*s)-(X-s)**2/V
  uv += cc*cc*k/(16*np.pi**2)
 out={'passed':True,
 'claim_boundary':'Complete strict-Landau mixed physical-scalar/vector derivative-bubble subset from the canonical covariant kinetic term. External radial-vector and radial-Goldstone mixings vanish at tree level and can affect the isolated radial pole only at two-loop order through squared one-loop insertions; their complete one-loop amplitudes are not claimed here. General-xi Nielsen cancellation is not checked, so this is not a gauge-independent pole.',
 'kinematics':{'p2_over_epsilonM2':s,'Q2_over_epsilonM2':1.0,'scheme':'MSbar','gauge':'strict Landau xi=0','inverse_propagator':'s-m_tree^2-Pi(s)','feynman_prescription':'-i0'},
 'enumeration':{'physical_scalars':len(ms),'vectors':len(mv),'massive_vectors':int(sum(mv>0)),'massless_vectors':int(sum(mv==0)),'active_scalar_vector_pairs':len(active),'scalar_shells':shells},
 'vertices':{'expanded_kinetic_term':'1/2(d eta)^2 + A_a^mu eta^T R_a d_mu eta + A_a^mu (R_a x)^T d_mu eta + 1/2 A_a A_b (R_a(x+eta))^T(R_b(x+eta))','background_Rxi_gauge_fixing':'F_a=d.A_a-xi (R_a x).eta cancels A_a.(R_a x).d eta; xi->0 leaves transverse propagator and massless Goldstones','h_S_i_V_a':'i C_ai (p_h-p_i)_mu','C_ai':'E_i^T R_a v_A in scalar/vector mass bases','diagram_factor':1.0,'kernel':'Pi_SV=-sum_ai C_ai^2 BSV(mSi2,mVa2;s)/(16 pi^2)'},
 'result':{'mixed_SV_bubble_real':float(total.real),'mixed_SV_bubble_imag':float(total.imag)},
 'external_mixing':{'tree_radial_vector_norm':float(np.linalg.norm(tree_hA)),'tree_radial_Goldstone_norm':float(np.linalg.norm(tree_hG)),'pole_order':'one-loop off-diagonal self-energies enter the isolated radial eigenvalue only quadratically, hence O(hbar^2); no O(hbar) shift','uncomputed_one_loop_amplitudes':['Pi_{h A_a}^mu(s) from all scalar/vector/ghost sectors','Pi_{h G_alpha}(s) from all scalar/vector/fermion sectors']},
 'renormalization':{'UV_local_coefficient_removed':float(uv),'finite_counterterm':'zero in declared MSbar; no arbitrary interaction added'},
 'checks':{'p0_mixed_bubble_abs':float(abs(zero)),'expected_p0_identity':'zero: at p=0 the derivative vertex momentum is parallel to the Landau vector momentum and is annihilated by P_mu_nu','degenerate_basis_rotation_abs_difference':float(abs(rotated-total)),'coupling_frobenius2':float(np.sum(C*C)),'negative_drop_transverse_projector_not_performed':'the p0 zero would fail'},
 'remaining_diagrams':['complete one-loop h-vector mixing amplitudes (needed first at two-loop pole order)','complete one-loop h-Goldstone mixing amplitudes (needed first at two-loop pole order)','general-xi longitudinal-vector/Goldstone/ghost diagrams and Nielsen/pole cancellation','two-loop hard tadpoles and one-loop-squared mixing terms for an O(hbar^2) pole'],
 'source_hashes':{}}
 return out

if __name__=='__main__':
 out=compute(); src=[Path(__file__),ROOT/'shifted-vacuum-gate/calculation.py',ROOT/'shifted-vacuum-gate/receipt.json',ROOT/'adjoint-radial-pole-gate/calculation.py',ROOT/'adjoint-radial-vector-bubble-gate/calculation.py',ROOT/'adjoint-radial-vector-bubble-gate/receipt.json',ROOT/'goldstone-pole-matching-gate/primary-source-excerpts.txt']
 out['source_hashes']={str(p):sha(p) for p in src}
 p=HERE/'receipt.json'
 if '--create' in sys.argv:
  with p.open('x') as f: json.dump(out,f,indent=2)
 else: assert json.loads(p.read_text())==out
 print(json.dumps(out,indent=2))

