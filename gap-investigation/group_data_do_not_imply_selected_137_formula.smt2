; benchmark generated from python API
(set-info :status unknown)
(declare-fun x1 () Real)
(declare-fun x2 () Real)
(declare-fun embedding_index () Real)
(declare-fun common_running_threshold () Real)
(declare-fun y1 () Real)
(declare-fun y2 () Real)
(assert
 (> x1 0.0))
(assert
 (> x2 0.0))
(assert
 (> embedding_index 0.0))
(assert
 (= y1 (+ (* embedding_index x1) common_running_threshold)))
(assert
 (= y2 (+ (* embedding_index x2) common_running_threshold)))
(assert
 (> y1 0.0))
(assert
 (> y2 0.0))
(assert
 (= embedding_index 1.0))
(assert
 (= common_running_threshold 0.0))
(assert
 (and (distinct y1 137.0) true))
(check-sat)
