import sympy as S,json,sys
from pathlib import Path
u,a,xi,s,X,C,k,z1,z2=S.symbols('u a xi s X C k z1 z2',nonzero=True)
identities={
'longitudinal_propagator':S.factor(1/(u-a)-u/a*(1/(u-a)-1/(u-xi*a))-xi/(u-xi*a)),
'contracted_Ward_vertex':S.factor((s-X)*C/k*k+X*C-s*C),
'FP_vs_longitudinal_tadpole':S.factor(xi*(z1+z2)-xi*z1-xi*z2),
'longitudinal_SV_numerator':S.expand((s-X)**2-(s**2-2*s*X+X**2)),
}
assert all(v==0 for v in identities.values())
negative=S.factor(xi*(z1+z2)+xi*z1+xi*z2)
assert negative!=0
out={'passed':True,'exact_sympy_identities':{k:str(v) for k,v in identities.items()},'wrong_ghost_sign':str(negative),'scope':'Rational polynomial identities only. Ward physical premises independently tested numerically. No Lean kernel evidence.'}
p=Path(__file__).with_name('symbolic_receipt.json')
if '--create' in sys.argv:
 with p.open('x') as f:json.dump(out,f,indent=2)
else:assert json.loads(p.read_text())==out
print(json.dumps(out,indent=2))
