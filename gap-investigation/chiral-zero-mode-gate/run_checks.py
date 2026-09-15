"""Run saved-certificate replay and tests; retain real command outputs."""
import sys,subprocess,json,hashlib
from pathlib import Path
HERE=Path(__file__).resolve().parent
commands=[[sys.executable,'-B',str(HERE/'orbifold_checks.py')],[sys.executable,'-B',str(HERE/'test_orbifold.py')]]
r=[]
for c in commands:
 p=subprocess.run(c,cwd=HERE,text=True,capture_output=True)
 r.append({'command':c,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
files=[p for p in HERE.iterdir() if p.suffix in ('.py','.smt2','.md')]+[HERE/'orbifold-receipt.json']
v={'passed':all(z['exit_code']==0 for z in r),'runs':r,'hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'scope':'Local exact Python and Z3; no Lean or hosted CI claimed.'}
(HERE/'verification.json').write_text(json.dumps(v,indent=2))
print(json.dumps(v,indent=2));sys.exit(0 if v['passed'] else 1)
