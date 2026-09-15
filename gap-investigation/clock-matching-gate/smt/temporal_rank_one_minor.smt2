; benchmark generated from python API
(set-info :status unknown)
(declare-fun a () Real)
(declare-fun s1 () Real)
(declare-fun y1 () Real)
(declare-fun s2 () Real)
(declare-fun y2 () Real)
(declare-fun at () Real)
(declare-fun y1t () Real)
(declare-fun y2t () Real)
(assert
 (let ((?x17 (* s1 a)))
 (= y1 ?x17)))
(assert
 (let ((?x19 (* s2 a)))
 (= y2 ?x19)))
(assert
 (= y1t (* s1 at)))
(assert
 (let ((?x116 (* s2 at)))
 (= y2t ?x116)))
(assert
 (and (distinct (- (* y1 y2t) (* y2 y1t)) 0.0) true))
(check-sat)
