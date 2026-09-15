"""Independent saved-chain, dual-boundary, quotient and Higgs contractions."""
import serre_pairing as v
u,m,c,a,s,P,N=v.u,v.m,v.c,v.a,v.s,v.P,v.N
json,sys=u.json,u.sys
import importlib.util

def main():
 d=json.loads((P/'module-action.json').read_text());t=json.loads((P/'serre-tensor.json').read_text())
 beta=[u.unpack(b) for b in t['dual_cocycles']];h2=[u.unpack(x) for x in d['H2_low']]+[u.unpack(x['cocycle']) for x in d['H2_high']]
 src=json.loads((P.parent/'tian-yau-neutral-d4-gate/d4-chains.json').read_text());alpha=[u.unpack(r['surviving_total_cocycle']) for r in src['records']]
 charged=[u.unpack(b) for b in d['charged_basis']]
 controls={'saved_product_decompositions':0,'dual_exact_changes':0,'quotient_phase_rejected':0,'wrong_curvature_rejected':0}
 for b in beta:u.validate(b,1);assert not c.total(b)
 for h in h2:u.validate(h,2);assert not c.total(h)
 for rec in d['products']:
  image=u.unpack(rec['image']);pr=u.unpack(rec['boundary_primitive']);coord=[s.Rational(x) for x in rec['coordinates']]
  actual=u.action(alpha[rec['neutral']],charged[rec['charged']]);assert image==actual
  representative=c.add(*[c.scale(h,c.F(str(z))) for h,z in zip(h2,coord)])
  assert image==c.add(representative,c.total(pr));controls['saved_product_decompositions']+=1
 for b in beta[2:]:
  key=next(k for k in b if len(k[3])>1 or len(k[4])>1);pair,I,e,X,Y=key
  U=X if len(X)>1 else Y;offset=0 if len(X)>1 else 4;ee=list(e);ii,jj=offset+U[0],offset+U[1]
  shift=3*max(1,(-ee[ii]+2)//3);ee[ii]+=shift;ee[jj]-=shift
  eta=c.hc({(pair,I,tuple(ee),X,Y):c.F(1)});assert eta and c.total(eta);u.validate(eta,0)
  delta=c.total(eta)
  for h in h2:
   assert u.action(delta,h)==c.total(u.action(eta,h))
   assert v.residue(u.action(delta,h))==0;controls['dual_exact_changes']+=1
 # Quotient equivariance: retain bidegree but deliberately move one exponent to a different phase.
 key=next(iter(charged[0]));pair,I,e,X,Y=key;ee=list(e);ee[3]-=1;ee[0]+=1
 try:u.validate({(pair,I,tuple(ee),X,Y):c.F(1)},1)
 except AssertionError:controls['quotient_phase_rejected']+=1
 assert controls['quotient_phase_rejected']==1
 for h in h2[-2:]:
  wrong=lambda x:c.add(c.dv(x),c.d1(x),c.d2cor(x,True))
  assert wrong(h);controls['wrong_curvature_rejected']+=1
 # Exact geometric flavor map to the predecessor's gauge matrices.
 path=P.parent/'tian-yau-wilson-line-gate/interactions.py'
 spec=importlib.util.spec_from_file_location('predecessor_interactions',path);g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
 witness=g.calculate();A=[s.Matrix(g.unit(2,1)),s.Matrix(g.unit(2,2))];B=[x.T for x in A]
 traces=s.Matrix([[s.trace(x*y) for y in B] for x in A]);assert traces==s.eye(2)
 tensor=[s.Matrix(slab).applyfunc(s.Rational) for slab in t['tensor']]
 def contraction(L,R):return [s.expand(sum(traces[r,ss]*(L[:,r].T*M*R[:,ss])[0] for r in range(2) for ss in range(2))) for M in tensor]
 L=s.zeros(9,2);R=s.zeros(6,2);L[0,0]=L[1,1]=R[0,0]=R[1,1]=1
 F=contraction(L,R);assert F==[0]*4
 L2=s.zeros(9,2);R2=s.zeros(6,2);L2[5,0]=L2[7,1]=R2[1,0]=R2[0,1]=1
 F2=contraction(L2,R2);assert F2==[-1,0,-1,0]
 lv=s.Matrix(9,2,lambda i,j:s.Symbol(f'l{i}_{j}'));rv=s.Matrix(6,2,lambda i,j:s.Symbol(f'b{i}_{j}'))
 generic=contraction(lv,rv)
 support=[(n,i,j,str(M[i,j])) for n,M in enumerate(tensor) for i in range(M.rows) for j in range(M.cols) if M[i,j]]
 # Full common charged kernel: exact 5-dimensional subspace, not genericity.
 combined=s.Matrix.vstack(*[M.T for M in tensor]);ker=combined.nullspace();assert len(ker)==5
 out={'passed':True,'controls':controls,'nonzero_tensor_entries':support,'nonzero_count':len(support),'common_charged_kernel_dimension':len(ker),'common_charged_kernel_basis':[[str(x) for x in z] for z in ker],'gauge_trace_pairing':a.sparse(traces),'generic_two_pair_neutral_F':[str(x) for x in generic],'explicit_unobstructed_embedding':{'L':a.sparse(L),'Lbar':a.sparse(R),'neutral_F':[str(x) for x in F]},'explicit_obstructed_embedding':{'L':a.sparse(L2),'Lbar':a.sparse(R2),'neutral_F':[str(x) for x in F2]},'predecessor_gauge_witness':witness['two_L_plus_conjugate_pairs'],'source_hashes':{'final_controls.py':u.sha(P/'final_controls.py'),'serre-tensor.json':u.sha(P/'serre-tensor.json'),'module-action.json':u.sha(P/'module-action.json'),'../tian-yau-wilson-line-gate/interactions.py':u.sha(path)},'claim_boundary':'The old witness specifies gauge matrices but no geometric flavor basis. We exhibit and check two explicit embeddings with different F outcomes. Zero neutral F on the first embedding is cubic algebraic evidence, not a Kahler-normalized, higher-order or stabilized vacuum.'}
 f=P/'final-controls.json';payload=u.text(out)
 if '--create' in sys.argv:
  with f.open('x',newline='\n') as h:h.write(payload)
 else:assert f.is_file() and f.read_text()==payload
 print(json.dumps({k:out[k] for k in ['controls','nonzero_tensor_entries','common_charged_kernel_dimension','generic_two_pair_neutral_F']},indent=2),flush=True)
if __name__=='__main__':main()
