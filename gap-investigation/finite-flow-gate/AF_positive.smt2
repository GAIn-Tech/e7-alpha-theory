; benchmark generated from python API
(set-info :status unknown)
(declare-fun x () Real)
(assert
 (> x 0.0))
(assert
 (< x 1.0))
(assert
 (let ((?x22 (- 1.0 x)))
(let ((?x20 (* x x)))
(let ((?x23 (* ?x20 ?x22)))
(<= ?x23 0.0)))))
(check-sat)
