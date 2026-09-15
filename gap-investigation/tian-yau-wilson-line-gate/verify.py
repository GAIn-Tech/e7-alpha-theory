"""Saved-evidence replay. --create exclusively writes a new verification receipt."""
from pathlib import Path
import sys, subprocess, json, hashlib, re, os
P=Path(__file__).resolve().parent
LEAN=P.parent/'lean-4.32.1-windows/bin/lean.exe'
def run(argv,cwd=P):
    r=subprocess.run([str(x) for x in argv],cwd=cwd,capture_output=True,text=True)
    return r.returncode,r.stdout+r.stderr

def calculate():
    for name in ['Formalization.lean','Challenge.lean']:
        text=(P/name).read_text(encoding='utf-8')
        # No proof escape keywords in source, comments included.
        assert not re.search(r'\b(sorry|admit|unsafe|axiom)\b',text)
    code,out=run([LEAN,'-o','Formalization.olean','Formalization.lean']);assert code==0,out
    theorem_names=['add_succ_left','right_swap','right_cancel','paired_mass_preserves_net','four_pairs_witness']
    expected=[f"'WilsonMass.{n}' does not depend on any axioms" for n in theorem_names]
    actual=[s for s in out.splitlines() if 'does not depend on any axioms' in s or 'depends on axioms' in s]
    assert actual==expected,(actual,expected)
    env=dict(os.environ);env['LEAN_PATH']=str(P)
    challenge=subprocess.run([str(LEAN),'Challenge.lean'],cwd=P,capture_output=True,text=True,env=env)
    assert challenge.returncode==0,challenge.stdout+challenge.stderr
    pre=P.parent/'heterotic-e6-three-family-gate'
    pc,po=run([sys.executable,'-B',pre/'exact_certificate.py','--verify'],cwd=pre);assert pc==0,po
    good,go=run([sys.executable,'-B','exact_certificate.py','--verify']);assert good==0,go
    target=P/'certificate.json';saved=target.read_bytes()
    # Test the real CLI's missing and tampered receipt paths, always restore.
    try:
        target.unlink()
        missing,mo=run([sys.executable,'-B','exact_certificate.py','--verify'])
        assert missing!=0 and 'Missing certificate' in mo,mo
        target.write_bytes(saved+b' ')
        tampered,to=run([sys.executable,'-B','exact_certificate.py','--verify'])
        assert tampered!=0 and 'Stale/tampered certificate' in to,to
    finally:target.write_bytes(saved)
    # Test exclusive creation without rewriting the good saved certificate.
    exclusive,eo=run([sys.executable,'-B','exact_certificate.py','--create'])
    assert exclusive!=0 and 'FileExistsError' in eo,eo
    assert target.read_bytes()==saved
    data=json.loads(saved)
    assert data['torus_points']==729 and data['Weyl_classes']==8
    tri=next(e for e in data['classes'] if e['surviving_root_count']==18)
    assert sorted((r['phase'],r['multiplicity'],r['conjugate_multiplicity']) for r in tri['representations_27'])==[(0,9,6),(1,7,4),(2,7,4)]
    assert data['interactions']['two_L_plus_conjugate_pairs']['including_color_dimension']==12
    files=['exact_certificate.py','interactions.py','certificate.json','Formalization.lean','Challenge.lean','formalization.yaml','RELEASE_DISCLOSURE.md','REPORT.md','verify.py']
    return {'passed':True,'python_executable':sys.executable,'lean_exit_code':code,'challenge_exit_code':challenge.returncode,'axiom_reports':actual,'predecessor_exact_replay_exit':pc,'certificate_replay_exit':good,'negative_controls':{'missing_receipt_rejected':missing!=0,'tampered_receipt_rejected':tampered!=0,'exclusive_creation_rejected_existing':exclusive!=0,'saved_receipt_restored':target.read_bytes()==saved},'physical_checks':{'toral_points':729,'Weyl_classes':8,'trinification_spectrum':data['interactions']['multiplicities'],'full_Higgs_stabilizer_dimension':12,'achieved_mass_ranks':None},'hashes':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in files},'scope':'Local exact and kernel checks; no compactification superpotential solution or hosted CI.'}

def main():
    d=calculate();s=json.dumps(d,sort_keys=True,indent=2)+'\n';p=P/'verification.json'
    if '--create' in sys.argv:
        with p.open('x',encoding='utf-8') as f:f.write(s)
    else:
        assert p.exists(),'Missing verification receipt';assert p.read_text(encoding='utf-8')==s,'Stale verification receipt'
    print(json.dumps({'passed':True,'physical_checks':d['physical_checks'],'axiom_reports':d['axiom_reports'],'negative_controls':d['negative_controls']},indent=2))
if __name__=='__main__':main()
