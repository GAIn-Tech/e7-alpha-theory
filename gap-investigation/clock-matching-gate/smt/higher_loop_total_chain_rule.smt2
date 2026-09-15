; benchmark generated from python API
(set-info :status unknown)
(declare-fun partial_u () Real)
(declare-fun f1 () Real)
(declare-fun partial_f () Real)
(declare-fun total () Real)
(declare-fun H1 () Real)
(assert
 (= total (+ (* partial_f f1) partial_u)))
(assert
 (= H1 (+ (* (/ 8.0 3.0) f1) total)))
(assert
 (and (distinct H1 (+ (* (+ (/ 8.0 3.0) partial_f) f1) partial_u)) true))
(check-sat)
