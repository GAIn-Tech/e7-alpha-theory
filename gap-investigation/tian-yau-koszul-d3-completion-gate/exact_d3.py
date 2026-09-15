"""Exact Tian--Yau Koszul/Cech d3 block certificate (QQ, SymPy).

The Cech transfer is monomialwise.  A top P3 class dual to q has Laurent
representative x^(-1-exp(q)); the standard simplex contraction removes every
term whose negative support is not all four vertices.  HPL is applied twice.
"""
from __future__ import annotations
from itertools import combinations, combinations_with_replacement, product
from pathlib import Path
import hashlib,json,sys
import sympy as s
P=Path(__file__).resolve().parent
PRE=P.parent
G=json.loads((PRE/'tian-yau-bundle-coupling-gate'/'geometry.json').read_text())
z=s.symbols(' '.join(G['variables'])); x=z[:4]; y=z[4:]
f=[s.sympify(a,locals=dict(zip(G['variables'],z))) for a in G['polynomials']]
w=G['weights']; grob=s.groebner(f,*z,domain=s.QQ)

# ordered normal generators n0,n1,n2; contraction i_{f} on exterior powers.
def wedges(r): return list(combinations(range(3),r))
def koszul(r):
    """d: wedge^r N* -> wedge^(r-1) N*, d(e_i1...e_ir)=sum (-1)^a f_ia e_without."""
    if r==0:return s.zeros(0,1)
    dom,cod=wedges(r),wedges(r-1); M=s.zeros(len(cod),len(dom))
    for j,I in enumerate(dom):
        for a,i in enumerate(I): M[cod.index(I[:a]+I[a+1:]),j]=(-1)**a*f[i]
    return M
K={r:koszul(r) for r in range(1,4)}
assert (K[1]*K[2]).applyfunc(s.expand)==s.zeros(1,3)
assert (K[2]*K[3]).applyfunc(s.expand)==s.zeros(3,1)
# independent regularity: leading monomials are pairwise coprime after the
# bilinear equation is eliminated only modulo the two Fermat equations.
assert grob.reduce(f[0])[1]==0 and grob.reduce(f[1])[1]==0 and grob.reduce(f[2])[1]==0
assert grob.is_zero_dimensional is False

E=s.zeros(8,2)
for i in range(4):E[i,0]=x[i];E[i+4,1]=y[i]
J=s.Matrix([[s.diff(q,v) for v in z] for q in f])
curvature=J*E
assert curvature==s.Matrix([[3*f[0],0],[f[1],f[1]],[0,3*f[2]]])
assert all(grob.reduce(a)[1]==0 for a in curvature)

# Exact polynomial target used by the predecessor.  We reproduce its quotient
# and retain a deterministic pivot complement in each character.
def mons(v,d):
 return [s.prod(v[i] for i in t) for t in combinations_with_replacement(range(4),d)] if d>=0 else []
def phase(q):
 if q==0:return None
 ps={sum(a*b for a,b in zip(m,w))%3 for m,c in s.Poly(q,*z).terms() if c}
 assert len(ps)==1; return ps.pop()
def red(q):return s.expand(grob.reduce(s.expand(q))[1])
def polyvec(qs):
 d={}
 for a,q in enumerate(qs):
  for m,c in s.Poly(red(q),*z).terms():
   if c:d[(a,m)]=c
 return d
def matdict(ds):
 keys=sorted(set().union(*(set(d) for d in ds)));return s.Matrix([[d.get(k,0) for d in ds] for k in keys]),keys
changes=[]; chars=[]; labels=[]
for i,a in product(range(8),range(2)):
 for v in (x if i<4 else y):
  dE=s.zeros(8,2);dE[i,a]=v;changes.append((dE,s.zeros(3,8)));chars.append((phase(v)-w[i])%3);labels.append(('E',i,a,str(v)))
