from pathlib import Path
import json,subprocess,hashlib
P=Path(__file__).resolve().parent
cert=P/'certificate.json'; before=hashlib.sha256(cert.read_bytes()).hexdigest()
r=subprocess.run([r'C:\Python313\python.exe','-B',str(P/'exact_d3.py')],capture_output=True,text=True)
assert r.returncode==0,r.stderr
after=hashlib.sha256(cert.read_bytes()).hexdigest(); assert before==after
c=json.loads(cert.read_text())
assert c['passed'] and c['block_ranks']==[0,0,0]
assert [c['blocks'][str(i)]['endpoint_matrix']['shape'] for i in range(3)]==[[12,4],[14,4],[14,4]]
assert all(c['blocks'][str(i)]['endpoint_matrix']['entries']==[] for i in range(3))
assert c['surviving_neutral_classes']['invariant_descended']==16
assert c['yoneda_action']['computed_subspace_dimension']==12 and c['yoneda_action']['unresolved_survivor_dimension']==4
out={'passed':True,'canonical_replay_returncode':r.returncode,'certificate_sha256':after,'shapes':[[12,4],[14,4],[14,4]],'ranks':[0,0,0],'invariant_neutral':16,'charged_action_complete':False}
(P/'verification.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
print(json.dumps(out,indent=2))
