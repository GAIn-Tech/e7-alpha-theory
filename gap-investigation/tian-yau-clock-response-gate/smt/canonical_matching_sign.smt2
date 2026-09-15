; benchmark generated from python API
(set-info :status unknown)
(declare-fun k () Real)
(declare-fun D () Real)
(declare-fun s () Real)
(declare-fun h () Real)
(declare-fun Du () Real)
(declare-fun Au () Real)
(declare-fun Dv () Real)
(declare-fun Av () Real)
(declare-fun dv () Real)
(declare-fun du () Real)
(assert
 (= (* k k) 2.0))
(assert
 (> k 0.0))
(assert
 (= h (+ (* (/ 8.0 3.0) s) D)))
(assert
 (> h 0.0))
(assert
 (= (* h Au) (- (+ (* (* (/ 8.0 3.0) k) s) Du))))
(assert
 (= (* h Av) (- Dv)))
(assert
 (let ((?x50 (+ (* h (+ (* Au du) (* Av dv))) (* (+ (* (* (/ 8.0 3.0) k) s) Du) du))))
(and (distinct (+ ?x50 (* Dv dv)) 0.0) true)))
(check-sat)
