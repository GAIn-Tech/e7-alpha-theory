"""Immutable exact replay of the invariant d4 and explicit total survivors."""
import compute as m
from pathlib import Path
import json,sys,hashlib,subprocess
c,a,s=m.c,m.a,m.s
P=Path(__file__).resolve().parent

def text(d):return json.dumps(d,sort_keys=True,indent=2)+'\n'
def unpack(rows):return {(tuple(pair),tuple(I),tuple(e),tuple(X),tuple(Y)):c.F(v) for pair,I,e,X,Y,v in rows}
def quotient(v,span,nb):return a.solve(span,m.hcoords(v,2,0))[nb:,:]
def signature(v):return sorted({(c.grade(k)[0],c.grade(k)[1]-c.grade(k)[2]) for k in v})

def calculate():
 A=m.drow(-2,3);B=m.drow(1,0);C=m.drow(0,0)
 assert B*C==s.zeros(B.rows,C.cols)
 src=A.nullspace();target,span,nb=a.quotient(s.zeros(0,B.rows),B)
 poly,_,_=a.quotient(B,C)
 assert len(src)==target.cols==4 and poly.cols==12
 qrows=json.loads((P.parent/'tian-yau-neutral-d2-gate/partial-character-0.json').read_text())['rows']
 pages={}
 for q in ['1','2']:
  r=qrows[q];d0=m.c.t.decode(r['d1'][str(r['ps'][0])]);d1=m.c.t.decode(r['d1'][str(r['ps'][1])]);dims=r['E1_dimensions'];ranks=[d0.rank(),d1.rank()]
  assert not any(d1*d0)
  e2=[dims[0]-ranks[0],dims[1]-sum(ranks),dims[2]-ranks[1]]
  pages[q]={'E1':dims,'d1_ranks':ranks,'E2':dict(zip(map(str,r['ps']),e2))}
 assert pages['1']['E2']=={'0':0,'1':60,'2':0}
 assert pages['2']['E2']=={'-2':0,'-1':60,'0':0}
 # d2 invertibility eliminates the only middle-page groups. Both possible
 # d2/d3 endpoints of (-2,3), and incoming sources to (2,0), are zero.
 d2=json.loads((P.parent/'tian-yau-neutral-d2-gate/d2-invariant-matrix.json').read_text());D=m.c.t.decode(d2['sparse']);DI=m.c.t.decode(d2['inverse'])
 assert D*DI==DI*D==s.eye(D.rows)
 records=[];cols=[];counts={'source_boundary':0,'target_vertical_boundary':0,'target_d1_boundary':0,'wrong_curvature':0,'wrong_primitive_sign':0,'nilpotence_keys':0,'cech_contraction_keys':0}
 used=set()
 for j,x in enumerate(src):
  print('derive source',j,flush=True)
  vs=[m.combine(m.classes(-2,3),x)];equations=[]
  for k in range(1,4):
   rhs=c.d1(vs[-1])
   if k>=2:rhs=c.add(rhs,c.d2cor(vs[-2]))
   u=m.primitive(c.scale(rhs,-1));assert not c.add(c.dv(u),rhs)
   equations.append({'step':k,'rhs_terms':len(rhs),'primitive_terms':len(u),'residual_terms':0})
   if rhs:
    assert c.add(c.dv(c.scale(u,-1)),rhs);counts['wrong_primitive_sign']+=1
   vs.append(u)
  end=c.add(c.d1(vs[3]),c.d2cor(vs[2]));assert not c.dv(end)
  col=quotient(end,span,nb);cols.append(col)
  # No class is declared surviving merely because a projected entry is zero.
  # Explicitly remove its target d1 boundary and vertical boundary.
  z=m.hcoords(end,2,0);bcoord=a.solve(B,z)
  gamma=m.combine(m.classes(1,0),bcoord)
  vs[3]=c.add(vs[3],c.scale(gamma,-1))
  adjusted=c.add(c.d1(vs[3]),c.d2cor(vs[2]))
  v4=m.primitive(c.scale(adjusted,-1));full=c.add(*vs,v4)
  assert not c.total(full)
  assert all(p+q==1 for p,q in signature(full))
  for v in vs+[v4,end]:
   assert not c.total(c.total(v));used.update(v)
  # Nontrivial exact source representative changes, with their entire
  # filtered total-boundary extension, on every contraction generator.
  etas=[]
  for key in vs[0]:
   eta=c.hc({key:c.F(1)})
   if eta and c.dv(eta):etas.append(eta)
  for eta in etas:
   assert not c.total(c.total(eta))
   changed=c.add(full,c.total(eta));assert not c.total(changed)
   assert m.hcoords(c.dv(eta),-2,3)==s.zeros(A.cols,1)
   counts['source_boundary']+=1
  # Wrong curvature sign must break actual source nilpotence.
  wrong=c.add(c.d1(c.d1(vs[0])),c.dv(c.d2cor(vs[0],True)),c.d2cor(c.dv(vs[0]),True))
  if wrong:counts['wrong_curvature']+=1
  # Full survivors are data for later Yoneda, not an assigned tensor.
  records.append({'column':j,'E1_source_coordinates':[str(v) for v in x],'initial_source':c.pack(vs[0]),'equations':equations,'primitives':[c.pack(v) for v in vs[1:]],'fourth_vertical_primitive':c.pack(v4),'raw_endpoint':c.pack(end),'target_boundary_coordinates':[str(v) for v in bcoord],'surviving_total_cocycle':c.pack(full),'total_D_residual_terms':0})
 M=s.Matrix.hstack(*cols)
 # Target representative controls span all sheaf H0 d1 boundaries.
 for *_,g in m.classes(1,0):
  dg=c.d1(g);assert not c.dv(dg);assert quotient(dg,span,nb)==s.zeros(target.cols,1)
  counts['target_d1_boundary']+=1
 # Every vertical-exact contraction generator appearing in a target lift.
 for rec in records:
  for key in unpack(rec['raw_endpoint']):
   beta=c.hc({key:c.F(1)})
   if beta and c.dv(beta):
    assert quotient(c.dv(beta),span,nb)==s.zeros(target.cols,1);counts['target_vertical_boundary']+=1
 # Strong keywise, not merely aggregate, identities on ALL chain supports.
 for key in sorted(used):
  v={key:c.F(1)}
  assert not c.total(c.total(v));counts['nilpotence_keys']+=1
  assert c.add(c.dc(c.hc(v)),c.hc(c.dc(v)))==c.add(v,c.scale(c.pc(v),-1));counts['cech_contraction_keys']+=1
 assert counts['wrong_curvature']>0 and counts['wrong_primitive_sign']>0
 assert counts['source_boundary']>0 and counts['target_d1_boundary']>0
 kernel=M.nullspace();assert all(M*v==s.zeros(M.rows,1) for v in kernel)
 assert M.rank()==0 and len(kernel)==4
 # Polynomial diagonal survives: its possible incoming d2 and d3 sources
 # E2(-1,1), E2(-2,2) vanish, and there is no further in-range arrow.
 return {'passed':True,'geometric_d4_computed':True,'field':'QQ','character':0,'source_bidegree':[-2,3],'target_bidegree':[2,0],'total_degree_change':[1,2],'matrix':a.sparse(M),'dense_matrix':[[str(M[i,j]) for j in range(M.cols)] for i in range(M.rows)],'rank':M.rank(),'determinant':str(M.det()),'kernel_basis':[[str(t) for t in v] for v in kernel],'kernel_dimension':len(kernel),'E1_edge_d1':{'q3':a.sparse(A),'q0_p0':a.sparse(C),'q0_p1':a.sparse(B)},'source_E1_basis':[[list(pair),q,k,col] for pair,q,k,col,_ in m.classes(-2,3)],'target_E1_basis':[[list(pair),q,k,col] for pair,q,k,col,_ in m.classes(2,0)],'target_quotient_representatives':a.sparse(target),'target_cycle_span':a.sparse(span),'target_boundary_rank':nb,'middle_pages':pages,'invariant_d2_rank':D.rank(),'E4_source_dimension':len(src),'E4_target_dimension':target.cols,'Ext1_associated_graded':{'-2,3':len(kernel),'-1,2':0,'0,1':0,'1,0':poly.cols},'invariant_Ext1_dimension':poly.cols+len(kernel),'controls':counts,'records':records,'claim_boundary':'Exact invariant hypercohomology of the declared curved-End Koszul model and explicit total degree-one survivors. No Yoneda tensor, full F-flatness, vacuum, or other-character conclusion.'}

