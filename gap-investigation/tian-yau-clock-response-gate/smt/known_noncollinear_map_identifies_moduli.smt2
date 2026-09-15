; benchmark generated from python API
(set-info :status unknown)
(declare-fun Nv () Real)
(declare-fun Bv () Real)
(declare-fun Au () Real)
(declare-fun Nu () Real)
(declare-fun Bu () Real)
(declare-fun Av () Real)
(declare-fun q2 () Real)
(declare-fun p2 () Real)
(declare-fun q () Real)
(declare-fun p () Real)
(assert
 (let ((?x49 (- (* Av (+ Bu Nu)) (* Au (+ Bv Nv)))))
 (and (distinct ?x49 0.0) true)))
(assert
 (= (+ (* Au p) (* Av q)) (+ (* Au p2) (* Av q2))))
(assert
 (let ((?x107 (+ (* (- (- (* (- 6.0) Au) Bu) Nu) p2) (* (- (- (* (- 6.0) Av) Bv) Nv) q2))))
 (let ((?x62 (+ (* (- (- (* (- 6.0) Au) Bu) Nu) p) (* (- (- (* (- 6.0) Av) Bv) Nv) q))))
 (= ?x62 ?x107))))
(assert
 (or (and (distinct p p2) true) (and (distinct q q2) true)))
(check-sat)
