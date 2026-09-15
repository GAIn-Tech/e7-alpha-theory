import json,hashlib,subprocess,sys,tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
PY=sys.executable

def run(args):
 r=subprocess.run([PY,'-B',*map(str,args)],cwd=HERE,capture_output=True,text=True)
 return {'command':[PY,'-B',*map(str,args)],'exit':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
def main():
 receipts=['receipt.json','resummation-receipt.json','soft-tadpole-receipt.json']
 pre={}
 for name in receipts:
  p=HERE/name;assert p.exists();d=json.loads(p.read_text());assert d['passed']
  pre[name]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'source_hashes_checked':0}
  for q,h in d['source_hashes'].items():assert hashlib.sha256(Path(q).read_bytes()).hexdigest()==h;pre[name]['source_hashes_checked']+=1
 results=[run(['calculation.py']),run(['resummation.py']),run(['soft_tadpole.py'])]
 assert all(x['exit']==0 for x in results)
 controls={}
 with tempfile.TemporaryDirectory(dir=HERE) as td:
  td=Path(td);p=td/'receipt.json';p.write_text((HERE/'receipt.json').read_text().replace('"passed": true','"passed": false',1))
  # Replay in a copied lane without all declared files must fail before computation.
  (td/'calculation.py').write_bytes((HERE/'calculation.py').read_bytes())
  controls['tampered_or_incomplete_copy']=run([td/'calculation.py'])
  assert controls['tampered_or_incomplete_copy']['exit']!=0
 controls['missing_receipt']=None
 with tempfile.TemporaryDirectory(dir=HERE) as td:
  td=Path(td);(td/'resummation.py').write_bytes((HERE/'resummation.py').read_bytes());controls['missing_receipt']=run([td/'resummation.py']);assert controls['missing_receipt']['exit']!=0
 out={'passed':True,'pre_replay_hash_checks':pre,'replays':results,'negative_file_controls':controls,'report_sha256':hashlib.sha256((HERE/'REPORT.md').read_bytes()).hexdigest()}
 (HERE/'verification.json').write_text(json.dumps(out,indent=2))
 print(json.dumps({'passed':True,'replay_exits':[x['exit'] for x in results],'negative_exits':[x['exit'] for x in controls.values()]},indent=2))
if __name__=='__main__':main()
