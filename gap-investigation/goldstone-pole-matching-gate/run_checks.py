"""Replay physical calculations without writing predecessor lanes."""
from pathlib import Path
import json,sys,subprocess,hashlib
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
# Read/hash saved inputs BEFORE replay; never regenerate to mask stale evidence.
old=json.loads((HERE/'receipt.json').read_text())
for p,h in old['source_hashes'].items():assert sha(Path(p))==h
originals=[ROOT/'shifted-vacuum-gate/receipt.json']+list((ROOT/'ir-resummed-vacuum-gate').glob('*receipt.json'))+[ROOT/'ir-resummed-vacuum-gate/projected-tensors.json']
before={str(p):sha(p) for p in originals}
results=[]
for rel in ['ir-resummed-vacuum-gate/resummation.py','ir-resummed-vacuum-gate/soft_tadpole.py','ir-resummed-vacuum-gate/calculation.py','goldstone-pole-matching-gate/calculation.py']:
 p=ROOT/rel
 r=subprocess.run([sys.executable,'-B',str(p)],cwd=str(HERE),text=True,capture_output=True,timeout=500)
 log=HERE/(rel.replace('/','_')+'.log');log.write_text(r.stdout+r.stderr)
 results.append({'calculation':rel,'exit_code':r.returncode,'log':str(log),'log_sha256':sha(log)})
 assert r.returncode==0,(rel,r.stderr)
assert before=={str(p):sha(p) for p in originals},'predecessor write detected'
artifacts=['receipt.json','tensors.json','transverse-trilinears.npy','calculation.py','REPORT.md','SOURCE_NOTES.md','primary-source-excerpts.txt','RELEASE_DISCLOSURE.md','run_checks.py']
out={'passed':True,'scope':'Read-only replay of predecessor IR matching/soft tadpole/Gaussian obstruction and new leading momentum matching. Numerical integrals and tensors are not Lean or interval proofs.','replays':results,'original_receipts_preserved':before,'artifact_sha256':{n:sha(HERE/n) for n in artifacts}}
(HERE/'verification.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
