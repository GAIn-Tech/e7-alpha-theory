"""Fetch original primary papers, retain bytes/text/hashes and search excerpts."""
from pathlib import Path
import urllib.request,hashlib,json
H=Path(__file__).resolve().parent/'sources';H.mkdir(exist_ok=True)
items=[('orbifold','https://arxiv.org/pdf/hep-th/0110073'),('E7-global','https://arxiv.org/pdf/1007.4758'),('trace-normalization','https://arxiv.org/pdf/1008.1062'),('axion-quantization','https://arxiv.org/pdf/2309.03937'),('bardeen-gravity','https://arxiv.org/pdf/1107.0368')]
import fitz
out=[]
for name,url in items:
 try:
  data=urllib.request.urlopen(url,timeout=60).read();assert data.startswith(b'%PDF')
  (H/(name+'.pdf')).write_bytes(data)
  doc=fitz.open(stream=data,filetype='pdf');pages=[p.get_text() for p in doc]
  (H/(name+'.txt')).write_text('\n'.join('[PDF PAGE '+str(i+1)+']\n'+t for i,t in enumerate(pages)),encoding='utf-8')
  terms={'orbifold':['integration','localized','Green-Schwarz'],'E7-global':['Z3','Z 3','simply connected'],'trace-normalization':['normalization factors','Table 1'],'axion-quantization':['fractional','periodicity'],'bardeen-gravity':['Bardeen','diffeomorphism']}[name]
  excerpts=[]
  for i,t in enumerate(pages):
   for term in terms:
    at=t.lower().find(term.lower())
    if at>=0:excerpts.append({'pdf_page':i+1,'term':term,'excerpt':t[max(0,at-220):at+650]})
  out.append({'name':name,'url':url,'sha256':hashlib.sha256(data).hexdigest(),'pages':len(pages),'excerpts':excerpts,'status':'downloaded-primary'})
 except Exception as e:out.append({'name':name,'url':url,'status':'failed','error':str(e)})
(H/'ledger.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
