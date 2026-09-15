; benchmark generated from python API
(set-info :status unknown)
(declare-fun n () Int)
(assert
 (>= n 0))
(assert
 (let (($x24 (<= n 8)))
(let (($x23 (>= n 4)))
(let (($x25 (and $x23 $x24)))
(let (($x21 (and (> (- 66 (* 8 n)) 0) (< (- 3672 (* 1062 n)) 0))))
(xor $x21 $x25))))))
(check-sat)
