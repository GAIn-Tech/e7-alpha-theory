import contextlib, hashlib, io, json, shutil, subprocess, sys, tempfile
from pathlib import Path
import checks
ROOT=Path(__file__).resolve().parent

def run():
    # Replay existing evidence first. Never regenerate in this verification runner.
    p=subprocess.run([sys.executable,'-B',str(ROOT/'checks.py')],capture_output=True,text=True)
    result={'replay':{'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr},'controls':{}}
    if p.returncode:
        print(p.stdout,p.stderr);raise SystemExit(p.returncode)
    for mode in ('missing','tampered'):
        with tempfile.TemporaryDirectory(prefix='receipt-control-',dir=ROOT) as d:
            d=Path(d)
            if mode=='tampered':
                payload=json.loads((ROOT/'receipt.json').read_text());payload['candidate']['light_net_27']=0
                (d/'receipt.json').write_text(json.dumps(payload))
                for f in ROOT.glob('search-n*.smt2'):shutil.copy2(f,d/f.name)
            oldroot=checks.ROOT;oldargs=sys.argv
            checks.ROOT=d;sys.argv=['checks.py'];rejected=False
            try:
                with contextlib.redirect_stdout(io.StringIO()):checks.main()
            except (SystemExit,AssertionError) as e:rejected=True;detail=str(e)
            finally:checks.ROOT=oldroot;sys.argv=oldargs
            assert rejected
            result['controls'][mode]={'rejected':True,'detail':detail}
    result['hashes']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in ROOT.iterdir() if p.is_file() and p.name!='verification.json'}
    result['passed']=True
    (ROOT/'verification.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({'passed':True,'replay_exit':p.returncode if hasattr(p,'returncode') else result['replay']['exit'],'controls':result['controls']},indent=2))
if __name__=='__main__':run()
