"""Conditional radial perturbativity, real i0 boundary. Native -B execution only.
--create exclusively creates receipt; ordinary execution compares saved payload.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import sys,json,hashlib,importlib.util
from pathlib import Path
from functools import lru_cache
import numpy as np
P=Path(__file__).resolve().parent;ROOT=P.parent
sys.path.insert(0,str(ROOT/'adjoint-radial-pole-convergence-gate/vendor'))
import mpmath as mp
mp.mp.dps=45
rho=mp.mpf(4320)
def load(p,n):
 spec=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def pack(z):return {'real':float(mp.re(z)),'imag':float(mp.im(z))}
conv=load(ROOT/'adjoint-radial-pole-convergence-gate/verify.py','conv_window')
S=load(ROOT/'adjoint-radial-pole-gate/calculation.py','scalar_window')
M=load(ROOT/'shifted-vacuum-gate/calculation.py','action_window')
D=np.load(ROOT/'adjoint-radial-mixed-pole-gate/recovery-tensors.npz')
@lru_cache(None)
def I(a,b,s,adaptive=False):return conv.integral(a,b,s,adaptive)

def Ip(a,b,s=rho):
 """Analytic rational PV plus delta-function cut; no regulator or root clipping."""
 a,b,s=map(mp.mpf,(a,b,s));disc=(a-b-s)**2-4*s*b
 if disc==0:raise ValueError('threshold derivative singular: no isolated analytic expansion')
 rt=mp.sqrt(mp.mpc(disc));roots=((s+b-a-rt)/(2*s),(s+b-a+rt)/(2*s))
 ans=mp.mpc(1/s);cut=mp.mpf(0)
 for r in roots:
  residue=r*(r-1)/(2*s*r+a-b-s)
  if abs(r.imag)==0:
   r=r.real
   if r in (0,1):
    assert abs(residue)==0
    continue
   ans+=residue*mp.log(abs((1-r)/r))
   if 0<r<1:cut+=r*(r-1)/abs(2*s*r+a-b-s)
  else:ans+=residue*(mp.log(1-r)-mp.log(-r))
 return mp.mpc(ans.real,mp.pi*cut)
def A(a):
 a=mp.mpf(a);return a*(mp.log(a)-1) if a else mp.mpf(0)
def vk(a,b,s,derivative=False,adaptive=False):
 a,b,s=map(mp.mpf,(a,b,s));ab=I(a,b,s,adaptive);a0=I(a,0,s,adaptive);zb=I(0,b,s,adaptive);zz=I(0,0,s,adaptive)
 L=(ab-zb)/a+(ab-a0)/b;d=ab-zb-a0+zz
 if not derivative:
  xx=(A(b)+a*ab-a*a0)/b;yy=(A(a)+b*ab-b*zb)/a
  return 2*ab+(xx+yy+2*ab-2*s*L+s*s*d/(a*b))/4+2
 p,pa,pb,pz=Ip(a,b,s),Ip(a,0,s),Ip(0,b,s),Ip(0,0,s)
 lp=(p-pb)/a+(p-pa)/b;dp=p-pb-pa+pz
 return 2*p+(a*(p-pa)/b+b*(p-pb)/a+2*p-2*L-2*s*lp+2*s*d/(a*b)+s*s*dp/(a*b))/4

def sk(x,v,s,derivative=False,adaptive=False):
 x,v,s=map(mp.mpf,(x,v,s));i=I(x,v,s,adaptive);j=I(x,0,s,adaptive)
 if not derivative:return -(2*x-v+2*s)*i+A(x)-A(v)+((x-s)*A(v)+(x-s)**2*(i-j))/v
 ip,jp=Ip(x,v,s),Ip(x,0,s)
 return -2*i-(2*x-v+2*s)*ip+(-A(v)-2*(x-s)*(i-j)+(x-s)**2*(ip-jp))/v

def tensor_sv(x,v,s):
 """Independent adaptive tensor-first representation, including evanescent -2s."""
 x,v,s=map(mp.mpf,(x,v,s));cuts={mp.mpf(0),mp.mpf(1)};rr={}
 for m in (mp.mpf(0),v):
  root=mp.sqrt(mp.mpc((x-m-s)**2-4*s*m));r=((s+m-x-root)/(2*s),(s+m-x+root)/(2*s));rr[m]=r
  cuts.update(z.real for z in r if z.imag==0 and 0<z.real<1)
 def af(t,m):
  z=mp.re(s*(t-rr[m][0])*(t-rr[m][1]))
  return z*(mp.log(abs(z))-1-mp.j*mp.pi*(z<0)) if z else mp.mpc(0)
 return 6*s/v*mp.quad(lambda t:af(t,0)-af(t,v),sorted(cuts))-2*s

def shells(m,U):
 keys=np.where(abs(m)<1e-8,0.,np.round(m,7));return [(float(np.mean(m[keys==k])) if k else 0.,U[:,keys==k]) for k in np.unique(keys)]
def threshold(a,b):return float((mp.sqrt(a)+mp.sqrt(b))**2)

def compute():
 source_paths=[]
 for lane in ('adjoint-radial-pole-convergence-gate','adjoint-radial-mixed-pole-gate','adjoint-radial-rxi-identity-gate','shifted-vacuum-gate'):
  source_paths.extend(q for q in (ROOT/lane).iterdir() if q.suffix in ('.py','.json','.md','.npz'))
 source_paths.append(ROOT/'adjoint-radial-pole-gate/calculation.py')
 hashes={str(q):sha(q) for q in source_paths}
 # Validate predecessor saved evidence before computing, without executing writers.
 for lane,file in [('adjoint-radial-pole-convergence-gate','receipt.json'),('adjoint-radial-mixed-pole-gate','finite-momentum-receipt.json'),('shifted-vacuum-gate','receipt.json')]:
  r=json.loads((ROOT/lane/file).read_text())
  assert r['passed']
  for p,h in r['source_hashes'].items():assert sha(Path(p))==h,p
 x,B,H,h,R=D['x'],D['B'],D['H'],D['h'],D['R']
 ms,Us=np.linalg.eigh(H);mv,Uv=np.linalg.eigh((R@x)@(R@x).T)
 T,U=S.tree_tensors(None,x,B,None,h);ss=shells(ms,Us);vs=shells(mv,Uv)
 G=D['G'];F=M.null(np.concatenate((H,R@x),axis=0));PE=D['E']
 assert F.shape[1]==11 and G.shape[1]==67
 categories=[('physical_flat',0.,F),('Goldstone',0.,G)]+[('physical_massive',a,E) for a,E in ss if a>0]
 scalar=[];inactive=[]
 for i,(na,a,E) in enumerate(categories):
  for nb,b,W in categories[i:]:
   weight=float(np.sum((E.T@T@W)**2))*(1 if E is W else 2)
   row={'a':a,'b':b,'weight':weight,'types':[na,nb],'threshold':threshold(a,b),'distance':abs(4320-threshold(a,b))}
   (scalar if weight>1e-14 else inactive).append(row)
 assert abs(sum(r['weight'] for r in scalar)-np.sum(T*T))/np.sum(T*T)<1e-11
 # The potentially coincident scalar channel is structurally zero: T h parallel h.
 th_res=float(np.linalg.norm(T@h-h*(h@T@h)))
 assert th_res<1e-8
 vec=[];mix=[];unphysical=[]
 vvertex=(R@h)@(R@x).T+(R@x)@(R@h).T
 for a,E in vs:
  for b,W in vs:
   w=float(np.sum((E.T@vvertex@W)**2))
   if w>1e-16:
    assert a>0 and b>0
    vec.append({'a':a,'b':b,'weight':w,'threshold':threshold(a,b),'distance':abs(4320-threshold(a,b))})
    for aa,bb in ((a,0.),(0.,b),(0.,0.)):
     unphysical.append({'sector':'VV_projector','a':aa,'b':bb,'threshold':threshold(aa,bb),'distance':abs(4320-threshold(aa,bb))})
  for name,b,W in categories:
   w=float(np.sum((E.T@(R@h)@W)**2))
   if w>1e-16:
    assert a>0
    mix.append({'a':b,'b':a,'weight':w,'scalar_type':name,'threshold':threshold(b,a),'distance':abs(4320-threshold(b,a))})
    unphysical.append({'sector':'SV_projector','a':b,'b':0.,'threshold':b,'distance':abs(4320-b)})
 fac=32*mp.pi**2
 # Group masters at actual shell means; structural zero channels are not evaluated.
 scalar_der=mp.fsum(mp.mpf(r['weight'])*Ip(r['a'],r['b'])/fac for r in scalar)
 vector_der=mp.fsum(mp.mpf(r['weight'])*vk(r['a'],r['b'],rho,True)/fac for r in vec)
 mixed_der=mp.fsum(mp.mpf(r['weight'])*sk(r['a'],r['b'],rho,True)/(fac/2) for r in mix)
 analytic=scalar_der+vector_der+mixed_der
 def adaptive(s):
  ss=mp.fsum(mp.mpf(r['weight'])*I(r['a'],r['b'],s,True)/fac for r in scalar)
  vv=mp.fsum(mp.mpf(r['weight'])*vk(r['a'],r['b'],s,adaptive=True)/fac for r in vec)
  # cache physical and Goldstone equal masses without merging their interpretation
  mm={}
  for r in mix:
   key=(r['a'],r['b']);mm[key]=mm.get(key,0)+r['weight']
  sv=mp.fsum(mp.mpf(w)*tensor_sv(a,b,s)/(fac/2) for (a,b),w in mm.items())
  return ss+vv+sv
 derivatives=[]
 for step in ('0.01','0.005'):
  d=mp.mpf(step);v=(-adaptive(rho+2*d)+8*adaptive(rho+d)-8*adaptive(rho-d)+adaptive(rho-2*d))/(12*d)
  derivatives.append({'step':step,'value':pack(v),'abs_error':float(abs(v-analytic))})
 assert max(r['abs_error'] for r in derivatives)<1e-10,derivatives
 # Independent elementary masters below threshold and cut slope above threshold.
 controls={}
 assert abs(Ip(0,0)-1/rho)<mp.mpf('1e-40')
 below=mp.quad(lambda t:-t*(1-t)/(4320-rho*t*(1-t)),[0,1])
 controls['below_threshold_direct_rational_error']=float(abs(Ip(4320,4320)-below))
 assert controls['below_threshold_direct_rational_error']<1e-35
 expected_cut=-2*mp.pi/(rho**2*mp.sqrt(1-4/rho))
 controls['equal_mass_cut_slope_error']=float(abs(Ip(1,1).imag-expected_cut))
 assert controls['equal_mass_cut_slope_error']<1e-35
 try:Ip(1080,1080)
 except ValueError:controls['threshold_collision_rejected']=True
 else:raise AssertionError('singular threshold accepted')
 controls['drop_imaginary_derivative_change']=float(abs(analytic.imag))
 controls['reverse_cut_sign_derivative_change']=float(2*abs(analytic.imag))
 controls['omit_mixed_derivative_change']=float(abs(mixed_der))
 controls['wrong_epsilon_order_at_1e_minus_7_ratio']=1e7
 cr=json.loads((ROOT/'adjoint-radial-pole-convergence-gate/receipt.json').read_text())
 C=mp.mpc(cr['compatible_sector_sum_NOT_a_pole']['real'],cr['compatible_sector_sum_NOT_a_pole']['imag'])
 sr=json.loads((ROOT/'shifted-vacuum-gate/receipt.json').read_text());delta=np.array(sr['leading_delta_canonical'])
 # Recompute canonical leading shift with all determinants instead of trusting its norm.
 tad=M.loop(x,B,D['c'],R)[1];pos=ms>1e-8;dd=-Us[:,pos]@((Us[:,pos].T@tad)/ms[pos])
 assert np.linalg.norm(dd-delta)<1e-7
 displacement={'norm':float(np.linalg.norm(dd)),'x_norm':float(np.linalg.norm(x)),'relative_norm_coefficient':float(np.linalg.norm(dd)/np.linalg.norm(x)),'radial_projection_coefficient':float(h@dd/np.linalg.norm(x[108:186])),'block_relative_coefficients':{name:float(np.linalg.norm(dd[lo:hi])/np.linalg.norm(x[lo:hi])) for name,lo,hi in [('h1',0,54),('h2',54,108),('A',108,186),('Phi',186,188)]},'stationarity_residual':float(np.linalg.norm(H@dd+tad)),'receipt_displacement_error':float(np.linalg.norm(dd-delta))}
 gap=float(min(abs(a-4320) for a,E in ss if abs(a-4320)>1e-7))
 active_threshold_gap=min(r['distance'] for r in scalar+vec+mix+unphysical)
 physical_threshold_gap=min(r['distance'] for r in scalar if 'Goldstone' not in r['types'])
 physical_threshold_gap=min(physical_threshold_gap,min(r['distance'] for r in vec),min(r['distance'] for r in mix if r['scalar_type']!='Goldstone'))
 coeff={'relative_complex_shift':float(abs(C)/rho),'relative_real_shift':float(abs(C.real)/rho),'relative_imaginary_shift':float(abs(C.imag)/rho),'displacement_total':displacement['relative_norm_coefficient'],'displacement_worst_block':max(displacement['block_relative_coefficients'].values()),'wavefunction_Landau':float(abs(analytic)),'scalar_pole_isolation':float(abs(C)/gap),'active_threshold_isolation':float(abs(C)/active_threshold_gap)}
 bounds=[]
 for tol in (.1,.01,.001):
  upper={k:tol/v for k,v in coeff.items()}
  bounds.append({'analysis_tolerance':tol,'epsilon_upper_bounds':upper,'necessary_joint_upper':min(upper.values())})
 scans=[{'epsilon':e,'diagnostics':{k:e*v for k,v in coeff.items()}} for e in (1.,.01,.001,.0001,1e-7)]
 # Rxi collision locations: unphysical masses xi*a, physical-G thresholds, GG thresholds.
 xi_poles=[{'a':a,'multiplicity':E.shape[1],'xi_pole_collision':4320/a,'xi_equal_GG_threshold_collision':1080/a} for a,E in vs if a>0]
 xi_pg=[]
 for r in mix:
  if r['scalar_type']=='Goldstone':continue
  if r['a']<4320:xi_pg.append({'t':r['a'],'a':r['b'],'xi_collision':float((mp.sqrt(rho)-mp.sqrt(r['a']))**2/r['b'])})
 xi_gg=[{'a':r['a'],'b':r['b'],'xi_collision':4320/r['threshold']} for r in vec]
 # EFT examples are conditional inequalities, not chosen values of the action.
 eft=[{'Lambda_over_M':ratio,'epsilon_upper_for_p2_over_Lambda2_lt_0p1':.1*ratio**2/4320,'A_norm_squared_over_Lambda_squared':float(np.sum(x[108:186]**2))/ratio**2,'total_background_norm_squared_over_Lambda_squared':float(x@x)/ratio**2} for ratio in (1,10,100)]
 for p,hsh in hashes.items():assert sha(Path(p))==hsh,'predecessor modified'
 return {'passed':True,'claim_boundary':'Conditional necessary perturbative diagnostics only; not certified physical pole/width, full resummed vacuum, error enclosure, or compactification prediction.','verifier_sha256':sha(Path(__file__)),'source_hashes':hashes,'mpmath_dps':mp.mp.dps,'derivative_units':'Pi_prime(s0)=epsilon * dimensionless_coefficient; Q2 fixed at epsilon M2 during derivative','derivative':{'scalar':pack(scalar_der),'vector':pack(vector_der),'mixed':pack(mixed_der),'total_Landau':pack(analytic),'independent_adaptive_five_point':derivatives},'coefficient':pack(C),'scalar_shells':[{'m2':a,'multiplicity':E.shape[1]} for a,E in ss],'vector_shells':[{'m2':a,'multiplicity':E.shape[1]} for a,E in vs],'physical_flats':F.shape[1],'Goldstones':G.shape[1],'scalar_channels':scalar,'VV_channels':vec,'SV_channels':mix,'Landau_projector_thresholds':unphysical,'inactive_scalar_channels':inactive,'support_classification':{'scalar_weight_cut':1e-14,'vector_mixed_weight_cut':1e-16,'scalar_total_omitted_weight':sum(r['weight'] for r in inactive),'radial_radial_soft_structural_identity_residual':th_res,'scope':'floating support only; T_h h parallel h implies exact zero soft+radial scalar coupling in declared sum-of-squares action; arbitrary perturbations need new threshold analysis'},'displacement':displacement,'distances':{'nearest_other_scalar_pole':gap,'nearest_active_threshold':active_threshold_gap,'nearest_active_physical_threshold':physical_threshold_gap,'inactive_radial_plus_soft_threshold_distance':0},'epsilon_diagnostic_coefficients':coeff,'conditional_bounds':bounds,'epsilon_scan':scans,'rxi_collisions':{'pole_and_equal_GG':xi_poles,'physical_G':xi_pg,'GG':xi_gg,'no_uniform_xi_window':True},'EFT_conditional_cutoff_examples':eft,'negative_controls':controls,'unclosed':['full physical-flat IR resummation/stability','bounds on higher loops and finite matching','offdiagonal selfenergy norm for quantitative Schur control','nonexceptional fixed-xi domain and gauge-dependent wavefunction','independent cutoff and higher-dimensional Wilson coefficients','independent epsilon and M selection']}

if __name__=='__main__':
 out=compute();path=P/'receipt.json'
 if '--create' in sys.argv:
  with path.open('x') as f:json.dump(out,f,indent=2)
 else:
  saved=json.loads(path.read_text());assert out==saved,'saved receipt mismatch; do not regenerate'
 print(json.dumps({k:out[k] for k in ('passed','derivative','distances','epsilon_diagnostic_coefficients','conditional_bounds','displacement','negative_controls')},indent=2))
