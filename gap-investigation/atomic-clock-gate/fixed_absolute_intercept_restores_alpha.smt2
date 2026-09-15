; benchmark generated from python API
(set-info :status unknown)
(declare-fun bb () Real)
(declare-fun b () Real)
(declare-fun aa () Real)
(declare-fun a () Real)
(assert
 (= b bb))
(assert
 (= (+ b (* (/ 16.0 5.0) a)) (+ bb (* (/ 16.0 5.0) aa))))
(assert
 (and (distinct a aa) true))
(check-sat)
