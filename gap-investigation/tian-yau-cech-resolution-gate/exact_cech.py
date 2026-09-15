"""Exact standard-cover Cech contraction certificate for the Tian--Yau d3 lane.

This builds the monomial subcomplexes of the four-chart cover of P^3 and their
external-product 16-chart cover of P^3 x P^3.  All matrices are over QQ.
It deliberately does not invent the missing Koszul-to-End(K) comparison map.
"""
from __future__ import annotations
from itertools import combinations, product
from fractions import Fraction
from pathlib import Path
import hashlib, json, sys
import sympy as S

P=Path(__file__).resolve().parent
ROOT=P.parent.parent
GEOM=ROOT/'gap-investigation'/'tian-yau-bundle-coupling-gate'/'geometry.json'
G=json.loads(GEOM.read_text(encoding='utf-8'))
weights=G['weights']
VERT=tuple(range(4))
subsets={q:list(combinations(VERT,q+1)) for q in range(4)}

def differential(q,N):
    """Cech delta C^q_N -> C^(q+1)_N; bases are intersections containing N."""
    dom=[I for I in subsets[q] if set(N)<=set(I)]
    if q==3:return S.zeros(0,len(dom)),dom,[]
    cod=[J for J in subsets[q+1] if set(N)<=set(J)]
    M=S.zeros(len(cod),len(dom)); row={J:i for i,J in enumerate(cod)}
    for j,I in enumerate(dom):
        for v in VERT:
            if v in I:continue
            J=tuple(sorted(I+(v,))); pos=J.index(v)
            M[row[J],j]+=(-1)**pos
    return M,dom,cod

def contraction(N):
    """Solve exactly for h with dh+hd=1-p on one Laurent-monomial sector."""
    D=[]; dims=[]
    for q in range(4):
        m,dom,_=differential(q,N);D.append(m);dims.append(len(dom))
    D.append(S.zeros(0,0))
    # Cohomology projector: only N=empty in q=0, or N=all vertices in q=3.
    Proj=[S.zeros(n,n) for n in dims]
    if len(N)==0: Proj[0]=S.ones(4,4)/4  # constants on vertices
    if len(N)==4: Proj[3]=S.eye(1)
    vars=[]; shapes=[]
    for q in range(4):
        sh=(dims[q-1] if q else 0,dims[q]);shapes.append(sh)
        block=S.symbols(f'h{q}_0:{sh[0]*sh[1]}') if sh[0]*sh[1] else ()
        vars.extend(block)
    mats=[];k=0
    for r,c in shapes:
        mats.append(S.Matrix(r,c,vars[k:k+r*c]) if r*c else S.zeros(r,c));k+=r*c
    equations=[]
    for q,n in enumerate(dims):
        lhs=S.zeros(n,n)
        if q>0: lhs += D[q-1]*mats[q]
        if q<3: lhs += mats[q+1]*D[q]
        equations.extend(list(lhs-(S.eye(n)-Proj[q])))
    A,b=S.linear_eq_to_matrix(equations,vars)
    sol=S.linsolve((A,b),vars)
    assert sol is not S.EmptySet
    tup=next(iter(sol)); free=sorted(set().union(*(e.free_symbols for e in tup)),key=str)
    tup=[e.subs({v:0 for v in free}) for e in tup]
    mats=[];k=0
    for r,c in shapes:
        mats.append(S.Matrix(r,c,tup[k:k+r*c]) if r*c else S.zeros(r,c));k+=r*c
    for q,n in enumerate(dims):
        lhs=S.zeros(n,n)
        if q>0:lhs+=D[q-1]*mats[q]
        if q<3:lhs+=mats[q+1]*D[q]
        assert lhs==S.eye(n)-Proj[q]
    assert all(D[q+1]*D[q]==S.zeros(D[q+1].rows,D[q].cols) for q in range(3))
    return D,mats,Proj,dims

