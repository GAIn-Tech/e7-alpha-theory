"""Exact finite checks; not Lean, not a derivation of a physical compactification."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from collections import Counter
import json,hashlib,sys
B=Path(__file__).resolve().parent

def add(a,b):
 c=Counter(a);c.update(b);return {k:v for k,v in c.items() if v}
def mul(a,b):
 c={}
 for i,x in a.items():
  for j,y in b.items():c[i+j]=c.get(i+j,0)+x*y
 return {k:v for k,v in c.items() if v}
def scale(a,c):return {i:v*c for i,v in a.items() if v*c}
def tlmul(x,y,d):
 a,b=x;c,e=y
 return mul(a,c),add(add(mul(a,e),mul(b,c)),mul(mul(b,e),d))
def bracket_trefoil(mirror=False):
 d={2:-1,-2:-1};cross=({1:1},{-1:1})
 x=({0:1},{})
 for _ in range(3):x=tlmul(x,cross,d)
 # tr(I)=delta and tr(e)=1, with <unknot>=1.
 bracket=add(mul(x[0],d),x[1]);normalized=mul({-9:-1},bracket)
 if mirror:normalized={-i:v for i,v in normalized.items()}
 assert all(i%4==0 for i in normalized)
 return {i//-4:v for i,v in normalized.items()}
def convolution(a,b,N):return [sum(a[j]*b[i-j] for j in range(i+1)) for i in range(N+1)]
def certificate():
 # Enumerate the E8 lattice perpendicular to e7+e8, in doubled coordinates.
 # Bound norm^2<=6 implies integer coordinates in [-2,2], half-integers in +/-1/2,+/-3/2.
 theta=[0]*4
 for values in [(-4,-2,0,2,4),(-3,-1,1,3)]:
  for x in product(values,repeat=7):
   v=x[:6]+(x[6],-x[6])
   if sum(v)%4:continue
   norm8=sum(a*a for a in v)
   if norm8<=24:
    assert norm8%8==0
    theta[norm8//8]+=1
 osc=[1,0,0,0]
 for m in range(1,4):
  for color in range(7):
   for n in range(m,4):osc[n]+=osc[n-m]
 character=convolution(theta,osc,3)
 assert theta[1]==126 and character[1]==133
 # exact Verlinde arithmetic S=M/sqrt(2), two sectors 0,x.
 M=[[1,1],[1,-1]]
 fusion={}
 for a,b,c in product(range(2),repeat=3):
  n=sum(F(M[a][j]*M[b][j]*M[c][j],2*M[0][j]) for j in range(2))
  assert n==int(c==(a+b)%2)
  fusion[f'{a},{b}->{c}']=int(n)
 genus=[int(2*F(1,2)**(1-g)) for g in range(5)]
 assert genus==[2**g for g in range(5)]
 central=F(133,19);assert central==7
 # b3 -> S3: standard Specht module (2,1), basis e1-e3,e2-e3.
 s=((0,1),(1,0));det=s[0][0]*s[1][1]-s[0][1]*s[1][0]
 assert det==-1
 mirror_det_equal=F(det)**3==F(det)**(-3)
 assert mirror_det_equal
 V=bracket_trefoil();Vm=bracket_trefoil(True);assert V!=Vm
 # first Rogers-Ramanujan identity coefficients via independent sum and product algorithms.
 N=30;lhs=[0]*(N+1)
 for n in range(6):
  shift=n*n
  if shift>N:continue
  a=[1]+[0]*N
  for k in range(1,n+1):
   for j in range(k,N+1):a[j]+=a[j-k]
  for j in range(N-shift+1):lhs[j+shift]+=a[j]
 rhs=[1]+[0]*N
 for k in range(1,N+1):
  if k%5 in (1,4):
   for j in range(k,N+1):rhs[j]+=rhs[j-k]
 assert lhs==rhs
 return dict(passed=True,claim_boundary='Exact finite algebra and coefficient checks only; modular identification is sourced/assumed, not kernel proved. No spacetime dimension, 4D chirality or coupling prediction.',e7_theta_norm_le_6=theta,seven_color_partitions=osc,theta_times_oscillator=character,e7_level1_c=str(central),level1_genus_hilbert_dimensions=genus,level1_fusion=fusion,level1_conformal_weight='3/4',level1_topological_spin='-i',trefoil_jones=V,mirror_jones=Vm,self_conjugate_partition=[2,1],standard_S3_transposition_determinant=det,braid_mirror_determinant_equal=mirror_det_equal,rogers_ramanujan_coefficients_0_to_30=lhs)
if __name__=='__main__':
 data=certificate();data['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();p=B/'exact_receipt.json'
 if '--verify' in sys.argv:
  assert p.exists(),'missing stored receipt';assert json.loads(p.read_text())==json.loads(json.dumps(data)),'stale receipt';print('PASS: saved exact receipt replayed without regeneration')
 else:p.write_text(json.dumps(data,indent=2));print(json.dumps(data,indent=2))
