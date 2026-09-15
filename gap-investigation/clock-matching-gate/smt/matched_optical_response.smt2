; benchmark generated from python API
(set-info :status unknown)
(declare-fun H () Real)
(declare-fun D1 () Real)
(declare-fun f1 () Real)
(declare-fun d () Real)
(declare-fun du () Real)
(declare-fun dalpha () Real)
(declare-fun s () Real)
(declare-fun y () Real)
(assert
 (> H 0.0))
(assert
 (let ((?x40 (* H d)))
 (= ?x40 (- (+ (* (/ 8.0 3.0) f1) D1)))))
(assert
 (= dalpha (* d du)))
(assert
 (let ((?x34 (* s dalpha)))
 (= y ?x34)))
(assert
 (and (distinct (+ (* H y) (* (* s (+ (* (/ 8.0 3.0) f1) D1)) du)) 0.0) true))
(check-sat)
