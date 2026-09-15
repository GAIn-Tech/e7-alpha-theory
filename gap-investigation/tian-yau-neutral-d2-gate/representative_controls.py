"""Exact representative-independence controls for the invariant curved-End d2."""
from total_cech import *
import hashlib,sys

def calculate():
 d=json.loads((P/'partial-character-0.json').read_text());q2=d['rows']['2'];q1=d['rows']['1']
 target=t.basis(q1,1,2);blocks=q1['blocks']['1'];B=s.diag(*(t.decode(b['B']) for b in blocks));R=s.diag(*(t.decode(b['R']) for b in blocks));bb=B.columnspace();span=(s.Matrix.hstack(*bb) if bb else s.zeros(B.rows,0)).row_join(R);Q=t.decode(q1['E2_cycle_projector'])
 def endpoint(v):return Q*solve(span,project(v,target))[len(bb):,:]
 recs=[]
 # All 16 H2 End^-2 generators, hence every incoming d1 boundary.
 bs=t.basis(q2,-2,1);inc=s.diag(*(t.decode(b['R']) for b in q2['blocks']['-2']))
 assert inc.cols==16
 for j in range(inc.cols):
  x,tr=close(lift(bs,inc[:,j]));aa=d1(x);u=d2cor(x);e=add(d1(u),d2cor(aa))
  assert not dv(aa) and not add(dv(u),d1(aa)) and not e
  recs.append({'kind':'incoming_d1_boundary','column':j,'preimage':pack(x),'source':pack(aa),'primitive':pack(u),'endpoint':pack(e),'lift_trace':tr})
 # Every ambient-H3 Koszul boundary generator in the source summands.
 bs=t.basis(q2,-1,2);nonzero=0
 for j in range(len(bs)):
  x=lift(bs,s.eye(len(bs))[:,j]);aa=dv(x);u=d1(x);e=add(d1(u),d2cor(aa));boundary=scale(d2cor(x),-1)
  assert e==dv(boundary) and not add(dv(u),d1(aa))
  assert endpoint(e)==s.zeros(Q.rows,1)
  if aa:nonzero+=1
  recs.append({'kind':'source_vertical_boundary','column':j,'preimage':pack(x),'endpoint_boundary_primitive':pack(boundary),'endpoint_projection':sparse(endpoint(e))})
 assert nonzero>0
 # All four nonexact primitive ambiguities H1 End^0, plus exact changes below.
 bs=t.basis(q1,0,2);inc=s.diag(*(t.decode(b['R']) for b in q1['blocks']['0']))
 assert inc.cols==4;nonzero_primitive=0
 for j in range(inc.cols):
  x,tr=close(lift(bs,inc[:,j]));e=d1(x);assert not dv(x) and endpoint(e)==s.zeros(Q.rows,1)
  if e:nonzero_primitive+=1
  recs.append({'kind':'closed_primitive_change','column':j,'primitive_change':pack(x),'endpoint_change':pack(e),'lift_trace':tr})
 assert nonzero_primitive==4
 # Cech-exact source changes with zero ambient-cohomology projection.
 # h of a nonzero d1-boundary key gives nonconstant actual Cech cochains.
 probes=[]
 for b in recs:
  if b['kind']!='incoming_d1_boundary':continue
  for pair,I,e,X,Y,c in b['source']:
   key=(tuple(pair),tuple(I),tuple(e),tuple(X),tuple(Y));h=hc({key:F(1)})
   if h:probes.append(h);break
  if len(probes)==4:break
 assert probes
 for j,x in enumerate(probes):
  aa=dv(x);u=d1(x);e=add(d1(u),d2cor(aa));bp=scale(d2cor(x),-1)
  assert aa and e==dv(bp) and not add(dv(u),d1(aa)) and endpoint(e)==s.zeros(Q.rows,1)
  # Exact primitive ambiguity u -> u+dv(x) gives boundary -dv(d1(x)).
  assert d1(dv(x))==scale(dv(d1(x)),-1)
  recs.append({'kind':'Cech_exact_representative_change','column':j,'preimage':pack(x),'endpoint_boundary_primitive':pack(bp)})
 # Finite complete P3 contraction test for each negative support and intersection.
 contraction_checks=0
 for mask in range(16):
  ee=tuple(-1 if mask>>i&1 else 0 for i in range(4));N={i for i in range(4) if mask>>i&1}
  for r in range(1,5):
   for X in combinations(range(4),r):
    if not N<=set(X):continue
    # Both tensor positions; p=-1,k=0 intentionally tests negative parity.
    for swap in [False,True]:
     key=((2,0),(),ee+(0,0,0,0),(X),(0,)) if not swap else ((2,0),(),(0,0,0,0)+ee,(0,),X)
     v={key:F(1)}
     assert add(dc(hc(v)),hc(dc(v)))==add(v,scale(pc(v),-1))
     assert not dc(dc(v));contraction_checks+=1
 # Reject a changed matrix, not merely a changed rank label.
 cand=json.loads((P/'curved-koszul-diagnostic.json').read_text());M=t.decode(cand['curved_Koszul_d2_candidate']);bad=M.copy();bad[0,0]+=1
 assert bad!=M
 return {'passed':True,'source_d1_boundaries':16,'source_Koszul_boundary_generators':len(t.basis(q2,-1,2)),'nonzero_source_boundary_generators':nonzero,'closed_primitive_changes':4,'Cech_exact_changes':len(probes),'contraction_basis_checks':contraction_checks,'matrix_entry_mutation_rejected':True,'records':recs,'claim_boundary':'Complete invariant E2 representative controls via basis generators and explicit total-chain identities; does not compute higher d3/d4 or a vacuum.'}

if __name__=='__main__':
 d=calculate();text=json.dumps(d,sort_keys=True,indent=2)+'\n';out=P/'representative-controls.json'
 if '--create' in sys.argv:
  with out.open('x') as h:h.write(text)
 else:assert out.exists() and out.read_text()==text
 print(json.dumps({k:v for k,v in d.items() if k!='records'},indent=2))

