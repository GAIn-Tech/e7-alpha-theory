"""Replay saved receipt before any creation; preserve real subprocess output."""
from pathlib import Path
import json,subprocess,sys,hashlib,copy,platform
HERE=Path(__file__).resolve().parent

def verify(path,expected):
 actual=json.loads(Path(path).read_text())
 assert actual==expected,'full payload mismatch'
 for p,h in actual['source_hashes'].items():
  assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,'source hash mismatch'
 return True

def main():
 old=json.loads((HERE/'receipt.json').read_text()) # fail closed if missing, never recreate
 verify(HERE/'receipt.json',old)
 cmd=[sys.executable,'-B',str(HERE/'diagnostic.py')]
 p=subprocess.run(cmd,capture_output=True,text=True,cwd=HERE)
 result={'command':cmd,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'python':sys.version,'platform':platform.platform()}
 assert p.returncode==0,p.stderr
 new=json.loads(p.stdout);assert new==old
 controls={}
 for name,mutation in [('tamper_curvature',lambda r:r['gauge_modes']['octet'].update(canonical_curvature_S='-1')),('tamper_hash',lambda r:r['source_hashes'].update({next(iter(r['source_hashes'])):'0'*64}))]:
  tmp=HERE/(name+'.json');bad=copy.deepcopy(old);mutation(bad)
  with tmp.open('x') as f:json.dump(bad,f)
  try:
   try:verify(tmp,old)
   except AssertionError:controls[name]=True
   else:raise AssertionError('corruption accepted')
  finally:tmp.unlink()
 missing=HERE/'intentionally-missing-receipt.json';assert not missing.exists()
 try:verify(missing,old)
 except FileNotFoundError:controls['missing_receipt']=True
 else:raise AssertionError('missing accepted')
 result['controls']=controls;result['passed']=True
 result['artifact_hashes']={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [HERE/'diagnostic.py',HERE/'receipt.json',HERE/'REPORT.md',Path(__file__),*sorted((HERE/'sources').glob('*.txt'))]}
 (HERE/'verification.json').write_text(json.dumps(result,indent=2))
 print(json.dumps({'passed':True,'prerequisite_replayed':new['prerequisite_replayed'],'replay_exit':p.returncode,'controls':controls,'verification':str(HERE/'verification.json'),'local_bound':new['combined_bound_lambda_over_g_squared'],'energy_bound':new['combined_SU4_energy_bound_lambda_over_g_squared']},indent=2))
if __name__=='__main__':main()
