"""Exact conditional EFT/clock matching gate. No measured inputs.
Default verifies retained evidence WITHOUT overwriting or generating it.
Initial creation: --create (exclusive); tests: --negative-controls.
"""
from pathlib import Path
import hashlib, json, sys, tempfile
import z3
ROOT = Path(__file__).resolve().parent
C = z3.RealVal('8/3')
BOUNDARY = 'Conditional scalar EFT matching and local identifiability only; no E7 completion or numerical physical prediction.'

def cases():
    out = []
    def add(name, expected, *constraints):
        s = z3.Solver(); s.add(*constraints)
        out.append((name, expected, s.to_smt2()))
    f, fy, f2, H, D = z3.Reals('f fy f2 H D')
    add('su5_inverse_matching', 'unsat', f>0, fy==z3.RealVal('5/3')*f,
        f2==f, H==fy+f2+D, H!=C*f+D)
    f1,D1,H1,d = z3.Reals('f1 D1 H1 d')
    add('log_response_sign', 'unsat', H>0, H1==C*f1+D1,
        H*d==-H1, H*d+C*f1+D1!=0)
    du,dalpha,y,s = z3.Reals('du dalpha y s')
    add('matched_optical_response', 'unsat', H>0, H*d==-(C*f1+D1),
        dalpha==d*du, y==s*dalpha, H*y+s*(C*f1+D1)*du!=0)
    partial_f,partial_u,total = z3.Reals('partial_f partial_u total')
    add('higher_loop_total_chain_rule', 'unsat', total==partial_f*f1+partial_u,
        H1==C*f1+total, H1!=(C+partial_f)*f1+partial_u)
    bH,bL,rho,R1 = z3.Reals('bH bL rho R1')
    # R1 denotes 8*pi^2 times the derivative of the running inverse coupling.
    add('moving_heavy_mass_running_derivative', 'unsat',
        R1==bH*(-rho)+bL*rho, R1!=(bL-bH)*rho)
    # Moving arbitrary matching scale: threshold derivative cancels residual running.
    ell,T1 = z3.Reals('ell T1')
    add('matching_scale_cancellation', 'unsat', T1==(bH-bL)*ell,
        (bL-bH)*ell+T1!=0)
    eps,fnew,Dnew,f1new,D1new = z3.Reals('eps fnew Dnew f1new D1new')
    add('threshold_boundary_reallocation', 'unsat', fnew==f+eps, Dnew==D-C*eps,
        C*fnew+Dnew!=C*f+D)
    add('threshold_slope_reallocation', 'unsat', f1new==f1+eps, D1new==D1-C*eps,
        C*f1new+D1new!=C*f1+D1)
    add('distinct_positive_boundaries_same_observables', 'sat',
        f>0, fnew>0, f!=fnew, H>0, H==C*f+D, H==C*fnew+Dnew,
        H*d==-(C*f1+D1), H*d==-(C*f1new+D1new), f1!=f1new)
    add('zero_clock_signal_nonzero_uv_slope', 'sat', H>0, f>0, f1!=0,
        H*d==-(C*f1+D1), d==0)
    add('threshold_prior_restores_uv_jet', 'unsat', H>0,
        H==C*f+D, H==C*fnew+D, H*d==-(C*f1+D1),
        H*d==-(C*f1new+D1), z3.Or(f!=fnew,f1!=f1new))
    # Static boundary remains undetermined by fractional response, even D=D1=0.
    add('known_clean_drift_not_boundary', 'sat', f>0, fnew>0, f!=fnew,
        d*f==-f1, d*fnew==-f1new, d!=0)
    # Four clocks, three ratios to common reference: s is symbolic atomic sensitivity.
    s1,s2,s3,a,y1,y2,y3 = z3.Reals('s1 s2 s3 a y1 y2 y3')
    add('three_ratio_alpha_nulls', 'unsat', y1==s1*a,y2==s2*a,y3==s3*a,
        z3.Or(s2*y1-s1*y2!=0,s3*y1-s1*y3!=0,s3*y2-s2*y3!=0))
    at, y1t,y2t = z3.Reals('at y1t y2t')
    add('temporal_rank_one_minor', 'unsat', y1==s1*a,y2==s2*a,
        y1t==s1*at,y2t==s2*at,y1*y2t-y2*y1t!=0)
    lA,lB,lC,yAB,yBC,yCA = z3.Reals('lA lB lC yAB yBC yCA')
    add('triangle_is_kinematic_not_e7', 'unsat', yAB==lA-lB,yBC==lB-lC,
        yCA==lC-lA,yAB+yBC+yCA!=0)
    # Construct an off-axis nuisance: s=(1,2,3), p=(0,1,1), with symbolic amplitudes.
    n,nnew,anew = z3.Reals('n nnew anew')
    add('off_axis_nuisance_breaks_alpha_null', 'sat', n!=0,
        y1==a,y2==2*a+n,y3==3*a+n,2*y1-y2!=0)
    p1,p2,p3 = z3.Reals('p1 p2 p3')
    add('one_nuisance_projected_null', 'unsat',
        y1==s1*a+p1*n,y2==s2*a+p2*n,y3==s3*a+p3*n,
        (s2*p3-s3*p2)*y1+(s3*p1-s1*p3)*y2+(s1*p2-s2*p1)*y3!=0)
    lam = z3.Real('lam')
    add('collinear_nuisance_hides_alpha', 'sat', lam!=0,a!=anew,
        a+lam*n==anew+lam*nnew)
    # If one two-row minor is nonzero, alpha and one nuisance are both identifiable.
    add('independent_nuisance_restores_two_parameters', 'unsat',
        s1*p2-s2*p1!=0, s1*a+p1*n==s1*anew+p1*nnew,
        s2*a+p2*n==s2*anew+p2*nnew,z3.Or(a!=anew,n!=nnew))
    N1,N2,N3 = z3.Reals('N1 N2 N3')
    add('free_differential_systematics_hide_alpha', 'sat', a!=anew,
        s1==1,s2==2,s3==3,s1*a==s1*anew+N1,
        s2*a==s2*anew+N2,s3*a==s3*anew+N3)
    amp,b,ampnew,bnew,q = z3.Reals('amp b ampnew bnew q')
    # Canonical fields held fixed in units; these are different physical parameter choices.
    add('harmonic_density_coupling_product_degeneracy', 'sat',
        amp>0,ampnew>0,b!=bnew,amp!=ampnew,q==b*amp,q==bnew*ampnew,q!=0)
    add('independent_scalar_history_restores_d', 'unsat',
        du!=0,d*du==q,b*du==q,d!=b)
    return out

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def solve(text):
    s=z3.Solver(); s.set(timeout=30000); s.from_string(text)
    r=s.check()
    result={'result':str(r)}
    if r==z3.sat:
        m=s.model()
        result['witness']={str(k):str(m[k]) for k in sorted(m.decls(),key=str)}
    if r==z3.unknown: result['reason_unknown']=s.reason_unknown()
    return result

