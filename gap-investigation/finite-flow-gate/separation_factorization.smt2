; benchmark generated from python API
(set-info :status unknown)
(declare-fun y () Real)
(declare-fun x () Real)
(assert
 (let ((?x68 (* (- x y) (- (- (- (+ x y) (* x x)) (* x y)) (* y y)))))
(and (distinct (- (* (* x x) (- 1.0 x)) (* (* y y) (- 1.0 y))) ?x68) true)))
(check-sat)
