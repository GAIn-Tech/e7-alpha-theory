"""Exclusive source freeze, or durable native replay with an exit receipt."""
from pathlib import Path
import sys,json,hashlib,subprocess,datetime
P=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def text(d):return json.dumps(d,sort_keys=True,indent=2)+'\n'
def main():
 if '--freeze' in sys.argv:
  import module_action as u
  files=set(P.glob('*.py'))|set(P.glob('*.md'))|{P/n for n in ['module-action.json','serre-tensor.json','final-controls.json']}
  for mod in list(sys.modules.values()):
   f=getattr(mod,'__file__',None)
   if f:
    p=Path(f).resolve()
    if p.is_relative_to(P.parent.parent) and p.suffix=='.py':files.add(p)
  for n in ['d4-chains.json','verify.py','receipt.json','native-replay-status.json']:files.add(P.parent/'tian-yau-neutral-d4-gate'/n)
  files.add(P.parent/'tian-yau-bundle-coupling-gate/geometry.json');files.add(P.parent/'tian-yau-wilson-line-gate/interactions.py')
  import os
  d={'interpreter':sys.executable.replace('\\','/'),'sympy':u.s.__version__,'sha256':{os.path.relpath(p,P).replace('\\','/'):sha(p) for p in sorted(files)},'scope':'Frozen release sources, exact payloads and read-only predecessor inputs. Historical failed-control snapshot is provenance, not executed by verify.py.'}
  with (P/'artifact-manifest.json').open('x',newline='\n') as h:h.write(text(d))
  print('frozen',len(files),'files')
 else:
  started=datetime.datetime.now(datetime.timezone.utc).isoformat();manifest=sha(P/'artifact-manifest.json')
  with (P/'native-replay.log').open('x',newline='\n') as log:
   r=subprocess.run([sys.executable,'-B',str(P/'verify.py')],stdout=log,stderr=subprocess.STDOUT,cwd=P)
  d={'started_utc':started,'ended_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':r.returncode,'command':[sys.executable.replace('\\','/'),'-B',str(P/'verify.py').replace('\\','/')],'manifest_sha256':manifest,'manifest_unchanged':sha(P/'artifact-manifest.json')==manifest,'log_sha256':sha(P/'native-replay.log')}
  with (P/'native-replay-status.json').open('x',newline='\n') as h:h.write(text(d))
  print(text(d),flush=True);sys.exit(r.returncode)
if __name__=='__main__':main()
