"""Exact cubic/constant-positive-metric gate. Default: immutable saved-payload replay."""
from pathlib import Path
import hashlib,json,sys
import sympy as s
P=Path(__file__).resolve().parent
G=P.parent
A=G/'tian-yau-actual-survivor-coupling-gate'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def enc(x):return json.dumps(x,sort_keys=True,indent=2)+'\n'
def simp(M):return M.applyfunc(s.simplify)
def zero(M):return all(s.simplify(x)==0 for x in M)
def unit(i,j):
 M=s.zeros(3);M[i,j]=1;return M
def packed(M):return [[str(s.simplify(x)) for x in row] for row in M.tolist()]
def load_inputs():
 manifest=json.loads((P/'source-manifest.json').read_text())
 for rel,h in manifest.items():assert sha(P/rel)==h,rel
 am=json.loads((A/'artifact-manifest.json').read_text())
 for rel,h in am['sha256'].items():assert sha(A/rel)==h,rel
 status=json.loads((A/'native-replay-status.json').read_text())
 assert status['exit_code']==0 and status['manifest_unchanged']
 assert status['log_sha256']==sha(A/'native-replay.log')
 assert status['manifest_sha256']==sha(A/'artifact-manifest.json')
 d=json.loads((A/'serre-tensor.json').read_text())
 p=json.loads((G/'tian-yau-bundle-coupling-gate/certificate.json').read_text())
 assert p['cup_product']['invariant_mass_tensor_all_zero']
 assert p['cup_product']['invariant_mass_tensor_shape']==[12,9,6]
 return manifest,d

