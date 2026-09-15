"""Actual-tensor hypothesis audit. NumPy double precision, no shell rounding."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np
import importlib.util,json,hashlib,sys
from pathlib import Path
P=Path(__file__).resolve().parent;ROOT=P.parent
sys.dont_write_bytecode=True
def load(path,name):
 sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
M=load(ROOT/'shifted-vacuum-gate/calculation.py','action_identity')
S=load(ROOT/'adjoint-radial-pole-gate/calculation.py','tensors_identity')
def compute():
 x,B,c,R,_,_,_=M.setup();_,grad,H,J,f=M.tree(x,B,c)
 h=np.zeros(188);h[108:186]=x[108:186]/np.linalg.norm(x[108:186]);rho=4320.
 T,U=S.tree_tensors(M,x,B,c,h)
 K=R@x;L=R@h;am,V=np.linalg.eigh(K@K.T);good=am>1e-8
 a=am[good];VV=V[:,good];Kr=VV.T@K;Lr=VV.T@L
 Rr=np.einsum('ka,kij->aij',VV,R);G=Kr.T/np.sqrt(a)
 Z=Kr@Lr.T
 eig,E=np.linalg.eigh(H);positive=eig>1e-8
 Hplus=(E[:,positive]/eig[positive])@E[:,positive].T
 def cubic_vv(v):
  bv=B@v
  return 4*bv.T@(J@v)+2*J.T@(bv@v)
 tau=np.column_stack([cubic_vv(g) for g in G.T]);thh=cubic_vv(h)
 d=-Hplus@tau;sig=thh@d
 q=np.einsum('ia,ij,ja->a',G,U,G)
 ell=np.einsum('ai,ij,aj->a',Lr,H-rho*np.eye(188),Lr)
 RK=np.einsum('aij,aj->ai',Rr,Kr).T
 stab=M.null(K.T);smR=np.einsum('ak,aij->kij',stab,R)
 SP=M.null(np.concatenate((smR.reshape(-1,188),K),axis=0))
 sing_inv=SP@np.linalg.inv(SP.T@H@SP)@SP.T
 shells=[]
 # Degeneracy grouping only for invariant tadpoles; raw masses enter all Ward tests.
 for shell in np.unique(np.round(a,7)):
  ids=np.where(abs(a-shell)<1e-6)[0];tt=tau[:,ids].sum(axis=1);ds=-sing_inv@tt
  shells.append({'mass2_display':float(shell),'multiplicity':len(ids),'sigma_sum':float(thh@ds),'quartic_sum':float(q[ids].sum()),'ell_over_a_sum':float((2*ell[ids]/a[ids]).sum()),'stationary_residual':float(np.linalg.norm(H@ds+tt)),'combined_A_coefficient_residual':float(q[ids].sum()+thh@ds-(2*ell[ids]/a[ids]).sum())})
 checks={
 'stationary_gradient':float(np.linalg.norm(grad)),
 'radial_eigenvector':float(np.linalg.norm(H@h-rho*h)),
 'unbroken_h_invariant':float(np.linalg.norm(V[:,~good].T@L)),
 'Goldstone_orthonormal':float(np.linalg.norm(G.T@G-np.eye(len(a)))),
 'H_K':float(np.linalg.norm(H@K.T)),
 'differentiated_Ward':float(np.linalg.norm(T@K.T+H@L.T-rho*L.T)),
 'Z_symmetry':float(np.linalg.norm(Z-Z.T)),
 'twice_differentiated_Ward':float(np.linalg.norm(U@K.T+2*T@L.T-(R@thh).T)),
 'Goldstone_tadpole_Ward':float(np.linalg.norm(tau*a+H@RK)),
 'stationary_solve_individual':float(np.linalg.norm(H@d+tau)),
 'shift_kernel_compatibility':float(np.linalg.norm(thh@(np.eye(188)-Hplus@H)@RK/a)),
 'quartic_plus_shift_Ward':float(np.linalg.norm(q+sig-2*ell/a)),
 't_hh_kernel_projection':float(np.linalg.norm((np.eye(188)-Hplus@H)@thh)),
 'all_shell_stationarity':max(z['stationary_residual'] for z in shells),
 'all_shell_A_coefficients':max(abs(z['combined_A_coefficient_residual']) for z in shells)}
 # Independent off-stationary checks of the action identity, not assigned Ward vertices.
 rng=np.random.default_rng(9713)
 off=[]
 for scale in (.001,.1):
  y=x+scale*rng.normal(size=188);_,gy,Hy,_,_=M.tree(y,B,c)
  off.append(float(np.linalg.norm((Hy@(R@y).T).T-R@gy)))
 assert max(checks.values())<1e-6,checks
 assert max(off)<1e-6,off
 assert any(abs(z['sigma_sum'])>1 for z in shells)
 assert np.linalg.norm(Z)>1
 inputs=[ROOT/'shifted-vacuum-gate/calculation.py',ROOT/'adjoint-radial-pole-gate/calculation.py',ROOT/'radiative-vacuum-gate/diagnostic.py',ROOT/'adjoint-radial-rxi-pole-gate/calculation.py',ROOT/'adjoint-radial-rxi-pole-gate/symbolic_checks.py',ROOT/'adjoint-radial-rxi-pole-gate/REPORT.md',Path(__file__)]
 return {'passed':True,'claim_boundary':'Double-precision verification of all hypotheses used by exact abstract identity; neither interval enclosure nor exact invariant tensor reconstruction.',
 'dimensions':{'scalar':188,'vector':79,'Goldstone':len(a),'physical':188-len(a)},'raw_mass_shell_rounding_for_Ward':False,'checks':checks,'off_stationary_action_Ward_norms':off,'shells':shells,'Z_frobenius_squared':float(np.sum(Z*Z)),
 'source_hashes':{str(z.relative_to(ROOT)):hashlib.sha256(z.read_bytes()).hexdigest() for z in inputs}}
if __name__=='__main__':
 o=compute();target=P/'tensor_receipt.json'
 if '--create' in sys.argv:
  with target.open('x') as f:json.dump(o,f,indent=2)
 else:assert json.loads(target.read_text())==o,'saved tensor receipt mismatch'
 print(json.dumps(o,indent=2))
