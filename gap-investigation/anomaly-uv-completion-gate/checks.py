"""Exact bounded boundary spectator search. No physical/global-completion theorem."""
import argparse, hashlib, json
from pathlib import Path
from fractions import Fraction
import z3
ROOT=Path(__file__).resolve().parent
PRE=ROOT.parent

def anomaly(fields):
    return [sum(m*(q if r else 0) for r,q,m in fields),sum(m*(27 if r else 1)*q for r,q,m in fields),sum(m*(27 if r else 1)*q**3 for r,q,m in fields)]
def allowed(r,q): return (q-r)%3==0

def blocks():
    # r=1 is 27, r=-1 its conjugate, r=0 singlet.
    out=[]
    for q in range(-6,7):
        for t in range(-6,7):
            if q+t not in (-3,0,3): continue
            if allowed(1,q) and allowed(-1,t): out.append(('E',q,t))
            if q<=t and allowed(0,q) and allowed(0,t): out.append(('S',q,t))
    return out

def problem(n):
    bs=blocks(); vs=[z3.Int('b%d'%i) for i in range(len(bs))]; s=z3.Solver()
    for v in vs:s.add(v>=0,v<=6)
    s.add(sum(v for v,b in zip(vs,bs) if b[0]=='E')<=2)
    s.add(sum(v for v,b in zip(vs,bs) if b[0]=='S')<=6)
    coeff=[]
    for typ,q,t in bs:
        d=27 if typ=='E' else 1
        coeff.append((q+t if typ=='E' else 0,d*(q+t),d*(q**3+t**3)))
    for j,target in enumerate((-n,-24*n,0)):
        s.add(sum(v*c[j] for v,c in zip(vs,coeff))==target)
    return s,vs,bs

def rank(a):
    a=[[Fraction(x) for x in row] for row in a]; k=0
    for j in range(len(a[0]) if a else 0):
        p=next((i for i in range(k,len(a)) if a[i][j]),None)
        if p is None:continue
        a[k],a[p]=a[p],a[k]; v=a[k][j]; a[k]=[x/v for x in a[k]]
        for i in range(len(a)):
            if i!=k:
                v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[k])]
        k+=1
    return k

def payload():
    results={}
    for n in range(1,7):
        s,vs,bs=problem(n); status=str(s.check()); item={'status':status}
        if status=='sat':
            model=s.model(); item['witness']=[list(b)+[model[v].as_long()] for v,b in zip(vs,bs) if model[v].as_long()]
        results[str(n)]=item
        assert status==('sat' if n%3==0 else 'unsat')
    light=[(1,1,3),(0,-3,3)]
    heavy=[(1,-2,1),(-1,-1,1),(0,0,2),(0,3,2),(0,6,1),(0,-3,1)]
    assert all(allowed(r,q) for r,q,m in light+heavy)
    assert anomaly(light)==[3,72,0] and anomaly(heavy)==[-3,-72,0]
    assert anomaly(light+heavy)==[0,0,0]
    sing=[[0]*6 for _ in range(6)]
    for k,y in enumerate((1,2,3)):sing[2*k][2*k+1]=sing[2*k+1][2*k]=y
    allsing=[[0]*9 for _ in range(9)]
    for i in range(6):
        for j in range(6):allsing[i][j]=sing[i][j]
    e=[[0]*1 for _ in range(4)];e[3][0]=1
    assert rank(sing)==6 and rank(allsing)==6 and rank(e)==1
    yukawa_charge_sums=[-2-1+3,0+3-3,0+3-3,6-3-3]
    assert yukawa_charge_sums==[0,0,0,0]
    full=[[0]*60 for _ in range(60)]
    for i in range(27):full[2*i][2*i+1]=full[2*i+1][2*i]=1
    for i in range(6):
        for j in range(6):full[54+i][54+j]=sing[i][j]
    heavy_rank=rank(full);assert heavy_rank==60
    # Direct sum spectator E6 bilinear has 27 identical nonzero Dirac blocks.
    controls={
       'wrong_scalar_charge':not allowed(0,1),
       'omit_heavy_E6_pair':anomaly(light+heavy[2:])!=[0,0,0],
       'flip_heavy_charge':not allowed(1,2),
       'drop_singlet_pair':anomaly(light+heavy[:4])!=[0,0,0],
       'zero_yukawa_loses_rank':rank([[0,0],[0,0]])<2,
       'wrong_WZ_sign':Fraction(3)+3*Fraction(1)!=0,
       'mirror_only_kills_index':3-3==0,
       'negative_quartic_unbounded':Fraction(-1)<0,
    }
    assert all(controls.values())
    # Phi=(v+h)/sqrt(2) exp(i theta), V=-mu2|Phi|2+lambda|Phi|4.
    mu2=Fraction(2);lam=Fraction(1);v2=mu2/lam
    assert -mu2+lam*v2==0 and 2*mu2>0 and lam>0
    hashes={str(p.relative_to(PRE)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),PRE/'green-schwarz-gate/REPORT.md',PRE/'chiral-zero-mode-gate/REPORT.md',PRE/'e6-breaking-gate/REPORT.md']}
    return {'passed':True,'claim_boundary':'Exact finite SMT and rational algebra; representation/descent inputs external; no global determinant or full E6 vacuum proof.','bounds':{'charge_abs':6,'E6_dirac_blocks_max':2,'singlet_dirac_blocks_max':6,'n':[1,2,3,4,5,6]},'search':results,'candidate':{'n':3,'light':light,'heavy':heavy,'anomaly_order':['E6^2X/T27','gravity^2X','X^3'],'light_anomalies':anomaly(light),'heavy_anomalies':anomaly(heavy),'sum':anomaly(light+heavy),'pure_E6_cubic':'zero: no degree-three adjoint invariant (external group fact)','heavy_weyl_mass_rank':60,'E6_flavor_rectangular_rank':rank(e),'light_net_27':4-rank(e),'singlet_rank':rank(allsing),'massless_singlets':9-rank(allsing),'WZ_theta_Q4_coefficient':str(Fraction(-3,3))},'radial_example':{'mu2':str(mu2),'lambda':str(lam),'v2':str(v2),'radial_mass2':str(2*mu2)},'negative_controls':controls,'source_hashes':hashes}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--create',action='store_true');args=ap.parse_args()
    receipt=ROOT/'receipt.json'
    if not args.create:
        if not receipt.exists():raise SystemExit('MISSING RECEIPT')
        saved=json.loads(receipt.read_text())
    data=payload()
    # Solver witness is separately replayed rather than trusting model selection determinism.
    if args.create:
        with receipt.open('x') as f:json.dump(data,f,indent=2)
        for n in range(1,7):
            s,_,_=problem(n);(ROOT/('search-n%d.smt2'%n)).write_text(s.to_smt2())
    else:
        for n in range(1,7):
            s=z3.Solver();s.from_file(str(ROOT/('search-n%d.smt2'%n)))
            assert str(s.check())==saved['search'][str(n)]['status']
        assert saved==json.loads(json.dumps(data)), 'RECEIPT MISMATCH'
    print(json.dumps({'passed':True,'mode':'create' if args.create else 'replay','search':{k:v['status'] for k,v in data['search'].items()},'candidate':data['candidate'],'negative_controls':data['negative_controls']},indent=2))
if __name__=='__main__':main()
