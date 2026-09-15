; benchmark generated from python API
(set-info :status unknown)
(declare-fun f () Real)
(declare-fun fnew () Real)
(declare-fun f1 () Real)
(declare-fun d () Real)
(declare-fun f1new () Real)
(assert
 (> f 0.0))
(assert
 (> fnew 0.0))
(assert
 (and (distinct f fnew) true))
(assert
 (= (* d f) (- f1)))
(assert
 (= (* d fnew) (- f1new)))
(assert
 (and (distinct d 0.0) true))
(check-sat)
