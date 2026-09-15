"""Exact two-loop implicit flow; rational certificates, not full ODE formalization."""
from pathlib import Path
from fractions import Fraction as Q
from decimal import Decimal as D, localcontext
import json, hashlib, sys, unittest
import z3
P=Path(__file__).resolve().parent

def log_bounds(q, n=55):
    q=Q(q)
    if q<=0: raise ValueError('positive log argument required')
    k=0
    while q>=2: q/=2; k+=1
    while q<1: q*=2; k-=1
    def series(r):
        z=(r-1)/(r+1); total=Q(0); power=z
        for j in range(n): total+=2*power/(2*j+1); power*=z*z
        return total,total+2*power/((2*n+1)*(1-z*z))
    lo,hi=series(q); a,b=series(Q(2))
    return (lo+k*a,hi+k*b) if k>=0 else (lo+k*b,hi+k*a)

def h_bounds(x):
    lo,hi=log_bounds(x/(1-x)); return lo-1/x,hi-1/x

def dec(q): return D(q.numerator)/D(q.denominator)
def h(x): return (x/(1-x)).ln()-1/x

def solve(x0,L):
    x0=Q(x0); L=Q(L)
    if not 0<x0<1 or L<0: raise ValueError('AF basin and IR interval required')
    if not L: return x0,x0
    with localcontext() as ctx:
        ctx.prec=85
        lo=dec(x0); hi=D(1)-D('1e-80'); target=h(lo)+dec(L)/603
        for _ in range(240):
            mid=(lo+hi)/2
            if h(mid)<target: lo=mid
            else: hi=mid
        mid=Q((lo+hi)/2); radius=Q(1,10**32)
        a,b=mid-radius,mid+radius
    assert x0<a<b<1
    h0=h_bounds(x0); ha=h_bounds(a); hb=h_bounds(b)
    assert ha[1]-h0[0]<L/603<hb[0]-h0[1], 'rational enclosure failed'
    return a,b

def f(x): return x*x*(1-x)
def obligations():
    x,y,u=z3.Reals('x y u')
    return {
      'normalized_IR_vector_field':[u==x/2412,2412*(4*u*u-9648*u*u*u)!=x*x*(1-x)/603],
      'implicit_derivative_denominator':[x>0,x<1, x*x*(1-x)*(1/x+1/(1-x)+1/(x*x))!=1],
      'AF_positive':[x>0,x<1,x*x*(1-x)<=0],
      'deficit_rate_bounds':[0<y,y<=x,x<1,z3.Or(x*x<y*y,x*x>1)],
      'jacobian_rate_bounds':[0<x,x<1,z3.Or(2*x-3*x*x < -1,2*x-3*x*x > z3.RealVal('1/3'))],
      'sensitivity_above_one_region':[0<y,y<x,x<=z3.RealVal('2/3'),x*x*(1-x)<=y*y*(1-y)],
      'separation_factorization':[x*x*(1-x)-y*y*(1-y)!=(x-y)*(x+y-x*x-x*y-y*y)]}

