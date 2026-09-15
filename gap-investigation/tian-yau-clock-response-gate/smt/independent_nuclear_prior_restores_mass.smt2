; benchmark generated from python API
(set-info :status unknown)
(declare-fun n () Real)
(declare-fun m () Real)
(declare-fun a () Real)
(declare-fun y2 () Real)
(declare-fun m2 () Real)
(assert
 (= y2 (- (- (* (- 6.0) a) m) n)))
(assert
 (= y2 (- (- (* (- 6.0) a) m2) n)))
(assert
 (and (distinct m m2) true))
(check-sat)
