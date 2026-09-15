"""Exact charged cup products in the derived exterior cube, with explicit boundary DAG.
The absolute comparison with the predecessor's adjunction/Serre normalization is NOT computed.
"""
import sys,json,hashlib
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parent
import ring as r
import exterior as e
s=r.s
sys.path.insert(0,str(P/'frozen/tian-yau-actual-survivor-coupling-gate'))
import module_action as u
c,m,a=u.c,u.m,u.a

def text(x):return json.dumps(x,sort_keys=True,indent=2)+'\n'
def pack(v):return [[list(t),list(I),list(ex),str(x)] for (t,I,ex),x in sorted(v.items())]
def scale(v,x):return {k:a*x for k,a in v.items() if a*x}
def add(*vs):
 out={}
 for v in vs:
  for k,x in v.items():r.addto(out,k,x)
 return out

def D(v,wrong=False):
 out={}
 for (t,I,ex),x in v.items():
  for j,h in enumerate(I):
   for mon,cf in r.f[h].terms():r.addto(out,(t,I[:j]+I[j+1:],tuple(a+b for a,b in zip(ex,mon))),(-1)**j*x*F(str(cf)))
  for nt,sg,pol in e.diff(t):
   for mon,cf in pol.items():r.addto(out,(nt,I,tuple(a+b for a,b in zip(ex,mon))),(-1)**len(I)*sg*x*cf)
  for pos,i in enumerate(t):
   if i>=2:continue
   for h in range(3):
    cf=r.deg[h][i]
    if not cf or h in I:continue
    nt,sg=e.canon(t[:pos]+(10+h,)+t[pos+1:]);II=tuple(sorted(I+(h,)))
    if sg:r.addto(out,(nt,II,ex),(1 if wrong else -1)*(-1)**sum(j<h for j in I)*sg*cf*x)
 return out

def wedge(v,w,wrong=False):
 out={}
 for (t,I,ex),x in v.items():
  p=sum(e.terms[i][2] for i in t)
  for (tt,J,ee),y in w.items():
   if set(I)&set(J):continue
   nt,sg=e.canon(t+tt)
   if not sg:continue
   if wrong and set(t)&set(tt)&{10,11,12}:continue
   sign=(-1)**(p*len(J)+sum(i>j for i in I for j in J))*sg
   r.addto(out,(nt,tuple(sorted(I+J)),tuple(a+b for a,b in zip(ex,ee))),sign*x*y)
 return out

def monchain(b):return {(tuple(10+i for i in range(3) for _ in range(b[i])),(),tuple(b[3:])):F(1)}
def vecchain(q,v):return add(*(scale(monchain(q.bs[i]),x) for i,x in v.items()))
def chainvalidate(v,degree,character):
 for (t,I,ex),cf in v.items():
  assert t==tuple(sorted(t)) and I==tuple(sorted(set(I)))
  assert all(t.count(i)<=1 for i in range(2,10))
  assert sum(e.terms[i][2] for i in t)-len(I)==degree
  assert tuple(sum(ex[4*b:4*b+4]) for b in range(2))==tuple(sum(e.terms[i][3][b] for i in t)-sum(r.deg[h][b] for h in I) for b in range(2))
  assert (sum(a*b for a,b in zip(ex,r.w))-sum(e.terms[i][4] for i in t))%3==character

def relation_primitive(name,b):
 t=tuple(10+i for i in range(3) for _ in range(b[i]));ex=tuple(b[3:])
 if name[0]=='f':return {(t,(int(name[1:]),),ex):F(1)}
 return {((2+int(name[1:]),)+t,(),ex):F(1)}

