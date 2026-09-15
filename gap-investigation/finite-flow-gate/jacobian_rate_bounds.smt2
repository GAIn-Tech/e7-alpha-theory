; benchmark generated from python API
(set-info :status unknown)
(declare-fun x () Real)
(assert
 (> x 0.0))
(assert
 (< x 1.0))
(assert
 (or (< (- (* 2.0 x) (* (* 3.0 x) x)) (- 1.0)) (< (/ 1.0 3.0) (- (* 2.0 x) (* (* 3.0 x) x)))))
(check-sat)
