import sys
sys.dont_write_bytecode=True
import unittest,json,tempfile
from pathlib import Path
import orbifold_checks as o
class Gate(unittest.TestCase):
 @classmethod
 def setUpClass(cls): cls.r=o.replay()
 def case(self,k,e=(1,1)):
  return next(c for c in self.r['cases'] if c['boundary_types']==list(k) and c['intrinsic_signs']==list(e))
 def test_complete_domain(self): self.assertEqual(len(self.r['cases']),16)
 def test_single_orbifold_full_hyper(self):
  c=self.case((1,1));self.assertEqual(c['H_charge_dimensions'],{-3:1,1:27});self.assertEqual(c['Hc_charge_dimensions'],{-3:1,1:27});self.assertEqual(c['net_27'],2)
 def test_mixed_boundary_single_27(self):
  c=self.case((0,1));self.assertEqual(c['H_charge_dimensions'],{-3:1,1:27});self.assertEqual(c['Hc_weights'],[]);self.assertEqual(c['net_27'],1)
 def test_second_sign_reverses_chirality(self):
  self.assertEqual(self.case((0,1),(1,-1))['net_27'],-1)
 def test_opposite_breaking_parities_remove_modes(self):
  c=self.case((1,1),(1,-1));self.assertEqual(c['H_weights']+c['Hc_weights'],[])
 def test_no_chiral_anomaly_free_case(self):
  for c in self.r['cases']:
   self.assertEqual(c['anomalies']['gravity_squared_X'],24*c['net_27'])
   self.assertEqual(c['anomalies']['X_cubed'],0)
 def test_gauge_and_sigma(self):
  self.assertEqual(self.case((1,1))['gauge_dimension'],79)
  self.assertEqual(self.case((1,1))['Sigma_charge_dimensions'],{-2:27,2:27})
  self.assertEqual(self.case((0,1))['Sigma_charge_dimensions'],{})
 def test_local_anomaly(self):
  self.assertEqual([z['gravity_squared_X'] for z in self.case((0,1))['endpoint_anomalies']],['0','24'])
  self.assertEqual([z['gravity_squared_X'] for z in self.case((1,1))['endpoint_anomalies']],['24','24'])
 def test_all_saved_smt_replayed(self):
  for r in self.r['smt']:
   s=o.z3.Solver();s.from_file(str(o.HERE/r['file']));self.assertEqual(str(s.check()),'unsat')
 def test_missing_receipt(self):
  with self.assertRaises(FileNotFoundError):o.replay(o.HERE/'NONEXISTENT.json')
 def test_tampered_receipt(self):
  with tempfile.TemporaryDirectory(dir=o.HERE) as d:
   p=Path(d)/'bad.json';r=json.loads(json.dumps(self.r));r['weight_count']=55;p.write_text(json.dumps(r))
   with self.assertRaises(AssertionError):o.replay(p)
 def test_negative_parity_not_cherry_pick(self):
  m,b=o.predecessor();x=list(map(int,b['X_coroot_coefficients']))
  self.assertEqual({q:{o.parity(w,x,1) for w in b['weights56'] if o.q(w,x)==q} for q in (-3,-1,1,3)},{-3:{1},-1:{-1},1:{1},3:{-1}})
if __name__=='__main__':unittest.main(verbosity=2)
