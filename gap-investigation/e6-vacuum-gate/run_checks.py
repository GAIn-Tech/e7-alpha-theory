from pathlib import Path
import subprocess,sys,json,hashlib,platform
import numpy as np
D=Path(__file__).resolve().parent
runs=[]
for script in ['checks.py','test_vacuum.py']:
 r=subprocess.run([sys.executable,'-B',str(D/script)],cwd=D,capture_output=True,text=True,timeout=300)
 runs.append({'command':[sys.executable,'-B',str(D/script)],'exit':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
 print(script,'exit',r.returncode,flush=True)
files=['checks.py','receipt.json','test_vacuum.py','REPORT.md','sources/deppisch.pdf','sources/retrieval-receipt.json']
out={'passed':all(r['exit']==0 for r in runs),'numpy':np.__version__,'python':sys.version,'executable':sys.executable,'platform':platform.platform(),'runs':runs,'hashes':{n:hashlib.sha256((D/n).read_bytes()).hexdigest() for n in files}}
(D/'verification.json').write_text(json.dumps(out,indent=2));print('passed',out['passed'])
if not out['passed']:raise SystemExit(1)
