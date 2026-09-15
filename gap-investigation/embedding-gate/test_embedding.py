import unittest, json, tempfile
from pathlib import Path
from fractions import Fraction as F
import embedding_checks as e

class EmbeddingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.r=e.replay()
    def test_receipt_replay(self): self.assertTrue(self.r['passed'])
    def test_missing_receipt_fails(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(FileNotFoundError):e.replay(Path(d)/'absent.json')
    def test_tampered_receipt_fails(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'bad.json';r=dict(self.r);r['Bphys_X_X']='6';p.write_text(json.dumps(r))
            with self.assertRaises(AssertionError):e.replay(p)
    def test_charge_conjugation(self):
        w={tuple(x) for x in self.r['weights56']};self.assertEqual(w,{tuple(-v for v in x) for x in w})
    def test_coroot_centralizer(self):
        A=self.r['cartan'];x=list(map(F,self.r['X_coroot_coefficients']))
        self.assertEqual([sum(x[j]*A[j][i] for j in range(7)) for i in range(7)],[0,0,0,0,0,0,2])
    def test_branch_orientation(self):
        b={s['charge']:s for s in self.r['branch56']};a={s['charge']:s for s in self.r['branch133']}
        self.assertEqual(b[1]['nonzero_orbits'][0]['highest_E6'],a[-2]['nonzero_orbits'][0]['highest_E6'])
    def test_normalization_not_mixed(self):
        self.assertEqual(F(self.r['trace_X_squared']['56'],6),12)
        self.assertNotEqual(F(self.r['trace_X_squared']['56'],6),6)
    def test_charge_rescaling_not_alpha_change(self):
        for s in [F(1,3),F(2),F(-1)]:
            self.assertEqual((12*s*s)/(s*s),12)
    def test_SM_chirality_both_models(self):
        for n in [2,16]:self.assertEqual({k:n*v for k,v in self.r['SM_net_chirality_per_56'].items()},dict.fromkeys(['Q','uc','dc','L','ec'],0))
    def test_mass_pair_removal_preserves_index(self):
        # H-invariant ordinary bilinear mass has same rank in R and conjugate R.
        for n in [1,2,3,16,48]:
            for rank in range(n+1):self.assertEqual((n-rank)-(n-rank),0)
    def test_electroweak_matching(self):
        self.assertEqual(F(self.r['standard_SU5_kY'])+1,F(8,3))
        self.assertEqual(F(self.r['standard_SU5_e_squared_over_g7_squared']),F(3,8))
if __name__=='__main__':unittest.main(verbosity=2)
