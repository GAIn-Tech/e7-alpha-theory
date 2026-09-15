; benchmark generated from python API
(set-info :status unknown)
(declare-fun c () Real)
(assert
 (> c 0.0))
(assert
 (or (<= (+ c 1.0) 0.0) (= (+ c 1.0) c)))
(check-sat)
