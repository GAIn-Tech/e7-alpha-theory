"""Exterior-cube q=1 diagonal calculation over QQ (exploratory)."""
import explore_ring as r
from itertools import combinations_with_replacement
from functools import lru_cache
s=r.s;F=r.F
terms=[('A',i,-1,(0,0),0) for i in range(2)]+[('B',i,0,(int(i<4),int(i>=4)),r.w[i]) for i in range(8)]+[('C',i,1,tuple(r.deg[i]),0) for i in range(3)]
triples=[t for t in combinations_with_replacement(range(13),3) if all(t.count(i)<=1 for i in range(2,10))]
def canon(t):
 if any(t.count(i)>1 for i in range(2,10)):return None,0
 sign=1
 for i in range(len(t)):
  for j in range(i+1,len(t)):
   if t[i]>t[j]:sign*= -1 if (terms[t[i]][2]*terms[t[j]][2])%2==0 else 1
 return tuple(sorted(t)),sign
arrows=[]
for i in range(8):arrows.append((int(i>=4),i+2,{tuple(int(j==i) for j in range(8)):F(1)}))
for a in range(3):
 for i in range(8):
  po={e:F(str(c)) for e,c in r.f[a].diff(r.z[i]).terms() if c}
  if po:arrows.append((i+2,a+10,po))
@lru_cache(None)
def diff(t):
 out=[]
 for k,i in enumerate(t):
  sg=1 if sum(terms[t[j]][2] for j in range(k))%2==0 else -1
  for aa,bb,po in arrows:
   if aa!=i:continue
   nt,ss=canon(t[:k]+(bb,)+t[k+1:])
   if ss:out.append((nt,sg*ss,po))
 return out
@lru_cache(None)
def info(t):return sum(terms[i][2] for i in t),tuple(sum(terms[i][3][a] for i in t) for a in range(2)),sum(terms[i][4] for i in t)%3
@lru_cache(None)
def basis(p,ch=0):
 out=[]
 for t in triples:
  pp,dd,weight=info(t)
  if pp!=p or not ((dd[0]>0 and dd[1]==0) or (dd[1]>0 and dd[0]==0)):continue
  side=int(dd[1]>0);d=dd[side]
  for e in r.comps(d-1,4):
   if e[3]>=3:continue
   es=e+(-1,)*4 if side==0 else (-1,)*4+e
   if (sum(a*b for a,b in zip(es,r.w))-weight)%3==ch:out.append((t,side,e))
 return out
@lru_cache(None)
def red(e):
 if e[3]<3:return {e:F(1)}
 out={}
 for i in range(3):
  ee=list(e);ee[3]-=3;ee[i]+=3
  for v,c in red(tuple(ee)).items():r.addto(out,v,-c)
 return out
def matrix(p,ch=0):
 bs=basis(p,ch);bt=basis(p+1,ch);idx={v:i for i,v in enumerate(bt)};cols=[]
 for t,side,e in bs:
  out={}
  for nt,sg,po in diff(t):
   pp,dd,weight=info(nt)
   if dd[1-side]:continue
   for mon,c in po.items():
    if any(mon[4*(1-side):4*(1-side)+4]):continue
    ee=tuple(a+b for a,b in zip(e,mon[4*side:4*side+4]))
    for ex,cc in red(ee).items():r.addto(out,idx[nt,side,ex],sg*c*cc)
  cols.append(out)
 return len(bt),cols
def rank(cols):
 piv={}
 for v in cols:
  v=v.copy()
  while v:
   i=max(v);x=v[i]
   if i not in piv:piv[i]={j:c/x for j,c in v.items()};break
   for j,c in piv[i].items():r.addto(v,j,-x*c)
 return len(piv)
def main():
 dims={p:len(basis(p)) for p in range(-3,4)};ms={p:matrix(p) for p in range(-3,3)};ranks={p:rank(cs) for p,(n,cs) in ms.items()}
 for p in range(-3,2):
  nxt=ms[p+1][1]
  for col in ms[p][1]:
   out={}
   for i,x in col.items():
    for j,y in nxt[i].items():r.addto(out,j,x*y)
   assert not out
 e2={p:dims[p]-ranks.get(p,0)-ranks.get(p-1,0) for p in dims}
 out={'dimensions':dims,'ranks':ranks,'E2':e2,'square_zero':True,'total3_other_q1_slot':e2[2]}
 print(out,flush=True);(r.P/'exterior-diagonal.json').write_text(r.json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
