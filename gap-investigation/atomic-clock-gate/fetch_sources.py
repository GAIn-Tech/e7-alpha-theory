from pathlib import Path
import urllib.request,json,hashlib,datetime,subprocess,sys
from html.parser import HTMLParser
P=Path(__file__).resolve().parent
class Text(HTMLParser):
 def __init__(self): super().__init__(); self.parts=[]; self.skip=0
 def handle_starttag(self,t,a):
  if t in ('script','style'): self.skip+=1
 def handle_endtag(self,t):
  if t in ('script','style'): self.skip-=1
 def handle_data(self,d):
  if not self.skip and d.strip(): self.parts.append(d.strip())
urls=[('hyperphysics','http://hyperphysics.phy-astr.gsu.edu/hbase/acloc.html'),('bipm','https://www.bipm.org/en/si-base-units/second'),('codata','https://physics.nist.gov/cgi-bin/cuu/Value?alphinv'),('nist-comparison','https://tf.nist.gov/general/pdf/2295.pdf'),('nist-network','https://www.nist.gov/news-events/news/2021/03/nist-team-compares-3-top-atomic-clocks-record-accuracy-over-both-fiber-and'),('network-paper','https://www.nature.com/articles/s41586-021-03253-4')]
S=Path('C:/Users/mikeb/AppData/Local/hermes/skills/research/grounded-citations/scripts/sources.py')
rows=[]
for name,url in urls:
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=90) as r: data=r.read(); final=r.url; status=r.status
  ext='.pdf' if data.startswith(b'%PDF') else '.html'; raw=P/(name+ext); raw.write_bytes(data)
  if ext=='.pdf':
   import fitz
   doc=fitz.open(raw); text='\n'.join(page.get_text() for page in doc)
  else:
   parser=Text(); parser.feed(data.decode('utf-8',errors='replace')); text='\n'.join(parser.parts)
  (P/(name+'.txt')).write_text(text,encoding='utf-8')
  q=subprocess.run([sys.executable,str(S),'--ledger',str(P/'citations.json'),'add',url,'--title',name],capture_output=True,text=True); print(q.stdout,q.stderr)
  rows.append(dict(name=name,url=url,final_url=final,status=status,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),text_sha256=hashlib.sha256(text.encode()).hexdigest(),retrieved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))
  print(name,len(data),len(text))
 except Exception as e: rows.append(dict(name=name,url=url,error=repr(e))); print(name,repr(e))
(P/'source-receipt.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
