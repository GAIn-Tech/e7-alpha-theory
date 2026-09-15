"""Local release gate; --verify never regenerates missing receipts."""
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
runs=[run([lean,'--version']),run([lean,'-o','Formalization.olean','Formalization.lean']),run([lean,'Challenge.lean']),run([sys.executable,'-B','exact_certificate.py','--verify'])]
names=re.findall(r"'([^']+)' does not depend on any axioms",runs[1]['stdout'])
assert names==re.findall(r'#print axioms ([\w.]+)',s) and len(names)==4
assert 'depends on axioms:' not in runs[1]['stdout']
rows=json.loads((P/'source_evidence.json').read_text(encoding='utf-8'))
for row in rows:
 f=P/'sources'/row['file'];t=f.read_text(encoding='utf-8');i=row['offset']
 assert t[i:i+len(row['quote'])]==row['quote']
 assert hashlib.sha256(f.read_bytes()).hexdigest()==row['sha256']
 assert hashlib.sha256(f.with_suffix('.pdf').read_bytes()).hexdigest()==row['pdf_sha256']
files=[f for f in P.iterdir() if f.suffix in {'.py','.lean','.md','.yaml'} or f.name in {'certificate.json','source_evidence.json'}]+list((P/'sources').iterdir())
receipt={'passed':True,'claim_boundary':'Sourced CY3 standard embedding plus exact arithmetic and conditional Lean cover-index magnitude cancellation; not a stabilized Standard Model.','axiom_free_declarations':names,'source_excerpt_count':len(rows),'runs':runs,'sha256':{str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(files)}}
out=P/'verification.json'
if '--verify' in sys.argv:
 assert out.exists(),'Missing verification receipt'
 assert json.loads(out.read_text(encoding='utf-8'))==receipt,'Stale verification receipt'
 print('PASS saved receipt replay: four axiom-free Lean declarations, full exact certificate, six primary-source excerpts')
else:
 out.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print('PASS verification receipt created after native kernel and certificate checks')
