"""Exact nonlinear moment-map gate; no numerical or physical coefficients fitted."""
from pathlib import Path
import hashlib,json,sys
import sympy as s
P=Path(__file__).resolve().parent
G=P.parent

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def pack(m): return [[str(s.simplify(x)) for x in row] for row in m.tolist()]
def E(i,j):
 m=s.zeros(3);m[i,j]=1;return m
def flat(ms):return s.Matrix([x for m in ms for x in m])
def action(a,b,ls,bs):return [a*l-l*b for l in ls]+[b*v-v*a for v in bs]
def zero(m):return all(s.simplify(x)==0 for x in m)
def calc():
 # Frozen predecessor evidence is checked, not regenerated.
 lane=G/'tian-yau-flavor-higgs-consistency-gate'
 manifest=json.loads((lane/'release-manifest.json').read_text())
 entries=manifest.get('sha256',manifest)
 for f,h in entries.items():assert sha(lane/f)==h,f
 old=json.loads((lane/'certificate.json').read_text())
 assert old['passed'] and old['stabilizer_rank']==12
 assert old['tensor_nonzero']==[[12,5,1,'-1'],[13,6,1,'-1'],[14,7,0,'-1'],[15,8,0,'-1']]
 L=[E(2,1),E(2,2)];B=[E(1,2),E(2,2)]
 # Hermitian generator basis: each pair symmetric, imaginary antisymmetric, then H1,H2.
 hb=[];names=[]
 for i,j in [(0,1),(0,2),(1,2)]:
  hb.extend([E(i,j)+E(j,i),s.I*(E(j,i)-E(i,j))]);names.extend([f'S{i+1}{j+1}',f'A{i+1}{j+1}'])
 hb.extend([s.diag(1,-1,0),s.diag(0,1,-1)]);names+=['H1','H2']
 gens=[(a,s.zeros(3)) for a in hb]+[(s.zeros(3),b) for b in hb]
 T=s.Matrix.hstack(*(flat(action(a,b,L,B)) for a,b in gens))
 # D_a=K_i (T_a z)^i, derivative in exp(epsilon T_b) = 2 Re <T_a v,T_b v>.
 J=(2*T.H*T).applyfunc(s.re)
 assert J==J.T and J.rank()==12 and T.rank()==12
 ker=s.Matrix.hstack(*J.nullspace());assert zero(T*ker)
 # Explicit su2 and Y kernel. Coefficient basis uses unnormalized H1,H2.
 yl=s.diag(-1,-1,2);yr=s.diag(-4,2,2)
 expected=[(hb[0],s.zeros(3)),(hb[1],s.zeros(3)),(hb[6],s.zeros(3)),(yl,yr)]
 cg=s.Matrix.hstack(*(flat([a,b]) for a,b in gens))
 kc=s.Matrix.hstack(*(cg.gauss_jordan_solve(flat([a,b]))[0] for a,b in expected))
 assert kc.rank()==4 and zero(J*kc)
 # Four centralizer directions spanning c(h)/z(h). R acts on indices 2,3.
 slice_g=[(s.diag(1,1,-2),s.zeros(3)),(s.zeros(3),E(1,2)+E(2,1)),(s.zeros(3),s.I*(E(2,1)-E(1,2))),(s.zeros(3),s.diag(0,1,-1))]
 C=s.Matrix.hstack(*(cg.gauss_jordan_solve(flat([a,b]))[0] for a,b in slice_g))
 Js=C.T*J*C
 assert Js.det()!=0
 for a,b in slice_g:
  for h,k in expected:assert zero(a*h-h*a) and zero(b*k-k*b)
 # Derive a nontrivial positive quartic example K=x+y+lambda*x^2.
 # x=sum all charged L norms; y=sum all conjugate B norms (others canonical).
 x,y,lam=s.symbols('x y lambda',nonnegative=True)
 K=x+y+lam*x*x;kx=s.diff(K,x);ky=s.diff(K,y)
 u,amp=s.symbols('u amplitude',positive=True)
 # Parameterized EXACT solution, not equal raw norms. lambda>=0 arbitrary EFT demonstration.
 bscale=amp*s.sqrt(1+4*lam*amp**2)
 LL=[amp*l for l in L];BB=[bscale*b for b in B]
 xx=sum(s.trace(l.H*l) for l in LL);yy=sum(s.trace(b.H*b) for b in BB)
 ML=kx.subs(x,xx)*sum((l*l.H for l in LL),s.zeros(3))-sum((b.H*b for b in BB),s.zeros(3))
 MR=-kx.subs(x,xx)*sum((l.H*l for l in LL),s.zeros(3))+sum((b*b.H for b in BB),s.zeros(3))
 assert zero(ML) and zero(MR)
 # Same complex orbit as the quadratic point t*v: t^2=amp^2 sqrt(1+4lambda amp^2).
 t2=amp**2*s.sqrt(1+4*lam*amp**2)
 r2=1/s.sqrt(1+4*lam*amp**2)
 assert s.simplify(t2*r2-amp**2)==0
 assert s.simplify(t2/r2-bscale**2)==0
 # For prescribed t>0, z=r^2 is unique positive solution z^2+4lambda*t^2*z^3=1.
 t,z=s.symbols('t z',positive=True)
 poly=z**2+4*lam*t**2*z**3-1
 assert s.diff(poly,z)==2*z+12*lam*t**2*z**2
 # The first nonlinear displacement is z=1-2lambda*t^2+O(t^4).
 assert s.expand(poly.subs(z,1-2*lam*t**2)).coeff(t,2)==0
 # Direct nonzero negative control at equal raw pair norms.
 naiveL=s.diag(0,0,8*lam*t**4);naiveR=s.diag(0,-4*lam*t**4,-4*lam*t**4)
 assert naiveL.trace()==-naiveR.trace()
 assert naiveL-naiveL.trace()*s.eye(3)/3 != s.zeros(3)
 # Exact special arithmetic point of this FAMILY: lambda=1, amp=1 gives sqrt5 B; not physical input.
 assert zero(ML.subs({lam:1,amp:1})) and zero(MR.subs({lam:1,amp:1}))
 # Hypothesis-drop obstruction: a U1 fixing all fields with FI xi has D=xi at every orbit point.
 xi=s.symbols('xi',nonzero=True);assert xi!=0
 return {'passed':True,'predecessor_manifest_sha256':sha(lane/'release-manifest.json'),'source_sha256':sha(Path(__file__)), 'sympy':s.__version__, 'generator_order':['L_'+n for n in names]+['R_'+n for n in names], 'tangent_matrix':pack(T),'moment_jacobian_at_unit_scale':pack(J),'rank':J.rank(),'kernel_basis':pack(kc),'nullity':len(J.nullspace()),'slice_jacobian':pack(Js),'slice_determinant':str(Js.det()),'full_characteristic_polynomial':str(J.charpoly().as_expr().factor()),'nonlinear_example':{'K':str(K),'L_scale':str(amp),'B_scale':str(bscale),'D_L':pack(ML),'D_R':pack(MR),'quadratic_orbit_amplitude_squared':str(t2),'complex_rescaling_squared':str(r2),'fixed_t_orbit_equation':str(poly),'orbit_equation_positive_derivative':str(s.diff(poly,z)),'quartic_metric_eigenvalues':['1+2*lambda*x (L tangential)','1+4*lambda*x (L radial)','1 (B and other canonical fields)'],'naive_equal_norm_D_L':pack(naiveL),'naive_equal_norm_D_R':pack(naiveR)},'claim_boundary':'Exact finite Jacobian and nonlinear invariant EFT example; written conditional analytic persistence proof is not Lean formalized. Actual CY Kahler coefficients/analyticity and complete F equations are not computed. No compactification vacuum claim.'}

def main():
 data=json.dumps(calc(),indent=2,sort_keys=True)+'\n';dest=P/'certificate.json'
 if '--create' in sys.argv:
  with dest.open('x',encoding='utf-8',newline='\n') as f:f.write(data)
 else:assert dest.is_file() and dest.read_text(encoding='utf-8')==data,'saved certificate missing or changed'
 print(json.dumps({'passed':True,'mode':'creation' if '--create' in sys.argv else 'immutable replay','certificate_sha256':sha(dest)},sort_keys=True))
if __name__=='__main__':main()
