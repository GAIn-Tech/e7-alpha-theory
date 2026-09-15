import hashlib,json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
art=['calculation.py','receipt.json','REPORT.md']
before={n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in art}
p=subprocess.run([sys.executable,'-B',str(HERE/'calculation.py')],capture_output=True,text=True)
assert p.returncode==0,p.stderr
after={n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in art}
assert before==after
out={'passed':True,'calculation_exit_code':p.returncode,'artifacts_unchanged':before,'claim_boundary':'Replay of bounded zero-momentum gauge determinant gate; finite-p pole diagrams remain.'}
(HERE/'verification.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))

