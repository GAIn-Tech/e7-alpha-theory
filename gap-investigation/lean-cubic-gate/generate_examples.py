"""Generate transparent finite recursor proof terms, then Lean checks all branches."""
from pathlib import Path
P=Path(__file__).resolve().parent
out=['namespace CubicGate\n']
def emit(s):out.append(s+'\n')
for n in [3,2]:
 N=f'F{n}'; vs=[f'{N}.v{i}' for i in range(n)]
 emit(f'inductive {N} where '+ ' '.join(f'| v{i} : {N}' for i in range(n)))
 def table(k,fn,vals=()):
  if not k:return vs[fn(*vals)%n]
  return f'({N}.rec (motive := fun _ => '+ (' → '.join([N]*k))+') '+ ' '.join('('+table(k-1,fn,vals+(i,))+')' for i in range(n))+')'
 emit(f'noncomputable def add{n} : {N} → {N} → {N} := '+table(2,lambda x,y:x+y))
 emit(f'noncomputable def neg{n} : {N} → {N} := '+table(1,lambda x:-x))
 emit(f'noncomputable def mul{n} : {N} → {N} → {N} := '+table(2,lambda x,y:x*y))
 for i in range(n):
  emit(f'def tag{n}_{i} : {N} → Prop := {N}.rec (motive := fun _ => Prop) '+ ' '.join('UnitP' if j==i else 'Void' for j in range(n)))
  for j in range(n):
   if i!=j:emit(f'theorem neq{n}_{i}_{j} (h : Eqv {vs[i]} {vs[j]}) : Void := Eqv.rec (a := {vs[i]}) (motive := fun q _ => tag{n}_{i} q) UnitP.intro h')
 def proof(names,goal,leaf,env=None):
  env=env or {}
  if not names:return leaf(env)
  x,*rest=names
  def subst(s):
   import re
   for k,v in env.items():s=re.sub(r'\b'+k+r'\b',vs[v],s)
   return s
  mot=('∀ '+ ' '.join(rest)+f' : {N}, ' if rest else '')+subst(goal)
  return f'({N}.rec (motive := fun {x} => {mot}) '+ ' '.join('('+proof(rest,goal,leaf,dict(env,**{x:i}))+')' for i in range(n))+')'
 def th(name,names,goal,leaf=lambda _: 'Eqv.refl'):
  emit(f'theorem {name} : ∀ '+ ' '.join(names)+f' : {N}, '+goal+' := '+proof(names,goal,leaf))
 th(f'rz{n}',['x'],f'Eqv (add{n} x {vs[0]}) x')
 th(f'an{n}',['x'],f'Eqv (add{n} x (neg{n} x)) {vs[0]}')
 th(f'na{n}',['x'],f'Eqv (add{n} (neg{n} x) x) {vs[0]}')
 th(f'can{n}',['a','b','c'],f'Eqv (add{n} a b) (add{n} a c) → Eqv b c',lambda e:'fun _ => Eqv.refl' if e['b']==e['c'] else f'fun h => Void.rec (motive := fun _ => Eqv {vs[e["b"]]} {vs[e["c"]]}) (neq{n}_{(e["a"]+e["b"])%n}_{(e["a"]+e["c"])%n} h)')
 emit(f'noncomputable def core{n} : AddCore {N} := AddCore.mk {vs[0]} add{n} neg{n} rz{n} an{n} na{n} can{n}')
 if n==3:th('noTwo3',['x'],f'Eqv (add3 x x) F3.v0 → Eqv x F3.v0',lambda e:'fun _ => Eqv.refl' if e['x']==0 else f'fun h => Void.rec (motive := fun _ => Eqv {vs[e["x"]]} F3.v0) (neq3_{2*e["x"]%3}_0 h)')
 emit(f'noncomputable def cubic{n} (x y z : {N}) : {N} := mul{n} (mul{n} x y) z')
 for slot,args in [('A',('p','q','y','z')),('B',('x','p','q','z')),('C',('x','y','p','q'))]:
  terms={'A':(f'(add{n} p q) y z','p y z','q y z'),'B':(f'x (add{n} p q) z','x p z','x q z'),'C':(f'x y (add{n} p q)','x y p','x y q')}[slot]
  goal=f'Eqv (cubic{n} {terms[0]}) (add{n} (cubic{n} {terms[1]}) (cubic{n} {terms[2]}))'
  th(f'linear{slot}{n}',list(args),goal)
 emit(f'theorem cubic{n}_nonzero : Eqv (cubic{n} {vs[1]} {vs[1]} {vs[1]}) {vs[0]} → Void := neq{n}_1_0')
 if n==2:
  th('cubic2_invariant',['x','y','z'],'Eqv (cubic2 (neg2 x) (neg2 y) (neg2 z)) (cubic2 x y z)')
  emit('theorem characteristic_two_fails (h : NoTwoTorsion core2) : Void := neq2_1_0 (h F2.v1 Eqv.refl)')
 else:
  emit('theorem cubic3_not_invariant (h : ∀ x y z, Eqv (cubic3 (neg3 x) (neg3 y) (neg3 z)) (cubic3 x y z)) : Void := neq3_2_1 (h F3.v1 F3.v1 F3.v1)')
  emit('theorem zero3_gate : ∀ x y z : F3, Eqv ((fun _ _ _ : F3 => F3.v0) x y z) F3.v0 := invariant_odd_trilinear_vanishes core3 core3 core3 core3 noTwo3 (fun _ _ _ => F3.v0) (fun _ _ _ _ => Eqv.refl) (fun _ _ _ _ => Eqv.refl) (fun _ _ _ _ => Eqv.refl) neg3 neg3 neg3 (fun _ => Eqv.refl) (fun _ => Eqv.refl) (fun _ => Eqv.refl) (fun _ _ _ => Eqv.refl)')
emit('end CubicGate')
for name in ['noTwo3','linearA3','linearB3','linearC3','cubic3_nonzero','cubic3_not_invariant','zero3_gate','linearA2','linearB2','linearC2','cubic2_nonzero','cubic2_invariant','characteristic_two_fails']:
 emit('#print axioms CubicGate.'+name)
(P/'Examples.lean.part').write_text(''.join(out),encoding='utf-8')
