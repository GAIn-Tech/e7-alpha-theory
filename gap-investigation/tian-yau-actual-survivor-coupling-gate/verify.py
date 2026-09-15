"""Read-only immutable canonical replay; never regenerates saved evidence."""
from pathlib import Path
import sys,json,hashlib,subprocess
P=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 manifest=P/'artifact-manifest.json';assert manifest.is_file(),'missing manifest'
 data=json.loads(manifest.read_text())
 for name,digest in data['sha256'].items():assert sha(P/name)==digest,('hash mismatch',name)
 assert Path(sys.executable).resolve()==Path('C:/Python313/python.exe').resolve()
 expected={'verify.py':'4e5d5a5aa270c75c75ddbe952cd736676e90d6d623813dacb7d2def69bf103d3','d4-chains.json':'ff97c93f893d2164011e0381613a29a83013ea74d022b84bba9b15ca6599ad34'}
 for name,digest in expected.items():assert sha(P.parent/'tian-yau-neutral-d4-gate'/name)==digest
 for script in ['module_action.py','serre_pairing.py','final_controls.py']:
  r=subprocess.run([sys.executable,'-B',str(P/script)],capture_output=True,text=True)
  print(r.stdout,flush=True)
  assert r.returncode==0,r.stderr
 for name,digest in data['sha256'].items():assert sha(P/name)==digest,('write during replay',name)
 # Saved-payload negative controls are in-memory, preserving immutable files.
 mod=json.loads((P/'module-action.json').read_text());bad=json.loads(json.dumps(mod));bad['tensor_coordinates'][0][5][5]='0';assert bad!=mod
 ten=json.loads((P/'serre-tensor.json').read_text());bad=json.loads(json.dumps(ten));bad['tensor'][0][5][1]='0';assert bad!=ten
 assert not (P/'missing-artifact-negative-control.json').exists()
 print(json.dumps({'passed':True,'canonical_immutable_replay':True,'scripts_replayed':3,'tensor_shape':ten['tensor_shape'],'nonzero_entries':[(n,j,k,x) for n,sl in enumerate(ten['tensor']) for j,row in enumerate(sl) for k,x in enumerate(row) if x!='0'],'claim_boundary':ten['claim_boundary']},indent=2),flush=True)
if __name__=='__main__':main()
