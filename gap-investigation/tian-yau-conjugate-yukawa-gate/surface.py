"""Exact adjunction trace on each cubic surface; exploratory calculation."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,permutations
import json,sys
import sympy as s
P=Path(__file__).resolve().parent
FROZEN=P/'frozen/tian-yau-colored-yukawa-gate'
x=s.symbols('z0:4');f=sum(z**3 for z in x)/3

def signperm(t):return (-1)**sum(t[i]>t[j] for i in range(len(t)) for j in range(i+1,len(t)))
def accum(v,k,c):
 if c:v[k]=v.get(k,F(0))+c
 if k in v and not v[k]:del v[k]
def add(*vs):
 out={}
 for v in vs:
  for k,c in v.items():accum(out,k,c)
 return out

def form(rows,side):
 out={}
 for pair,I,e,X,Y,v in rows:
  if I or not 2+4*side<=pair[0]<6+4*side:continue
  U=(X,Y)[side];V=(X,Y)[1-side]
  if V!=[0]:continue
  assert len(U)==2 and not any(e[4*(1-side):4*(1-side)+4])
  accum(out,(pair[0]-2-4*side,tuple(e[side*4:side*4+4]),tuple(U)),F(v))
 return out

def hyperplane():
 out={}
 for i,j in combinations(range(4),2):
  for k,cf in [(i,-1),(j,1)]:
   e=tuple(-int(a==k) for a in range(4));out[k,e,(i,j)]=F(cf)
 return out

def topform(a,b):
 """AW wedge, then alpha wedge beta wedge df = h Omega, modulo f.
 Omega=sum_i (-1)^i z_i dz_0...hat(dz_i)...dz_3.
 Anchor=min chart intersection, so all Laurent denominators are allowed.
 """
 out={}
 for (i,e,U),aa in a.items():
  for (j,ee,V),bb in b.items():
   if U[-1]!=V[0] or i==j:continue
   W=U+V[1:];anchor=W[0]
   for k in range(4):
    if len({anchor,i,j,k})!=4:continue
    ex=tuple(e[n]+ee[n]+2*int(n==k)-int(n==anchor) for n in range(4))
    sg=signperm((anchor,i,j,k))
    accum(out,(ex,W),sg*aa*bb)
 return out

def delta(v):
 out={}
 for (e,U),cf in v.items():
  for j in range(4):
   if j in U:continue
   W=tuple(sorted(U+(j,)));accum(out,(e,W),(-1)**W.index(j)*cf)
 return out

def divide_f(v):
 out={}
 for U in sorted(set(k[1] for k in v)):
  rows=[(e,c) for (e,W),c in v.items() if W==U]
  mins=tuple(min(e[j] for e,c in rows) for j in range(4))
  expr=sum(s.Rational(c.numerator,c.denominator)*s.prod(x[j]**(e[j]-mins[j]) for j in range(4)) for e,c in rows)
  q,r=s.div(expr,f,*x);assert r==0,('not divisible',U,r)
  for e,c in s.Poly(q,*x).terms():
   if c:accum(out,(tuple(e[j]+mins[j] for j in range(4)),U),F(str(c)))
 return out

def trace(a,b):
 h=topform(a,b);d=delta(h);pr=divide_f(d)
 return pr.get(((-1,)*4,(0,1,2,3)),F(0)),h,pr

if __name__=='__main__':
 d=json.loads((FROZEN/'charged-dual-bases.json').read_text())
 aa={ch:[form(r['cocycle'],int(i>=2)) for i,r in enumerate(d['characters'][str(ch)]['records'])] for ch in [1,2]}
 H=hyperplane();print('HH',trace(H,H)[0])
 for side in [0,1]:
  print('side',side)
  for a in aa[1][2*side:2*side+2]:print([str(trace(a,b)[0]) for b in aa[2][2*side:2*side+2]],'H',trace(a,H)[0])
