"""Exact regular E6 x U1 restriction. Adapted from ../next-gate/representation_checks.py.
No floating point, observed alpha, or character table input. Default replays saved receipt.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import importlib.util, hashlib, json, sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
SOURCE=ROOT.parent/'theory2-full/docs/analysis/weyl_verification.py'
PROVENANCE=HERE.parent/'next-gate/representation_checks.py'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load():
    spec=importlib.util.spec_from_file_location('theory_weyl',SOURCE)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def inverse(A):
    n=len(A); M=[[F(v) for v in row]+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for i in range(n):
        k=next(k for k in range(i,n) if M[k][i]);M[i],M[k]=M[k],M[i]
        d=M[i][i];M[i]=[x/d for x in M[i]]
        for k in range(n):
            if k!=i:
                d=M[k][i];M[k]=[x-d*y for x,y in zip(M[k],M[i])]
    return [r[n:] for r in M]
def orbit(w,A,n=None):
    n=len(A) if n is None else n; seen={w}; todo=[w]
    while todo:
        u=todo.pop()
        for i in range(n):
            v=tuple(u[j]-u[i]*A[i][j] for j in range(len(A)))
            if v not in seen:seen.add(v);todo.append(v)
    return seen

def compute():
    t=load();A=t.cartan_E(7);G=inverse(A);pos=t.positive_roots(A)
    weights=orbit((0,0,0,0,0,0,1),A)
    assert len(weights)==t.weyl_dim((0,0,0,0,0,0,1),pos)==56
    # X=2 omega7^vee: coefficients in the simple-coroot basis.
    x=[2*G[i][6] for i in range(7)]
    def charge(w):
        q=sum(a*b for a,b in zip(x,w));assert q.denominator==1;return int(q)
    roots=[tuple(sum(r[i]*A[i][j] for i in range(7)) for j in range(7)) for r in pos]
    roots+= [tuple(-v for v in r) for r in roots]
    adj=Counter(roots);adj[(0,)*7]=7
    E6=[row[:6] for row in A[:6]];p6=t.positive_roots(E6)
    def restrict(ch):
        groups=[]
        for q in sorted({charge(w) for w in ch}):
            sector={w:m for w,m in ch.items() if charge(w)==q}
            nonzero=set(sector)-{(0,)*7}; ors=[]
            while nonzero:
                o=orbit(next(iter(nonzero)),A,6);assert o<=nonzero
                hw=[w[:6] for w in o if min(w[:6])>=0];assert len(hw)==1
                ors.append({'highest_E6':list(hw[0]),'orbit_size':len(o),'weyl_dimension':t.weyl_dim(hw[0],p6)})
                nonzero-=o
            groups.append({'charge':q,'dimension':sum(sector.values()),'zero_weight_multiplicity':sector.get((0,)*7,0),'nonzero_orbits':sorted(ors,key=lambda z:z['highest_E6'])})
        return groups
    b56=restrict(Counter(weights));ba=restrict(adj)
    assert {r['charge']:r['dimension'] for r in b56}=={-3:1,-1:27,1:27,3:1}
    assert {r['charge']:r['dimension'] for r in ba}=={-2:27,0:79,2:27}
    for b in (b56,ba):
        for sector in b:
            if sector['charge']:
                assert all(o['orbit_size']==o['weyl_dimension'] for o in sector['nonzero_orbits'])
    neutral=next(s for s in ba if s['charge']==0)
    assert neutral['nonzero_orbits'][0]['orbit_size']==72
    assert neutral['nonzero_orbits'][0]['weyl_dimension']==78
    assert neutral['zero_weight_multiplicity']==7 # E6 adjoint rank six + one singlet
    traces={name:sum(m*charge(w)**2 for w,m in ch.items()) for name,ch in [('56',Counter(weights)),('133',adj)]}
    norm0=sum(x[i]*A[i][j]*x[j] for i in range(7) for j in range(7));normphys=2*norm0
    assert norm0==6 and normphys==12 and traces=={'56':72,'133':216}
    assert traces['56']/normphys==6 and traces['133']/normphys==18
    assert all(sum(x[j]*A[j][i] for j in range(7))==0 for i in range(6))
    assert all(sum(charge(w)*w[i] for w in weights)==0 for i in range(6))
    assert all(tuple(-v for v in w) in weights for w in weights)
    # Standard SU5 Cartan generators, Bphys=2 tr_5. Hypercharge is fixed by family charges.
    Y=[F(-1,3)]*3+[F(1,2)]*2;T3=[F(0)]*3+[F(1,2),F(-1,2)]
    ky=2*sum(y*y for y in Y);k2=2*sum(v*v for v in T3)
    assert ky==F(5,3) and k2==1 and sum(y*v for y,v in zip(Y,T3))==0
    # SU5 content of 27: 10 + 2*5bar + 5 + 2*1, with conjugate for 27bar.
    sm27=Counter({'Q':1,'uc':1,'ec':1,'dc':2,'L':2,'dc_bar':1,'L_bar':1,'singlet':2})
    conj={'Q':'Q_bar','uc':'uc_bar','ec':'ec_bar','dc':'dc_bar','L':'L_bar','singlet':'singlet'}
    conj.update({v:k for k,v in list(conj.items())})
    sm56=sm27+Counter({conj[k]:v for k,v in sm27.items()})+Counter(singlet=2)
    assert sum(sm56[k]*{'Q':6,'uc':3,'ec':1,'dc':3,'L':2,'Q_bar':6,'uc_bar':3,'ec_bar':1,'dc_bar':3,'L_bar':2,'singlet':1}[k] for k in sm56)==56
    chirality={k:sm56[k]-sm56[conj[k]] for k in ['Q','uc','dc','L','ec']};assert not any(chirality.values())
    return {'passed':True,'boundary':'Exact Python finite weights; SM branching is sourced input; not kernel representation theory or physical vacuum.',
      'sources':{str(p):sha(p) for p in [SOURCE,PROVENANCE,Path(__file__)]},
      'cartan':A,'X_coroot_coefficients':[str(v) for v in x],'branch56':b56,'branch133':ba,
      'trace_X_squared':traces,'B0_X_X':str(norm0),'Bphys_X_X':str(normphys),
      'weights56':[list(w) for w in sorted(weights)],'subgroup_level_E6':1,'integer_X_coupling_squared_over_g7_squared':'1/12',
      'standard_SU5_kY':str(ky),'standard_SU5_sin2_theta_tree':str(k2/(ky+k2)),
      'standard_SU5_e_squared_over_g7_squared':str(1/(ky+k2)),
      'SM_left_Weyl_multiplicities_per_56':dict(sorted(sm56.items())),
      'SM_net_chirality_per_56':chirality,'SUSY_two56_multiplier':2,'Dirac_N8_Weyl56_multiplier':16}

def replay(path=None):
    path=HERE/'embedding-receipt.json' if path is None else path
    old=json.loads(path.read_text());new=compute();assert old==new,'Receipt mismatch';return new
if __name__=='__main__':
    if '--create' in sys.argv:
        result=compute()
        with (HERE/'embedding-receipt.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    else:result=replay()
    print(json.dumps({k:v for k,v in result.items() if k not in ['weights56','cartan','sources']},indent=2))
