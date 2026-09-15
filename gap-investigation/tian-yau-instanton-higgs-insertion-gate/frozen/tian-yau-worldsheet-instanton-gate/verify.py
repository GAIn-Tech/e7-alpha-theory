#!/usr/bin/env python3
import json, subprocess, sys
from pathlib import Path
D=Path(__file__).resolve().parent
p=subprocess.run([sys.executable,'-B',str(D/'exact_certificate.py'),'--verify'],capture_output=True,text=True,cwd=D)
assert p.returncode==0,(p.stdout,p.stderr)
r=json.loads((D/'certificate.json').read_text(encoding='utf-8'))
assert r['cover_counts']=={'(1,0)':81,'(0,1)':81,'(1,1)_isolated':567,'(1,1)_rank1_no_solution':162,'(1,1)_families_rank0':0}
assert r['quotient_counts']=={'(1,0)':27,'(0,1)':27,'(1,1)':189,'total':243}
assert r['b11_rank_counts']=={'0':0,'1':162,'2':567}
assert r['tangent_restriction']['h0']==2
assert r['pfaffian']['V=TQ']=='zero for every listed curve'
for name in ['REPORT.md','RELEASE_DISCLOSURE.md','sources/evidence-notes.md']:
    assert (D/name).is_file() and (D/name).stat().st_size>500
print(json.dumps({'passed':True,'certificate':json.loads(p.stdout),'files_checked':4},sort_keys=True))
