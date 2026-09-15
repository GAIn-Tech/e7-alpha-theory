"""Read-only replay of retained mathematical/source evidence; writes only verification.json.
Run using the installed Python with PyMuPDF. Solver subprocess uses existing Z3 venv.
"""
from pathlib import Path
import collections, hashlib, json, subprocess, sys
import fitz
ROOT=Path(__file__).resolve().parent
PY=ROOT.parent/'.venv/Scripts/python.exe'
LEAN=ROOT.parent/'lean-4.32.1-windows/bin/lean.exe'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
receipt=ROOT/'gate-receipt.json'
before=sha(receipt)
commands=[
    [str(PY),'-B',str(ROOT/'check_matching.py')],
    [str(PY),'-B',str(ROOT/'check_matching.py'),'--negative-controls'],
    [str(LEAN),str(ROOT/'Matching.lean')]]
results=[]
for cmd in commands:
    run=subprocess.run(cmd,capture_output=True,text=True,timeout=240)
    results.append({'command':cmd,'returncode':run.returncode,'stdout':run.stdout,'stderr':run.stderr})
    if run.returncode:raise RuntimeError(results[-1])
assert results[2]['stdout'].count('does not depend on any axioms')==2
assert 'sorry' not in (ROOT/'Matching.lean').read_text()
assert sha(receipt)==before
controls=json.loads(results[1]['stdout']);assert len(controls)==5 and all(controls.values())
# Independently verify exact retained primary PDFs/text/evidence, not child status booleans.
source=ROOT/'sources'
manifest=json.loads((source/'verification.json').read_text())
for entry in manifest['files']:
    p=source/entry['name']
    assert p.stat().st_size==entry['bytes'] and sha(p)==entry['sha256'],p
receipts=json.loads((source/'source-receipts.json').read_text())
for entry in receipts:
    for kind in ['pdf','text','reading_order']:
        p=Path(entry[kind+'_path'])
        assert p.parent==source and sha(p)==entry[kind+'_sha256'],p
quotes=json.loads((source/'quotation-evidence.json').read_text())
for q in quotes:
    with fitz.open(source/(q['arxiv_id']+'.pdf')) as doc:
        page=doc[q['pdf_page']-1]
        assert q['quote'] in page.get_text() or q['quote'] in page.get_text(sort=True),q['topic']
gate=json.loads(receipt.read_text())
counts=dict(collections.Counter(c['result'] for c in gate['checks']))
correction=json.loads((ROOT/'provenance-count-correction/correction.json').read_text())
assert correction['new_receipt_sha256']==before
output={'passed':True,'canonical_directory':str(ROOT),'commands':results,
        'receipt_sha256_before':before,'receipt_sha256_after':sha(receipt),
        'receipt_unchanged':True,'negative_controls':controls,
        'source_manifest_files_verified':len(manifest['files']),
        'primary_pdfs_verified':len(receipts),'exact_primary_quotations_verified':len(quotes),
        'solver_check_count':len(gate['checks']),'solver_status_counts':counts,
        'lean_axiom_free_declarations':2,'count_correction_provenance':correction,
        'verification_script_sha256':sha(Path(__file__)),
        'claim_boundary':gate['claim_boundary'],'hosted_ci':'not run'}
(ROOT/'verification.json').write_text(json.dumps(output,indent=2,sort_keys=True))
print(json.dumps({k:v for k,v in output.items() if k not in ['commands','count_correction_provenance']},indent=2))
