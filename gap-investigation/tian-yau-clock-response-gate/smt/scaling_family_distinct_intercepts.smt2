; benchmark generated from python API
(set-info :status unknown)
(declare-fun I () Real)
(declare-fun I2 () Real)
(declare-fun s () Real)
(declare-fun lambda () Real)
(declare-fun r () Real)
(declare-fun Vbase () Real)
(declare-fun Vnew () Real)
(declare-fun snew () Real)
(assert
 (= I 3.0))
(assert
 (= I2 I))
(assert
 (> s 0.0))
(assert
 (> lambda 1.0))
(assert
 (= r 1.0))
(assert
 (> Vbase 0.0))
(assert
 (= Vnew (* (* (* lambda lambda) lambda) Vbase)))
(assert
 (= snew (* (* (* (* s lambda) lambda) lambda) r)))
(assert
 (and (distinct snew s) true))
(check-sat)
