; benchmark generated from python API
(set-info :status unknown)
(declare-fun a () Real)
(declare-fun y1 () Real)
(declare-fun a2 () Real)
(declare-fun y12 () Real)
(assert
 (let ((?x55 (* (/ 16.0 5.0) a)))
 (= y1 ?x55)))
(assert
 (let ((?x70 (* (/ 16.0 5.0) a2)))
 (= y12 ?x70)))
(assert
 (= y1 y12))
(assert
 (and (distinct a a2) true))
(check-sat)
