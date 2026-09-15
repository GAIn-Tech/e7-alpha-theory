; benchmark generated from python API
(set-info :status unknown)
(declare-fun a () Real)
(assert
 (> a 0.0))
(assert
 (and (distinct (* 18.0 a) (* (* 2.0 18.0) (/ a 2.0))) true))
(check-sat)
