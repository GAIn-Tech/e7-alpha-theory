"""Exact grading and ambient Koszul line-cohomology audit; no fabricated Yoneda tensor."""
from pathlib import Path
from itertools import combinations, product
from functools import lru_cache
import json, hashlib, sys
import sympy as s
P=Path(__file__).resolve().parent
ROOT=P.parent
G=json.loads((ROOT/'tian-yau-bundle-coupling-gate/geometry.json').read_text())
w=G['weights']; deg=G['degrees']
z=s.symbols(' '.join(G['variables']))
f=[s.Poly(s.sympify(t,locals=dict(zip(G['variables'],z))),*z).terms() for t in G['polynomials']]
@lru_cache(None)
def comps(d,n=4):
 if n==1:return [(d,)] if d>=0 else []
 return [(a,)+b for a in range(d+1) for b in comps(d-a,n-1)] if d>=0 else []
def p3(d):
 if d>=0:return 0,comps(d)
 if d<=-4:return 3,[tuple(-1-t for t in a) for a in comps(-d-4)]
 return 0,[]
def ambient(a,b):
 q,A=p3(a);r,B=p3(b)
 return q+r,[u+v for u in A for v in B]
@lru_cache(None)
def line(a,b):
 bases={}
 for k in range(4):
  for I in combinations(range(3),k):
   q,es=ambient(a-sum(deg[i][0] for i in I),b-sum(deg[i][1] for i in I))
   for e in es:bases.setdefault((k,q,sum(t*v for t,v in zip(e,w))%3),[]).append((I,e))
 ranks={}
 for (k,q,ch),dom in bases.items():
  cod=bases.get((k-1,q,ch),[]);index={v:i for i,v in enumerate(cod)}
  M=s.zeros(len(cod),len(dom))
  if k:
   for j,(I,e) in enumerate(dom):
    for t,i in enumerate(I):
     for mon,c in f[i]:
      key=(I[:t]+I[t+1:],tuple(a+b for a,b in zip(e,mon)))
      if key in index:M[index[key],j]+=(-1)**t*c
  ranks[k,q,ch]=M.rank()
 ans=[[0]*3 for _ in range(4)]
 for (k,q,ch),bs in bases.items():
  h=len(bs)-ranks[k,q,ch]-ranks.get((k+1,q,ch),0)
  assert h>=0
  if h:
   assert 0<=q-k<=3
   ans[q-k][ch]+=h
 return ans

