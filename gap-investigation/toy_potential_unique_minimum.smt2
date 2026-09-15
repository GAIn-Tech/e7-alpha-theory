; benchmark generated from python API
(set-info :status unknown)
(declare-fun vacuum_location () Real)
(declare-fun vacuum_coordinate () Real)
(assert
 (and (distinct vacuum_coordinate vacuum_location) true))
(assert
 (let ((?x3864 (- vacuum_coordinate vacuum_location)))
(<= (* ?x3864 ?x3864) 0.0)))
(check-sat)
