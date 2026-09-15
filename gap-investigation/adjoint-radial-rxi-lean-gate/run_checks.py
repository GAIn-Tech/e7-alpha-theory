"""Canonical native verification; validates immutable predecessor first."""
from pathlib import Path
import subprocess,json,hashlib,sys,os
P=Path(__file__).resolve().parent; PRE=P.parent/'adjoint-radial-rxi-identity-gate'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(cmd,cwd=P,env=None):
 r=subprocess.run(cmd,cwd=cwd,env=env,text=True,capture_output=True)
 if r.returncode:print(r.stdout,r.stderr);raise SystemExit(r.returncode)
 return {'command':cmd,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
# Never regenerate predecessor evidence.
saved=json.loads((PRE/'symbolic_receipt.json').read_text())
assert sha(PRE/'symbolic_certificate.py')==saved['source_sha256']
upstream=run([sys.executable,'-B',str(PRE/'symbolic_certificate.py')])
run([sys.executable,str(P/'generate_formalization.py')])
assert not any(x in (P/'Formalization.lean').read_text() for x in ['sorry','admit','axiom '])
lean=P/'toolchain/bin/lean.exe'; mathlib=P/'mathlib-src'
assert lean.exists() and (P/'toolchain/lib/lean/Init.olean').exists()
env=os.environ.copy();env['LEAN_PATH']=';'.join([str(P),str(mathlib/'.lake/build/lib/lean'),str(mathlib/'.lake/packages/batteries/.lake/build/lib/lean'),str(mathlib/'.lake/packages/Qq/.lake/build/lib/lean'),str(mathlib/'.lake/packages/aesop/.lake/build/lib/lean'),str(mathlib/'.lake/packages/proofwidgets/.lake/build/lib/lean'),str(mathlib/'.lake/packages/plausible/.lake/build/lib/lean'),str(mathlib/'.lake/packages/Cli/.lake/build/lib/lean')])
version=run([str(lean),'--version'],env=env);formal=run([str(lean),str(P/'Formalization.lean')],env=env);challenge=run([str(lean),str(P/'Challenge.lean')],env=env)
for name in json.loads((P/'coefficient_translation.json').read_text())['declarations']:
 assert f"'Rxi.{name}' depends on axioms: []" in formal['stdout'],name
sources=['Formalization.lean','Challenge.lean','generate_formalization.py','RELEASE_DISCLOSURE.md','coefficient_translation.json']
receipt={'passed':True,'claim_boundary':'Lean-kernel exact free-master coefficient algebra over arbitrary characteristic-zero fields; physical Ward/action inputs remain external numerical evidence.','upstream_saved_receipt_sha256':sha(PRE/'symbolic_receipt.json'),'upstream_source_sha256':sha(PRE/'symbolic_certificate.py'),'upstream_replay_exit_code':0,'lean_version':version['stdout'].strip(),'formal_exit_code':0,'challenge_exit_code':0,'axiom_report':formal['stdout'],'no_sorry':True,'source_sha256':{x:sha(P/x) for x in sources}}
(P/'verification_receipt.json').write_text(json.dumps(receipt,indent=2))
print(json.dumps(receipt,indent=2))
