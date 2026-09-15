"""Freeze read-only predecessors and retrieved source for this lane only."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,urllib.request
P=Path(__file__).resolve().parent
assert P==Path('C:/Users/mikeb/e7-alpha-theory/gap-investigation/tian-yau-instanton-higgs-insertion-gate')
files={'tian-yau-worldsheet-instanton-gate':['exact_certificate.py','certificate.json','REPORT.md','verify.py'], 'tian-yau-actual-survivor-coupling-gate':['module-action.json','serre-tensor.json','REPORT.md'], 'tian-yau-flavor-higgs-consistency-gate':['REPORT.md','certificate.json']}
manifest={}
for lane,names in files.items():
 for name in names:
  src=P.parent/lane/name; dest=P/'frozen'/lane/name
  dest.parent.mkdir(parents=True,exist_ok=True)
  if dest.exists(): assert dest.read_bytes()==src.read_bytes()
  else: shutil.copyfile(src,dest)
  manifest[str(dest.relative_to(P)).replace('\\','/')]={'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'canonical_source':str(src)}
(P/'sources').mkdir(exist_ok=True)
src=Path('C:/Users/mikeb/AppData/Local/hermes/cache/web/arxiv.org-79f7149634.md')
shutil.copyfile(src,P/'sources/yukawa.md')
S=Path('C:/Users/mikeb/AppData/Local/hermes/skills/research/grounded-citations/scripts/sources.py')
cmd=[sys.executable,str(S),'--ledger',str(P/'sources/ledger.json')]
subprocess.run(cmd+['add','https://arxiv.org/html/2402.13563v1','--title','Modular forms and hierarchical Yukawa couplings in heterotic Calabi-Yau compactifications'],check=True)
subprocess.run(cmd+['quote','1','--text','However, it will be corrected by instanton contributions.','--from',str(P/'sources/yukawa.md')],check=True)
manifest['sources/yukawa.md']={'sha256':hashlib.sha256((P/'sources/yukawa.md').read_bytes()).hexdigest()}
out=P/'input-manifest.json'
data=json.dumps(manifest,sort_keys=True,indent=2)+'\n'
if out.exists(): assert out.read_text()==data
else: out.write_text(data)
print(json.dumps({'frozen_inputs':len(manifest),'canonical':str(P)}))
