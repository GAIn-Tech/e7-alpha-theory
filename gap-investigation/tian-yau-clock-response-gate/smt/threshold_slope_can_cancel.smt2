; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Real)
(declare-fun k () Real)
(declare-fun Du () Real)
(assert
 (> s 0.0))
(assert
 (> k 0.0))
(assert
 (= (* k k) 2.0))
(assert
 (= Du (* (* (- (/ 8.0 3.0)) k) s)))
(assert
 (and (distinct Du 0.0) true))
(check-sat)
