; benchmark generated from python API
(set-info :status unknown)
(declare-fun dv () Real)
(declare-fun Av () Real)
(declare-fun du () Real)
(declare-fun Au () Real)
(declare-fun a () Real)
(declare-fun y1 () Real)
(declare-fun n () Real)
(declare-fun m () Real)
(declare-fun y2 () Real)
(assert
 (let ((?x16 (* Av dv)))
 (let ((?x15 (* Au du)))
 (let ((?x17 (+ ?x15 ?x16)))
 (= a ?x17)))))
(assert
 (let ((?x20 (* (/ 16.0 5.0) a)))
 (= y1 ?x20)))
(assert
 (= y2 (- (- (* (- 6.0) a) m) n)))
(assert
 (let ((?x28 (* 5.0 y1)))
(and (distinct ?x28 (* 16.0 (+ (* Au du) (* Av dv)))) true)))
(check-sat)
