import os
os.environ['OPENBLAS_NUM_THREADS']='1'
from pathlib import Path
import numpy as np, importlib.util
nodes,weights=np.polynomial.legendre.leggauss(128)
def quad(f,a,b,epsabs=None):
 return (sum(w*f(a+(b-a)*(t+1)/2) for t,w in zip(nodes,weights))*(b-a)/2,0)
P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('old',P/'calculation.py');o=importlib.util.module_from_spec(sp);sp.loader.exec_module(o)
def inte(x,v,s):
 def fun(t):
  d0=t*x-s*t*(1-t);dv=d0+(1-t)*v
  def a(d):return 0j if d==0 else d*(np.log(complex(d,-0.0))-1)
  return a(d0)-a(dv)
 cuts={0.,1.}
 for m in [0,v]:
  if s:
   for r in np.roots([s,x-m-s,m]):
    if abs(r.imag)<1e-10 and 0<r.real<1:cuts.add(float(r.real))
 cuts=sorted(cuts);z=0j
 for lo,hi in zip(cuts,cuts[1:]):
  z+=quad(lambda t:fun(t).real,lo,hi,epsabs=1e-9)[0]+1j*quad(lambda t:fun(t).imag,lo,hi,epsabs=1e-9)[0]
 return -6*s*z/v+2*s
for x,v,s in [(0,25,4320),(16.5,16.5,4320),(4,5,1),(0,2,0),(0,25,1e-4)]:print(x,v,s,o.bsv(x,v,s),inte(x,v,s))