def main():
 creating='--create' in sys.argv
 receipt=P/'receipt.json';chains=P/'d4-chains.json'
 if not creating:assert receipt.is_file() and chains.is_file(),'missing immutable artifacts'
 pre=P.parent/'tian-yau-neutral-d2-gate/verify.py'
 run=subprocess.run([sys.executable,'-B',str(pre)],capture_output=True,text=True)
 assert run.returncode==0,run.stdout+run.stderr
 out=calculate();payload=text(out)
 deps=[P/'compute.py',Path(__file__),P/'REPORT.md']
 for lane in ['tian-yau-neutral-d2-gate','tian-yau-survivor-yoneda-gate']:
  deps.extend(f for f in sorted((P.parent/lane).glob('*')) if f.suffix in ['.py','.json','.md'])
 deps.append(P.parent/'tian-yau-bundle-coupling-gate/geometry.json')
 hashes={str(f.relative_to(P.parent)).replace('\\','/'):hashlib.sha256(f.read_bytes()).hexdigest() for f in deps}
 r={k:v for k,v in out.items() if k not in ['records','E1_edge_d1','source_E1_basis','target_E1_basis','target_cycle_span','target_quotient_representatives']}
 r.update({'source_hashes':hashes,'chain_payload_sha256':hashlib.sha256(payload.encode()).hexdigest(),'canonical_predecessor_replay_exit_code':run.returncode,'interpreter':sys.executable.replace('\\','/'),'sympy_version':s.__version__})
 if creating:
  for f,t in [(chains,payload),(receipt,text(r))]:
   with f.open('x',newline='\n') as h:h.write(t)
 else:
  assert chains.read_text()==payload,'chain payload stale/tampered'
  assert receipt.read_text()==text(r),'receipt stale/tampered'
  bad=json.loads(payload);bad['dense_matrix'][0][0]='1'
  assert text(bad)!=chains.read_text(),'matrix mutation was not detected'
 print(json.dumps({k:v for k,v in r.items() if k not in ['source_hashes','middle_pages','kernel_basis']},indent=2))
if __name__=='__main__':main()
