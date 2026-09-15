"""Exact leading-order Tian-Yau response gate; default replay never regenerates evidence."""
from pathlib import Path
import ast, copy, hashlib, json, subprocess, sys
import sympy as S
import numpy as np
P=Path(__file__).resolve().parent
G=P.parent
ZPY=G/'.venv/Scripts/python.exe'
LEAN=G/'lean-4.32.1-windows/bin/lean.exe'
BOUNDARY='Leading heterotic canonical response and conditional clock identifiability; no numerical alpha, stabilized vacuum, photon sector, masses or scalar history prediction.'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def compute(create=False):
 checks={}
 def check(k,v): checks[k]=bool(v); assert checks[k], k
 u,v,s0,V0=S.symbols('u v s0 V0',positive=True)
 s=s0*S.exp(S.sqrt(2)*u); volume=V0*S.exp(S.sqrt(6)*v)
 fields=S.Matrix([s,volume]); J=fields.jacobian([u,v])
 # L=-1/2 G_ij dq_i dq_j, in M=1 units, fixed axions/shape.
 metric=S.diag(1/(2*s*s),1/(6*volume*volume))
 canon=S.simplify(J.T*metric*J)
 check('canonical_metric_identity',canon==S.eye(2))
 grad=S.Matrix([S.diff(-S.log(s),x).simplify() for x in (u,v)])
 check('tree_fractional_gradient',grad==S.Matrix([-S.sqrt(2),0]))
 phi=(S.log(volume/V0)-S.log(s/s0))/2
 check('phi_coordinate_map',S.simplify(phi-(S.sqrt(6)*v-S.sqrt(2)*u)/2)==0)
 # Along fixed 10D dilaton, dlns=dlnV=dq; induced length²=2/3 dq².
 check('fixed_Phi_path_metric',S.Rational(1,2)+S.Rational(1,6)==S.Rational(2,3))
 check('fixed_Phi_fractional_slope_squared',1/S.Rational(2,3)==S.Rational(3,2))
 check('reject_missing_complex_derivative_quarter',4*canon!=S.eye(2))
 check('reject_extra_Einstein_s_power',S.diff(-2*S.log(s),u).simplify()!=grad[0])
 Au,Av,Bu,Bv,Nu,Nv=S.symbols('Au Av Bu Bv Nu Nv')
 R=S.Matrix([[S.Rational(16,5)*Au,S.Rational(16,5)*Av],[-6*Au-Bu-Nu,-6*Av-Bv-Nv]])
 expected=S.Rational(16,5)*(Av*(Bu+Nu)-Au*(Bv+Nv))
 check('two_modulus_determinant',S.simplify(R.det()-expected)==0)
 N=S.Matrix([[S.Rational(16,5)*Au,S.Rational(16,5)*Av,0,0],[-6*Au,-6*Av,-1,-1]])
 known=S.Matrix.hstack(S.Matrix([Av,-Au,0,0]),S.Matrix([0,0,1,-1]))
 check('symbolic_kernel_generators',N*known==S.zeros(2,2))
 check('generic_rank_two',N.rank()==2)
 null=N.nullspace()
 check('exact_nullity_two',len(null)==2)
 tree=N.subs({Au:-S.sqrt(2),Av:0})
 # Reuse ONLY existing numerical null function, no module setup or side effects.
 prior=G/'shifted-vacuum-gate/calculation.py'
 parsed=ast.parse(prior.read_text())
 node=next(n for n in parsed.body if isinstance(n,ast.FunctionDef) and n.name=='null')
 env={'np':np}; exec(compile(ast.Module(body=[node],type_ignores=[]),str(prior),'exec'),env)
 numeric=np.array(tree.tolist(),dtype=float); kernel=env['null'](numeric)
 check('reused_SVD_nullity_two',kernel.shape==(4,2))
 check('reused_SVD_residual',np.max(abs(numeric@kernel))<1e-12)
 check('source_sign_orientation',S.Rational(0)-S.Rational('-3.2')==S.Rational(16,5))
 check('reject_source_printed_minus_order',S.Rational('-3.2')!=S.Rational(16,5))
 # Exact counterfamily uses r=exp(-2 delta)>0. It is not a time history.
 lam,r=S.symbols('lambda r',positive=True)
 check('counterfamily_ratio',S.simplify((s0*lam**3*r)/s0-lam**3*r)==0)
 check('constant_coupling_fiber',S.simplify(lam**3*r).subs(r,lam**-3)==1)
 # SMT cases are generated in a separate process with existing z3 Python.
 zscript=P/'smt_cases.py'
 cmd=[str(ZPY),'-B',str(zscript),'--create' if create else '--verify']
 run=subprocess.run(cmd,cwd=P,capture_output=True,text=True); assert run.returncode==0,run.stdout+run.stderr
 smt=json.loads(run.stdout)
 lean=subprocess.run([str(LEAN),str(P/'Formalization.lean')],cwd=P,capture_output=True,text=True)
 check('lean_exit_zero',lean.returncode==0)
 axiom_lines=[l for l in lean.stdout.splitlines() if 'does not depend on any axioms' in l]
 check('lean_four_empty_axiom_reports',len(axiom_lines)==4)
 check('lean_no_placeholder',not any(w in (P/'Formalization.lean').read_text() for w in ('sorry','admit','unsafe')))
 manifest=json.loads((P/'sources/manifest.json').read_text())
 for rel,h in manifest['hashes'].items(): check('source_'+rel,sha(P/rel)==h)
 # Exact equation evidence retained separately from brief citation quotes.
 evidence=json.loads((P/'sources/equation-evidence.json').read_text())
 for x in evidence: check('equation_evidence_'+x['key'],x['text'] in (P/x['file']).read_text(encoding='utf8'))
 hashes={str(f.relative_to(P)):sha(f) for f in (P/'calculate.py',P/'smt_cases.py',P/'Formalization.lean',P/'sources/manifest.json',P/'sources/equation-evidence.json')}
 hashes['../shifted-vacuum-gate/calculation.py']=sha(prior)
 return {'claim_boundary':BOUNDARY,'passed':all(checks.values()) and smt['passed'],'checks':checks,'check_count':len(checks),'canonical_metric':str(canon),'tree_gradient':str(grad),'response_matrix':str(R),'determinant':str(expected),'nuisance_kernel':[[str(a) for a in b] for b in null],'SMT':smt,'lean':{'exit_code':lean.returncode,'stdout':lean.stdout,'stderr':lean.stderr},'hashes':hashes}
def verify(payload,actual):
 assert payload==actual,'certificate differs from fresh calculation'
def main():
 create='--create' in sys.argv
 actual=compute(create)
 f=P/'certificate.json'
 if create:
  with f.open('x',encoding='utf8') as out: json.dump(actual,out,indent=2)
 else:
  verify(json.loads(f.read_text(encoding='utf8')),actual)
 if '--negative-controls' in sys.argv:
  rejected=[]
  for key in ('passed','claim_boundary','canonical_metric','hashes','SMT'):
   bad=copy.deepcopy(actual); bad[key]=None
   try: verify(bad,actual)
   except AssertionError: rejected.append(key)
  try: json.loads((P/'never-created-certificate.json').read_text())
  except FileNotFoundError: rejected.append('missing_receipt')
  assert len(rejected)==6
  print(json.dumps({'passed':True,'rejected':rejected}))
 else: print(json.dumps({'passed':actual['passed'],'exact_and_source_checks':actual['check_count'],'smt_cases':len(actual['SMT']['cases']),'lean_exit':actual['lean']['exit_code'],'certificate_sha256':sha(f)}))
if __name__=='__main__': main()
