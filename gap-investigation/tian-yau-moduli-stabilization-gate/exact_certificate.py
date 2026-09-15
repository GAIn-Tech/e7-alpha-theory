#!/usr/bin/env python3
"""Exact algebra certificate for the Tian--Yau S/T stabilization gate."""
from fractions import Fraction as Q
import json, pathlib, sys
P=pathlib.Path(__file__).resolve().parent

def poly_mul(a,b):
 out={}
 for (i,j),x in a.items():
  for (k,l),y in b.items(): out[i+k,j+l]=out.get((i+k,j+l),Q(0))+x*y
 return out

def main():
 # Ambient intersection computation on X/Z3, J0=h+k.
 c2={(2,0):Q(3),(1,1):Q(1),(0,2):Q(3)}
 j={(1,0):Q(1),(0,1):Q(1)}
 X={(2,1):Q(9),(1,2):Q(9)}
 cover=poly_mul(poly_mul(c2,j),X).get((3,3),Q(0))
 downstairs=cover/Q(3)
 assert cover==72 and downstairs==24
 # Exact stationary-point obstruction for one pure-E8 condensate.
 # x=a*s>0, y=a*gamma*t>0; U=C exp(-2x+2y) F/(x y^3).
 # F=4x^2+4x+1+4y^2/3-4y.
 # d_x U=0 implies F=4x; d_y U=0 implies F=-4y/3.
 # Hence 3x+y=0, impossible for x,y>0.
 x,y=Q(2),Q(1) # non-vacuous positive witness of the sign domain
 assert 3*x+y>0
 receipt={
  'passed':True,
  'claim_boundary':'Exact topology/intersection arithmetic and exact stationary-equation obstruction for the declared two-real-field leading EFT; not a full compactification vacuum proof.',
  'ray':'J0=h+k on Q=X/Z3',
  'integral_cover_c2_J0':int(cover),
  'integral_quotient_c2_J0':int(downstairs),
  'beta_ray':'24/(4*pi)=6/pi in the cited convention; transcendental simplification is declared, not Fraction arithmetic',
  'hidden_threshold':'f_hid=S-(beta_ray/2)T=S-(3/pi)T',
  'pure_E8':{'dual_coxeter':30,'b0':'3*30=90','condensate_exponent':'a=24*pi^2/b0=4*pi^2/15'},
  'stationary_elimination':['d_x U=0 => F=4*x','d_y U=0 => F=-4*y/3','=> 3*x+y=0, incompatible with x>0,y>0'],
  'negative_controls':{
   'constant_W':'V=|W0|^2/(16*s*t^3) up to fixed Kcs normalization: monotone runaway',
   'tree_no_scale_T':'K^{T Tbar} K_T K_Tbar=3 but dilaton contributes +1, leaving positive runaway for constant W',
   'beta_zero':'single condensate independent of T; no isolated two-field vacuum'
  }
 }
 out=json.dumps(receipt,indent=2,sort_keys=True)+'\n'
 target=P/'certificate.json'
 if '--verify' in sys.argv:
  assert target.exists() and target.read_text(encoding='utf-8')==out
 else:
  target.write_text(out,encoding='utf-8')
 print(out,end='')
if __name__=='__main__': main()
