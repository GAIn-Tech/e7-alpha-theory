"""Verify existing receipt without regenerating it; compile Lean and record outputs."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import z3
ROOT=Path(__file__).resolve().parent
receipt=json.loads((ROOT/'smt-receipt.json').read_text())
assert receipt['script_sha256']==hashlib.sha256((ROOT/'check_gap.py').read_bytes()).hexdigest()
for name,digest in receipt['source_sha256'].items():
    assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==digest,name
replayed=[]
for case in receipt['checks']:
    s=z3.Solver(); s.set(timeout=15000); s.from_file(str(ROOT/(case['name']+'.smt2')))
    actual=str(s.check())
    assert actual==case['actual']==case['expected'],case['name']
    replayed.append({'name':case['name'],'result':actual})
source=(ROOT/'Gap.lean').read_text(encoding='utf-8')
assert 'sorry' not in source and '\naxiom ' not in source
lean=ROOT/'lean-4.32.1-windows/bin/lean.exe'
commands=[[str(lean),'--version'],[str(lean),'--root='+str(ROOT),'-o',str(ROOT/'Gap.olean'),str(ROOT/'Gap.lean')]]
logs=[]
for cmd in commands:
    p=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True,timeout=120)
    logs.append({'command':cmd,'cwd':str(ROOT),'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr})
    assert p.returncode==0,logs[-1]
assert logs[-1]['stdout'].count('does not depend on any axioms')==3
assert (ROOT/'Gap.olean').is_file()
result={'passed':True,'lean_commands':logs,'lean_source_sha256':hashlib.sha256((ROOT/'Gap.lean').read_bytes()).hexdigest(),'lean_olean_sha256':hashlib.sha256((ROOT/'Gap.olean').read_bytes()).hexdigest(),'smt_receipt_sha256':hashlib.sha256((ROOT/'smt-receipt.json').read_bytes()).hexdigest(),'smt_replayed':replayed,'scope':'Three polymorphic conditional bridge theorems kernel-checked without axioms. Real/E7 Cartan and affine algebra checked separately by Z3, not imported as Lean theorems. Full Theory2 Mathlib library NOT built.'}
(ROOT/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
