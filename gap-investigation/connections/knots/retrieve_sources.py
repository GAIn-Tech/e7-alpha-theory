from pathlib import Path
import requests, concurrent.futures, json, hashlib, subprocess
import pymupdf
BASE=Path('C:/Users/mikeb/e7-alpha-theory/gap-investigation/connections/knots')
S=Path('C:/Users/mikeb/AppData/Local/hermes/skills/research/grounded-citations/scripts/sources.py')
SOURCES=[
('witten1989','Quantum Field Theory and the Jones Polynomial','https://webhomes.maths.ed.ac.uk/~v1ranick/papers/witten.pdf'),
('kauffman1988','New invariants in the theory of knots','https://www.numdam.org/item/AST_1988__163-164__137_0.pdf'),
('mukhi2020','Universal Correlators and Novel Cosets in 2d RCFT','https://arxiv.org/pdf/2011.09487'),
('fuchs1997','A representation theoretic approach to the WZW Verlinde formula','https://cds.cern.ch/record/329645/files/9707069.pdf'),
('gukov2005','Khovanov-Rozansky Homology and Topological Strings','https://arxiv.org/pdf/hep-th/0412243'),
('witten2011','Fivebranes and Knots','https://ems.press/content/serial-article-files/36765'),
('warnaar2010','Dedekinds eta-function and Rogers-Ramanujan identities','https://arxiv.org/pdf/1001.1571'),
('coincidences','Knot polynomial identities and quantum group coincidences','https://ems.press/content/serial-article-files/36754')]
def get(s):
 name,title,url=s
 try:
  r=requests.get(url,timeout=80);r.raise_for_status(); assert r.content.startswith(b'%PDF'),r.headers.get('content-type')
  p=BASE/(name+'.pdf');p.write_bytes(r.content)
  d=pymupdf.open(p);text='\n'.join(f'\n--- PAGE {i+1} ---\n'+page.get_text() for i,page in enumerate(d))
  (BASE/(name+'.txt')).write_text(text,encoding='utf-8')
  return dict(name=name,title=title,url=url,sha256=hashlib.sha256(r.content).hexdigest(),pages=len(d),characters=len(text),ok=True)
 except Exception as e:return dict(name=name,title=title,url=url,ok=False,error=str(e))
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: rows=list(ex.map(get,SOURCES))
 for row in rows:
  out=subprocess.run(['python',str(S),'--ledger',str(BASE/'sources-ledger.json'),'add',row['url'],'--title',row['title']],capture_output=True,text=True)
  row['citation_registration']=out.stdout.strip();print(json.dumps(row))
 (BASE/'retrieval_manifest.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
