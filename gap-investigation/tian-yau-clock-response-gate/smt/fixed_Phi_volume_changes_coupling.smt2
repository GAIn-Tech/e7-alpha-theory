; benchmark generated from python API
(set-info :status unknown)
(declare-fun lambda () Real)
(assert
 (> lambda 0.0))
(assert
 (and (distinct lambda 1.0) true))
(assert
 (= (* (* lambda lambda) lambda) 1.0))
(check-sat)
