; benchmark generated from python API
(set-info :status unknown)
(declare-fun T56 () Real)
(declare-fun C56 () Real)
(assert
 (let ((?x1635 (* 133.0 T56)))
 (= (* 56.0 C56) ?x1635)))
(assert
 (= (/ 57.0 4.0) C56))
(assert
 (and (distinct T56 6.0) true))
(check-sat)
