"""Additive recovery audit. Does not execute/overwrite interrupted calculation receipts."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np, json, hashlib, importlib.util, sys, time
from pathlib import Path
P=Path(__file__).resolve().parent; ROOT=P.parent
s=importlib.util.spec_from_file_location('shift',ROOT/'shifted-vacuum-gate/calculation.py');M=importlib.util.module_from_spec(s);s.loader.exec_module(M)
print('setup-start',flush=True)
x,B,c,R,T,si,aa=M.setup(); print('setup-end',flush=True)
_,grad,H,J,f=M.tree(x,B,c)
h=np.zeros(188);h[108:186]=x[108:186]/np.linalg.norm(x[108:186])
K=R@x; dK=R@h
# SVD, not unpivoted QR: generator columns contain dependent/unbroken directions.
u,z,vh=np.linalg.svd(K,full_matrices=True); rank=int(sum(z>1e-8)); G=vh[:rank].T; E=vh[rank:].T
ms,Us=np.linalg.eigh(H); mv,Uv=np.linalg.eigh(K@K.T)
C=Uv.T@dK@Us
cg=dK@G;cp=dK@E
res={'dimensions':{'real_scalar':188,'vector':79,'Goldstone':rank,'physical':E.shape[1]},'norm2_all_SV':float(np.sum(dK**2)),'norm2_Goldstone_SV_omitted':float(np.sum(cg**2)),'norm2_physical_SV_retained':float(np.sum(cp**2)),'Ward_HK_max':float(np.max(abs(H@K.T))),'radial_eigenvector_residual':float(np.linalg.norm(H@h-4320*h)),'tree_hA_norm':float(np.linalg.norm(K@h)),'tree_hG_norm':float(np.linalg.norm(G.T@H@h)),'nearest_other_scalar_pole_gap':float(np.sort(abs(ms-4320))[1])}
assert rank==67 and E.shape[1]==121
assert res['Ward_HK_max']<1e-8
assert res['norm2_Goldstone_SV_omitted']>1e-4
assert abs(res['norm2_all_SV']-res['norm2_Goldstone_SV_omitted']-res['norm2_physical_SV_retained'])<1e-10
np.savez(P/'recovery-tensors.npz',x=x,B=B,c=c,R=R,H=H,h=h,ms=ms,Us=Us,mv=mv,Uv=Uv,G=G,E=E,C=C)
res['failed_assertion']={'assertion':'Physical quotient alone is complete for strict-Landau internal scalar-vector bubbles','passed':False,'reason':'Massless gauge-Goldstone scalars remain internal propagating fields in xi=0. Their nonzero squared derivative couplings are projected out by the interrupted code.'}
res['interrupted_code_other_errors']=['UV residue omitted A tadpole residues and B(X,0) residue; full BSV residue is 3s, not expression used there.','Unpivoted QR of dependent gauge tangent columns does not reliably identify all Goldstones.','setup called inside 79-entry comprehension, generating expensive tensors repeatedly; no checkpoint existed.','passed=True was hardcoded; zero-momentum/rotation diagnostics were not asserted.']
res['claim_boundary']='Verified failed completeness assertion in interrupted candidate; not a verified finite-momentum mixed correction and not a physical/gauge-independent pole.'
res['passed']=True
res['source_hashes']={str(q):hashlib.sha256(q.read_bytes()).hexdigest() for q in [P/'calculation.py',ROOT/'shifted-vacuum-gate/calculation.py',ROOT/'adjoint-radial-vector-bubble-gate/receipt.json',ROOT/'adjoint-radial-pole-gate/receipt.json']}
q=P/'recovery-audit.json'
if '--create' in sys.argv:
 with q.open('x') as f:json.dump(res,f,indent=2)
else: assert json.loads(q.read_text())==res
print(json.dumps(res,indent=2))
