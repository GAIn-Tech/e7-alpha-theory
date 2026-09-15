from pathlib import Path
import urllib.request, concurrent.futures, subprocess, sys, json
import fitz
BASE=Path(__file__).resolve().parent
SCRIPT=Path('C:/Users/mikeb/AppData/Local/hermes/skills/research/grounded-citations/scripts/sources.py')
SOURCES=[('pacheco','https://arxiv.org/pdf/0804.1362'),('grana','https://arxiv.org/pdf/0904.2333'),('witten_flux','https://arxiv.org/pdf/hep-th/9609122'),('gkp','https://arxiv.org/pdf/hep-th/0105097'),('e7_stability','https://arxiv.org/pdf/0706.1893'),('sixd_review','https://arxiv.org/pdf/hep-th/0611133'),('sphere_index','https://arxiv.org/pdf/2001.02208'),('witten_jones','https://webhomes.maths.ed.ac.uk/~v1ranick/papers/witten.pdf'),('freed_index','https://arxiv.org/pdf/2107.03557'),('dirac1937','https://www.nature.com/articles/139323a0'),('wu_yang','https://encyclopediaofmath.org/wiki/Dirac_monopole')]
def cli(*args):
 return subprocess.check_output([sys.executable,str(SCRIPT),'--ledger',str(BASE/'ledger.json'),*args],text=True).strip()
for name,url in SOURCES: print(name,cli('add',url,'--title',name))
def fetch(item):
 name,url=item
 try:
  data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=75).read()
  if data.startswith(b'%PDF'):
   (BASE/(name+'.pdf')).write_bytes(data)
   doc=fitz.open(stream=data,filetype='pdf'); text='\n'.join(f'PAGE {i+1}\n'+p.get_text() for i,p in enumerate(doc))
  else:
   from bs4 import BeautifulSoup
   text=BeautifulSoup(data,'html.parser').get_text(' ',strip=True)
  (BASE/(name+'.txt')).write_text(text,encoding='utf-8')
  return {'name':name,'url':url,'chars':len(text),'ok':True}
 except Exception as e:return {'name':name,'url':url,'ok':False,'error':str(e)}
r=list(concurrent.futures.ThreadPoolExecutor(6).map(fetch,SOURCES)); (BASE/'retrieval.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
