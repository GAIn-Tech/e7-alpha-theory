"""Kernel checks and saved certificate replay. --verify never creates receipts."""
from pathlib import Path
import subprocess,sys,os,json,hashlib,re
P=Path(__file__).resolve().parent
lean=P.parent/'lean-4.32.1-windows/bin/lean.exe'
env=dict(os.environ,LEAN_PATH=str(P))
def run(cmd):
 r=subprocess.run(list(map(str,cmd)),capture_output=True,text=True,encoding='utf-8',env=env,timeout=180,cwd=P)
 assert r.returncode==0,r.stdout+r.stderr
 return {'command':list(map(str,cmd)),'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
source=(P/'Formalization.lean').read_text(encoding='utf-8')
assert not re.search(r'\b(sorry|admit|axiom|unsafe)\b',source)
runs=[run([lean,'--version']),run([lean,'-o',P/'Formalization.olean',P/'Formalization.lean']),run([lean,P/'Challenge.lean']),run([sys.executable,'-B',P/'exact_certificate.py','--verify'])]
names=re.findall(r"'([^']+)' does not depend on any axioms",runs[1]['stdout'])
assert names==re.findall(r'#print axioms ([\w.]+)',source) and len(names)==5
assert 'depends on axioms:' not in runs[1]['stdout']
for row in json.loads((P/'source_evidence.json').read_text(encoding='utf-8')):
 f=P/'sources'/row['file']
 assert row['quote'] in f.read_text(encoding='utf-8')
 assert row['sha256']==hashlib.sha256(f.read_bytes()).hexdigest()
files=[x for x in P.iterdir() if x.suffix in {'.py','.lean','.md','.yaml'} or x.name in {'certificate.json','source_evidence.json'}]+list((P/'sources').glob('*'))
receipt={'passed':True,'claim_boundary':'Local exact modular building block and finite Lean discriminant algebra only; not a string vacuum.','axiom_free_declarations':names,'runs':runs,'sha256':{str(x.relative_to(P)):hashlib.sha256(x.read_bytes()).hexdigest() for x in sorted(files)}}
target=P/'verification.json'
if '--verify' in sys.argv:
 assert target.exists(),'Missing verification receipt'
 assert json.loads(target.read_text())==receipt,'Stale verification receipt'
 print('PASS: saved verification receipt replay; five axiom-free Lean declarations; exact S/T and lattice certificate; primary-source excerpts')
else:
 target.write_text(json.dumps(receipt,indent=2)+'\n');print('PASS: verification receipt created after kernel and exact certificate checks')
