"""Finite exact E7 Cartan/kinetic-normalization and EFT identifiability audit.
Not a proof that no UV completion can predict alpha. See README.md.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import platform
import z3

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
THEORY = REPO.parent / 'theory2-full'
N = 7
# Bourbaki E7: chain 1-3-4-5-6-7, branch 2-4; arm lengths 2,1,3.
A = [[2 if i == j else 0 for j in range(N)] for i in range(N)]
for i, j in [(0,2),(2,3),(1,3),(3,4),(4,5),(5,6)]:
    A[i][j] = A[j][i] = -1

def matmul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def transpose(a):
    return list(map(list, zip(*a)))

# Exact LDL^T: positivity of these pivots certifies positive definiteness.
L = [[F(i == j) for j in range(N)] for i in range(N)]
D = []
for j in range(N):
    D.append(F(A[j][j])-sum(L[j][k]**2*D[k] for k in range(j)))
    for i in range(j+1,N):
        L[i][j]=(F(A[i][j])-sum(L[i][k]*L[j][k]*D[k] for k in range(j)))/D[j]
assert all(d > 0 for d in D)
assert matmul(matmul(L, [[D[i] if i==j else F(0) for j in range(N)] for i in range(N)]), transpose(L)) == A

def determinant(a):
    b=[list(map(F,row)) for row in a]; out=F(1)
    for j in range(len(b)):
        p=next(i for i in range(j,len(b)) if b[i][j])
        if p!=j: b[p],b[j]=b[j],b[p]; out=-out
        pivot=b[j][j]; out*=pivot
        for i in range(j+1,len(b)):
            scale=b[i][j]/pivot
            for k in range(j,len(b)): b[i][k]-=scale*b[j][k]
    return out
assert determinant(A)==2

K=[[None]*N for _ in range(N)]
for i in range(N):
    for j in range(i,N): K[i][j]=K[j][i]=z3.Real(f'K_{i}_{j}')
constraints=[]
reflections=[]
for r in range(N):
    S=[[int(i==j)-(A[r][j] if i==r else 0) for j in range(N)] for i in range(N)]
    assert matmul(matmul(transpose(S),A),S)==A
    reflections.append(S)
    transformed=matmul(matmul(transpose(S),K),S)
    constraints += [transformed[i][j]==K[i][j] for i in range(N) for j in range(i,N)]

checks=[]
def check(name, assertions, expected, witness_vars=()):
    s=z3.Solver(); s.set(timeout=15000); s.add(*assertions)
    (ROOT/f'{name}.smt2').write_text(s.to_smt2(),encoding='utf-8')
    result=s.check()
    entry={'name':name,'expected':expected,'actual':str(result),'passed':str(result)==expected}
    if result==z3.sat:
        m=s.model(); entry['witness']={str(x):str(m.eval(x,model_completion=True)) for x in witness_vars}
    if result==z3.unknown: entry['reason_unknown']=s.reason_unknown()
    checks.append(entry)
    assert entry['passed'],entry

k=z3.Real('k')
check('weyl_invariance_forces_only_shape',constraints+[k==K[0][0]/2,z3.Or(*[K[i][j]!=k*A[i][j] for i in range(N) for j in range(i,N)])],'unsat')
# Existential negation: any real positive k breaking a reflection is impossible.
scaled=[[k*A[i][j] for j in range(N)] for i in range(N)]
bad=[]
for S in reflections:
    t=matmul(matmul(transpose(S),scaled),S)
    bad += [t[i][j]!=scaled[i][j] for i in range(N) for j in range(N)]
check('every_positive_real_scale_preserves_weyl_invariance',[k>0,z3.Or(*bad)],'unsat')
check('same_E7_two_kinetic_coefficients',[k>0,k!=1]+[K[i][j]==k*A[i][j] for i in range(N) for j in range(i,N)]+constraints,'sat',[k,K[0][0]])
# For every positive c, c+1 is another positive coefficient; not just finite sampling.
c=z3.Real('c')
check('positive_ray_has_another_point',[c>0,z3.Or(c+1<=0,c+1==c)],'unsat')
# Invariant functional equality survives any real coefficient. Full E7 invariance
# of the base functional is an ASSUMPTION; Weyl invariance above is derived.
f,ft=z3.Reals('functional transformed_functional')
check('invariant_functional_scaling',[f==ft,c*f!=c*ft],'unsat')
# y=alpha^-1(mu) with fixed embedding index kY>0 and common running/threshold
# contribution d. The affine map is the stated one-loop/matching approximation.
x1,x2,y1,y2,kY,d=z3.Reals('x1 x2 y1 y2 embedding_index common_running_threshold')
rg=[x1>0,x2>0,kY>0,y1==kY*x1+d,y2==kY*x2+d,y1>0,y2>0]
check('running_does_not_erase_boundary_parameter',rg+[x1!=x2,y1==y2],'unsat')
check('fixed_group_and_matching_allow_distinct_low_energy_couplings',rg+[x1!=x2,y1!=y2,kY==1,d==0],'sat',[x1,x2,y1,y2])
check('independent_boundary_restores_matching_uniqueness',rg+[x1==x2,y1!=y2],'unsat')
# Adding a selected alpha formula is itself an extra constraint, not a consequence.
check('group_data_do_not_imply_selected_137_formula',rg+[kY==1,d==0,y1!=137],'sat',[x1,y1])
# Toy EFT potential unique vacuum x=v, completely independent of gauge coefficient.
x,v=z3.Reals('vacuum_coordinate vacuum_location')
check('toy_potential_unique_minimum',[x!=v,(x-v)*(x-v)<=0],'unsat')
check('toy_unique_vacuum_two_positive_kinetic_coefficients',[x==v,c>0,k>0,c!=k],'sat',[x,v,c,k])
# Normalization consistency check from dim(R) C2(R)=dim(G) T(R).
T,C=z3.Reals('T56 C56')
check('standard_trace_identity',[56*C==133*T,C==z3.RealVal('57/4'),T!=6],'unsat')
check('legacy_exp44_values_produce_T12_not_T6',[56*C==133*T,C==z3.RealVal('57/2'),T==6],'unsat')

measurement=F('137.035999177'); uncertainty=F('0.000000021')
candidates={name:val for name,val in [('integer',F(133)+F(56,14)),('chosen_correction',F(137)+F(9,250))]}
comparisons={name:{'value':str(val),'signed_residual':str(val-measurement),'absolute_residual':str(abs(val-measurement)), 'residual_over_experimental_uncertainty':str((val-measurement)/uncertainty),'relative_error_denominator':'CODATA2022 central alpha inverse','relative_error':str((val-measurement)/measurement),'inside_one_quoted_uncertainty':abs(val-measurement)<=uncertainty} for name,val in candidates.items()}
assert candidates['chosen_correction']-measurement==F(823,10**9)
sources=[REPO/f for f in ['exp44_lagrangian_derivation.py','exp46_coupling_running.py','exp47_unique_vacuum.py','exp58_alpha_running.py','exp63_delta_derivation.py']]+[THEORY/'formal'/f for f in ['lean-toolchain','lakefile.toml','Formal/E7.lean','Formal/Running.lean','Formal/AlphaContentAudit.lean']]
hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
receipt={'passed':all(c['passed'] for c in checks),'solver_version':z3.get_version_string(),'python_version':platform.python_version(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'source_sha256':hashes,'cartan_matrix':A,'cartan_determinant':str(determinant(A)),'ldlt_positive_pivots':list(map(str,D)),'checks':checks,'comparisons':comparisons,'claim_boundary':'Conditional symmetry-normalization and affine one-loop EFT identifiability only. Weyl Cartan action constructed, full E7 adjoint kinetic invariance assumed. No Lagrangian/UV vacuum or physical alpha prediction derived. SMT results are Z3 solver results, not Lean kernel certificates. Measurement/uncertainty supplied by user; no model uncertainty asserted.'}
(ROOT/'smt-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':receipt['passed'],'solver':receipt['solver_version'],'checks':len(checks),'checks_detail':checks,'comparisons':comparisons,'pivots':receipt['ldlt_positive_pivots']},indent=2))