def payload(create=False):
    results=[]
    for name,expected,text in cases():
        path=ROOT/'smt'/f'{name}.smt2'
        if create:
            path.parent.mkdir(exist_ok=True)
            with path.open('x',encoding='utf-8',newline='\n') as fh: fh.write(text)
        if not path.exists(): raise ValueError('missing SMT '+name)
        if path.read_text()!=text: raise ValueError('SMT differs from mathematical definition '+name)
        actual=solve(path.read_text())
        if actual['result']!=expected: raise ValueError(f'{name}: {actual}, expected {expected}')
        results.append({'name':name,'expected':expected,'smt_sha256':sha(path),**actual})
    names=['check_matching.py','Matching.lean','REPORT.md','RELEASE_DISCLOSURE.md','formalization.yaml']
    files={name:sha(ROOT/name) for name in names}
    for p in sorted((ROOT/'sources').iterdir()):
        if p.is_file(): files['sources/'+p.name]=sha(p)
    return {'schema':1,'claim_boundary':BOUNDARY,'z3_version':z3.get_version_string(),
            'files':files,'checks':results,'passed':True}

def verify(path):
    if not path.is_file(): raise ValueError('missing receipt')
    retained=json.loads(path.read_text())
    # Compare full deterministic payload, not just its self-declared passed field.
    fresh=payload(False)
    if retained!=fresh: raise ValueError('retained receipt mismatch')
    return len(fresh['checks'])

def negative_controls():
    receipt=ROOT/'gate-receipt.json'
    good=json.loads(receipt.read_text())
    outcomes={}
    with tempfile.TemporaryDirectory(dir=ROOT,prefix='negative-') as tmp:
        p=Path(tmp)/'receipt.json'
        try: verify(p)
        except ValueError: outcomes['missing_receipt_rejected']=True
        else: raise AssertionError('missing receipt accepted')
        for label, mutate in [
            ('tampered_result_rejected',lambda v:v['checks'][0].update(result='sat')),
            ('forged_claim_boundary_rejected',lambda v:v.update(claim_boundary='E7 predicts measured alpha')),
            ('missing_check_rejected',lambda v:v['checks'].pop()),
            ('tampered_source_hash_rejected',lambda v:v['files'].update({'Matching.lean':'0'*64}))]:
            value=json.loads(json.dumps(good));mutate(value);p.write_text(json.dumps(value))
            try: verify(p)
            except ValueError: outcomes[label]=True
            else: raise AssertionError(label+' accepted')
    return outcomes

if __name__=='__main__':
    target=ROOT/'gate-receipt.json'
    if sys.argv[1:]==['--create']:
        if target.exists(): raise SystemExit('refusing to overwrite retained receipt')
        data=payload(True)
        with target.open('x') as fh: json.dump(data,fh,indent=2,sort_keys=True)
        print(json.dumps({'created':str(target),'checks':len(data['checks']),'passed':True}))
    elif sys.argv[1:]==['--negative-controls']:
        print(json.dumps(negative_controls(),sort_keys=True))
    elif not sys.argv[1:]:
        before=sha(target) if target.exists() else None
        n=verify(target)
        assert sha(target)==before
        print(json.dumps({'verified_existing_checks':n,'receipt_sha256':before,'unchanged':True}))
    else: raise SystemExit('usage: check_matching.py [--create|--negative-controls]')
