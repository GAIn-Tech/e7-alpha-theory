"""Immutable native replay; require the saved certificate and release manifest."""
from pathlib import Path
import hashlib,json,subprocess,sys
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 mf=P/'release-manifest.json'
 frozen=mf.read_bytes()
 manifest=json.loads(frozen)
 for rel,h in manifest.items():assert sha(P/rel)==h,rel
 proc=subprocess.run([sys.executable,'-B',str(P/'calculate.py')],capture_output=True,text=True)
 print(proc.stdout,end='');print(proc.stderr,end='',file=sys.stderr)
 assert proc.returncode==0,'exact calculation failed'
 assert mf.read_bytes()==frozen
 for rel,h in manifest.items():assert sha(P/rel)==h,rel
 print(json.dumps({'passed':True,'manifest_unchanged':True,'manifest_sha256':sha(mf),'verification':'Native exact SymPy replay. Analytic theorem written, not Lean formalized.'},sort_keys=True))
if __name__=='__main__':main()
