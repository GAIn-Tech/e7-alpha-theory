"""Read-only full replay with receipt integrity negative controls."""
from pathlib import Path
import subprocess,sys,json,hashlib,re,os
P=Path(__file__).resolve().parent
LEAN=P.parent/'lean-4.32.1-windows/bin/lean.exe'
def run(a,cwd=P,env=None):
 r=subprocess.run([str(x) for x in a],cwd=cwd,capture_output=True,text=True,env=env);return r.returncode,r.stdout+r.stderr
def calculate():
 for n in ['Formalization.lean','Challenge.lean']:
  t=(P/n).read_text();assert not re.search(r'\b(sorry|admit|unsafe|axiom)\b',t)
 code,out=run([LEAN,'-o','Formalization.olean','Formalization.lean']);assert code==0,out
 axioms=[q for q in out.splitlines() if 'does not depend on any axioms' in q or 'depends on axioms' in q]
 assert axioms==["'BundleCup.terminal_zero_cup' does not depend on any axioms","'BundleCup.boundary_is_closed' does not depend on any axioms"],axioms
 env=dict(os.environ);env['LEAN_PATH']=str(P)
 cc,co=run([LEAN,'Challenge.lean'],env=env);assert cc==0,co
 for lane in ['heterotic-e6-three-family-gate','tian-yau-wilson-line-gate']:
  q=P.parent/lane;c,o=run([sys.executable,'-B',q/'verify.py','--verify'],cwd=q);assert c==0,o
 c,o=run([sys.executable,'-B','exact_certificate.py']);assert c==0,o
 target=P/'certificate.json';saved=target.read_bytes()
 try:
  target.unlink();m,mo=run([sys.executable,'-B','exact_certificate.py']);assert m!=0 and 'Missing certificate' in mo
  target.write_bytes(saved+b' ');t,to=run([sys.executable,'-B','exact_certificate.py']);assert t!=0 and 'Stale/tampered' in to
 finally:target.write_bytes(saved)
 e,eo=run([sys.executable,'-B','exact_certificate.py','--create']);assert e!=0 and 'FileExistsError' in eo
 d=json.loads(saved);assert d['polynomial_deformation']['characters'][0]['presentation_quotient_dimension']==12
 assert d['cup_product']['invariant_mass_tensor_all_zero'] and d['derived_identification_gate']['potential_d3_source_dimension']==12
 files=['exact_certificate.py','geometry.json','certificate.json','Formalization.lean','Challenge.lean','REPORT.md','RELEASE_DISCLOSURE.md','formalization.yaml','verify.py']
 return {'passed':True,'python_executable':sys.executable,'lean_exit':code,'challenge_exit':cc,'axiom_reports':axioms,'certificate_replay':c,'negative_controls':{'missing':m!=0,'tampered':t!=0,'exclusive_create':e!=0,'restored':target.read_bytes()==saved},'physical_verdict':{'invariant_polynomial_moduli':12,'mass_tensor_shape':[12,9,6],'mass_tensor_zero':True,'potential_missing_d3_source':12},'hashes':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in files},'scope':'Local exact replay; polynomial subspace only; no hosted CI.'}
def main():
 d=calculate();text=json.dumps(d,sort_keys=True,indent=2)+'\n';p=P/'verification.json'
 if '--create' in sys.argv:
  with p.open('x') as h:h.write(text)
 else:
  assert p.exists(),'Missing verification receipt';assert p.read_text()==text,'Stale verification receipt'
 print(json.dumps(d['physical_verdict'],indent=2))
if __name__=='__main__':main()
