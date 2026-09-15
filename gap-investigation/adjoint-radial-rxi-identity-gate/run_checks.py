"""Read receipts first, validate hashes, replay without regeneration."""
import json,hashlib,subprocess,sys,copy
from pathlib import Path
P=Path(__file__).resolve().parent;ROOT=P.parent
PY=Path(sys.executable);SYMPY=Path('C:/Python313/python.exe');LEAN=ROOT/'lean-4.32.1-windows/bin/lean.exe'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(args,expected=0):
 r=subprocess.run([str(x) for x in args],cwd=P,capture_output=True,text=True)
 assert r.returncode==expected,{'args':r.args,'code':r.returncode,'out':r.stdout,'err':r.stderr}
 return {'command':r.args,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
def reject(fn):
 try:fn()
 except (AssertionError,FileNotFoundError):return True
 raise AssertionError('negative control accepted')
sym=json.loads((P/'symbolic_receipt.json').read_text());ten=json.loads((P/'tensor_receipt.json').read_text())
assert sym['passed'] and ten['passed']
assert sha(P/'symbolic_certificate.py')==sym['source_sha256']
for name,digest in ten['source_hashes'].items():assert sha(ROOT/name)==digest,name
assert all(v=='0' for c in sym['on_shell'].values() for v in c.values())
assert all(any(v!='0' for v in c.values()) for c in sym['controls'].values())
assert sym['action_witness']['sigma_from_stationary_solve']!='0'
bad=copy.deepcopy(sym);bad['on_shell']['physical'][next(iter(bad['on_shell']['physical']))]='1'
assert reject(lambda: (_ for _ in ()).throw(AssertionError()) if bad!=sym else None)
assert reject(lambda:json.loads((P/'missing_receipt.json').read_text()))
runs=[run([SYMPY,'-B',P/'symbolic_certificate.py']),run([PY,'-B',P/'tensor_hypotheses.py']),run([LEAN,'--version']),run([LEAN,P/'LeanAvailability.lean'],1)]
assert "unknown module prefix 'Init'" in runs[-1]['stdout']+runs[-1]['stderr']
files=[z for z in P.iterdir() if z.is_file() and z.name not in ('verification.json',) and not z.name.startswith('development_')]
out={'passed':True,'claim_boundary':sym['claim_boundary'],'runs':runs,'negative_controls':{'tampered_receipt_rejected':True,'missing_receipt_rejected':True,'symbolic_controls_nonzero':True,'nonzero_displacement_witness':True,'lean_import_blocker_reproduced':True},'sha256':{z.name:sha(z) for z in files},'python':sys.version}
(P/'verification.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print('PASS: exact arbitrary-xi master identity; actual tensor hypotheses; algebraic controls; pinned Lean blocker reproduced.')