def payload():
    rows=[]
    for offset in ['0.01','0.1','0.5','0.9','0.99']:
        x0=1-Q(offset)
        for L in [0,1,10,100,603,1000,10000]:
            a,b=solve(x0,L)
            jl=a*a*(1-b)/f(x0); jh=b*b*(1-a)/f(x0)
            with localcontext() as ctx:
                ctx.prec=40
                linear=(-D(L)/603).exp()
                rows.append({'initial_fractional_deficit':offset,'L_ln_mu0_over_mu':L,'x_bracket':[str(a),str(b)],'J_bracket':[str(jl),str(jh)],'x_approx':str(dec((a+b)/2)),'remaining_deficit_fraction_approx':str(dec((1-(a+b)/2)/(1-x0))),'J_approx':str(dec((jl+jh)/2)),'linear_factor_approx':str(linear)})
    targets=[]
    for offset in ['0.01','0.1','0.5','0.9','0.99']:
        x0=1-Q(offset)
        for reduction in [Q(1,2),Q(1,10),Q(1,100)]:
            xf=1-(1-x0)*reduction
            a,b=h_bounds(xf); c,d=h_bounds(x0)
            lo,hi=603*(a-d),603*(b-c)
            targets.append({'initial_deficit':offset,'remaining_fraction':str(reduction),'L_bracket':[str(lo),str(hi)],'L_approx':float((lo+hi)/2),'decades_approx':float((lo+hi)/2)/float(D(10).ln())})
    return {'claim_boundary':'Scenario inputs, not observations. Rational enclosures of exact implicit two-loop flow, conditional on analytic derivation. SMT algebra only; no full ODE/QFT/EM theorem.','rows':rows,'target_reductions':targets}

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def run(write=False):
    data=payload(); checks=[]
    for name,conditions in obligations().items():
        solver=z3.Solver(); solver.set(timeout=30000); solver.add(*conditions)
        assert solver.check()==z3.unsat,name
        path=P/(name+'.smt2')
        if write: path.write_text(solver.to_smt2(),encoding='utf-8')
        else:
            replay=z3.Solver(); replay.set(timeout=30000); replay.from_file(str(path)); assert replay.check()==z3.unsat
        checks.append({'name':name,'result':'unsat','sha256':digest(path)})
    data.update(passed=True,z3_version=z3.get_version_string(),checks=checks,source_sha256=digest(P/'flow.py'))
    dest=P/'receipt.json'
    if write: dest.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    else: assert json.loads(dest.read_text())==data,'stale or missing receipt'
    print(json.dumps({'passed':True,'mode':'write' if write else 'replay_without_regeneration','rows':len(data['rows']),'SMT_checks':len(checks),'canonical':str(P)}))

class Tests(unittest.TestCase):
    def test_log_one(self): self.assertEqual(log_bounds(Q(1)),(0,0))
    def test_log_reciprocal(self):
        a,b=log_bounds(Q(7)); c,d=log_bounds(Q(1,7)); self.assertLessEqual(a+c,0); self.assertGreaterEqual(b+d,0)
    def test_log_against_decimal(self):
        with localcontext() as ctx:
            ctx.prec=100
            for q in [Q(1,1000),Q(3,2),Q(1000)]:
                a,b=log_bounds(q); self.assertLessEqual(dec(a),dec(q).ln()); self.assertGreaterEqual(dec(b),dec(q).ln())
    def test_zero_interval(self): self.assertEqual(solve(Q(1,2),0),(Q(1,2),Q(1,2)))
    def test_invalid_domain(self):
        for x,L in [(0,1),(1,1),(Q(1,2),-1)]:
            with self.assertRaises(ValueError): solve(x,L)
    def test_semigroup(self):
        a,b=solve(Q(1,2),100); c,d=solve(a,100); e,g=solve(b,100); h0,h1=solve(Q(1,2),200)
        self.assertLess(c,h1); self.assertGreater(g,h0)
    def test_sensitivity_finite_difference(self):
        x=Q(1,2); eps=Q(1,10**10); a,b=solve(x,603); c,d=solve(x+eps,603)
        numerical=(float(c+d)-float(a+b))/(2*float(eps)); exact=float(f((a+b)/2)/f(x))
        self.assertAlmostEqual(numerical,exact,places=5)
    def test_far_boundary_amplification(self):
        a,b=solve(Q(1,10),100); self.assertGreater(f(a)/f(Q(1,10)),1)
    def test_near_fixed_point_linear_lower_bound(self):
        a,b=solve(Q(99,100),603); self.assertGreater(float((1-b)/Q(1,100)),float((-D(1)).exp()))
    def test_nonzero_finite_sensitivity(self):
        a,b=solve(Q(99,100),10000); self.assertGreater(a*a*(1-b),0)
if __name__=='__main__':
    if '--test' in sys.argv: unittest.main(argv=[sys.argv[0]],verbosity=2)
    else: run('--write' in sys.argv)
