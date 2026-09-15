; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Real)
(declare-fun k () Real)
(declare-fun h () Real)
(declare-fun Au () Real)
(assert
 (> s 0.0))
(assert
 (= (* k k) 2.0))
(assert
 (> k 0.0))
(assert
 (= h (* (/ 8.0 3.0) s)))
(assert
 (= (* h Au) (* (* (- (/ 8.0 3.0)) k) s)))
(assert
 (and (distinct Au (- k)) true))
(check-sat)
