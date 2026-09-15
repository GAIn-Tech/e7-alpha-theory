"""Replay saved evidence; save real local execution, never regenerate the certificate."""
from pathlib import Path
import sys, subprocess, hashlib, json
p=Path(__file__).resolve().parent
commands=[[sys.executable,'-B',str(p/'test_embedding.py')],
 [str(p.parent/'lean-4.32.1-windows/bin/lean.exe'),str(p/'Chirality.lean')],
 [sys.executable,str(Path.home()/'AppData/Local/hermes/skills/research/grounded-citations/scripts/sources.py'),
  '--ledger',str(p/'sources/citation-ledger.json'),'verify',str(p/'REPORT.md'),'--evidence']]
results=[]
for command in commands:
    r=subprocess.run(command,cwd=p,capture_output=True,text=True)
    results.append(dict(command=command,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr))
files=['embedding_checks.py','embedding-receipt.json','test_embedding.py','Chirality.lean','REPORT.md','formalization.yaml','RELEASE_DISCLOSURE.md','run_checks.py']
record=dict(passed=all(r['exit_code']==0 for r in results),checks=results,
 hashes={n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in files})
(p/'verification.json').write_text(json.dumps(record,indent=2)+'\n')
for r in results:print(r['stdout']+r['stderr'])
assert record['passed']
