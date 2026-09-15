; benchmark generated from python API
(set-info :status unknown)
(declare-fun anew () Real)
(declare-fun a () Real)
(declare-fun s1 () Real)
(declare-fun s2 () Real)
(declare-fun s3 () Real)
(declare-fun N1 () Real)
(declare-fun N2 () Real)
(declare-fun N3 () Real)
(assert
 (and (distinct a anew) true))
(assert
 (= s1 1.0))
(assert
 (= s2 2.0))
(assert
 (= s3 3.0))
(assert
 (let ((?x68 (* s1 a)))
 (= ?x68 (+ (* s1 anew) N1))))
(assert
 (let ((?x153 (* s2 a)))
 (= ?x153 (+ (* s2 anew) N2))))
(assert
 (= (* s3 a) (+ (* s3 anew) N3)))
(check-sat)
