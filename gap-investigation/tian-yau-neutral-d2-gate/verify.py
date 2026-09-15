"""Immutable full replay for the actual invariant geometric d2 release."""
from pathlib import Path
import sys,json,hashlib,subprocess
sys.dont_write_bytecode=True
import partial_chains as a
import try_d2 as candidate
import total_cech as total
import representative_controls as controls
s=a.s
P=Path(__file__).resolve().parent

def text(d):return json.dumps(d,sort_keys=True,indent=2)+'\n'
def match(path,d):
 assert path.is_file(),f'missing saved artifact: {path.name}'
 assert path.read_text()==text(d),f'stale or tampered artifact: {path.name}'

def calculate():
 match(P/'partial-character-0.json',a.run(0))
 # The diagnostic stage used json.dump without terminal newline; preserve it.
 cd=candidate.calculate();assert json.loads((P/'curved-koszul-diagnostic.json').read_text())==cd
 td=total.calculate();match(P/'total-cech-lifts.json',td)
 rc=controls.calculate();match(P/'representative-controls.json',rc)
 M=candidate.decode(td['matrix']);assert M==candidate.decode(cd['curved_Koszul_d2_candidate'])
 assert M.shape==(60,60) and M.rank()==60
 inv=M.inv();assert M*inv==s.eye(60) and inv*M==s.eye(60)
 mat={'character':0,'source_bidegree':[-1,2],'target_bidegree':[1,1],'shape':[60,60],'rank':M.rank(),'determinant':str(M.det()),'dense_entries':[[str(M[i,j]) for j in range(M.cols)] for i in range(M.rows)],'sparse':a.sparse(M),'inverse':a.sparse(inv),'basis_receipt':'partial-character-0.json','total_lifts_receipt':'total-cech-lifts.json','representative_controls_receipt':'representative-controls.json'}
 # Deliberately corrupted payload must fail the actual saved-matrix comparator.
 # In creation mode matrix is not yet present, so use the saved total-lift payload.
 bad=dict(td);bad['matrix']=dict(td['matrix']);badM=M.copy();badM[0,0]+=1;bad['matrix']=a.sparse(badM)
 try:match(P/'total-cech-lifts.json',bad)
 except AssertionError:pass
 else:raise AssertionError('matrix mutation not rejected')
 try:match(P/'never-created-negative-control.json',{})
 except AssertionError:pass
 else:raise AssertionError('missing artifact not rejected')
 pre=P.parent/'tian-yau-survivor-yoneda-gate/verify.py'
 replay=subprocess.run([sys.executable,'-B',str(pre)],capture_output=True,text=True)
 assert replay.returncode==0,replay.stderr
 pred=json.loads(replay.stdout);assert pred['passed']
 names=['partial_chains.py','try_d2.py','total_cech.py','representative_controls.py','verify.py','REPORT.md','partial-character-0.json','curved-koszul-diagnostic.json','total-cech-lifts.json','representative-controls.json']
 hashes={n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in names}
 receipt={'passed':True,'geometric_d2_computed':True,'character':0,'matrix_shape':[60,60],'rank':M.rank(),'kernel_dimension':M.cols-M.rank(),'cokernel_dimension':M.rows-M.rank(),'determinant':str(M.det()),'all_60_total_lift_equations_verified':td['total_lift_equations_verified'],'nilpotence_on_all_source_and_primitive_lifts':td['full_total_nilpotence_on_lifts'],'wrong_curvature_sign_detected_columns':td['wrong_curvature_sign_nonzero_columns'],'representative_control_summary':{k:v for k,v in rc.items() if k!='records'},'canonical_predecessor_replay_exit_code':replay.returncode,'canonical_predecessor_replay_output':pred,'E3_invariant_slots':{'-1,2':0,'1,1':0,'-2,3':4,'1,0':12},'remaining_invariant_differential':'d4: (-2,3)->(2,0), shape 4x4; not computed','invariant_Ext1_dimension_bounds':[12,16],'invariant_Ext1_formula':'16-rank(d4_invariant)','other_character_d2_computed':False,'full_Higgs_vacuum_claim':False,'claim_boundary':'Actual exact invariant geometric d2 via a curved-End Koszul resolution, full Cech lifts, and representative controls. d4 and other-character higher pages remain unresolved. No full neutral count or Higgs vacuum.','interpreter':sys.executable.replace('\\','/'),'sympy_version':s.__version__,'artifact_hashes':hashes,'matrix_payload_sha256':hashlib.sha256(text(mat).encode()).hexdigest()}
 return receipt,mat

if __name__=='__main__':
 # Existing artifacts must be present before computation in replay mode.
 creating='--create' in sys.argv
 if not creating:assert (P/'receipt.json').is_file() and (P/'d2-invariant-matrix.json').is_file(),'missing final artifact'
 d,M=calculate()
 if creating:
  for name,obj in [('d2-invariant-matrix.json',M),('receipt.json',d)]:
   with (P/name).open('x',newline='\n') as h:h.write(text(obj))
 else:
  match(P/'d2-invariant-matrix.json',M);match(P/'receipt.json',d)
 print(json.dumps({k:v for k,v in d.items() if k not in ['artifact_hashes','canonical_predecessor_replay_output','representative_control_summary']},indent=2))

