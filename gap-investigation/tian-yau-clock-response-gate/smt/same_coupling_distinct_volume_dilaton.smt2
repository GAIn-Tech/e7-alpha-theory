; benchmark generated from python API
(set-info :status unknown)
(declare-fun lambda () Real)
(declare-fun r () Real)
(assert
 (> lambda 0.0))
(assert
 (and (distinct lambda 1.0) true))
(assert
 (> r 0.0))
(assert
 (= (* (* (* lambda lambda) lambda) r) 1.0))
(check-sat)
