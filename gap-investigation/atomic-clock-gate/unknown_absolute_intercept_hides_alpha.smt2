; benchmark generated from python API
(set-info :status unknown)
(declare-fun aa () Real)
(declare-fun bb () Real)
(declare-fun a () Real)
(declare-fun b () Real)
(assert
 (= (+ b (* (/ 16.0 5.0) a)) (+ bb (* (/ 16.0 5.0) aa))))
(assert
 (and (distinct a aa) true))
(check-sat)
