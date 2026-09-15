"""Actual End(K) d1 on H1 via exact ambient Koszul quotient representatives."""
from exact_audit import *
@lru_cache(None)
def space(a,b,ch):
 bases={}
 for k in range(4):
  for I in combinations(range(3),k):
   q,es=ambient(a-sum(deg[i][0] for i in I),b-sum(deg[i][1] for i in I))
   if q==3:
    for e in es:
     if sum(t*v for t,v in zip(e,w))%3==ch:bases.setdefault(k,[]).append((I,e))
 def matrix(k):
  dom=bases.get(k,[]);cod=bases.get(k-1,[]);idx={t:i for i,t in enumerate(cod)};M=s.zeros(len(cod),len(dom))
  for j,(I,e) in enumerate(dom):
   for t,i in enumerate(I):
    for mon,c in f[i]:
     key=(I[:t]+I[t+1:],tuple(u+v for u,v in zip(e,mon)))
     if key in idx:M[idx[key],j]+=(-1)**t*c
  return M
 D=matrix(2);B=matrix(3);assert D*B==s.zeros(D.rows,B.cols)
 N=D.nullspace();bound=B.columnspace();span=s.Matrix.hstack(*bound) if bound else s.zeros(D.cols,0);reps=[]
 for v in N:
  if span.row_join(v).rank()>span.cols:reps.append(v);span=span.row_join(v)
 R=s.Matrix.hstack(*reps) if reps else s.zeros(D.cols,0)
 assert len(reps)==line(a,b)[1][ch]
 return bases.get(2,[]),R,span,len(bound)

def run():
 terms=[]
 for name,p in [('A',-1),('B',0),('C',1)]:
  for i,d in enumerate(G[name]):terms.append((name,i,p,d,w[i] if name=='B' else 0))
 idx={(a[0],a[1]):i for i,a in enumerate(terms)}
 arrows=[]
 for i in range(8):arrows.append((idx['A',int(i>=4)],idx['B',i],z[i]))
 fs=[s.sympify(t,locals=dict(zip(G['variables'],z))) for t in G['polynomials']]
 for a in range(3):
  for i in range(8):
   q=s.diff(fs[a],z[i])
   if q:arrows.append((idx['B',i],idx['C',a],q))
 allrec=[]
 for ch in range(3):
  blocks={}
  for i,a in enumerate(terms):
   for j,b in enumerate(terms):
    p=b[2]-a[2];d=tuple(v-u for u,v in zip(a[3],b[3]));lc=(ch-a[4]+b[4])%3
    sp=space(*d,lc)
    if sp[1].cols:blocks.setdefault(p,[]).append(((i,j),sp))
  mats={}
  for p in [0,1]:
   src=blocks.get(p,[]);dst=blocks.get(p+1,[]);nr=sum(v[1].cols for _,v in dst);nc=sum(v[1].cols for _,v in src);M=s.zeros(nr,nc)
   ro={};offset=0
   for pair,sp in dst:ro[pair]=(offset,sp);offset+=sp[1].cols
   col=0
   for (i,j),sp in src:
    for aa,bb,poly in arrows:
     targets=[]
     if aa==j:targets.append(((i,bb),1))
     if bb==i:targets.append(((aa,j),-(-1)**p))
     for pair,sign in targets:
      if pair not in ro:continue
      off,dp=ro[pair];index={v:n for n,v in enumerate(dp[0])};mult=s.zeros(len(dp[0]),len(sp[0]))
      for c,(I,e) in enumerate(sp[0]):
       for mon,coef in s.Poly(poly,*z).terms():
        key=(I,tuple(u+v for u,v in zip(e,mon)))
        if key in index:mult[index[key],c]+=sign*coef
      image=mult*sp[1]
      # Actual representative control: every source Koszul boundary maps
      # into target boundaries, hence has zero target cohomology coordinates.
      boundary_image=mult*sp[2][:,:sp[3]]
      if sp[3]:
       boundary_sol=dp[2].gauss_jordan_solve(boundary_image)[0]
       assert boundary_sol[dp[3]:,:]==s.zeros(dp[1].cols,sp[3])
      sol=dp[2].gauss_jordan_solve(image)[0]
      projected=sol[dp[3]:,:]
      M[off:off+projected.rows,col:col+sp[1].cols]+=projected
    col+=sp[1].cols
   mats[p]=M
  assert mats[1]*mats[0]==s.zeros(mats[1].rows,mats[0].cols)
  dims=[sum(sp[1].cols for _,sp in blocks.get(p,[])) for p in [0,1,2]];ranks=[mats[p].rank() for p in [0,1]]
  e2=[dims[0]-ranks[0],dims[1]-sum(ranks),dims[2]-ranks[1]]
  allrec.append({'character':ch,'q1_E1_dimensions':dims,'q1_d1_ranks':ranks,'q1_E2_dimensions':e2,'q2_E2_dimensions_by_p_minus2_minus1_0':'Serre dual of opposite-character q1 E2 in reverse order','matrices':{str(p):{'shape':list(M.shape),'entries':[[i,j,str(M[i,j])] for i in range(M.rows) for j in range(M.cols) if M[i,j]]} for p,M in mats.items()}})
 return {'passed':True,'records':allrec,'source_hashes':{q.name:hashlib.sha256(q.read_bytes()).hexdigest() for q in [Path(__file__),P/'exact_audit.py']},'scope':'Exact End d1 on sheaf H1 and Serre-dual H2; higher dr and full Yoneda not computed.'}
if __name__=='__main__':
 d=run();text=json.dumps(d,sort_keys=True,indent=2)+'\n';out=P/'q1-certificate.json'
 if '--create' in sys.argv:
  with out.open('x') as h:h.write(text)
 else:assert out.exists() and out.read_text()==text
 print(json.dumps([{k:v for k,v in t.items() if k!='matrices'} for t in d['records']],indent=2))

