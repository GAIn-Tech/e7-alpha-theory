"""Exact A4-in-E8 charged deformation and first transferred obstruction.
Creation is exclusive; default replay compares existing immutable receipt.
"""
from pathlib import Path
import sys,json,hashlib,itertools
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'tian-yau-actual-survivor-coupling-gate'))
import module_action as u
c,m,a,s=u.c,u.m,u.a,u.s
N=u.N
assert N==13
c.terms.append(('O',1,0,(0,0)))

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def text(x):return json.dumps(x,sort_keys=True,indent=2)+'\n'
def bracket(x,y,dx,dy):return c.add(u.action(x,y),c.scale(u.action(y,x),-u.parity(dx*dy)))
def globalv(pair,I,e,coef=1):
 return {(pair,I,e,(i,),(j,)):c.F(coef) for i in range(4) for j in range(4)}
def remap(v,old,new):
 return {((new if ij[0]==old else ij[0],new if ij[1]==old else ij[1]),I,e,X,Y):z for (ij,I,e,X,Y),z in v.items()}
def root_embedding():
 eye=[s.eye(9)[:,i] for i in range(9)];one=s.ones(9,1)
 roots={tuple(eye[i]-eye[j]) for i in range(9) for j in range(9) if i!=j}
 for I in itertools.combinations(range(9),3):
  r=sum((eye[i] for i in I),s.zeros(9,1))-one/3
  roots.add(tuple(r));roots.add(tuple(-r))
 assert len(roots)==240 and all(sum(t*t for t in r)==2 for r in roots)
 weights=eye[:3]+[-eye[5]-eye[7]+one/3,-eye[5]-eye[8]+one/3]
 embedded={(i,j):weights[i]-weights[j] for i in range(5) for j in range(5) if i!=j}
 assert len(set(map(tuple,embedded.values())))==20
 assert all(tuple(r) in roots for r in embedded.values())
 simple=[weights[i]-weights[i+1] for i in range(4)]
 gram=s.Matrix(4,4,lambda i,j:(simple[i].T*simple[j])[0])
 assert gram==s.Matrix([[2,-1,0,0],[-1,2,-1,0],[0,-1,2,-1],[0,0,-1,2]])
 for i in range(3):
  for j,r in [(3,7),(4,8)]:assert embedded[i,j]==eye[i]+eye[5]+eye[r]-one/3
 # Root addition closure, not dimension-only identification.
 for x in embedded.values():
  for y in embedded.values():
   if tuple(x+y) in roots:assert tuple(x+y) in set(map(tuple,embedded.values()))
 # The full sl5 matrix bracket fixes Chevalley signs and all Jacobi identities.
 basis=[]
 for i,j in embedded:
  z=s.zeros(5);z[i,j]=1;basis.append(z)
 for i in range(4):
  z=s.zeros(5);z[i,i]=1;z[i+1,i+1]=-1;basis.append(z)
 def comm(x,y):return x*y-y*x
 # Associativity proves general Jacobi; evaluate all basis triples using sparse dicts.
 def mul(x,y):
  out={}
  for (i,j),v in x.items():
   for (k,l),w in y.items():
    if j==k:out[i,l]=out.get((i,l),0)+v*w
  return {k:v for k,v in out.items() if v}
 def add(*xs):
  out={}
  for x in xs:
   for k,v in x.items():out[k]=out.get(k,0)+v
  return {k:v for k,v in out.items() if v}
 def neg(x):return {k:-v for k,v in x.items()}
 def cb(x,y):return add(mul(x,y),neg(mul(y,x)))
 bs=[{(i,j):int(z[i,j]) for i in range(5) for j in range(5) if z[i,j]} for z in basis]
 tests=0
 for x,y,z in itertools.product(bs,repeat=3):
  assert not add(cb(x,cb(y,z)),cb(y,cb(z,x)),cb(z,cb(x,y)));tests+=1
 return {'E8_roots':len(roots),'A4_roots':len(embedded),'Cartan':a.sparse(gram),'weight_vectors':[[str(t) for t in v] for v in weights],'Jacobi_basis_triples':tests,'embedding_index':1}

