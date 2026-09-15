; benchmark generated from python API
(set-info :status unknown)
(declare-fun a () Real)
(declare-fun y () Real)
(declare-fun x () Real)
(assert
 (> a 0.0))
(assert
 (and (distinct x y) true))
(assert
 (let ((?x89 (* a y)))
(let ((?x88 (* a x)))
(= ?x88 ?x89))))
(check-sat)
