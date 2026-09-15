from pathlib import Path
import json, subprocess, sys
P=Path(__file__).resolve().parent
r=subprocess.run([sys.executable,'-B',str(P/'exact_cech.py')],check=True,capture_output=True,text=True)
c=json.loads((P/'certificate.json').read_text(encoding='utf-8'))
assert c['passed'] and c['cover']['count']==16
assert c['source']['characters']==[4,4,4] and not c['d3_computed']
for v in c['p3_monomial_contractions'].values():
    assert len(v['d'])==4 and len(v['h'])==4 and len(v['projector'])==4
print(json.dumps({'passed':True,'charts':16,'source_characters':[4,4,4],'d3_computed':False},indent=2))
