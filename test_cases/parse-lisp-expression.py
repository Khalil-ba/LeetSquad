# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))") == 14
    assert candidate(expression = "(let x 7 (let y 2 (let z 3 (mult x (add y z)))))") == 35
    assert candidate(expression = "(mult (let x 2 (mult 3 x)) (let x 2 (add 4 x)))") == 36
    assert candidate(expression = "(let x 0 (let x 1 x) x)") == 1
    assert candidate(expression = "(add 1 2)") == 3
    assert candidate(expression = "(mult 3 4)") == 12
    assert candidate(expression = "(let a 5 (let b 6 (let c 7 (mult (add a b) (add b c)))))") == 143
    assert candidate(expression = "(let x 0 (let x 1 x))") == 1
    assert candidate(expression = "(mult (add 1 2) (add 3 4))") == 21
    assert candidate(expression = "(let x 0 (let x (add 1 x) (let x (mult x 2) x)))") == 2
    assert candidate(expression = "(mult (let x 2 (add x 2)) (let y 3 (mult y y)))") == 36
    assert candidate(expression = "(let x 1 y (add x 2) (mult x y))") == 3
    assert candidate(expression = "(let a 3 b (add a 1) c (mult a b) c)") == 12
    assert candidate(expression = "(let x 1 y 1 x (add x y) (add x y))") == 3
    assert candidate(expression = "(let x 1 y 2 x (add x y) (add x y))") == 5
    assert candidate(expression = "(let x 3 x 2 x)") == 2
    assert candidate(expression = "(let x 2 (mult 3 (let x 3 y 4 (add x y))))") == 21
    assert candidate(expression = "(let x 1 (add x (let x 2 (add x (let x 3 (add x 4)))))") == 10
    assert candidate(expression = "(let x 1 (let y 2 (let z 3 (add x (add y z)))))") == 6
    assert candidate(expression = "(let x 1 (mult (let x 2 (add x 2)) x))") == 4
    assert candidate(expression = "(let x 7 (let y 2 (let x 3 (add x y))))") == 5
    assert candidate(expression = "(mult (let a 2 b 3 (add a b)) (let c 4 d 5 (mult c d)))") == 100
    assert candidate(expression = "(let x 7 (add x 3) (mult x 2))") == 10
    assert candidate(expression = "(let x (add 1 2) (mult x 3))") == 9
    assert candidate(expression = "(let x 2 (let y 3 (let z (add x y) (mult x z))))") == 10
    assert candidate(expression = "(let a1 3 b2 4 (add a1 b2))") == 7
    assert candidate(expression = "(let a1 3 b2 (add a1 1) b2)") == 4
    assert candidate(expression = "(let x 1 (let y (let z 3 (add z 2)) (mult x y)) (add x y))") == 5
    assert candidate(expression = "(let x (let y 2 (mult y 3)) (add x 5))") == 11
    assert candidate(expression = "(let x 5 y (add x 3) z (mult x y) (let w 7 (add w (mult x z))))") == 207
    assert candidate(expression = "(let m 8 n (add m 2) o (mult m n) p (add o n) (mult p m))") == 720
    assert candidate(expression = "(let a 1 b (let a (add a 1) (mult a a)) (add a b))") == 5
    assert candidate(expression = "(let a 1 b 2 c (mult a b) d (add a b) (mult c d))") == 6
    assert candidate(expression = "(let a 1 b (add a 1) c (mult a b) (add c (let a 2 (mult a b))))") == 6
    assert candidate(expression = "(mult (let x 2 (let y 3 (add x y))) (let x 4 (let y 5 (mult x y))))") == 100
    assert candidate(expression = "(let a 1 b 2 c (add a b) d (mult a c) (add d c))") == 6
    assert candidate(expression = "(let x 2 y 3 z (mult x y) (add (let x 5 (mult x y)) (let y 4 (add y z))))") == 25
    assert candidate(expression = "(mult (let x 5 y (mult x 2) (add y 3)) (let z 4 w (add z 1) (mult w 3)))") == 195
    assert candidate(expression = "(let a 5 b (add a 3) (mult a b))") == 40
    assert candidate(expression = "(let a 1 (let b (add a 1) (let c (mult b 2) (let d (add c 3) (let e (mult d 4) (add e 5)))))") == 33
    assert candidate(expression = "(let m 5 n 10 (let p (add m n) (mult p (let q (mult m n) (add q (let r (add p q) r)))))") == 1725
    assert candidate(expression = "(let x (mult 3 3) y (add 5 5) z (let w (mult x y) (add w 10)) (mult z x))") == 900
    assert candidate(expression = "(let a 1 b (let c (mult a a) d (add a a) (mult c d)) e (let f (mult b b) g (add b b) (mult f g)) (add e e))") == 32
    assert candidate(expression = "(let a 1 b (add a 1) c (mult b 2) d (add c 3) e (mult d 2) (add e (mult e (add d (mult c (add b a))))))") == 280
    assert candidate(expression = "(add (let x 5 (mult x 2)) (let y 3 (mult y 4)))") == 22
    assert candidate(expression = "(let a 10 (let b (mult a 2) (let c (add a b) (let d (mult b c) d))))") == 600
    assert candidate(expression = "(let m 2 (let n (mult m 3) (let o (add m n) (let p (mult m o) (add p (mult n o)))))") == 64
    assert candidate(expression = "(let x 5 (let y 3 (mult (add x y) (let z 2 (add z (mult x y)))))") == 136
    assert candidate(expression = "(let a (mult 2 3) b (add a 4) c (mult b a) d (add c b) (mult d c))") == 4200
    assert candidate(expression = "(let x 5 y 3 (let z (mult x y) (let w (add x z) (mult w (let v (add y z) v)))))") == 360
    assert candidate(expression = "(let x 1 (let y (add x 1) (let z (mult y 2) (let a (add z 3) (let b (mult a 4) (add (mult b 5) (let c (add b 6) (mult c 7)))))))") == 378
    assert candidate(expression = "(let a 1 b (add a 1) c (mult b 2) d (let e (add c b) (mult e a)) (add d (mult c a)))") == 10
    assert candidate(expression = "(mult (let x 2 (let y 3 (let z (add x y) (mult z 4)))) (let a 5 (let b 6 (let c (add a b) (mult c 7))))") == 1540
    assert candidate(expression = "(let x 7 y (mult x 2) z (add x y) (let w 3 (add w (mult x z))))") == 150
    assert candidate(expression = "(let x 1 y 2 (let x (add x y) y (mult x y) (let z (add x y) (mult x z))))") == 27
    assert candidate(expression = "(let x 1 (let y 2 (let z 3 (let a 4 (let b 5 (let c 6 (let d 7 (let e 8 (let f 9 (add x (mult y (add z (mult a (add b (mult c (add d (mult e f))))))))))))))))") == 3839
    assert candidate(expression = "(let x 10 (let y (add x 5) z (mult y 2) (let a (add z 3) b (mult a 4) (let c (add b 2) (mult c 5))))") == 670
    assert candidate(expression = "(let x 7 y (add x 2) z (mult x y) (let w (add y z) (mult w x)))") == 504
    assert candidate(expression = "(let x 5 y (add x 3) z (mult y 2) (let w (add x y) (mult w z)))") == 208
    assert candidate(expression = "(let x (let y (let z 3 (add z 1)) (mult y 2)) (mult x 5))") == 40
    assert candidate(expression = "(let x 10 (let y (mult x 3) (let z (add x y) (let w (mult y z) (let v (add w z) v)))))") == 1240
    assert candidate(expression = "(let x 1 (let y 2 (let z 3 (let w 4 (add (add x y) (add z w))))))") == 10
    assert candidate(expression = "(let a 2 b (mult a 3) c (add a b) d (mult b c) (add d c))") == 56
    assert candidate(expression = "(mult (add 1 2) (mult 3 4))") == 36
    assert candidate(expression = "(let x 5 y (add x 3) z (mult x y) (add z (let x 10 (mult x y))))") == 120
    assert candidate(expression = "(let x 10 y (add x 5) z (mult y 2) (let w (add x y) (mult w z)))") == 750
    assert candidate(expression = "(let x 5 (let y (add x 3) (mult x y)))") == 40
    assert candidate(expression = "(mult (let x 3 (let y 5 (add x y))) (let a 2 (mult a (let b 4 (add b 1))))") == 80
    assert candidate(expression = "(let x 5 y (let x 10 (add x 5)) z (mult y 2) (add z y))") == 45
    assert candidate(expression = "(let x 1 (let y 2 (let z 3 (let a (add x y) (let b (mult y z) (add (mult a b) (let c (add a b) (mult c 2)))))))") == 36
    assert candidate(expression = "(let x 1 (let y (let x 2 (let z 3 (add x z))) (mult x y)) (add x y))") == 5
    assert candidate(expression = "(let x 1 y 2 z 3 a (add x y) b (mult a z) c (add b a) d (mult c b) (add d c) e (mult d a) (add e b))") == 120
    assert candidate(expression = "(let x 5 (let y (let z 3 (add x z)) (mult x y)) (let w (add x y) (mult w x)))") == 40
    assert candidate(expression = "(let x 1 (let y (add x 1) (let z (mult y 2) (add x (add y z)))))") == 7
    assert candidate(expression = "(let a 1 b 2 c 3 (add (mult a b) (mult b c)))") == 8
    assert candidate(expression = "(let x 1 (let y (mult x 2) (let z (add y 3) (mult x (add y z)))))") == 7
    assert candidate(expression = "(let a 2 b (mult a 2) c (let d (add b 1) (mult d 3)) (add c (mult a b)))") == 23
    assert candidate(expression = "(let a 1 b 2 (add a b) (mult a b))") == 3
    assert candidate(expression = "(let x 7 (let y (add x 3) z (mult y 2) (let w (add z 5) (mult w y))))") == 250
    assert candidate(expression = "(let x 10 y (add x 5) z (mult y 2) (let w (add y z) (mult w x)))") == 450
    assert candidate(expression = "(let a 1 b 2 c 3 (add (mult a b) c))") == 5
    assert candidate(expression = "(let x 1 (let y 2 (let z 3 (let w 4 (mult (add x y) (mult z w))))))") == 36
    assert candidate(expression = "(mult (let x 3 (let y 4 (add x y))) (let x 6 (let y 7 (mult x y))))") == 294
    assert candidate(expression = "(let a 1 b 2 c 3 (let d (add a b) e (mult b c) (add d e)))") == 9
    assert candidate(expression = "(let a 1 (let b 2 (let a 3 (let b 4 (add (mult a b) (let a 5 (mult a b)))))))") == 32
    assert candidate(expression = "(let x 5 (let y (mult x 2) (let z (add y 3) (mult x z))))") == 65
    assert candidate(expression = "(add (mult 2 3) (let x 4 (mult x 5)))") == 26
    assert candidate(expression = "(let x 1 (let y 2 (let z 3 (let a (add x y) b (mult y z) c (add a b) d (mult b c) (let e (add c d) (mult d e)))))") == 3402
    assert candidate(expression = "(let x 1 (let y 2 (let z 3 (let a (add x y) b (mult y z) c (add a b) (mult b c)))))") == 54
    assert candidate(expression = "(let x (let y (let z 3 (mult z z)) (add y 5)) (mult x x))") == 196
    assert candidate(expression = "(mult (let a 3 b (add a 2) c (mult b 2) (add c a)) (let d 4 e (mult d 3) (add e d)))") == 208
    assert candidate(expression = "(mult (let x 7 (let y 3 (add x y))) (let x 4 (let y 6 (mult x y))))") == 240
    assert candidate(expression = "(let x 2 (let y (let z 2 (add z z)) (mult x y)) (let a 3 (let b (mult a x) (add b (let c 4 (mult c x)))))") == 8
    assert candidate(expression = "(let x 1 y 2 (let z (add x y) (let w (mult x y) (let u (add z w) u))))") == 5
    assert candidate(expression = "(let a 1 (let b 2 (let c (add a b) (let d (mult b c) (mult c d))))") == 18
    assert candidate(expression = "(let a 1 b 2 c 3 d (add a b) e (add c d) (mult d (let a 5 (add a b))))") == 21
    assert candidate(expression = "(let x 10 (let y (mult x 2) (let z (add x y) (let w (mult y z) (add w z))))") == 630
    assert candidate(expression = "(let x 1 (let y (add x 1) (let z (mult y 2) (let w (add x z) (mult w (let v (mult z 2) v)))))") == 40
    assert candidate(expression = "(let x 5 y (add x 3) (mult x y))") == 40
    assert candidate(expression = "(let x 5 (let y 10 (let z (add x y) (mult z x))))") == 75
    assert candidate(expression = "(let x 10 y (let x 5 (add x 3)) z (mult x y) (add z y))") == 88
    assert candidate(expression = "(let x 1 y 2 z 3 a (add x y) b (mult a z) c (add b a) (mult c b))") == 108
    assert candidate(expression = "(let x 1 (let y 2 (let z 3 (add (mult x y) z))))") == 5
    assert candidate(expression = "(let a 1 b 2 c (add a b) (mult c (let b 4 (add a b))))") == 15
    assert candidate(expression = "(let x 1 (let y 2 (let z 3 (add (mult x y) (add y z)))))") == 7
    assert candidate(expression = "(let a 1 b 2 c 3 d 4 e 5 (add (mult a b) (add (mult b c) (add (mult c d) (mult d e)))))") == 40
    assert candidate(expression = "(add (let a 1 b (add a 1) c (mult b 2) (add c a)) (let d 4 e (mult d 3) (add e d)))") == 21
    assert candidate(expression = "(let z (mult 3 4) w (add z 5) x (let y (mult z w) (add y z)) x)") == 216
    assert candidate(expression = "(let x 5 (add (mult x 2) (let x 3 (add (mult x 4) (let x 6 (mult x 7))))))") == 64
    assert candidate(expression = "(let x 5 (let y (add x 2) z (mult y 3) (let w (add z 4) (mult w x))))") == 125
    assert candidate(expression = "(let x (mult 2 3) y (add x 5) (let z (mult x y) (add z (mult x y))))") == 132
