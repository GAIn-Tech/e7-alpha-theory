; benchmark generated from python API
(set-info :status unknown)
(declare-fun n () Int)
(assert
 (>= n 0))
(assert
 (let ((?x10 (* 8 n)))
 (let ((?x12 (- 66 ?x10)))
 (< ?x12 0))))
(assert
 (let ((?x14 (* 1062 n)))
(let ((?x16 (- 3672 ?x14)))
(> ?x16 0))))
(check-sat)
