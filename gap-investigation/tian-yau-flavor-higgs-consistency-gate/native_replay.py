from pathlib import Path
import json,hashlib,subprocess,datetime
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=sha(P/'release-manifest.json')
cmd=['C:/Python313/python.exe','-B',str(P/'verify.py')]
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (P/'native-replay.log').open('xb') as log:
 result=subprocess.run(cmd,stdout=log,stderr=subprocess.STDOUT,cwd=P)
status={'command':cmd,'started_utc':start,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':result.returncode,'log_sha256':sha(P/'native-replay.log'),'release_manifest_sha256':manifest,'manifest_unchanged':manifest==sha(P/'release-manifest.json')}
with (P/'native-replay-status.json').open('x') as f:f.write(json.dumps(status,sort_keys=True,indent=2)+'\n')
print(json.dumps(status,indent=2))
raise SystemExit(result.returncode)
