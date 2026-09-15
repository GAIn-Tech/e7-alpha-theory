; benchmark generated from python API
(set-info :status unknown)
(declare-fun Au () Real)
(declare-fun Av () Real)
(declare-fun Bu () Real)
(declare-fun Nu () Real)
(declare-fun Bv () Real)
(declare-fun Nv () Real)
(declare-fun q2 () Real)
(declare-fun p2 () Real)
(declare-fun q () Real)
(declare-fun p () Real)
(assert
 (= Au 1.0))
(assert
 (= Av 0.0))
(assert
 (= Bu 0.0))
(assert
 (= Nu 0.0))
(assert
 (= Bv 0.0))
(assert
 (= Nv 0.0))
(assert
 (= (+ (* Au p) (* Av q)) (+ (* Au p2) (* Av q2))))
(assert
 (let ((?x107 (+ (* (- (- (* (- 6.0) Au) Bu) Nu) p2) (* (- (- (* (- 6.0) Av) Bv) Nv) q2))))
 (let ((?x62 (+ (* (- (- (* (- 6.0) Au) Bu) Nu) p) (* (- (- (* (- 6.0) Av) Bv) Nv) q))))
 (= ?x62 ?x107))))
(assert
 (and (distinct q q2) true))
(check-sat)
