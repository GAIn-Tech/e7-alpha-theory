; benchmark generated from python API
(set-info :status unknown)
(declare-fun x () Real)
(declare-fun u () Real)
(assert
 (= u (/ x 2412.0)))
(assert
 (let ((?x19 (* 2412.0 (- (* (* 4.0 u) u) (* (* (* 9648.0 u) u) u)))))
(and (distinct ?x19 (/ (* (* x x) (- 1.0 x)) 603.0)) true)))
(check-sat)