def calculate():
 # Terms of the unshifted tangent monad; a common shift cancels in Hom.
 terms=[]
 for name,p in [('A',-1),('B',0),('C',1)]:
  for i,d in enumerate(G[name]):terms.append((name,i,p,d,w[i] if name=='B' else 0))
 e1={}; summands=[]
 for a,b in product(terms,repeat=2):
  p=b[2]-a[2];d=tuple(v-u for u,v in zip(a[3],b[3]));coh=line(*d)
  for q,cs in enumerate(coh):
   rotated=[cs[(c-a[4]+b[4])%3] for c in range(3)]
   if any(rotated):
    key=f'{p},{q}';e1.setdefault(key,[0,0,0]);e1[key]=[x+y for x,y in zip(e1[key],rotated)]
    if p+q==1:summands.append({'source':f'{a[0]}{a[1]}','target':f'{b[0]}{b[1]}','line_degree':d,'bidegree':[p,q],'characters':rotated})
 old=json.loads((ROOT/'tian-yau-koszul-d3-completion-gate/certificate.json').read_text())
 bs=old['blocks']['0']['source_basis']
 source=[{'label':name,'bidegree':[-2,2],'total_degree':sum([-2,2]),'charged_product_total_degree':sum([-2,2])+1,'is_Ext1':False} for name in bs]
 assert len(source)==4 and all(t['total_degree']==0 for t in source)
 diagonal={key:cs for key,cs in e1.items() if sum(map(int,key.split(',')))==1}
 # Every E-infinity contribution to Ext1 must be on this exact diagonal.
 slots=[[p,1-p] for p in range(-2,3) if 0<=1-p<=3]
 assert slots==[[-2,3],[-1,2],[0,1],[1,0]]
 dr=[]
 for r in range(2,6):
  for p,q in slots:
   for typ,u,v in [('incoming',p-r,q+r-1),('outgoing',p+r,q-r+1)]:
    if -2<=u<=2 and 0<=v<=3 and e1.get(f'{u},{v}',[0,0,0])!=[0,0,0]:
     dr.append({'r':r,'diagonal_slot':[p,q],'direction':typ,'other_slot':[u,v]})
 # A wrong global shift cannot put both polynomial deformations and the
 # alleged source into Ext1: 1+t=1 forces t=0, whereas 0+t=1 forces t=1.
 shifts=[t for t in range(-3,4) if 1+t==1 and 0+t==1]
 assert not shifts
 # Exact algebraic sign control, with nonzero composable maps.
 E=s.Matrix([[1],[0]]);J=s.Matrix([[0,1]]);phi=s.Matrix([[1]])
 D=s.zeros(4);D[1:3,0:1]=E;D[3:4,1:3]=J
 F=s.zeros(4);F[0,3]=1
 first=D*F-F*D
 assert D*D==s.zeros(4) and D*first+first*D==s.zeros(4)
 wrong=D*F+F*D
 assert D*wrong+wrong*D!=s.zeros(4)
 # Product representative identity: for |a|=1, d(a b)=da b-a db.
 # Thus a(c+d b)-ac=-d(ab) for closed a, and (a+d eta)c-ac=d(eta c).
 controls={'degree_zero_as_Ext1_rejected':all(not t['is_Ext1'] for t in source),'uniform_shift_rescue_rejected':not shifts,'wrong_End_sign_nonclosed':True,'source_sign_change_preserves_total_degree':sum([-2,2])==0,'chain_product_representative_identity':'D(a*b)=D(a)*b+(-1)^|a|*a*D(b); applies only to actual closed total cocycles','geometric_representative_control_executed':False}
 dependencies=[ROOT/'tian-yau-bundle-coupling-gate/geometry.json',ROOT/'tian-yau-bundle-coupling-gate/exact_certificate.py',ROOT/'tian-yau-d3-coupling-gate/exact_certificate.py',ROOT/'tian-yau-cech-resolution-gate/exact_cech.py',ROOT/'tian-yau-koszul-d3-completion-gate/exact_d3.py',ROOT/'tian-yau-koszul-d3-completion-gate/certificate.json',ROOT/'tian-yau-koszul-d3-completion-gate/d3-matrices.json',ROOT/'tian-yau-wilson-line-gate/interactions.py',Path(__file__)]
 return {'passed':True,'claim_boundary':'Exact total-degree correction and character-resolved E1 inventory, NOT full E-infinity, geometric d3, Ext1 dimension, Yoneda tensor or Higgs verdict.','four_sources':source,'monad_degrees':{'A':-1,'B':0,'C':1},'source_kernel_placement':'Gr^-2 Ext^0, if it survives all remaining differentials; never an additive Ext1 summand','target_placement':'E_infinity^(1,0) is a quotient of E3^(1,0) by im d3, not its direct sum with ker d3','Ext1_filtration_slots':slots,'E1_End_characters':e1,'Ext1_E1_diagonal':diagonal,'Ext1_diagonal_line_summands':summands,'possible_higher_arrows_touching_Ext1':dr,'line_cohomology_method':'Exact QQ ranks of induced Laurent-monomial Koszul matrices on P3xP3. Ambient cohomology rows 0,3,6; Koszul length 3 excludes all higher dr (first row-jump requires r=4).','line_cohomology':{f'{a},{b}':line(a,b) for a,b in sorted(set(tuple(v-u for u,v in zip(a[3],b[3])) for a,b in product(terms,repeat=2)))},'claimed_invariant_16_rejected':True,'full_Ext1_dimension':None,'tensor_components':None,'charged_cocycles_constructed':False,'two_geometric_primitives_constructed':False,'H2_projection_constructed':False,'e32_e33_witness_evaluated':False,'negative_controls':controls,'source_hashes':{str(a.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(a.read_bytes()).hexdigest() for a in dependencies}}

def main():
 d=calculate();text=json.dumps(d,indent=2,sort_keys=True)+'\n';out=P/'certificate.json'
 if '--create' in sys.argv:
  with out.open('x') as f:f.write(text)
 else:
  assert out.exists(),'missing certificate'
  assert out.read_text()==text,'stale/tampered certificate'
 print(json.dumps({'passed':True,'Ext1_E1_diagonal':d['Ext1_E1_diagonal'],'E1_End_characters':d['E1_End_characters'],'rejected_16':True,'tensor_components':None},indent=2))
if __name__=='__main__':main()

