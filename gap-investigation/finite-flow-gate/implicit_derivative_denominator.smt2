; benchmark generated from python API
(set-info :status unknown)
(declare-fun x () Real)
(assert
 (> x 0.0))
(assert
 (< x 1.0))
(assert
 (let ((?x20 (* x x)))
(let ((?x33 (/ 1.0 ?x20)))
(let ((?x22 (- 1.0 x)))
(let ((?x23 (* ?x20 ?x22)))
(and (distinct (* ?x23 (+ (+ (/ 1.0 x) (/ 1.0 ?x22)) ?x33)) 1.0) true))))))
(check-sat)
