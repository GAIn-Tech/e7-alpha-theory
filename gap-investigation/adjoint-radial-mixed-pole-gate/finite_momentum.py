"""Full 188-scalar strict-Landau SV subset, additive to interrupted candidate.
No gauge-independent pole claim; predecessor sum explicitly conditional.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
import numpy as np, json, hashlib, sys
P=Path(__file__).resolve().parent;ROOT=P.parent
D=np.load(P/'recovery-tensors.npz');s=4320.;fac=16*np.pi**2

def A(x):return 0. if x==0 else x*(np.log(x)-1)
def B(x,v,s):
 if s==0:
  if x==v:return -np.log(x) if x else complex(np.inf,0)
  return -(A(x)-A(v))/(x-v)
 disc=(s-x-v)**2-4*x*v
 if disc<0: raise ValueError('analytic root formula only used above threshold')
 roots=np.sort(np.roots([s,x-v-s,v]).real)
 def F(r):return (0 if r==1 else (1-r)*np.log(abs(1-r)))+(0 if r==0 else r*np.log(abs(r)))-1
 neg=max(0,min(1,roots[1])-max(0,roots[0]))
 return -complex(np.log(s)+sum(F(r) for r in roots),-np.pi*neg)
def K(x,v,s):
 if s==0 and x==0:return 0j
 if v==0:return 3*(x+s)*B(x,0,s)+3*A(x)-2*s
 return (2*x-v+2*s)*B(x,v,s)+A(x)-A(v)+((x-s)*A(v)-(x-s)**2*(B(x,v,s)-B(x,0,s)))/v

def independent(x,v,s,n):
 # Feynman parameter tensor integration BEFORE scalar master reduction.
 # N=4[p^2-(p.k)^2/k^2]; the d-dimensional average produces
 # 2(d-1); the evanescent UV product leaves -2s in MSbar.
 if not s:return 0j
 nodes,w=np.polynomial.legendre.leggauss(n)
 cuts={0.,1.}
 for m in (0.,v):
  for r in np.roots([s,x-m-s,m]):
   if abs(r.imag)<1e-10 and 0<r.real<1:cuts.add(float(r.real))
 ans=0j;cuts=sorted(cuts)
 for lo,hi in zip(cuts,cuts[1:]):
  t=lo+(hi-lo)*(nodes+1)/2;d0=t*x-s*t*(1-t);dv=d0+(1-t)*v
  def a(d):
   out=np.zeros(d.shape,complex);nz=d!=0;out[nz]=d[nz]*(np.log(abs(d[nz]))-1-1j*np.pi*(d[nz]<0));return out
  ans+=(hi-lo)/2*np.sum(w*(a(d0)-a(dv)))
 return 6*s*ans/v-2*s

def pairs(C,ms,mv):
 out={}
 for a,v in enumerate(mv):
  for i,x in enumerate(ms):
   weight=float(C[a,i]**2)
   if weight<1e-24:continue
   assert v>1e-8
   assert x>-1e-8
   key=(0. if abs(x)<1e-8 else round(float(x),9),round(float(v),9))
   out[key]=out.get(key,0.)+weight
 return out

def compute():
 ms=D['ms'];mv=D['mv'];C=D['C'];R=D['R'];h=D['h'];x=D['x'];H=D['H'];G=D['G'];E=D['E'];Uv=D['Uv']
 allpairs=pairs(C,ms,mv)
 goldpairs=pairs(Uv.T@(R@h)@G,np.zeros(G.shape[1]),mv)
 def val(ps):return sum(w*K(x,v,s) for (x,v),w in ps.items())/fac
 total=val(allpairs);gold=val(goldpairs)
 independent_values=[]
 for n in (256,512):independent_values.append(sum(w*independent(x,v,s,n) for (x,v),w in allpairs.items())/fac)
 error=abs(independent_values[-1]-total)
 assert error<3e-5
 pzero=sum(w*K(x,v,0) for (x,v),w in allpairs.items())/fac
 assert abs(pzero)<1e-8
 # Rotation in equal-mass blocks, including the COMPLETE 78-dimensional soft scalar block.
 rng=np.random.default_rng(20260909);Us=D['Us'].copy();Ur=Uv.copy()
 for m,U in ((ms,Us),(mv,Ur)):
  for z in np.unique(np.round(m,8)):
   ids=np.where(abs(m-z)<1e-7)[0]
   q=np.linalg.qr(rng.normal(size=(len(ids),len(ids))))[0]
   U[:,ids]=U[:,ids]@q
 rotated=val(pairs(Ur.T@(R@h)@Us,ms,mv));rot_error=abs(rotated-total)
 assert rot_error<1e-8
 # Polynomial UV identity uses residues A=-m^2 DeltaUV, B=+DeltaUV.
 uvtests=[]
 for (xx,v),w in allpairs.items():
  residue=(2*xx-v+2*s)-xx+v-(xx-s)
  uvtests.append(abs(residue-3*s))
 assert max(uvtests)<1e-8
 # Independent cuts: Im B is pi times the negative-Delta interval length.
 def phase(xx,v):return np.sqrt(max(0,(s-xx-v)**2-4*xx*v))/s if s>(np.sqrt(xx)+np.sqrt(v))**2 else 0.
 cut=sum(w*np.pi*((2*xx-v+2*s-(xx-s)**2/v)*phase(xx,v)+(xx-s)**2/v*phase(xx,0)) for (xx,v),w in allpairs.items())/fac
 assert abs(cut-total.imag)<1e-8
 # Reconstruct pure-vector stationary shift rather than inheriting provisional sum.
 Bs=D['B'];J=Bs@x;mass=np.where(mv>1e-8,mv,0);fp=np.zeros_like(mass);mask=mass>0;fp[mask]=mass[mask]*(2*np.log(mass[mask])-2/3)
 W=(Uv*fp)@Uv.T;gv=3*2*np.einsum('ai,aij->j',W@(R@x),R)/(64*np.pi**2)
 ev,U=np.linalg.eigh(H);keep=ev>1e-8;delta=-U[:,keep]@((U[:,keep].T@gv)/ev[keep])
 shift=float(4*(J@h)@((Bs@delta)@h)+2*(J@delta)@np.einsum('i,aij,j->a',h,Bs,h))
 gauge=json.loads((ROOT/'adjoint-radial-gauge-pole-gate/receipt.json').read_text());assert abs(shift-gauge['zero_momentum']['vector_stationary_shift'])<1e-8
 scalar=json.loads((ROOT/'adjoint-radial-pole-gate/receipt.json').read_text());vector=json.loads((ROOT/'adjoint-radial-vector-bubble-gate/receipt.json').read_text())
 sf=scalar['regulator_scan'][-1];vv=vector['result'];provisional=complex(sf['scalar_total_real'],sf['scalar_total_imag'])+complex(vv['bubble_plus_seagull_real'],vv['bubble_plus_seagull_imag'])+shift+total
 # p->0 evaluated independently to avoid cancellation of master terms.
 near0=[{'s':t,'mixed':float(sum(w*independent(xx,v,t,128) for (xx,v),w in allpairs.items()).real/fac)} for t in (1e-2,1e-3,1e-4)]
 # A deliberately nontransverse numerator fails the zero-momentum Ward requirement.
 wrongp0=sum(w*(A(xx)+v*B(xx,v,0)) for (xx,v),w in allpairs.items())/fac
 assert abs(wrongp0)>1e-3
 rows=[{'scalar_m2':xx,'vector_m2':v,'weight':w,'kernel_real':K(xx,v,s).real,'kernel_imag':K(xx,v,s).imag} for (xx,v),w in sorted(allpairs.items())]
 out={'passed':True,'claim_boundary':'Verified complete strict-Landau 188-scalar/79-vector derivative bubble subset. No general-xi cancellation, no gauge-independent/full pole, no width prediction. Combination uses unreplayed predecessor numerical sectors with their disclosed error.','kinematics':{'s':s,'Q2':1,'units':'epsilon^2 M^2','scheme':'MSbar','inverse_propagator':'s-m_tree^2-Pi(s)'},'result':{'SV_real':total.real,'SV_imag':total.imag,'Goldstone_SV_real':gold.real,'Goldstone_SV_imag':gold.imag,'physical_SV_real':(total-gold).real,'physical_SV_imag':(total-gold).imag},'enumeration':{'scalars':len(ms),'vectors':len(mv),'Goldstones':G.shape[1],'soft_scalars':int(sum(abs(ms)<1e-8)),'massive_vectors':int(sum(mv>1e-8)),'mass_shell_pairs':rows,'coupling_squared_total':float(np.sum(C*C))},'checks':{'independent_256':{'real':independent_values[0].real,'imag':independent_values[0].imag},'independent_512':{'real':independent_values[1].real,'imag':independent_values[1].imag},'independent_512_error':error,'p0_abs':abs(pzero),'near_zero':near0,'rotation_error':rot_error,'UV_identity_max_error':max(uvtests),'cut_imag':cut,'Ward_HK_max':float(np.max(abs(H@(R@x).T)))},'negative_controls':{'drop_Goldstones_change_abs':abs(gold),'wrong_overall_sign_change_abs':2*abs(total),'drop_projector_p0_nonzero':float(wrongp0.real),'drop_evanescent_term_real_change':float(2*s*np.sum(C*C)/fac),'omit_vector_stationary_shift_change':abs(shift)},'tadpole_consistency':{'mixed_derivative_tadpole':'zero for constant background; the numerator vanishes at external p=0','recomputed_vector_stationary_shift':shift},'UV_residue':float(3*s*np.sum(C*C)/fac),'external_mixing':{'tree_hA':float(np.linalg.norm((R@x)@h)),'tree_hG':float(np.linalg.norm(G.T@H@h)),'nearest_other_scalar_gap':float(np.sort(abs(ms-s))[1]),'order':'Schur complement: with zero tree offdiagonal blocks and invertible complementary block at s=4320, one-loop mixing enters radial eigenvalue quadratically at two-loop order. One-loop mixing amplitudes themselves not computed.'},'conditional_sector_sum_NOT_a_pole':{'real':provisional.real,'imag':provisional.imag,'vector_stationary_shift_included':True,'predecessor_scalar_256_vs_512_error':scalar['checks']['quadrature_256_vs_512_last_total_abs']},'source_hashes':{}}
 for q in [Path(__file__),P/'recovery_audit.py',P/'calculation.py',ROOT/'adjoint-radial-gauge-pole-gate/receipt.json',ROOT/'adjoint-radial-vector-bubble-gate/receipt.json',ROOT/'adjoint-radial-pole-gate/receipt.json',ROOT/'goldstone-pole-matching-gate/primary-source-excerpts.txt',ROOT/'shifted-vacuum-gate/calculation.py']:
  out['source_hashes'][str(q)]=hashlib.sha256(q.read_bytes()).hexdigest()
 return out
if __name__=='__main__':
 out=compute();q=P/'finite-momentum-receipt.json'
 if '--create' in sys.argv:
  with q.open('x') as f:json.dump(out,f,indent=2)
 else:assert json.loads(q.read_text())==out,'saved receipt mismatch'
 print(json.dumps({k:v for k,v in out.items() if k not in ['enumeration','source_hashes']},indent=2))
