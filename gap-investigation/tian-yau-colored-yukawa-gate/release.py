"""Freeze the additive release and preserve a completed native replay log/status."""
from pathlib import Path
import json,sys,subprocess,hashlib
P=Path(__file__).resolve().parent
assert P==Path('C:/Users/mikeb/e7-alpha-theory/gap-investigation/tian-yau-colored-yukawa-gate')
excluded={'release-manifest.json','native-replay.log','native-replay-status.json'}
paths=[p for p in P.rglob('*') if p.is_file() and p.name not in excluded and '__pycache__' not in p.parts]
manifest={str(p.relative_to(P)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}
with (P/'release-manifest.json').open('x',newline='\n') as f:f.write(json.dumps(manifest,sort_keys=True,indent=2)+'\n')
cmd=[sys.executable,'-B',str(P/'verify.py')]
with (P/'native-replay.log').open('xb') as f:run=subprocess.run(cmd,cwd=P,stdout=f,stderr=subprocess.STDOUT)
status={'command':cmd,'cwd':str(P),'exit_code':run.returncode,'log_sha256':hashlib.sha256((P/'native-replay.log').read_bytes()).hexdigest(),'release_manifest_sha256':hashlib.sha256((P/'release-manifest.json').read_bytes()).hexdigest(),'certificate_sha256':hashlib.sha256((P/'certificate.json').read_bytes()).hexdigest(),'boundary':'Completed exact relative charged Yukawa replay; absolute adjunction normalization and conjugate slices remain open.'}
with (P/'native-replay-status.json').open('x',newline='\n') as f:f.write(json.dumps(status,indent=2)+'\n')
print(json.dumps(status,indent=2));sys.exit(run.returncode)
