; benchmark generated from python API
(set-info :status unknown)
(declare-fun eps () Real)
(declare-fun f () Real)
(declare-fun fnew () Real)
(declare-fun D () Real)
(declare-fun Dnew () Real)
(assert
 (= fnew (+ f eps)))
(assert
 (= Dnew (- D (* (/ 8.0 3.0) eps))))
(assert
 (let ((?x84 (* (/ 8.0 3.0) f)))
(let ((?x31 (+ ?x84 D)))
(let ((?x17 (+ (* (/ 8.0 3.0) fnew) Dnew)))
(and (distinct ?x17 ?x31) true)))))
(check-sat)
