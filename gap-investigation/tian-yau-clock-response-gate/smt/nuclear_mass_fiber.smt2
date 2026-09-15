; benchmark generated from python API
(set-info :status unknown)
(declare-fun a () Real)
(declare-fun y1 () Real)
(declare-fun n () Real)
(declare-fun m () Real)
(declare-fun y2 () Real)
(declare-fun n2 () Real)
(declare-fun m2 () Real)
(assert
 (let ((?x55 (* (/ 16.0 5.0) a)))
 (= y1 ?x55)))
(assert
 (= y2 (- (- (* (- 6.0) a) m) n)))
(assert
 (= y2 (- (- (* (- 6.0) a) m2) n2)))
(assert
 (and (distinct m m2) true))
(check-sat)
