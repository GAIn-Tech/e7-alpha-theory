"""Canonical next-gate local suite; replay existing evidence before logging results."""
from pathlib import Path
import hashlib,json,subprocess,sys
P=Path(__file__).resolve().parent
runs=[]
for name in ['representation_checks.py','vacuum_audit.py','candidate_checks.py']:
    command=[sys.executable,'-B',str(P/name)]
    r=subprocess.run(command,capture_output=True,text=True,timeout=600)
    runs.append({'command':command,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
    print(name,'exit',r.returncode)
files=['representation_checks.py','representation-receipt.json','candidate_checks.py','vacuum_audit.py','vacuum-receipt.json','vacuum-report.md','REPORT.md','run_checks.py']
result={'passed':all(r['exit_code']==0 for r in runs),'runs':runs,
        'artifact_sha256':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in files},
        'claim_boundary':'Local Python exact checks only; no hosted CI, full vacuum classification or alpha prediction.'}
(P/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
assert result['passed'],'At least one next-gate check failed'
print('NEXT-GATE SUITE PASSED')
