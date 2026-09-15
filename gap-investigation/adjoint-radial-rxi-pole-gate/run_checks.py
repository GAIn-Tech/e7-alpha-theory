import subprocess,json,hashlib,sys
from pathlib import Path
P=Path(__file__).resolve().parent
rows=[]
for exe,name in [('C:/Users/mikeb/AppData/Local/hermes/hermes-agent/venv/Scripts/python.exe','calculation.py'),('C:/Python313/python.exe','symbolic_checks.py')]:
 r=subprocess.run([exe,'-B',str(P/name)],capture_output=True,text=True)
 rows.append({'script':name,'exit':r.returncode,'stdout_sha256':hashlib.sha256(r.stdout.encode()).hexdigest()})
 assert r.returncode==0,r.stderr
out={'passed':True,'replays':rows,'boundary':'Replay and symbolic identities, not full pole or Lean proof.'}
print(json.dumps(out,indent=2))
