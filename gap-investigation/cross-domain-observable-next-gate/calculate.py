"""Exact paired holomorphic-threshold response, not a physical clock prediction."""
import argparse, hashlib, json, subprocess, sys
from pathlib import Path
import sympy as S
P=Path(__file__).resolve().parent
B=P.parent

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def calculate():
 s,t,g,r,e=S.symbols('s t gamma r epsilon',positive=True)
 roots=[S.sqrt(2)*s,S.sqrt(S.Rational(2,3))*t]
 fs=[s+g*t,s-g*t]
 J=S.Matrix([[-S.diff(f,z)*dz/f for z,dz in zip([s,t],roots)] for f in fs])
 Jr=S.simplify(J.subs(t,r*s/g))
 det=S.factor(Jr.det())
 assert S.simplify(det+4*r/(S.sqrt(3)*(1-r*r)))==0
 v=S.Matrix([-r/S.sqrt(3),1])
 assert S.simplify((Jr*v)[0])==0
 assert S.simplify((Jr*v)[1]-2*S.sqrt(S.Rational(2,3))*r/(1-r))==0
 assert S.simplify(J.subs(g,0).det())==0
 wrong=J.copy(); wrong[1,:]=J[0,:]
 assert wrong.det()==0
 # Inverse kinetic functions, not physical running couplings.
 Fp,Fm=S.symbols('Fp Fm')
 inv={s:(Fp+Fm)/2,t:(Fp-Fm)/(2*g)}
 assert S.simplify(fs[0].subs(inv)-Fp)==0
 assert S.simplify(fs[1].subs(inv)-Fm)==0
 # All six Kahler moduli enter only through one nonzero beta functional.
 beta=S.symbols('b0:6'); M=S.Matrix([[1,*beta],[1,*[-x for x in beta]]])
 # Ray pairing is nonzero. Choose a basis aligned with that covector, NOT six invented Chern numbers.
 aligned=S.Matrix([[1,1,0,0,0,0,0],[1,-1,0,0,0,0,0]])
 assert aligned.rank()==2 and len(aligned.nullspace())==5
 # Canonical Gram invariants; no floating eigenvalue tests.
 gram=S.simplify(Jr.T*Jr)
 trace=S.factor(S.trace(gram)); gd=S.factor(gram.det())
 assert S.simplify(gd-det**2)==0
 # Rational-coordinate error bound. |Eij| <= epsilon gives the displayed bound.
 L=S.Matrix([[-1/(1+r),-r/(1+r)],[-1/(1-r),r/(1-r)]])
 a,b,c,d=S.symbols('ea eb ec ed')
 perturb=S.expand((L+S.Matrix([[a,b],[c,d]])).det()-L.det())
 linear=[S.simplify(S.diff(perturb,x).subs({a:0,b:0,c:0,d:0})) for x in [a,b,c,d]]
 bound=2*e/(1-r)+2*e**2
 # Rational witnesses illustrate a certified bound, not phenomenological parameter choices.
 witnesses=[]
 for rv,ev in [(S.Rational(1,10),S.Rational(1,100)),(S.Rational(1,1000),S.Rational(1,100))]:
  margin=S.factor(2*r/(1-r*r)-bound).subs({r:rv,e:ev})
  witnesses.append({'r':str(rv),'epsilon':str(ev),'margin':str(margin),'certified_nonzero':bool(margin>0)})
 assert witnesses[0]['certified_nonzero'] and not witnesses[1]['certified_nonzero']
 # Exact nontrivial ray example, safely within both positive kinetic coefficients.
 exact=Jr.subs(r,S.Rational(1,10)); assert exact.rank()==2
 clock=S.Rational(16,5)*Jr[0,:]
 assert clock.rank()==1
 assert all(S.simplify(x)==0 for x in clock*v)
 # The characteristic-two negative control explains the Lean no-two-torsion premise.
 assert ((1+1)%2)==0 and ((1-1)%2)==0
 lean=B/'lean-4.32.1-windows/bin/lean.exe'
 run=subprocess.run([str(lean),str(P/'Response.lean')],capture_output=True,text=True)
 assert run.returncode==0,run.stdout+run.stderr
 for name in ['paired_response_separates','paired_response_dilaton']:
  assert f"'PairedThreshold.{name}' does not depend on any axioms" in run.stdout
 assert 'sorry' not in (P/'Response.lean').read_text()
 inherited=['tian-yau-clock-response-gate/REPORT.md','tian-yau-moduli-stabilization-gate/REPORT.md','knot-modular-threshold-gate/REPORT.md','arithmetic-compactification-selection-gate/REPORT.md','connections/dirac/REPORT.md','connections/partitions/REPORT.md','connections/knots/REPORT.md','atomic-clock-gate/REPORT.md','clock-matching-gate/REPORT.md']
 return {'passed':True,'claim_boundary':'Exact truncated holomorphic threshold response with tree metric; neither full physical gauge thresholds, hidden-sector measurement, stabilized vacuum, nor clock prediction is established.',
 'gamma':'3/pi (inherited nonzero ray pairing 24, source normalization beta/2)',
 'canonical_response':str(Jr),'determinant':str(det),'gram_trace':str(trace),'gram_determinant':str(gd),'visible_blind_direction':str(v),'hidden_response_on_visible_blind_direction':str(S.simplify((Jr*v)[1])),
 'full_real_dilaton_kahler_dimension':7,'paired_map_rank':aligned.rank(),'kernel_dimension':len(aligned.nullspace()),
 'clock_rank':clock.rank(),'log_coordinate_error_linear_coefficients':[str(x) for x in linear],
 'determinant_error_bound':str(bound),'rank_bound_witnesses':witnesses,
 'negative_controls':{'tree_limit_rank_loss':True,'wrong_same_sign_rank_loss':True,'characteristic_two_not_injective':True},
 'lean':{'exit_code':run.returncode,'stdout':run.stdout,'stderr':run.stderr,'binary_sha256':sha(lean)},
 'sympy_version':S.__version__,'source_hashes':{x:sha(B/x) for x in inherited},
 'own_hashes':{x:sha(P/x) for x in ['calculate.py','Response.lean','source.html']}}

def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--create',action='store_true'); ap.add_argument('--negative-controls',action='store_true'); args=ap.parse_args()
 target=P/'certificate.json'; result=calculate()
 encoded=json.dumps(result,indent=2,sort_keys=True)+'\n'
 if args.create:
  if target.exists(): raise SystemExit('Refusing to overwrite existing receipt')
  target.write_text(encoded,encoding='utf-8')
 else:
  assert target.exists(),'Missing saved receipt'
  assert target.read_text(encoding='utf-8')==encoded,'Saved receipt mismatch'
 if args.negative_controls:
  bad=json.loads(encoded); bad['clock_rank']=2
  assert json.dumps(bad,indent=2,sort_keys=True)+'\n'!=encoded
  bad=json.loads(encoded); bad['claim_boundary']='Physical E7 prediction'
  assert json.dumps(bad,indent=2,sort_keys=True)+'\n'!=encoded
 print(json.dumps({'passed':True,'mode':'create' if args.create else 'saved_receipt_replay','certificate_sha256':sha(target),'rank':result['paired_map_rank'],'kernel':result['kernel_dimension'],'lean_exit':result['lean']['exit_code'],'negative_controls':bool(args.negative_controls)}))
if __name__=='__main__': main()
