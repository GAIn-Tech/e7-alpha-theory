"""Exact Q(zeta_24) modular algebra and bounded lattice coset enumeration."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter
import json, hashlib, sys
P=Path(__file__).resolve().parent
# Phi_24(X)=X^8-X^4+1; canonical rational coefficient vectors.
def elt(v):
 v=list(map(F,v))+[F(0)]*max(0,8-len(v))
 for k in range(len(v)-1,7,-1):
  v[k-4]+=v[k];v[k-8]-=v[k]
 return tuple(v[:8])
Z=elt([0]); O=elt([1])
def add(a,b):return elt([x+y for x,y in zip(a,b)])
def neg(a):return elt([-x for x in a])
def mul(a,b):
 v=[F(0)]*15
 for i,x in enumerate(a):
  for j,y in enumerate(b):v[i+j]+=x*y
 return elt(v)
def powe(a,n):
 r=O
 for _ in range(n):r=mul(r,a)
 return r
z=elt([0,1])
def phase(n):return powe(z,n%24)
def conj(a):
 r=Z
 for i,x in enumerate(a):r=add(r,mul(elt([x]),phase(-i)))
 return r
def mm(a,b):return [[sumel(mul(x,y) for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def sumel(xs):
 r=Z
 for x in xs:r=add(r,x)
 return r
def dagger(a):return [[conj(x) for x in col] for col in zip(*a)]
def identity(n):return [[O if i==j else Z for j in range(n)] for i in range(n)]
def serial(a):return [[[str(c) for c in x] for x in row] for row in a]
def kron(a,b):return [[mul(a[i][j],b[k][l]) for j in range(len(a)) for l in range(len(b))] for i in range(len(a)) for k in range(len(b))]
def osc(rank,N):
 a=[1]+[0]*N
 for _ in range(rank):
  for k in range(1,N+1):
   for j in range(k,N+1):a[j]+=a[j-k]
 return a
def conv(a,b,N=2):return [sum(a[j]*b[n-j] for j in range(n+1)) for n in range(N+1)]
def lattice():
 # E8 = integer coordinates of even sum, or half-integers of even sum.
 # Doubled coordinates have uniform parity and sum divisible by four.
 # Exhaust norm <=4; each coordinate abs <=4 in doubled units.
 pts=[]
 def rec(v,sq,parity):
  if len(v)==8:
   if sum(v)%4==0:pts.append(tuple(v))
   return
  for x in range(-4+parity,5,2):
   if sq+x*x<=16:rec(v+[x],sq+x*x,parity)
 rec([],0,0);rec([],0,1)
 theta=Counter(sum(x*x for x in v)//8 for v in pts)
 e7=Counter(sum(x*x for x in v)//8 for v in pts if v[6]+v[7]==0)
 # Fix (v,alpha)=1: subtract alpha/2. Unique representatives of coset shells <=7/2.
 sector=Counter(F(sum(x*x for x in v),8)-F(1,4) for v in pts if v[6]+v[7]==2)
 roots=[v for v in pts if sum(x*x for x in v)==8]
 groups=Counter((v[6]+v[7])//2 for v in roots)
 assert theta=={0:1,1:240,2:2160}
 assert e7=={0:1,1:126,2:756}
 assert sector=={F(3,4):56,F(7,4):576}
 assert groups=={-2:1,-1:56,0:126,1:56,2:1}
 # Explicit lambda from one E8 root; all inner products with the prior simple basis integral.
 basis=[(1,-1,-1,-1,-1,-1,-1,1),(2,2,0,0,0,0,0,0),(-2,2,0,0,0,0,0,0)]
 for i in range(1,5):
  v=[0]*8;v[i]=-2;v[i+1]=2;basis.append(tuple(v))
 import importlib.util
 spec=importlib.util.spec_from_file_location('prior',P.parent/'connections/partitions/exact_certificate.py');prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)
 G=[[sum(F(x*y,4) for x,y in zip(a,b)) for b in basis] for a in basis]
 assert prior.det(G)==2
 r=next(v for v in roots if v[6]+v[7]==2)
 lam=tuple(F(r[i],2)-(F(1,2) if i>=6 else 0) for i in range(8))
 assert sum(x*x for x in lam)==F(3,2)
 assert all(sum(x*F(y,2) for x,y in zip(lam,b)).denominator==1 for b in basis)
 # 2lambda belongs to E8 and is perpendicular to alpha; lambda does not (non-even norm).
 two=[int(4*x) for x in lam]
 assert len({x%2 for x in two})==1 and sum(two)%4==0 and two[6]+two[7]==0
 glued_basis=basis+[r]
 G8=[[sum(F(x*y,4) for x,y in zip(a,b)) for b in glued_basis] for a in glued_basis]
 assert prior.det(G8)==1
 assert all(x.denominator==1 for row in G8 for x in row)
 assert all(G8[i][i]%2==0 for i in range(8))
 e7vac=conv([1,126,756],osc(7,2));e7non=conv([56,576],osc(7,1),1)
 a1vac=conv([1,2,0],osc(1,2));a1non=conv([2,0],osc(1,1),1)
 glued=conv(e7vac,a1vac)
 extra=conv(e7non,a1non,1)
 glued[1]+=extra[0];glued[2]+=extra[1]
 assert glued==conv([1,240,2160],osc(8,2))==[1,248,4124]
 return {'gram_determinant':'2','lambda':[str(x) for x in lam],'theta_E7':[1,126,756],'theta_E7_coset_shift_3_4':[56,576],'theta_E8':[1,240,2160],'E8_root_alpha_inner_product_counts':dict(sorted(groups.items())),'E7_vacuum_character':e7vac,'E7_nonvacuum_character':e7non,'A1_vacuum_character':a1vac,'A1_nonvacuum_character':a1non,'E8_glued_character':glued,'unglued_character':conv(e7vac,a1vac),'glue_index':2,'glued_determinant':str(F(2*2,2**2))}
def payload():
 assert phase(24)==O and phase(12)==neg(O)
 rt=add(phase(3),phase(-3));assert mul(rt,rt)==elt([2])
 invrt=mul(elt([F(1,2)]),rt)
 S=[[invrt,invrt],[invrt,neg(invrt)]]
 T=[[phase(-7),Z],[Z,phase(11)]]
 Ttop=[[O,Z],[Z,phase(18)]]
 I=identity(2);ST=mm(S,T)
 fusion=[[[sumel(mul(mul(mul(S[i][a],S[j][a]),conj(S[k][a])),rt) for a in range(2)) for k in range(2)] for j in range(2)] for i in range(2)]
 assert all(fusion[i][j][k]==(O if k==(i+j)%2 else Z) for i,j,k in product(range(2),repeat=3))
 assert mul(invrt,add(O,phase(18)))==phase(21)
 mirrored=[[conj(x) for x in row] for row in T]
 mST=mm(S,mirrored);assert mm(mm(mST,mST),mST)==I
 doubledST=mm(kron(S,S),kron(T,T));assert mm(mm(doubledST,doubledST),doubledST)==identity(4)
 assert (F(3,4)+F(3,4))%1!=0 # wrong-sign E7+E7 diagonal glue is not even
 assert mm(S,S)==I and mm(mm(ST,ST),ST)==I
 assert mm(S,dagger(S))==I and mm(T,dagger(T))==I
 topo=mm(S,Ttop);assert mm(mm(topo,topo),topo)==[[mul(phase(21),x) for x in row] for row in I]
 # Diagonal sesquilinear coefficient matrix and omitted-sector controls.
 missing=[[O,Z],[Z,Z]];image=mm(mm(dagger(S),missing),S)
 assert image!=missing and image==[[elt([F(1,2)])]*2 for _ in range(2)]
 assert mm(mm(dagger(S),I),S)==I and mm(mm(dagger(T),I),T)==I
 off=[[Z,O],[O,Z]];assert mm(mm(dagger(T),off),T)!=off
 Ta=[[phase(-1),Z],[Z,phase(5)]];Sa=S
 Sp=kron(S,Sa);Tp=kron(T,Ta);v=[[O],[Z],[Z],[O]]
 assert mm(Sp,v)==v and mm(Tp,v)==[[mul(phase(-8),x[0])] for x in v]
 omitted=[[O],[Z],[Z],[Z]];assert mm(Sp,omitted)!=omitted
 # Discriminant q7=3x/4, qA=x/4; unique nonzero isotropic vector in product.
 isotropic=[(x,y) for x,y in product(range(2),repeat=2) if (3*x+y)%4==0]
 assert isotropic==[(0,0),(1,1)]
 # H perp computed from b7=bA=xy/2.
 perp=[(x,y) for x,y in product(range(2),repeat=2) if (x+y)%2==0];assert perp==isotropic
 sources=[P/'exact_certificate.py',P/'Formalization.lean',P/'Challenge.lean',P.parent/'connections/partitions/exact_certificate.py']+sorted((P/'sources').glob('*'))
 return {'passed':True,'claim_boundary':'Exact worldsheet modular building block, not full string vacuum or spacetime chirality/family/dimension/scale selection. Python cyclotomic equalities are not Lean modular proofs.','cyclotomic_modulus':'X^8-X^4+1','S':serial(S),'T':serial(T),'topological_ST_cube_phase':'exp(2pi i *7/8)','relations':{'S_squared_identity':True,'ST_cubed_identity':True,'unitary':True,'diagonal_invariant':True},'negative_controls':{'missing_E7_sector_S_failure':True,'offdiagonal_T_failure':True,'unglued_product_S_failure':True,'omitting_central_phase_ST_failure':True},'glue_isotropic_subgroup':isotropic,'glue_perp':perp,'lattice':lattice(),'sha256':{str(x.relative_to(P)) if x.is_relative_to(P) else str(x):hashlib.sha256(x.read_bytes()).hexdigest() for x in sources}}
if __name__=='__main__':
 r=payload();f=P/'certificate.json'
 if '--verify' in sys.argv:
  assert f.exists(),'Missing receipt';assert json.loads(f.read_text())==json.loads(json.dumps(r)),'Stale or corrupted receipt';print('PASS: saved receipt replay; exact cyclotomic, lattice, gluing, negative controls')
 else:f.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r['lattice'],indent=2))
