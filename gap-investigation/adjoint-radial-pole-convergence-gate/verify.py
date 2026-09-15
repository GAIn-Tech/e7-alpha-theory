"""Additive numerical convergence audit. Run with -B; --create once, then replay."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,hashlib,subprocess,importlib.util
from pathlib import Path
P=Path(__file__).resolve().parent; ROOT=P.parent
sys.path.insert(0,str(P/'vendor'))
import mpmath as mp
import numpy as np

def load(p,n):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pack(z):return {'real':float(mp.re(z)),'imag':float(mp.im(z))}
def integral(a,b,s=4320,adaptive=False):
 a,b,s=map(mp.mpf,(a,b,s)); disc=(a-b-s)**2-4*s*b
 r1=(s+b-a-mp.sqrt(mp.mpc(disc)))/(2*s);r2=(s+b-a+mp.sqrt(mp.mpc(disc)))/(2*s)
 cuts=sorted(set([mp.mpf(0),mp.mpf(1)]+[r.real for r in (r1,r2) if abs(r.imag)==0 and 0<r.real<1]))
 neg=sum(hi-lo for lo,hi in zip(cuts,cuts[1:]) if ((lo+hi)/2*a+(1-(lo+hi)/2)*b-s*(lo+hi)/2*(1-(lo+hi)/2))<0)
 if adaptive:
  # Factored polynomial prevents catastrophic endpoint subtraction. Exact endpoints
  # have measure zero; tanh-sinh normally avoids them, but rounding can hit them.
  def f(t):
   d=s*(t-r1)*(t-r2)
   return mp.log(abs(d)) if d else mp.mpf(0)
  re=mp.quad(f,cuts,method='tanh-sinh')
 else:
  def F(r):
   if r.imag==0:
    def xlog(x):return x*mp.log(abs(x)) if x else mp.mpf(0)
    return xlog(1-r.real)+xlog(r.real)-1
   return mp.re((1-r)*mp.log(1-r)+r*mp.log(-r)-1)
  re=mp.log(s)+F(r1)+F(r2)
 return mp.mpc(re,-mp.pi*neg)

def replay():
 paths=['adjoint-radial-pole-gate/calculation.py','adjoint-radial-gauge-pole-gate/calculation.py','adjoint-radial-vector-bubble-gate/calculation.py','adjoint-radial-mixed-pole-gate/run_checks.py']
 out=[]
 for rel in paths:
  q=ROOT/rel;r=subprocess.run([sys.executable,'-B',str(q)],capture_output=True,text=True)
  assert r.returncode==0,(rel,r.stderr)
  out.append({'entry':rel,'exit':r.returncode,'stdout_sha256':hashlib.sha256(r.stdout.encode()).hexdigest()})
 return out

def compute():
 inputs=[]
 for name in ['adjoint-radial-pole-gate','adjoint-radial-gauge-pole-gate','adjoint-radial-vector-bubble-gate','adjoint-radial-mixed-pole-gate']:
  inputs += [p for p in (ROOT/name).iterdir() if p.suffix in ('.py','.json','.md','.npz')]
 inputs += [ROOT/'shifted-vacuum-gate/calculation.py',ROOT/'ir-resummed-vacuum-gate/calculation.py']
 hashes={str(p):sha(p) for p in inputs}
 replays=replay()
 S=load(ROOT/'adjoint-radial-pole-gate/calculation.py','scalar_audit')
 D=np.load(ROOT/'adjoint-radial-mixed-pole-gate/recovery-tensors.npz');x,B,H,h=D['x'],D['B'],D['H'],D['h']
 m,E=np.linalg.eigh(H);T,U=S.tree_tensors(None,x,B,None,h);t=E.T@T@E;q=np.diag(E.T@U@E)
 keys=np.where(m<1e-8,-1.,np.round(m,8));vals=np.unique(keys);masses={k:(0. if k==-1 else float(np.mean(m[keys==k]))) for k in vals}
 pairs=[]
 for i,a in enumerate(vals):
  for b in vals[i:]:
   mask=np.ix_(keys==a,keys==b);w=float(np.sum(t[mask]**2))*(1 if a==b else 2)
   pairs.append((a,b,w))
 assert abs(sum(w for a,b,w in pairs)-np.sum(t*t))<1e-7
 old={n:S.log_integral_matrix(np.where(m>1e-8,m,1e-60),4320,n) for n in (128,256,512,1024)}
 rows=[];hp={};quaderr={};totals={};precision=[]
 for dps in (40,70):
  mp.mp.dps=dps;fac=32*mp.pi**2;analytic=mp.mpc(0);adaptive=mp.mpc(0);err=mp.mpf(0)
  for a,b,w in pairs:
   z=integral(masses[a],masses[b]);zz=integral(masses[a],masses[b],adaptive=True)
   analytic+=mp.mpf(w)*z/fac;adaptive+=mp.mpf(w)*zz/fac;err+=mp.mpf(w)*abs(z-zz)/fac
   if dps==70:
    hp[a,b]=z;quaderr[a,b]=float(abs(z-zz));
  precision.append({'dps':dps,'bubble_analytic':pack(analytic),'bubble_adaptive':pack(adaptive),'weighted_absolute_integration_disagreement':float(err),'analytic_full_digits':str(analytic)})
 assert max(z['weighted_absolute_integration_disagreement'] for z in precision)<1e-20
 for a,b,w in pairs:
  ii=np.where(keys==a)[0][0];jj=np.where(keys==b)[0][0]
  gl={str(n):float(w*(old[n][ii,jj].real-float(hp[a,b].real))/(32*np.pi**2)) for n in old}
  rows.append({'m2_a':masses[a],'m2_b':masses[b],'ordered_weight':w,'I':pack(hp[a,b]),'adaptive_abs_error':quaderr[a,b],'weighted_GL_real_error':gl,'GL256_minus_GL512':gl['256']-gl['512']})
 rows.sort(key=lambda r:abs(r['GL256_minus_GL512']),reverse=True)
 sf=json.loads((ROOT/'adjoint-radial-pole-gate/receipt.json').read_text());vf=json.loads((ROOT/'adjoint-radial-vector-bubble-gate/receipt.json').read_text());sv=json.loads((ROOT/'adjoint-radial-mixed-pole-gate/finite-momentum-receipt.json').read_text())
 tad=mp.fsum(mp.mpf(float(qi))*mp.mpf(float(mi))*(mp.log(float(mi))-1)/(32*mp.pi**2) for qi,mi in zip(q,m) if mi>1e-8)
 scalar=analytic+tad+mp.mpf(sf['tadpole_scheme']['scalar_induced_tree_shift'])+mp.mpf(sf['tadpole_scheme']['fermion_total_including_shift'])
 # Vector cancellation audit: same action weights, arbitrary precision masters.
 R=D['R'];rx=R@x;rh=R@h;mv,ev=np.linalg.eigh(rx@rx.T);dd=ev.T@(rh@rx.T+rx@rh.T)@ev
 def A(a):return a*(mp.log(a)-1) if a else mp.mpf(0)
 def K(a,b,ad):
  a,b=mp.mpf(float(a)),mp.mpf(float(b));s=mp.mpf(4320)
  ab,a0,zb,zz=[integral(u,v,adaptive=ad) for u,v in [(a,b),(a,0),(0,b),(0,0)]]
  xx=(A(b)+a*ab-a*a0)/b;yy=(A(a)+b*ab-b*zb)/a
  return 2*ab+(xx+yy+2*ab-2*s*((ab-zb)/a+(ab-a0)/b)+s*s*(ab-zb-a0+zz)/(a*b))/4+2
 vv=[]
 for ad in (False,True):
  cache={};z=mp.mpc(0)
  for i,a in enumerate(mv):
   for j,b in enumerate(mv):
    if a>1e-8 and b>1e-8 and abs(dd[i,j])>1e-12:
     key=(float(a),float(b));
     if key not in cache:cache[key]=K(a,b,ad)
     z+=mp.mpf(float(dd[i,j]**2))*cache[key]/(32*mp.pi**2)
  vv.append(z)
 assert abs(vv[0]-vv[1])<mp.mpf('1e-20')
 # Use freshly replayed compatible sectors; vector HP replaces cancellation-limited double master.
 vector=vv[0]+mp.mpf(vf['result']['vector_seagull_momentum_independent'])
 mixed=mp.mpc(sv['result']['SV_real'],sv['result']['SV_imag']);shift=mp.mpf(sv['tadpole_consistency']['recomputed_vector_stationary_shift'])
 assert abs(shift-mp.mpf('-45.10700126487947'))<mp.mpf('1e-12')
 combined=scalar+vector+mixed+shift
 for n,mat in old.items():totals[str(n)]=pack(np.sum(t*t*mat)/(32*np.pi**2))
 # Analytic regulator approach, avoiding impossible double-precision eta endpoint resolution.
 regs=[]
 for eta in ('1e-4','1e-8','1e-16','1e-32','0'):
  bsum=mp.fsum(mp.mpf(w)*integral(mp.mpf(eta) if a==-1 else masses[a],mp.mpf(eta) if b==-1 else masses[b])/(32*mp.pi**2) for a,b,w in pairs)
  regs.append({'eta':eta,'bubble':pack(bsum),'difference_from_zero_abs':float(abs(bsum-analytic))})
 # Master negative controls exercise below-threshold complex roots and the cut sign.
 assert abs(integral(0,0)-(mp.log(4320)-2-mp.j*mp.pi))<mp.mpf('1e-60')
 assert abs(integral(4320,4320)-integral(4320,4320,adaptive=True))<mp.mpf('1e-60')
 assert integral(4320,4320).imag==0
 assert all(sha(Path(p))==v for p,v in hashes.items()),'predecessor changed'
 discrepancy=sum(r['GL256_minus_GL512'] for r in rows)
 assert abs(abs(discrepancy)-sf['checks']['quadrature_256_vs_512_last_total_abs'])<1e-8
 return {'passed':True,'claim_boundary':'Numerical convergence audit and compatible strict-Landau sector bookkeeping only; not a full pole, gauge independence, or width. Floating action input; no interval proof.','source_hashes':hashes,'verifier_sha256':sha(Path(__file__)),'versions':{'numpy':np.__version__,'mpmath':mp.__version__},'replays':replays,'scalar_channels':rows,'gauss_bubble_totals':totals,'precision_comparison':precision,'analytic_regulator_scan':regs,'scalar_quartic':float(tad),'scalar_fermion_corrected':pack(scalar),'scalar_correction_to_512':float(scalar.real-sf['regulator_scan'][-1]['scalar_total_real']),'reproduced_signed_256_minus_512':discrepancy,'vector_high_precision_bubble':pack(vv[0]),'vector_adaptive_error':float(abs(vv[0]-vv[1])),'vector_double_receipt_abs_error':float(abs(vv[0]-complex(vf['result']['transverse_VV_bubble_real'],vf['result']['transverse_VV_bubble_imag']))),'vector_stationary_shift':float(shift),'mixed_replayed':pack(mixed),'mixed_independent_512_error':sv['checks']['independent_512_error'],'compatible_sector_sum_NOT_a_pole':pack(combined),'reporting_policy':'Report scalar and combined to 0.001 coefficient units; integration evidence is not an interval enclosure or physical error. Mixed independent check remains about 2.3e-6, action tensors are double precision.'}

if __name__=='__main__':
 out=compute();p=P/'receipt.json'
 if '--create' in sys.argv:
  with p.open('x') as f:json.dump(out,f,indent=2)
 else:
  saved=json.loads(p.read_text());assert saved==out,'receipt mismatch: do not regenerate'
 print(json.dumps({k:v for k,v in out.items() if k not in ('source_hashes','scalar_channels')},indent=2))

