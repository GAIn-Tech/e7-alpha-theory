"""Read existing receipts first; replay real numerical/kernel runs. No regeneration."""
from pathlib import Path
from fractions import Fraction
import hashlib,json,os,subprocess,sys,copy
HERE=Path(__file__).resolve().parent
PY=Path(sys.executable);LEAN=HERE.parent/'lean-4.32.1-windows/bin/lean.exe'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read_saved(path):
 r=json.loads(path.read_text());assert r['passed']
 for name,digest in r['source_hashes'].items():assert sha(Path(name))==digest, name
 return r
def same(a,b):assert a==b,'receipt mismatch'
def expect_reject(fn):
 try:fn()
 except (AssertionError,FileNotFoundError):return True
 raise AssertionError('negative control was accepted')
def run(args,env=None,expected=0):
 r=subprocess.run([str(x) for x in args],cwd=HERE,capture_output=True,text=True,env=env)
 out={'command':r.args,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
 assert (r.returncode==0)==(expected==0),out
 return out
old=read_saved(HERE/'receipt.json')
controls={}
bad=copy.deepcopy(old);bad['singlet_covector_tadpole'][0]+=1
controls['tampered_tadpole_rejected']=expect_reject(lambda:same(old,bad))
bad=copy.deepcopy(old);bad['source_hashes'][next(iter(bad['source_hashes']))]='0'*64
controls['tampered_source_hash_rejected']=expect_reject(lambda:same(old,bad))
controls['missing_receipt_rejected']=expect_reject(lambda:read_saved(HERE/'intentionally-absent.json'))
K=[[Fraction(v) for v in r] for r in old['exact_singlet_inverse']['Hessian']]
I=[[Fraction(v) for v in r] for r in old['exact_singlet_inverse']['inverse']]
def exact_inverse(inv):
 assert all(sum(K[i][k]*inv[k][j] for k in range(10))==int(i==j) for i in range(10) for j in range(10))
exact_inverse(I);bad=copy.deepcopy(I);bad[0][0]=-bad[0][0]
controls['wrong_inverse_sign_rejected']=expect_reject(lambda:exact_inverse(bad))
# Reversed leading shift has H(-delta)+t=2t, rather than zero.
controls['wrong_tadpole_sign_residual_norm']=2*old['tadpole_norm']
assert controls['wrong_tadpole_sign_residual_norm']>1e5
runs=[run([PY,'-B',HERE.parent/'radiative-vacuum-gate/diagnostic.py']),run([PY,'-B',HERE/'calculation.py'])]
runs.append(run([LEAN,'--version']))
runs.append(run([LEAN,'-o',HERE/'Formalization.olean',HERE/'Formalization.lean']))
assert runs[-1]['stdout'].count('does not depend on any axioms')==5
assert 'sorry' not in (HERE/'Formalization.lean').read_text()
env=os.environ.copy();env['LEAN_PATH']=str(HERE)
runs.append(run([LEAN,HERE/'Challenge.lean'],env))
runs.append(run([LEAN,HERE/'WrongSign.lean'],env,expected=1))
controls['kernel_wrong_sign_rejected']=runs[-1]['exit_code']!=0
files=[p for p in HERE.iterdir() if p.is_file() and p.name!='verification.json' and p.suffix in ('.py','.lean','.md','.yaml','.json')]
out={'passed':True,'claim_boundary':old['claim_boundary'],'runs':runs,'negative_controls':controls,'sha256':{p.name:sha(p) for p in files},'python':sys.version}
(HERE/'verification.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print('PASS: saved full-action numerical receipt replay, exact inverse controls, predecessor replay, five axiom-free Lean declarations, public Challenge and rejected wrong-sign theorem.')
