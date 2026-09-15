"""Investigate the curved ambient Koszul correction; diagnostic until comparison proved."""
import partial_chains as a
from partial_chains import s,json,Path,P,sparse,solve

def decode(d):
 M=s.zeros(*d['shape'])
 for i,j,v in d['entries']:M[i,j]=s.Rational(v)
 return M

def basis(row,p,k):
 return [(tuple(b['pair']),tuple(I),tuple(e)) for b in row['blocks'][str(p)] for I,e in b['bases'].get(str(k),[])]
def remap(src,dst):
 idx={t:i for i,t in enumerate(dst)};M=s.zeros(len(dst),len(src))
 for j,t in enumerate(src):
  assert t in idx;M[idx[t],j]=1
 return M

def calculate():
 d=json.loads((P/'partial-character-0.json').read_text());q2=d['rows']['2'];q1=d['rows']['1']
 A=decode(q2['E2_actual_ambient_Koszul_representatives']);U=decode(q2['first_projected_Koszul_primitive'])
 src=basis(q2,-1,1);us=basis(q2,0,2);ut=basis(q1,0,2);dst=basis(q1,1,2)
 # Some k1 summands vanish but have nonzero k2 boundaries. Embed existing primitive.
 T=remap(us,ut);U=T*U
 end=decode(q1['raw_End']['0'])*U
 # H_a:A_b -> C_a has constant coefficient degree[a][b].
 terms=[]
 for name,p in [('A',-1),('B',0),('C',1)]:
  for i,dd in enumerate(a.G[name]):terms.append((name,i,p,dd))
 idx={(t[0],t[1]):i for i,t in enumerate(terms)}
 H=[(idx['A',b],idx['C',aa],aa,a.deg[aa][b]) for aa in range(3) for b in range(2) if a.deg[aa][b]]
 target={v:i for i,v in enumerate(dst)};W=s.zeros(len(dst),len(src))
 for j,((i,t),I,e) in enumerate(src):
  for aa,bb,fi,coef in H:
   if fi in I:continue
   J=tuple(sorted((fi,)+I));wsg=(-1)**sum(x<fi for x in I)
   for pair,sign in ([((i,bb),1)] if aa==t else [])+([((aa,t),-1)] if bb==i else []):
    key=(pair,J,e)
    if key in target:W[target[key],j]-=wsg*sign*coef
 end+=W*A
 blocks=q1['blocks']['1'];D=s.diag(*(decode(b['D']) for b in blocks));B=s.diag(*(decode(b['B']) for b in blocks));R=s.diag(*(decode(b['R']) for b in blocks))
 assert D*end==s.zeros(D.rows,end.cols),'endpoint not Koszul closed'
 bb=B.columnspace();span=(s.Matrix.hstack(*bb) if bb else s.zeros(B.rows,0)).row_join(R)
 sol=solve(span,end);coords=sol[len(bb):,:]
 assert decode(q1['d1']['1'])*coords==s.zeros(decode(q1['d1']['1']).rows,coords.cols),'not d1 closed'
 M=decode(q1['E2_cycle_projector'])*coords
 return {'diagnostic_only':True,'comparison_to_geometric_d2_proved':False,'curved_Koszul_d2_candidate':sparse(M),'rank':M.rank(),'primitive':sparse(U),'correction':sparse(W),'endpoint':sparse(end),'target_E1_coordinates':sparse(coords),'endpoint_Koszul_closed':True,'endpoint_d1_closed':True}
if __name__=='__main__':
 d=calculate();print(json.dumps({k:v for k,v in d.items() if k not in ['curved_Koszul_d2_candidate','primitive','correction','endpoint','target_E1_coordinates']},indent=2))
 with (P/'curved-koszul-diagnostic.json').open('x') as h:json.dump(d,h,indent=2,sort_keys=True)

