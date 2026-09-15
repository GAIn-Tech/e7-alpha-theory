; benchmark generated from python API
(set-info :status unknown)
(declare-fun H () Real)
(declare-fun D () Real)
(declare-fun f () Real)
(declare-fun fnew () Real)
(declare-fun D1 () Real)
(declare-fun f1 () Real)
(declare-fun d () Real)
(declare-fun f1new () Real)
(assert
 (> H 0.0))
(assert
 (= H (+ (* (/ 8.0 3.0) f) D)))
(assert
 (= H (+ (* (/ 8.0 3.0) fnew) D)))
(assert
 (let ((?x57 (* H d)))
 (= ?x57 (- (+ (* (/ 8.0 3.0) f1) D1)))))
(assert
 (let ((?x57 (* H d)))
 (= ?x57 (- (+ (* (/ 8.0 3.0) f1new) D1)))))
(assert
 (or (and (distinct f fnew) true) (and (distinct f1 f1new) true)))
(check-sat)
