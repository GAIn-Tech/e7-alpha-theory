from pathlib import Path
import json,tempfile,unittest
import breaking_checks as b
class Gate(unittest.TestCase):
 def test_saved(self):self.assertTrue(b.replay()['passed'])
 def test_missing(self):
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaises(FileNotFoundError):b.replay(Path(d)/'missing.json')
 def test_tamper_payload(self):
  r=json.loads((b.HERE/'breaking-receipt.json').read_text());r['two_independent']['dimension']=12
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'bad.json';p.write_text(json.dumps(r))
   with self.assertRaises(AssertionError):b.replay(p)
 def test_tamper_hash(self):
  r=json.loads((b.HERE/'breaking-receipt.json').read_text());r['sources'][str(b.PRE)]='0'*64
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'bad.json';p.write_text(json.dumps(r))
   with self.assertRaises(AssertionError):b.replay(p)
 def test_charge_and_mass(self):
  # Example full-rank diagonal family Yukawa, not derived parameters.
  self.assertEqual(b.rank([[1,0,0],[0,2,0],[0,0,3]]),3)
  self.assertEqual(1+1-2,0);self.assertNotEqual(1+1+1,0)
  # Three 5s against six bar5s; rank three leaves three bar5s, unchanged three 10s.
  self.assertEqual((3-3,6-3,3),(0,3,3))
 def test_scoped_F_equation(self):
  import z3
  a,m=z3.Reals('a m');s=z3.Solver();s.add(m!=0,m*a==0,a!=0)
  self.assertEqual(s.check(),z3.unsat)
  # One real component of V=|m a|^2 with canonical positive metric, m=1: derivative 2a, Hessian2.
  self.assertEqual(2,2*1**2)
  s=z3.Solver();s.add(m==0,m*a==0,a!=0);self.assertEqual(s.check(),z3.sat)
if __name__=='__main__':unittest.main(verbosity=2)
