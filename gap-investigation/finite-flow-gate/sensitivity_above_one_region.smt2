; benchmark generated from python API
(set-info :status unknown)
(declare-fun y () Real)
(declare-fun x () Real)
(assert
 (> y 0.0))
(assert
 (< y x))
(assert
 (>= (/ 2.0 3.0) x))
(assert
 (let ((?x40 (* y y)))
(let ((?x59 (* ?x40 (- 1.0 y))))
(let ((?x22 (- 1.0 x)))
(let ((?x20 (* x x)))
(let ((?x23 (* ?x20 ?x22)))
(<= ?x23 ?x59)))))))
(check-sat)
