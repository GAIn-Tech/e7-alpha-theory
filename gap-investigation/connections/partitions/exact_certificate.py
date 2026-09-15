"""Finite exact checks, not a formal kernel proof or physical derivation."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product, combinations
from math import factorial, prod
import json, hashlib, sys
ROOT=Path(__file__).resolve().parent

def partitions(n,cap=None):
 if n==0: yield (); return
 for k in range(min(n,cap or n),0,-1):
  for tail in partitions(n-k,k): yield (k,)+tail

def conjugate(l): return tuple(sum(x>=j for x in l) for j in range(1,(l[0] if l else 0)+1))
def chirality(l):
 n=sum(l); c=conjugate(l)
 f=factorial(n)//prod(l[i]-j+c[j]-i-1 for i in range(len(l)) for j in range(l[i]))
 if n<2: return f,0,False
 chi=F(f*sum(j-i for i in range(len(l)) for j in range(l[i])),n*(n-1)//2)
 g=(f-chi)/2
 assert chi.denominator==g.denominator==1
 return f,int(chi),bool(g%2)
def det(a):
 a=[[F(x) for x in row] for row in a]; d=F(1)
 for i in range(len(a)):
  j=next(j for j in range(i,len(a)) if a[j][i])
  if j!=i: a[i],a[j]=a[j],a[i]; d=-d
  pivot=a[i][i]; d*=pivot
  for j in range(i+1,len(a)):
   ratio=a[j][i]/pivot
   for k in range(i,len(a)): a[j][k]-=ratio*a[i][k]
 return d

def payload():
 N=5000; p=[1]+[0]*N
 for k in range(1,N+1):
  for n in range(k,N+1): p[n]+=p[n-k]
 # Independent Euler pentagonal recurrence
 e=[1]+[0]*N
 for n in range(1,N+1):
  k=1
  while k*(3*k-1)//2<=n:
   for t in (k*(3*k-1)//2,k*(3*k+1)//2):
    if t<=n: e[n]+=(-1 if k%2==0 else 1)*e[n-t]
   k+=1
 assert p==e
 congr=[]
 for prime,residue in ((5,4),(7,5),(11,6)):
  indices=list(range(residue,N+1,prime)); failures=[n for n in indices if p[n]%prime]
  assert not failures
  congr.append({'prime':prime,'residue':residue,'tested':len(indices),'failures':failures})
 # Finite witnesses reject every simple p(ell*n+b)=0 mod ell for ell=13,137.
 no_simple={}
 for ell in (13,137):
  witnesses={str(b):next((n for n in range(b,N+1,ell) if p[n]%ell),None) for b in range(ell)}
  assert None not in witnesses.values(); no_simple[str(ell)]=witnesses
 roots=[]
 for i,j in combinations(range(8),2):
  for a,b in product((-2,2),repeat=2):
   v=[0]*8;v[i]=a;v[j]=b;roots.append(tuple(v))
 roots += [v for v in product((-1,1),repeat=8) if sum(x<0 for x in v)%2==0]
 e7=[v for v in roots if v[6]+v[7]==0]
 assert len(roots)==240 and len(e7)==126
 # a_i represented in doubled orthonormal coordinates.
 basis=[(1,-1,-1,-1,-1,-1,-1,1),(2,2,0,0,0,0,0,0),(-2,2,0,0,0,0,0,0)]
 for i in range(1,5):
  v=[0]*8;v[i]=-2;v[i+1]=2;basis.append(tuple(v))
 gram=[[sum(F(x*y,4) for x,y in zip(a,b)) for b in basis] for a in basis]
 determinant=det(gram); assert determinant==2
 # Exhaust all E8 lattice points of norm <=4, perpendicular to e7+e8.
 theta={0:0,2:0,4:0}
 for coords in (range(-4,5,2),range(-3,4,2)):
  for v in product(coords,repeat=8):
   if v[6]+v[7] or sum(v)%4: continue
   norm=F(sum(x*x for x in v),4)
   if norm<=4:
    assert norm in theta; theta[int(norm)]+=1
 assert theta=={0:1,2:126,4:756}
 weight_sector=[v for v in roots if v[6]+v[7]==2]
 assert len(weight_sector)==56
 osc=[1,0,0]
 for color in range(7):
  for k in range(1,3):
   for n in range(k,3): osc[n]+=osc[n-k]
 assert osc==[1,7,35]
 # Projection r-alpha/2 of E8 roots with (r,alpha)=1; alpha=e7+e8.
 projected_norms={sum((F(v[i],2)-(F(1,2) if i>=6 else 0))**2 for i in range(8)) for v in weight_sector}
 assert projected_norms=={F(3,2)}
 character=[theta[0],theta[2]+osc[1],theta[4]+theta[2]*osc[1]+osc[2]]
 assert character==[1,133,1673]
 chiral=[]
 for n in range(1,13):
  ls=list(partitions(n)); sc=sum(conjugate(l)==l for l in ls)
  odd_distinct=sum(len(set(l))==len(l) and all(x%2 for x in l) for l in ls)
  assert len(ls)==p[n] and sc==odd_distinct
  chiral.append({'n':n,'p':p[n],'self_conjugate':sc,'chiral':sum(chirality(l)[2] for l in ls)})
 assert [r['chiral'] for r in chiral]==[0,1,2,3,5,4,8,12,20,8,16,24]
 ded=[]
 for n in range(5):
  size=1<<n; funcs=[]
  for f in range(1<<size):
   if all(not((f>>x)&1) or ((f>>y)&1) for x in range(size) for y in range(size) if x&y==x): funcs.append(f)
  selfdual=sum(all(((f>>x)&1)==1-((f>>(size-1-x))&1) for x in range(size)) for f in funcs)
  assert (len(funcs)-selfdual)%2==0
  ded.append({'n':n,'dedekind':len(funcs),'selfdual':selfdual})
 assert [x['dedekind'] for x in ded]==[2,3,6,20,168]
 # Circle convention alpha'=1, p_L=n/R+wR, p_R=n/R-wR.
 circles=[]
 for R in (F(1),F(2),F(3,2)):
  for n,w in product(range(-3,4),repeat=2):
   L=F(n,R)+w*R; right=F(n,R)-w*R
   assert (L*L-right*right)/4==n*w
  circles.append({'R':str(R),'momentum_n1_w0_mass_squared':str(1/(R*R)),'level_matching_integral':True})
 return {'passed':True,'claim_boundary':'Exact finite enumeration and rational algebra only; no Lean proof, no all-n Ramanujan proof, no selected spacetime dimension, physical prime mass scale, or alpha.','partition_limit':N,'crosscheck':'dynamic product equals pentagonal recurrence at every coefficient','congruences':congr,'no_simple_prime_congruence_witnesses':no_simple,'e7':{'roots':len(e7),'rank':len(basis),'gram':[[str(x) for x in row] for row in gram],'determinant':str(determinant),'theta':theta,'eta_inverse_7_initial':osc,'vacuum_character_after_q_shift':character,'nontrivial_coset_minimal_weights':len(weight_sector),'coset_h':'3/4','central_charge_level_1':str(F(133,1+18))},'chiral_partitions':chiral,'selfconjugate_chiral_counterexample':{'partition':[2,1],'dimension_trace_chiral':chirality((2,1))},'dedekind':ded,'circle_family':circles,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
 result=payload(); target=ROOT/'certificate.json'
 if '--verify' in sys.argv:
  saved=json.loads(target.read_text()); assert saved==json.loads(json.dumps(result)); print('PASS: saved exact certificate matches independent recomputation')
 else:
  target.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps({k:v for k,v in result.items() if k!='no_simple_prime_congruence_witnesses'},indent=2))
