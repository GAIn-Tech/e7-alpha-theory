"""Explicit dual-tangent cocycles, residue pairing, and nontrivial controls."""
import module_action as u
from functools import lru_cache
m,c,a,s,P,N=u.m,u.c,u.a,u.s,u.P,u.N
json,sys=u.json,u.sys

@lru_cache(None)
def classes(p,vq):
 out=[]
 for i in range(N):
  if -c.terms[i][2]!=p:continue
  for q in (0,3,6):
   k=q-vq
   if not 0<=k<=3:continue
   R,_,_,_=m.cohom((i,N),q,k)
   for col in range(R.cols):
    v=m.inc(c.lift(m.basis((i,N),q,k),R[:,col]));assert not c.dv(v)
    out.append(((i,N),q,k,col,v))
 return out

def hcvec(v,p,vq):
 pv=m.proj(v);out=[]
 for i in range(N):
  if -c.terms[i][2]!=p:continue
  for q in (0,3,6):
   k=q-vq
   if not 0<=k<=3:continue
   R,S,n,B=m.cohom((i,N),q,k)
   if not S.rows:continue
   out.extend(list(a.solve(S,m.coords(pv,m.basis((i,N),q,k)))[n:,:]))
 return s.Matrix(len(out),1,out)

def drow(p,q):
 cols=[hcvec(c.d1(v),p+1,q) for *_,v in classes(p,q)]
 return s.Matrix.hstack(*cols) if cols else s.zeros(len(classes(p+1,q)),0)

def residue(v):
 assert not c.total(v)
 pair=(N,N);pv=m.proj(v);R,S,n,B=m.cohom(pair,6,3)
 assert R.cols==1
 coords=a.solve(S,m.coords(pv,m.basis(pair,6,3)))[n:,:]
 assert coords.rows==1
 return coords[0]

