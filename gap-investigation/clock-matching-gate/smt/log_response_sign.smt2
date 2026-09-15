; benchmark generated from python API
(set-info :status unknown)
(declare-fun H () Real)
(declare-fun D1 () Real)
(declare-fun f1 () Real)
(declare-fun H1 () Real)
(declare-fun d () Real)
(assert
 (> H 0.0))
(assert
 (= H1 (+ (* (/ 8.0 3.0) f1) D1)))
(assert
 (let ((?x40 (* H d)))
 (= ?x40 (- H1))))
(assert
 (and (distinct (+ (+ (* H d) (* (/ 8.0 3.0) f1)) D1) 0.0) true))
(check-sat)
