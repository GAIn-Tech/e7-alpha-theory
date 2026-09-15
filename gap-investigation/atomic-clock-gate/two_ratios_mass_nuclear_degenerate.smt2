; benchmark generated from python API
(set-info :status unknown)
(declare-fun aa () Real)
(declare-fun a () Real)
(declare-fun gg () Real)
(declare-fun mm () Real)
(declare-fun g () Real)
(declare-fun m () Real)
(assert
 (let ((?x36 (* (/ 16.0 5.0) aa)))
 (let ((?x18 (* (/ 16.0 5.0) a)))
 (= ?x18 ?x36))))
(assert
 (let ((?x22 (- (- (* (- 6.0) a) m) g)))
 (= ?x22 (- (- (* (- 6.0) aa) mm) gg))))
(assert
 (and (distinct m mm) true))
(check-sat)
