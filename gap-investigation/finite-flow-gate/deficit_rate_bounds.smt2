; benchmark generated from python API
(set-info :status unknown)
(declare-fun y () Real)
(declare-fun x () Real)
(assert
 (> y 0.0))
(assert
 (<= y x))
(assert
 (< x 1.0))
(assert
 (or (< (* x x) (* y y)) (> (* x x) 1.0)))
(check-sat)
