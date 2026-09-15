; benchmark generated from python API
(set-info :status unknown)
(declare-fun s () Real)
(declare-fun D () Real)
(declare-fun k () Real)
(declare-fun Au () Real)
(assert
 (> s 0.0))
(assert
 (> D 0.0))
(assert
 (and (distinct s D) true))
(assert
 (= (* k k) 2.0))
(assert
 (> k 0.0))
(assert
 (= Au (- k)))
(check-sat)
