; benchmark generated from python API
(set-info :status unknown)
(declare-fun amp () Real)
(declare-fun ampnew () Real)
(declare-fun bnew () Real)
(declare-fun b () Real)
(declare-fun q () Real)
(assert
 (> amp 0.0))
(assert
 (> ampnew 0.0))
(assert
 (and (distinct b bnew) true))
(assert
 (and (distinct amp ampnew) true))
(assert
 (= q (* b amp)))
(assert
 (let ((?x114 (* bnew ampnew)))
 (= q ?x114)))
(assert
 (and (distinct q 0.0) true))
(check-sat)
