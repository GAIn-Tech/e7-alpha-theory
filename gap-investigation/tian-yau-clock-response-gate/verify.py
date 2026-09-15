"""Replay all retained certificates, sources, formal result and citation gate."""
from pathlib import Path
import subprocess,sys,json,hashlib
P=Path(__file__).resolve().parent
PY='C:/Python313/python.exe'
CITE='C:/Users/mikeb/AppData/Local/hermes/skills/research/grounded-citations/scripts/sources.py'
commands=[[PY,'-B',str(P/'calculate.py'),'--verify'],[PY,'-B',str(P/'calculate.py'),'--verify','--negative-controls'],[PY,CITE,'--ledger',str(P/'sources/ledger.json'),'verify',str(P/'REPORT.md'),'--evidence']]
results=[]
for c in commands:
 r=subprocess.run(c,cwd=P,capture_output=True,text=True,encoding='utf8');results.append(dict(command=c,exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr));assert r.returncode==0,results[-1]
files={str(x.relative_to(P)):hashlib.sha256(x.read_bytes()).hexdigest() for x in sorted(P.rglob('*')) if x.is_file() and x.name!='verification.json'}
actual={'passed':True,'commands':results,'artifact_hashes':files,'hosted_CI':'not run','scope':'Only this lane; no public publication or numerical alpha prediction.'}
f=P/'verification.json'
if '--create' in sys.argv:
 with f.open('x',encoding='utf8') as o:json.dump(actual,o,indent=2)
else: assert json.loads(f.read_text(encoding='utf8'))==actual,'verification artifact mismatch'
print(json.dumps({'passed':True,'commands':len(results),'artifacts':len(files),'verification_sha256':hashlib.sha256(f.read_bytes()).hexdigest()}))
