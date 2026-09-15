; benchmark generated from python API
(set-info :status unknown)
(declare-fun d () Real)
(declare-fun k () Real)
(declare-fun a () Real)
(declare-fun h () Real)
(declare-fun aa () Real)
(assert
 (= a (* k d)))
(assert
 (= aa (* (* h 2.0) d)))
(assert
 (let ((?x64 (* 2.0 h)))
 (= k ?x64)))
(assert
 (and (distinct d 0.0) true))
(assert
 (and (distinct h 0.0) true))
(assert
 (= a aa))
(assert
 (and (distinct k h) true))
(check-sat)
