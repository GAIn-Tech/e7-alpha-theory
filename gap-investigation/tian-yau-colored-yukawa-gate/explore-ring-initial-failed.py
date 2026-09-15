"""Exploratory exact multigraded Cayley-Jacobian quotient; NOT yet a trace certificate."""
import sys,json,time
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from functools import lru_cache
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parent
G=json.loads((P.parent/'tian-yau-bundle-coupling-gate/geometry.json').read_text())
import sympy as s
z=s.symbols(' '.join(G['variables']));w=G['weights'];deg=G['degrees']
f=[s.Poly(s.sympify(v,locals=dict(zip(G['variables'],z))),*z) for v in G['polynomials']]
@lru_cache(None)
def comps(d,n):
 if n==1:return [(d,)] if d>=0 else []
 return [(a,)+b for a in range(d+1) for b in comps(d-a,n-1)] if d>=0 else []
def basis(k,dx=0,dy=0,ch=0):
 out=[]
 for ps in reversed(comps(k,3)):
  a=dx+sum(ps[i]*deg[i][0] for i in range(3));b=dy+sum(ps[i]*deg[i][1] for i in range(3))
  for e in comps(a,4):
   for h in comps(b,4):
    if sum(x*y for x,y in zip(e+h,w))%3==ch:out.append(ps+e+h)
 return out
def poly(p,ps):return {ps+e:F(str(c)) for e,c in p.terms()}
zero=(0,)*3
relations=[(poly(f[i],zero),0,*deg[i],0,'f'+str(i)) for i in range(3)]
for j in range(8):
 v={}
 for i in range(3):
  ps=tuple(int(h==i) for h in range(3))
  v.update(poly(f[i].diff(z[j]),ps))
 relations.append((v,1,-int(j<4),-int(j>=4),-w[j]%3,'J'+str(j)))
def addto(v,i,x):
 if x:v[i]=v.get(i,F(0))+x
 if not v.get(i):v.pop(i,None)
class Quotient:
 def __init__(self,k,ch):
  self.bs=basis(k,ch=ch);self.index={b:i for i,b in enumerate(self.bs)};self.piv={};self.count=0
  print('space',k,ch,len(self.bs),flush=True)
  for pol,pk,dx,dy,weight,name in relations:
   for b in basis(k-pk,-dx,-dy,(ch-weight)%3):
    v={self.index[tuple(x+y for x,y in zip(b,e))]:c for e,c in pol.items()}
    self.count+=1;v=self.reduce(v)
    if v:
     i=max(v);a=v[i];self.piv[i]={j:x/a for j,x in v.items()}
   print('relation',name,'rank',len(self.piv),flush=True)
  self.free=[i for i in range(len(self.bs)) if i not in self.piv]
  print('quotient',k,ch,len(self.free),flush=True)
 def reduce(self,v):
  v=v.copy();out={}
  while v:
   i=max(v);a=v[i]
   if i not in self.piv:out[i]=v.pop(i);continue
   for j,x in self.piv[i].items():addto(v,j,-a*x)
  return out
 def mon(self,b):return self.reduce({self.index[b]:F(1)})
if __name__=='__main__':
 qs={ch:Quotient(1,ch) for ch in [0,1,2]}
 top=Quotient(3,0)
 result={'bases':{str(ch):[q.bs[i] for i in q.free] for ch,q in qs.items()},'top_free':[top.bs[i] for i in top.free],'top_dimension':len(top.free),'matrices':[]}
 for c in result['bases']['0'][:2]:
  mat=[]
  for u in result['bases']['2']:
   row=[]
   for v in result['bases']['1']:
    b=tuple(x+y+zz for x,y,zz in zip(u,v,c));a=top.mon(b)
    row.append({str(top.free.index(i)):str(x) for i,x in a.items()})
   mat.append(row)
  result['matrices'].append(mat)
 (P/'explore-ring.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result),flush=True)
