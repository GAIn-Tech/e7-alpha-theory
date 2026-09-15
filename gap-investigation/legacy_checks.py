"""Exact finite falsification of the stated exp47 flux search and exp44 dimensions.
Uses the literal experiment domains, not randomly generated empirical data.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib
import json
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parent
# exp47:895 samples exactly four integers from [0,10]. Exhaust that domain.
fluxes=list(product(range(11),repeat=4))
values=[F(133)+F(sum(f),14) for f in fluxes]
accepted=[f for f,y in zip(fluxes,values) if abs(y-137)<F(1,10)]
assert len(fluxes)==11**4
assert not accepted
assert max(values)<F('136.9')
# Even allowing four entries up to 56, sum=56 is not a unique tuple.
witnesses=[(14,14,14,14),(7,7,21,21)]
assert len(set(witnesses))==2 and all(sum(f)==56 for f in witnesses)
# These are algebraic dimension contradictions, not a tensor decomposition proof.
true_symdim=56*57//2
claimed_symdim=1+1463
assert true_symdim!=claimed_symdim
assert true_symdim==133+1463
assert 56*55//2==1+1539
# Counterexample to normalized vector => uniform squared amplitudes.
v=[F(1)]+[F(0)]*55
assert sum(x*x for x in v)==1 and v[0]**2!=F(1,56)
result={'passed':True,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'sources_sha256':{f:hashlib.sha256((REPO/f).read_bytes()).hexdigest() for f in ['exp44_lagrangian_derivation.py','exp47_unique_vacuum.py']},'flux_domain':'four integers each 0..10 inclusive; exp47 line 895','enumerated_count':len(fluxes),'alpha_inverse_max':str(max(values)),'candidate_count_within_0_1_of_137':len(accepted),'reported_eight_entry_solution_outside_domain':True,'nonunique_sum56_examples_in_expanded_domain':witnesses,'symmetric_square_dimension':true_symdim,'exp44_claimed_symmetric_dimension':claimed_symdim,'unit_norm_counterexample_first_component_squared':str(v[0]**2),'claim_boundary':'Exact failures of these literal toy search/dimension/normalization claims only; no general flux-vacuum nonexistence theorem, no proof of the physical E7 tensor decomposition.'}
(ROOT/'legacy-checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
