"""Save exact excerpts from previously downloaded primary PDFs/texts."""
from pathlib import Path
import hashlib,json
P=Path(__file__).resolve().parent
specs=[
 ('yukawas','https://arxiv.org/pdf/2401.15078','4.3\nTian',3000,2900,'Explicit equations, free diagonal action, cover Hodge numbers'),
 ('yukawas','https://arxiv.org/pdf/2401.15078','Let us now specialize',0,2100,'SU3/E6 branching and cohomology; overbars may be lost in PDF text'),
 ('yukawas','https://arxiv.org/pdf/2401.15078','Hermitian',0,1400,'Standard embedding HYM and Ricci flat metric discussion'),
 ('triadophilia','https://people.maths.ox.ac.uk/szendroi/atmp_triadophilia.pdf','2.1\nThree families',3000,6100,'Tian-Yau family, generic freeness, quotient Hodge numbers'),
 ('triadophilia','https://people.maths.ox.ac.uk/szendroi/atmp_triadophilia.pdf','2.2\nSome quotients',3000,2300,'Prime Z3 bicubic quotient not three families'),
 ('composite12','https://arxiv.org/pdf/0910.5464','Abstract',0,1600,'Composite order12 free quotients with three net families')]
rows=[]
for name,url,marker,start,length,claim in specs:
 f=P/'sources'/(name+'.txt');t=f.read_text(encoding='utf-8');i=t.find(marker,start);assert i>=0,(name,marker)
 rows.append({'file':name+'.txt','url':url,'claim':claim,'offset':i,'quote':t[i:i+length],'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256(f.with_suffix('.pdf').read_bytes()).hexdigest()})
(P/'source_evidence.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Saved primary source excerpts: '+str(len(rows)))
