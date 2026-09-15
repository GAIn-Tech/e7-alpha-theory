import sys, subprocess, hashlib, json
from pathlib import Path
H=Path(__file__).resolve().parent
commands=[[sys.executable,'-B',str(H/'quotient_check.py')],[sys.executable,'-B',str(H/'checks.py')],[sys.executable,'-B',str(H/'checks.py'),'--test'],[str(H.parent/'lean-4.32.1-windows/bin/lean.exe'),str(H/'Conditional.lean')]]
r=[]
for c in commands:
 p=subprocess.run(c,cwd=H,text=True,capture_output=True);r.append({'command':c,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
v={'passed':all(x['exit_code']==0 for x in r),'runs':r,'hashes':{str(p.relative_to(H)):hashlib.sha256(p.read_bytes()).hexdigest() for p in H.rglob('*') if p.is_file() and p.name!='verification.json'},'scope':'Exact Fraction arithmetic and minimal Lean conditional additive bridge. No Mathlib or hosted CI.'}
(H/'verification.json').write_text(json.dumps(v,indent=2));print(json.dumps(v,indent=2));sys.exit(not v['passed'])
