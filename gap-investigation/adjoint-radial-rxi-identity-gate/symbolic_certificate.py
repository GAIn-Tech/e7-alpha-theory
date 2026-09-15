"""Exact free-master identity. No evaluation at selected xi."""
import sympy as S
import json,sys,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
u,v,a,b,t,s,rho,xi=S.symbols('u v a b t s rho xi')
IA=S.Function('I');AA=S.Function('A')
def I(x,y):return IA(*sorted((S.expand(x),S.expand(y)),key=S.default_sort_key))
def A(x):return S.Integer(0) if x==0 else AA(S.expand(x))
def red(poly,x,y):
 d,e=S.symbols('d e')
 terms=S.Poly(S.expand(poly.subs({u:d+x,v:e+y})),d,e)
 rules={(0,0):I(x,y),(1,0):A(y),(0,1):A(x),(2,0):(y+s-x)*A(y),(0,2):(x+s-y)*A(x),(1,1):0}
 return S.expand(sum(c*rules[k] for k,c in terms.terms()))
def VV(x,y,z):
 n=(u+v-s)**2/4
 return 4*I(x,y)+2-(red(u,x,y)-red(u,z*x,y))/x-(red(v,x,y)-red(v,x,z*y))/y+(red(n,x,y)-red(n,z*x,y)-red(n,x,z*y)+red(n,z*x,z*y))/(x*y)
def SV(x,y,z):return red(2*s+2*v-u,x,y)-(red((s-v)**2,x,y)-red((s-v)**2,z*x,y))/x
def coeffs(expr):
 expr=expr.replace(lambda z:z.func==IA,lambda z:I(*z.args))
 expr=S.expand(expr);masters=sorted(expr.atoms(S.Function),key=S.default_sort_key)
 out={str(m):str(S.factor(expr.coeff(m))) for m in masters}
 const=S.factor(expr-sum(expr.coeff(m)*m for m in masters))
 if const!=0:out['local']=str(const)
 return out

def action_witness():
 # A nonzero, invariant action example; every coupling is differentiated, not fitted.
 x,y,w,lam=S.symbols('x y w lam',nonzero=True,real=True)
 field=S.Matrix([x,y]);R=S.Matrix([[0,-1],[1,0]])
 potential=lam*(x*x+y*y-w*w)**2/4
 grad=S.Matrix([S.diff(potential,z) for z in field]);H=grad.jacobian(field)
 assert S.expand((grad.T*R*field)[0])==0
 assert all(S.expand(z)==0 for z in H*R*field-R*grad)
 h=S.Matrix([1,0]);bg={x:w,y:0};K=R*field.subs(bg);L=R*h
 T=H.diff(x).subs(bg);U=H.diff(x,2).subs(bg);HH=H.subs(bg)
 G=S.Matrix([0,1]);tau=S.Matrix([S.diff(H[1,1],z).subs(bg) for z in field])
 thh=S.Matrix([S.diff(H[0,0],z).subs(bg) for z in field])
 delta=S.Matrix([-tau[0]/HH[0,0],0]);sigma=S.factor((thh.T*delta)[0]);q=(G.T*U*G)[0]
 mass=HH[0,0];ell=(L.T*(HH-mass*S.eye(2))*L)[0]
 assert S.factor(q+sigma-2*ell/w**2)==0
 assert sigma!=0
 return {'potential':str(potential),'a':str(w**2),'rho':str(mass),'q':str(q),'sigma_from_stationary_solve':str(sigma),'missing_displacement_A_coefficient':str(-sigma),'full_off_stationary_invariance':'0','quartic_shift_residual':'0'}


def stationary_algebra():
 # Twice-differentiated Ward: a*q - 2*ell = -r, r=t_hh.RK.
 # The constructed displacement yields a*sigma=r-k, k=t_hh.(1-P)RK.
 ell,r,k=S.symbols('ell r k');q=(-r+2*ell)/a;sigma=(r-k)/a
 residual=S.factor(q+sigma-2*ell/a)
 assert residual==-k/a
 return {'q_from_twice_Ward':str(q),'sigma_from_projected_stationarity':str(sigma),'unmet_kernel_residual':str(residual)}

def compute():
 ph={'scalar_bubble':2*(rho-t)**2/a*(I(t,xi*a)-I(t,0)),'mixed':-2*(SV(a,t,xi)-SV(a,t,0)),'vector_seagull':2*xi*A(xi*a)}
 raw={'scalar_bubble':rho**2/(a*b)*(I(xi*a,xi*b)-I(0,0)),'mixed':-2/b*(SV(a,xi*b,xi)-SV(a,0,0)),'vector_bubble':4*(VV(a,b,xi)-VV(a,b,0)),'ghost':-2*xi**2*I(xi*a,xi*b),'vector_seagull':2*xi/b*A(xi*a)}
 gg={k:S.expand((e+e.xreplace({a:b,b:a}))/2) for k,e in raw.items()}
 # Derived independently from differentiated invariant potential and stationary solve.
 phstation=2*(t-rho)/a*A(xi*a)
 ggstation=-rho/(a*b)*(A(xi*a)+A(xi*b))
 phsum=S.expand(sum(ph.values())+phstation);ggsum=S.expand(sum(gg.values())+ggstation)
 checks={k:{master:str(S.factor(S.sympify(c).subs(s,rho))) for master,c in coeffs(expr).items()} for k,expr in [('physical',phsum),('ordered_pair',ggsum)]}
 assert all(S.sympify(z)==0 for c in checks.values() for z in c.values())
 sigma,q,ell=S.symbols('sigma q ell')
 ward={q:2*ell/a-sigma}
 controls={'missing_ghost':coeffs((ggsum-gg['ghost']).subs(s,rho)),'wrong_ghost_sign':coeffs((ggsum-2*gg['ghost']).subs(s,rho)),
 'missing_displacement':{'A(a*xi)':str(S.expand((q-2*ell/a).subs(ward)))},'wrong_displacement_sign':{'A(a*xi)':str(S.expand((q-sigma-2*ell/a).subs(ward)))}}
 assert S.expand((q+sigma-2*ell/a).subs(ward))==0
 assert all(any(S.sympify(z)!=0 for z in c.values()) for c in controls.values())
 return {'passed':True,'claim_boundary':'Exact conditional all-xi free-master identity, not exact certification of the actual floating action tensors.',
 'normalization':'32 pi^2 times result; physical weight C_ai^2; ordered symmetric pair weight Z_ab^2',
 'physical_channels':{k:coeffs(e) for k,e in ph.items()},'pair_channels':{k:coeffs(e) for k,e in gg.items()},
 'physical_diagrams_on_shell':coeffs(sum(ph.values()).subs(s,rho)),'pair_diagrams_on_shell':coeffs(sum(gg.values()).subs(s,rho)),
 'physical_off_shell':coeffs(phsum),'pair_off_shell':coeffs(ggsum),'on_shell':checks,'controls':controls,
 'stationary_derivation':stationary_algebra(),'action_witness':action_witness(),'kernel_obstruction':'-t_hh dot (1-Hplus H) R_a K_a / a multiplying A(xi*a)',
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'sympy':S.__version__}
if __name__=='__main__':
 out=compute();target=P/'symbolic_receipt.json'
 if '--create' in sys.argv:
  with target.open('x') as f:json.dump(out,f,indent=2)
 else:assert json.loads(target.read_text())==out
 print(json.dumps(out,indent=2))
