; benchmark generated from python API
(set-info :status unknown)
(declare-fun y () Real)
(declare-fun x () Real)
(assert
 (let ((?x84 (+ (* (- 4.0) (+ x y)) (* 9648.0 (+ (+ (* x x) (* x y)) (* y y))))))
(let ((?x72 (+ (* (* (* (- 2.0) x) x) (- 2.0 (* 4824.0 x))) (* (* (* 2.0 y) y) (- 2.0 (* 4824.0 y))))))
(and (distinct ?x72 (* (- x y) ?x84)) true))))
(check-sat)
