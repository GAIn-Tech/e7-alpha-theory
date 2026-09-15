; benchmark generated from python API
(set-info :status unknown)
(declare-fun n () Int)
(declare-fun a () Real)
(assert
 (>= n 4))
(assert
 (<= n 8))
(assert
 (> a 0.0))
(assert
 (let ((?x38 (* (to_real (- 3672 (* 1062 n))) a)))
 (let ((?x10 (* 8 n)))
 (let ((?x12 (- 66 ?x10)))
 (let ((?x34 (to_real ?x12)))
 (let ((?x39 (+ ?x34 ?x38)))
 (= ?x39 0.0)))))))
(assert
 (let ((?x54 (- (* (to_real (* (- 4) (- 66 (* 8 n)))) a) (* (* (to_real (* 6 (- 3672 (* 1062 n)))) a) a))))
(<= ?x54 0.0)))
(check-sat)
