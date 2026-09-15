"""Mixed-character dual H1 cocycles; no conjugate cubic is inferred from dimensions."""
import calculate as k
import importlib,json,sys
from functools import lru_cache
from itertools import combinations
u,m,c,a,s=k.u,k.m,k.c,k.a,k.s
sp=importlib.import_module('serre_pairing')
CH=0
@lru_cache(None)
def basis(pair,q,kk):
 i,j=pair;dd=tuple(y-x for x,y in zip(c.terms[i][3],c.terms[j][3]));out=[]
 for I in combinations(range(3),kk):
  aq,es=a.ambient(*(dd[b]-sum(a.deg[h][b] for h in I) for b in range(2)))
  if aq!=q:continue
  for ex in es:
   if (sum(x*y for x,y in zip(ex,a.w))+m.weight(i)-m.weight(j))%3==CH:out.append((pair,I,ex))
 return out
m.basis=basis

def validate(v):
 assert not c.total(v)
 for key in v:
  pair,I,ex,X,Y=key;i,j=pair
  assert (sum(x*y for x,y in zip(ex,a.w))+m.weight(i)-m.weight(j))%3==CH
  p,q,kk=c.grade(key);assert p+q-kk==1
  assert tuple(sum(ex[4*b:4*b+4]) for b in range(2))==tuple(c.terms[j][3][b]-c.terms[i][3][b]-sum(a.deg[h][b] for h in I) for b in range(2))
  assert all(all(n in U for n,t in enumerate(E) if t<0) for E,U in [(ex[:4],X),(ex[4:],Y)])

def main():
 global CH
 out={}
 for ch in [1,2]:
  CH=ch
  for fn in [basis,m.kmat,m.cohom,sp.classes]:fn.cache_clear()
  rows={}
  for q in range(4):
   A=sp.drow(-1,q);B=sp.drow(0,q);assert not any(B*A)
   dims=[len(sp.classes(p,q)) for p in [-1,0,1]]
   rows[q]={'dims':dims,'ranks':[A.rank(),B.rank()],'E2':[dims[0]-A.rank(),dims[1]-A.rank()-B.rank(),dims[2]-B.rank()],'A':a.sparse(A),'B':a.sparse(B)}
  assert rows[0]['E2'][2]==rows[1]['E2'][1]==0
  mat=sp.drow(-1,2);records=[]
  for j,x in enumerate(mat.nullspace()):
   v0=m.combine(sp.classes(-1,2),x)
   v1=m.primitive(c.scale(c.d1(v0),-1))
   v2=m.primitive(c.scale(c.add(c.d1(v1),c.d2cor(v0)),-1))
   full=c.add(v0,v1,v2);validate(full)
   assert not c.add(c.dv(v1),c.d1(v0)) and not c.add(c.dv(v2),c.d1(v1),c.d2cor(v0))
   records.append({'coordinates':[str(v) for v in x],'initial':c.pack(v0),'primitive1':c.pack(v1),'primitive2':c.pack(v2),'cocycle':c.pack(full)})
  assert len(records)==4
  out[str(ch)]={'rows':rows,'records':records,'H1_dimension':len(records)}
  print('dual character',ch,'constructed',len(records),'sizes',[len(t['cocycle']) for t in records],flush=True)
 payload=k.text({'passed':True,'characters':out,'conjugate_cubic_computed':False,'scope':'Both four-dimensional charged-character dual bases are now actual closed Cech-Koszul cocycles. Missing beta0/beta1 4x4 slices require their exterior-cube product/adjunction trace, not additional assumed generic ranks.'})
 path=k.P/'charged-dual-bases.json'
 if '--create' in sys.argv:
  with path.open('x',newline='\n') as f:f.write(payload)
 else:assert path.is_file() and path.read_text()==payload
if __name__=='__main__':main()
