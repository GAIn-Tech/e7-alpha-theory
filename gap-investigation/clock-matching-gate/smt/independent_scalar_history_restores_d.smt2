; benchmark generated from python API
(set-info :status unknown)
(declare-fun du () Real)
(declare-fun q () Real)
(declare-fun d () Real)
(declare-fun b () Real)
(assert
 (and (distinct du 0.0) true))
(assert
 (= (* d du) q))
(assert
 (= (* b du) q))
(assert
 (and (distinct d b) true))
(check-sat)
