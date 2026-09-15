"""Independent saved-boundary replay, full Koszul-sign controls, and Higgs representative changes."""
import calculate as k
from itertools import combinations,product
r,e,s=k.r,k.e,k.s
F=k.F

def decode(rows):return {int(i):F(v) for i,v in rows}
def unpack(rows):return {(tuple(t),tuple(I),tuple(ex)):F(x) for t,I,ex,x in rows}
def main():
 d=k.json.loads((k.P/'certificate.json').read_text());data=k.json.loads((k.P/'charged-wedge-chains.json').read_text())
 top=data['quotients'][-1];bs=[tuple(b) for b in top['monomial_basis']];idx={b:i for i,b in enumerate(bs)};piv={};raw=top['raw_boundaries']
 for rec in top['boundary_DAG']:
  origin=raw[rec['origin']];v=decode(origin['image']);primitive=unpack(origin['primitive']);actual=k.D(primitive)
  def vchain(v):return k.add(*(k.scale(k.monchain(bs[i]),x) for i,x in v.items()))
  assert actual==vchain(v)
  for i,xx in rec['subtract_pivots']:
   assert i in piv
   for j,y in piv[i].items():r.addto(v,j,-F(xx)*y)
  v={i:x/F(rec['divisor']) for i,x in v.items()};assert v==decode(rec['image']);piv[rec['pivot']]=v
 assert len(bs)-len(piv)==1
 for rec in data['products']:
  v={top['free_indices'][0]:F(rec['coordinate'])};v={i:x for i,x in v.items() if x}
  for i,xx in rec['boundary_DAG_combination']:
   for j,y in piv[i].items():r.addto(v,j,F(xx)*y)
  assert vchain(v)==unpack(rec['wedge_cocycle'])
 # Check H0 completeness independently by the regular-sequence Koszul Hilbert series,
 # character by character, against full inherited sheaf line-cohomology.
 h0=0
 for dd in sorted({e.info(t)[1] for t in e.triples}):
  expected=[0,0,0]
  for n in range(4):
   for I in combinations(range(3),n):
    da=dd[0]-sum(r.deg[h][0] for h in I);db=dd[1]-sum(r.deg[h][1] for h in I)
    for ex in r.comps(da,4):
     for ee in r.comps(db,4):expected[sum(a*b for a,b in zip(ex+ee,r.w))%3]+=(-1)**n
  assert expected==k.a.line(*dd)[0];h0+=1
 # Koszul curvature nilpotence on all exterior-cube basis generators and every exterior-Koszul sector.
 full=bad=0
 for t in e.triples:
  for n in range(4):
   for I in combinations(range(3),n):
    v={(t,I,(0,)*8):F(1)};assert not k.D(k.D(v));full+=1
    if k.D(k.D(v,True),True):bad+=1
 # Keywise Leibniz also uses nonclosed generators; degree signs cannot be masked by testing closed products alone.
 leib=0
 for i,j in product(range(13),repeat=2):
  for I,J in [((),()),((0,),()),((),(1,)),((0,),(1,))]:
   v={((i,),I,(0,)*8):F(1)};w={((j,),J,(0,)*8):F(1)};deg=e.terms[i][2]-len(I)
   assert k.D(k.wedge(v,w))==k.add(k.wedge(k.D(v),w),k.scale(k.wedge(v,k.D(w)),(-1)**deg));leib+=1
 # Nonzero primitive and boundary for every admitted invariant Higgs boundary.
 qs0=data['quotients'][0];higgs_changes=nonzero=0
 for origin in qs0['raw_boundaries']:
  eta=unpack(origin['primitive']);de=k.D(eta)
  if not de:continue
  assert eta
  for b,bb in product(d['bases']['2'],d['bases']['1']):
   uv=k.wedge(k.monchain(b),k.monchain(bb));primitive=k.wedge(uv,eta);delta=k.wedge(uv,de)
   assert k.D(primitive)==delta;higgs_changes+=1
   if delta:nonzero+=1
   vec={}
   for (t,I,ex),x in delta.items():
    assert not I;mon=tuple(t.count(10+i) for i in range(3))+ex;r.addto(vec,idx[mon],x)
   while vec:
    i=max(vec);x=vec[i];assert i in piv
    for j,y in piv[i].items():r.addto(vec,j,-x*y)
 assert nonzero>0
 Y=[s.Matrix(t).applyfunc(s.Rational) for t in d['relative_two_slices']]
 independent=[e.rank([{i:F(str(M[i,j])) for i in range(M.rows) if M[i,j]} for j in range(M.cols)]) for M in Y+[Y[0].row_join(Y[1])]]
 assert independent==d['slice_ranks']+[d['per_color_rank']]
 # Exact minor and wrong-flavor negative controls: c1 alone really has a null row;
 # assigning its rank seven is rejected independently of the overall colored block.
 assert not any(Y[1][5,:]) and Y[1].rank()==6
 assert Y[0].det()!=0
 lam=s.Symbol('lambda',nonzero=True)
 assert (lam*Y[0]).det()==lam**7*Y[0].det()
 result={'passed':True,'boundary_DAG_pivots':len(piv),'product_boundary_equalities':len(data['products']),'H0_character_checks':h0,'full_Koszul_sector_nilpotence':full,'wrong_curvature_failures':bad,'nonclosed_keywise_Leibniz':leib,'Higgs_boundary_changes':higgs_changes,'nonzero_Higgs_boundary_products':nonzero,'independent_ranks':independent,'absolute_comparison_factor_computed':False}
 payload=k.text(result);path=k.P/'supplementary-audit.json'
 if '--create' in k.sys.argv:
  with path.open('x',newline='\n') as f:f.write(payload)
 else:assert path.is_file() and path.read_text()==payload
 print(payload,flush=True)
if __name__=='__main__':main()
