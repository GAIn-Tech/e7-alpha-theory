"""Bounded source recovery; save each receipt before next network call."""
from pathlib import Path
import subprocess,json,hashlib,datetime
D=Path(__file__).resolve().parent/'sources';D.mkdir(exist_ok=True)
urls={
 'deppisch.pdf':'https://arxiv.org/pdf/1605.05920',
 'kephart-vaughn-kek.pdf':'https://lib-extopc.kek.jp/preprints/PDF/1981/8111/8111149.pdf',
 'kalashnikov-inspire.json':'https://inspirehep.net/api/literature/141557',
 'kephart-inspire.json':'https://inspirehep.net/api/literature/167756',
 'kalashnikov-publisher.html':'https://www.sciencedirect.com/science/article/pii/0550321380902102',
 'kalashnikov-wayback.json':'https://archive.org/wayback/available?url=https%3A%2F%2Fwww.sciencedirect.com%2Fscience%2Farticle%2Fpii%2F0550321380902102',
 'kalashnikov-archive.html':'https://archive.ph/newest/https://www.sciencedirect.com/science/article/pii/0550321380902102'
}
out=[]
for name,url in urls.items():
 p=D/name;item={'file':name,'url':url}
 if p.exists():item['retrieval']='saved during interrupted initial requests run; HTTP status not retained'
 else:
  r=subprocess.run(['curl','-L','--max-time','45','-sS','-w','%{http_code}','-o',str(p),url],capture_output=True,text=True,timeout=55)
  item.update(exit=r.returncode,http_status=r.stdout,stderr=r.stderr)
 if p.exists():
  body=p.read_bytes();item.update(bytes=len(body),sha256=hashlib.sha256(body).hexdigest(),pdf_header=body.startswith(b'%PDF'))
  if body.startswith(b'%PDF'):
   import pymupdf
   doc=pymupdf.open(p);txt=D/(name+'.txt');txt.write_text('\n'.join('PDF PAGE '+str(i+1)+'\n'+pg.get_text() for i,pg in enumerate(doc)),encoding='utf-8')
   item.update(pages=len(doc),text_characters=len(txt.read_text(encoding='utf-8')))
 item['receipt_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();out.append(item)
 (D/'retrieval-receipt.json').write_text(json.dumps(out,indent=2));print(json.dumps(item),flush=True)
