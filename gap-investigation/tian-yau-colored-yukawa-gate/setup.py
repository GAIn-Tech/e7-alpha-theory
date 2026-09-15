"""Exclusive source freezer. Writes only this lane; never updates predecessors."""
from pathlib import Path
import shutil,json,hashlib
P=Path(__file__).resolve().parent
assert P==Path('C:/Users/mikeb/e7-alpha-theory/gap-investigation/tian-yau-colored-yukawa-gate')
assert not (P/'source-manifest.json').exists()
files=['tian-yau-survivor-yoneda-gate/exact_audit.py','tian-yau-neutral-d2-gate/partial_chains.py','tian-yau-neutral-d2-gate/try_d2.py','tian-yau-neutral-d2-gate/total_cech.py','tian-yau-neutral-d4-gate/compute.py','tian-yau-actual-survivor-coupling-gate/module_action.py','tian-yau-actual-survivor-coupling-gate/serre_pairing.py','tian-yau-actual-survivor-coupling-gate/serre-tensor.json','tian-yau-actual-survivor-coupling-gate/artifact-manifest.json','tian-yau-flavor-higgs-consistency-gate/REPORT.md','tian-yau-flavor-higgs-consistency-gate/certificate.json','tian-yau-flavor-higgs-consistency-gate/release-manifest.json','tian-yau-bundle-coupling-gate/geometry.json']
for name in files:
 target=P/'frozen'/name;target.parent.mkdir(parents=True,exist_ok=True)
 assert not target.exists();shutil.copy2(P.parent/name,target)
ring=(P/'explore_ring.py').read_text().replace("P.parent/'tian-yau-bundle-coupling-gate/geometry.json'","P/'frozen/tian-yau-bundle-coupling-gate/geometry.json'")
with (P/'ring.py').open('x',newline='\n') as f:f.write(ring)
ex=(P/'exterior_diagonal.py').read_text().replace('import explore_ring as r','import ring as r')
with (P/'exterior.py').open('x',newline='\n') as f:f.write(ex)
manifest={str(x.relative_to(P)).replace('\\','/'):hashlib.sha256(x.read_bytes()).hexdigest() for x in [P/'calculate.py',P/'ring.py',P/'exterior.py',P/'setup.py']+sorted((P/'frozen').rglob('*')) if x.is_file()}
with (P/'source-manifest.json').open('x',newline='\n') as f:f.write(json.dumps(manifest,sort_keys=True,indent=2)+'\n')
print('frozen',len(manifest),'sources')
