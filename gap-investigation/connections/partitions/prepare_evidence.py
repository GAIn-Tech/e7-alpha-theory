from pathlib import Path
import subprocess,sys,shutil,json,re,hashlib
R=Path('C:/Users/mikeb/e7-alpha-theory/gap-investigation/connections/partitions')
S='C:/Users/mikeb/AppData/Local/hermes/skills/research/grounded-citations/scripts/sources.py'
def cli(*args):
 p=subprocess.run([sys.executable,S,'--ledger',str(R/'ledger.json'),*args],capture_output=True,text=True,encoding='utf-8'); print(p.stdout.strip()); assert p.returncode==0,p.stderr
shutil.copyfile('C:/Users/mikeb/AppData/Local/hermes/cache/web/projecteuclid.org-f2c3c30332.md',R/'witten.txt')
cli('add','https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-109/issue-4/Elliptic-genera-and-quantum-field-theory/cmp/1104117076.pdf','--title','Witten: Elliptic Genera and Quantum Field Theory')
items=[
(1,'dedekind','We study some divisibility properties of Dedekind numbers.',200),
(2,'narain','This is the situation that gets generalized',900),
(3,'k3','The standard embedding breaks one',420),
(4,'selfconjugate','A partition of',420),
(5,'rademacher','Dedekind sums',250),
(6,'mocknotes','holomorphic parts',400),
(7,'chiral','We call',600),
(8,'ramanujan','We have shown',450),
(9,'blackholes','We show that the meromorphic Jacobi form',1300),
(10,'nimbers','Conway’s kind of multiplication',650),
(11,'witten','Subsequent work',650)]
receipts=[]
for idx,name,phrase,length in items:
 text=(R/(name+'.txt')).read_text(encoding='utf-8'); start=text.find(phrase)
 if start<0:
  # Explicitly expose alternatives rather than invent quote.
  print('MISSING',name,phrase); continue
 quote=text[max(0,start-40):start+length]
 cli('quote',str(idx),'--text',quote,'--from',str(R/(name+'.txt')))
 receipts.append({'id':idx,'file':name+'.txt','quote':quote,'url_in_ledger':True,'sha256':hashlib.sha256((R/(name+'.txt')).read_bytes()).hexdigest()})
(R/'source_evidence.json').write_text(json.dumps(receipts,indent=2,ensure_ascii=False),encoding='utf-8')
print('evidence entries',len(receipts))
