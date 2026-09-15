; benchmark generated from python API
(set-info :status unknown)
(declare-fun n () Real)
(declare-fun a () Real)
(declare-fun y1 () Real)
(declare-fun y2 () Real)
(declare-fun y3 () Real)
(assert
 (and (distinct n 0.0) true))
(assert
 (= y1 a))
(assert
 (= y2 (+ (* 2.0 a) n)))
(assert
 (= y3 (+ (* 3.0 a) n)))
(assert
 (and (distinct (- (* 2.0 y1) y2) 0.0) true))
(check-sat)
