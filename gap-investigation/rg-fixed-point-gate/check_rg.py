"""Conditional perturbative E7 algebra, not a QFT or EM proof. Run --write once; default verifies saved evidence."""
from fractions import Fraction as F
from pathlib import Path
import hashlib, json, sys, unittest
import z3
P=Path(__file__).resolve().parent
CA, CF, TF = F(18), F(57,4), F(6)
def coeff(n):
    return (F(11,3)*CA-F(4,3)*TF*n,
            F(34,3)*CA**2-(4*CF+F(20,3)*CA)*TF*n,
            F(2857,54)*CA**3+(2*CF**2-F(205,9)*CF*CA-F(1415,27)*CA**2)*TF*n+(F(44,9)*CF+F(158,27)*CA)*TF**2*n*n)
def beta(a,n):
    b0,b1,_=coeff(n)
    return -2*a*a*(b0+b1*a)
def q(x): return z3.RealVal(str(x))
def obligations():
    n=z3.Int('n'); a,x,y=z3.Reals('a x y'); b0=66-8*n; b1=3672-1062*n
    return {
      'integer_IR_window': [n>=0, z3.Xor(z3.And(b0>0,b1<0),z3.And(n>=4,n<=8))],
      'no_interacting_UV': [n>=0,b0<0,b1>0],
      'one_loop_no_positive_zero': [n>=0,a>0,-2*a*a*b0==0],
      'two_loop_root_unique': [n>=4,n<=8,a>0,-2*a*a*(b0+b1*a)==0,b1*a+b0!=0],
      'IR_slope_positive': [n>=4,n<=8,a>0,b0+b1*a==0,-4*b0*a-6*b1*a*a<=0],
      'flow_below_root': [n>=4,n<=8,a>0,b0+b1*a>0,-2*a*a*(b0+b1*a)>=0],
      'flow_above_root': [n>=4,n<=8,a>0,b0+b1*a<0,-2*a*a*(b0+b1*a)<=0],
      'difference_factorization': [(-2*x*x*(2-4824*x)+2*y*y*(2-4824*y)) != (x-y)*(-4*(x+y)+9648*(x*x+x*y+y*y))],
      'finite_linear_map_injective': [a>0,x!=y,a*x==a*y],
      'normalization_products': [a>0, q(CA)*a != (2*q(CA))*(a/2)],
    }
def results():
    rows=[]
    for n in range(0,10): # bounded full integer AF domain plus first non-AF case
        b0,b1,b2=coeff(n)
        row={'Dirac_flavors':n,'b0':str(b0),'b1':str(b1),'b2_MSbar':str(b2)}
        if b0>0>b1:
            a=-b0/b1; omega=-2*b0*b0/b1
            row.update(a2=str(a),omega=str(omega),CA_a2=str(CA*a),CF_a2=str(CF*a),N_T_a2=str(n*TF*a),gamma_mass_1loop=str(6*CF*a),third_to_second_term_abs=str(abs(b2*a/b1)))
        rows.append(row)
    b0,b1,b2=coeff(8); a2=-b0/b1
    lo,hi=F(0),a2
    for _ in range(100):
        mid=(lo+hi)/2
        if b0+b1*mid+b2*mid*mid>0: lo=mid
        else: hi=mid
    return {'claim_boundary':'Exact algebra conditional on sourced perturbative coefficients. No all-orders QFT, SM matching, CODATA fit, or Lean proof claimed.', 'invariants':{'CA':str(CA),'CF':str(CF),'TF':str(TF),'dimF':56,'dimG':133},'rows':rows,'N8_a3_bracket':[str(lo),str(hi)],'N8_relative_shift_bracket':[str((a2-hi)/a2),str((a2-lo)/a2)],'N8_linear_halving_scale_ratio':'mu/mu0=2^(-603); mu^2/mu0^2=2^(-1206), for t=ln(mu); local linearized sensitivity only'}
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def certificate(write=False):
    checks=[]
    for name, expr in obligations().items():
        s=z3.Solver();s.set(timeout=30000);s.add(*expr)
        status=str(s.check()); assert status=='unsat',(name,status)
        f=P/(name+'.smt2')
        if write: f.write_text(s.to_smt2(),encoding='utf-8')
        else:
            replay=z3.Solver();replay.set(timeout=30000);replay.from_file(str(f));assert str(replay.check())=='unsat'
        checks.append({'name':name,'result':status,'sha256':digest(f)})
    files=['check_rg.py','exceptional-source.txt','beta-source.txt']
    data=results()|{'passed':True,'z3_version':z3.get_version_string(),'checks':checks,'source_hashes':{f:digest(P/f) for f in files}}
    f=P/'receipt.json'
    if write: f.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    else: assert json.loads(f.read_text())==data,'missing/stale receipt'
    print(json.dumps({'passed':True,'mode':'write' if write else 'replay_saved_without_regeneration','checks':len(checks),'canonical':str(P),'N8':data['rows'][8],'N8_a3_approx':float(F(data['N8_a3_bracket'][0])),'N8_relative_shift_approx':float(F(data['N8_relative_shift_bracket'][0]))},indent=2))
class Tests(unittest.TestCase):
    def test_trace_identity(self): self.assertEqual(CF*56,TF*133)
    def test_convention_negative_control(self): self.assertNotEqual(F(57,2)*56,TF*133)
    def test_coefficients(self):
        for n in range(10): self.assertEqual(coeff(n)[:2],(66-8*n,3672-1062*n))
    def test_weyl_conversion(self):
        for n in range(10): self.assertEqual(F(11,3)*CA-F(2,3)*TF*(2*n),coeff(n)[0])
    def test_N1_no_root(self): self.assertEqual(coeff(1)[:2],(58,2610))
    def test_N8_root(self): self.assertEqual(beta(F(1,2412),8),0)
    def test_N8_slope(self): self.assertEqual(-2*F(2)**2/F(-4824),F(1,603))
    def test_N8_third_root_bracket(self):
        lo,hi=map(F,results()['N8_a3_bracket']);b0,b1,b2=coeff(8)
        self.assertGreater(b0+b1*lo+b2*lo*lo,0);self.assertLess(b0+b1*hi+b2*hi*hi,0)
    def test_reject_false_IR(self):
        self.assertFalse(coeff(3)[0]>0>coeff(3)[1]);self.assertFalse(coeff(9)[0]>0>coeff(9)[1])
if __name__=='__main__':
    if '--test' in sys.argv: unittest.main(argv=[sys.argv[0]],verbosity=2)
    else: certificate('--write' in sys.argv)