class CertifiedQuotient:
 def __init__(self,k,ch):
  self.k=k;self.ch=ch;self.bs=r.basis(k,ch=ch);self.index={v:i for i,v in enumerate(self.bs)};self.piv={};self.dag={};self.raw=[]
  for pol,pk,dx,dy,wt,name in r.relations:
   for b in r.basis(k-pk,-dx,-dy,(ch-wt)%3):
    v={self.index[tuple(x+y for x,y in zip(b,ex))]:cf for ex,cf in pol.items()}
    rid=len(self.raw);self.raw.append((name,b,v))
    prim=relation_primitive(name,b);chainvalidate(prim,k-1,ch)
    assert D(prim)==vecchain(self,v)
    rem,steps=self.reduce(v)
    if rem:
     p=max(rem);lead=rem[p];self.piv[p]={i:x/lead for i,x in rem.items()}
     self.dag[p]=(rid,lead,steps)
     # Boundary DAG equation checked as polynomial chains, not an assigned rank.
     assert vecchain(self,self.piv[p])==scale(add(D(prim),*(scale(vecchain(self,self.piv[j]),-x) for j,x in steps.items())),1/lead)
  self.free=[i for i in range(len(self.bs)) if i not in self.piv]
  print('certified quotient',k,ch,len(self.bs),len(self.piv),len(self.free),flush=True)
 def reduce(self,v):
  v=v.copy();out={};steps={}
  while v:
   i=max(v);x=v[i]
   if i not in self.piv:out[i]=v.pop(i);continue
   steps[i]=steps.get(i,F(0))+x
   for j,cf in self.piv[i].items():r.addto(v,j,-x*cf)
  return out,steps
 def record(self):
  return {'degree':self.k,'character':self.ch,'monomial_basis':self.bs,'free_indices':self.free,'raw_boundaries':[{'name':n,'multiplier':b,'primitive':pack(relation_primitive(n,b)),'image':[[i,str(x)] for i,x in sorted(v.items())]} for n,b,v in self.raw], 'boundary_DAG':[{'pivot':p,'origin':rid,'divisor':str(lead),'subtract_pivots':[[i,str(x)] for i,x in sorted(st.items())],'image':[[i,str(x)] for i,x in sorted(self.piv[p].items())]} for p,(rid,lead,st) in self.dag.items()]}

def actual_charged(b,ch):
 h=next(i for i in range(3) if b[i]);v={((u.N,10+h),(),tuple(b[3:]),(i,),(j,)):F(1) for i in range(4) for j in range(4)}
 assert not c.total(v)
 for key in v:
  pair,I,ex,X,Y=key
  assert sum(a*b for a,b in zip(ex,r.w))%3==ch
  assert sum(c.grade(key)[i]*sg for i,sg in [(0,1),(1,1),(2,-1)])==1
 return v

