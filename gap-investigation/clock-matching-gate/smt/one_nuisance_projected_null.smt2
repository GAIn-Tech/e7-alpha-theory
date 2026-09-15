; benchmark generated from python API
(set-info :status unknown)
(declare-fun n () Real)
(declare-fun p1 () Real)
(declare-fun a () Real)
(declare-fun s1 () Real)
(declare-fun y1 () Real)
(declare-fun p2 () Real)
(declare-fun s2 () Real)
(declare-fun y2 () Real)
(declare-fun p3 () Real)
(declare-fun s3 () Real)
(declare-fun y3 () Real)
(assert
 (= y1 (+ (* s1 a) (* p1 n))))
(assert
 (= y2 (+ (* s2 a) (* p2 n))))
(assert
 (= y3 (+ (* s3 a) (* p3 n))))
(assert
 (let ((?x92 (+ (* (- (* s2 p3) (* s3 p2)) y1) (* (- (* s3 p1) (* s1 p3)) y2))))
(and (distinct (+ ?x92 (* (- (* s1 p2) (* s2 p1)) y3)) 0.0) true)))
(check-sat)
