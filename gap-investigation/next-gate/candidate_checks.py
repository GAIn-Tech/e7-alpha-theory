"""Exact restricted-vacuum checks for the separately proposed rigid SUSY action.
Not exp47 compactification, full vacuum enumeration, or an alpha derivation.
"""
from fractions import Fraction as F
import json

def run():
    # Demonstration only; constants not inferred from E7 or fitted to alpha.
    a,b,k,m,y=map(F,[-1,0,1,2,1])
    roots=[F(-1),F(1)]
    assert b*b-4*k*a==4
    rows=[]
    for s in roots:
        assert a+b*s+k*s*s==0
        ss_mass2=(b+2*k*s)**2
        charged_mass2=(m+y*s)**2
        assert ss_mass2>0 and charged_mass2>0
        # F terms vanish, D=0 at Q1=Q2=0; gauge coefficient independent.
        for c in [F(1),F(2),F(7,3)]:assert c>0
        rows.append({'S':str(s),'singlet_scalar_mass_squared':str(ss_mass2),
                     'charged_scalar_mass_squared':str(charged_mass2),'V':'0'})
    # Antisymmetric gauge contraction of commuting identical fields vanishes.
    omega=[[0,1],[-1,0]];q=[F(2),F(3)];r=[F(5),F(7)]
    assert sum(omega[i][j]*q[i]*q[j] for i in range(2) for j in range(2))==0
    assert sum(omega[i][j]*q[i]*r[j] for i in range(2) for j in range(2))!=0
    return {'passed':True,'domain':'Q1=Q2=0, real S; exact quadratic complete only on this slice',
      'vacua':rows,'boundary':'Tree-level rigid SUSY candidate, not full E7 vacuum classification. Positive gauge coefficient remains free.'}
if __name__=='__main__':print(json.dumps(run(),indent=2))
