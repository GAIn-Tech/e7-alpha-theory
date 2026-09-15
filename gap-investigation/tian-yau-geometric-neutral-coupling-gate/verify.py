"""Read-only native replay and exclusive release freeze, confined to this lane."""
from pathlib import Path
import sys,hashlib,json,subprocess,tempfile
P=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
text=lambda x:json.dumps(x,sort_keys=True,indent=2)+'\n'

def check_file(path,expected):
 assert path.is_file(),f'missing {path}'
 assert sha(path)==expected,f'tampered {path}'

def main():
 manifest=P/'release-manifest.json'; output=P/'verification.json'
 create='--create' in sys.argv
 if create:
  assert not manifest.exists() and not output.exists()
  files=[P/n for n in ['calculate.py','verify.py','certificate.json','REPORT.md','RELEASE_DISCLOSURE.md','formalization.yaml','setup_sources.py']]
  files+=list((P/'sources').glob('*'))
  data={str(f.relative_to(P)).replace('\\','/'):sha(f) for f in sorted(files) if f.is_file()}
  with manifest.open('x',encoding='utf-8',newline='\n') as f:f.write(text(data))
 else: assert manifest.is_file() and output.is_file(),'missing frozen release evidence'
 data=json.loads(manifest.read_text(encoding='utf-8'))
 for rel,h in data.items():check_file(P/rel,h)
 before=sha(manifest)
 r=subprocess.run([sys.executable,'-B',str(P/'calculate.py')],capture_output=True,text=True)
 assert r.returncode==0,r.stdout+r.stderr
 payload=json.loads(r.stdout); assert payload['passed']
 for rel,h in data.items():check_file(P/rel,h)
 assert sha(manifest)==before
 with tempfile.TemporaryDirectory(dir=P,prefix='verify-controls-') as temp:
  f=Path(temp)/'receipt.json'; good=(P/'certificate.json').read_bytes(); expected=hashlib.sha256(good).hexdigest()
  try:check_file(f,expected)
  except AssertionError:missing=True
  else:raise AssertionError('missing receipt accepted')
  f.write_bytes(good+b' ')
  try:check_file(f,expected)
  except AssertionError:tamper=True
  else:raise AssertionError('tampered receipt accepted')
  f.write_bytes(good);check_file(f,expected)
 result={'passed':True,'command':[sys.executable,'-B',str(P/'calculate.py')],'returncode':r.returncode,'manifest_sha256':before,'certificate_sha256':sha(P/'certificate.json'),'release_file_count':len(data),'source_and_receipt_bytes_unchanged':True,'missing_receipt_rejected':missing,'tampered_receipt_rejected':tamper,'calculation_stdout_sha256':hashlib.sha256(r.stdout.encode()).hexdigest(),'scope':'Immutable local exact replay. External geometric/PQ theorems are written proof inputs, not Lean-checked; no full string vacuum.'}
 if create:
  with output.open('x',encoding='utf-8',newline='\n') as f:f.write(text(result))
 else:assert output.read_text(encoding='utf-8')==text(result)
 print(text(result))
if __name__=='__main__':main()