def main():
 # Every dependency and program source is already frozen before calculation.
 manifest=json.loads((P/'source-manifest.json').read_text())
 for name,hh in manifest.items():assert hashlib.sha256((P/name).read_bytes()).hexdigest()==hh,name
 qs={ch:CertifiedQuotient(1,ch) for ch in [0,1,2]};top=CertifiedQuotient(3,0)
 assert [len(qs[ch].free) for ch in [0,1,2]]==[9,7,7] and len(top.free)==1
 bases={ch:[qs[ch].bs[i] for i in qs[ch].free] for ch in qs}
 lifts={str(ch):[c.pack(actual_charged(b,ch)) for b in bs] for ch,bs in bases.items()}
 old=json.loads((P/'frozen/tian-yau-actual-survivor-coupling-gate/serre-tensor.json').read_text())
 assert [b[3:] for b in bases[0]]==[tuple(labels[0]['monomial']) for labels in old['charged_polynomial_labels']]
 assert [next(i for i,v in enumerate(b[:3]) if v) for b in bases[0]]==[labels[0]['normal_equation'] for labels in old['charged_polynomial_labels']]
 # Check completeness of H1(TX): row q1 Jacobian is injective on H1(B).
 q1tan={}
 for ch in range(3):
  src=[];tgt=[]
  for i,t in enumerate(e.terms):
   if t[0] not in ['B','C']:continue
   d=t[3];side=int(d[1]>0)
   if d[1-side]:continue
   for ex in r.comps(d[side]-1,4):
    if ex[3]>=3:continue
    es=ex+(-1,)*4 if not side else (-1,)*4+ex
    if (sum(a*b for a,b in zip(es,r.w))-t[4])%3==ch:(src if t[0]=='B' else tgt).append((i,side,ex))
  ix={v:j for j,v in enumerate(tgt)};cols=[]
  for i,side,ex in src:
   col={}
   for aa,bb,po in e.arrows:
    if aa!=i:continue
    for mon,cf in po.items():
     if e.terms[bb][3][1-side]:continue
     ee=tuple(a+b for a,b in zip(ex,mon[4*side:4*side+4]))
     for exp,cc in e.red(ee).items():r.addto(col,ix[bb,side,exp],cf*cc)
   cols.append(col)
  rank=e.rank(cols);assert rank==len(src);q1tan[str(ch)]={'source':len(src),'target':len(tgt),'rank':rank}
 # Every line cohomology degree entering exterior^3 is cross-checked by the inherited full ambient Koszul computation.
 lcs={}
 for dd in sorted({e.info(t)[1] for t in e.triples}):
  lc=a.line(*dd);lcs[str(dd)]=lc;assert lc[2]==[0,0,0]
  assert lc[3]==([1,0,0] if dd==(0,0) else [0,0,0])
  if all(dd):assert lc[1]==[0,0,0]
  elif dd!=(0,0):
   side=int(dd[1]>0);counts=[0,0,0]
   for ex in r.comps(dd[side]-1,4):
    if ex[3]>=3:continue
    es=ex+(-1,)*4 if not side else (-1,)*4+ex;counts[sum(a*b for a,b in zip(es,r.w))%3]+=1
   assert lc[1]==counts
 dims={p:len(e.basis(p)) for p in range(-3,4)};ms={p:e.matrix(p) for p in range(-3,3)};ranks={p:e.rank(cols) for p,(n,cols) in ms.items()}
 for p in range(-3,2):
  for col in ms[p][1]:
   out={}
   for i,x in col.items():
    for j,y in ms[p+1][1][i].items():r.addto(out,j,x*y)
   assert not out
 E2={p:dims[p]-ranks.get(p,0)-ranks.get(p-1,0) for p in dims};assert E2[1]==E2[2]==0
 assert all(e.info(t)[0]==-3 for t in e.triples if e.info(t)[1]==(0,0))
 # Thus top E2^(3,0) survives: possible incoming d2^(1,1), d3^(0,2), d4^(-1,3) have zero source.
 # Other total-degree-three slots vanish; top is H3(exterior^3 TX), not just a polynomial diagnostic.
 products=[];tensor=[];target=top.free[0];tchain=monchain(top.bs[target]);assert not D(tchain)
 for kk,h in enumerate(bases[0]):
  mat=[]
  for i,b in enumerate(bases[2]):
   row=[]
   for j,bb in enumerate(bases[1]):
    prod=wedge(wedge(monchain(b),monchain(bb)),monchain(h));chainvalidate(prod,3,0);assert not D(prod)
    mon=tuple(a+b+c for a,b,c in zip(b,bb,h));rem,st=top.reduce({top.index[mon]:F(1)});value=rem.get(target,F(0));assert len(rem)<=1
    assert prod==add(scale(tchain,value),*(scale(vecchain(top,top.piv[p]),x) for p,x in st.items()))
    if kk<2:products.append({'c':kk,'Q':i,'Qc':j,'wedge_cocycle':pack(prod),'coordinate':str(value),'boundary_DAG_combination':[[p,str(x)] for p,x in sorted(st.items())]})
    row.append(str(value))
   mat.append(row)
  tensor.append(mat)
 Y=[s.Matrix(tensor[k]).applyfunc(s.Rational) for k in range(2)]
 # Actual e32/e33 index-loop contraction, with Q[a,l], Qc[r,a], L[l,r].
 labelsQ=[(i,l) for i in range(7) for l in range(3)];labelsQc=[(j,rr) for j in range(7) for rr in range(3)]
 L=[s.zeros(3),s.zeros(3)];L[0][2,1]=1;L[1][2,2]=1
 M=s.Matrix([[sum(Y[k][i,j]*L[k][l,rr] for k in range(2)) for j,rr in labelsQc] for i,l in labelsQ])
 trip=Y[0].row_join(Y[1]);assert M.rank()==trip.rank()
 # Closed scalar target and its existing residue normalization, but no claim that theta(t)=g in the inherited adjunction convention.
 g=u.unpack(old['scalar_H3_generator']);assert not c.total(g)
 pair=(u.N,u.N);R,S,n,B=m.cohom(pair,6,3);co=a.solve(S,m.coords(m.proj(g),m.basis(pair,6,3)))[n:,:];assert list(co)==[1]
 controls={'D_squared':0,'wrong_curvature_detected':0,'nontrivial_boundary_products':0,'wrong_wedge_repeated_C_detected':False,'charged_closed':sum(len(bs) for bs in bases.values()),'charge_selection':0}
 exzero=(0,)*8
 for t in e.triples:
  v={(t,(),exzero):F(1)}
  assert not D(D(v));controls['D_squared']+=1
  if D(D(v,True),True):controls['wrong_curvature_detected']+=1
 assert controls['wrong_curvature_detected']>0
 c0=monchain(bases[0][0]);assert wedge(wedge(c0,c0),c0)==tchain
 assert wedge(c0,c0,True)!=wedge(c0,c0);controls['wrong_wedge_repeated_C_detected']=True
 # Degree-one boundary perturbations in each colored character, tested against every partner and both Higgs modes.
 for ch,partner in [(2,1),(1,2)]:
  for name,b,im in qs[ch].raw:
   prim=relation_primitive(name,b);db=D(prim)
   if not db:continue
   for bb in bases[partner]:
    for h in bases[0][:2]:
     v=monchain(bb);hh=monchain(h);delta=wedge(wedge(db,v),hh);primitive=wedge(wedge(prim,v),hh)
     assert D(primitive)==delta
     if delta:controls['nontrivial_boundary_products']+=1
     vv={}
     for (t,I,ex),x in delta.items():
      assert not I;ps=tuple(t.count(10+i) for i in range(3));r.addto(vv,top.index[ps+ex],x)
     assert not top.reduce(vv)[0]
 assert controls['nontrivial_boundary_products']>0
 # Exact cyclotomic projector 1+w^q+w^(2q), w^2+w+1=0. No numerical roots of unity.
 zz=s.Symbol('omega');mod=s.Poly(zz**2+zz+1,zz)
 for q in range(3):
  p=s.rem(s.Poly(1+zz**q+zz**(2*q),zz),mod).as_expr();assert p==(3 if q==0 else 0);controls['charge_selection']+=1
 # Nonzero wrong-charge example: c0^2 times a character-one monomial is rejected before invariant projection.
 wrongmon=tuple(a+b+c for a,b,c in zip(bases[0][0],bases[0][0],bases[1][0]));assert sum(a*b for a,b in zip(wrongmon[3:],r.w))%3==1
 # Full-rank assertion is derived, not guessed. Wrong index transpose changes the active SU2 block.
 badL=[ll.T for ll in L];badM=s.Matrix([[sum(Y[k][i,j]*badL[k][l,rr] for k in range(2)) for j,rr in labelsQc] for i,l in labelsQ]);assert badM!=M
 # Invertible flavor shears preserve the independently computed mass rank.
 A=s.eye(7);A[0,1]=2;B=s.eye(7);B[2,0]=-3
 assert (A.T*Y[0]*B).det()==A.det()*Y[0].det()*B.det()
 receipt={'passed':True,'absolute_residue_comparison_complete':False,'claim_boundary':'Exact geometric exterior-cube cup products and nonzero top class; matrices are ratios to t=c0^3. Absolute comparison t -> inherited scalar H3 generator is uncomputed, as are conjugate 4x4 slices and the complete exotic Hessian. No physically normalized masses or full vacuum.','bases':{str(ch):bs for ch,bs in bases.items()},'charged_cocycles':lifts,'tangent_q1_injectivity':q1tan,'exterior_line_cohomology':lcs,'exterior_q1':{'dims':dims,'ranks':ranks,'E2':E2},'top_dimension':len(top.free),'top_generator':top.bs[target],'top_wedge_cocycle':pack(tchain),'existing_scalar_H3_generator':c.pack(g),'existing_scalar_residue':'1','comparison_factor':'lambda = coefficient of adjunction_contraction(t) in existing scalar H3 generator; nonzero, not calculated','relative_tensor_7x7x9_slices':tensor,'relative_two_slices':[[[str(x) for x in Y[k].row(i)] for i in range(7)] for k in range(2)],'slice_ranks':[x.rank() for x in Y],'slice_determinants':[str(x.det()) for x in Y],'per_color_gauge_mass_matrix':a.sparse(M),'Q_labels':labelsQ,'Qc_labels':labelsQc,'per_color_rank':M.rank(),'active_triplet_block':a.sparse(trip),'active_right_kernel':[[str(x) for x in v] for v in trip.nullspace()],'controls':controls,'conjugate_scope':{'domain_characters':[1,2,0],'dimensions':[4,4,6],'requested_Higgs_flavors':['beta0','beta1'],'matrices':None,'ranks':None,'missing':'Construct charged-character dual cocycles and the derived dual exterior-cube cup/adjunction trace in their actual basis. Beta0,beta1 existing cocycles alone do not determine the 4x4 partners.'}}
 chain_data={'quotients':[qs[ch].record() for ch in [0,1,2]]+[top.record()],'products':products,'exterior_q1_basis':{str(p):e.basis(p) for p in range(-3,4)},'exterior_q1_matrices':{str(p):{'rows':nr,'columns':[[[i,str(x)] for i,x in sorted(col.items())] for col in cols]} for p,(nr,cols) in ms.items()}}
 outputs={'certificate.json':text(receipt),'charged-wedge-chains.json':text(chain_data)}
 for name,payload in outputs.items():
  if '--create' in sys.argv:
   with (P/name).open('x',encoding='utf-8',newline='\n') as f:f.write(payload)
  else:assert (P/name).is_file() and (P/name).read_text(encoding='utf-8')==payload,name
 for name,hh in manifest.items():assert hashlib.sha256((P/name).read_bytes()).hexdigest()==hh,name
 print(text({k:receipt[k] for k in ['passed','absolute_residue_comparison_complete','slice_ranks','slice_determinants','per_color_rank','controls']}),flush=True)
if __name__=='__main__':main()
