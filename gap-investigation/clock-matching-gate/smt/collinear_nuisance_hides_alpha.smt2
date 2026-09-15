; benchmark generated from python API
(set-info :status unknown)
(declare-fun lam () Real)
(declare-fun anew () Real)
(declare-fun a () Real)
(declare-fun nnew () Real)
(declare-fun n () Real)
(assert
 (and (distinct lam 0.0) true))
(assert
 (and (distinct a anew) true))
(assert
 (= (+ a (* lam n)) (+ anew (* lam nnew))))
(check-sat)
