"""Preserve primary retrieval text and evidence; no source inference."""
from pathlib import Path
import requests,pymupdf,json,subprocess,sys,concurrent.futures,hashlib
H=Path(__file__).resolve().parent
S='C:/Users/mikeb/AppData/Local/hermes/skills/research/grounded-citations/scripts/sources.py'
items=[(1,'https://arxiv.org/pdf/hep-th/0110073','Notice that this mechanism can work only when the integrated anomaly vanishes.'),(2,'https://arxiv.org/pdf/hep-th/0202144','there is no periodic'),(3,'https://arxiv.org/pdf/hep-th/0103135','Again this is independent of the shape of the chiral zero mode.'),(4,'https://arxiv.org/html/1001.4074v3','two oppositely charged chiral superfields'),(5,'https://par.nsf.gov/servlets/purl/10635146','E6 admits complex representations')]
def fetch(item):
 i,url,needle=item
 r=requests.get(url,timeout=90);r.raise_for_status()
 if r.content[:4]==b'%PDF':
  (H/f'primary-{i}.pdf').write_bytes(r.content)
  with pymupdf.open(stream=r.content,filetype='pdf') as d:text='\n'.join(p.get_text() for p in d)
 else:
  from html.parser import HTMLParser
  class Text(HTMLParser):
   def handle_data(self,data): self.parts.append(data)
  parser=Text();parser.parts=[];parser.feed(r.text);text=' '.join(parser.parts)
 p=H/f'primary-{i}.txt';p.write_text(text,encoding='utf-8')
 normalized=' '.join(text.split()); at=normalized.casefold().find(needle.casefold())
 assert at>=0,(i,'quote not found')
 quote=normalized[at:at+len(needle)]
 c=[sys.executable,S,'--ledger',str(H/'research-ledger.json'),'quote',str(i),'--text',quote,'--from',str(p)]
 # Ledger writes serialized below.
 return {'id':i,'url':url,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'command':c}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:rows=list(pool.map(fetch,items))
for row in rows:
 p=subprocess.run(row.pop('command'),text=True,capture_output=True);row.update(exit_code=p.returncode,output=p.stdout+p.stderr);print(row)
 assert p.returncode==0
(H/'retrieval.json').write_text(json.dumps(rows,indent=2))
