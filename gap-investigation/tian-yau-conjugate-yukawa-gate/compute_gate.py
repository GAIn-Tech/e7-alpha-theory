"""Exact dual cups, cubic-surface adjunction comparisons and X Gysin trace.
No reference matrix/rank is used as input. --create exclusively creates receipts;
default recomputes and compares existing deterministic receipts.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,combinations_with_replacement
import json,hashlib,sys
import sympy as s
import dual_exterior as d
import surface as z
P=Path(__file__).resolve().parent
text=lambda x:json.dumps(x,sort_keys=True,indent=2)+'\n'

def pack(v):return [[list(e),list(U),str(c)] for (e,U),c in sorted(v.items())]
def fmul(v):
 out={}
 for (e,U),cf in v.items():
  for j in range(4):
   ee=tuple(e[i]+3*int(i==j) for i in range(4));z.accum(out,(ee,U),cf/3)
 return out

def homotopy(v):
 out={}
 for (e,U),cf in v.items():
  neg={i for i,a in enumerate(e) if a<0}
  if len(neg)==4:continue
  anchor=next(i for i in range(4) if i not in neg)
  if anchor in U and len(U)>1:
   j=U.index(anchor);z.accum(out,(e,U[:j]+U[j+1:]),(-1)**j*cf)
 return out

def scal(v,x):return {k:x*c for k,c in v.items() if x*c}

def comparison(a,b,ref,reftrace):
 value,h,pr=z.trace(a,b);ratio=value/reftrace
 rem=z.add(h,scal(ref,-ratio));rhs=z.divide_f(z.delta(rem))
 eta=homotopy(rhs);assert z.delta(eta)==rhs
 closed=z.add(rem,scal(fmul(eta),-1));assert not z.delta(closed)
 primitive=homotopy(closed);assert z.delta(primitive)==closed
 assert h==z.add(scal(ref,ratio),z.delta(primitive),fmul(eta))
 return ratio,{'surface_trace':str(value),'ratio_to_H_squared':str(ratio),'adjunction_cocycle':pack(h),'ambient_top_lift':pack(pr),'cech_primitive':pack(primitive),'defining_equation_primitive':pack(eta)}

def lift_surface(form,side):
 out={}
 for (i,e,U),cf in form.items():
  ee=e+(0,)*4 if not side else (0,)*4+e
  for j in range(4):out[(2+4*side+i,),(),ee,U if not side else (j,),(j,) if not side else U]=cf
 return out

def delta_form(form):
 out={}
 for (i,e,U),cf in form.items():
  for j in range(4):
   if j not in U:
    W=tuple(sorted(U+(j,)));z.accum(out,(i,e,W),(-1)**W.index(j)*cf)
 return out

def exact_form(side,ch):
 # A nonzero patch-0 horizontal rational 1-form d(z_j/z_0).
 weights=d.inherited.r.w[4*side:4*side+4]
 j=next(j for j in range(1,4) if weights[j]%3==ch)
 e0=tuple(-2*int(i==0)+int(i==j) for i in range(4))
 ej=tuple(-int(i==0) for i in range(4))
 return {(0,e0,(0,)):F(-1),(j,ej,(0,)):F(1)}

def verify_manifest():
 manifest=json.loads((P/'source-manifest.json').read_text())
 for f,h in manifest.items():assert hashlib.sha256((P/f).read_bytes()).hexdigest()==h,f
 return manifest

def main():
 manifest=verify_manifest()
 old=P/'frozen/tian-yau-colored-yukawa-gate'
 source=json.loads((old/'charged-dual-bases.json').read_text())
 scalar=json.loads((old/'frozen/tian-yau-actual-survivor-coupling-gate/serre-tensor.json').read_text())
 vs={ch:[d.from_dual(d.u.unpack(r['cocycle'])) for r in source['characters'][str(ch)]['records']] for ch in [1,2]}
 bs=[d.from_dual(d.u.unpack(v)) for v in scalar['dual_cocycles'][:2]]
 surfaces={ch:[z.form(r['cocycle'],int(i>=2)) for i,r in enumerate(source['characters'][str(ch)]['records'])] for ch in [1,2]}
 controls={'dual_inputs_closed':0,'degree_one_differential_agreement':0,'nilpotence':0,'wrong_curvature_detected':0,'keywise_Leibniz':0,'wrong_product_sign_detected':0,'representative_changes':0,'surface_boundary_comparisons':0,'beta_euler_comparisons':0}
 for ch in vs:
  for v in vs[ch]:
   d.validate(v,1,ch);assert not d.D(v);controls['dual_inputs_closed']+=1
   for key in v:
    t,I,e,X,Y=key;orig={((t[0],13),I,e,X,Y):F(1)}
    assert d.D({key:F(1)})==d.from_dual(d.c.total(orig));controls['degree_one_differential_agreement']+=1
 # Nilpotence/sign controls include nonclosed exterior-sector generators, not merely cycles.
 for t in combinations_with_replacement(range(13),3):
  if not d.canon(t)[1]:continue
  probe={(t,(),(0,)*8,(0,),(0,)):F(1)}
  assert not d.D(d.D(probe));controls['nilpotence']+=1
  if d.D(d.D(probe,True),True):controls['wrong_curvature_detected']+=1
 assert controls['wrong_curvature_detected']>0
 beta_forms=[];beta_records=[]
 for k,b in enumerate(bs):
  eta=d.beta_primitive(k);d.validate(eta,0,0)
  form=d.add(b,d.scale(d.D(eta),-1));assert form and not d.D(form)
  assert form==lift_surface(z.hyperplane(),k)
  beta_forms.append(form);beta_records.append({'beta':k,'Euler_primitive':d.pack(eta),'dlog_representative':d.pack(form)})
  controls['beta_euler_comparisons']+=1
 H=z.hyperplane();htrace,href,hpr=z.trace(H,H)
 assert htrace!=0
 refdata={'trace':str(htrace),'cocycle':pack(href),'ambient_top_lift':pack(hpr),'ambient_top_projection':str(hpr.get(((-1,)*4,(0,1,2,3)),0))}
 pairdata={};ratios={};hdata={}
 for side in [0,1]:
  for i in range(2*side,2*side+2):
   for j in range(2*side,2*side+2):
    value,rec=comparison(surfaces[1][i],surfaces[2][j],href,htrace)
    ratios[i,j]=value;pairdata[f'{i},{j}']=rec;controls['surface_boundary_comparisons']+=1
  for ch in [1,2]:
   for i in range(2*side,2*side+2):
    value,rec=comparison(surfaces[ch][i],H,href,htrace)
    assert value==0;hdata[f'{ch},{i}']=rec;controls['surface_boundary_comparisons']+=1
 # Nontrivial exact changes stay horizontal, preserve character, and are recomputed through trace.
 change_records=[]
 for ch in [1,2]:
  for i,a in enumerate(vs[ch]):
   side=int(i>=2);eta=exact_form(side,ch);eta_full=lift_surface(eta,side);de=delta_form(eta)
   assert eta and de and d.D(eta_full)==lift_surface(de,side)
   d.validate(eta_full,0,ch);changed=z.add(surfaces[ch][i],de)
   for j,b in enumerate(vs[3-ch]):
    for k,beta in enumerate(bs):
     # Slot-1 change: D(eta wedge b wedge beta), all other factors closed.
     delta=d.wedge(d.wedge(d.D(eta_full),b),beta)
     primitive=d.wedge(d.wedge(eta_full,b),beta)
     assert primitive and delta and delta==d.D(primitive)
     if int(j>=2)==side:
      v1,_=comparison(changed,surfaces[3-ch][j],href,htrace)
      v0,_=comparison(surfaces[ch][i],surfaces[3-ch][j],href,htrace)
      assert v1==v0
     controls['representative_changes']+=1
   assert z.trace(changed,H)[0]==z.trace(surfaces[ch][i],H)[0]
   change_records.append({'character':ch,'flavor':i,'primitive':d.pack(eta_full),'nonzero_boundary':d.pack(d.D(eta_full))})
 # Keywise Leibniz includes C*, B*, Koszul and both Cech directions.
 probes=sorted(set().union(*(set(v) for ch in vs for v in vs[ch])))
 for key in probes:
  aa={key:F(1)};sg=d.parity(d.degree(key))
  for b in [vs[1][0],vs[2][2],bs[0]]:
   lhs=d.D(d.wedge(aa,b));rhs=d.add(d.wedge(d.D(aa),b),d.scale(d.wedge(aa,d.D(b)),sg));assert lhs==rhs
   controls['keywise_Leibniz']+=1
   if d.D(d.wedge(aa,b,True))!=d.add(d.wedge(d.D(aa),b,True),d.scale(d.wedge(aa,d.D(b),True),sg)):controls['wrong_product_sign_detected']+=1
 assert controls['wrong_product_sign_detected']>0
 products=[];slices=[]
 for k,beta in enumerate(bs):
  mat=[]
  for i,a in enumerate(vs[1]):
   row=[]
   for j,b in enumerate(vs[2]):
    cup=d.wedge(d.wedge(a,b),beta);d.validate(cup,3,0);assert not d.D(cup)
    new=d.wedge(d.wedge(a,b),beta_forms[k]);primitive=d.wedge(d.wedge(a,b),d.beta_primitive(k))
    assert d.add(cup,d.scale(new,-1))==d.D(primitive)
    assert d.wedge(d.wedge(a,b),beta)==d.wedge(a,d.wedge(b,beta))
    # This is the sheaf-level exterior-cube image after killing Euler A*.
    bproj=d.raw_b_projection(new)
    assert bproj==d.wedge(d.wedge(lift_surface(surfaces[1][i],int(i>=2)),lift_surface(surfaces[2][j],int(j>=2))),beta_forms[k])
    si,sj=int(i>=2),int(j>=2)
    if si==sj:
     if k==si:
      assert not bproj;value=F(0);reason='actual B-cube vanishes on the single surface cover'
     else:value=ratios[i,j];reason='surface adjunction comparison times opposite hyperplane'
    else:
     assert hdata[f'{1 if si==k else 2},{i if si==k else j}']['surface_trace']=='0'
     value=F(0);reason='explicit primitive for primitive-surface class cup hyperplane'
    row.append(str(value))
    products.append({'beta':k,'row':i,'column':j,'wedge_cocycle':d.pack(cup),'Euler_changed_cocycle':d.pack(new),'Euler_change_primitive':d.pack(primitive),'cotangent_three_form':d.pack(bproj),'relative_trace':str(value),'comparison':reason})
   mat.append(row)
  slices.append(mat)
 Y=[s.Matrix(v).applyfunc(s.Rational) for v in slices]
 # Gysin X subset Sx x Sy of class Hx+Hy: coefficient of Hx^2 Hy^2.
 xx,yy=s.symbols('Hx Hy')
 gysin=lambda expr:s.expand(expr*(xx+yy)).coeff(xx,2).coeff(yy,2)*htrace*htrace
 reference=gysin(xx**2*yy);other=gysin(xx*yy**2)
 assert reference==other and reference!=0
 # Pure reference surfaces have nonzero residue, so this reference top class is nonzero.
 labelsQ=[(i,l) for i in range(4) for l in range(3)];labelsQc=[(j,r) for j in range(4) for r in range(3)]
 B=[s.zeros(3),s.zeros(3)];B[0][1,2]=1;B[1][2,2]=1
 mass=s.Matrix([[sum(Y[k][i,j]*B[k][r,l] for k in range(2)) for j,r in labelsQc] for i,l in labelsQ])
 active=Y[0].row_join(Y[1]);rank=active.rank();assert mass.rank()==rank
 sparse_rank=d.inherited.e.rank
 for mat in Y+[active,mass]:assert sparse_rank([{i:F(str(mat[i,j])) for i in range(mat.rows) if mat[i,j]} for j in range(mat.cols)])==mat.rank()
 bad=s.Matrix([[sum(Y[k][i,j]*B[k][l,r] for k in range(2)) for j,r in labelsQc] for i,l in labelsQ]);assert bad!=mass
 controls['wrong_gauge_transpose_detected']=True
 controls['independent_sparse_rank_checks']=4
 controls['generic_full_slice_rank_rejected']=all(v.rank()<4 for v in Y)
 A=s.eye(4);A[0,2]=2;C=s.eye(4);C[3,1]=-3
 assert (A.T*Y[0]*C).row_join(A.T*Y[1]*C).rank()==rank
 controls['flavor_shear']=True
 result={'passed':True,'claim_boundary':'Exact relative dual cubic slices and gauge block, via actual dual exterior Cech/Koszul cups, Euler primitives, cubic-surface adjunction primitives and Gysin naturality. Common nonzero reference trace remains unconverted to predecessor scalar generator. Not complete exotic removal or stabilized vacuum.','basis_order':'rows: character-1 records 0..3; columns: character-2 records 0..3 in charged-dual-bases.json','relative_slices':slices,'slice_ranks':[v.rank() for v in Y],'active_block':[[str(x) for x in active.row(i)] for i in range(active.rows)],'active_rank':rank,'active_right_kernel':[[str(x) for x in v] for v in active.nullspace()],'per_color_matrix':[[str(x) for x in mass.row(i)] for i in range(mass.rows)],'per_color_rank':mass.rank(),'Qbar_labels':labelsQ,'Qcbar_labels':labelsQc,'normalization':'lambda_dual=trace_X(beta0^2 beta1), provably nonzero, not set to 1 and not identified with charged lambda; beta0 beta1^2 has the same trace','Gysin_reference_product':str(reference),'Gysin_other_product':str(other),'absolute_scalar_comparison_complete':False,'surface_reference':refdata,'surface_pair_comparisons':pairdata,'primitive_hyperplane_comparisons':hdata,'controls':controls}
 chains={'beta_comparisons':beta_records,'representative_change_controls':change_records,'products':products}
 for name,out in [('certificate.json',result),('dual-cup-chains.json',chains)]:
  payload=text(out)
  if '--create' in sys.argv:
   with (P/name).open('x',encoding='utf-8',newline='\n') as f:f.write(payload)
  else:assert (P/name).is_file() and (P/name).read_text(encoding='utf-8')==payload,name
 assert verify_manifest()==manifest
 print(text({k:result[k] for k in ['passed','relative_slices','slice_ranks','active_rank','per_color_rank','controls']}),flush=True)
if __name__=='__main__':main()
