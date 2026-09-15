; benchmark generated from python API
(set-info :status unknown)
(declare-fun k () Real)
(declare-fun aa () Real)
(declare-fun a () Real)
(assert
 (and (distinct k 0.0) true))
(assert
 (= (* k a) (* k aa)))
(assert
 (and (distinct a aa) true))
(check-sat)
