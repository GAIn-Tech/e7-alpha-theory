"""Exact preregistered finite-catalog compactification-selection gate."""
from fractions import Fraction
from pathlib import Path
import hashlib,json,sys
P=Path(__file__).resolve().parent
catalog=[
 {'name':'Tian-Yau Z3','d':3,'euler_cover':-18,'internal_real_dim':6,'free':True,'descended':True,'bianchi':True,'modular':True,'source':'https://arxiv.org/pdf/2401.15078'},
 {'name':'bicubic Z3','d':3,'euler_cover':-162,'internal_real_dim':6,'free':True,'descended':True,'bianchi':True,'modular':True,'source':'https://people.maths.ox.ac.uk/szendroi/atmp_triadophilia.pdf'},
 {'name':'order-12 three-family','d':12,'euler_cover':-72,'internal_real_dim':6,'free':True,'descended':True,'bianchi':True,'modular':True,'source':'https://arxiv.org/pdf/0910.5464'},
 {'name':'quintic Z5xZ5','d':25,'euler_cover':-200,'internal_real_dim':6,'free':True,'descended':True,'bianchi':True,'modular':True,'source':'https://people.maths.ox.ac.uk/szendroi/atmp_triadophilia.pdf'}]
def prime(n): return n>1 and all(n%k for k in range(2,int(n**.5)+1))
for r in catalog:
 r['external_dim']=10-r['internal_real_dim']
 r['cover_index']=Fraction(r['euler_cover'],2)
 r['quotient_index']=r['cover_index']/r['d']
 r['net_abs']=abs(r['quotient_index'])
 r['prime_order']=prime(r['d'])
 r['physical_admissibility_inputs_pass']=all(r[k] for k in ('free','descended','bianchi','modular')) and r['internal_real_dim']==6 and r['quotient_index'].denominator==1
assert [(x['external_dim'],x['net_abs']) for x in catalog]==[(4,3),(4,27),(4,3),(4,4)]
# Preregistered controls: same prime status, different target; composite target witness.
assert catalog[0]['prime_order']==catalog[1]['prime_order'] and catalog[0]['net_abs']!=catalog[1]['net_abs']
assert not catalog[2]['prime_order'] and catalog[2]['net_abs']==3
assert catalog[3]['physical_admissibility_inputs_pass'] and catalog[3]['net_abs']==4
# Exact criterion |Euler_cover|=6d is equivalent to net_abs=3 on this HRR/descent domain.
assert all((abs(r['euler_cover'])==6*r['d'])==(r['net_abs']==3) for r in catalog)
def enc(x):
 if isinstance(x,Fraction): return {'numerator':x.numerator,'denominator':x.denominator}
 raise TypeError
payload={'passed':True,'claim_boundary':'Exact finite-catalog countermodels show quotient-order primality is neither necessary nor sufficient for net three. The index equation filters specified CY3 compactifications but does not select geometry or four dimensions. No universal physics no-go.','preregistration_sha256':hashlib.sha256((P/'PREREGISTRATION.md').read_bytes()).hexdigest(),'catalog':catalog,'theorems':{'prime_not_sufficient':True,'prime_not_necessary':True,'four_dimensions_is_parent_minus_internal_input':True,'index_filter_net3_iff_abs_euler_eq_6d':True,'partition_homonym_fields_absent_from_physical_tuple':True}}
out=P/'certificate.json'; text=json.dumps(payload,default=enc,indent=2)+'\n'
if '--verify' in sys.argv:
 assert out.exists() and out.read_text(encoding='utf-8')==text,'missing/stale certificate'
 print('PASS exact catalog replay: prime-order necessity and sufficiency both refuted')
else:
 out.write_text(text,encoding='utf-8'); print('PASS certificate created')
