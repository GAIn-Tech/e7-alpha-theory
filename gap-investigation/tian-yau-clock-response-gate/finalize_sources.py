from pathlib import Path
import subprocess,json,hashlib,shutil
P=Path(__file__).resolve().parent
S=Path('C:/Users/mikeb/AppData/Local/hermes/skills/research/grounded-citations/scripts/sources.py')
PY='C:/Python313/python.exe'
def cmd(*a):
 r=subprocess.run([PY,str(S),'--ledger',str(P/'sources/ledger.json'),*a],capture_output=True,text=True,encoding='utf8'); assert r.returncode==0,r.stdout+r.stderr; return r.stdout
for e in json.loads((P/'sources/equation-evidence.json').read_text(encoding='utf8')):
 idx='2' if 'dilaton' in e['file'] else '3' if 'walls' in e['file'] else '5'
 cmd('quote',idx,'--text',e['text'],'--from',str(P/e['file']))
cmd('render','--replace-in',str(P/'REPORT.md'))
print(cmd('verify',str(P/'REPORT.md'),'--evidence'))
files={str(x.relative_to(P)):hashlib.sha256(x.read_bytes()).hexdigest() for x in (P/'sources').iterdir() if x.is_file() and x.name!='manifest.json'}
(P/'sources/manifest.json').write_text(json.dumps({'hashes':files,'retrieval_note':'HTTP HyperPhysics freshly fetched; HTTPS web extraction failed. PDFs retained exactly; Kim returned v4. Predecessor Yukawa/NIST files copied byte-for-byte. No substitutes for failed HTML.'},indent=2))
