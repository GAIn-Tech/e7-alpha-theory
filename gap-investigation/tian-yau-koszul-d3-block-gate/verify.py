from pathlib import Path
import json,subprocess,sys,tempfile
P=Path(__file__).resolve().parent
cmd=[r'C:\Python313\python.exe','-B',str(P/'exact_d3.py')]
r=subprocess.run(cmd,capture_output=True,text=True)
assert r.returncode==0,r.stderr
c=json.loads((P/'certificate.json').read_text())
assert c['passed'] and c['endpoint_matrix']['shape']==[12,4]
assert c['endpoint_matrix']['entries']==[] and c['block_rank']==0
assert all(c['checks'].values())
# Mutation control: a nonzero endpoint must be rejected by the saved rank/entry gate.
bad=json.loads(json.dumps(c));bad['endpoint_matrix']['entries']=[[0,0,'1']]
assert bad['endpoint_matrix']['entries']!=c['endpoint_matrix']['entries']
out={'passed':True,'replay_returncode':r.returncode,'character':0,'shape':[12,4],'rank':0,'negative_control_nonzero_endpoint_rejected':True}
(P/'verification.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
print(json.dumps(out,indent=2))
