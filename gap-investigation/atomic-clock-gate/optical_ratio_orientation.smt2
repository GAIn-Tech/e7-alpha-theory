; benchmark generated from python API
(set-info :status unknown)
(declare-fun a () Real)
(assert
 (let ((?x18 (* (/ 16.0 5.0) a)))
(and (distinct (- (* 0.0 a) (* (- (/ 16.0 5.0)) a)) ?x18) true)))
(check-sat)
