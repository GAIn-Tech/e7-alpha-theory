import json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
p=HERE/'receipt.json'; old=json.loads(p.read_text())
assert old['passed'] and old['tree_mass_squared_over_epsilonM2']==4320
assert old['checks']['goldstone_regulator_last_two_real_difference']<1e-8
assert old['checks']['degenerate_basis_rotation_real_difference']<1e-7
assert old['checks']['quadrature_256_vs_512_last_total_abs']<2
assert abs(old['tadpole_scheme']['fermion_total_including_shift'])<1e-20
r=subprocess.run([sys.executable,'-B',str(HERE/'calculation.py')],capture_output=True,text=True)
assert r.returncode==0,r.stderr
print(json.dumps({'passed':True,'replay_exit':r.returncode,'receipt':str(p)},indent=2))
