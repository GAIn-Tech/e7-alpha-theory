"""Leading two-Goldstone momentum matching, MSbar Landau, M=1.
Run native Python -B. Inputs and old receipts never overwritten.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import sys,json,hashlib,importlib.util,math
from pathlib import Path
from decimal import Decimal,localcontext
import numpy as np
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
PI=Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def bubble(s,g):
 """I=-B of 1406.2652 (A.4). Return Re, Im at muhat^2=1.
 Decimal analytic evaluation at s<0 or s>4g. Small |s/g| uses
 convergent beta-integral series, avoiding cancellation at s=0.
 """
 s=Decimal(str(s));g=Decimal(str(g))
 if g<=0:raise ValueError('regulator must be positive, not clipped')
 if s==0:return g.ln(),Decimal(0)
 if abs(s/g)<Decimal('.1'):
  z=s/g;res=g.ln()
  for n in range(1,50):res-=z**n*Decimal(math.factorial(n)**2)/Decimal(n*math.factorial(2*n+1))
  return res,Decimal(0)
 if s<0:
  b=(1-4*g/s).sqrt()
  return g.ln()-2+b*((b+1)**2/(-4*g/s)).ln(),Decimal(0)
 if s>4*g:
  b=(1-4*g/s).sqrt()
  return g.ln()-2+b*((b+1)**2/(4*g/s)).ln(),-PI*b
 raise ValueError('this implementation excludes intermediate timelike below-threshold points')

def quadrature(s,g,n):
 """Independent real quadrature, split at physical branch points.
 Squared endpoint maps tame logarithmic integrable root singularities.
 Imaginary part follows measure of negative Feynman denominator.
 """
 z,w=np.polynomial.legendre.leggauss(n);u=(z+1)/2;w=w/2
 if s>4*g:
  b=math.sqrt(1-4*g/s);cuts=[0,(1-b)/2,(1+b)/2,1]
 else:cuts=[0,1]
 val=0
 for a,b in zip(cuts,cuts[1:]):
  mid=(a+b)/2
  for end,sign in ((a,1),(b,-1)):
   t=end+sign*(b-a)/2*u*u
   v=np.abs(g-s*t*(1-t))
   assert np.all(v>0)
   val+=np.sum(w*(b-a)*u*np.log(v))
 imag=-math.pi*math.sqrt(1-4*g/s) if s>4*g else 0
 return complex(val,imag)

def integrals(coeff,shell):
 rows=[];validation=[]
 with localcontext() as ctx:
  ctx.prec=90;c=Decimal(str(coeff));ss=Decimal(str(shell))
  for s,g in [(-1,.2),(-1,.01),(4,.1),(4,.01),(.001,1),(-.001,1)]:
   re,im=bubble(s,g);v=complex(float(re),float(im))
   e=[]
   for n in (128,256,512):e.append(abs(quadrature(s,g,n)-v))
   assert e[-1]<2e-9,(s,g,e)
   validation.append({'s':s,'g':g,'quadrature_absolute_errors_128_256_512':e})
  for stype,s in [('spacelike',-ss),('tree_shell',ss)]:
   target_real=abs(s).ln()-2;target_im=-PI if s>0 else Decimal(0)
   for gs in ['1e-4','1e-8','1e-16','1e-32','1e-60']:
    g=Decimal(gs);re,im=bubble(s,g);curv=c*g.ln();diff=c*(re-g.ln());good=curv+diff
    missing=curv+c*re;wrong=curv-diff
    assert abs(good-c*re)<max(Decimal(1),abs(c))*Decimal('1e-80')
    rows.append({'momentum':stype,'s_hat':str(s),'G_hat':gs,'curvature_over_epsilon2':str(curv),'Pi_s_minus_Pi_0_real_over_epsilon2':str(diff),'matched_real_over_epsilon2':str(good),'matched_imag_over_epsilon2':str(c*im),'massless_limit_real_over_epsilon2':str(c*target_real),'massless_limit_imag_over_epsilon2':str(c*target_im),'limit_error':str(abs(good-c*target_real)+abs(c*(im-target_im))),'negative_missing_subtraction':str(missing),'negative_wrong_sign':str(wrong)})
   last=rows[-1];assert Decimal(last['limit_error'])<Decimal('1e-54')
   # Divergent negative-control slopes approach c and 2c per log G.
   a,b=rows[-2:];dl=Decimal(b['G_hat']).ln()-Decimal(a['G_hat']).ln()
   assert abs((Decimal(b['negative_missing_subtraction'])-Decimal(a['negative_missing_subtraction']))/dl-c)<Decimal('1e-28')
   assert abs((Decimal(b['negative_wrong_sign'])-Decimal(a['negative_wrong_sign']))/dl-2*c)<Decimal('1e-28')
  small=[]
  for ratio in ['1e-2','1e-4','1e-8','1e-16']:
   g=Decimal('.01');s=g*Decimal(ratio);re,im=bubble(s,g);difference=re-g.ln()
   # I(s,G)-I(0,G)=-s/(6G)+O((s/G)^2).
   small.append({'s_over_G':ratio,'difference_over_s_over_G':str(difference/Decimal(ratio))})
  assert abs(Decimal(small[-1]['difference_over_s_over_G'])+Decimal(1)/6)<Decimal('1e-16')
 return {'quadrature_validation':validation,'fixed_nonzero_momentum_scan':rows,'small_momentum_at_fixed_G':small}

def compute():
 M=load(ROOT/'shifted-vacuum-gate/calculation.py','shift_pole');IR=load(ROOT/'ir-resummed-vacuum-gate/calculation.py','ir_pole');IR.M=M
 receipts={}
 for name in ['shifted-vacuum-gate/receipt.json','ir-resummed-vacuum-gate/receipt.json','ir-resummed-vacuum-gate/resummation-receipt.json','ir-resummed-vacuum-gate/soft-tadpole-receipt.json']:
  p=ROOT/name;r=json.loads(p.read_text());receipts[name]=r
  for k,h in r['source_hashes'].items():assert sha(Path(k))==h,(k,'changed input')
 old=receipts['shifted-vacuum-gate/receipt.json'];t=json.loads((ROOT/'ir-resummed-vacuum-gate/projected-tensors.json').read_text())
 x,B,c,R,T,si,a=M.setup();_,grad,H,J,f=M.tree(x,B,c)
 assert np.linalg.norm(f)<1e-10 and np.linalg.norm(grad)<1e-8
 D,inv,exact=M.exact_singlet_inverse(x,B,c,T,si,a)
 assert exact==old['exact_singlet_inverse'],'exact rational residual/Hessian changed'
 G=np.array(t['basis_G']);F=np.array(t['basis_F']);Q=M.null(R@x)
 assert G.shape==(188,67) and Q.shape==(188,121)
 gauge_err=float(np.linalg.norm(G@G.T@(R@x).T-(R@x).T))
 assert gauge_err<1e-10 and np.linalg.norm(H@G)<1e-8
 _,tad,HL=IR.hard(x,B,c,R,np.eye(188));HL=(HL+HL.T)/2
 shift=np.array(old['leading_delta_canonical']);H1=IR.tree_dH(x,shift,B)+HL
 S=np.column_stack((G,F));summed=S.T@H1@S
 assert np.max(abs(summed-np.array(t['sum_over_epsilon_squared'])))<1e-9
 assert np.linalg.norm(summed[:,:67],2)<1e-7
 # Singlet tree degenerate perturbation, with canonical metric not raw rational metric.
 Z=np.linalg.qr(D)[0];hz=Z.T@H@Z;z,U=np.linalg.eigh(hz)
 E=Z@U[:,abs(z-4)<1e-7]
 assert np.linalg.norm(E@E.T@np.eye(188)[:,186]-np.eye(188)[:,186])<1e-8
 d,W=np.linalg.eigh(E.T@H1@E);modes=E@W
 overlaps=modes[186]**2;k=int(np.argmax(overlaps));v=modes[:,k]
 if v[186]<0:v=-v
 assert np.linalg.norm((R@x)@v)<1e-9
 assert np.linalg.norm(H@v-4*v)<1e-8
 assert np.linalg.norm(E.T@(H1@v-d[k]*v))<1e-7
 phi=np.eye(188)[:,186];bare_offdiag=float(np.linalg.norm((np.eye(188)-np.outer(phi,phi))@H1@phi))
 assert bare_offdiag>1e-3
 L=G.T@IR.tree_dH(x,v,B)@G;coeff=float(np.sum(L*L)/(32*np.pi**2))
 # Ward derivative: T(v) R_a x + H R_a v = R_a H v at tree stationarity.
 dHv=IR.tree_dH(x,v,B)
 ward=float(np.max(abs((dHv@(R@x).T).T+(H@(R@v).T).T-R@(H@v))))
 assert ward<1e-8
 fd=[]
 for h in [1e-3,5e-4,2.5e-4]:
  difference=(M.tree(x+h*v,B,c)[2]-M.tree(x-h*v,B,c)[2])/(2*h)
  fd.append(float(np.max(abs(G.T@difference@G-L))))
 assert max(fd)<1e-8
 # Full physical 121x121 two-Goldstone log coefficient, including off-diagonal entries.
 couplings=np.array([G.T@IR.tree_dH(x,q,B)@G for q in Q.T])
 flat=couplings.reshape(121,-1);C=flat@flat.T/(32*np.pi**2)
 assert np.linalg.norm(C-C.T)<1e-10
 assert min(np.linalg.eigvalsh(C))>-1e-8
 cq=Q.T@v;assert abs(cq@C@cq-coeff)<1e-8
 flat_coupling=float(np.linalg.norm(np.einsum('ia,ijk->ajk',Q.T@F,couplings)))
 assert flat_coupling<1e-7
 phi_coeff=float((Q.T@phi)@C@(Q.T@phi));assert abs(phi_coeff-1/(4*np.pi**2))<1e-10
 # Full corrected singlet mass matrix at actual saved shifted point: eigenvector convergence.
 xp0=np.array(old['hard_mode_stationary_solution']['singlet_coordinates']);sample=[]
 for eps in (1e-7,5e-8,2.5e-8):
  xp=x+eps*shift
  Qp=M.null(R@xp);Zp=np.linalg.qr(Qp@(Qp.T@D))[0]
  _,_,Hp,_,_=M.tree(xp,B,c);_,_,Lp=IR.hard(xp,B,c,R,Zp)
  hphys=Zp.T@Hp@Zp+eps*(Zp.T@Lp);hphys=(hphys+hphys.T)/2
  zp,Up=np.linalg.eigh(hphys);vp=Zp@Up;kk=int(np.argmax(abs(vp.T@v)))
  sample.append({'epsilon':eps,'mass_squared_over_epsilon':float(zp[kk]),'leading_mass_correction':float((zp[kk]-4)/eps),'Phi_weight':float(vp[186,kk]**2),'overlap_squared_with_leading_mode':float((vp[:,kk]@v)**2)})
 assert sample[-1]['overlap_squared_with_leading_mode']>.999999
 # Common infinitesimal G is an IR regulator only, not a physical Goldstone mass assignment.
 ints=integrals(coeff,4)
 # An isolated, nondegenerate physical radial eigenmode avoids the Phi
 # degeneracy ambiguity in interpreting the leading on-shell projection.
 ar=np.zeros(188);ar[108:186]=x[108:186]/np.linalg.norm(x[108:186])
 mass_ar=float(ar@H@ar)
 assert abs(mass_ar-4320)<1e-8 and np.linalg.norm(H@ar-mass_ar*ar)<1e-8
 assert sum(abs(np.linalg.eigvalsh(H)-mass_ar)<1e-7)==1
 assert np.linalg.norm((R@x)@ar)<1e-9
 Lar=G.T@IR.tree_dH(x,ar,B)@G;car=float(np.sum(Lar*Lar)/(32*np.pi**2))
 ar_ints=integrals(car,4320)
 ardata={'tree_mass_squared_over_epsilon':mass_ar,'full_tree_multiplicity':1,'direction':'adjoint A0 / sqrt(B(A0,A0)); all h and Phi components zero','two_Goldstone_log_coefficient':car,'hard_mass_shift_over_epsilon_squared':float(ar@H1@ar),'integrals':ar_ints}
 # Degenerate Phi sector requires a matrix pole problem even after log cancellation.
 flatE=np.array([G.T@IR.tree_dH(x,e,B)@G for e in E.T]).reshape(E.shape[1],-1)
 CE=flatE@flatE.T/(32*np.pi**2);HE=E.T@H1@E
 partial=HE+CE*(math.log(4)-2-1j*math.pi)
 pe=np.linalg.eigvals(partial)
 partialdata={'hard_curvature_matrix':HE.tolist(),'Goldstone_coefficient_matrix':CE.tolist(),'commutator_norm':float(np.linalg.norm(HE@CE-CE@HE)),'partial_pole_shift_eigenvalues':[{'real':float(y.real),'imag':float(y.imag)} for y in sorted(pe,key=lambda y:y.real)],'scope':'Only hard curvature plus two-Goldstone momentum-matched bubble. Missing hard momentum and other soft diagrams, so these are NOT full pole eigenvalues.'}
 allpaths=[Path(__file__),ROOT/'shifted-vacuum-gate/calculation.py',ROOT/'ir-resummed-vacuum-gate/calculation.py',ROOT/'ir-resummed-vacuum-gate/projected-tensors.json']+[ROOT/n for n in receipts]+list((ROOT/'ir-resummed-vacuum-gate/sources').glob('*.pdf'))
 out={'passed':True,'claim_boundary':'Leading one-loop two-Goldstone bubble log cancellation, full transverse coefficient block and Phi-containing degenerate-perturbation radial mode; not a full gauge-independent pole or two-loop stationary theory.','gauge_tangent_projection_error':gauge_err,'trilinear_Ward_max_abs':ward,'trilinear_FD_errors':fd,'tree_eigenvalue_4_singlet_multiplicity':len(d),'degenerate_mass4_shifts':d.tolist(),'degenerate_modes_Phi_weights':overlaps.tolist(),'selected_mode':{'index':k,'tree_mass_squared_over_epsilon':4,'mass_shift_over_epsilon_squared':float(d[k]),'Phi_weight':float(v[186]**2),'bare_Phi_offdiagonal_H1_norm':bare_offdiag,'two_Goldstone_log_coefficient':coeff,'canonical_components_nonzero':[{'index':i,'value':float(y)} for i,y in enumerate(v) if abs(y)>1e-10],'small_epsilon_full_singlet_checks':sample},'full_transverse':{'dimension':121,'coefficient_eigenvalues':np.linalg.eigvalsh(C).tolist(),'physical_flat_trilinear_norm':flat_coupling,'bare_Phi_log_coefficient':phi_coeff},'integrals':ints,'source_hashes':{str(p):sha(p) for p in allpaths}}
 tensors={'basis_G':G.tolist(),'basis_Q':Q.tolist(),'selected_radial_mode':v.tolist(),'selected_radial_GG_trilinear':L.tolist(),'transverse_log_coefficient':C.tolist()}
 out['isolated_adjoint_radial']=ardata
 out['Phi_degenerate_partial_pole_block']=partialdata
 tensors['isolated_adjoint_radial_mode']=ar.tolist()
 tensors['isolated_adjoint_radial_GG_trilinear']=Lar.tolist()
 return out,tensors,couplings
if __name__=='__main__':
 p=HERE/'receipt.json';tp=HERE/'tensors.json'
 if '--create' not in sys.argv:
  old=json.loads(p.read_text());old_t=json.loads(tp.read_text())
  for k,h in old['source_hashes'].items():assert sha(Path(k))==h
 out,tensors,couplings=compute()
 if '--create' in sys.argv:
  with p.open('x') as f:json.dump(out,f,indent=2)
  with tp.open('x') as f:json.dump(tensors,f,indent=2)
  np.save(HERE/'transverse-trilinears.npy',couplings,allow_pickle=False)
 else:
  assert out==old and tensors==old_t,'saved numerical replay differs'
  assert np.array_equal(couplings,np.load(HERE/'transverse-trilinears.npy',allow_pickle=False))
 print(json.dumps({k:v for k,v in out.items() if k not in ['integrals','source_hashes','full_transverse']},indent=2))
