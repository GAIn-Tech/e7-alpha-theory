; benchmark generated from python API
(set-info :status unknown)
(declare-fun lB () Real)
(declare-fun lA () Real)
(declare-fun yAB () Real)
(declare-fun lC () Real)
(declare-fun yBC () Real)
(declare-fun yCA () Real)
(assert
 (= yAB (- lA lB)))
(assert
 (= yBC (- lB lC)))
(assert
 (= yCA (- lC lA)))
(assert
 (and (distinct (+ (+ yAB yBC) yCA) 0.0) true))
(check-sat)
