"""Read-only upstream fetch; isolated pinned Mathlib and dependency archives."""
import json,urllib.request,tarfile,time,concurrent.futures,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
REV='520045ab14e26149ee970e2e617ca04b09bde5d6'

def fetch(repo,rev,dest):
 archive=P/(repo.replace('/','_')+'-'+rev+'.tar.gz')
 if not archive.exists():
  for i in range(5):
   try:
    urllib.request.urlretrieve('https://codeload.github.com/'+repo+'/tar.gz/'+rev,archive)
    break
   except Exception:
    if i==4:raise
    time.sleep(2**i)
 dest.mkdir(parents=True,exist_ok=True)
 with tarfile.open(archive) as t:
  for m in t.getmembers():
   bits=m.name.split('/',1)
   if len(bits)<2 or not bits[1]:continue
   m.name=bits[1];t.extract(m,dest,filter='data')
 return {'repository':repo,'revision':rev,'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'destination':str(dest),'provenance':'GitHub commit-pinned codeload archive, not a git checkout'}

if __name__=='__main__':
 root=P/'mathlib-src'; receipts=[fetch('leanprover-community/mathlib4',REV,root)]
 print('MATHLIB_EXTRACTED',flush=True)
 manifest=json.loads((root/'lake-manifest.json').read_text())
 def dep(x):return fetch(x['url'].removeprefix('https://github.com/').removesuffix('.git'),x['rev'],root/'.lake/packages'/x['name'])
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:receipts+=list(pool.map(dep,manifest['packages']))
 (P/'mathlib_archive_provenance.json').write_text(json.dumps(receipts,indent=2))
 print('ARCHIVES_COMPLETE',len(receipts),flush=True)
