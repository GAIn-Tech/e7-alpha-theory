from fractions import Fraction
import json

def sector(n, q, R):
    # U(1) line bundle over oriented S^2: c1=n; twisted 2D Dirac index=q*n.
    # A representative round-sphere flux has F_{theta phi}=(n/2) sin(theta),
    # hence integral F/(2*pi)=n independent of R. Maxwell integral scales n^2/R^2
    # up to a common convention-dependent positive prefactor.
    return {"n": n, "q": q, "R": str(R),
            "flux_over_2pi": n, "dirac_index": q*n,
            "orientation_reversed_index": -q*n,
            "maxwell_scaling": str(Fraction(n*n, R*R))}

cases=[sector(3,1,1),sector(3,1,2),sector(4,1,1),sector(3,2,1)]
assert cases[0]["flux_over_2pi"] == cases[1]["flux_over_2pi"] == 3
assert cases[0]["maxwell_scaling"] != cases[1]["maxwell_scaling"]
assert cases[0]["dirac_index"] == 3 and cases[0]["orientation_reversed_index"] == -3
assert cases[2]["dirac_index"] == 4
assert cases[3]["dirac_index"] == 6
receipt={"passed":True,"cases":cases,"claim_boundary":"Exact topology/algebra example: integral flux fixes c1 and the twisted Dirac index q*n, but does not by itself fix the continuous radius or action extremum. Family count depends on charge, representation multiplicity, projection, and orientation; primality is neither necessary nor sufficient."}
print(json.dumps(receipt,indent=2))
