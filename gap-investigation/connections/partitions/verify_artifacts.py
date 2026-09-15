"""Read back exact targets; do not regenerate the certificate before checking it."""
from pathlib import Path
import hashlib,json,subprocess,sys
R=Path(__file__).resolve().parent
subprocess.run([sys.executable,str(R/'exact_certificate.py'),'--verify'],check=True)
evidence=json.loads((R/'source_evidence.json').read_text(encoding='utf-8'))
for row in evidence:
 raw=(R/row['file']).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==row['sha256'],row['file']
 assert row['quote'] in (R/row['file']).read_text(encoding='utf-8'),row['file']
edges=json.loads((R/'edge_ledger.json').read_text(encoding='utf-8'))['edges']
assert len({r['id'] for r in evidence})==11
assert 'projected_norms' in (R/'exact_certificate.py').read_text()
assert (R/'REPORT.md').read_text(encoding='utf-8').count('## Sources')==1
S='C:/Users/mikeb/AppData/Local/hermes/skills/research/grounded-citations/scripts/sources.py'
subprocess.run([sys.executable,S,'--ledger',str(R/'ledger.json'),'verify',str(R/'REPORT.md'),'--evidence'],check=True)
manifest={p.name:{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in R.iterdir() if p.is_file() and p.name not in ('verification.json',)}
result={'passed':True,'native_directory':str(R),'sources_with_exact_quotes':len(evidence),'typed_edges':len(edges),'certificate_replayed_without_regeneration':True,'source_hashes_and_quote_substrings_verified':True,'formal_kernel_proof':False,'files':manifest}
(R/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='files'},indent=2))
