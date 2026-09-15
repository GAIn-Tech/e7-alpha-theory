from pathlib import Path
import json
import dual_exterior as d
P=Path(__file__).resolve().parent
src=json.loads((P/'frozen/tian-yau-colored-yukawa-gate/charged-dual-bases.json').read_text())
vs={ch:[d.from_dual(d.u.unpack(r['cocycle'])) for r in src['characters'][str(ch)]['records']] for ch in [1,2]}
betas=json.loads((P/'frozen/tian-yau-colored-yukawa-gate/frozen/tian-yau-actual-survivor-coupling-gate/serre-tensor.json').read_text())['dual_cocycles'][:2]
betas=[d.from_dual(d.u.unpack(v)) for v in betas]
for ch in vs:
 for v in vs[ch]:d.validate(v,1,ch);assert not d.D(v)
for k,b in enumerate(betas):
 eta=d.beta_primitive(k);db=d.D(eta);bform=d.add(b,d.scale(db,-1));assert not d.D(bform)
 print('beta',k,len(bform),len(d.raw_b_projection(bform)))
 for i,a in enumerate(vs[1]):
  for j,c in enumerate(vs[2]):
   prod=d.wedge(d.wedge(a,c),b);new=d.wedge(d.wedge(a,c),bform);primitive=d.wedge(d.wedge(a,c),eta)
   assert not d.D(prod)
   assert d.add(prod,d.scale(new,-1))==d.D(primitive)
   print(k,i,j,'prod',len(prod),'omega',len(d.raw_b_projection(new)))
print('PASS')
