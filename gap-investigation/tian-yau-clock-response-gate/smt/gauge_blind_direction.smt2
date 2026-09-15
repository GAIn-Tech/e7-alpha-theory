; benchmark generated from python API
(set-info :status unknown)
(declare-fun Au () Real)
(declare-fun Av () Real)
(declare-fun a () Real)
(assert
 (= a (+ (* Au Av) (* Av (- Au)))))
(assert
 (and (distinct a 0.0) true))
(check-sat)
