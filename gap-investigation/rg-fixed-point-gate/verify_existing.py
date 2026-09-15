"""Run saved-evidence verification and tests; never regenerate receipt."""
from pathlib import Path
import subprocess, json, hashlib, sys
P=Path(__file__).resolve().parent
python=P.parent/'.venv/Scripts/python.exe'
source=Path('C:/Users/mikeb/AppData/Local/hermes/skills/research/grounded-citations/scripts/sources.py')
commands=[[str(python),'-B',str(P/'check_rg.py')],[str(python),'-B',str(P/'check_rg.py'),'--test'],[sys.executable,str(source),'--ledger',str(P/'sources.json'),'verify',str(P/'REPORT.md'),'--evidence']]
runs=[]
for cmd in commands:
    r=subprocess.run(cmd,capture_output=True,text=True,timeout=180)
    runs.append({'args':cmd,'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
    print(r.stdout,r.stderr)
passed=all(r['returncode']==0 for r in runs)
files=sorted(p for p in P.iterdir() if p.is_file() and p.name!='verification.json')
data={'passed':passed,'runs':runs,'artifact_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'scope':'local exact arithmetic, saved SMT replay and citation evidence; no Lean/QFT proof or hosted CI'}
(P/'verification.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':passed,'verification':str(P/'verification.json')},indent=2))
raise SystemExit(0 if passed else 1)
