"""Exact actual H2/H1 E2 representatives and ambient-cohomology Koszul primitives.
NOT a geometric d2: no Cech/Koszul/curved-End totalization is silently assumed.
"""
from pathlib import Path
import sys,json,hashlib
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parent
PRE=P.parent/'tian-yau-survivor-yoneda-gate'
sys.path.insert(0,str(PRE))
from exact_audit import *
P=Path(__file__).resolve().parent

def sparse(M):
 return {'shape':list(M.shape),'entries':[[int(i),int(j),str(v)] for (i,j),v in s.MutableSparseMatrix(M).todok().items()]}
def solve(A,B):
 if not B.cols:return s.zeros(A.cols,0)
 X,t=A.gauss_jordan_solve(B);X=X.subs({v:0 for v in t});assert A*X==B;return X

def quotient(D,B):
 assert D*B==s.zeros(D.rows,B.cols)
 bs=B.columnspace();span=s.Matrix.hstack(*bs) if bs else s.zeros(D.cols,0);n=span.cols;reps=[]
 for v in D.nullspace():
  if span.row_join(v).rank()>span.cols:span=span.row_join(v);reps.append(v)
 R=s.Matrix.hstack(*reps) if reps else s.zeros(D.cols,0)
 return R,span,n

@lru_cache(None)
def space2(a,b,ch,k):
 bases={}
 for kk in range(4):
  for I in combinations(range(3),kk):
   q,es=ambient(a-sum(deg[i][0] for i in I),b-sum(deg[i][1] for i in I))
   if q==3:
    for e in es:
     if sum(t*v for t,v in zip(e,w))%3==ch:bases.setdefault(kk,[]).append((I,e))
 def matrix(kk):
  dom=bases.get(kk,[]);cod=bases.get(kk-1,[]);idx={t:i for i,t in enumerate(cod)};M=s.zeros(len(cod),len(dom))
  for j,(I,e) in enumerate(dom):
   for t,i in enumerate(I):
    for mon,c in f[i]:
     key=(I[:t]+I[t+1:],tuple(u+v for u,v in zip(e,mon)))
     if key in idx:M[idx[key],j]+=(-1)**t*c
  return M
 D=matrix(k);B=matrix(k+1);R,S,n=quotient(D,B)
 assert R.cols==line(a,b)[3-k][ch]
 return {'bases':bases,'D':D,'B':B,'R':R,'span':S,'nb':n,'k':k}

