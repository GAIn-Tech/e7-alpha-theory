import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import json, hashlib, importlib.util, subprocess, sys
from pathlib import Path
import numpy as np
P=Path(__file__).resolve().parent
r=json.loads((P/'finite-momentum-receipt.json').read_text())
for q,h in r['source_hashes'].items():assert hashlib.sha256(Path(q).read_bytes()).hexdigest()==h,q
ck=np.load(P/'recovery-tensors.npz')
s=importlib.util.spec_from_file_location('shift_verify',P.parent/'shifted-vacuum-gate/calculation.py');M=importlib.util.module_from_spec(s);s.loader.exec_module(M)
x,B,c,R,T,si,aa=M.setup();_,_,H,_,_=M.tree(x,B,c)
for k,v in [('x',x),('B',B),('c',c),('R',R),('H',H)]:assert np.array_equal(v,ck[k]),k
assert np.max(abs(ck['Us']@np.diag(ck['ms'])@ck['Us'].T-H))<1e-8
assert np.max(abs(ck['Uv']@np.diag(ck['mv'])@ck['Uv'].T-(R@x)@(R@x).T))<1e-8
assert np.max(abs(ck['C']-ck['Uv'].T@(R@ck['h'])@ck['Us']))<1e-10
assert np.max(abs(ck['G']@ck['G'].T+ck['E']@ck['E'].T-np.eye(188)))<1e-10
subprocess.run([sys.executable,str(P/'finite_momentum.py')],check=True)
out={'passed':True,'checkpoint_fresh_native_tensor_comparison':True,'saved_receipt_replay_without_regeneration':True,'checkpoint_sha256':hashlib.sha256((P/'recovery-tensors.npz').read_bytes()).hexdigest(),'claim_boundary':'Strict Landau SV subset; not a gauge-independent/full pole','release_hashes':{q.name:hashlib.sha256(q.read_bytes()).hexdigest() for q in [P/'finite_momentum.py',P/'finite-momentum-receipt.json',P/'REPORT.md',P/'RELEASE_DISCLOSURE.md',Path(__file__)]}}
q=P/'verification.json'
if q.exists():assert json.loads(q.read_text())==out
else:
 with q.open('x') as f:json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
