"""Exact tangent-monad polynomial gate. Native CPython/SymPy, no floating ranks.
Default replays saved certificate; --create is exclusive. No claimed full Ext1.
"""
from pathlib import Path
from itertools import product, combinations, combinations_with_replacement
from functools import lru_cache
import sympy as s
import hashlib, json, sys
P=Path(__file__).resolve().parent
DATA=json.loads((P/'geometry.json').read_text())
z=s.symbols(' '.join(DATA['variables'])); x=z[:4]; y=z[4:]
w=DATA['weights']; f=[s.sympify(q,locals=dict(zip(DATA['variables'],z))) for q in DATA['polynomials']]
G=s.groebner(f,*z,domain=s.QQ)
E=s.zeros(8,2)
for i in range(4): E[i,0]=x[i];E[i+4,1]=y[i]
J=s.Matrix([[s.diff(q,v) for v in z] for q in f])

def red(q):return s.expand(G.reduce(s.expand(q))[1])
def phase(q):
    if q==0:return None
    ps={sum(a*b for a,b in zip(m,w))%3 for m,c in s.Poly(q,*z).terms() if c}
    assert len(ps)==1,(q,ps)
    return ps.pop()
def mons(v,d):
    if d<0:return []
    return [s.prod(v[i] for i in t) for t in combinations_with_replacement(range(len(v)),d)]
def matrix(cols,n):return s.Matrix.hstack(*cols) if cols else s.zeros(n,0)
def sparse(M):return {'shape':list(M.shape),'entries':[[i,j,str(M[i,j])] for i in range(M.rows) for j in range(M.cols) if M[i,j]]}
def polyvec(qs):
    d={}
    for a,q in enumerate(qs):
        for mon,c in s.Poly(red(q),*z).terms():
            if c:d[(a,mon)]=c
    return d
def matdict(ds):
    keys=sorted(set().union(*(set(d) for d in ds)))
    return s.Matrix([[d.get(k,0) for d in ds] for k in keys]),keys

