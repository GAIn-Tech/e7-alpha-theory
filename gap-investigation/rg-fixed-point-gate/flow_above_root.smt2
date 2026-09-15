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
 (< ?x39 0.0)))))))
(assert
 (let ((?x38 (* (to_real (- 3672 (* 1062 n))) a)))
(let ((?x10 (* 8 n)))
(let ((?x12 (- 66 ?x10)))
(let ((?x34 (to_real ?x12)))
(let ((?x39 (+ ?x34 ?x38)))
(let ((?x33 (* (* (- 2.0) a) a)))
(let ((?x40 (* ?x33 ?x39)))
(<= ?x40 0.0)))))))))
(check-sat)
