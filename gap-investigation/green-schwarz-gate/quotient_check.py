"""Supplementary exact global-quotient check; does not claim all-bundle sufficiency."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
H=Path(__file__).resolve().parent
b=json.loads((H.parent/'embedding-gate/embedding-receipt.json').read_text())
r=json.loads((H/'receipt.json').read_text())
mu=list(map(F,r['central_coweight'])); x=list(map(F,b['X_coroot_coefficients']))
res=[]
for s in (F(1,3),F(-1,3)):
 vals=[sum(w[i]*mu[i] for i in range(6))+s*sum(a*c for a,c in zip(w,x)) for w in b['weights56']]
 res.append({'u1_component':str(s),'all_56_pairings_integral':all(v.denominator==1 for v in vals),'pairings':list(map(str,vals))})
assert res[0]['all_56_pairings_integral'] and not res[1]['all_56_pairings_integral']
payload={'passed':True,'checks':res,'claim_boundary':'Cocharacter admissibility checked on faithful 56 only; no full global anomaly classification.','source_hash':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
p=H/'quotient-receipt.json'
import sys
if '--create' in sys.argv:
 with p.open('x') as f:json.dump(payload,f,indent=2)
else:assert json.loads(p.read_text())==payload
print('Faithful-56 quotient cocharacter +1/3 passes; -1/3 rejected.')
