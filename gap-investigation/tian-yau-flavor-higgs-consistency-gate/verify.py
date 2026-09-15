"""Replay exact saved gate without regeneration; immutable/missing/tamper controls."""
from pathlib import Path
import hashlib,json,tempfile
import calculate as c
P=Path(__file__).resolve().parent

def check(path,payload):
 assert path.is_file(),'missing saved certificate'
 assert path.read_text()==payload,'tampered saved certificate'

def main():
 manifest=json.loads((P/'release-manifest.json').read_text())
 def frozen():
  for name,h in manifest.items():assert c.sha(P/name)==h,name
 frozen()
 saved=(P/'certificate.json').read_bytes()
 payload=c.enc(c.calculate());check(P/'certificate.json',payload)
 controls={}
 with tempfile.TemporaryDirectory(prefix='receipt-controls-',dir=P) as temp:
  f=Path(temp)/'certificate.json'
  try:check(f,payload)
  except AssertionError:controls['missing_rejected']=True
  else:raise AssertionError('missing accepted')
  f.write_text(payload.replace('"passed": true','"passed": false',1))
  assert f.read_text()!=payload
  try:check(f,payload)
  except AssertionError:controls['tampered_rejected']=True
  else:raise AssertionError('tamper accepted')
 frozen();assert (P/'certificate.json').read_bytes()==saved
 print(c.enc({'passed':True,'mode':'immutable replay','certificate_sha256':c.sha(P/'certificate.json'),'release_manifest_sha256':c.sha(P/'release-manifest.json'),'controls':controls,'source_and_receipt_unchanged':True}),end='')
if __name__=='__main__':main()