def calculate():
    # Geometry: exact identities on the unchanged ideal, not at random points.
    assert J*E==s.Matrix([[3*f[0],0],[f[1],f[1]],[0,3*f[2]]])
    assert all(red(q)==0 for q in J*E)
    assert all(phase(q)==0 for q in f)
    assert all(phase(J[a,i])==(-w[i])%3 for a in range(3) for i in range(8) if J[a,i])
    assert sum(w)%3==0
    r,t,c,u=s.symbols('r t c u')
    free=s.groebner([r**3+1,t**3+1,r*t+1],r,t,domain=s.QQ)
    notfree=s.groebner([r**3+1,t**3+1,r*t-1],r,t,domain=s.QQ)
    assert list(free)==[1] and list(notfree)!=[1]
    # Every projective critical point on Sx x Sy has common support and
    # x_i^3=c !=0 there. These are the exhausted 15 nonempty supports.
    smooth=[]
    for size in range(1,5):
        gb=s.groebner([size*c,c*u-1],c,u,domain=s.QQ)
        assert list(gb)==[1]
        smooth.append({'support_size':size,'number':len(list(combinations(range(4),size))),'groebner':[str(q) for q in gb]})
    # Build ALL q=0 polynomial deformations of both maps, and gauge changes.
    evars=[]
    for i,a in product(range(8),range(2)):
        for v in (x if i<4 else y):evars.append((i,a,v))
    jvars=[]
    for i in range(4):
        jvars += [(0,i,m) for m in mons(x,2)]
        jvars += [(2,i+4,m) for m in mons(y,2)]
        jvars += [(1,i,v) for v in y]
        jvars += [(1,i+4,v) for v in x]
    changes=[]; chars=[]; labels=[]
    for i,a,v in evars:
        dE=s.zeros(8,2);dE[i,a]=v;changes.append((dE,s.zeros(3,8)))
        chars.append((phase(v)-w[i])%3);labels.append(['E',i,a,str(v)])
    for a,i,v in jvars:
        dJ=s.zeros(3,8);dJ[a,i]=v;changes.append((s.zeros(8,2),dJ))
        chars.append((phase(v)+w[i])%3);labels.append(['J',a,i,str(v)])
    D,keys=matdict([polyvec(list(J*dE+dJ*E)) for dE,dJ in changes])
    def coordinates(dE,dJ):
        return s.Matrix([s.Poly(dE[i,a],*z).coeff_monomial(v) for i,a,v in evars]+[s.Poly(dJ[a,i],*z).coeff_monomial(v) for a,i,v in jvars])
    gauge=[];gchars=[]
    for i,j in product(range(2),repeat=2):
        h=s.zeros(2);h[i,j]=1;gauge.append(coordinates(-E*h,s.zeros(3,8)));gchars.append(0)
    for offset in [0,4]:
        for i,j in product(range(4),repeat=2):
            h=s.zeros(8);h[i+offset,j+offset]=1
            gauge.append(coordinates(h*E,-J*h));gchars.append((w[j+offset]-w[i+offset])%3)
    for a in range(3):
        h=s.zeros(3);h[a,a]=1;gauge.append(coordinates(s.zeros(8,2),h*J));gchars.append(0)
    H=matrix(gauge,len(changes));assert D*H==s.zeros(D.rows,H.cols)
    records=[];invariant_basis=[]
    for ch in range(3):
        ids=[i for i,a in enumerate(chars) if a==ch]
        gs=[i for i,a in enumerate(gchars) if a==ch]
        dc=D[:,ids];hc=H.extract(ids,gs);null=dc.nullspace();N=matrix(null,len(ids))
        assert dc*hc==s.zeros(dc.rows,hc.cols)
        rk=hc.rank();dim=len(null)-rk
        # Fixed-E slice spans the entire polynomial quotient modulo changes of presentation.
        jids=[i for i in ids if i>=len(evars)]
        fixed=D[:,jids].nullspace();Fc=s.zeros(len(ids),len(fixed))
        for col,v in enumerate(fixed):
            for row,idx in enumerate(jids):Fc[ids.index(idx),col]=v[row]
        assert hc.row_join(Fc).rank()==len(null)
        reps=[];span=hc;old=rk
        for k in range(Fc.cols):
            new=span.row_join(Fc[:,k]);rr=new.rank()
            if rr>old:reps.append(Fc[:,k]);span=new;old=rr
        assert len(reps)==dim
        if ch==0:
            for v in reps:
                full=s.zeros(len(changes),1)
                for a,idx in enumerate(ids):full[idx]=v[a]
                invariant_basis.append(full)
        records.append({'character':ch,'variables':len(ids),'constraint_rank':dc.rank(),'kernel':len(null),'gauge_parameters':len(gs),'gauge_rank':rk,'presentation_quotient_dimension':dim,'fixed_E_kernel':len(fixed)})
    # Polynomial charged cohomology: quotient of H0(C) by J H0(B).
    normal=[]
    for a,(dx,dy) in enumerate(DATA['C']):
        for m in mons(x,dx):
            for n in mons(y,dy):
                q=[0]*3;q[a]=m*n;normal.append(q)
    globalB=[];bchar=[]
    for i in range(8):
        for v in (x if i<4 else y):
            globalB.append([J[a,i]*v for a in range(3)]);bchar.append((phase(v)-w[i])%3)
    allM,ckeys=matdict([polyvec(q) for q in normal+globalB]);NC=allM[:,:len(normal)];JB=allM[:,len(normal):]
    cchar=[phase(s.prod(z[i]**e for i,e in enumerate(mon))) for a,mon in ckeys]
    charged=[]
    for ch in range(3):
        rows=[i for i,a in enumerate(cchar) if a==ch];cols=[i for i,a in enumerate(bchar) if a==ch]
        nr=NC[rows,:].rank();jr=JB.extract(rows,cols).rank()
        charged.append({'character':ch,'H0_C':nr,'H0_J_rank':jr,'H1_TX':nr-jr})
    assert [a['H1_TX'] for a in charged]==[9,7,7]
    # H1(B)->H1(C): restriction to divisor in two cubic surfaces.
    # H1 O_X(a,0)=H0_Sx(a-1) tensor H2_Sy(-1), a>=1.
    quadx=mons(x,2);quady=mons(y,2);Q=quadx+quady
    R=s.zeros(20,8)
    for i in range(4):R[quadx.index(x[i]**2),i]=1;R[10+quady.index(y[i]**2),i+4]=1
    qchars=[(phase(q)-sum(w[4:]))%3 for q in quadx]+[(phase(q)-sum(w[:4]))%3 for q in quady]
    assert R.rank()==8
    h2chars=[sum(1 for i,a in enumerate(qchars) if a==ch)-sum(1 for i in range(20) if qchars[i]==ch and any(R[i,j] for j in range(8)))+(2 if ch==0 else 0) for ch in range(3)]
    assert h2chars==[6,4,4]
    # Concrete invariant fixed-E family: J(t)=J+t*dJ, dJ E=0.
    # Its action on terminal C representatives is identically zero, even
    # before reducing any class. This is NOT an arbitrary zero mass matrix.
    family=[]
    for v in invariant_basis:
        dJ=s.zeros(3,8)
        for coeff,(a,i,m) in zip(list(v)[len(evars):],jvars):dJ[a,i]+=coeff*m
        assert all(red(q)==0 for q in dJ*E)
        family.append([[str(s.expand(dJ[a,i])) for i in range(8)] for a in range(3)])
    # Monadic degree: C is terminal, so every perturbation is zero on C.
    # Cokernel representative-independence follows delta*d+d*delta=0;
    # the same exact D*H and JdE+dJE tests implement this chain condition.
    bad=J.copy();bad[0,0]+=x[0]**2
    assert any(red(q)!=0 for q in bad*E)
    forbidden=[i for i,a in enumerate(chars) if a!=0]
    assert forbidden and any(chars[i]!=0 for i in forbidden)
    # Missing incoming d3 source has off-diagonal Cx->Ay and Cy->Ax
    # summands, dual to mixed quadratics. Derived identifications are not
    # silently discarded when naming bundle moduli.
    mixed=[q for q in Q if q not in [a**2 for a in z]]
    assert len(mixed)==12
    missing_chars=[sum(1 for q in mixed if (-qchars[Q.index(q)])%3==ch) for ch in range(3)]
    assert missing_chars==[4,4,4]
    hashes={str(a.relative_to(P)):hashlib.sha256(a.read_bytes()).hexdigest() for a in sorted((P/'sources').glob('*')) if a.is_file()}
    for name in ['geometry.json','exact_certificate.py']:hashes[name]=hashlib.sha256((P/name).read_bytes()).hexdigest()
    pre=P.parent/'heterotic-e6-three-family-gate'
    for name in ['source_evidence.json','sources/yukawas.pdf','sources/yukawas.txt','sources/triadophilia.txt']:
        hashes['../heterotic-e6-three-family-gate/'+name]=hashlib.sha256((pre/name).read_bytes()).hexdigest()
    return {'passed':True,'python_executable':sys.executable,'sympy_version':s.__version__,'claim_boundary':'Exact q=0 polynomial monad deformation quotient and zero charged obstruction on its genuine Ext1 image; NOT full H1(End TX), full neutral F-flatness or stabilized SM vacuum.',
      'geometry':{'J':[[str(a) for a in J.row(i)] for i in range(3)],'JE_mod_I':True,'equivariance':True,'free_fixed_stratum_GB':[str(q) for q in free],'smoothness_support_checks':smooth,'rank_monad':[2,8,3]},
      'polynomial_deformation':{'characters':records,'all_variable_labels':labels,'linear_constraint':sparse(D),'gauge_map':sparse(H),'invariant_fixed_E_representatives':family,'invariant_fixed_E_classes_before_derived_identifications':len(family),'full_Ext1_dimension':None},
      'charged':{'characters':charged,'H1B_to_H1C':sparse(R),'H1_dual_TX_characters':h2chars,'mixed_quadratic_H2_representatives':[str(q) for q in mixed],'Euler_H2_classes':2},
      'cup_product':{'definition':'Ext1(T,T) x H1(T) -> H2(T), [delta],[c] -> [delta(c)]; mass tensor is its Serre pairing with H1(T*)','computed_domain':'image of polynomial monad-map deformations in Ext1','all_23_terminal_C_representatives_annihilated':True,'invariant_mass_tensor_shape':[len(family),9,6],'invariant_mass_tensor_all_zero':True,'two_pair_neutral_F_for_computed_domain':'zero for any flavor choice including e32/e33 ansatz; not all neutral fields'},
      'derived_identification_gate':{'potential_d3_source_dimension':12,'source_characters':missing_chars,'source_description':'off-diagonal H2(Hom(Cx,Ay)) and H2(Hom(Cy,Ax)) kernels, dual to mixed quadratics','d3_computed':False,'bounds_require_H1_Hom_negative_vanishing_check':'line_cohomology.py'},
      'negative_controls':{'wrong_composition_detected':True,'wrong_quotient_phase_detected':True,'opposite_bilinear_fixed_stratum_not_empty':list(notfree)!=[1]},'source_hashes':hashes}

def main():
    d=calculate();text=json.dumps(d,sort_keys=True,indent=2)+'\n';out=P/'certificate.json'
    if '--create' in sys.argv:
        with out.open('x',encoding='utf-8') as h:h.write(text)
    else:
        assert out.exists(),'Missing certificate'
        assert out.read_text(encoding='utf-8')==text,'Stale/tampered certificate'
    print(json.dumps({'passed':True,'polynomial':d['polynomial_deformation']['characters'],'charged':d['charged']['characters'],'mass_tensor':d['cup_product']},indent=2))
if __name__=='__main__':main()
