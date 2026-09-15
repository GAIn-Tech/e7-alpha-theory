"""Exact curved tangent-module and tensor-cover Alexander-Whitney action."""
import sys,json,hashlib
from pathlib import Path
from functools import lru_cache
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'tian-yau-neutral-d4-gate'))
import compute as m
c,a,s=m.c,m.a,m.s
N=len(c.terms)
c.terms.append(('O',0,0,(0,0)))

def unpack(rows):return {(tuple(pair),tuple(I),tuple(e),tuple(X),tuple(Y)):c.F(v) for pair,I,e,X,Y,v in rows}
def text(d):return json.dumps(d,sort_keys=True,indent=2)+'\n'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def parity(n):return 1 if n%2==0 else -1

@lru_cache(None)
def classes(p,vq):
 out=[]
 for j in range(N):
  if c.terms[j][2]!=p:continue
  for q in (0,3,6):
   k=q-vq
   if not 0<=k<=3:continue
   R,_,_,_=m.cohom((N,j),q,k)
   for col in range(R.cols):
    v=m.inc(c.lift(m.basis((N,j),q,k),R[:,col]));assert not c.dv(v)
    out.append(((N,j),q,k,col,v))
 return out

def hcvec(v,p,vq):
 pv=m.proj(v);out=[]
 for j in range(N):
  if c.terms[j][2]!=p:continue
  for q in (0,3,6):
   k=q-vq
   if not 0<=k<=3:continue
   R,S,n,B=m.cohom((N,j),q,k)
   if not S.rows:continue
   sol=a.solve(S,m.coords(pv,m.basis((N,j),q,k)))
   out.extend(list(sol[n:,:]))
 return s.Matrix(len(out),1,out)

def drow(p,q):
 cols=[hcvec(c.d1(v),p+1,q) for *_,v in classes(p,q)]
 return s.Matrix.hstack(*cols) if cols else s.zeros(len(classes(p+1,q)),0)

def action(alpha,v,wrong=False):
 """Koszul-End composition times tensor-cover AW product, without projection."""
 out={};by_source={}
 for key,coef in alpha.items():by_source.setdefault(key[0][0],[]).append((key,coef))
 for (pair,J,f,U,V),b in v.items():
  src,j=pair;pb=c.terms[j][2]-c.terms[src][2]
  for ((i,t),I,e,X,Y),aa in by_source.get(j,[]):
   if set(I)&set(J) or X[-1]!=U[0] or Y[-1]!=V[0]:continue
   p=c.terms[t][2]-c.terms[i][2];q=len(X)+len(Y)-2
   exponent=p*len(J)+q*(pb-len(J))+(len(Y)-1)*(len(U)-1)+sum(x>y for x in I for y in J)
   sign=1 if wrong else parity(exponent)
   c.accum(out,((src,t),tuple(sorted(I+J)),tuple(x+y for x,y in zip(e,f)),X+U[1:],Y+V[1:]),sign*aa*b)
 return out

def validate(v,degree):
 for key in v:
  pair,I,e,X,Y=key;i,j=pair
  assert I==tuple(sorted(set(I))) and set(I)<=set(range(3))
  assert (sum(e[:4]),sum(e[4:]))==tuple(c.terms[j][3][b]-c.terms[i][3][b]-sum(a.deg[h][b] for h in I) for b in range(2))
  for E,U in [(e[:4],X),(e[4:],Y)]:
   assert U and U==tuple(sorted(set(U))) and all(n in U for n,t in enumerate(E) if t<0)
  assert (sum(x*y for x,y in zip(e,a.w))+m.weight(i)-m.weight(j))%3==0
  p,q,k=c.grade(key);assert p+q-k==degree

def component(v,p):return {key:x for key,x in v.items() if c.grade(key)[0]==p}

