; benchmark generated from python API
(set-info :status unknown)
(declare-fun f () Real)
(declare-fun fy () Real)
(declare-fun f2 () Real)
(declare-fun D () Real)
(declare-fun H () Real)
(assert
 (> f 0.0))
(assert
 (let ((?x14 (* (/ 5.0 3.0) f)))
 (= fy ?x14)))
(assert
 (= f2 f))
(assert
 (= H (+ (+ fy f2) D)))
(assert
 (let ((?x20 (* (/ 8.0 3.0) f)))
(let ((?x21 (+ ?x20 D)))
(and (distinct H ?x21) true))))
(check-sat)
