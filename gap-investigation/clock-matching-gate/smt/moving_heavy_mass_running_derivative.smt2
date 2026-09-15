; benchmark generated from python API
(set-info :status unknown)
(declare-fun rho () Real)
(declare-fun bL () Real)
(declare-fun bH () Real)
(declare-fun R1 () Real)
(assert
 (= R1 (+ (* bH (- rho)) (* bL rho))))
(assert
 (and (distinct R1 (* (- bL bH) rho)) true))
(check-sat)