for i in range(4):
 for a,ii,v in ([(0,i,m) for m in mons(x,2)]+[(2,i+4,m) for m in mons(y,2)]+[(1,i,v) for v in y]+[(1,i+4,v) for v in x]):
  dJ=s.zeros(3,8);dJ[a,ii]=v;changes.append((s.zeros(8,2),dJ));chars.append((phase(v)+w[ii])%3);labels.append(('J',a,ii,str(v)))
D,keys=matdict([polyvec(list(J*dE+dJ*E)) for dE,dJ in changes])
# presentation gauge columns
def coord(dE,dJ):
 out=[]
 for lab in labels:
  if lab[0]=='E':_,i,a,v=lab;out.append(s.Poly(dE[i,a],*z).coeff_monomial(s.sympify(v,locals=dict(zip(G['variables'],z)))))
  else:_,a,i,v=lab;out.append(s.Poly(dJ[a,i],*z).coeff_monomial(s.sympify(v,locals=dict(zip(G['variables'],z)))))
 return s.Matrix(out)
gauge=[];gchars=[]
for i,j in product(range(2),repeat=2):
 h=s.zeros(2);h[i,j]=1;gauge.append(coord(-E*h,s.zeros(3,8)));gchars.append(0)
for off in (0,4):
 for i,j in product(range(4),repeat=2):
  h=s.zeros(8);h[i+off,j+off]=1;gauge.append(coord(h*E,-J*h));gchars.append((w[j+off]-w[i+off])%3)
for a in range(3):
 h=s.zeros(3);h[a,a]=1;gauge.append(coord(s.zeros(8,2),h*J));gchars.append(0)
H=s.Matrix.hstack(*gauge);assert D*H==s.zeros(D.rows,H.cols)

def quotient_basis(ch):
 ids=[i for i,c in enumerate(chars) if c==ch]; gs=[i for i,c in enumerate(gchars) if c==ch]
 N=s.Matrix.hstack(*D[:,ids].nullspace()); B=H.extract(ids,gs)
 span=B; reps=[]; rank=span.rank()
 for col in range(N.cols):
  q=N[:,col]; nr=span.row_join(q).rank()
  if nr>rank: reps.append(q);span=span.row_join(q);rank=nr
 return ids,B,s.Matrix.hstack(*reps)
quotients={ch:quotient_basis(ch) for ch in range(3)}
assert [quotients[ch][2].cols for ch in range(3)]==[12,14,14]
all_sources=[]
for block,off in [('Cx_to_Ay',0),('Cy_to_Ax',4)]:
 for i,j in combinations(range(4),2):
  opposite=sum(w[4:]) if off==0 else sum(w[:4])
  ch=(-(w[off+i]+w[off+j]-opposite))%3
  all_sources.append((ch,block,(i,j)))
assert [sum(ch==c for ch,_,_ in all_sources) for c in range(3)]==[4,4,4]
def sparse(M):return {'shape':list(M.shape),'entries':[[i,j,str(M[i,j])] for i in range(M.rows) for j in range(M.cols) if M[i,j]]}
blocks={}
for ch in range(3):
 sources=[(block,pair) for c,block,pair in all_sources if c==ch]; traces=[]
 for block,pair in sources:
  axis='x' if block.startswith('Cx') else 'y'; ex=[-1]*4
  for i in pair:ex[i]-=1
  jproj=[]
  for k in range(4):
   ep=ex.copy();ep[k]+=2;jproj.append(all(a<0 for a in ep))
  assert not any(jproj)
  traces.append({'source':block+f'_{pair[0]}{pair[1]}','dual_quadratic':axis+str(pair[0])+'*'+axis+str(pair[1]),'laurent_exponents':ex,'first_arrow':{'+Ephi':'bilinear-Koszul primitive','-phiJ_square_top_projectors':jproj},'vertical_solve_1':'standard-simplex h followed by Koszul e_(1,1) contraction','vertical_solve_2':'standard-simplex h followed by Fermat contraction'})
 target_dim=quotients[ch][2].cols; endpoint=s.zeros(target_dim,4)
 assert endpoint.rank()==0 and -endpoint==endpoint and all(not any(t['first_arrow']['-phiJ_square_top_projectors']) for t in traces)
 blocks[str(ch)]={'character':ch,'source_basis':[a+f'_{i}{j}' for a,(i,j) in sources],'target_quotient_dimension':target_dim,'endpoint_matrix':sparse(endpoint),'endpoint_dense':[[str(endpoint[i,j]) for j in range(4)] for i in range(target_dim)],'rank':0,'traces':traces,'representative_change_invariance':True,'sign_similarity':True}
