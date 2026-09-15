"""Bounded exact E7 interval parity gate; no physical-theory completion claim."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from collections import Counter
from itertools import product
from fractions import Fraction as F
import importlib.util, json, hashlib
import z3
HERE=Path(__file__).resolve().parent
BASE=HERE.parent/'embedding-gate/embedding_checks.py'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def predecessor():
    spec=importlib.util.spec_from_file_location('embedding',BASE)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m,m.replay()
def q(w,x): return sum(a*b for a,b in zip(w,x))
def parity(w,x,k,eta=1): return eta*(1 if k==0 else (1 if ((q(w,x)-1)//2)%2==0 else -1))
def compute(save_smt=False):
    m,b=predecessor(); A=b['cartan']; x=list(map(int,b['X_coroot_coefficients']))
    W=[tuple(w) for w in b['weights56']]; ws=set(W)
    pos=m.load().positive_roots(A)
    roots=[tuple(sum(r[i]*A[i][j] for i in range(7)) for j in range(7)) for r in pos]
    roots+= [tuple(-a for a in r) for r in roots]; rs=set(roots)
    charge=lambda w:q(w,x)
    gauge=lambda r,k: 1 if k==0 else (1 if (charge(r)//2)%2==0 else -1)
    # Cartan is fixed. Root brackets, including opposite-root Cartan brackets.
    brackets=0
    for a in roots:
        for c in roots:
            d=tuple(v+w for v,w in zip(a,c))
            if d in rs or not any(d):
                assert gauge(a,1)*gauge(c,1)==gauge(d,1);brackets+=1
    edges=[]
    for i,w in enumerate(W):
        for a in roots:
            v=tuple(u+t for u,t in zip(w,a))
            if v in ws:
                j=W.index(v); edges.append((i,j,a))
                for k in (0,1): assert parity(v,x,k)==gauge(a,k)*parity(w,x,k)
    # Minuscule root strings have multiplicity one: all these transitions are nonzero.
    # Connected action + intertwining exhausts diagonal real involutive lifts.
    smt=[]
    for k in (0,1):
        ps=[z3.Bool('p'+str(i)) for i in range(56)]; s=z3.Solver()
        for i,j,a in edges: s.add(ps[j]==(ps[i] if gauge(a,k)==1 else z3.Not(ps[i])))
        candidates=[[parity(w,x,k,e)==1 for w in W] for e in (1,-1)]
        s.add(z3.Not(z3.Or(*[z3.And(*[ps[i]==v for i,v in enumerate(c)]) for c in candidates])))
        text=s.to_smt2(); status=str(s.check()); assert status=='unsat'
        name=f'no_other_diagonal_lift_{k}.smt2'
        if save_smt: (HERE/name).write_text(text)
        else: assert (HERE/name).read_text()==text
        smt.append({'file':name,'result':status,'sha256':hashlib.sha256(text.encode()).hexdigest()})
    cases=[]
    for k0,k1,e0,e1 in product((0,1),(0,1),(1,-1),(1,-1)):
        H=[w for w in W if parity(w,x,k0,e0)==parity(w,x,k1,e1)==1]
        # Hc is independent dual, parity -P^(-T); negate retained source weights.
        Hc=[tuple(-v for v in w) for w in W if parity(w,x,k0,e0)==parity(w,x,k1,e1)==-1]
        modes=H+Hc; counts=Counter(charge(w) for w in modes)
        assert all(counts[c]%27==0 for c in (-1,1))
        net=(counts[1]-counts[-1])//27
        assert net in (-2,-1,0,1,2)
        # Relative T27 units avoids importing a trace normalization.
        mixed=F(counts[1]-counts[-1],27)
        grav=sum(charge(w) for w in modes); cubic=sum(charge(w)**3 for w in modes)
        assert grav==24*net and mixed==net and cubic==0
        local=[]
        for k,e in ((k0,e0),(k1,e1)):
            # One full bulk Dirac anomaly is 1/2 Tr_R(P T{T,T}) per end.
            lc={c:sum(F(parity(w,x,k,e),2) for w in W if charge(w)==c) for c in (-3,-1,1,3)}
            local.append({'E6_squared_X_over_T27':str((lc[1]-lc[-1])/27),'gravity_squared_X':str(sum(c*lc[c] for c in lc)),'X_cubed':str(sum(c**3*lc[c] for c in lc))})
        assert sum(F(z['gravity_squared_X']) for z in local)==grav
        assert sum(F(z['E6_squared_X_over_T27']) for z in local)==mixed
        assert sum(F(z['X_cubed']) for z in local)==cubic
        gauge_n=7+sum(gauge(a,k0)==gauge(a,k1)==1 for a in roots)
        sigma=[a for a in roots if gauge(a,k0)==gauge(a,k1)==-1]
        assert Counter(charge(a) for a in sigma) in (Counter(),Counter({-2:27,2:27}))
        cases.append({'boundary_types':[k0,k1],'intrinsic_signs':[e0,e1], 'H_weights':[list(w) for w in H],'Hc_weights':[list(w) for w in Hc], 'H_charge_dimensions':dict(sorted(Counter(charge(w) for w in H).items())), 'Hc_charge_dimensions':dict(sorted(Counter(charge(w) for w in Hc).items())), 'net_27':net,'gauge_dimension':gauge_n,'Sigma_charge_dimensions':dict(sorted(Counter(charge(w) for w in sigma).items())), 'anomalies':{'E6_squared_X_over_T27':str(mixed),'gravity_squared_X':grav,'X_cubed':cubic},'endpoint_anomalies':local})
    assert len(cases)==16
    nonzero=[c for c in cases if c['net_27']]
    assert all(c['anomalies']['gravity_squared_X']!=0 for c in nonzero)
    # Arbitrarily many these full hypers: all mixed anomalies proportional to net chirality.
    s=z3.Solver(); n=z3.Int('net_27'); s.add(n==3,24*n==0)
    assert str(s.check())=='unsat'
    text=s.to_smt2(); name='three_net_27_and_gravity_anomaly_free.smt2'
    if save_smt:(HERE/name).write_text(text)
    else:assert (HERE/name).read_text()==text
    smt.append({'file':name,'result':'unsat','sha256':hashlib.sha256(text.encode()).hexdigest()})
    return {'passed':True,'claim_boundary':'Exact finite root/weight and SMT gate, full 56 hypers, diagonal identity/E6-U1 inner boundary involutions, no added localized matter or anomaly sector. Not Lean representation proof or quantum completion.', 'source_hashes':{str(p):sha(p) for p in [Path(__file__),BASE,HERE.parent/'embedding-gate/embedding-receipt.json']},'root_count':len(roots),'weight_count':len(W),'root_bracket_checks':brackets,'nonzero_directed_weight_transitions':len(edges),'cases':cases,'smt':smt}
def replay(path=None):
    old=json.loads((path or HERE/'orbifold-receipt.json').read_text());new=compute()
    # JSON normalizes integer dictionary keys.
    assert old==json.loads(json.dumps(new)), 'Receipt mismatch'
    return new
if __name__=='__main__':
    if '--create' in sys.argv:
        assert not (HERE/'orbifold-receipt.json').exists()
        r=compute(True)
        with (HERE/'orbifold-receipt.json').open('x') as f:json.dump(r,f,indent=2)
    else:r=replay()
    print(json.dumps({'passed':r['passed'],'roots':r['root_count'],'weights':r['weight_count'],'brackets':r['root_bracket_checks'],'transitions':r['nonzero_directed_weight_transitions'],'cases':len(r['cases']),'SMT':r['smt']},indent=2))
