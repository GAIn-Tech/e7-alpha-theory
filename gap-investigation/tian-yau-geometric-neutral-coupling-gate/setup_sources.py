from pathlib import Path
import shutil, subprocess, sys
P=Path(__file__).resolve().parent
cache=Path('C:/Users/mikeb/AppData/Local/hermes/cache/web')
S=Path('C:/Users/mikeb/AppData/Local/hermes/skills/research/grounded-citations/scripts/sources.py')
(P/'sources').mkdir(exist_ok=True)
items=[('arxiv.org-bd056b4870.md','decoupling.md','https://arxiv.org/html/2409.04350v2','The decoupling of moduli about the standard embedding','However, in the case of the standard embedding, the extension map'),('arxiv.org-9956b811ae.md','yukawa.md','https://arxiv.org/html/2401.15078v2','Physical Yukawa Couplings in Heterotic String Compactifications','These are the unnormalized Yukawa couplings:'),('arxiv.org-4afd09f8bf.md','nonrenormalization.md','https://arxiv.org/pdf/hep-th/0510213','Nonrenormalization of Flux Superpotentials in String Theory','We conclude from this that the PQ symmetry precludes W from developing a dependence on S')]
for idx,(src,dest,url,title,needle) in enumerate(items,1):
 f=P/'sources'/dest
 if not f.exists(): shutil.copyfile(cache/src,f)
 cmd=[sys.executable,str(S),'--ledger',str(P/'sources/ledger.json')]
 subprocess.run(cmd+['add',url,'--title',title],check=True)
 text=f.read_text(encoding='utf-8'); start=text.index(needle); quote=text[start:text.index('\n',start)]
 subprocess.run(cmd+['quote',str(idx),'--text',quote,'--from',str(f)],check=True)
