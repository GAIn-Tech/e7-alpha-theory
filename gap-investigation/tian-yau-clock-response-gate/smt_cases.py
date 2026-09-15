from pathlib import Path
import sys,json,hashlib
import z3 as z
P=Path(__file__).resolve().parent
C=z.RealVal('8/3')
def cases():
 out=[]
 def add(n,expected,*constraints):
  s=z.Solver();s.add(*constraints);out.append((n,expected,s.to_smt2()))
 Au,Av,du,dv,m,n,a,y1,y2=z.Reals('Au Av du dv m n a y1 y2')
 add('response_total_chain','unsat',a==Au*du+Av*dv,y1==z.RealVal('16/5')*a,y2==-6*a-m-n,5*y1!=16*(Au*du+Av*dv))
 h,s,D,Du,Dv,k=z.Reals('h s D Du Dv k')
 add('canonical_matching_sign','unsat',k*k==2,k>0,h==C*s+D,h>0,h*Au==-(C*k*s+Du),h*Av==-Dv,h*(Au*du+Av*dv)+(C*k*s+Du)*du+Dv*dv!=0)
 add('pure_tree_dilaton_response','unsat',s>0,k*k==2,k>0,h==C*s,h*Au==-C*k*s,Au!=-k)
 l,r=z.Reals('lambda r')
 I,I2,snew,Vbase,Vnew=z.Reals('I I2 snew Vbase Vnew')
 add('scaling_family_distinct_intercepts','sat',I==3,I2==I,s>0,l>1,r==1,Vbase>0,Vnew==l*l*l*Vbase,snew==s*l*l*l*r,snew!=s)
 add('fixed_boundary_leaves_volume_family','sat',I==3,I2==I,s>0,l>1,r>0,Vbase>0,Vnew==l*l*l*Vbase,snew==s*l*l*l*r,snew==s,Vnew!=Vbase)
 add('same_coupling_distinct_volume_dilaton','sat',l>0,l!=1,r>0,l*l*l*r==1)
 add('fixed_Phi_volume_changes_coupling','unsat',l>0,l!=1,l*l*l==1)
 a2,m2,n2,y12,y22=z.Reals('a2 m2 n2 y12 y22')
 add('optical_identifies_matched_change','unsat',y1==z.RealVal('16/5')*a,y12==z.RealVal('16/5')*a2,y1==y12,a!=a2)
 add('nuclear_mass_fiber','sat',y1==z.RealVal('16/5')*a,y2==-6*a-m-n,y2==-6*a-m2-n2,m!=m2)
 add('independent_nuclear_prior_restores_mass','unsat',y2==-6*a-m-n,y2==-6*a-m2-n,m!=m2)
 add('gauge_blind_direction','unsat',a==Au*Av+Av*(-Au),a!=0)
 add('threshold_slope_can_cancel','sat',s>0,k>0,k*k==2,Du==-C*k*s,Du!=0)
 eps=z.Real('eps')
 add('free_optical_systematic_hides_change','sat',a!=a2,z.RealVal('16/5')*a==z.RealVal('16/5')*a2+eps)
 Bu,Bv,Nu,Nv=z.Reals('Bu Bv Nu Nv')
 p,q,p2,q2=z.Reals('p q p2 q2')
 det=Av*(Bu+Nu)-Au*(Bv+Nv)
 eq1=Au*p+Av*q==Au*p2+Av*q2
 eq2=(-6*Au-Bu-Nu)*p+(-6*Av-Bv-Nv)*q==(-6*Au-Bu-Nu)*p2+(-6*Av-Bv-Nv)*q2
 add('known_noncollinear_map_identifies_moduli','unsat',det!=0,eq1,eq2,z.Or(p!=p2,q!=q2))
 add('singular_map_negative_control','sat',Au==1,Av==0,Bu==0,Nu==0,Bv==0,Nv==0,eq1,eq2,q!=q2)
 add('tree_response_not_intercept','sat',s>0,D>0,s!=D,k*k==2,k>0,Au==-k)
 return out
out=[]
create='--create' in sys.argv
folder=P/'smt';folder.mkdir(exist_ok=True)
for name,expected,text in cases():
 f=folder/(name+'.smt2')
 if create and not f.exists():
  with f.open('x') as o:o.write(text)
 else: assert f.read_text()==text,name
 solver=z.Solver();solver.set(timeout=30000);solver.from_string(f.read_text());result=str(solver.check()); assert result==expected,(name,result)
 # SAT witness deliberately not compared across solver versions; satisfiability is replayed.
 out.append({'name':name,'expected':expected,'result':result,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
print(json.dumps({'passed':True,'z3_version':z.get_version_string(),'cases':out}))
