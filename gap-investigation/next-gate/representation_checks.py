"""Exact E7 weight-character audit; stdlib, Theory2 root/Weyl routines.
Default verifies saved receipt without replacing it. --create is exclusive.
This is executable representation mathematics, not a Lean proof or QFT model.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from itertools import combinations_with_replacement, combinations, product
import importlib.util, hashlib, json, sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
SOURCE=ROOT.parent/'theory2-full/docs/analysis/weyl_verification.py'
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def run():
    spec=importlib.util.spec_from_file_location('theory_weyl',SOURCE)
    theory=importlib.util.module_from_spec(spec); spec.loader.exec_module(theory)
    A=theory.cartan_E(7); pos=sorted(theory.positive_roots(A))
    assert len(pos)==63
    M=[[Q(x) for x in row]+[Q(i==j) for j in range(7)] for i,row in enumerate(A)]
    for i in range(7):
        k=next(k for k in range(i,7) if M[k][i]); M[i],M[k]=M[k],M[i]
        d=M[i][i]; M[i]=[x/d for x in M[i]]
        for k in range(7):
            if k!=i:
                d=M[k][i]; M[k]=[x-d*y for x,y in zip(M[k],M[i])]
    G=[r[7:] for r in M]
    B=[[int(2*x) for x in r] for r in G]
    assert all(Q(B[i][j],2)==G[i][j] for i in range(7) for j in range(7))
    def inner2(u,v):return sum(u[i]*B[i][j]*v[j] for i in range(7) for j in range(7))
    def add(u,v):return tuple(x+y for x,y in zip(u,v))
    def reflect(w,i):return tuple(w[j]-w[i]*A[i][j] for j in range(7))
    def orbit(w):
        seen={w}; todo=[w]
        while todo:
            for i in range(7):
                v=reflect(todo[-1],i)
                if v not in seen:seen.add(v);todo.insert(0,v)
            todo.pop()
        return seen
    highest=(0,0,0,0,0,0,1); weights=sorted(orbit(highest))
    assert len(weights)==theory.weyl_dim(highest,pos)==56
    # The orbit already saturates the Weyl dimension: all weights multiplicity one.
    assert all(abs(sum(c*x for c,x in zip(r,highest)))<=1 for r in pos)
    sym=Counter(add(u,v) for u,v in combinations_with_replacement(weights,2))
    ext=Counter(add(u,v) for u,v in combinations(weights,2))
    root_dyn=[tuple(sum(r[i]*A[i][j] for i in range(7)) for j in range(7)) for r in pos]
    rho=(1,)*7
    def height(w):return inner2(w,rho)
    # Freudenthal recurrence evaluated over actual tensor support. No guessed irrep dimensions.
    def character(lam,support):
        mult={lam:1}; ceiling=height(lam)
        for mu in sorted(support,key=lambda w:(height(w),w),reverse=True):
            if mu==lam or height(mu)>=ceiling:continue
            den=inner2(add(lam,rho),add(lam,rho))-inner2(add(mu,rho),add(mu,rho))
            if den<=0:continue
            numerator=0
            for rd,rs in zip(root_dyn,pos):
                nu=add(mu,rd); k=1
                while height(nu)<=ceiling:
                    # (mu+k alpha,alpha)=sum(mu_i*alpha_i)+2k
                    numerator+=4*(sum(x*y for x,y in zip(mu,rs))+2*k)*mult.get(nu,0)
                    nu=add(nu,rd);k+=1
            m=Q(numerator,den)
            assert m.denominator==1 and m>=0,(lam,mu,m)
            if m:mult[mu]=int(m)
        assert sum(mult.values())==theory.weyl_dim(lam,pos)
        for w,m in mult.items():
            for i in range(7):assert mult.get(reflect(w,i),0)==m
        return Counter(mult)
    def decompose(original):
        left=original.copy(); result=[]
        while left:
            lam=max(left,key=lambda w:(height(w),w));assert min(lam)>=0
            copies=left[lam];ch=character(lam,set(original))
            for w,m in ch.items():
                assert left[w]>=copies*m
                left[w]-=copies*m
                if not left[w]:del left[w]
            result.append({'highest_weight':lam,'dimension':sum(ch.values()),'multiplicity':copies})
        return result
    sd=decompose(sym);ed=decompose(ext)
    assert sorted(x['dimension'] for x in sd)==[133,1463]
    assert sorted(x['dimension'] for x in ed)==[1,1539]
    # Stronger than absent 56 in square: not even a zero weight in the cubic tensor.
    cubic_zero=sum((sym+ext).get(tuple(-x for x in w),0) for w in weights)
    assert cubic_zero==0
    # Root-lattice coset test: 2*omega7 integral in simple basis, omega7 not.
    coords=[G[i][6] for i in range(7)]
    assert any(x.denominator==2 for x in coords) and all((2*x).denominator==1 for x in coords)
    # Cartan traces, independently using every weight and every root, not quoted Casimirs.
    allroots=root_dyn+[tuple(-x for x in r) for r in root_dyn]
    for i,j in product(range(7),repeat=2):
        assert sum(w[i]*w[j] for w in weights)==12*A[i][j]
        assert sum(r[i]*r[j] for r in allroots)==36*A[i][j]
    c56=Q(inner2(highest,add(highest,tuple(2 for _ in range(7)))),4)
    theta=max(root_dyn,key=height)
    cadj=Q(inner2(theta,add(theta,tuple(2 for _ in range(7)))),4)
    assert c56==Q(57,4) and cadj==18 and c56*56/133==6
    return {'claim_boundary':'Exact root/weight characters and stated normalization only; no physical alpha prediction or Lean formalization.',
      'sources':{str(p):digest(p) for p in [SOURCE,ROOT/'exp44_lagrangian_derivation.py',Path(__file__)]},
      'positive_roots':len(pos),'fundamental_weights':len(weights),'sym_square':sd,'exterior_square':ed,
      'cubic_tensor_zero_weight_multiplicity':cubic_zero,'omega7_simple_coordinates':[str(x) for x in coords],
      'trace_on_simple_coroots':{'56':'12*A','adjoint':'36*A'},
      'convention':'B0 root-length-squared 2; Bphys=2*B0, physics basis Bphys(t_a,t_b)=delta_ab',
      'physics_C2_56':str(c56),'physics_C2_adj':str(cadj),'physics_T56':'6','physics_Tadj':'18',
      'passed':True}
if __name__=='__main__':
    receipt=HERE/'representation-receipt.json'
    existing=None if '--create' in sys.argv else json.loads(receipt.read_text())
    data=run();data=json.loads(json.dumps(data))
    if '--create' in sys.argv:
        with receipt.open('x') as f:json.dump(data,f,indent=2);f.write('\n')
    else:assert data==existing,'Receipt stale: inputs/results changed'
    print(json.dumps(data,indent=2))
