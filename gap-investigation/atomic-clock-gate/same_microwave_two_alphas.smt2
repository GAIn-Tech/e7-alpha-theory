; benchmark generated from python API
(set-info :status unknown)
(declare-fun gg () Real)
(declare-fun mm () Real)
(declare-fun aa () Real)
(declare-fun g () Real)
(declare-fun m () Real)
(declare-fun a () Real)
(assert
 (let ((?x22 (- (- (* (- 6.0) a) m) g)))
 (= ?x22 (- (- (* (- 6.0) aa) mm) gg))))
(assert
 (and (distinct a aa) true))
(check-sat)
