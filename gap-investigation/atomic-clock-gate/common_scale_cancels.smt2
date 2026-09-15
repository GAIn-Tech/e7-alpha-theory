; benchmark generated from python API
(set-info :status unknown)
(declare-fun g () Real)
(declare-fun m () Real)
(declare-fun a () Real)
(declare-fun r () Real)
(assert
 (let ((?x22 (- (- (* (- 6.0) a) m) g)))
(and (distinct (- (+ r (* (- (/ 16.0 5.0)) a)) (+ (+ (+ r (* (/ 14.0 5.0) a)) m) g)) ?x22) true)))
(check-sat)
