"""Read existing evidence first; replay locally without predecessor regeneration."""
import os,sys,json,hashlib,subprocess,copy
from pathlib import Path
P=Path(__file__).resolve().parent
FILES=['calculate.py','gauge_cutoff_checks.py','receipt.json','gauge-cutoff-receipt.json','REPORT.md','RELEASE_DISCLOSURE.md','formalization.yaml','run_checks.py']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def validate(m):
 for name,h in m['sha256'].items():
  q=P/name
  if not q.is_file():raise FileNotFoundError(q)
  if sha(q)!=h:raise ValueError('hash mismatch: '+name)
if '--create-manifest' in sys.argv:
 manifest={'sha256':{name:sha(P/name) for name in FILES}}
 with (P/'manifest.json').open('x') as f:json.dump(manifest,f,indent=2)
manifest=json.loads((P/'manifest.json').read_text());validate(manifest)
base=json.loads((P/'receipt.json').read_text());extra=json.loads((P/'gauge-cutoff-receipt.json').read_text())
assert base['passed'] and extra['passed']
assert extra['base_receipt_sha256']==sha(P/'receipt.json')
for q,h in base['source_hashes'].items():assert sha(Path(q))==h,q
negative={}
for kind in ('missing','tampered'):
 bad=copy.deepcopy(manifest)
 if kind=='missing':bad['sha256']['does-not-exist.receipt.json']='0'*64
 else:bad['sha256']['receipt.json']='0'*64
 try:validate(bad)
 except (FileNotFoundError,ValueError):negative[kind+'_rejected']=True
 else:raise AssertionError('integrity negative control accepted')
env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
commands=[
 [sys.executable,'-B',str(P/'calculate.py')],
 [sys.executable,'-B',str(P/'gauge_cutoff_checks.py')],
 [sys.executable,'-B',str(P.parent/'adjoint-radial-pole-convergence-gate/run_checks.py')],
 ['C:/Python313/python.exe','-B',str(P.parent/'adjoint-radial-rxi-identity-gate/symbolic_certificate.py')]
]
results=[]
for i,cmd in enumerate(commands):
 result=subprocess.run(cmd,cwd=P,env=env,capture_output=True,text=True)
 log=P/('replay-'+str(i)+'.txt');log.write_text(result.stdout+'\nSTDERR\n'+result.stderr)
 results.append({'command':cmd,'exit_code':result.returncode,'stdout_sha256':hashlib.sha256(result.stdout.encode()).hexdigest(),'log':str(log)})
 if result.returncode:
  print(result.stderr);raise AssertionError(cmd)
validate(manifest)
for q,h in base['source_hashes'].items():assert sha(Path(q))==h,'predecessor changed: '+q
out={'passed':True,'claim_boundary':base['claim_boundary'],'manifest_sha256':sha(P/'manifest.json'),'saved_receipts_compared_without_regeneration':True,'predecessors_unchanged':True,'negative_controls':negative,'replays':results,'hosted_CI':'not run','Lean':'no new proof claimed'}
(P/'verification.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
