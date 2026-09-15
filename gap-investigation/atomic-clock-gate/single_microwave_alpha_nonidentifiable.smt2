; benchmark generated from python API
(set-info :status unknown)
(declare-fun g () Real)
(declare-fun m () Real)
(declare-fun a () Real)
(assert
 (let ((?x22 (- (- (* (- 6.0) a) m) g)))
 (= ?x22 0.0)))
(assert
 (and (distinct a 0.0) true))
(check-sat)