def calculate():
 manifest,d=load_inputs()
 # Twelve zero slabs are the inherited computed polynomial Yoneda action,
 # not assigned values for the four newly established survivors.
 tensors=[s.zeros(9,6) for _ in range(12)]+[s.Matrix(t).applyfunc(s.Rational) for t in d['tensor']]
 stack=s.Matrix.vstack(*(T.T for T in tensors));K=stack.nullspace()
 assert len(K)==5 and s.Matrix.hstack(*K)==s.eye(9)[:,:5]
 L=[s.zeros(3) for _ in range(9)];B=[s.zeros(3) for _ in range(6)]
 L[0],L[1]=unit(2,1),unit(2,2);B[0],B[1]=unit(1,2),unit(2,2)
 def fs(L,B):return [s.simplify(sum(T[i,j]*s.trace(L[i]*B[j]) for i in range(9) for j in range(6))) for T in tensors]
 assert fs(L,B)==[0]*16
 # Full charged gradients of actual neutral couplings, no neutral VEV.
 ns=s.symbols('n0:16');Lm=[s.Matrix(3,3,s.symbols(f'l{i}_0:9')) for i in range(9)]
 Bm=[s.Matrix(3,3,s.symbols(f'b{j}_0:9')) for j in range(6)]
 W=sum(ns[a]*T[i,j]*s.trace(Lm[i]*Bm[j]) for a,T in enumerate(tensors) for i in range(9) for j in range(6))
 at={x:0 for x in ns}
 for field,vev in zip(Lm+Bm,L+B):at.update(dict(zip(field,vev)))
 vars=list(ns)+[x for M in Lm+Bm for x in M]
 assert all(s.diff(W,x).subs(at)==0 for x in vars)
 # Universal charged cubic coefficient test: three independent flavor slots.
 # Polarized epsilon determinant and index loop generate all eight species.
 X=[s.Matrix(3,3,s.symbols(f'x{k}_0:9')) for k in range(3)]
 abc=s.symbols('a b c'); pol=s.Poly(sum((abc[k]*X[k] for k in range(3)),s.zeros(3)).det(),*abc).coeff_monomial(abc[0]*abc[1]*abc[2])
 loop=s.trace(X[0]*X[1]*X[2]);allx=[x for M in X for x in M]
 co=s.symbols('v0:6');charged_checks={}
 for name,typ in [('Q3','zero'),('Qc3','zero'),('L3','row'),('Qbar3','zero'),('Qcbar3','zero'),('Lbar3','col'),('QQcL','looprow'),('QbarQcbarLbar','loopcol')]:
  sub={};expr=loop if typ.startswith('loop') else pol
  for k,M in enumerate(X):
   V=s.zeros(3)
   if typ in ['row','col'] or (typ.startswith('loop') and k==2):
    V=co[2*k]*unit(2,1)+co[2*k+1]*unit(2,2)
    if typ in ['col','loopcol']:V=V.T
   sub.update(dict(zip(M,V)))
  gradients=[s.expand(s.diff(expr,x).subs(sub)) for x in allx]
  assert gradients==[0]*27,name
  charged_checks[name]=len(gradients)
 # Moment-map conventions K=sum H_ij Tr(L_i^dag L_j)+Hb_jk Tr(B_j^dag B_k).
 def moments(L,B,H,Hb):
  DL=sum((H[i,j]*L[j]*L[i].H for i in range(9) for j in range(9)),s.zeros(3))-sum((Hb[i,j]*B[i].H*B[j] for i in range(6) for j in range(6)),s.zeros(3))
  DR=-sum((H[i,j]*L[i].H*L[j] for i in range(9) for j in range(9)),s.zeros(3))+sum((Hb[i,j]*B[j]*B[i].H for i in range(6) for j in range(6)),s.zeros(3))
  return simp(DL),simp(DR)
 assert all(zero(M) for M in moments(L,B,s.eye(9),s.eye(6)))
 # Arbitrary positive Hermitian principal metrics via Cholesky factors.
 r,t,p,q=s.symbols('r t p q',positive=True);x,y,u,v=s.symbols('x y u v',real=True)
 R=s.Matrix([[r,0],[x+s.I*y,t]]);S=s.Matrix([[p,0],[u+s.I*v,q]])
 M=R*R.H;N=S*S.H;U=simp(R*S.inv())
 assert zero(U*N*U.H-M)
 H=s.eye(9);H[:2,:2]=M;Hb=s.eye(6);Hb[:2,:2]=N.T
 BB=[s.zeros(3) for _ in range(6)]
 for j in range(2):BB[j][1,2]=U[0,j];BB[j][2,2]=U[1,j]
 DM=moments(L,BB,H,Hb)
 assert all(zero(z) for z in DM) and fs(L,BB)==[0]*16
 # Cross entries to zero-VEV flavors never enter these moments.
 # Full complexified stabilizer, all raising/lowering roots plus Cartans.
 basis=[unit(i,j) for i in range(3) for j in range(3) if i!=j]+[s.diag(1,-1,0),s.diag(0,1,-1)]
 def stabilizer(L,B):
  cols=[]
  for side in range(2):
   for gen in basis:
    a,b=(gen,s.zeros(3)) if side==0 else (s.zeros(3),gen)
    cols.append(s.Matrix([x for V in L for x in a*V-V*b]+[x for V in B for x in b*V-V*a]))
  mat=s.Matrix.hstack(*cols);return mat,mat.rank()
 mat,rank=stabilizer(L[:2],B[:2]);assert rank==12
 YL=s.diag(-s.Rational(1,6),-s.Rational(1,6),s.Rational(1,3));YR=s.diag(-s.Rational(2,3),s.Rational(1,3),s.Rational(1,3))
 survivors=[(unit(0,1),s.zeros(3)),(unit(1,0),s.zeros(3)),(s.diag(1,-1,0),s.zeros(3)),(YL,YR)]
 assert s.Matrix.hstack(*(s.Matrix(list(a)+list(b)) for a,b in survivors)).rank()==4
 for a,b in survivors:
  assert all(zero(a*V-V*b) for V in L) and all(zero(b*V-V*a) for V in BB)
 # U invertible implies the parameterized dual VEV span equals canonical span,
 # so both complete constraint kernels coincide, not just a dimension guess.
 assert s.simplify(U.det()-r*t/(p*q))==0
 # Controls: actual flavor change obstructed, canonical raw VEV fails nontrivial metric,
 # determinant F gradients do not vanish for unrestricted matrix support.
 badL=[s.zeros(3) for _ in range(9)];badB=[s.zeros(3) for _ in range(6)]
 badL[5],badL[7]=unit(2,1),unit(2,2);badB[1],badB[0]=unit(1,2),unit(2,2)
 badF=fs(badL,badB);assert badF==[0]*12+[-1,0,-1,0]
 Hbad=s.eye(9);Hbad[0,0]=2;badD=moments(L,B,Hbad,s.eye(6));assert any(not zero(z) for z in badD)
 wrongB=[V.T for V in B];assert stabilizer(L[:2],wrongB[:2])[1]!=rank
 assert X[0].det().diff(X[0][0,0]).subs(dict(zip(X[0],s.eye(3))))==1
 return {'passed':True,'source_manifest':manifest,'sympy':s.__version__,'tensor_nonzero':[[a,i,j,str(T[i,j])] for a,T in enumerate(tensors) for i in range(9) for j in range(6) if T[i,j]],'common_charged_kernel':packed(s.Matrix.hstack(*K)),'canonical_neutral_F':list(map(str,fs(L,B))),'known_neutral_W':str(W),'known_neutral_gradient_count':len(vars),'charged_cubic_gradient_checks':charged_checks,'full_stabilizer_constraint_matrix':packed(mat),'stabilizer_rank':rank,'stabilizer_basis':[[packed(a),packed(b)] for a,b in survivors],'including_color_dimension':12,'metric_family':{'charged_principal_H':packed(M),'dual_principal_Hbar':packed(N.T),'dual_gauge_columns_U':packed(U),'positive_domain':'r,t,p,q>0; x,y,u,v real. H and Hbar are arbitrary positive Hermitian constant flavor metrics; shown principal blocks have their general Cholesky form. Cross entries to zero fields do not contribute.','D_matrices':list(map(packed,DM)),'neutral_F':list(map(str,fs(L,BB))),'dual_span_determinant':str(s.factor(U.det()))},'negative_controls':{'alternate_flavor_F':list(map(str,badF)),'naive_equal_VEV_noncanonical_D':list(map(packed,badD)),'wrong_dual_orientation_rank':stabilizer(L[:2],wrongB[:2])[1],'generic_determinant_gradient':1},'mass_ranks':None,'claim_boundary':'Simultaneous known cubic F and quadratic-Kahler D branch, with 16 bundle neutrals at zero and all colored fields zero. Includes arbitrary positive constant flavor metrics; no actual CY Kahler metric supplied, no other-neutral tensor completion, no higher-order vacuum/stability or exotic rank claim. Twelve zero slabs inherited from polynomial Yoneda evidence. Actual four slabs read from frozen Serre tensor.'}

def main():
 out=enc(calculate());f=P/'certificate.json'
 if '--create' in sys.argv:
  with f.open('x',newline='\n') as h:h.write(out)
 else:assert f.is_file() and f.read_text()==out,'missing or changed saved certificate'
 print(enc({'passed':True,'certificate_sha256':sha(f),'mode':'create' if '--create' in sys.argv else 'immutable replay'}),end='')
if __name__=='__main__':main()
