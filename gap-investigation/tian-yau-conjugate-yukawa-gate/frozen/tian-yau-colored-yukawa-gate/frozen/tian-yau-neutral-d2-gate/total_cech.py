"""Executable tensor-standard-cover Cech/Koszul curved-End lifts over QQ."""
from fractions import Fraction as F
from itertools import combinations,product
import try_d2 as t
import partial_chains as a
from partial_chains import s,json,Path,P,sparse,solve
terms=[]
for name,p in [('A',-1),('B',0),('C',1)]:
 for i,dd in enumerate(a.G[name]):terms.append((name,i,p,dd))
idx={(v[0],v[1]):i for i,v in enumerate(terms)}
polys=[s.Poly(s.sympify(v,locals=dict(zip(a.G['variables'],a.z))),*a.z) for v in a.G['polynomials']]
mon=lambda pol:[(tuple(e),F(str(c))) for e,c in s.Poly(pol,*a.z).terms() if c]
fs=[mon(v.as_expr()) for v in polys]
arrows=[(idx['A',int(i>=4)],idx['B',i],mon(a.z[i])) for i in range(8)]
for aa in range(3):
 for i in range(8):
  pol=s.diff(polys[aa].as_expr(),a.z[i])
  if pol:arrows.append((idx['B',i],idx['C',aa],mon(pol)))
Hs=[(idx['A',b],idx['C',aa],aa,a.deg[aa][b]) for aa in range(3) for b in range(2) if a.deg[aa][b]]

def accum(out,key,v):
 if v:out[key]=out.get(key,F(0))+v
 if key in out and not out[key]:del out[key]
def add(*vs):
 out={}
 for v in vs:
  for k,x in v.items():accum(out,k,x)
 return out
def scale(v,c):return {k:x*c for k,x in v.items() if x*c}
def grade(key):
 pair,I,e,X,Y=key;p=terms[pair[1]][2]-terms[pair[0]][2];return p,len(X)+len(Y)-2,len(I)

def dc(v):
 out={}
 for (pair,I,e,X,Y),coef in v.items():
  p=terms[pair[1]][2]-terms[pair[0]][2];sign=(-1)**(p+len(I))
  # parity exponent is nonnegative modulo two; cast to avoid float negative powers
  sign=1 if (p+len(I))%2==0 else -1
  for axis,U in enumerate([X,Y]):
   for j in range(4):
    if j in U:continue
    V=tuple(sorted(U+(j,)));sgn=sign*(-1)**V.index(j)*((-1)**(len(X)-1) if axis else 1)
    accum(out,(pair,I,e,V if axis==0 else X,V if axis==1 else Y),sgn*coef)
 return out

def kap(v):
 out={}
 for (pair,I,e,X,Y),coef in v.items():
  for j,fi in enumerate(I):
   for exp,c in fs[fi]:accum(out,(pair,I[:j]+I[j+1:],tuple(x+y for x,y in zip(e,exp)),X,Y),(-1)**j*c*coef)
 return out

def d1(v):
 out={}
 for (pair,I,e,X,Y),coef in v.items():
  i,j=pair;p=terms[j][2]-terms[i][2];sgn=1 if p%2==0 else -1
  for aa,bb,poly in arrows:
   for target,sign in ([((i,bb),1)] if aa==j else [])+([((aa,j),-sgn)] if bb==i else []):
    for exp,c in poly:accum(out,(target,I,tuple(x+y for x,y in zip(e,exp)),X,Y),(-1)**len(I)*sign*c*coef)
 return out

def d2cor(v,wrong=False):
 out={}
 for (pair,I,e,X,Y),coef in v.items():
  i,j=pair
  for aa,bb,fi,c in Hs:
   if fi in I:continue
   J=tuple(sorted((fi,)+I));sgn=-(-1)**sum(x<fi for x in I)
   for target,sign in ([((i,bb),1)] if aa==j else [])+([((aa,j),-1)] if bb==i else []):accum(out,(target,J,e,X,Y),(-1 if wrong else 1)*sgn*sign*c*coef)
 return out

def dv(v):return add(dc(v),kap(v))
def total(v):return add(dv(v),d1(v),d2cor(v))

def hp(U,e):
 N={i for i,x in enumerate(e) if x<0}
 if len(N)==4:return []
 anchor=next(i for i in range(4) if i not in N)
 if anchor not in U or len(U)==1:return []
 return [(U[:U.index(anchor)]+U[U.index(anchor)+1:],(-1)**U.index(anchor))]
def pp(U,e):
 N={i for i,x in enumerate(e) if x<0}
 if len(N)==4:return [(U,1)] if len(U)==4 else []
 if not N and U==(0,):return [((j,),1) for j in range(4)]
 return []
def hc(v):
 out={}
 for (pair,I,e,X,Y),c in v.items():
  p=terms[pair[1]][2]-terms[pair[0]][2];sgn=1 if (p+len(I))%2==0 else -1
  for V,b in hp(X,e[:4]):accum(out,(pair,I,e,V,Y),sgn*b*c)
  for V,b in pp(X,e[:4]):
   for W,cc in hp(Y,e[4:]):accum(out,(pair,I,e,V,W),sgn*(-1)**(len(X)-1)*b*cc*c)
 return out

