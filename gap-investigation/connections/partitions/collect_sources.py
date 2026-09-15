from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
import requests, subprocess, sys, json
ROOT=Path('C:/Users/mikeb/e7-alpha-theory/gap-investigation/connections/partitions')
S=Path('C:/Users/mikeb/AppData/Local/hermes/skills/research/grounded-citations/scripts/sources.py')
SOURCES=[
('ramanujan','https://pmc.ncbi.nlm.nih.gov/articles/PMC60793/'),
('chiral','https://arxiv.org/html/1604.08837v1'),
('dedekind','https://arxiv.org/html/2302.04615v1'),
('narain','https://fisica.usac.edu.gt/public/curccaf_proc/quevedo1/node4.html'),
('blackholes','https://arxiv.org/html/1208.4074v2'),
('k3','https://arxiv.org/html/1112.5106v2'),
('selfconjugate','https://www.whitman.edu/mathematics/cgt_online/book/section03.03.html'),
('nimbers','https://en.wikipedia.org/wiki/Nimber'),
('rademacher','https://btw-47.github.io/rademacher2.pdf'),
('scarcity','https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-ahlg-beck-raum.pdf'),
('mocknotes','https://swc-math.github.io/aws/2013/2013OnoNotes.pdf'),
('e7','https://en.wikipedia.org/wiki/E7_(mathematics)')]
class Text(HTMLParser):
 def __init__(self): super().__init__(); self.out=[]; self.skip=0
 def handle_starttag(self,t,a):
  if t in ('script','style'): self.skip+=1
 def handle_endtag(self,t):
  if t in ('script','style'): self.skip=max(0,self.skip-1)
 def handle_data(self,d):
  if not self.skip and d.strip(): self.out.append(d.strip())
def fetch(pair):
 name,url=pair
 try:
  r=requests.get(url,timeout=90); r.raise_for_status()
  if url.endswith('.pdf'):
   (ROOT/(name+'.pdf')).write_bytes(r.content)
   import pymupdf
   doc=pymupdf.open(stream=r.content,filetype='pdf'); text='\n'.join(p.get_text() for p in doc)
  else:
   p=Text(); p.feed(r.text); text='\n'.join(p.out)
  (ROOT/(name+'.txt')).write_text(text,encoding='utf-8')
  return {'name':name,'url':url,'chars':len(text),'status':'retrieved'}
 except Exception as e: return {'name':name,'url':url,'status':'failed','error':str(e)}
if __name__=='__main__':
 ROOT.mkdir(parents=True,exist_ok=True)
 receipts=list(ThreadPoolExecutor(8).map(fetch,SOURCES))
 for row in receipts:
  if row['status']=='retrieved':
   p=subprocess.run([sys.executable,str(S),'--ledger',str(ROOT/'ledger.json'),'add',row['url'],'--title',row['name']],capture_output=True,text=True)
   row['ledger_result']=p.stdout.strip()
 (ROOT/'retrieval.json').write_text(json.dumps(receipts,indent=2),encoding='utf-8')
 print(json.dumps(receipts,indent=2))