def sparse(M):
    return {'shape':[M.rows,M.cols], 'entries':[[i,j,str(M[i,j])] for i in range(M.rows) for j in range(M.cols) if M[i,j]]}

def hP3(d):
    if d>=0:return [S.binomial(d+3,3),0,0,0]
    if d<=-4:return [0,0,0,S.binomial(-d-1,3)]
    return [0,0,0,0]

def kunneth(a,b):
    A=hP3(a);B=hP3(b)
    return [sum(A[i]*B[j] for i in range(4) for j in range(4) if i+j==q) for q in range(7)]

def calculate():
    contractions={}
    for r in range(5):
        for N in combinations(VERT,r):
            D,H,Q,dims=contraction(N)
            contractions[','.join(map(str,N))]={'negative_support':list(N),'dimensions':dims,
              'd':[sparse(x) for x in D[:4]],'h':[sparse(x) for x in H],
              'projector':[sparse(x) for x in Q]}
    # Exact Bott and Kunneth checks, including the two sectors used in predecessor.
    checks={f'{a},{b}':[int(x) for x in kunneth(a,b)] for a,b in [(-1,-4),(2,-4),(-4,-1),(-4,2),(0,0),(3,0)]}
    assert checks['2,-4']==[0,0,0,10,0,0,0]
    assert checks['-4,2']==[0,0,0,10,0,0,0]
    assert checks['0,0']==[1,0,0,0,0,0,0]
    # 16 affine charts and the exact source labels/characters.
    charts=[f'U{x}{y}' for x in range(4) for y in range(4)]
    source=[]
    for name,off,var in [('Cx_to_Ay',0,'x'),('Cy_to_Ax',4,'y')]:
        opp=sum(weights[4:]) if off==0 else sum(weights[:4])
        for i,j in combinations(range(4),2):
            ch=(-(weights[off+i]+weights[off+j]-opp))%3
            source.append({'summand':name,'pair':[i,j],'serre_dual_monomial':f'{var}{i}*{var}{j}','character':ch})
    counts=[sum(v['character']==c for v in source) for c in range(3)]
    assert counts==[4,4,4]
    # Sign control on the first End(K) arrow, encoded independently of dimensions.
    sign={'total':'D(phi)=d_K phi-(-1)^p phi d_K','p':-2,
          'C_to_B':'+E*phi','B_to_A':'-phi*J'}
    return {'passed':True,'d3_computed':False,
      'claim_boundary':'Concrete exact 16-chart ambient Cech normal forms/contractions and source grading. The Koszul/Tate comparison carrying these classes through both vertical solves into End(K) is not yet constructed, so no endpoint matrix or rank is claimed.',
      'cover':{'charts':charts,'count':len(charts),'construction':'external product of the four standard affine charts in each P3'},
      'p3_monomial_contractions':contractions,'bott_kunneth_checks':checks,
      'source':{'dimension':12,'characters':counts,'basis':source},'first_arrow_sign':sign,
      'invariance':{'ambient_representative_change':'proved by d*h+h*d=1-projector for every negative-support sector','endpoint_chain_map_invariance':False,'reason':'requires missing Koszul-to-End(K) comparison'},
      'source_hashes':{'../tian-yau-bundle-coupling-gate/geometry.json':hashlib.sha256(GEOM.read_bytes()).hexdigest(),
                       'exact_cech.py':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}}

def main():
    obj=calculate(); text=json.dumps(obj,sort_keys=True,indent=2)+'\n'; out=P/'certificate.json'
    if '--create' in sys.argv:
        with out.open('x',encoding='utf-8') as f:f.write(text)
    else:
        assert out.exists(),'Missing certificate; create exclusively with --create'
        assert out.read_text(encoding='utf-8')==text,'Stale/tampered certificate'
    print(json.dumps({'passed':obj['passed'],'d3_computed':obj['d3_computed'],'source_characters':obj['source']['characters'],'charts':obj['cover']['count'],'claim_boundary':obj['claim_boundary']},indent=2))
if __name__=='__main__':main()
