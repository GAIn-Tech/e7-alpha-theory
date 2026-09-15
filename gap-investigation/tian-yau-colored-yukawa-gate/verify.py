"""Immutable replay: never generates, replaces or repairs a missing certificate."""
import sys,json,hashlib,subprocess
from pathlib import Path
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parent

def check(manifest,overrides=None):
 overrides=overrides or {}
 for name,expected in manifest.items():
  if name in overrides:
   payload=overrides[name]
   if payload is None:raise AssertionError('missing artifact: '+name)
  else:
   f=P/name
   assert f.is_file(),'missing artifact: '+name
   payload=f.read_bytes()
  assert hashlib.sha256(payload).hexdigest()==expected,'changed artifact: '+name

def main():
 manifest=json.loads((P/'release-manifest.json').read_text());check(manifest)
 for name in ['source-manifest.json','dual-source-manifest.json','supplementary-source-manifest.json']:
  check(json.loads((P/name).read_text()))
 for override in [None,(P/'certificate.json').read_bytes()+b'\n']:
  try:check(manifest,{'certificate.json':override})
  except AssertionError:pass
  else:raise AssertionError('missing/tampered receipt was accepted')
 for script in ['calculate.py','charged_dual_bases.py','supplementary_audit.py']:
  print('REPLAY',script,flush=True)
  run=subprocess.run([sys.executable,'-B',str(P/script)],cwd=P)
  assert run.returncode==0,(script,run.returncode)
  check(manifest)
 print(json.dumps({'passed':True,'missing_receipt_rejected':True,'tampered_receipt_rejected':True,'absolute_residue_comparison_complete':False,'conjugate_slices_computed':False,'certificate_sha256':hashlib.sha256((P/'certificate.json').read_bytes()).hexdigest()},indent=2),flush=True)
if __name__=='__main__':main()
