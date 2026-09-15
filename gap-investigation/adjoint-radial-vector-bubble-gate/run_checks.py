"""Independent threshold-split Gauss integration check of the analytic finite VV result."""
import importlib.util,json
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent;s=importlib.util.spec_from_file_location('vv',HERE/'calculation.py');v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
base=v.compute(512);M=v.load(v.ROOT/'shifted-vacuum-gate/calculation.py','shift_check');x,B,c,R,T,si,aa=M.setup();rv=np.zeros(188);rv[108:186]=x[108:186]/np.linalg.norm(x[108:186]);K=R@x;dK=R@rv
mass,U=np.linalg.eigh(K@K.T);mass[np.abs(mass)<1e-10]=0;D=U.T@(dK@K.T+K@dK.T)@U;s0=4320.;n=512;z,w=np.polynomial.legendre.leggauss(n);u=(z+1)/2;w=w/2;cache={}
def BI(a,b):
 key=(a,b)
 if key in cache:return cache[key]
 roots=np.roots([s0,a-b-s0,b]);cuts=[0.]+sorted(float(r.real) for r in roots if abs(r.imag)<1e-10 and 0<r.real<1)+[1.];q=0j
 for lo,hi in zip(cuts,cuts[1:]):
  xx=lo+(hi-lo)*u;dd=xx*a+(1-xx)*b-s0*xx*(1-xx);ad=np.maximum(abs(dd),max(a,b,s0)*(hi-lo)/(n*n));q+=(hi-lo)*np.sum(w*np.log(ad));mid=(lo+hi)/2
  if mid*a+(1-mid)*b-s0*mid*(1-mid)<0:q-=1j*np.pi*(hi-lo)
 cache[key]=q;return q
def A(a):return a*(np.log(a)-1)
def ker(a,b):
 ab,a0,zb,zz=BI(a,b),BI(a,0),BI(0,b),complex(np.log(s0)-2,-np.pi);X=(A(b)+a*ab-a*a0)/b;Y=(A(a)+b*ab-b*zb)/a;uu=(ab-zb)/a;vv=(ab-a0)/b;ww=(ab-zb-a0+zz)/(a*b);return 2*ab+(X+Y+2*ab-2*s0*(uu+vv)+s0*s0*ww)/4+2
tot=sum(D[i,j]**2*ker(a,b) for i,a in enumerate(mass) if a>0 for j,b in enumerate(mass) if b>0 and abs(D[i,j])>1e-12)/(32*np.pi**2);ref=complex(base['result']['transverse_VV_bubble_real'],base['result']['transverse_VV_bubble_imag']);diff=abs(tot-ref)
out={'passed':bool(diff<0.5),'independent_method':'separate 512-point threshold-split Gauss integration (analytic receipt uses root antiderivative)','independent_real':float(tot.real),'independent_imag':float(tot.imag),'abs_difference':float(diff),'relative_difference':float(diff/abs(ref)),'tolerance_reason':'Direct quadrature suffers amplified cancellation among B functions; agreement is required to 0.5 absolute (<0.7%).'}
(HERE/'verification.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2));assert out['passed']

