"""Actual relative tangent-monad deformation and geometric-neutral cubic gate.
No frozen zero tensor is differentiated. Run --create once, then immutable replay.
"""
from pathlib import Path
import sys,json,hashlib
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parent
G=P.parent
sys.path.insert(0,str(G/'tian-yau-actual-survivor-coupling-gate'))
import module_action as u
c,a,s=u.c,u.a,u.s
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
text=lambda x:json.dumps(x,sort_keys=True,indent=2)+'\n'

def inputs():
 paths=set()
 for lane,name,key in [('tian-yau-actual-survivor-coupling-gate','artifact-manifest.json','sha256'),('tian-yau-flavor-higgs-consistency-gate','release-manifest.json',None),('tian-yau-flavor-higgs-consistency-gate','source-manifest.json',None)]:
  root=G/lane; f=root/name; paths.add(f); d=json.loads(f.read_text()); d=d[key] if key else d
  for rel,h in d.items():
   q=(root/rel).resolve(); assert q.is_file() and sha(q)==h, str(q); paths.add(q)
 for lane in ['heterotic-e6-three-family-gate','tian-yau-actual-survivor-coupling-gate','tian-yau-flavor-higgs-consistency-gate','tian-yau-nonlinear-dflat-gate','tian-yau-worldsheet-instanton-gate']:
  paths.add(G/lane/'REPORT.md')
 for name in ['module-action.json','serre-tensor.json']:
  paths.add(G/'tian-yau-actual-survivor-coupling-gate'/name)
 paths.add(G/'tian-yau-nonlinear-dflat-gate/certificate.json')
 for mod in list(sys.modules.values()):
  f=getattr(mod,'__file__',None)
  if f and Path(f).is_relative_to(G) and Path(f).suffix=='.py': paths.add(Path(f))
 paths.add(Path(__file__))
 paths.update((P/'sources').glob('*.md'))
 return {str(q.relative_to(G)).replace('\\','/'):sha(q) for q in sorted(paths)}

