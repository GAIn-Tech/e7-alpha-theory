from pathlib import Path
import shutil, urllib.request, hashlib, json, subprocess
P=Path(__file__).resolve().parent
S=P/'sources'; S.mkdir(exist_ok=True)
root=P.parent
copies={'witten.txt':root/'connections/knots/witten1989.txt','jones.txt':root/'connections/knots/jones.txt','mukhi.txt':root/'connections/knots/mukhi2020.txt','dilaton.txt':root/'tian-yau-clock-response-gate/sources/dilaton.txt','modular-report.md':root/'modular-completion-gate/REPORT.md','modular-algebra.py':root/'modular-completion-gate/exact_certificate.py'}
for name,src in copies.items(): shutil.copyfile(src,S/name)
u='https://arxiv.org/pdf/1611.09442'
with urllib.request.urlopen(u,timeout=90) as r: data=r.read(); final=r.url
(S/'threshold.pdf').write_bytes(data)
import pymupdf
with pymupdf.open(S/'threshold.pdf') as d: (S/'threshold.txt').write_text('\n'.join(page.get_text() for page in d),encoding='utf-8')
urls=[('https://webhomes.maths.ed.ac.uk/~v1ranick/papers/witten.pdf','Witten: Quantum Field Theory and the Jones Polynomial','witten.txt'),('https://math.berkeley.edu/~vfr/jones.pdf','Jones: The Jones Polynomial','jones.txt'),('https://arxiv.org/pdf/2011.09487','Mukhi and Poddar: Universal Correlators and Novel Cosets','mukhi.txt'),('https://arxiv.org/pdf/2305.08263','Kim: On one-loop corrected dilaton action','dilaton.txt'),(u,'Angelantonj Israel Sarkis: Threshold corrections in heterotic flux compactifications','threshold.txt')]
cli=Path('C:/Users/mikeb/AppData/Local/hermes/skills/research/grounded-citations/scripts/sources.py')
import sys
for url,title,file in urls:
 r=subprocess.run([sys.executable,str(cli),'--ledger',str(S/'ledger.json'),'add',url,'--title',title],capture_output=True,text=True); print(r.stdout,r.stderr);assert r.returncode==0
manifest={'new_retrieval':{'requested':u,'final':final,'bytes':len(data)},'files':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(S.iterdir()) if f.name!='ledger.json'},'inherited_sources':{k:str(v) for k,v in copies.items()}}
(S/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Prepared native lane',P)
