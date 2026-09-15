"""Fail closed on absent/stale release files, then replay without regeneration."""
import hashlib,json,subprocess,sys
from pathlib import Path
P=Path(__file__).resolve().parent
m=json.loads((P/'manifest.json').read_text())
for rel,h in m['sha256'].items():
 assert hashlib.sha256((P/rel).read_bytes()).hexdigest()==h,rel
r=json.loads((P/'receipt.json').read_text())
for name,h in r['source_hashes'].items():
 assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==h,name
subprocess.run([sys.executable,'-B',str(P/'verify.py')],check=True)
print(json.dumps({'passed':True,'manifest_files':len(m['sha256']),'receipt_sha256':hashlib.sha256((P/'receipt.json').read_bytes()).hexdigest(),'claim_boundary':'Convergence and compatible sector bookkeeping only, not a full pole.'},indent=2))