def pc(v):
 out={}
 for (pair,I,e,X,Y),c in v.items():
  for V,b in pp(X,e[:4]):
   for W,cc in pp(Y,e[4:]):accum(out,(pair,I,e,V,W),b*cc*c)
 return out

def lift(basis,col):
 out={}
 for row,(pair,I,e) in enumerate(basis):
  c=F(str(col[row]))
  if not c:continue
  charts=[]
  for E in [e[:4],e[4:]]:
   if all(x>=0 for x in E):charts.append([(i,) for i in range(4)])
   else:assert all(x<0 for x in E);charts.append([(0,1,2,3)])
  for X,Y in product(*charts):out[(pair,I,e,X,Y)]=c
 return out

def close(initial,rhs=None):
 v=initial.copy();rhs=rhs or {};trace=[]
 for step in range(5):
  residual=add(dv(v),scale(rhs,-1));trace.append(len(residual))
  if not residual:return v,trace
  assert not pc(residual),'nonzero Cech-cohomology obstruction'
  correction=scale(hc(residual),-1)
  assert correction,'nonzero residual with zero contraction'
  v=add(v,correction)
 raise AssertionError('vertical lift did not terminate')

def project(v,basis):
 # H3 projection evaluates positive factor at chart0; negative factor on top.
 idx={b:i for i,b in enumerate(basis)};M=s.zeros(len(basis),1)
 for (pair,I,e,X,Y),c in v.items():
  if len(X)+len(Y)-2!=3:continue
  if (pair,I,e) not in idx:continue
  if (all(x>=0 for x in e[:4]) and X==(0,) and all(x<0 for x in e[4:]) and Y==(0,1,2,3)) or (all(x<0 for x in e[:4]) and X==(0,1,2,3) and all(x>=0 for x in e[4:]) and Y==(0,)):
   M[idx[pair,I,e],0]+=s.Rational(c.numerator,c.denominator)
 return M

def pack(v):return [[list(pair),list(I),list(e),list(X),list(Y),str(c)] for (pair,I,e,X,Y),c in sorted(v.items())]

def calculate():
 d=json.loads((P/'partial-character-0.json').read_text());q2=d['rows']['2'];q1=d['rows']['1'];candidate=json.loads((P/'curved-koszul-diagnostic.json').read_text())
 src=t.basis(q2,-1,1);ub=t.basis(q1,0,2);target=t.basis(q1,1,2)
 A=t.decode(q2['E2_actual_ambient_Koszul_representatives']);U=t.decode(candidate['primitive']);expected=t.decode(candidate['curved_Koszul_d2_candidate'])
 blocks=q1['blocks']['1'];B=s.diag(*(t.decode(b['B']) for b in blocks));R=s.diag(*(t.decode(b['R']) for b in blocks));bb=B.columnspace();span=(s.Matrix.hstack(*bb) if bb else s.zeros(B.rows,0)).row_join(R);Q=t.decode(q1['E2_cycle_projector'])
 def endpoint(v):return Q*solve(span,project(v,target))[len(bb):,:]
 records=[];cols=[];negative=0
 for j in range(A.cols):
  aa,at=close(lift(src,A[:,j]));assert not dv(aa)
  uu,ut=close(lift(ub,U[:,j]),scale(d1(aa),-1));assert not add(dv(uu),d1(aa))
  ee=add(d1(uu),d2cor(aa));assert not dv(ee)
  assert not total(total(aa)) and not total(total(uu))
  # Exact Cech contraction on every key used, not only projected cycles.
  assert add(dc(hc(aa)),hc(dc(aa)))==add(aa,scale(pc(aa),-1))
  col=endpoint(ee);assert col==expected[:,j];cols.append(col)
  wrong=add(d1(d1(aa)),dv(d2cor(aa,True)),d2cor(dv(aa),True))
  if wrong:negative+=1
  records.append({'column':j,'source':pack(aa),'primitive':pack(uu),'endpoint':pack(ee),'source_lift_residual_nnz':at,'primitive_lift_residual_nnz':ut})
 assert negative>0,'wrong curvature sign failed to be detected'
 M=s.Matrix.hstack(*cols)
 return {'passed':True,'total_lift_equations_verified':True,'full_total_nilpotence_on_lifts':True,'wrong_curvature_sign_nonzero_columns':negative,'matrix':sparse(M),'rank':M.rank(),'traces':records,'representative_independence_complete':False,'geometric_d2_release_accepted':False,'boundary':'Actual total cocycles and primitives completed; source-boundary and arbitrary primitive-change tests still required before promotion.'}

if __name__=='__main__':
 d=calculate();text=json.dumps(d,sort_keys=True,indent=2)+'\n';out=P/'total-cech-lifts.json'
 if '--create' in a.sys.argv:
  with out.open('x') as h:h.write(text)
 else:assert out.exists() and out.read_text()==text
 print(json.dumps({k:v for k,v in d.items() if k not in ['matrix','traces']},indent=2))

