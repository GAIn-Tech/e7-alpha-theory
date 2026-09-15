"""Exact boundary certificate for the unresolved Tian--Yau d3.

This deliberately does not replace the geometric d3 by a generic-rank matrix.
It reconstructs the stated source and its Z/3 grading and records the unique
spectral-sequence bidegree.  A passed receipt means the boundary is correct,
not that d3 has been computed.
"""
from itertools import combinations
from pathlib import Path
from fractions import Fraction
import hashlib, json, sys

P=Path(__file__).resolve().parent
PRE=P.parent/'tian-yau-bundle-coupling-gate'
G=json.loads((PRE/'geometry.json').read_text(encoding='utf-8'))
w=G['weights']

# End(K), with K^{-1}=A, K^0=B, K^1=C: d_r:(p,q)->(p+r,q-r+1).
source_bidegree=(-2,2)
target_bidegree=(1,0)
assert (source_bidegree[0]+3,source_bidegree[1]-3+1)==target_bidegree
assert sum(source_bidegree)==0 and sum(target_bidegree)==1

# Serre/Koszul labels used by the predecessor: off-diagonal Cx->Ay and
# Cy->Ax classes are dual to square-free quadrics in the corresponding P3.
source=[]
for block,offset in [('Cx_to_Ay',0),('Cy_to_Ax',4)]:
    for i,j in combinations(range(4),2):
        # predecessor qchar is phase(q)-sum(weights of opposite P3);
        qphase=(w[offset+i]+w[offset+j])%3
        opposite=sum(w[4:]) if offset==0 else sum(w[:4])
        dual_character=(-(qphase-opposite))%3
        source.append({'summand':block,'pair':[i,j],
                       'dual_monomial':('x' if offset==0 else 'y')+str(i)+'*'+('x' if offset==0 else 'y')+str(j),
                       'character':dual_character})
counts=[sum(a['character']==c for a in source) for c in range(3)]
assert len(source)==12 and counts==[4,4,4]

# The actual zig-zag starts with the signed End-complex differential.
# For phi:C->A (degree -2), [d_K,phi]=d_K phi-phi d_K, hence components
# C->B and B->A are E phi and -phi J.  Subsequent arrows require specified
# vertical (Cech/Koszul) primitives; cohomology dimensions do not determine
# those primitives or the endpoint matrix.
zigzag={'K_degrees':{'A':-1,'B':0,'C':1},
        'endomorphism_sign':'D(phi)=d_K*phi-(-1)^deg(phi)*phi*d_K',
        'degree_minus_2_components':['C_to_A'],
        'first_horizontal_components':{'C_to_B':'+E*phi','B_to_A':'-phi*J'},
        'required_vertical_primitives':2,
        'endpoint':'End^1 = Hom(A,B) direct_sum Hom(B,C)',
        'well_definedness_condition':'changing either vertical primitive changes endpoint by d1-boundary'}

# Negative control: dimensions/characters admit inequivalent maps, so maximal
# rank cannot be inferred.  Zero and block injections both commute with Z3.
target_dims=[12,14,14]
possible_ranks={'zero':[0,0,0],'block_injection':[4,4,4]}
assert all(possible_ranks['block_injection'][c] <= min(counts[c],target_dims[c]) for c in range(3))
assert possible_ranks['zero'] != possible_ranks['block_injection']

result={'passed':True,'d3_computed':False,
 'claim_boundary':'Exact source, characters, signs and bidegree only. The geometric d3 and charged Yoneda action remain unresolved; no maximal-rank or zero-map assumption is made.',
 'source':{'dimension':len(source),'characters':counts,'basis':source,'bidegree':list(source_bidegree)},
 'target':{'polynomial_quotient_characters':target_dims,'bidegree':list(target_bidegree)},
 'zigzag_convention':zigzag,
 'underdetermination_negative_control':{'equivariant_candidate_block_ranks':possible_ranks,'conclusion':'grading and dimensions alone do not fix d3'},
 'charged_action':{'computed':False,'reason':'depends on geometric d3 survivors; assigning couplings before that would be arbitrary'},
 'source_hashes':{'../tian-yau-bundle-coupling-gate/geometry.json':hashlib.sha256((PRE/'geometry.json').read_bytes()).hexdigest(),
                  '../tian-yau-bundle-coupling-gate/exact_certificate.py':hashlib.sha256((PRE/'exact_certificate.py').read_bytes()).hexdigest()}}
text=json.dumps(result,sort_keys=True,indent=2)+'\n'
out=P/'certificate.json'
if '--create' in sys.argv:
    with out.open('x',encoding='utf-8') as f:f.write(text)
else:
    assert out.exists(),'Missing certificate; create exclusively with --create'
    assert out.read_text(encoding='utf-8')==text,'Stale/tampered certificate'
print(json.dumps({'passed':True,'d3_computed':False,'source_characters':counts,'claim_boundary':result['claim_boundary']},indent=2))
