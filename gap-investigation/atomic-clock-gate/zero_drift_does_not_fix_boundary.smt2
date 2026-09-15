; benchmark generated from python API
(set-info :status unknown)
(declare-fun d () Real)
(declare-fun b () Real)
(declare-fun bb () Real)
(assert
 (= d 0.0))
(assert
 (> b 0.0))
(assert
 (> bb 0.0))
(assert
 (and (distinct b bb) true))
(check-sat)
