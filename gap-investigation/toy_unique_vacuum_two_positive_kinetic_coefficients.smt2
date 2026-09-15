; benchmark generated from python API
(set-info :status unknown)
(declare-fun vacuum_location () Real)
(declare-fun vacuum_coordinate () Real)
(declare-fun c () Real)
(declare-fun k () Real)
(assert
 (= vacuum_coordinate vacuum_location))
(assert
 (> c 0.0))
(assert
 (> k 0.0))
(assert
 (and (distinct c k) true))
(check-sat)
