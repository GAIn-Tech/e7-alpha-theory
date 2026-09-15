"""Immutable replay and nonvacuous rejection tests. All mutations stay in owned temporary copies."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,tempfile
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((P/'release-manifest.json').read_text())
for name,digest in m.items():assert sha(P/name)==digest,name
before={n:sha(P/n) for n in m}
def call(p):return subprocess.run([sys.executable,'-B',str(p/'calculate.py')],capture_output=True,text=True)
p=call(P);assert p.returncode==0,(p.stdout,p.stderr)
controls={}
with tempfile.TemporaryDirectory(dir=P) as td:
 T=Path(td)
 for name in ['calculate.py','certificate.json','input-manifest.json']:
  shutil.copyfile(P/name,T/name)
 shutil.copytree(P/'frozen',T/'frozen');shutil.copytree(P/'sources',T/'sources')
 cert=T/'certificate.json';original=cert.read_bytes();cert.unlink()
 p=call(T);assert p.returncode!=0;controls['missing_certificate_rejected']=True
 cert.write_bytes(original);d=json.loads(original);d['restricted_cocycles']['beta1']='1/z';cert.write_text(json.dumps(d))
 p=call(T);assert p.returncode!=0;controls['tampered_restriction_receipt_rejected']=True
 cert.write_bytes(original)
 target=T/'frozen/tian-yau-actual-survivor-coupling-gate/module-action.json';target.write_bytes(target.read_bytes()+b' ')
 p=call(T);assert p.returncode!=0;controls['mutated_frozen_cocycle_rejected']=True
assert before=={n:sha(P/n) for n in m}
print(json.dumps({'passed':True,'immutable_files':len(m),'controls':controls,'certificate_sha256':sha(P/'certificate.json')},sort_keys=True,indent=2))
