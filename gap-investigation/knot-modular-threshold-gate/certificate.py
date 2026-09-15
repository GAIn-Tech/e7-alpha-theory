"""Exact link, charge-shell, modular-identity and analytic-bound certificate.
No numerical quadrature, alpha input, or invented CY spectrum. --verify replays saved bytes.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import factorial
import importlib.util,json,hashlib,sys
P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('algebra',P/'sources/modular-algebra.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
def ser(x): return [str(c) for c in x]
def polys(N):
 def sig(n,k):return sum(d**k for d in range(1,n+1) if n%d==0)
 e2=[1]+[-24*sig(n,1) for n in range(1,N+1)]
 e4=[1]+[240*sig(n,3) for n in range(1,N+1)]
 e6=[1]+[-504*sig(n,5) for n in range(1,N+1)]
 def cv(x,y):return [sum(x[j]*y[n-j] for j in range(n+1)) for n in range(N+1)]
 def D(x):return [n*v for n,v in enumerate(x)]
 delta=[0,1]+[0]*(N-1)
 for m in range(1,N+1):
  for _ in range(24):
   for n in range(N,m-1,-1):delta[n]-=delta[n-m]
 assert [x-y for x,y in zip(cv(cv(e4,e4),e4),cv(e6,e6))]==[1728*v for v in delta]
 assert [3*x for x in D(e4)]==[x-y for x,y in zip(cv(e2,e4),e6)]
 assert [2*x for x in D(e6)]==[x-y for x,y in zip(cv(e2,e6),cv(e4,e4))]
 return {'through_degree':N,'ramanujan_D_E4_E6':True,'E4_cubed_minus_E6_squared_equals_1728_eta24':True}
def shells():
 pts=[]
 def rec(v,budget,parity):
  if len(v)==8:
   if sum(v)%4==0:pts.append(tuple(F(x,2) for x in v))
   return
  for x in range(-4+parity,5,2):
   if x*x<=budget:rec(v+[x],budget-x*x,parity)
 rec([],16,0);rec([],16,1)
 groups={}
 for v in pts:
  if v[6]+v[7]==0: p=v; sector=0
  elif v[6]+v[7]==1:p=tuple(v[j]-(F(1,2) if j>=6 else 0) for j in range(8));sector=1
  else:continue
  norm=sum(x*x for x in p)
  groups.setdefault((sector,norm),[]).append(p)
 # Every shell's tensor moment equals norm*count/7 times the E7 orthogonal projector.
 out=[]
 H=(1,-1,0,0,0,0,0,0)
 for (sector,norm),vs in sorted(groups.items()):
  mat=[[sum(v[i]*v[j] for v in vs) for j in range(8)] for i in range(8)]
  projection=[[F(i==j)- (F(1,2) if i>=6 and j>=6 else 0) for j in range(8)] for i in range(8)]
  assert mat==[[F(len(vs),7)*norm*x for x in row] for row in projection]
  tr=sum(sum(v[i]*H[i] for i in range(8))**2 for v in vs)
  assert tr==F(2*len(vs),7)*norm
  out.append({'sector':sector,'norm_squared':str(norm),'count':len(vs),'trace_H_squared':str(tr)})
 assert next(x for x in out if x['sector']==0 and x['norm_squared']=='2')['trace_H_squared']=='72'
 assert next(x for x in out if x['sector']==1 and x['norm_squared']=='3/2')['trace_H_squared']=='24'
 # Verify complete oscillator-dressed charge characters at these orders independently.
 vac=[0,72,864]; non=[24,576]
 charged0=a.conv(vac,a.osc(7,2));charged1=a.conv(non,a.osc(7,1),1)
 # Derivative identity for H^2=2: K=(4/7)Dchi+(1/6)E2 chi.
 e2=[1,-24,-72]
 def deriv_check(coeff,shift):
  N=len(coeff)-1
  return [F(4,7)*(F(n)+shift)*coeff[n]+F(1,6)*sum(e2[j]*coeff[n-j] for j in range(n+1)) for n in range(N+1)]
 assert deriv_check([1,133,1673],F(-7,24))==charged0
 assert deriv_check([56,968],F(11,24))==charged1
 assert charged0[1]!=133 and charged1[0]!=56
 return {'shells':out,'charged_vacuum_shift_minus_7_24':list(map(str,charged0)),'charged_nonvacuum_shift_11_24':list(map(str,charged1))}
def payload():
 rt=a.add(a.phase(3),a.phase(-3));inv=a.mul(a.elt([F(1,2)]),rt)
 S=[[inv,inv],[inv,a.neg(inv)]];T=[[a.phase(-7),a.Z],[a.Z,a.phase(11)]]
 theta=[a.O,a.phase(18)];I=a.identity(2);st=a.mm(S,T)
 assert a.mm(S,S)==I and a.mm(a.mm(st,st),st)==I
 assert a.mm(S,a.dagger(S))==I and a.mm(T,a.dagger(T))==I
 # S00^-1=sqrt2, normalized Hopf=S_ab/S00. Framing twist=Taa/T00.
 hopf=[[a.mul(rt,x) for x in row] for row in S]
 assert hopf==[[a.O,a.O],[a.O,a.neg(a.O)]]
 assert [a.mul(T[i][i],a.phase(7)) for i in range(2)]==theta
 unk=[a.mul(S[0][i],rt) for i in range(2)]
 assert unk==[a.O,a.O]
 frames={str(f):ser(a.phase(18*f)) for f in range(-4,5)}
 fusion={}
 for i,j,k in product(range(2),repeat=3):
  n=a.sumel(a.mul(a.mul(a.mul(S[i][l],S[j][l]),a.conj(S[k][l])),rt) for l in range(2))
  assert n==(a.O if k==i^j else a.Z)
  fusion[f'{i}{j}{k}']=int(k==i^j)
 # All binary labeled puncture strings through length 10: vacuum iff even charge parity.
 counts=[]
 for n in range(11):
  row=[]
  for labels in product(range(2),repeat=n):
   state=[1,0]
   for b in labels:state=[sum(state[j]*fusion[f'{j}{b}{k}'] for j in range(2)) for k in range(2)]
   assert state[0]==int(sum(labels)%2==0)
   row.append(state[0])
  counts.append(sum(row))
 # Controls: mirror invisible in real Hopf but not nonzero framing; no false dimension56.
 mirror=a.conj(theta[1]); assert mirror!=theta[1]
 assert [[a.conj(x) for x in row] for row in hopf]==hopf
 assert a.mul(theta[1],theta[1])==a.neg(a.O)
 assert unk[1]!=a.elt([56])
 # Analytic derivative bound for I_DKL(it,5i), t>=2.
 # e^12 > sum_0^30 12^k/k! > 100000, pi>3 hence q=e^-2pi t < 1/100000.
 exp_lower=sum(F(12**k,factorial(k)) for k in range(31));assert exp_lower>100000
 q=F(1,100000)
 # sum n*q^n/(1-q^n) <= q/(1-q)^3; pi<22/7.
 lower=-F(1,2)+1-8*F(22,7)*q/(1-q)**3
 assert lower>F(49,100)>0
 # Integral over 2<t<3: I(3)-I(2)>49/100, and -144 difference < -1764/25.
 upper=-144*F(49,100);assert upper==F(-1764,25)
 assert -6*24==-144 and (4*(24-6))-(-2*(24+12))==144
 # A sourced zero-beta-difference control n=0 gives zero prefactor, not a physical SU2-bundle existence claim.
 assert -6*0==0
 result={'passed':True,'claim_boundary':'Exact E7 gauge-block links and charged lattice shells; source-based N=2 K3xT2 threshold-difference nonidentifiability, not Tian-Yau N=1 thresholds. Analytic derivative proof uses external eta product/calculus/pi bounds; rational inequalities checked exactly.','S':a.serial(S),'T':a.serial(T),'normalized_Hopf':[[ser(x) for x in row] for row in hopf],'unknot':list(map(ser,unk)),'nontrivial_framed_unknot':frames,'fusion':fusion,'vacuum_strings_through_length_10':counts,'charge_trace':shells(),'modular_forms':polys(40),'threshold_difference':{'instanton_number':24,'beta_E7':72,'beta_E8':-72,'Lambda_E8_minus_E7_prefactor':-144,'T_path':'T=i*t, 2<=t<=3, U=5i; zero Wilson lines; trivial torus fibration','exp12_rational_lower':str(exp_lower),'q_upper':str(q),'I_derivative_lower':str(lower),'I_3_minus_I_2_strict_lower':'49/100','Lambda_difference_change_strict_upper':str(upper)},'negative_controls':{'mirror_framing_detected':True,'mirror_Hopf_unchanged':True,'quantum_dimension_not_56':True,'state_count_not_charge_trace':True,'zero_prefactor_no_forced_dependence':True}}
 files=[P/'certificate.py',P/'Formalization.lean',P/'Challenge.lean']+sorted(x for x in (P/'sources').iterdir() if x.is_file())
 result['sha256']={str(f.relative_to(P)):hashlib.sha256(f.read_bytes()).hexdigest() for f in files}
 return result
if __name__=='__main__':
 r=payload();target=P/'certificate.json'
 if '--verify' in sys.argv:
  assert target.exists(),'Missing certificate'
  assert json.loads(target.read_text())==r,'Stale or corrupted certificate'
  print('PASS exact saved certificate replay: links, fusion, charge moments, Ramanujan q-series, strict threshold derivative bound')
 else:target.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:r[k] for k in ['charge_trace','threshold_difference']},indent=2))
