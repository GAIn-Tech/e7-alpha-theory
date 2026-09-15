"""Local gate: Lean kernel plus deterministic exact certificate."""
from pathlib import Path
import subprocess,sys,os,re,json,hashlib
P=Path(__file__).resolve().parent
lean=P.parent/'lean-4.32.1-windows/bin/lean.exe'
env=dict(os.environ,LEAN_PATH=str(P))
def run(cmd):
 r=subprocess.run(list(map(str,cmd)),cwd=P,env=env,capture_output=True,text=True,encoding='utf-8',timeout=180)
 assert r.returncode==0,r.stdout+r.stderr
 return {'command':list(map(str,cmd)),'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
s=(P/'Formalization.lean').read_text(encoding='utf-8')
assert not re.search(r'\b(sorry|admit|axiom|unsafe)\b',s)
runs=[run([lean,'--version']),run([lean,'-o','Formalization.olean','Formalization.lean']),run([lean,'Challenge.lean']),run(['C:/Python313/python.exe','-B','exact_certificate.py','--verify'])]
names=re.findall(r"'([^']+)' does not depend on any axioms",runs[1]['stdout'])
assert names==re.findall(r'#print axioms ([\w.]+)',s) and len(names)==3
files=[f for f in P.iterdir() if f.suffix in {'.py','.lean','.md','.yaml'} or f.name=='certificate.json']
receipt={'passed':True,'claim_boundary':'Finite sourced catalog; exact arithmetic and axiom-free countermodel theorem. Not a universal physical no-go or selector.','axiom_free_declarations':names,'runs':runs,'sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(files)}}
out=P/'verification.json'; text=json.dumps(receipt,indent=2)+'\n'
if '--verify' in sys.argv:
 assert out.exists() and out.read_text(encoding='utf-8')==text,'missing/stale verification receipt'
 print('PASS saved receipt replay: 3 axiom-free declarations and exact finite catalog')
else:
 out.write_text(text,encoding='utf-8'); print('PASS verification receipt created')
