"""Build/replay the local gate. --verify never regenerates receipts."""
from pathlib import Path
import subprocess,sys,os,re,json,hashlib
P=Path(__file__).resolve().parent
lean=P.parent/'lean-4.32.1-windows/bin/lean.exe'
def run(cmd):
 r=subprocess.run(list(map(str,cmd)),cwd=P,capture_output=True,text=True,encoding='utf-8',env=dict(os.environ,LEAN_PATH=str(P)),timeout=180)
 assert r.returncode==0,r.stdout+r.stderr
 return {'command':list(map(str,cmd)),'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
source=(P/'Formalization.lean').read_text()
assert not re.search(r'\b(sorry|admit|axiom|unsafe)\b',source)
runs=[run([lean,'--version']),run([lean,'-o',P/'Formalization.olean',P/'Formalization.lean']),run([lean,P/'Challenge.lean']),run([sys.executable,'-B',P/'certificate.py','--verify'])]
names=re.findall(r"'([^']+)' does not depend on any axioms",runs[1]['stdout'])
assert names==re.findall(r'#print axioms ([\w.]+)',source) and len(names)==6
assert 'depends on axioms:' not in runs[1]['stdout']
# Grounded-citations structural check without rewriting the deliberately explanatory source block.
ledger=json.loads((P/'sources/ledger.json').read_text()); report=(P/'REPORT.md').read_text()
for n in range(1,7):assert f'[{n}]' in report
assert len(ledger['sources'])==6
files=[x for x in P.iterdir() if x.suffix in {'.py','.lean','.md','.json'} and x.name!='verification.json']+list((P/'sources').iterdir())
receipt={'passed':True,'claim_boundary':'Local exact/Lean bridge and sourced scoped physical counterexample; not a Tian-Yau threshold calculation.','axiom_free_declarations':names,'runs':runs,'sha256':{str(x.relative_to(P)):hashlib.sha256(x.read_bytes()).hexdigest() for x in sorted(files) if x.is_file()}}
t=P/'verification.json'
if '--verify' in sys.argv:
 assert t.exists(),'Missing verification receipt';assert json.loads(t.read_text())==receipt,'Stale verification receipt';print('PASS saved verification replay: six axiom-free Lean declarations, exact certificate, source ledger')
else:t.write_text(json.dumps(receipt,indent=2)+'\n');print('PASS verification receipt created')
