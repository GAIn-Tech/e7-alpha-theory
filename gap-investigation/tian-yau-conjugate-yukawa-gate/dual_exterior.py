"""Derived exterior algebra of the dual curved Euler/normal complex, over QQ.
Keys (tuple of dual indices, Koszul subset, Laurent exponents, Xchart,Ychart).
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement
import sys
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P/'frozen/tian-yau-colored-yukawa-gate'))
import calculate as inherited
c,u=inherited.c,inherited.u
parity=lambda n:1 if n%2==0 else -1
pd=lambda i:-c.terms[i][2]

def accum(out,k,v):
 if v:out[k]=out.get(k,F(0))+v
 if k in out and not out[k]:del out[k]
def add(*vs):
 out={}
 for v in vs:
  for k,x in v.items():accum(out,k,x)
 return out
def scale(v,x):return {k:x*y for k,y in v.items() if x*y}
def canon(t):
 if any(t.count(i)>1 for i in range(2,10)):return (),0
 sg=1
 for a in range(len(t)):
  for b in range(a+1,len(t)):
   if t[a]>t[b]:sg*=-parity(pd(t[a])*pd(t[b]))
 return tuple(sorted(t)),sg

def degree(key):
 t,I,e,X,Y=key
 return sum(pd(i) for i in t)-len(I)+len(X)+len(Y)-2

def from_dual(v):
 out={}
 for (pair,I,e,X,Y),cf in v.items():
  assert pair[1]==13;out[(pair[0],),I,e,X,Y]=cf
 return out

def D(v,wrong=False):
 out={}
 for (t,I,e,X,Y),cf in v.items():
  p=sum(pd(i) for i in t)
  for axis,U in enumerate([X,Y]):
   for j in range(4):
    if j in U:continue
    V=tuple(sorted(U+(j,)))
    sg=parity(p+len(I)+V.index(j)+(len(X)-1 if axis else 0))
    accum(out,(t,I,e,V if axis==0 else X,V if axis else Y),sg*cf)
  for j,h in enumerate(I):
   for mon,co in c.fs[h]:accum(out,(t,I[:j]+I[j+1:],tuple(a+b for a,b in zip(e,mon)),X,Y),parity(j)*co*cf)
  for pos,i in enumerate(t):
   sg=parity(len(I)+sum(pd(vv) for vv in t[:pos]))
   for aa,bb,poly in c.arrows:
    if bb!=i:continue
    nt,ss=canon(t[:pos]+(aa,)+t[pos+1:])
    for mon,co in poly:
     if ss:accum(out,(nt,I,tuple(a+b for a,b in zip(e,mon)),X,Y),-parity(pd(i))*sg*ss*co*cf)
   for aa,bb,h,co in c.Hs:
    if bb!=i or h in I:continue
    nt,ss=canon(t[:pos]+(aa,)+t[pos+1:]);J=tuple(sorted(I+(h,)))
    if ss:accum(out,(nt,J,e,X,Y),(-1 if wrong else 1)*parity(sum(j<h for j in I))*ss*co*cf)
 return out

def wedge(v,w,wrong=False):
 out={}
 for (t,I,e,X,Y),a in v.items():
  p=sum(pd(i) for i in t);q=len(X)+len(Y)-2
  for (tt,J,ee,U,V),b in w.items():
   if set(I)&set(J) or X[-1]!=U[0] or Y[-1]!=V[0]:continue
   nt,sg=canon(t+tt)
   if not sg:continue
   pp=sum(pd(i) for i in tt)
   exponent=p*len(J)+q*(pp-len(J))+(len(Y)-1)*(len(U)-1)+sum(i>j for i in I for j in J)
   accum(out,(nt,tuple(sorted(I+J)),tuple(a+b for a,b in zip(e,ee)),X+U[1:],Y+V[1:]),sg*(1 if wrong else parity(exponent))*a*b)
 return out

def validate(v,deg,ch):
 w=inherited.r.w
 for key,cf in v.items():
  t,I,e,X,Y=key
  assert degree(key)==deg and canon(t)==(t,1)
  assert I==tuple(sorted(set(I)))
  assert tuple(sum(e[4*b:4*b+4]) for b in range(2))==tuple(-sum(c.terms[i][3][b] for i in t)-sum(inherited.r.deg[h][b] for h in I) for b in range(2))
  assert (sum(a*b for a,b in zip(e,w))+sum(inherited.m.weight(i) for i in t))%3==ch
  assert all(U==tuple(sorted(set(U))) and all(j in U for j,z in enumerate(E) if z<0) for E,U in [(e[:4],X),(e[4:],Y)])

def beta_primitive(side):
 out={}
 for i in range(4):
  for j in range(4):
   k=(i,j)[side]+4*side;e=tuple(-int(n==k) for n in range(8))
   out[(2+k,),(),e,(i,),(j,)]=F(-1)
 return out

def pack(v):return [[list(t),list(I),list(e),list(X),list(Y),str(c)] for (t,I,e,X,Y),c in sorted(v.items())]

def raw_b_projection(v):return {k:c for k,c in v.items() if not k[1] and all(2<=i<10 for i in k[0])}
