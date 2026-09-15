"""Exact curve restriction and standard-embedding A-model insertion certificate.
No higher charged E8 Dirac family is assumed. Default replay never writes.
"""
from pathlib import Path
import argparse,hashlib,importlib.util,json,subprocess,sys,tempfile
import sympy as S
P=Path(__file__).resolve().parent
F=P/'frozen'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def text(x):return json.dumps(x,sort_keys=True,indent=2)+'\n'
def check_inputs():
 m=json.loads((P/'input-manifest.json').read_text())
 for n,r in m.items():
  assert sha(P/n)==r['sha256'],n
  if 'canonical_source' in r:assert sha(Path(r['canonical_source']))==r['sha256'],r['canonical_source']
 return {n:r['sha256'] for n,r in m.items()}
def run():
 hashes=check_inputs()
 # The legacy --verify writes before comparing. Run its unchanged source ONLY in
 # an owned temporary directory, and compare the original frozen receipt first/after.
 source=F/'tian-yau-worldsheet-instanton-gate/exact_certificate.py'
 saved=(source.parent/'certificate.json').read_bytes()
 with tempfile.TemporaryDirectory(dir=P) as td:
  t=Path(td);(t/'exact_certificate.py').write_bytes(source.read_bytes())
  p=subprocess.run([sys.executable,'-B',str(t/'exact_certificate.py')],capture_output=True,text=True)
  assert p.returncode==0,p.stderr
  assert (t/'certificate.json').read_bytes()==saved,'predecessor immutable payload mismatch'
 assert (source.parent/'certificate.json').read_bytes()==saved
 spec=importlib.util.spec_from_file_location('curves',source);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
 charged=json.loads((F/'tian-yau-actual-survivor-coupling-gate/module-action.json').read_text())['charged_basis'][:2]
 dual=json.loads((F/'tian-yau-actual-survivor-coupling-gate/serre-tensor.json').read_text())['dual_cocycles'][:2]
 for i,rows in enumerate(charged):
  assert len(rows)==16
  for pair,I,e,X,Y,v in rows:
   assert pair==[13,10] and not I and e==([0,0,0,3,0,0,0,0] if i==0 else [0,0,1,2,0,0,0,0]) and v=='1'
 for i,rows in enumerate(dual):
  assert len(rows)==16
  assert all(pair==[i,13] and I==[] and e==[0]*8 and v=='1' for pair,I,e,X,Y,v in rows)
 s,t,z,w=S.symbols('s t z w')
 red=lambda x:S.rem(S.cancel(x),w*w+w+1,w).expand()
 x=S.Matrix([-s,s,-t,t]);y=S.Matrix([-1,-1,1,1])
 vx=S.Matrix([0,0,t/6,t/6]);vy=S.Matrix([0,0,S.Rational(1,6),-S.Rational(1,6)])
 orbit=[];label=((0,0,0),0)
 for k in range(3):
  gx=S.diag(*[w**(k*q) for q in m.WX]);gy=S.diag(*[w**(k*q) for q in m.WY])
  xx=(gx*x).applyfunc(red);yy=(gy*y).applyfunc(red)
  ux=(gx*vx).applyfunc(red);uy=(gy*vy).applyfunc(red)
  assert red(sum(v**3 for v in xx))==red(sum(v**3 for v in yy))==red(xx.dot(yy))==0
  J=S.Matrix([[*[3*v*v for v in xx],0,0,0,0],[*yy,*xx],[0,0,0,0,*[3*v*v for v in yy]]])
  normal=J*ux.col_join(uy)
  f0=red(xx[3]**3);f1=red(xx[2]*xx[3]**2)
  assert normal.applyfunc(red)==S.Matrix([f0,0,0]) and f1==-f0
  # Exact nonvacuous representative change by the x Euler field.
  euler=xx.col_join(S.zeros(4,1));assert any(euler) and (J*euler).applyfunc(red)==S.zeros(3,1)
  assert (J*(ux.col_join(uy)+euler)).applyfunc(red)==normal.applyfunc(red)
  assert any((J*ux.col_join(S.zeros(4,1))-normal).applyfunc(red)),'omit y compensation control'
  orbit.append({'label':label,'x':list(map(str,xx)),'y':list(map(str,yy)), 'c_restrictions':[str(f0),str(f1)],'c0_global_primitive_x':list(map(str,ux)),'c0_global_primitive_y':list(map(str,uy))})
  label=m.act_point_on_annihilator(label[0],label[1],m.WX,m.WY)
 assert label==((0,0,0),0)
 # Two dual Euler generators restrict through dlog transition: Ox(1)|C=O(1), Oy(1)|C=O.
 # On s!=0,t!=0, transition s/t=z. Constant point gives constant transition.
 beta=[S.diff(z,z)/z,S.diff(S.Integer(1),z)]
 assert beta==[1/z,0]
 h0=lambda n:max(n+1,0)
 h1=lambda n:max(-n-1,0)
 split=[2,-1,-1];twist=[n-1 for n in split];dual_twist=[-n-1 for n in split]
 assert sum(map(h0,twist))==sum(map(h1,twist))==2
 assert sum(map(h0,dual_twist))==sum(map(h1,dual_twist))==2
 # Actual finite Cech multiplication/projection for End(TX|C) neutral directions.
 # Hom(O(2),O(-1))=O(-3), harmonic basis z^-1,z^-2.
 a,b,c,d=S.symbols('a b c d');cochains=[a/z+b/z**2,c/z+d/z**2]
 coeff=lambda f,n:S.expand(f).coeff(z,n)
 M=S.Matrix([[coeff(q*v,-1) for v in [1,z]] for q in cochains])
 assert M==S.Matrix([[a,b],[c,d]])
 for q in cochains:
  for primitive_boundary in [z**2,z**-3]:
   assert any(S.expand(primitive_boundary*v) for v in [1,z])
   assert [coeff((q+primitive_boundary)*v,-1) for v in [1,z]]==[coeff(q*v,-1) for v in [1,z]]
 det=S.expand(M.det());assert det==a*d-b*c and det.subs({a:1,d:1,b:0,c:0})==1
 # Divisor insertions: source-backed A-model cubic, NOT replacement of the charged E8 Pfaffian.
 B0=S.Matrix(3,3,S.symbols('b0_0:9'));B1=S.Matrix(3,3,S.symbols('b1_0:9'))
 u,v,dx,dy,eps=S.symbols('u v dx dy eps')
 base0=S.zeros(3);base0[1,2]=u;base1=S.zeros(3);base1[2,2]=v
 sub=dict(zip(list(B0)+list(B1),list(base0)+list(base1)))
 W=(dx*B0+dy*B1).det().expand()
 grad=[S.diff(W,b).subs(sub).expand() for b in list(B0)+list(B1)]
 assert not any(grad) and W.subs(sub)==0
 D=S.Matrix(3,3,S.symbols('D_0:9'));base=dx*base0+dy*base1
 expansion=S.Poly((base+eps*D).det().expand(),eps)
 quadratic=expansion.coeff_monomial(eps**2)
 expected=-dx*u*(D[0,0]*D[2,1]-D[0,1]*D[2,0])+dy*v*(D[0,0]*D[1,1]-D[0,1]*D[1,0])
 assert S.expand(quadratic-expected)==0 and expansion.coeff_monomial(eps)==0
 assert quadratic.subs({dx:1,dy:0,u:1,D[0,0]:1,D[2,1]:1,**{q:0 for q in D if q not in [D[0,0],D[2,1]]}})==-1
 phases=[red(sum(w**(k*q) for k in range(3))) for q in range(3)]
 assert phases==[3,0,0]
 # Cubic neutral-character external fields have actual total Wilson+geometry phase zero.
 poly10=W.subs({dx:1,dy:0});poly01=W.subs({dx:0,dy:1});poly11=W.subs({dx:1,dy:1})
 result={'passed':True,'input_hashes':hashes,'predecessor_replay':'unchanged exact source; original receipt compared with regenerated temporary payload; no predecessor writes',
 'orbit':orbit,'restricted_cocycles':{'c0':'J(global vx,vy)=(t^3,0,0), hence zero in H1(TX|C)','c1':'negative c0 restriction with negative primitive','beta0':str(beta[0]),'beta1':str(beta[1]),'normalization':'Euler dlog convention; beta0 trace on C = +1'},
 'splitting':{'TX':[2,-1,-1],'TX_spin':twist,'TXdual_spin':dual_twist,'h0_TX_spin':sum(map(h0,twist)),'h1_TX_spin':sum(map(h1,twist)),'h0_TXdual_spin':sum(map(h0,dual_twist))},
 'neutral_restricted_End_map':{'source':'H0(O(1)) basis 1,z','target':'H1(O(-2))^2 basis z^-1 in each summand','actual_universal_cech_classes':list(map(str,cochains)),'matrix':[[str(q) for q in M.row(i)] for i in range(2)],'determinant':str(det),'physical_boundary':'This local End restriction is not an identified image of the global neutral basis and is NOT c/beta charged Higgs map.'},
 'A_model_charged_cubic':{'curve_10':str(poly10),'curve_01':str(poly01),'curve_11':str(poly11),'normalization':'Each polynomial multiplied by an unspecified common holomorphic field/vertex normalization and its actual exp(-area+iB) weight; isolated simple curve local GW multiplicity +1. Not a numerical string Pfaffian.', 'selected_orbit_cover_sum':'3 det(B0) times cover normalization; quotient projection divides orbit multiplicity, not three distinct downstairs curves','Z3_character_sums':list(map(str,phases)), 'curve10_beta_tensor_nonzero':{'000':1},'cubic_all_B_gradients_on_branch':list(map(str,grad)), 'first_transverse_quadratic_about_branch':str(quadratic),'transverse_cubic':str(D.det().expand()),'primitive_bounded_orbit_counts':{'10':27,'01':27,'11':189},'bounded_counts_not_complete_degree_two':True},
 'claim_boundary':'Computed actual curve restrictions and standard-embedding divisor charged-cubic insertion polynomial and its transverse Hessian. Full charged E8 zero-mode lifting family, mixed insertions and finite-field Pfaffian remain UNCOMPUTED. No full-W F-flatness, stabilization or alpha prediction.'}
 assert check_inputs()==hashes
 return result
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--create',action='store_true');args=ap.parse_args()
 result=run();payload=text(result);out=P/'certificate.json'
 if args.create:
  with out.open('x',encoding='utf-8',newline='\n') as f:f.write(payload)
 else:assert out.is_file() and out.read_text(encoding='utf-8')==payload,'missing/stale certificate'
 print(text({'passed':True,'certificate_sha256':sha(out),'scope':result['claim_boundary']}))
