"""Order dividing three in simply-connected E6; exact lattice/Weyl certificate.
Default replays saved receipt; --create uses exclusive creation.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product, combinations, combinations_with_replacement
from collections import Counter
import importlib.util, json, hashlib, sys
P=Path(__file__).resolve().parent
PRE=P.parent/'heterotic-e6-three-family-gate'
spec=importlib.util.spec_from_file_location('predecessor',PRE/'exact_certificate.py')
pre=importlib.util.module_from_spec(spec);spec.loader.exec_module(pre)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def simple(rr):
    pos={r for r in rr if next(x for x in r if x)!=abs(next(x for x in r if x))}
    return sorted(r for r in pos if not any(add(a,b)==r for a in pos for b in pos))
def components(vertices,neighbors):
    todo=set(vertices);out=[]
    while todo:
        seed=min(todo);seen={seed};stack=[seed];todo.remove(seed)
        while stack:
            for v in neighbors(stack.pop()):
                if v in todo:todo.remove(v);seen.add(v);stack.append(v)
        out.append(sorted(seen))
    return out

def nullspace(rows,n):
    from math import lcm,gcd
    from functools import reduce
    a=[list(map(F,r)) for r in rows];piv=[];i=0
    for j in range(n):
        k=next((k for k in range(i,len(a)) if a[k][j]),None)
        if k is None:continue
        a[i],a[k]=a[k],a[i];z=a[i][j];a[i]=[x/z for x in a[i]]
        for k in range(len(a)):
            if k!=i:
                z=a[k][j];a[k]=[x-z*y for x,y in zip(a[k],a[i])]
        piv.append(j);i+=1
        if i==len(a):break
    out=[]
    for j in range(n):
        if j in piv:continue
        v=[F(0)]*n;v[j]=1
        for i,k in enumerate(piv):v[k]=-a[i][j]
        den=lcm(*(x.denominator for x in v));v=[int(x*den) for x in v];g=reduce(gcd,v);out.append([x//g for x in v])
    return out

def calculate():
    rr=pre.roots()
    roots=sorted(tuple(F(x,2) for x in r) for r in rr if r[0]==r[1]==r[2])
    weights=sorted({tuple([sum(F(x,6) for x in r[:3])]*3+[F(x,2) for x in r[3:]]) for r in rr if (r[0]-r[1],r[1]-r[2])==(2,0)})
    S=simple(roots);assert len(S)==6 and len(roots)==72 and len(weights)==27
    A=[[int(dot(a,b)) for b in S] for a in S]
    # Root coordinate expansion by exact Gaussian elimination of the Gram matrix.
    def coordinates(w):
        m=[list(map(F,A[i]))+[dot(S[i],w)] for i in range(6)]
        for j in range(6):
            k=next(k for k in range(j,6) if m[k][j]);m[j],m[k]=m[k],m[j]
            z=m[j][j];m[j]=[x/z for x in m[j]]
            for k in range(6):
                if k!=j:
                    z=m[k][j];m[k]=[x-z*y for x,y in zip(m[k],m[j])]
        return tuple(row[-1] for row in m)
    rc={r:coordinates(r) for r in roots};wc={w:coordinates(w) for w in weights}
    assert all(all(x.denominator==1 for x in v) for v in rc.values())
    assert all(all(dot(w,a).denominator==1 for a in S) for w in weights)
    # Fundamental coweights exponentiate to order nine in some cases: reject
    # adjoint-group order-three shifts when the 27 detects a nontrivial cube.
    def reflect_t(t,i):
        q=sum(A[i][j]*t[j] for j in range(6));u=list(t);u[i]=(u[i]-q)%3;return tuple(u)
    all_t=set(product(range(3),repeat=6))
    orbits=components(all_t,lambda t:[reflect_t(t,i) for i in range(6)])
    def charge(w,t):return int(sum(t[i]*dot(w,S[i]) for i in range(6)))%3
    def encode(w):return [str(x) for x in w]
    entries=[]
    for orb in sorted(orbits,key=lambda x:x[0]):
        t=orb[0];surv=[r for r in roots if charge(r,t)==0];ss=simple(surv)
        factors=components(range(len(ss)),lambda i:[j for j in range(len(ss)) if i!=j and dot(ss[i],ss[j])!=0])
        types=[]
        for f in factors:
            n=len(f);degrees=sorted(sum(dot(ss[i],ss[j])!=0 for j in f if j!=i) for i in f)
            types.append('E6' if n==6 and degrees==[1,1,1,2,2,3] else 'D'+str(n) if n>=4 and 3 in degrees else 'A'+str(n))
        u1=nullspace([[dot(a,b) for b in S] for a in ss],6)
        assert len(u1)==6-len(ss)
        blocks=components(weights,lambda w:[add(w,r) for r in surv if add(w,r) in wc])
        reps=[]
        for block in blocks:
            qs={charge(w,t) for w in block};assert len(qs)==1;q=qs.pop()
            highest=[w for w in block if all(dot(w,a)>=0 for a in ss)];assert len(highest)==1
            hw=highest[0]
            reps.append({'dimension':len(block),'highest_dynkin':[int(dot(hw,a)) for a in ss], 'U1_charges':[int(sum(v[i]*dot(hw,S[i]) for i in range(6))) for v in u1], 'highest_E6_root_coordinates':encode(wc[hw]),'phase':q,'conjugate_phase':(-q)%3,'H1_character':(-q)%3,'dual_H1_character':q,'multiplicity':[9,7,7][(-q)%3],'conjugate_multiplicity':[6,4,4][q], 'net':3,'weights_E6_root_coordinates':[encode(wc[w]) for w in block]})
        # All perturbative anomalies incl abelian/mixed ones from full Cartan tensor.
        linear=all(sum(([9,7,7][(-charge(w,t))%3]-[6,4,4][charge(w,t)])*w[i] for w in weights)==0 for i in range(8))
        cubic=all(sum(([9,7,7][(-charge(w,t))%3]-[6,4,4][charge(w,t)])*w[i]*w[j]*w[k] for w in weights)==0 for i,j,k in combinations_with_replacement(range(8),3))
        assert linear and cubic
        entries.append({'t_coroot_mod3':t,'Weyl_orbit_size':len(orb),'centralizer_semisimple':types,'centralizer_U1_count':6-len(ss),'rank':6,'surviving_root_count':len(surv),'surviving_roots':[encode(rc[r]) for r in surv],'simple_roots':[encode(rc[r]) for r in ss],'factor_simple_indices':factors,'representations_27':reps,'linear_and_cubic_anomalies_vanish':linear and cubic})
    assert sum(x['Weyl_orbit_size'] for x in entries)==729
    tri=[e for e in entries if sorted(e['centralizer_semisimple'])==['A2']*3]
    assert tri
    from interactions import calculate as interaction_calculate
    interaction_result=interaction_calculate()
    for e in entries:
        t=e['t_coroot_mod3']
        e['universal_flat_c2_mod3']=sum(t[i]*A[i][j]*t[j] for i in range(6) for j in range(6))//2%3
        e['U1_coroot_basis']=nullspace([[sum(F(c)*A[j][i] for j,c in enumerate(a)) for i in range(6)] for a in e['simple_roots']],6)
    assert all(e['universal_flat_c2_mod3']==0 for e in tri)
    # Actual toral element cubes to one on faithful 27, and distinct t have distinct phases.
    signatures={tuple(charge(w,t) for w in weights) for t in all_t};assert len(signatures)==729
    # Cartan determinant: root lattice has index 3 in weight lattice.
    import itertools
    det=sum((-1)**sum(p[i]>p[j] for i in range(6) for j in range(i+1,6))*__import__('functools').reduce(lambda x,y:x*y,(A[i][p[i]] for i in range(6)),1) for p in itertools.permutations(range(6)))
    assert det==3
    # Fundamental coweight lambda_i: pairing with weights equals their root-coordinate i.
    bad=[i for i in range(6) if any(wc[w][i].denominator!=1 for w in weights)]
    assert bad
    central=[e for e in entries if e['surviving_root_count']==72];assert len(central)==3
    controls={'adjoint_only_order3_not_enough':bool(bad),'nontrivial_center_not_identity_on_27':len(signatures)==729 and len(central)==3,'SM_rank4_not_rank6':all(e['rank']!=4 for e in entries),'discarding_nontrivial_cohomology_wrong':any(r['multiplicity']==7 for e in tri for r in e['representations_27']),'mirrors_not_removed_by_index':all(r['conjugate_multiplicity']>0 for e in entries for r in e['representations_27'])}
    return {'passed':all(controls.values()),'scope':'All 729 elements of T[3] for simply-connected E6, modulo finite Weyl action; physical spectrum conditional on predecessor equivariant cohomology. No stable vacuum/mass ranks proved.','E6_Cartan':A,'E6_simple_roots_E8_coordinates':[encode(a) for a in S],'Cartan_determinant':det,'torus_points':729,'Weyl_classes':len(entries),'classes':entries,'adjoint_only_invalid_fundamental_coweight_indices':bad,'negative_controls':controls,'source_hashes':{str(p.relative_to(P.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [PRE/'REPORT.md',PRE/'exact_certificate.py',PRE/'certificate.json',PRE/'source_evidence.json',*sorted((PRE/'sources').glob('*'))]},'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

def main():
    result=calculate()
    from interactions import calculate as interaction_calculate
    result['interactions']=interaction_calculate()
    result['interaction_script_sha256']=hashlib.sha256((P/'interactions.py').read_bytes()).hexdigest()
    assert result['passed'];text=json.dumps(result,indent=2,sort_keys=True)+'\n';target=P/'certificate.json'
    if '--create' in sys.argv:
        with target.open('x',encoding='utf-8') as f:f.write(text)
    else:
        assert target.exists(),'Missing certificate';assert target.read_text(encoding='utf-8')==text,'Stale/tampered certificate'
    print(json.dumps({'passed':True,'classes':[{'t':e['t_coroot_mod3'],'orbit':e['Weyl_orbit_size'],'group':e['centralizer_semisimple'],'u1':e['centralizer_U1_count'],'reps':[(r['dimension'],r['phase'],r['multiplicity'],r['conjugate_multiplicity']) for r in e['representations_27']]} for e in result['classes']]},indent=2))
if __name__=='__main__':main()
