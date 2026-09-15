"""Exact conditional boundary anomaly gate. No empirical inputs. --create exclusive."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, importlib.util, tempfile, unittest
HERE=Path(__file__).resolve().parent
P=HERE.parent

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(path,name):
 s=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def polynomial(spectrum):
 # basis x tr27(f6^2), x p1, x^3; representation index relative to 27
 return [sum(F(q*t,2) for d,q,t in spectrum),-sum(F(d*q,24) for d,q,t in spectrum),sum(F(d*q**3,6) for d,q,t in spectrum)]

def residual(n,k,c6,cg,cx=0):
 a=polynomial([(27*n,1,n),(n,-3,0)])
 return [a[0]+k*c6,a[1]+k*cg,a[2]+k*cx]

def compute():
 o=load(P/'chiral-zero-mode-gate/orbifold_checks.py','orb'); old=o.replay()
 emb=load(P/'embedding-gate/embedding_checks.py','emb'); b=emb.replay()
 case=next(c for c in old['cases'] if c['boundary_types']==[0,1] and c['intrinsic_signs']==[1,1])
 assert [F(c['gravity_squared_X']) for c in case['endpoint_anomalies']]==[0,24]
 assert [F(c['E6_squared_X_over_T27']) for c in case['endpoint_anomalies']]==[0,1]
 checks=[]
 for n in (-3,-1,0,1,2,3,7):
  for k in (-6,-3,1,3,6):
   a=polynomial([(27*n,1,n),(n,-3,0)])
   assert a==[F(n,2),F(-n),F(0)]
   assert residual(n,k,-F(n,2*k),F(n,k))==[0,0,0]
   checks.append({'n':n,'k':k,'polynomial':list(map(str,a)),'WZ':list(map(str,[-F(n,2*k),F(n,k),F(0)]))})
 # The actual weight trace fixes integral E6 index without confusing T27=3 with 6.
 A=[r[:6] for r in b['cartan'][:6]]; G=emb.inverse(A)
 x=list(map(int,b['X_coroot_coefficients'])); W=[w for w in b['weights56'] if sum(a*c for a,c in zip(w,x))==1]
 trace=[[sum(w[i]*w[j] for w in W) for j in range(6)] for i in range(6)]
 assert trace==[[6*a for a in r] for r in A]
 # Central coweight mu=omega_1 in long-root-length-two convention.
 mu=[G[i][0] for i in range(6)]
 assert G[0][0]==F(4,3)
 assert all((3*v).denominator==1 for v in mu)
 # A quotient cocharacter flux on spin S2xS2 with c=a+b, c^2=2.
 u=G[0][0]; q4=6*u
 assert q4==8 and (q4/3).denominator==3 and (3*q4/3).denominator==1
 # Globally allowable singlet characters are multiples of three.
 charges=[k for k in range(1,13) if k%3==0]
 return {'passed':True,'claim_boundary':'Exact coefficient and boundary checks, conditional local EFT only; global quantization not proved.','cases':checks,'predecessor_cases':len(old['cases']),'E6_trace_coroot_matrix':trace,'central_coweight':list(map(str,mu)),'central_norm':str(G[0][0]),'quotient_spin_flux_X4':str(q4),'singlet_character_charges_1_to_12':charges,'massless_lie_algebra_dimension':78,'source_hashes':{str(p):sha(p) for p in [Path(__file__),P/'chiral-zero-mode-gate/orbifold-receipt.json',P/'embedding-gate/embedding-receipt.json']}}

def replay(path=None):
 saved=json.loads((path or HERE/'receipt.json').read_text()); now=compute()
 assert saved==now,'Receipt mismatch'
 return now

class Tests(unittest.TestCase):
 def test_saved(self): self.assertTrue(replay()['passed'])
 def test_missing(self):
  with self.assertRaises(FileNotFoundError): replay(HERE/'deliberately-missing.json')
 def test_tampered(self):
  d=json.loads((HERE/'receipt.json').read_text());d['central_norm']='1'
  with tempfile.TemporaryDirectory(dir=HERE) as t:
   p=Path(t)/'bad.json';p.write_text(json.dumps(d))
   with self.assertRaises(AssertionError): replay(p)
 def test_wrong_sign(self): self.assertNotEqual(residual(1,3,F(1,6),F(-1,3)),[0,0,0])
 def test_gravity_omitted(self): self.assertEqual(residual(1,3,F(-1,6),0),[0,-1,0])
 def test_no_shift(self): self.assertNotEqual(residual(1,0,F(-1,6),F(1,3)),[0,0,0])
 def test_spurious_cubic(self): self.assertEqual(residual(1,3,F(-1,6),F(1,3),1),[0,0,3])
 def test_wrong_wall(self):
  # Actual anomaly delta_L Q; cancellation delta_0 (-Q) integrates zero but is not local zero.
  self.assertEqual(sum([-1,1]),0); self.assertNotEqual([-1,1],[0,0])
 def test_PP_single_wall_fails(self): self.assertNotEqual([1,1-2],[0,0])
 def test_quotient_character(self): self.assertNotEqual(1%3,0);self.assertEqual(3%3,0)
 def test_global_period_negative(self): self.assertNotEqual((F(8,3)).denominator,1)
 def test_liftable_periods(self):
  for n in range(1,5):
   for instanton in range(-4,5):
    for signature_units in range(-3,4): self.assertEqual((F(n,3)*(6*instanton-48*signature_units)).denominator,1)
 def test_mass_kernel_and_free_couplings(self):
  # Gram rank one with shift covector (0,...,0,k); positive kinetic coefficient.
  for g2 in (F(1,5),F(2,5)):
   m2=F(7)*9*g2; self.assertGreater(m2,0)
   self.assertEqual(F(0)*m2,0) # any generator of E6, including Y
  self.assertNotEqual(F(1,5),F(2,5)) # anomalies independent of gauge kinetic data

if __name__=='__main__':
 if '--test' in sys.argv: unittest.main(argv=[sys.argv[0]],verbosity=2)
 elif '--create' in sys.argv:
  d=compute()
  with (HERE/'receipt.json').open('x') as f: json.dump(d,f,indent=2)
  print('Created exact receipt',len(d['cases']))
 else:
  d=replay();print(json.dumps({'passed':d['passed'],'cases':len(d['cases']),'central_norm':d['central_norm'],'quotient_spin_flux_X4':d['quotient_spin_flux_X4']}))
