; benchmark generated from python API
(set-info :status unknown)
(declare-fun f () Real)
(declare-fun fnew () Real)
(declare-fun H () Real)
(declare-fun D () Real)
(declare-fun Dnew () Real)
(declare-fun D1 () Real)
(declare-fun f1 () Real)
(declare-fun d () Real)
(declare-fun D1new () Real)
(declare-fun f1new () Real)
(assert
 (> f 0.0))
(assert
 (> fnew 0.0))
(assert
 (and (distinct f fnew) true))
(assert
 (> H 0.0))
(assert
 (= H (+ (* (/ 8.0 3.0) f) D)))
(assert
 (= H (+ (* (/ 8.0 3.0) fnew) Dnew)))
(assert
 (let ((?x57 (* H d)))
 (= ?x57 (- (+ (* (/ 8.0 3.0) f1) D1)))))
(assert
 (let ((?x57 (* H d)))
 (= ?x57 (- (+ (* (/ 8.0 3.0) f1new) D1new)))))
(assert
 (and (distinct f1 f1new) true))
(check-sat)
