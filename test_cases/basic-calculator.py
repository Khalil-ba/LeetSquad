# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = "30 - (5 + (10 - 15) + 20)") == 10
    assert candidate(s = "2147483647") == 2147483647
    assert candidate(s = "-2147483647") == -2147483647
    assert candidate(s = "- (3 + (2 - 1))") == -4
    assert candidate(s = "1 + (2 + 3) + (4 + (5 + 6))") == 21
    assert candidate(s = "5 - (3 - (1 + 2))") == 5
    assert candidate(s = "(1-2+(3-(4-5)))") == 3
    assert candidate(s = " 2-1 + 2 ") == 3
    assert candidate(s = "(1+(4+5+2)-3)+(6+8)") == 23
    assert candidate(s = "- (3 + (2 - 1) )") == -4
    assert candidate(s = "100 * 2 + 12") == 114
    assert candidate(s = "(1+(2+(3+(4+(5+(6+(7+(8+(9+(10)))))))))") == 55
    assert candidate(s = "((100 - 50) + (25 - 10))") == 65
    assert candidate(s = "10 + 2 * 6") == 18
    assert candidate(s = "10 + 20 - 5") == 25
    assert candidate(s = "- (5 - (- (1 + 1)))") == -7
    assert candidate(s = "-1 + (2 - (-3 + 4))") == 0
    assert candidate(s = "10 + (2 - 6)") == 6
    assert candidate(s = "-1 + (3-5)") == -3
    assert candidate(s = "10 - (-5 + 3)") == 12
    assert candidate(s = "(123 + (456 - 789))") == -210
    assert candidate(s = "(10 - (5 + 3))") == 2
    assert candidate(s = "(1 + (2 + (3 + (4 + 5))))") == 15
    assert candidate(s = "10 - (2 - (3 - 4))") == 7
    assert candidate(s = "100 * ( 2 + 12 )") == 114
    assert candidate(s = "10 + (2 - 3)") == 9
    assert candidate(s = "(5 + 15) - (10 + 20)") == -10
    assert candidate(s = "(123 + 456) - 789") == -210
    assert candidate(s = "1 - (2 - (3 - (4 - (5 - (6 - (7 - (8 - 9)))))))") == 5
    assert candidate(s = "- (5 + 10 + (15 - 20))") == -10
    assert candidate(s = "1 - (-1)") == 2
    assert candidate(s = "((1 + 3) + (5 + 7))") == 16
    assert candidate(s = "1 + 1") == 2
    assert candidate(s = "(1 + ((2 + 3) * (4 / 2)))") == 12
    assert candidate(s = "(100 - (50 + (25 - (12 + (6 - (3 + (1 - 1)))))))") == 40
    assert candidate(s = "100 / ((5 + (5 - (5 + (5 - 5)))) * 2)") == 103
    assert candidate(s = "10 - (5 - (3 - (2 - (1 - 0))))") == 7
    assert candidate(s = "-1 + (2 - (3 + (4 - (5 + (6 - (7 + (8 - 9)))))))") == -1
    assert candidate(s = "5 + (8 * 3 + 9 + (3 * 5))") == 33
    assert candidate(s = "((10 + 20) * (30 / 5)) - (40 + (50 - 60))") == 35
    assert candidate(s = "(1 + 2) * (3 + 4) * (5 + 6) * (7 + 8)") == 36
    assert candidate(s = "1 + (2 + (3 + (4 + (5 + (6 + (7 + (8 + (9 + 10))))))))") == 55
    assert candidate(s = "100 - (50 + ((25 * 2) - (10 + 5)))") == 38
    assert candidate(s = "(3 + (2 * 2) - (1 + 3) + (4 - (5 + 6)))") == -4
    assert candidate(s = "(1 - (2 - (3 - (4 - (5 - (6 - (7 - 8)))))))") == -4
    assert candidate(s = "(1 + (2 - (3 + (4 - (5 + 6)))))") == 7
    assert candidate(s = "(((((1 + 2) + 3) + 4) + 5) + 6)") == 21
    assert candidate(s = "10 + 20 * (30 + 40 / 5) + 5 * (6 + 7 * (8 + 9))") == 140
    assert candidate(s = "(10 + 20) - (30 - 40) + (50 * 60) / (70 - 80)") == 140
    assert candidate(s = "123 + (456 - 789) * (10 - 5)") == -215
    assert candidate(s = "3 * (5 + 2 * (2 + 3)) + 4 * (2 + (3 - 1))") == 23
    assert candidate(s = "((5 - 3) * (6 + 2) - (4 + 1) * (3 - 8)) + 10") == -6
    assert candidate(s = "((1 + 2) * (3 + (4 * (5 + 6))))") == 21
    assert candidate(s = "( 10 - ( 20 - ( 30 - ( 40 - ( 50 - 60 ) ) ) ) )") == -30
    assert candidate(s = "(1 + (2 + (3 + (4 + (5 + 6)))))") == 21
    assert candidate(s = "((1 + 2) * (3 - 4) + (5 * 6) - 7)") == 6
    assert candidate(s = "1 + (2 * (2 + 2) - (3 - 4) * (3 + (2 - 1)))") == 4
    assert candidate(s = "(9 + (8 + (7 + (6 + (5 + (4 + (3 + (2 + 1))))))))") == 45
    assert candidate(s = "10 - (20 + (30 - (40 + (50 - 60))))") == -10
    assert candidate(s = "(9 - (8 + 7 - (6 + 5 - 4))) * (3 + (2 - (1 + 0 - (-1))))") == -2
    assert candidate(s = "100 - (25 + 3 * (4 + 5))") == 63
    assert candidate(s = "100 - (50 + (25 - (10 + (5 - (2 + (1 - (0 + 1)))))))") == 38
    assert candidate(s = "(1 + (2 + (3 + (4 + (5 + (6 + (7 + (8 + 9))))))))") == 45
    assert candidate(s = "100 + ((-200 + (300 - (400 + (500 - (600 + (700 - (800 + (900 - 1000))))))))") == -200
    assert candidate(s = "(100 - (50 - (25 - (10 - (5 - 1)))))") == 69
    assert candidate(s = "5 + 3 * (10 - 2) / 4 - 1") == 11
    assert candidate(s = "1 + 2 * (3 + (4 * (5 + (6 * (7 + 8)))))") == 36
    assert candidate(s = "(9 + (8 - (7 + (6 - (5 + (4 - (3 + (2 - 1))))))))") == 9
    assert candidate(s = "( 1 + 2 ) * ( 3 + 4 ) - ( 5 + 6 ) * ( 7 + 8 )") == 14
    assert candidate(s = "(100 - 50) + ((25 * 2) - (10 + 5))") == 62
    assert candidate(s = "10 - (20 - (30 - (40 - 50)))") == 30
    assert candidate(s = "5 + ((1 + (2 * 2) + (3 * (4 + 5))) * 6)") == 28
    assert candidate(s = "(((((1 + 2) * 3) + 4) - 5) * 6) - 7") == -8
    assert candidate(s = "((2 + 3) * (5 - 1) + 7)") == 16
    assert candidate(s = "((10 + 2) - (5 + 3) * (2 - 8)) + 4") == 2
    assert candidate(s = "((1 + (2 + (3 + (4 + (5 + (6 + (7 + (8 + (9 + 0)))))))))") == 45
    assert candidate(s = "(((10 - 2) * 3) / 2) + (((4 + 5) * 6) / 3)") == 21
    assert candidate(s = "(1 - (2 + (3 - (4 + (5 - (6 + (7 - (8 + 9))))))))") == 9
    assert candidate(s = "(1 + (2 * (2 + 3) - 4) + 5)") == 9
    assert candidate(s = "((1 + 2) * (3 + 4) - 5) * 2") == 3
    assert candidate(s = "((10 + 20) - (30 + 40)) + (50 + (60 - (70 + (80 - (90 + (100 - (110 + (120 - 130))))))))") == 10
    assert candidate(s = "((1 + 2) * (3 + 4)) - ((5 + 6) * (7 + 8))") == -16
    assert candidate(s = "(2 + 6 * (25 - (3 + 3) * 2 ) ) + 5") == 34
    assert candidate(s = "(1 + (4 + (5 + (2 - 3)) - 3)) + (6 + 8)") == 20
    assert candidate(s = "((22 + (2 * (3 + 5))) - (7 + 3))") == 22
    assert candidate(s = "(1 + (2 - 3) * (4 + 5) - 6)") == -15
    assert candidate(s = "(1 + (2 - (3 + (4 - (5 + (6 - (7 + (8 - 9))))))))") == 1
    assert candidate(s = "(1 + 2) * (3 + 4) - (5 + 6) * (7 + 8) + (9 * 10)") == 33
    assert candidate(s = "1 - (2 + (3 - (4 - (5 - 6))))") == 1
    assert candidate(s = "(1 + (2 + (3 + (4 + (5 + (6 + (7 + 8)))))))") == 36
    assert candidate(s = "(1 + 2) + (3 + 4) + (5 + 6) + (7 + 8) + (9 + 10)") == 55
    assert candidate(s = "30 - (10 + 20) + (5 * (2 + 3))") == 10
    assert candidate(s = "(123 - (45 + (67 - (89 + 10))) + 21)") == 131
    assert candidate(s = "- ( - ( - ( - ( - 1 ) ) ) )") == -1
    assert candidate(s = "- (3 + (4 - 5))") == -2
    assert candidate(s = "(((((1 + 2) * 3) - 4) + 5) * (6 - (7 + 8)))") == -2
    assert candidate(s = "3 * (2 + (1 - 5) * (3 + 7)) - 2") == -11
    assert candidate(s = "( ( 1 + 2 ) * ( 3 + 4 ) ) - ( ( 5 + 6 ) * ( 7 + 8 ) )") == -16
    assert candidate(s = "(3 * (4 - (5 + 2)) / (1 - 2))") == -1
    assert candidate(s = "((((-1 + 2) - 3) + 4) - 5)") == -3
    assert candidate(s = "(12 - (4 + 3) * (2 - 1)) + 7") == 13
    assert candidate(s = "( 123 + ( 456 - ( 789 + ( 12 - 34 ) ) ) )") == -188
    assert candidate(s = "10 + 20 * (30 - 20 / 2) + 5") == 43
    assert candidate(s = "((2 + 3) * (4 + 5) - 6) + 7 * (8 - 9)") == 14
    assert candidate(s = "(1 + (2 * (2 + 3)) - (4 * (5 - 6))) + (7 * (8 - (9 + 1)))") == 10
    assert candidate(s = "(((1 + 2) * 3) + ((4 + 5) * 6) + ((7 + 8) * 9))") == 45
    assert candidate(s = "(10 + 20) - (30 + 40) + (50 - 60)") == -50
    assert candidate(s = "(5 + (10 + (15 + (20 + (25 + (30 + (35 + (40 + (45 + 50)))))))))") == 275
    assert candidate(s = "10 - 2 * (6 / (3 + 1))") == -2
    assert candidate(s = "(10 + 2) * 6 - (3 + (4 - 5))") == 16
    assert candidate(s = "100 + ( 50 - ( 25 * ( 4 + 1 ) ) ) + ( 10 - ( 2 * 3 ) )") == 125
    assert candidate(s = "((2 + 3) * (4 + 5)) - (6 * (7 + 8))") == -7
    assert candidate(s = "100 - ((99 - (98 - (97 - (96 - (95 - (94 - (93 - (92 - (91 - 90)))))))))") == 5
    assert candidate(s = "((3 + 5) - (2 * (8 / 4)) + 1)") == -5
    assert candidate(s = "(123 - (456 + 789) + (101 - 202))") == -1223
    assert candidate(s = "100 - ( 3 * ( 2 + 4 ) ) + 5") == 96
    assert candidate(s = "-1 + (-2 + (-3 * (-4 - (-5))))") == -7
    assert candidate(s = "- ( 2 + 3 ) + ( 4 - 5 )") == -6
    assert candidate(s = "(100 - (50 + (25 - (10 + (5 - 2)))))") == 38
    assert candidate(s = "(10 + 2 * 6) / ((5 - 3) * 2)") == 18
    assert candidate(s = "10 + (2 * (6 / 3))") == 21
    assert candidate(s = "5 * (3 + (2 * (2 + (1 + (0 - (-1))))))") == 14
    assert candidate(s = "1 - (2 + 3) * (4 - 5) + (6 / 3)") == 4
    assert candidate(s = "1 - (2 + (3 * (4 + (5 * (6 + (7 * (8 + (9 * (10 + 11)))))))))") == -64
    assert candidate(s = "(100 - 50) - ((25 * 2) - (10 + 5))") == 38
    assert candidate(s = "1 + (2 + (3 + (4 + (5 + 6))))") == 21
    assert candidate(s = "((22 + (2 * 3)) * (4 + 3))") == 34
    assert candidate(s = "(10 + 20) - ((30 + 40) - (50 + (60 - (70 + (80 - (90 + (100 - 110)))))))") == 0
    assert candidate(s = "(8 - (4 + (1 - 3) + (2 - (5 + 7))))") == 16
    assert candidate(s = "100 - (25 * (2 + 3))") == 70
    assert candidate(s = "-((1 + 2) + (3 + 4)) + ((5 + 6) + (7 + 8))") == 16
    assert candidate(s = "(100 + 200 + (300 + (400 + (500 + (600 + (700 + (800 + 900)))))))") == 4500
    assert candidate(s = "10 - (9 - (8 - (7 - (6 - (5 - (4 - (3 - (2 - 1))))))))") == 5
    assert candidate(s = "100 + (200 * (300 + 400) - 500)") == 500
    assert candidate(s = "1 - (-2 - (-3 - (-4)))") == 4
    assert candidate(s = "10 + 20 - 30 + (40 - 50)") == -10
    assert candidate(s = "((1 + 2) * (3 - 4)) + (5 + 6)") == 13
    assert candidate(s = "12 - (4 * (2 + 3)) + 15") == 18
    assert candidate(s = "3 + 5 / 2") == 10
    assert candidate(s = "1 + (2 * (2 + 2) - (3 - 4) * 3)") == 5
    assert candidate(s = "(5 + 3) * (7 - (2 + 3))") == 10
    assert candidate(s = "10 + 2 * (6 / (3 + 1)) - (8 - 4) * (2 + 1)") == 15
    assert candidate(s = "2 * ((3 + 4) * (5 - 6) + 7) - 8") == 7
    assert candidate(s = "(1 + (2 * (2 + (3 * (4 + (5 * (6 + 7)))))))") == 30
    assert candidate(s = "123 + (456 - (789 + (101 - 202) ) )") == -109
    assert candidate(s = "3 + (2 * (2 + (2 * (2 + (2 * 2)))))") == 15
    assert candidate(s = "-1 + (-2 + (-3 + (-4 + (-5))))") == -15
    assert candidate(s = "(((1 + 2) * (3 + 4)) - 5) * (6 + 7)") == -8
    assert candidate(s = "(3 + (2 * (2 + 1)))") == 8
    assert candidate(s = "20 * ((1 + 2) * (3 + 4) - (5 * 6)) / 10") == 29
    assert candidate(s = "((100 - (50 + (25 - (10 + (5 - (2 + (1 - 0))))))) + (10 - 5))") == 42
    assert candidate(s = "(5 - 3) * (10 - (4 + 2) * (3 - 1))") == -4
    assert candidate(s = "(1 + 2) * 3 - 4 * (5 + 6)") == -9
    assert candidate(s = "(1 - (2 + (3 - (4 + (5 - 6)))))") == -1
    assert candidate(s = "(1 - (2 - (3 - (4 - (5 - (6 - (7 - (8 - 9)))))))") == 5
    assert candidate(s = "(3 - 4) * (5 - (6 - (7 - (8 - (9 - 10)))))") == 2
    assert candidate(s = "(10 + ((20 + 30) - (40 + (50 - (60 + (70 - 80))))))") == 20
    assert candidate(s = "(((1 + 2) * (3 + 4)) - (5 + 6)) * (7 - (8 + 9))") == -11
    assert candidate(s = "(1 + (2 * (3 + (4 * (5 + (6 * (7 + (8 * (9 + 10))))))))") == 55
    assert candidate(s = "1 + (2 - (3 + (4 - (5 + (6 - (7 + (8 - 9)))))))") == 1
    assert candidate(s = "(3 * (5 - (2 + 1)) + 4) - (6 * (8 - (7 + 1)))") == 3
    assert candidate(s = "((1 + 2) * (3 + 4) - (5 + 6)) * (7 + 8) - (9 + 10)") == -5
    assert candidate(s = "(1 + 2) * (3 - 4) * (5 + 6) * (7 - 8)") == -10
    assert candidate(s = "1 + 2 - 3 * (4 - 5) / (6 - 7) + 8") == 10
    assert candidate(s = "(1 + (2 * 3)) - (4 + (5 * 6))") == -9
    assert candidate(s = "(((3 + 2) * (4 + 5)) - (6 + (7 * 8) - 9)) + 10") == 12
    assert candidate(s = "(100 - (50 + 25 - (10 * 2 + 5)) + 15)") == 57
    assert candidate(s = "1000 + (2000 - (3000 - (4000 - (5000 - (6000 - (7000 - 8000))))))") == 6000
    assert candidate(s = "( ( ( 1 + 2 ) * 3 ) - ( 4 + 5 ) )") == -3
    assert candidate(s = "(1 + (2 * (3 + (4 * (5 + 6))))) - (7 + (8 * (9 + 10)))") == -13
    assert candidate(s = "((1 + 2) * (3 + 4) - (5 * 6))") == -1
    assert candidate(s = "(10 - 5) + (3 * 2) + (8 / 4)") == 22
    assert candidate(s = "3 + 5 * ( 2 - 8 )") == 2
    assert candidate(s = "(3 - (5 - (7 - (9 - (11 - (13 - (15 - 17))))))") == -8
