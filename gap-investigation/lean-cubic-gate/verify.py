"""Local kernel build and predecessor receipt replay; no network/downloads."""
from pathlib import Path
import subprocess, hashlib, json, re, sys, tempfile
P=Path(__file__).resolve().parent
lean=P.parent/'lean-4.32.1-windows/bin/lean.exe'
source=(P/'Cubic.lean').read_text(encoding='utf-8')+(P/'Examples.lean.part').read_text(encoding='utf-8')
assert not re.search(r'\b(sorry|admit|axiom|unsafe)\b',source)
assert source==(P/'Checked.lean').read_text(encoding='utf-8'),'Combined proof stale'
commands=[[str(lean),'--version'],[str(lean),str(P/'Checked.lean')],[sys.executable,'-B',str(P.parent/'next-gate/representation_checks.py')]]
runs=[]
for cmd in commands:
 r=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',timeout=180)
 runs.append(dict(command=cmd,returncode=r.returncode,stdout=r.stdout,stderr=r.stderr))
 assert r.returncode==0,r.stdout+r.stderr
axioms=re.findall(r"'([^']+)' does not depend on any axioms",runs[1]['stdout'])
expected=re.findall(r'#print axioms ([\w.]+)',source)
assert axioms==expected and len(axioms)==18
assert 'depends on axioms:' not in runs[1]['stdout']
# Ensure the finite proof generator regenerates byte-identical proof terms.
with tempfile.TemporaryDirectory() as td:
 import shutil
 q=Path(td)/'generate_examples.py';shutil.copyfile(P/'generate_examples.py',q)
 subprocess.run([sys.executable,str(q)],check=True)
 assert (Path(td)/'Examples.lean.part').read_bytes()==(P/'Examples.lean.part').read_bytes()
receipt={'passed':True,'claim_boundary':'Kernel-only additive order-two cubic obstruction; E7 representation bridge remains external, not a physics solution.','axiom_free_declarations':axioms,'runs':runs,'sha256':{x.name:hashlib.sha256(x.read_bytes()).hexdigest() for x in P.iterdir() if x.is_file() and x.name not in ['verification.json']}}
(P/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'axiom_free_declarations':len(axioms),'predecessor_receipt_replayed':True,'finite_examples_regenerated_identically':True}))
