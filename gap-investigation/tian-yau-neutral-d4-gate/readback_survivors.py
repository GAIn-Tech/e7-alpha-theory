"""Independent readback of saved chain data, admissibility and survivor export."""
from pathlib import Path
import json,hashlib,sys
import compute as m
c,a,s=m.c,m.a,m.s
P=Path(__file__).resolve().parent

def unpack(rows):return {(tuple(pair),tuple(I),tuple(e),tuple(X),tuple(Y)):c.F(v) for pair,I,e,X,Y,v in rows}
def main():
 payload=(P/'d4-chains.json').read_bytes();data=json.loads(payload)
 receipt=json.loads((P/'receipt.json').read_text())
 assert hashlib.sha256(payload).hexdigest()==receipt['chain_payload_sha256']
 X=[];outs=[];valid=0
 for rec in data['records']:
  v0=unpack(rec['initial_source']);vs=[v0]+[unpack(r) for r in rec['primitives']];v4=unpack(rec['fourth_vertical_primitive']);full=unpack(rec['surviving_total_cocycle'])
  assert full==c.add(*vs,v4) and not c.total(full)
  assert not c.dv(v0)
  for step in range(1,4):
   rhs=c.d1(vs[step-1])
   if step>=2:rhs=c.add(rhs,c.d2cor(vs[step-2]))
   assert c.add(c.dv(vs[step]),rhs)=={}
  actual_end=c.add(c.d1(vs[3]),c.d2cor(vs[2]))
  assert actual_end==unpack(rec['raw_endpoint'])
  assert c.add(actual_end,c.dv(v4))=={}
  for key in full:
   pair,I,e,xx,yy=key;i,j=pair
   assert I==tuple(sorted(set(I))) and set(I)<=set(range(3))
   dd=tuple(c.terms[j][3][b]-c.terms[i][3][b]-sum(a.deg[h][b] for h in I) for b in range(2))
   assert (sum(e[:4]),sum(e[4:]))==dd
   for E,U in [(e[:4],xx),(e[4:],yy)]:
    assert U and U==tuple(sorted(set(U))) and set(U)<=set(range(4))
    assert all(n in U for n,t in enumerate(E) if t<0),'inadmissible localization'
   assert (sum(x*y for x,y in zip(e,a.w))+m.weight(i)-m.weight(j))%3==0
   p,q,k=c.grade(key);assert p+q-k==1
   valid+=1
  x=s.Matrix([s.Rational(v) for v in rec['E1_source_coordinates']]);assert m.hcoords(v0,-2,3)==x;X.append(x)
  outs.append({'label':'neutral-d4-survivor-'+str(rec['column']),'total_degree':1,'character_mod_3':0,'E1_source_coordinates':rec['E1_source_coordinates'],'total_cocycle':rec['surviving_total_cocycle']})
 source=s.Matrix.hstack(*X);assert source.rank()==len(outs)
 M=m.c.t.decode(data['matrix']);rank=M.rank();ker=M.nullspace()
 assert rank==data['rank'] and M.cols-rank==len(ker)==len(outs)
 d={'passed':True,'serialized_lifts_rechecked':True,'all_terms_admissible_and_invariant':True,'admissible_terms_with_multiplicity':valid,'source_independent_rank':source.rank(),'derived_endpoint_rank':rank,'derived_kernel_dimension':len(ker),'chain_payload_sha256':hashlib.sha256(payload).hexdigest(),'survivors':outs,'boundary':'Explicit total cocycles only; no Yoneda tensor or F-flatness assertion.'}
 text=json.dumps(d,sort_keys=True,indent=2)+'\n';out=P/'survivor-representatives.json'
 if '--create' in sys.argv:
  with out.open('x',newline='\n') as f:f.write(text)
 else:assert out.is_file() and out.read_text()==text
 print(json.dumps({k:v for k,v in d.items() if k!='survivors'},indent=2))
if __name__=='__main__':main()
