; benchmark generated from python API
(set-info :status unknown)
(declare-fun a2 () Real)
(declare-fun a () Real)
(declare-fun eps () Real)
(assert
 (and (distinct a a2) true))
(assert
 (let ((?x59 (* (/ 16.0 5.0) a)))
(= ?x59 (+ (* (/ 16.0 5.0) a2) eps))))
(check-sat)
