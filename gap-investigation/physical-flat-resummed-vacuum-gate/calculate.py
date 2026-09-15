"""Physical-flat matched tree EFT and bounded next-order stability component.
No assumed higher-loop coefficients; native execution, immutable receipts.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import sys,json,hashlib,importlib.util
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def compute():
 m=load(ROOT/'shifted-vacuum-gate/calculation.py','shifted_flat')
 ir=load(ROOT/'ir-resummed-vacuum-gate/calculation.py','ir_flat');ir.M=m
 inputs=[ROOT/'shifted-vacuum-gate/receipt.json',ROOT/'ir-resummed-vacuum-gate/receipt.json',ROOT/'ir-resummed-vacuum-gate/projected-tensors.json',ROOT/'goldstone-pole-matching-gate/receipt.json',ROOT/'adjoint-radial-perturbative-window-gate/receipt.json']
 for p in inputs:
  d=json.loads(p.read_text())
  for q,h in d.get('source_hashes',{}).items():assert sha(Path(q))==h,(q,'stale input')
 x,B,c,R,T,si,a=m.setup();_,g,H,J,f=m.tree(x,B,c)
 data=json.loads(inputs[2].read_text());F=np.array(data['basis_F']);G=np.array(data['basis_G'])
 z,P=np.linalg.eigh(H);P=P[:,z>1e-7];hz=z[z>1e-7];HI=(P/hz)@P.T
 assert F.shape==(188,11) and G.shape==(188,67) and P.shape==(188,110)
 projectors={'physical_soft':F@F.T,'gauge':G@G.T,'hard':P@P.T}
 pres=max(float(np.linalg.norm(v@v-v,2)) for v in projectors.values())
 closure=float(np.linalg.norm(sum(projectors.values())-np.eye(188),2));assert max(pres,closure)<1e-9
 L,tad,HL=ir.hard(x,B,c,R,np.eye(188));HL=(HL+HL.T)/2
 delta=-HI@tad;dold=np.array(json.loads(inputs[0].read_text())['leading_delta_canonical']);assert np.linalg.norm(delta-dold)<2e-7
 A=ir.tree_dH(x,delta,B)+HL;M1=F.T@A@F;lam,O=np.linalg.eigh(M1)
 ward=float(np.linalg.norm(np.column_stack((G,F)).T@A@G,2));assert ward<2e-7
 P8=F@O[:,:8]@O[:,:8].T@F.T;P3=F@O[:,8:]@O[:,8:].T@F.T
 stab=m.null((R@x).T);smR=np.einsum('ak,aij->kij',stab,R)
 comm=max(float(np.linalg.norm(v@r-r@v,2)) for v in (P8,P3) for r in smR)
 assert comm<1e-8
 # Source polynomial U_abcd and heavy exchange, all four external legs soft.
 b=np.einsum('ia,rij,jb->rab',F,B,F,optimize=True)
 Tab=2*np.einsum('ri,rab->iab',J,b,optimize=True)
 direct=2*np.einsum('rab,rcd->abcd',b,b)
 direct=direct+direct.transpose(0,2,1,3)+direct.transpose(0,3,2,1)
 exchange=np.einsum('iab,ij,jcd->abcd',Tab,HI,Tab,optimize=True)
 exchange=exchange+exchange.transpose(0,2,1,3)+exchange.transpose(0,3,2,1)
 eff=direct-exchange
 assert np.max(abs(eff))<1e-8
 # epsilon^3 log epsilon coefficient from a scalar soft tadpole in matched EFT.
 scalar_log=np.einsum('abcd,cd->ab',eff,M1)/(32*np.pi**2)
 wrong_log=np.einsum('abcd,cd->ab',direct,M1)/(32*np.pi**2)
 assert np.linalg.norm(wrong_log)>1 and np.linalg.norm(scalar_log)<1e-8
 # Full tree-soft cubic vanishes, including GG and mixed gauge/physical lines.
 S=np.column_stack((G,F));softcubic=max(float(np.linalg.norm(S.T@ir.tree_dH(x,v,B)@S)) for v in F.T)
 assert softcubic<1e-8
 # A finite necessary NLO coefficient, not full NLO mass: massive Schur mixing.
 C=P.T@A@F;schur=-C.T@(C/hz[:,None]);assert max(np.linalg.eigvalsh(schur))<1e-8
 # Soft scalar derivative metric: heavy relaxation h=-1/2 H+ T_ab q_a q_b.
 curvature=np.einsum('ij,jab->iab',HI,Tab)
 geom=np.einsum('iab,icd->abcd',curvature,curvature)
 # Residual unbroken Casimir acting on physical flats, from actual 79 generators.
 cas=-sum((F.T@r@F)@(F.T@r@F) for r in smR)
 eigen={ 'leading':lam.tolist(),'negative_heavy_Schur':np.linalg.eigvalsh(schur).tolist(),'unbroken_Casimir':np.linalg.eigvalsh(cas).tolist()}
 # Frame-rotation control on all finite matrices.
 rng=np.random.default_rng(713);V=np.linalg.qr(rng.normal(size=(11,11)))[0]
 rotate=float(np.max(abs(np.linalg.eigvalsh(V.T@M1@V)-lam)));assert rotate<1e-10
 samples=[]
 for eps in [1e-7,1e-5,1e-3]:
  val=eps**4*np.sum(lam**2*(np.log(eps*lam)-1.5))/(64*np.pi**2)
  samples.append({'epsilon':eps,'Gaussian_physical_soft_potential':float(val),'partial_M1_plus_epsilon_Schur_min':float(np.linalg.eigvalsh(M1+eps*schur)[0])})
 mats={'F':F.tolist(),'G':G.tolist(),'P8':P8.tolist(),'P3':P3.tolist(),'M1':M1.tolist(),'negative_heavy_Schur':schur.tolist(),'scalar_epsilon3_log_coefficient':scalar_log.tolist(),'wrong_omit_heavy_exchange_log_coefficient':wrong_log.tolist(),'unbroken_Casimir':cas.tolist(),'tree_matched_quartic':eff.tolist(),'heavy_relaxation_tensor':curvature.tolist()}
 out={'passed':True,'claim_boundary':'Complete physical-soft projectors, matched scalar quartic cancellation and finite heavy-Schur NLO component only; full NLO pole/stationarity coefficient is not computed.','dimensions':[188,67,110,8,3], 'projector_residual':pres,'closure_residual':closure,'Ward_residual':ward,'residual_symmetry_commutator':comm,'tree_soft_cubic_norm':softcubic,'tree_direct_quartic_max':float(np.max(abs(direct))),'tree_matched_quartic_max':float(np.max(abs(eff))),'scalar_epsilon3_log_norm':float(np.linalg.norm(scalar_log)),'omit_exchange_negative_control_norm':float(np.linalg.norm(wrong_log)),'geometric_derivative_tensor_norm':float(np.linalg.norm(geom)),'eigenvalues':eigen,'rotated_frame_eigenvalue_error':rotate,'wrong_self_energy_Ward_norm':float(np.linalg.norm(G.T@(ir.tree_dH(x,delta,B)-HL)@G,2)),'samples':samples,'source_hashes':{str(p):sha(p) for p in inputs+[Path(__file__),ROOT/'shifted-vacuum-gate/calculation.py',ROOT/'ir-resummed-vacuum-gate/calculation.py']}}
 return out,mats
if __name__=='__main__':
 p=HERE/'receipt.json';q=HERE/'matrices.json'
 if '--create' not in sys.argv:
  saved=json.loads(p.read_text());sm=json.loads(q.read_text())
  for f,h in saved['source_hashes'].items():assert sha(Path(f))==h
 out,mat=compute()
 if '--create' in sys.argv:
  with p.open('x') as f:json.dump(out,f,indent=2)
  with q.open('x') as f:json.dump(mat,f)
 else:assert out==saved and mat==sm,'deterministic replay mismatch'
 print(json.dumps(out,indent=2))