def main():
 roots=root_embedding();print('A4 in E8 and Jacobi verified',flush=True)
 mod=json.loads((P.parent/'tian-yau-actual-survivor-coupling-gate/module-action.json').read_text())
 ser=json.loads((P.parent/'tian-yau-actual-survivor-coupling-gate/serre-tensor.json').read_text())
 cs=[u.unpack(x) for x in mod['charged_basis'][:2]]
 bs=[u.unpack(x) for x in ser['dual_cocycles'][:2]]
 cs[1]=remap(cs[1],N,N+1);bs[1]=remap(bs[1],N,N+1)
 a1=c.add(*cs,*bs);u.validate(a1,1);assert not c.total(a1)
 S2=c.scale(bracket(a1,a1,1,1),c.F(1,2))
 assert S2 and not c.total(S2)
 # All global degree-one End(L) and ideal-homotopy generators relevant to this source.
 # No cohomology projection, generic-rank assignment, or target fitting.
 dom=[]
 for i in range(N):
  for j in range(N):
   p=c.terms[j][2]-c.terms[i][2]
   k=p-1
   if not 0<=k<=3:continue
   for _,I,e in m.basis((i,j),0,k):dom.append(globalv((i,j),I,e))
 images=[c.total(x) for x in dom]
 keys=sorted(set(S2).union(*(set(v) for v in images)))
 # Global zero-Cech cochains are determined on one chart; retain the full lift check.
 keys=[k for k in keys if k[3]==k[4]==(0,)]
 M=s.Matrix(len(keys),len(dom),lambda i,j:s.Rational(images[j].get(keys[i],0)))
 b=s.Matrix([s.Rational(S2.get(k,0)) for k in keys])
 sol,params=M.gauss_jordan_solve(-b)
 sol=sol.subs({x:0 for x in params})
 a2=c.add(*[c.scale(v,c.F(str(sol[i]))) for i,v in enumerate(dom)])
 u.validate(a2,1);assert c.total(a2)==c.scale(S2,-1)
 print('quadratic exact lift',M.shape,'rank',M.rank(),'primitive terms',len(a2),flush=True)
 S3=bracket(a1,a2,1,1)
 assert not c.total(S3)
 # Record computed cochain; zero is asserted only after actual multiplication.
 S4=c.scale(bracket(a2,a2,1,1),c.F(1,2))
 print('order3 source terms',len(S3),'order4 with a3=0 terms',len(S4),flush=True)
 # Nonvacuous degree-zero representative perturbations, plus AW sign controls.
 controls={'nilpotence':0,'Leibniz':0,'wrong_product_sign_detected':0,'representative_changes':0,'graded_Jacobi':0}
 probes=[]
 for v in [a1,a2,S2]:
  for key in list(v)[:48]:probes.append(({key:c.F(1)},sum(c.grade(key)[:2])-c.grade(key)[2]))
 # Include a nonclosed Cech and Koszul fixture from genuine survivor support.
 d4=json.loads((P.parent/'tian-yau-neutral-d4-gate/d4-chains.json').read_text())
 for r in d4['records']:
  al=u.unpack(r['surviving_total_cocycle'])
  for key in list(al)[:24]:probes.append(({key:c.F(1)},1))
 for v,d in probes:
  assert not c.total(c.total(v));controls['nilpotence']+=1
  for w,e in [(a1,1),(a2,1)]:
   lhs=c.total(u.action(v,w));rhs=c.add(u.action(c.total(v),w),c.scale(u.action(v,c.total(w)),u.parity(d)))
   assert lhs==rhs;controls['Leibniz']+=1
   bad=c.add(u.action(c.total(v),w,True),c.scale(u.action(v,c.total(w),True),u.parity(d)))
   if c.total(u.action(v,w,True))!=bad:controls['wrong_product_sign_detected']+=1
  # [v,[a1,a2]]=[[v,a1],a2]+(-1)^d[a1,[v,a2]].
  assert bracket(v,bracket(a1,a2,1,1),d,2)==c.add(bracket(bracket(v,a1,d,1),a2,d+1,1),c.scale(bracket(a1,bracket(v,a2,d,1),1,d+1),u.parity(d)))
  controls['graded_Jacobi']+=1
 # Gauge representative changes: a1'=a1+D eta; explicit change of order-two lift.
 # Use global degree-zero Hom(O,V) polynomial B generators, with D eta !=0.
 for i in range(2,10):
  for _,I,e in m.basis((N,i),0,0):
   eta=globalv((N,i),I,e);deta=c.total(eta)
   if not deta:continue
   u.validate(eta,0);u.validate(deta,1)
   ap=c.add(a1,deta)
   # S2'-S2=D(-[a1,eta]+1/2[eta,Deta]).
   correction=c.add(bracket(a1,eta,1,0),c.scale(bracket(eta,deta,0,1),-c.F(1,2)))
   a2p=c.add(a2,correction)
   assert c.total(a2p)==c.scale(c.scale(bracket(ap,ap,1,1),c.F(1,2)),-1)
   # Gauge transform exp(-t ad_eta)(A) + (1-exp(-t ad_eta))/ad_eta Deta
   # yields a3'= -[eta,a2]+1/2[eta,[eta,a1]]+1/6[eta,[eta,Deta]].
   a3p=c.add(c.scale(bracket(eta,a2,0,1),-1),c.scale(bracket(eta,bracket(eta,a1,0,1),0,1),c.F(1,2)),c.scale(bracket(eta,bracket(eta,deta,0,1),0,1),c.F(1,6)))
   assert c.add(c.total(a3p),bracket(ap,a2p,1,1))==S3
   controls['representative_changes']+=1
 assert controls['representative_changes']>0
 # Explicit polynomial coefficients of lifts independent of chart repetition.
 compact=lambda v:c.pack({k:x for k,x in v.items() if k[3]==k[4]==(0,)})
 used=[Path(__file__),P.parent/'tian-yau-actual-survivor-coupling-gate/module_action.py',P.parent/'tian-yau-actual-survivor-coupling-gate/module-action.json',P.parent/'tian-yau-actual-survivor-coupling-gate/serre_pairing.py',P.parent/'tian-yau-actual-survivor-coupling-gate/serre-tensor.json',P.parent/'tian-yau-neutral-d4-gate/compute.py',P.parent/'tian-yau-neutral-d4-gate/d4-chains.json',P.parent/'tian-yau-neutral-d2-gate/total_cech.py',P.parent/'tian-yau-geometric-neutral-coupling-gate/certificate.json',P.parent/'tian-yau-flavor-higgs-consistency-gate/certificate.json']
 out={'passed':True,'embedding':roots,'a1':c.pack(a1),'quadratic_source':c.pack(S2),'quadratic_matrix':a.sparse(M),'quadratic_rhs':a.sparse(-b),'quadratic_solution':a.sparse(sol),'domain_generators':[compact(v) for v in dom],'target_keys':[[list(t) for t in k] for k in keys],'quadratic_matrix_rank':M.rank(),'a2':c.pack(a2),'a2_compact':compact(a2),'cubic_source':c.pack(S3),'quartic_source_a3_zero':c.pack(S4),'controls':controls,'source_hashes':{str(f.relative_to(P.parent)).replace('\\','/'):sha(f) for f in used},'claim_boundary':'Exact charged A4 sub-DGLA in E8, actual quadratic primitive and next MC source; not full higher superpotential, stabilized vacuum or all-orders family.'}
 f=P/'certificate.json';payload=text(out)
 if '--create' in sys.argv:
  with f.open('x',encoding='utf-8',newline='\n') as h:h.write(payload)
 else:assert f.is_file() and f.read_text(encoding='utf-8')==payload
 print(text({'passed':True,'controls':controls,'S3_terms':len(S3),'S4_terms':len(S4),'certificate_sha256':sha(f)}),flush=True)
if __name__=='__main__':main()
