from pathlib import Path
import subprocess,sys,json
P=Path(__file__).resolve().parent
S=Path('C:/Users/mikeb/AppData/Local/hermes/skills/research/grounded-citations/scripts/sources.py')
def run(*args):
 r=subprocess.run([sys.executable,str(S),'--ledger',str(P/'citations.json'),*args],capture_output=True,text=True,encoding='utf-8'); print(r.stdout,r.stderr); assert r.returncode==0; return {'args':list(args),'returncode':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
queries=[(1,'hyperphysics','Very accurate clocks'),(2,'bipm','It is defined by taking'),(3,'codata','137.035'),(4,'nist-comparison','Temporal variation of Ry is common'),(5,'nist-network','frequency ratios'),(6,'network-paper','Here we operate a network')]
logs=[]
for id,name,needle in queries:
 t=(P/(name+'.txt')).read_text(encoding='utf-8'); i=t.index(needle); quote=t[i:i+600]; logs.append(run('quote',str(id),'--text',quote,'--from',str(P/(name+'.txt'))))
logs.append(run('render','--style','evidence','--replace-in',str(P/'REPORT.md')))
logs.append(run('verify',str(P/'REPORT.md'),'--evidence','--strict'))
import fitz
pages=len(fitz.open(P/'nist-comparison.pdf'))
t=(P/'hyperphysics.txt').read_text(encoding='utf-8'); sections=['Atomic Clocks','Cesium Atomic Clock','Description of the Cesium Atom','Rubidium Atomic Clock']; assert all(s in t for s in sections); assert pages==17
(P/'citation-verification.json').write_text(json.dumps({'logs':logs,'hyperphysics_sections':sections,'nist_pdf_pages':pages,'passed':True},indent=2),encoding='utf-8')