def run(ch=0):
 terms=[]
 for name,p in [('A',-1),('B',0),('C',1)]:
  for i,d in enumerate(G[name]):terms.append((name,i,p,d,w[i] if name=='B' else 0))
 idx={(a[0],a[1]):i for i,a in enumerate(terms)}
 arrows=[(idx['A',int(i>=4)],idx['B',i],z[i]) for i in range(8)]
 fs=[s.sympify(t,locals=dict(zip(G['variables'],z))) for t in G['polynomials']]
 for a in range(3):
  for i in range(8):
   pol=s.diff(fs[a],z[i])
   if pol:arrows.append((idx['B',i],idx['C',a],pol))
 saved={};rowdata={}
 for k,ps in [(1,[-2,-1,0]),(2,[0,1,2])]:
  blocks={p:[] for p in ps}
  # Include acyclic summands with nonempty middle Koszul chain groups:
  # dropping these loses boundary-valued End images.
  for i,a in enumerate(terms):
   for j,b in enumerate(terms):
    p=b[2]-a[2]
    if p not in blocks:continue
    d=tuple(v-u for u,v in zip(a[3],b[3]));lc=(ch-a[4]+b[4])%3;sp=space2(*d,lc,k)
    if sp['D'].cols:blocks[p].append(((i,j),sp))
  raw={};inc={};bound={};dvert={};coh={};offsets={}
  for p in ps:
   bs=blocks[p];inc[p]=s.diag(*(sp['R'] for _,sp in bs)) if bs else s.zeros(0,0)
   bound[p]=s.diag(*(sp['B'] for _,sp in bs)) if bs else s.zeros(0,0)
   dvert[p]=s.diag(*(sp['D'] for _,sp in bs)) if bs else s.zeros(0,0)
   off=0;offsets[p]={}
   for pair,sp in bs:offsets[p][pair]=(off,sp);off+=sp['D'].cols
  for p in ps[:-1]:
   M=s.zeros(inc[p+1].rows,inc[p].rows);col=0
   for (i,j),sp in blocks[p]:
    for aa,bb,poly in arrows:
     targets=[]
     if aa==j:targets.append(((i,bb),1))
     if bb==i:targets.append(((aa,j),-s.Integer(-1)**p))
     for pair,sign in targets:
      if pair not in offsets[p+1]:continue
      off,dp=offsets[p+1][pair];index={v:n for n,v in enumerate(dp['bases'].get(k,[]))}
      for c,(I,e) in enumerate(sp['bases'].get(k,[])):
       for mon,coef in s.Poly(poly,*z).terms():
        key=(I,tuple(u+v for u,v in zip(e,mon)))
        if key in index:M[off+index[key],col+c]+=sign*coef
    col+=sp['D'].cols
   raw[p]=M
   # Each block has independent [boundary basis, cohomology reps] coordinates.
   image=M*inc[p];boundary_image=M*bound[p];out=[];bprim=[];start=0
   for pair,dp in blocks[p+1]:
    nr=dp['D'].cols;im=image[start:start+nr,:];bim=boundary_image[start:start+nr,:]
    sol=solve(dp['span'],im);out.append(sol[dp['nb']:,:])
    bsol=solve(dp['span'],bim)
    assert bsol[dp['nb']:,:]==s.zeros(dp['R'].cols,bim.cols)
    bprim.append(solve(dp['B'],bim));start+=nr
   coh[p]=s.Matrix.vstack(*out) if out else s.zeros(0,inc[p].cols)
   primitive=s.Matrix.vstack(*bprim) if bprim else s.zeros(bound[p+1].cols,bound[p].cols)
   assert bound[p+1]*primitive==boundary_image
   saved[f'q{3-k}_p{p}_source_boundary_primitive']=sparse(primitive)
  a,b,c=ps
  assert coh[b]*coh[a]==s.zeros(coh[b].rows,coh[a].cols)
  R,S,nb=quotient(coh[b],coh[a]);actual=inc[b]*R
  primitive=solve(bound[c],raw[b]*actual)
  assert dvert[b]*actual==s.zeros(dvert[b].rows,actual.cols)
  assert raw[b]*actual==bound[c]*primitive
  # A real kernel/cokernel projection, defined only on d1 cycles.
  projection=solve(S,s.eye(S.rows)) if S.rows==S.cols else None
  # Coordinate left inverse on im(d1) + chosen E2 reps; use pivot rows.
  piv=list(S.T.rref()[1]);L=S[piv,:].inv();Q=s.zeros(R.cols,S.rows)
  for j,row in enumerate(piv):Q[:,row]=L[nb:,j]
  assert Q*S==s.eye(S.cols)[nb:,:] and Q*coh[a]==s.zeros(R.cols,coh[a].cols)
  assert Q*R==s.eye(R.cols)
  # Nontrivial mutations of actual lifts/projectors must fail.
  assert actual.cols and R.cols
  bad=actual.copy();bad[0,0]+=1
  mutation_closed=(dvert[b]*bad!=s.zeros(dvert[b].rows,bad.cols) or raw[b]*bad!=bound[c]*primitive)
  if not mutation_closed:
   badprimitive=primitive.copy()
   pos=next((j for j in range(bound[c].cols) if any(bound[c][:,j])),None)
   assert pos is not None;badprimitive[pos,0]+=1
   mutation_closed=raw[b]*actual!=bound[c]*badprimitive
  assert mutation_closed
  badQ=Q.copy();ii,jj=next((i,j) for i in range(R.rows) for j in range(R.cols) if R[i,j]);badQ[0,ii]+=1
  assert badQ*R!=s.eye(R.cols)
  row={'ps':ps,'E1_dimensions':[inc[p].cols for p in ps],'d1_ranks':[coh[p].rank() for p in ps[:-1]],'E2_dimension':R.cols,
       'blocks':{str(p):[{'pair':list(pair),'source':terms[pair[0]],'target':terms[pair[1]],'bases':{str(kk):v for kk,v in sp['bases'].items()},'D':sparse(sp['D']),'B':sparse(sp['B']),'R':sparse(sp['R'])} for pair,sp in blocks[p]] for p in ps},
       'd1':{str(p):sparse(coh[p]) for p in ps[:-1]},'raw_End':{str(p):sparse(raw[p]) for p in ps[:-1]},'E2_coordinates_in_E1':sparse(R),'E2_actual_ambient_Koszul_representatives':sparse(actual),'E2_cycle_projector':sparse(Q),'first_projected_Koszul_primitive':sparse(primitive),
       'checks':{'d1_square_zero':True,'E2_representatives_closed':True,'End_image_equals_Koszul_boundary':True,'source_boundary_primitives_verified':True,'projector_kills_d1_boundaries':True,'lift_mutation_rejected':bool(mutation_closed),'projector_mutation_rejected':True}}
  rowdata[str(3-k)]=row
 assert rowdata['2']['E2_dimension']==rowdata['1']['E2_dimension']==(60 if ch==0 else 56)
 # Ambient monad is curved: J E consists of multidegrees times equations.
 E=s.zeros(8,2);J=s.zeros(3,8)
 for i in range(8):E[i,int(i>=4)]=z[i]
 for a in range(3):
  for i in range(8):J[a,i]=s.diff(fs[a],z[i])
 curvature=(J*E).applyfunc(s.expand)
 assert curvature==s.Matrix([[deg[a][b]*fs[a] for b in range(2)] for a in range(3)])
 assert curvature!=s.zeros(3,2)
 files=[Path(__file__),PRE/'exact_audit.py',PRE/'q1_differential.py',PRE/'certificate.json',PRE/'q1-certificate.json',PRE/'verification.json',P.parent/'tian-yau-bundle-coupling-gate/geometry.json']
 return {'character':ch,'passed':True,'d2_computed':False,'d2_matrix':None,'d2_rank':None,'rows':rowdata,'boundary_primitives':saved,'ambient_monad_curvature':[[str(v) for v in curvature.row(i)] for i in range(curvature.rows)],'claim_boundary':'Actual E2 representatives and exact primitives on ambient H3 Koszul complexes only. No total Cech/Koszul lift, geometric d2, E3 rank, or vacuum verdict.','missing_solve':'Lift the ambient-H3 Koszul cycles to Cech-Koszul total cocycles, extend curved ambient End differential by explicit JE=f homotopies, solve D_vertical u=-D_horizontal a in the resulting total complex, then apply corrected next horizontal action and project into the saved E2^(1,1) quotient. The saved projected Koszul primitive is not this total primitive.','source_hashes':{str(t.relative_to(P.parent)).replace('\\','/'):hashlib.sha256(t.read_bytes()).hexdigest() for t in files}}

if __name__=='__main__':
 ch=int(sys.argv[sys.argv.index('--character')+1]) if '--character' in sys.argv else 0
 d=run(ch);text=json.dumps(d,sort_keys=True,indent=2)+'\n';out=P/f'partial-character-{ch}.json'
 if '--create' in sys.argv:
  with out.open('x',encoding='utf-8') as h:h.write(text)
 else:assert out.exists() and out.read_text(encoding='utf-8')==text,'missing/stale partial chain receipt'
 print(json.dumps({'passed':True,'character':ch,'d2_computed':False,'rows':{q:{k:v for k,v in r.items() if k in ['E1_dimensions','d1_ranks','E2_dimension','checks']} for q,r in d['rows'].items()}},indent=2))

