; benchmark generated from python API
(set-info :status unknown)
(declare-fun ell () Real)
(declare-fun bL () Real)
(declare-fun bH () Real)
(declare-fun T1 () Real)
(assert
 (= T1 (* (- bH bL) ell)))
(assert
 (and (distinct (+ (* (- bL bH) ell) T1) 0.0) true))
(check-sat)
