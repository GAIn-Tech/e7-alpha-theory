"""Replay endpoint derivation without assigning any matrix entry."""
import readback_survivors as r
import json,hashlib,sys
c,P=r.c,r.P

def calculate():
 d=json.loads((P/'d4-chains.json').read_text());records=[]
 for rec in d['records']:
  vs=[r.unpack(rec['initial_source'])]+[r.unpack(t) for t in rec['primitives']]
  steps=[]
  for k in range(1,5):
   left=c.d1(vs[k-1]);right=c.d2cor(vs[k-2]) if k>=2 else {}
   rhs=c.add(left,right)
   residual=c.add(rhs,c.dv(vs[k])) if k<4 else rhs
   assert not residual
   steps.append({'horizontal_step':k,'End_terms':len(left),'curvature_terms':len(right),'rhs_terms':len(rhs),'vertical_primitive_terms':len(vs[k]) if k<4 else None,'checked_residual_terms':len(residual)})
  left=c.d1(vs[3]);right=c.d2cor(vs[2])
  assert left==c.scale(right,-1)
  neg=c.add(left,c.scale(right,-1))
  if left:assert neg
  records.append({'column':rec['column'],'steps':steps,'fourth_End_component':c.pack(left),'fourth_curvature_component':c.pack(right),'wrong_endpoint_curvature_sign_terms':len(neg)})
 return {'passed':True,'chain_payload_sha256':hashlib.sha256((P/'d4-chains.json').read_bytes()).hexdigest(),'records':records,'boundary':'Each fourth endpoint is recomputed as d1(a3)+d2cor(a2). First two cancel 39 nonzero terms; last two have individually vanishing fourth components after the third-step cancellation.'}
if __name__=='__main__':
 d=calculate();text=json.dumps(d,sort_keys=True,indent=2)+'\n';p=P/'endpoint-derivation.json'
 if '--create' in sys.argv:
  with p.open('x',newline='\n') as f:f.write(text)
 else:assert p.is_file() and p.read_text()==text
 print(json.dumps({'passed':d['passed'],'columns':[{'column':v['column'],'steps':v['steps'],'wrong_endpoint_curvature_sign_terms':v['wrong_endpoint_curvature_sign_terms']} for v in d['records']]},indent=2))
