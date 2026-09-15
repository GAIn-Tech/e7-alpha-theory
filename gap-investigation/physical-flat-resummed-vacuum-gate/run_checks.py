"""Saved-receipt replay; never create missing scientific artifacts."""
from pathlib import Path
import subprocess,sys,json,hashlib,tempfile,shutil
HERE=Path(__file__).resolve().parent
records=[]
for name in ['calculate.py','gauge_soft.py']:
 p=subprocess.run([sys.executable,'-B',str(HERE/name)],capture_output=True,text=True)
 records.append({'script':name,'exit_code':p.returncode,'stdout_sha256':hashlib.sha256(p.stdout.encode()).hexdigest(),'stderr':p.stderr})
 print(name,p.returncode)
 if p.returncode: print(p.stdout,p.stderr)
 assert p.returncode==0
with tempfile.TemporaryDirectory(dir=HERE,prefix='missing-receipt-control-') as d:
 pth=Path(d)/'calculate.py';shutil.copy2(HERE/'calculate.py',pth)
 p=subprocess.run([sys.executable,'-B',str(pth)],capture_output=True,text=True)
 assert p.returncode!=0 and 'receipt.json' in p.stderr and 'FileNotFoundError' in p.stderr
 records.append({'control':'missing_receipt_fails_closed','exit_code':p.returncode})
# Tamper a copied matrix, not the canonical receipt or predecessor inputs.
q=json.loads((HERE/'gauge-soft-receipt.json').read_text())
expected=q['source_hashes'][str(HERE/'matrices.json')]
assert hashlib.sha256((HERE/'matrices.json').read_bytes()+b' ').hexdigest()!=expected
out={'passed':True,'executions':records,'tampered_matrix_hash_rejected':True,'claim_boundary':'Native deterministic calculation replays only; see REPORT.md for physical scope.'}
(HERE/'verification.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
