; benchmark generated from python API
(set-info :status unknown)
(declare-fun n () Int)
(declare-fun a () Real)
(assert
 (>= n 0))
(assert
 (> a 0.0))
(assert
 (= (* (* (* (- 2.0) a) a) (to_real (- 66 (* 8 n)))) 0.0))
(check-sat)
