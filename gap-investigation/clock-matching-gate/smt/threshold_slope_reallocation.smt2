; benchmark generated from python API
(set-info :status unknown)
(declare-fun eps () Real)
(declare-fun f1 () Real)
(declare-fun f1new () Real)
(declare-fun D1 () Real)
(declare-fun D1new () Real)
(assert
 (= f1new (+ f1 eps)))
(assert
 (= D1new (- D1 (* (/ 8.0 3.0) eps))))
(assert
 (let ((?x78 (+ (* (/ 8.0 3.0) f1) D1)))
(let ((?x42 (* (/ 8.0 3.0) f1new)))
(let ((?x27 (+ ?x42 D1new)))
(and (distinct ?x27 ?x78) true)))))
(check-sat)
