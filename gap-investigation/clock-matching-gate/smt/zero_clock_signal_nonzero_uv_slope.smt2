; benchmark generated from python API
(set-info :status unknown)
(declare-fun H () Real)
(declare-fun f () Real)
(declare-fun f1 () Real)
(declare-fun D1 () Real)
(declare-fun d () Real)
(assert
 (> H 0.0))
(assert
 (> f 0.0))
(assert
 (and (distinct f1 0.0) true))
(assert
 (let ((?x57 (* H d)))
 (= ?x57 (- (+ (* (/ 8.0 3.0) f1) D1)))))
(assert
 (= d 0.0))
(check-sat)
