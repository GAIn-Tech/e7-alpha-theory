"""Exact chain computation. Exploratory until immutable verification release exists."""
from pathlib import Path
import sys,json,hashlib
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'tian-yau-neutral-d2-gate'))
import total_cech as c
import partial_chains as a
s=a.s
from functools import lru_cache
from itertools import combinations

def inc(v):
 out=v.copy();term=v
 for _ in range(4):
  term=c.scale(c.hc(c.kap(term)),-1);out=c.add(out,term)
 assert not term
 return out

def proj(v):
 out={};term=v
 for _ in range(5):
  out=c.add(out,c.pc(term));term=c.scale(c.kap(c.hc(term)),-1)
 assert not term
 return out

def hom(v):
 out={};term=v
 for _ in range(5):
  out=c.add(out,c.hc(term));term=c.scale(c.kap(c.hc(term)),-1)
 assert not term
 return out

def weight(i):
 t=c.terms[i];return a.w[t[1]] if t[0]=='B' else 0
@lru_cache(None)
def basis(pair,q,k):
 i,j=pair;dd=tuple(y-x for x,y in zip(c.terms[i][3],c.terms[j][3]));out=[]
 for I in combinations(range(3),k):
  aq,es=a.ambient(*(dd[b]-sum(a.deg[h][b] for h in I) for b in range(2)))
  if aq!=q:continue
  for e in es:
   if (sum(x*y for x,y in zip(e,a.w))+weight(i)-weight(j))%3==0:out.append((pair,I,e))
 return out

def coords(v,bs):
 index={b:i for i,b in enumerate(bs)};out=s.zeros(len(bs),1)
 for (pair,I,e,X,Y),val in v.items():
  canonical=all(U==((0,) if all(t>=0 for t in E) else (0,1,2,3)) for U,E in [(X,e[:4]),(Y,e[4:])])
  if canonical and (pair,I,e) in index:out[index[pair,I,e]]+=s.Rational(val.numerator,val.denominator)
 return out
@lru_cache(None)
def kmat(pair,q,k):
 bs=basis(pair,q,k);bt=basis(pair,q,k-1) if k else [];idx={b:i for i,b in enumerate(bt)};M=s.zeros(len(bt),len(bs))
 for j,(_,I,e) in enumerate(bs):
  for t,h in enumerate(I):
   for mon,coef in a.f[h]:
    key=(pair,I[:t]+I[t+1:],tuple(x+y for x,y in zip(e,mon)))
    if key in idx:M[idx[key],j]+=(-1)**t*coef
 return M
@lru_cache(None)
def cohom(pair,q,k):
 D=kmat(pair,q,k);B=kmat(pair,q,k+1) if k<3 else s.zeros(D.cols,0)
 R,S,n=a.quotient(D,B)
 return R,S,n,B
@lru_cache(None)
def classes(p,vq):
 out=[]
 for i in range(len(c.terms)):
  for j in range(len(c.terms)):
   if c.terms[j][2]-c.terms[i][2]!=p:continue
   for q in (0,3,6):
    k=q-vq
    if not 0<=k<=3:continue
    R,_,_,_=cohom((i,j),q,k)
    for col in range(R.cols):
     v=inc(c.lift(basis((i,j),q,k),R[:,col]));assert not c.dv(v)
     out.append(((i,j),q,k,col,v))
 return out

def hcoords(v,p,vq):
 pv=proj(v);out=[]
 for i,j in [(i,j) for i in range(len(c.terms)) for j in range(len(c.terms)) if c.terms[j][2]-c.terms[i][2]==p]:
  for q in (0,3,6):
   k=q-vq
   if not 0<=k<=3:continue
   R,S,n,B=cohom((i,j),q,k)
   if not S.rows:continue
   vec=coords(pv,basis((i,j),q,k));sol=a.solve(S,vec)
   out.extend(list(sol[n:,:]))
 return s.Matrix(len(out),1,out)

def primitive(v):
 assert not c.dv(v)
 pv=proj(v);u={}
 pairs=set(key[0] for key in pv)
 for pair in sorted(pairs):
  for q in (0,3,6):
   for k in range(3):
    bs=basis(pair,q,k);b=coords(pv,bs)
    if any(b):
     x=a.solve(kmat(pair,q,k+1),b);u=c.add(u,c.lift(basis(pair,q,k+1),x))
 u=c.add(hom(v),inc(u))
 assert c.dv(u)==v,('primitive residual',len(c.add(c.dv(u),c.scale(v,-1))))
 return u

def combine(cs,x):
 out={}
 for j,rec in enumerate(cs):out=c.add(out,c.scale(rec[-1],a.Fraction(str(x[j])) if hasattr(a,'Fraction') else c.F(str(x[j]))))
 return out

def drow(p,q):
 cs=classes(p,q);cols=[hcoords(c.d1(v),p+1,q) for *_,v in cs]
 return s.Matrix.hstack(*cols) if cols else s.zeros(len(classes(p+1,q)),0)

def main():
 print('building edge rows',flush=True)
 A=drow(-2,3);B=drow(1,0)
 src=A.nullspace();target,span,nb=a.quotient(s.zeros(0,B.rows),B)
 print('edge dimensions',A.shape,len(src),B.shape,target.cols,flush=True)
 records=[];endcols=[]
 for j,x in enumerate(src):
  v0=combine(classes(-2,3),x);vs=[v0]
  print('source',j,'terms',len(v0),flush=True)
  for step in range(1,4):
   rhs=c.d1(vs[-1])
   if step>=2:rhs=c.add(rhs,c.d2cor(vs[-2]))
   try:u=primitive(c.scale(rhs,-1))
   except Exception as exc:
    print('primitive blocked',j,step,repr(exc),flush=True);raise
   vs.append(u);print('step',step,'terms',len(u),flush=True)
  end=c.add(c.d1(vs[3]),c.d2cor(vs[2]));assert not c.dv(end)
  z=hcoords(end,2,0);co=a.solve(span,z)[nb:,:];endcols.append(co)
  for v in vs:assert not c.total(c.total(v))
  records.append({'column':j,'lifts':[c.pack(v) for v in vs],'endpoint':c.pack(end)})
 M=s.Matrix.hstack(*endcols)
 data={'matrix':a.sparse(M),'rank':M.rank(),'det':str(M.det()),'records':records,'source_dimension':len(src),'target_dimension':target.cols,'status':'exploratory; representative controls and page survival not complete'}
 (P/'computed-chains.json').write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
 print({k:v for k,v in data.items() if k!='records'},flush=True)
if __name__=='__main__':main()

