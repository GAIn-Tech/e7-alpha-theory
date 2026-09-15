import unittest,json,tempfile
from pathlib import Path
from unittest.mock import patch
import checks
class VacuumTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.r=checks.replay()
 def test_full_eft_inertia(self):
  self.assertEqual(self.r['EFT_hessian'],{'positive':120,'zero':66,'negative':0,'gauge_zero':66,'physical_zero':0})
 def test_renormalizable_physical_flats(self):
  self.assertEqual(self.r['renormalizable_hessian']['physical_zero'],11)
  self.assertEqual(self.r['unavoidable_physical_flat_lower_bound'],11)
 def test_wrong_sign_is_tachyonic(self):self.assertLess(self.r['negative_control_hessian_quadratic'],0)
 def test_representation_and_invariant_completeness(self):
  self.assertEqual(self.r['weyl_invariant_dimensions'],{'2':1,'3':0,'4':1})
  self.assertEqual(self.r['gauge_jacobian_annihilation_checks'],78)
 def test_eft_not_renormalizable(self):self.assertEqual(self.r['EFT_highest_operator_dimension'],16)
 def test_external_X_tangent(self):
  b=json.loads((checks.HERE.parent/'e6-breaking-gate/breaking-receipt.json').read_text())
  # -2H6 acts as X=-2 on BOTH singlets and commutes with Cartan A0.
  self.assertTrue(all(-2*s[5]==-2 for s in b['singlets']))
 def test_missing_receipt_rejected(self):
  with tempfile.TemporaryDirectory(dir=checks.HERE) as d:
   with self.assertRaises(FileNotFoundError):checks.replay(Path(d)/'missing.json')
 def test_tampered_receipt_rejected(self):
  with tempfile.TemporaryDirectory(dir=checks.HERE) as d:
   p=Path(d)/'bad.json';r=json.loads(json.dumps(self.r));r['EFT_hessian']['physical_zero']=1;p.write_text(json.dumps(r))
   with patch.object(checks,'compute',return_value=self.r):
    with self.assertRaises(AssertionError):checks.replay(p)
 def test_tampered_source_hash_rejected(self):
  with tempfile.TemporaryDirectory(dir=checks.HERE) as d:
   p=Path(d)/'bad.json';r=json.loads(json.dumps(self.r));r['source_hashes'][str(checks.PRE)]='0'*64;p.write_text(json.dumps(r))
   with patch.object(checks,'compute',return_value=self.r):
    with self.assertRaises(AssertionError):checks.replay(p)
if __name__=='__main__':unittest.main(verbosity=2)