def main():
 before=inputs()
 data=json.loads((G/'tian-yau-actual-survivor-coupling-gate/module-action.json').read_text())
 sr=json.loads((G/'tian-yau-actual-survivor-coupling-gate/serre-tensor.json').read_text())
 charged=[u.unpack(v) for v in data['charged_basis']]
 dual=[u.unpack(v) for v in sr['dual_cocycles']]
 assert len(charged)==9 and len(dual)==6
 for v in charged+dual: u.validate(v,1); assert not c.total(v)
 z=a.z; t=s.symbols('t'); F0=[p.as_expr() for p in c.polys]
 E=s.zeros(8,2)
 for i in range(8): E[i,int(i>=4)]=z[i]
 deformations=[]
 for lab in sr['charged_polynomial_labels']:
  v=[s.Integer(0)]*3
  for term in lab:
   v[term['normal_equation']]+=s.Rational(term['coefficient'])*s.prod(zz**n for zz,n in zip(z,term['monomial']))
  deformations.append(v)
 # Actual global B-valued degree-zero primitives; their boundaries are nonzero.
 bs=[]
 for i in range(8):
  ex=tuple(int(k==i) for k in range(8)); pair=(u.N,c.idx['B',i])
  b={(pair,(),ex,(j,),(k,)):c.F(1) for j in range(4) for k in range(4)}
  u.validate(b,0); assert b and c.total(b); bs.append(b)
 # A-valued primitive with one Koszul index probes the changing ideal, not J alone.
 pair=(u.N,c.idx['A',0]); ex=(-3,0,0,0,0,0,0,0)
 ks={(pair,(0,),ex,(0,),(0,)):c.F(1)}
 probes=bs+[ks]
 savedfs,savedarrows=c.fs,c.arrows
 records=[]; nilpotence=transport_nonzero=ideal_controls=0
 try:
  for mu,delta in enumerate(deformations):
   Ft=s.Matrix([f+t*d for f,d in zip(F0,delta)])
   J=Ft.jacobian(z)
   curvature=s.Matrix([[a.deg[i][b]*Ft[i] for b in range(2)] for i in range(3)])
   assert all(s.expand(x)==0 for x in J*E-curvature)
   # Differentiating the relative family changes BOTH Koszul f and Jacobian J.
   dfs=[c.mon(d) for d in delta]
   darrows=[]
   for j in range(3):
    for i in range(8):
     p=s.diff(delta[j],z[i])
     if p: darrows.append((c.idx['B',i],c.idx['C',j],c.mon(p)))
   assert darrows and any(dfs)
   def dot(v,omit_koszul=False):
    c.fs=dfs if not omit_koszul else [[],[],[]]; c.arrows=darrows
    try:return c.add(c.kap(v),c.d1(v))
    finally:c.fs=savedfs; c.arrows=savedarrows
   images=[dot(v) for v in charged]
   # The represented family is terminal-C with no outgoing arrows or Koszul index.
   assert all(not x for x in images)
   pairings=[]
   for image in images:
    row=[]
    for beta in dual:
     scalar=u.action(beta,image); assert not scalar
     # Exact scalar chain is empty, so its residue is zero in every normalization.
     row.append(str(sum(scalar.values(),c.F(0))))
    pairings.append(row)
   for v in probes:
    assert not c.total(c.total(v))
    assert not c.add(c.total(dot(v)),dot(c.total(v)))
    assert not dot(dot(v)); nilpotence+=1
    if c.add(c.total(dot(v,True)),dot(c.total(v),True)): ideal_controls+=1
   # Nontrivial exact-change transport: c'=c+D_t b, c'_dot=D_dot b.
   for b in bs:
    v=c.add(charged[0],c.total(b)); vdot=dot(b)
    assert not c.add(dot(v),c.total(vdot))
    assert not dot(vdot)
    if vdot: transport_nonzero+=1
   records.append({'complex_direction':mu,'delta_polynomials':[str(x) for x in delta],
      'Jacobian_derivative':[[int(i),int(j),str(x)] for i in range(3) for j in range(8) if (x:=s.diff(delta[i],z[j]))!=0],
      'deformed_Euler_identity':True,'action_images':[c.pack(x) for x in images],
      'U_Z_slab':pairings,'first_required_slice':[r[:2] for r in pairings[:2]]})
 finally:c.fs=savedfs;c.arrows=savedarrows
 assert ideal_controls>0 and transport_nonzero>0
 # Real tensor negative control: not all neutral-matter couplings vanish.
 nonzero=[]
 for aa,slab in enumerate(sr['tensor']):
  for i,row in enumerate(slab):
   for j,v in enumerate(row):
    if s.Rational(v):nonzero.append([aa+12,i,j,v])
 assert nonzero==[[12,5,1,'-1'],[13,6,1,'-1'],[14,7,0,'-1'],[15,8,0,'-1']]
 slab=s.Matrix([[s.Rational(sr['tensor'][aa][i][j]) for i in range(9)] for aa in range(4) for j in range(6)])
 kernel=slab.nullspace(); assert len(kernel)==5
 branch=[sum(s.Rational(sr['tensor'][aa][i][i]) for i in [0,1]) for aa in range(4)]
 assert branch==[0]*4
 # Holomorphic PQ generator d/d(Im M)=i*d/dM forbids every positive Taylor power.
 M=s.symbols('M'); pq=[str(s.diff(M**n,M)*s.I) for n in range(1,5)]
 assert all(x!='0' for x in pq)
 flavor=json.loads((G/'tian-yau-flavor-higgs-consistency-gate/certificate.json').read_text())
 assert all(s.Rational(x)==0 for x in flavor['canonical_neutral_F'])
 assert inputs()==before
 return {'passed':True,'source_hashes':before,'sympy':s.__version__,
 'inventory':{'complex_structure':9,'complexified_Kahler_including_internal_B_axions':6,'dilaton_including_universal_axion':1,'bundle_Ext1_inherited':16,'total_neutral_chiral_infinitesimal':9+6+1+16},
 'family':records,'controls':{'derivative_nilpotence_probes':nilpotence,'nonzero_exact_change_transports':transport_nonzero,'omitted_Koszul_derivative_detected':ideal_controls,'known_bundle_nonzero':nonzero,'positive_PQ_Taylor_generators':pq},
 'branch':{'geometric_Z_F':['0']*len(records),'bundle_F_inherited':flavor['canonical_neutral_F'],'bundle_common_kernel_dimension':len(kernel),'S_and_T_F':'zero by holomorphic ungauged PQ rule, not by assigned cup tensor'},
 'claim_boundary':'Actual classical relative tangent-monad derivative kills all nine charged representatives in all nine invariant complex directions; primary-sourced axion holomorphy excludes dilaton/Kahler dependence perturbatively. Supports full-neutral massless cubic F on c0,c1/beta0,beta1. Not an instanton derivative, full W, exact string vacuum, stabilized vacuum, all-orders alpha-prime cohomology count or Lean proof.'}

if __name__=='__main__':
 out=P/'certificate.json'
 if '--create' not in sys.argv: assert out.is_file(),'missing receipt; replay never creates it'
 payload=text(main())
 if '--create' in sys.argv:
  with out.open('x',encoding='utf-8',newline='\n') as f:f.write(payload)
 else: assert out.read_text(encoding='utf-8')==payload,'immutable receipt mismatch'
 d=json.loads(payload)
 print(text({k:d[k] for k in ['passed','inventory','controls','branch','claim_boundary']}))
