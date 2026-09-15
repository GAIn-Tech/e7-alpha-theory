; benchmark generated from python API
(set-info :status unknown)
(declare-fun p1 () Real)
(declare-fun s2 () Real)
(declare-fun p2 () Real)
(declare-fun s1 () Real)
(declare-fun nnew () Real)
(declare-fun anew () Real)
(declare-fun n () Real)
(declare-fun a () Real)
(assert
 (and (distinct (- (* s1 p2) (* s2 p1)) 0.0) true))
(assert
 (= (+ (* s1 a) (* p1 n)) (+ (* s1 anew) (* p1 nnew))))
(assert
 (= (+ (* s2 a) (* p2 n)) (+ (* s2 anew) (* p2 nnew))))
(assert
 (or (and (distinct a anew) true) (and (distinct n nnew) true)))
(check-sat)
