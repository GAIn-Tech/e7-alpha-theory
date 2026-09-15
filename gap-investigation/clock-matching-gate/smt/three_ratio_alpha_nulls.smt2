; benchmark generated from python API
(set-info :status unknown)
(declare-fun a () Real)
(declare-fun s1 () Real)
(declare-fun y1 () Real)
(declare-fun s2 () Real)
(declare-fun y2 () Real)
(declare-fun s3 () Real)
(declare-fun y3 () Real)
(assert
 (let ((?x17 (* s1 a)))
 (= y1 ?x17)))
(assert
 (let ((?x19 (* s2 a)))
 (= y2 ?x19)))
(assert
 (= y3 (* s3 a)))
(assert
 (or (and (distinct (- (* s2 y1) (* s1 y2)) 0.0) true) (and (distinct (- (* s3 y1) (* s1 y3)) 0.0) true) (and (distinct (- (* s3 y2) (* s2 y3)) 0.0) true)))
(check-sat)
