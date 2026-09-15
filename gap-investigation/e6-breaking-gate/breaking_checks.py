"""Exact compact stabilizers of weight-line VEVs, not a vacuum solver."""
from pathlib import Path
from fractions import Fraction as F
import importlib.util,json,hashlib,sys
HERE=Path(__file__).resolve().parent
PRE=HERE.parent/'embedding-gate/embedding_checks.py'
def load():
 s=importlib.util.spec_from_file_location('embedding',PRE);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def rank(rows):
 a=[list(map(F,r)) for r in rows];i=0
 for j in range(len(a[0]) if a else 0):
  k=next((k for k in range(i,len(a)) if a[k][j]),None)
  if k is None:continue
  a[i],a[k]=a[k],a[i];d=a[i][j];a[i]=[x/d for x in a[i]]
  for k in range(len(a)):
   if k!=i:
    d=a[k][j];a[k]=[x-d*y for x,y in zip(a[k],a[i])]
  i+=1
 return i
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def compute():
 m=load();pr=m.replay();A=[r[:6] for r in pr['cartan'][:6]];t=m.load()
 W=m.orbit((0,0,0,0,0,1),A);assert len(W)==27
 R=[tuple(sum(r[i]*A[i][j] for i in range(6)) for j in range(6)) for r in t.positive_roots(A)];R+= [tuple(-x for x in r) for r in R]
 su=[0,2,3,4];sing=sorted(w for w in W if all(w[i]==0 for i in su));assert len(sing)==2
 Y=[F(0)]*6
 for i,c in zip(su,[F(-1,3),F(-2,3),F(-1),F(-1,2)]):Y[i]=c
 # SM singlets are joint SU3,SU2 invariants with zero Y. Minuscule strings tested, not just zero Dynkin labels.
 smnodes=[su[0],su[1],su[3]]
 sms=[w for w in W if dot(w,Y)==0 and all(w[i]==0 for i in smnodes)]
 assert sorted(sms)==sing
 def stabilizer(vs,adj=False):
  # Compact real root plane survives iff BOTH E_alpha and E_-alpha kill EACH VEV.
  # For weight basis VEVs different root outputs cannot cancel; Cartan outputs are on original weights.
  roots=[r for r in R if all(tuple(w[i]+r[i] for i in range(6)) not in W and tuple(w[i]-r[i] for i in range(6)) not in W for w in vs) and (not adj or dot(r,Y)==0)]
  cartan=6-rank(vs)
  return {'root_count':len(roots),'cartan_dimension':cartan,'dimension':len(roots)+cartan,'roots':[list(r) for r in sorted(roots)]}
 one=[stabilizer([s]) for s in sing];two=stabilizer(sing);sm=stabilizer(sing,True)
 assert [r['dimension'] for r in one]==[45,45] and two['dimension']==24 and sm['dimension']==12
 assert two['cartan_dimension']==4 and sm['root_count']==8
 # Root subset identification, not dimension-only names.
 G=m.inverse(A)
 def coeff(r):return [sum(F(r[j])*G[j][i] for j in range(6)) for i in range(6)]
 suroots=[r for r in R if all(coeff(r)[i]==0 for i in [1,5])]
 assert set(map(tuple,two['roots']))==set(suroots)
 assert set(map(tuple,sm['roots']))=={r for r in suroots if dot(r,Y)==0}
 # minuscule pairings certify actual nonzero root-string action
 transitions=sum(tuple(w[i]+r[i] for i in range(6)) in W for w in W for r in R)
 assert all(dot(w,coeff(r)) in [-1,0,1] for w in W for r in R)
 # Explicit charge-selected cubic monomials: zero-weight triples exist; singlet-only restriction vanishes.
 triples=[(a,b,c) for ia,a in enumerate(sorted(W)) for ib,b in enumerate(sorted(W)) if ib>=ia for c in sorted(W)[ib:] if all(a[i]+b[i]+c[i]==0 for i in range(6))]
 assert triples and not any(all(w in sing for w in tri) for tri in triples)
 norm=2*sum(Y[i]*A[i][j]*Y[j] for i in range(6) for j in range(6));assert norm==F(5,3)
 assert all(stabilizer([s],True)['dimension']==13 for s in sing)
 files=[Path(__file__),PRE,m.SOURCE,m.PROVENANCE,HERE/'sources/evidence-notes.md']
 return {'passed':True,'claim_boundary':'Exact compact stabilizer for explicit independent weight VEVs; external minuscule representation theory. Not full potential stability, global gauge group, anomaly repair or phenomenology.', 'sources':{str(p):sha(p) for p in files},'weights27':[list(w) for w in sorted(W)],'singlets':sing,'Y_coroot':[str(x) for x in Y],'kY':str(norm),'root_transitions':transitions,'one_weight':one,'two_independent':two,'two_plus_Yadjoint':sm,'unordered_zero_weight_cubic_triples':len(triples),'X_Yukawa_scalar_charge':-2}
def replay(path=None):
 p=HERE/'breaking-receipt.json' if path is None else Path(path)
 old=json.loads(p.read_text());new=json.loads(json.dumps(compute()));assert old==new,'Receipt mismatch';return new
if __name__=='__main__':
 if '--create' in sys.argv:
  r=compute()
  with (HERE/'breaking-receipt.json').open('x') as f:json.dump(r,f,indent=2)
 else:r=replay()
 print(json.dumps({'passed':r['passed'],'singlets':r['singlets'],'dimensions':[x['dimension'] for x in r['one_weight']]+[r['two_independent']['dimension'],r['two_plus_Yadjoint']['dimension']],'root_transitions':r['root_transitions'],'kY':r['kY']}))
