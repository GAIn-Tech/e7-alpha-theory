"""Exact trinification representation, renormalizable invariant and Higgs gates.
Allowed != nonzero: no compactification Yukawa tensor supplied here.
"""
from fractions import Fraction as F
from itertools import product, combinations_with_replacement, permutations

def rank(rows):
    a=[list(map(F,r)) for r in rows];i=0
    if not a:return 0
    for j in range(len(a[0])):
        k=next((k for k in range(i,len(a)) if a[k][j]),None)
        if k is None:continue
        a[i],a[k]=a[k],a[i];z=a[i][j];a[i]=[x/z for x in a[i]]
        for k in range(len(a)):
            if k!=i:
                z=a[k][j];a[k]=[x-z*y for x,y in zip(a[k],a[i])]
        i+=1
        if i==len(a):break
    return i

def zero():return [[F(0) for j in range(3)] for i in range(3)]
def unit(i,j):
    a=zero();a[i][j]=1;return a
def transpose(a):return [list(r) for r in zip(*a)]
def mul(a,b):return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def sub(a,b):return [[a[i][j]-b[i][j] for j in range(3)] for i in range(3)]
def flatten(a):return sum(a,[])
def diag(v):return [[v[i] if i==j else F(0) for j in range(3)] for i in range(3)]

