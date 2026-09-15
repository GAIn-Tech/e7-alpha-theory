; benchmark generated from python API
(set-info :status unknown)
(declare-fun transformed_functional () Real)
(declare-fun functional () Real)
(declare-fun c () Real)
(assert
 (= functional transformed_functional))
(assert
 (let ((?x1629 (* c functional)))
(and (distinct ?x1629 (* c transformed_functional)) true)))
(check-sat)