def main():
 inp=json.loads((P/'module-action.json').read_text());src=json.loads((P.parent/'tian-yau-neutral-d4-gate/d4-chains.json').read_text())
 alphas=[u.unpack(r['surviving_total_cocycle']) for r in src['records']]
 charged=[u.unpack(v) for v in inp['charged_basis']]
 h2=[u.unpack(v) for v in inp['H2_low']]+[u.unpack(v['cocycle']) for v in inp['H2_high']]
 dual=[v for *_,v in classes(1,0)];dualrecords=[];rows={}
 for q in range(4):
  A=drow(-1,q);B=drow(0,q);assert not any(B*A)
  dims=[len(classes(p,q)) for p in [-1,0,1]]
  rows[str(q)]={'dimensions':dims,'A':a.sparse(A),'B':a.sparse(B),'E2':[dims[0]-A.rank(),dims[1]-A.rank()-B.rank(),dims[2]-B.rank()]}
  print('dual row',q,rows[str(q)]['E2'],flush=True)
 K=drow(-1,2)
 for x in K.nullspace():
  v0=m.combine(classes(-1,2),x)
  v1=m.primitive(c.scale(c.d1(v0),-1))
  v2=m.primitive(c.scale(c.add(c.d1(v1),c.d2cor(v0)),-1))
  full=c.add(v0,v1,v2);u.validate(full,1);assert not c.total(full)
  dual.append(full);dualrecords.append({'source':c.pack(v0),'primitive1':c.pack(v1),'primitive2':c.pack(v2),'cocycle':c.pack(full)})
 assert len(dual)==6
 pairing=s.Matrix([[residue(u.action(beta,h)) for h in h2] for beta in dual]);assert pairing.det()!=0
 print('Serre matrix',pairing,'det',pairing.det(),flush=True)
 tensor=[];pairrecords=[]
 for n in range(4):
  slab=[]
  for j in range(9):
   rec=next(r for r in inp['products'] if r['neutral']==n and r['charged']==j)
   image=u.unpack(rec['image']);co=s.Matrix([s.Rational(x) for x in rec['coordinates']]);vals=[]
   for k,beta in enumerate(dual):
    scalar=u.action(beta,image);value=residue(scalar)
    assert value==(pairing*co)[k];vals.append(str(value))
    pairrecords.append({'neutral':n,'charged':j,'dual':k,'scalar_cocycle':c.pack(scalar),'residue':str(value)})
   slab.append(vals)
  tensor.append(slab)
  print('paired slab',n,slab,flush=True)
 # Leibniz on every alpha-support monomial, against every charged cocycle.
 controls={'keywise_Leibniz':0,'wrong_product_sign':0,'charged_boundaries':0,'neutral_boundaries':0,'dual_boundaries':0,'pairing_boundary_residues':0}
 used=set().union(*(set(v) for v in alphas))
 for key in sorted(used):
  av={key:c.F(1)}
  for v in charged:
   lhs=c.total(u.action(av,v));rhs=c.add(u.action(c.total(av),v),c.scale(u.action(av,c.total(v)),-1));assert lhs==rhs
   controls['keywise_Leibniz']+=1
   if c.total(u.action(av,v,True))!=c.add(u.action(c.total(av),v,True),c.scale(u.action(av,c.total(v),True),-1)):controls['wrong_product_sign']+=1
 print('keywise controls',controls,flush=True)
 # Every invariant H0(B) generator produces an actual charged exact change.
 for *_,b in u.classes(0,0):
  db=c.total(b)
  if not db:continue
  for alpha in alphas:
   lhs=u.action(alpha,db);primitive=c.scale(u.action(alpha,b),-1)
   assert lhs==c.total(primitive)
   for beta in dual:
    assert residue(u.action(beta,lhs))==0;controls['pairing_boundary_residues']+=1
   controls['charged_boundaries']+=1
 # Nontrivial neutral exact perturbations preserve total degree and character.
 for alpha in alphas:
  key=next(k for k in alpha if c.grade(k)[0]==-2);pair,I,e,X,Y=key
  U=X if len(X)>1 else Y;offset=0 if len(X)>1 else 4;ee=list(e);ii,jj=offset+U[0],offset+U[1]
  shift=3*max(1,(-ee[ii]+2)//3);ee[ii]+=shift;ee[jj]-=shift
  eta=c.hc({(pair,I,tuple(ee),X,Y):c.F(1)});assert eta and c.total(eta);u.validate(eta,0)
  for v in charged:
   delta=u.action(c.total(eta),v);primitive=u.action(eta,v)
   assert delta==c.total(primitive)
   for beta in dual:assert residue(u.action(beta,delta))==0;controls['pairing_boundary_residues']+=1
   controls['neutral_boundaries']+=1
 # Pairing boundary and sign tests with nonclosed individual dual monomials.
 for beta in dual:
  for key in list(beta)[:20]:
   bv={key:c.F(1)}
   for h in h2:
    assert c.total(u.action(bv,h))==c.add(u.action(c.total(bv),h),c.scale(u.action(bv,c.total(h)),-1))
    controls['dual_boundaries']+=1
 assert controls['wrong_product_sign']>0
 # Basis covariance with nontrivial invertible charged and dual shears.
 C=s.eye(9);C[0,5]=2;Q=s.eye(6);Q[1,0]=-3
 changed_c=c.add(charged[5],c.scale(charged[0],2));changed_b=c.add(dual[0],c.scale(dual[1],-3))
 for n,alpha in enumerate(alphas):
  actual=residue(u.action(changed_b,u.action(alpha,changed_c)))
  M=s.Matrix(tensor[n]).applyfunc(s.Rational)
  assert actual==(C.T*M*Q)[5,0]
 controls['basis_shear']=4
 # Unit e32/e33 gauge witness: flavors 0 and 1 in the declared actual bases.
 F=[str(s.Rational(tensor[n][0][0])+s.Rational(tensor[n][1][1])) for n in range(4)]
 # Another legitimate embedding of the same gauge matrices tests flavor dependence.
 F_nonzero=[str(s.Rational(tensor[n][5][1])+s.Rational(tensor[n][7][0])) for n in range(4)]
 chargedlabels=[]
 for v in charged:
  labels=[]
  for (pair,I,e,X,Y),coef in v.items():
   if X==Y==(0,):labels.append({'normal_equation':c.terms[pair[1]][1],'monomial':list(e),'coefficient':str(coef)})
  chargedlabels.append(labels)
 out={'passed':True,'source_hashes':{'module_action.py':u.sha(P/'module_action.py'),'module-action.json':u.sha(P/'module-action.json'),'serre_pairing.py':u.sha(P/'serre_pairing.py')},'dual_rows':rows,'dual_cocycles':[c.pack(v) for v in dual],'dual_nonpolynomial_lifts':dualrecords,'scalar_H3_generator':c.pack(m.inc(c.lift(m.basis((N,N),6,3),m.cohom((N,N),6,3)[0][:,0]))),'Serre_pairing':a.sparse(pairing),'Serre_determinant':str(pairing.det()),'tensor_shape':[4,9,6],'tensor':tensor,'scalar_products':pairrecords,'controls':controls,'charged_polynomial_labels':chargedlabels,'Higgs_same_gauge_alignment_first_two_flavors':{'L_flavors':[0,1],'Lbar_flavors':[0,1],'unit_neutral_F':F},'Higgs_alternate_flavor_embedding':{'L_flavors':[5,7],'Lbar_flavors':[1,0],'unit_neutral_F':F_nonzero},'claim_boundary':'Exact algebraic cubic tensor in explicit invariant cohomology bases; residue normalization fixed to displayed H3 generator. Gauge e32/e33 alignment does not specify geometric flavor embeddings. Neither canonical Kahler normalization nor full physical F/D vacuum is established.'}
 f=P/'serre-tensor.json';payload=u.text(out)
 if '--create' in sys.argv:
  with f.open('x',newline='\n') as h:h.write(payload)
 else:assert f.is_file() and f.read_text()==payload
 print(json.dumps({k:out[k] for k in ['Serre_determinant','controls','Higgs_same_gauge_alignment_first_two_flavors','Higgs_alternate_flavor_embedding']},indent=2),flush=True)
if __name__=='__main__':main()