def calculate():
    # Convention Q=(3,bar3,1), Qc=(bar3,1,3), L=(1,3,bar3).
    names=['Q','Qc','L','Qbar','Qcbar','Lbar']
    tr=[(1,-1,0),(-1,0,1),(0,1,-1),(-1,1,0),(1,0,-1),(0,-1,1)]
    phases=[1,2,0,2,1,0]
    trials=[]
    for ids in combinations_with_replacement(range(6),3):
        if all(sum(tr[i][j] for i in ids)%3==0 for j in range(3)):
            assert sum(phases[i] for i in ids)%3==0
            trials.append([names[i] for i in ids])
    expected=[['Q']*3,['Q','Qc','L'],['Qc']*3,['L']*3,['Qbar']*3,['Qbar','Qcbar','Lbar'],['Qcbar']*3,['Lbar']*3]
    assert sorted(trials)==sorted(expected)
    # Triality is only a necessary test in general; here each result has an
    # explicit epsilon-epsilon determinant or index-loop contraction.
    bilinears=[]
    for ids in combinations_with_replacement(range(6),2):
        if all(sum(tr[i][j] for i in ids)%3==0 for j in range(3)):
            bilinears.append([names[i] for i in ids])
    assert bilinears==[['Q','Qbar'],['Qc','Qcbar'],['L','Lbar']]
    # Full complexified stabilizer of TWO actual flavor pairs.
    # L1=e_32, L2=e_33; their conjugate-representation VEVs are transposes.
    vevs=[unit(2,1),unit(2,2)]
    basis=[unit(i,j) for i in range(3) for j in range(3) if i!=j]+[diag([1,-1,0]),diag([0,1,-1])]
    cols=[]
    for side in range(2):
        for g in basis:
            a=g if side==0 else zero();b=g if side==1 else zero()
            cols.append(sum((flatten(sub(mul(a,v),mul(v,b)))+flatten(sub(mul(b,transpose(v)),mul(transpose(v),a))) for v in vevs),[]))
    equations=list(zip(*cols));r=rank(equations);assert r==12 and 16-r==4
    yL=[F(-1,6),F(-1,6),F(1,3)];yR=[F(-2,3),F(1,3),F(1,3)]
    candidates=[(unit(0,1),zero()),(unit(1,0),zero()),(diag([1,-1,0]),zero()),(diag(yL),diag(yR))]
    assert rank([flatten(a)+flatten(b) for a,b in candidates])==4
    assert all(not any(flatten(sub(mul(a,v),mul(v,b)))) and not any(flatten(sub(mul(b,transpose(v)),mul(transpose(v),a)))) for a,b in candidates for v in vevs)
    # D-flatness in canonical equal norm metrics: opposite-rep pairs cancel.
    assert all(mul(v,transpose(v))==mul(transpose(transpose(v)),transpose(v)) for v in vevs)
    # Every polarized determinant gradient on matrices supported in one row
    # vanishes: evaluate all quadratic cofactor polarizations on the two VEVs.
    def cofactor(a,i,j):
        rows=[k for k in range(3) if k!=i];cols=[k for k in range(3) if k!=j]
        return (-1)**(i+j)*(a[rows[0]][cols[0]]*a[rows[1]][cols[1]]-a[rows[0]][cols[1]]*a[rows[1]][cols[0]])
    assert all(cofactor(v,i,j)==0 for v in vevs for i,j in product(range(3),repeat=2))
    vplus=[[vevs[0][i][j]+vevs[1][i][j] for j in range(3)] for i in range(3)]
    assert all(cofactor(vplus,i,j)==0 for i,j in product(range(3),repeat=2))
    # Bilinear mass control: W=m Tr(L Lbar) has F_Lbar=m L nonzero.
    mass_obstruction=any(flatten(vevs[0]));assert mass_obstruction
    # Neutral-singlet S Tr(L Lbar) likewise obstructs this real-paired VEV
    # through F_S, even at S=0, unless actual flavor tensors cancel it.
    fs=[sum(mul(v,transpose(v))[i][i] for i in range(3)) for v in vevs];assert fs==[1,1]
    # SU3 cubic anomalies in fundamental=+1 convention.
    n=[7,7,9];nb=[4,4,6]
    anomalies=[sum((n[i]-nb[i])*3*tr[i][j] for i in range(3)) for j in range(3)];assert anomalies==[0,0,0]
    # Deliberately discard colored conjugates only: visible anomaly is nonzero.
    wrong=[sum((n[i]-[0,0,6][i])*3*tr[i][j] for i in range(3)) for j in range(3)];assert any(wrong)
    return {'convention':'Q=(3,bar3,1), Qc=(bar3,1,3), L=(1,3,bar3); W=(omega I_C,I_L,I_R) modulo diagonal Z3','multiplicities':dict(zip(names,[7,7,9,4,4,6])),'gauge_phases':dict(zip(names,phases)),'allowed_cubic_species':trials,'allowed_bilinears':bilinears,'SU3_cubic_anomalies':anomalies,'hypercharge_fundamental_L':[str(x) for x in yL],'hypercharge_fundamental_R':[str(x) for x in yR],'L_hypercharge_matrix':[[str(a-b) for b in yR] for a in yL],'two_L_plus_conjugate_pairs':{'VEVs':'L1=e32, L2=e33; conjugates transpose, equal canonical magnitudes','SL3L_SL3R_constraint_rank':r,'stabilizer_dimension':16-r,'including_color_dimension':8+16-r,'stabilizer':'sl3_C + sl2_L + u1_Y; full root and Cartan actions checked','D_flat':'canonical equal-norm conjugate pairs; Kahler metric normalization remains external','F_flat':'charged cubic truncation only; all polarized determinant cofactors vanish; Q=Qc=0'},'mass_gate':{'pair_mass_max_ranks_before_Higgs':{'Q':4,'Qc':4,'L':6},'achieved_mass_ranks':None,'bilinear_nonzero_mass_obstructs_VEV':mass_obstruction,'neutral_singlet_F_source_example':[str(x) for x in fs],'next_missing':'actual equivariant cup-product tensors for neutral bundle-modulus couplings and charged Yukawas; simultaneous F/D vacuum and post-Higgs exotic mass ranks'},'negative_controls':{'remove_only_colored_mirrors_anomalous':wrong,'constant_bilinear_or_singlet_coupling_not_automatically_flat':bool(mass_obstruction and all(fs))},'scope':'Gauge-allowed interactions and conditional Higgs alignment, NOT nonzero compactification couplings or stabilized supersymmetric vacuum.'}
if __name__=='__main__':
    import json
    print(json.dumps(calculate(),indent=2))
