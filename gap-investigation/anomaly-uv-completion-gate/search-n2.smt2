; benchmark generated from python API
(set-info :status unknown)
(declare-fun b0 () Int)
(declare-fun b1 () Int)
(declare-fun b2 () Int)
(declare-fun b3 () Int)
(declare-fun b4 () Int)
(declare-fun b5 () Int)
(declare-fun b6 () Int)
(declare-fun b7 () Int)
(declare-fun b8 () Int)
(declare-fun b9 () Int)
(declare-fun b10 () Int)
(declare-fun b11 () Int)
(declare-fun b12 () Int)
(declare-fun b13 () Int)
(declare-fun b14 () Int)
(declare-fun b15 () Int)
(declare-fun b16 () Int)
(assert
 (>= b0 0))
(assert
 (<= b0 6))
(assert
 (>= b1 0))
(assert
 (<= b1 6))
(assert
 (>= b2 0))
(assert
 (<= b2 6))
(assert
 (>= b3 0))
(assert
 (<= b3 6))
(assert
 (>= b4 0))
(assert
 (<= b4 6))
(assert
 (>= b5 0))
(assert
 (<= b5 6))
(assert
 (>= b6 0))
(assert
 (<= b6 6))
(assert
 (>= b7 0))
(assert
 (<= b7 6))
(assert
 (>= b8 0))
(assert
 (<= b8 6))
(assert
 (>= b9 0))
(assert
 (<= b9 6))
(assert
 (>= b10 0))
(assert
 (<= b10 6))
(assert
 (>= b11 0))
(assert
 (<= b11 6))
(assert
 (>= b12 0))
(assert
 (<= b12 6))
(assert
 (>= b13 0))
(assert
 (<= b13 6))
(assert
 (>= b14 0))
(assert
 (<= b14 6))
(assert
 (>= b15 0))
(assert
 (<= b15 6))
(assert
 (>= b16 0))
(assert
 (<= b16 6))
(assert
 (let ((?x148 (+ (+ (+ (+ (+ (+ (+ 0 b2) b3) b7) b8) b9) b12) b13)))
 (<= (+ (+ (+ ?x148 b14) b15) b16) 2)))
(assert
 (let ((?x161 (+ (+ (+ (+ (+ (+ (+ 0 b0) b1) b4) b5) b6) b10) b11)))
 (<= ?x161 6)))
(assert
 (let ((?x224 (* b15 0)))
 (let ((?x132 (* b13 0)))
 (let ((?x124 (* b10 0)))
 (let ((?x119 (* b8 0)))
 (let ((?x111 (* b5 0)))
 (let ((?x105 (* b3 0)))
 (let ((?x107 (+ (+ (+ (+ 0 (* b0 0)) (* b1 0)) (* b2 (- 3))) ?x105)))
 (let ((?x117 (+ (+ (+ (+ ?x107 (* b4 0)) ?x111) (* b6 0)) (* b7 (- 3)))))
 (let ((?x130 (+ (+ (+ (+ (+ ?x117 ?x119) (* b9 3)) ?x124) (* b11 0)) (* b12 (- 3)))))
 (let ((?x91 (+ (+ (+ (+ ?x130 ?x132) (* b14 3)) ?x224) (* b16 3))))
 (= ?x91 (- 2)))))))))))))
(assert
 (let ((?x224 (* b15 0)))
 (let ((?x132 (* b13 0)))
 (let ((?x124 (* b10 0)))
 (let ((?x119 (* b8 0)))
 (let ((?x111 (* b5 0)))
 (let ((?x105 (* b3 0)))
 (let ((?x78 (+ (+ (+ (+ 0 (* b0 (- 3))) (* b1 0)) (* b2 (- 81))) ?x105)))
 (let ((?x86 (+ (+ (+ (+ ?x78 (* b4 (- 3))) ?x111) (* b6 3)) (* b7 (- 81)))))
 (let ((?x66 (+ (+ (+ (+ (+ ?x86 ?x119) (* b9 81)) ?x124) (* b11 3)) (* b12 (- 81)))))
 (= (+ (+ (+ (+ ?x66 ?x132) (* b14 81)) ?x224) (* b16 81)) (- 48))))))))))))
(assert
 (let ((?x224 (* b15 0)))
(let ((?x132 (* b13 0)))
(let ((?x124 (* b10 0)))
(let ((?x119 (* b8 0)))
(let ((?x111 (* b5 0)))
(let ((?x105 (* b3 0)))
(let ((?x50 (+ (+ (+ (+ 0 (* b0 (- 189))) (* b1 0)) (* b2 (- 3159))) ?x105)))
(let ((?x216 (+ (+ (+ (+ ?x50 (* b4 (- 27))) ?x111) (* b6 189)) (* b7 (- 243)))))
(let ((?x274 (+ (+ (+ (+ (+ ?x216 ?x119) (* b9 3159)) ?x124) (* b11 27)) (* b12 (- 1701)))))
(= (+ (+ (+ (+ ?x274 ?x132) (* b14 243)) ?x224) (* b16 1701)) 0)))))))))))
(check-sat)