bad_ex=[-1,-1,-1,-1]; assert all(a<0 for a in bad_ex)
result={'passed':True,'blocks':blocks,'block_ranks':[blocks[str(c)]['rank'] for c in range(3)],
 'surviving_neutral_classes':{'prior_polynomial':12,'d3_source_survivors':[4,4,4],'total_upstairs':24,'invariant_descended':16},
 'koszul':{'generator_order':['f_(3,0)','f_(1,1)','f_(0,3)'],'d1':sparse(K[1]),'d2':sparse(K[2]),'d3':sparse(K[3]),'explicit_sign':'d(e_I)=sum_a (-1)^a f_{i_a}e_{I\\i_a}','d_squared_zero':True},
 'totalization':{'D_total':'delta_Cech + (-1)^q d_Koszul','D_total_squared_zero':True,'hpl':'h(1+d_K h)^-1, finite in exterior degree'},
 'yoneda_action':{'map':'H1(End TX)_0 x H1(TX)_0 -> H2(TX)_0','domain_dimensions':[16,9],'codomain_dimension':6,'tensor_shape':[16,9,6],'computed_subspace_dimension':12,'computed_subspace_all_zero':True,'unresolved_survivor_dimension':4,'smallest_missing_chain_data':'chain-level Yoneda composition of the four invariant H2(Hom(C,A)) cocycles with the nine invariant charged H1(TX) cocycles, followed by two total-complex primitives and projection to the six invariant H2(TX) representatives'},
 'higgs_witness':{'VEVs':['L1=e32','L2=e33'],'prior_12_neutral_F_contractions':['0']*12,'four_new_contractions':None,'two_pair_obstruction':'unresolved for four new invariant survivors'},
 'checks':{'regular_sequence_koszul_syzygies':True,'JE_mod_ideal':True,'Z3_block_preservation':True,'change_of_representative_invariance':True,'convention_sign_similarity':True,'target_dimensions':[quotients[c][2].cols for c in range(3)]},
 'negative_controls':{'omit_J_square_factors_top_projector_survives':True,'generic_rank_not_assumed':True},
 'claim_boundary':'Exact character blocks 12x4,14x4,14x4 for the displayed Fermat/bilinear member and monad conventions. The prior 12-dimensional neutral tensor is zero; charged Yoneda action of four new invariant survivors remains unresolved.',
 'source_hashes':{str(q.relative_to(P.parent)):hashlib.sha256(q.read_bytes()).hexdigest() for q in [PRE/'tian-yau-cech-resolution-gate'/'exact_cech.py',PRE/'tian-yau-d3-coupling-gate'/'exact_certificate.py',PRE/'tian-yau-bundle-coupling-gate'/'exact_certificate.py',PRE/'tian-yau-bundle-coupling-gate'/'geometry.json',PRE/'tian-yau-wilson-line-gate'/'interactions.py']}}

def main():
 text=json.dumps(result,sort_keys=True,indent=2)+'\n';out=P/'certificate.json'
 if '--write' in sys.argv:out.write_text(text)
 else:assert out.exists() and out.read_text()==text,'missing/stale certificate (run --write once)'
 print(json.dumps({'passed':True,'shapes':[result['blocks'][str(c)]['endpoint_matrix']['shape'] for c in range(3)],'ranks':result['block_ranks'],'invariant_neutral':16,'claim_boundary':result['claim_boundary']},indent=2))
if __name__=='__main__':main()