def main():
 data=json.loads((P.parent/'tian-yau-neutral-d4-gate/d4-chains.json').read_text())
 assert sha(P.parent/'tian-yau-neutral-d4-gate/d4-chains.json')=='ff97c93f893d2164011e0381613a29a83013ea74d022b84bba9b15ca6599ad34'
 alphas=[unpack(r['surviving_total_cocycle']) for r in data['records']]
 for v in alphas:validate(v,1);assert not c.total(v)
 print('survivors read and closed',flush=True)
 rows={}
 for q in range(4):
  dims=[len(classes(p,q)) for p in [-1,0,1]]
  A=drow(-1,q);B=drow(0,q);assert not any(B*A)
  rows[str(q)]={'dimensions':dims,'A':a.sparse(A),'B':a.sparse(B),'ranks':[A.rank(),B.rank()],'E2':[dims[0]-A.rank(),dims[1]-A.rank()-B.rank(),dims[2]-B.rank()]}
  print('row',q,rows[str(q)]['dimensions'],rows[str(q)]['E2'],flush=True)
 J=drow(0,0);R,span,nb=a.quotient(s.zeros(0,J.rows),J)
 charged=[m.combine(classes(1,0),R[:,j]) for j in range(R.cols)]
 assert len(charged)==9
 for v in charged:validate(v,1);assert not c.total(v)
 # Construct the actual H2 basis, first four terminal C H1 quotient modes.
 J1=drow(0,1);R1,S1,n1=a.quotient(s.zeros(0,J1.rows),J1)
 h2low=[m.combine(classes(1,1),R1[:,j]) for j in range(R1.cols)]
 for v in h2low:validate(v,2);assert not c.total(v)
 h2high=[];highrecords=[]
 for *_,v0 in classes(-1,3):
  v1=m.primitive(c.scale(c.d1(v0),-1))
  v2=m.primitive(c.scale(c.add(c.d1(v1),c.d2cor(v0)),-1))
  full=c.add(v0,v1,v2);validate(full,2);assert not c.total(full)
  h2high.append(full);highrecords.append({'source':c.pack(v0),'primitive1':c.pack(v1),'primitive2':c.pack(v2),'cocycle':c.pack(full)})
 print('H2 basis',len(h2low),len(h2high),flush=True)
 assert len(h2low)+len(h2high)==6
 def reduce2(v):
  assert not c.total(v);w=v;pr={};coords=[]
  leading=hcvec(component(w,-1),-1,3)
  for i,h in enumerate(h2high):w=c.add(w,c.scale(h,-c.F(str(leading[i]))))
  # eliminate remaining p=-1 and p=0 vertical boundaries by genuine primitives
  for p in [-1,0]:
   z=component(w,p)
   if z:
    u=m.primitive(z);w=c.add(w,c.scale(c.total(u),-1));pr=c.add(pr,u)
   assert not component(w,p)
  z=hcvec(w,1,1);sol=a.solve(S1,z);low=sol[n1:,:]
  representative=c.add(*[c.scale(h,c.F(str(low[i]))) for i,h in enumerate(h2low)])
  # Lift the terminal C H1 d1-boundary; complete its vertical remainder.
  boundarycoord=a.solve(J1,z-R1*low)
  b=m.combine(classes(0,1),boundarycoord)
  rem=c.add(w,c.scale(representative,-1),c.scale(c.total(b),-1))
  u=m.primitive(rem);pr=c.add(pr,b,u)
  rep=c.add(representative,*[c.scale(h,c.F(str(leading[i]))) for i,h in enumerate(h2high)])
  assert v==c.add(rep,c.total(pr))
  return list(low)+list(leading),pr
 records=[];tensor=[];control={'leibniz':0,'wrong_sign_detected':0,'charged_boundary':0,'neutral_boundary':0}
 for n,alpha in enumerate(alphas):
  slab=[]
  for j,v in enumerate(charged):
   image=action(alpha,v);validate(image,2)
   assert c.total(image)==c.add(action(c.total(alpha),v),c.scale(action(alpha,c.total(v)),-1))
   control['leibniz']+=1
   co,pr=reduce2(image);slab.append([str(x) for x in co])
   records.append({'neutral':n,'charged':j,'image':c.pack(image),'coordinates':[str(x) for x in co],'boundary_primitive':c.pack(pr)})
   print('product',n,j,'terms',len(image),'coordinates',co,'primitive',len(pr),flush=True)
  tensor.append(slab)
 out={'passed':True,'source_hashes':{str(p.relative_to(P.parent)).replace('\\','/'):sha(p) for p in [Path(__file__),P.parent/'tian-yau-neutral-d4-gate/d4-chains.json',P.parent/'tian-yau-neutral-d4-gate/compute.py',P.parent/'tian-yau-neutral-d2-gate/total_cech.py']},'rows':rows,'charged_basis':[c.pack(v) for v in charged],'charged_quotient_representatives':a.sparse(R),'charged_boundary_map':a.sparse(J),'H2_low':[c.pack(v) for v in h2low],'H2_high':highrecords,'H2_low_quotient_representatives':a.sparse(R1),'tensor_coordinates':tensor,'products':records,'controls':control,'boundary':'Exact module action and H2 coordinates; dual basis pairing abstract, geometric dual cocycles and Higgs convention checks pending.'}
 f=P/'module-action.json';payload=text(out)
 if '--create' in sys.argv:
  with f.open('x',newline='\n') as h:h.write(payload)
 else:assert f.is_file() and f.read_text()==payload
 print('module action saved/replayed',flush=True)
if __name__=='__main__':main()
