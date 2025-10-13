# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = "2 - 3 + 4") == 3
    assert candidate(s = " 1000000000 - 500000000 + 250000000") == 750000000
    assert candidate(s = "30 + 2 * 6 / (3 - 1)") == 33
    assert candidate(s = "100 * ( 2 + 12 ) / 14") == 200
    assert candidate(s = "1 + 1 * 1 + 1") == 3
    assert candidate(s = "2*3+4/5") == 6
    assert candidate(s = "3 + 5 / ( 2 + 3 )") == 8
    assert candidate(s = "0 + 0") == 0
    assert candidate(s = "100*2+12") == 212
    assert candidate(s = "2147483647 + 1 - 1") == 2147483647
    assert candidate(s = "100000 + 100000 - 50000 * 2 + 25000 * 4 / 5") == 120000
    assert candidate(s = "100 * 2 + 12") == 212
    assert candidate(s = " 200 - 3 * 50 + 25") == 75
    assert candidate(s = "10 + 2 * 6") == 22
    assert candidate(s = "3+2*2") == 7
    assert candidate(s = " 30 + 2 * 6 - 12 / 3 ") == 38
    assert candidate(s = "100*(2+12)/14") == 200
    assert candidate(s = " 3+5 / 2 ") == 5
    assert candidate(s = "1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10") == 3628800
    assert candidate(s = "100 * 2 / 25") == 8
    assert candidate(s = " 0 + 0 * 1 / 1") == 0
    assert candidate(s = " 3/2 ") == 1
    assert candidate(s = "3 + 5 - ( 2 + 3 )") == 9
    assert candidate(s = "2147483647 - 2147483646") == 1
    assert candidate(s = "3+5 / 2 * 3") == 9
    assert candidate(s = "3 + 2 * 2 + 1 - 5 / 2") == 6
    assert candidate(s = "10 * 5 + 3") == 53
    assert candidate(s = "3+5-2*3/4") == 7
    assert candidate(s = "3 + 5 / 2 + 3") == 8
    assert candidate(s = "1000 / 10 / 10") == 10
    assert candidate(s = "3 + 5 / 2 - 8 * 3 + 4 / 2") == -17
    assert candidate(s = "1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1") == 10
    assert candidate(s = " 30 / 3 + 10 * 2 - 5") == 25
    assert candidate(s = "100*(2+12)") == 212
    assert candidate(s = "100 * ( 2 + 12 )") == 212
    assert candidate(s = " 1 + 2 * 3 / 4 + 5 * 6 - 7") == 25
    assert candidate(s = "( 2 + 6 ) * 3 + 8") == 28
    assert candidate(s = "(2 + 6 * 3 + 5 - (3 * 14 / 7 + 2) * 5) + 3") == 32
    assert candidate(s = "2147483647 / 1") == 2147483647
    assert candidate(s = "1 - 1 + 1") == 1
    assert candidate(s = "2*3+4/5*6-7+8") == 7
    assert candidate(s = "10 + 2 - 5") == 7
    assert candidate(s = " 30 /3 + 10 * 2 ") == 30
    assert candidate(s = "2 * 3 + 4 / 5") == 6
    assert candidate(s = "3 + 2 * 2 + 1") == 8
    assert candidate(s = "10+2*6") == 22
    assert candidate(s = "3 + ( 2 * 2 )") == 7
    assert candidate(s = "123 + 456 * 789 / 100 - 987") == 2733
    assert candidate(s = "1000 - 500 * 2 + 250 / 5") == 50
    assert candidate(s = " 100000 - 50000 * 2 + 25000 / 5000 * 20000") == 100000
    assert candidate(s = "987654 * 321 / 123 - 456789 + 987654") == 3108401
    assert candidate(s = " 1 + 2 - 3 * (4 / 5) + 6 - 7 * 8 / 9") == 1
    assert candidate(s = "   8 *    5 / 4 + 3 - 1") == 12
    assert candidate(s = " 2000 / 10 + 50 * 2 - 300 ") == 0
    assert candidate(s = " 1234 + 567 * 89 - 101112 / 1314") == 51621
    assert candidate(s = " (123 + 456) * 789 - 101112 / (13 * 14) ") == 251029
    assert candidate(s = "1 * 2 + 3 * 4 + 5 * 6 + 7 * 8 + 9 * 10") == 190
    assert candidate(s = "100 / 10 - 90 * 0 + 80 / 8") == 20
    assert candidate(s = " 1000000 - 500000 + 250000 * 2 - 125000 ") == 875000
    assert candidate(s = "1000 - 500 * 2 / 5 + 300 / 3") == 900
    assert candidate(s = " 1000 + 2000 - (3000 / 4000 + 5000 - 6000 * (7000 / 8000))") == 2750
    assert candidate(s = " 200 * 5 + 300 / 100 - 10 ") == 993
    assert candidate(s = "123 + 456 * 789 - 101112 / 1314") == 359831
    assert candidate(s = " 5 + 4 - 3 * 2 + 1 / 1") == 4
    assert candidate(s = " ( 100 + 200 ) * ( 300 - 100 ) / 50") == 60098
    assert candidate(s = "7 * 8 * 9 / 6 + 5 - 3 * 2") == 83
    assert candidate(s = "300 + 200 * 5 / 10 - 25") == 375
    assert candidate(s = "100 * 200 / 500 + 200 - 100") == 140
    assert candidate(s = "100000 / 100 - 99999 * 0 + 1") == 1001
    assert candidate(s = "   42   *   (5 - 3) / 2 + 8  ") == 217
    assert candidate(s = "   23 + 56 * 99 / 77 - 44   ") == 51
    assert candidate(s = "100 * 2 + 12 / 3 - 5") == 199
    assert candidate(s = "   123 + 456 - 789 * 0 / 1 + 1000   ") == 1579
    assert candidate(s = "33 + 22 * 11 - 44 / 11 + 55") == 326
    assert candidate(s = "3 * 3 * 3 * 3 * 3 - 3 * 3 * 3 + 3") == 219
    assert candidate(s = "2147483647 - 2147483646 + 1") == 2
    assert candidate(s = "10 + 2 * 6 / ( 1 - 2 ) * 3") == 16
    assert candidate(s = "999999 + 1 - 999999 * 0 + 999999 / 1") == 1999999
    assert candidate(s = "12 + 34 * 56 / 78 - 90 + 12") == -42
    assert candidate(s = " 2 * (3 + 4 * (5 - 6 / 2)) + 7") == 30
    assert candidate(s = "2 + 3 * 5 / 2 - 8 / 4 + 6") == 13
    assert candidate(s = "5 * 5 * 5 * 5 * 5 / 5 + 5 - 5") == 625
    assert candidate(s = "3 * 3 + 3 / 3 * 3 - 3") == 9
    assert candidate(s = " 100 - 25 * 2 + 50 / 5 - 10") == 50
    assert candidate(s = " 2 * 3 + ( 2 * ( 1 + 4 ) / 2 ) - 5 ") == 5
    assert candidate(s = "333333 + 222222 * 1 - 111111 / 1") == 444444
    assert candidate(s = "2222 + 1111 * 2 - 3333 / 11 + 4444") == 8585
    assert candidate(s = " 1000 - 500 * 2 + 250 / 50 * 20") == 100
    assert candidate(s = " 99 * 100 - 99 * 99 + 99 * 98") == 9801
    assert candidate(s = "10 / 2 + 15 * 3 - 7 * (5 - 3) + 20") == 32
    assert candidate(s = "10000 / 1000 + 200 * 2 - 500") == -90
    assert candidate(s = " 33333 + 22222 - 11111 + 44444 * 55555 / 66666") == 81480
    assert candidate(s = "1000 * 2 / 25 + 100 - 50") == 130
    assert candidate(s = "123456789 + 987654321 * 1 - 123456789 / 1") == 987654321
    assert candidate(s = "100 * 2 + 3 * 5 / 15 - 10") == 191
    assert candidate(s = " 2 * ( 3 + 4 * ( 5 - 6 ) / 7 ) - 8 ") == 18
    assert candidate(s = "1000 * 5 / 25 + 20 - 40") == 180
    assert candidate(s = " 200 + 50 / 5 - 30 * 2 + 10") == 160
    assert candidate(s = "32 / 2 * 2 + 1 - 1") == 32
    assert candidate(s = " 987654321 - 123456789 + 98765 * 43210 / 54321") == 864276095
    assert candidate(s = "    1234 + 5678 * 90 / 100 - 12345 / 5    ") == 3875
    assert candidate(s = " 3 + 8 * 10 / 5 - 2 ") == 17
    assert candidate(s = " 7 + 3 * ( 10 / 2 ) - 5") == 17
    assert candidate(s = "  100 * 2 / 5 + 3 * (20 - 15)  ") == 85
    assert candidate(s = " 10 * 20 - 5 * 4 + 3 * 2 - 1 / 1 + 8 * 2") == 201
    assert candidate(s = "  8  *  (  4  /  2  )  +  12  -  6") == 22
    assert candidate(s = " 99 + 99 * 99 / 99 - 99 ") == 99
    assert candidate(s = "100 - 50 + 25 - 12 + 6 - 3 + 1") == 67
    assert candidate(s = "1000 * 2 + 300 - 50 / 2") == 2275
    assert candidate(s = "100 + 200 * (300 - 150 / 50) - 400") == 59697
    assert candidate(s = "333 * 111 + 222 * 444 / 666 - 777 + 888") == 37222
    assert candidate(s = "7 + 3 * (10 / 2) - 1") == 21
    assert candidate(s = "2 * 3 + 4 * 5 - 6 / 2 + 7") == 30
    assert candidate(s = "(1 + 2) * 3 / 4 + 5 - 6") == 1
    assert candidate(s = " 123 + 456 * 789 / 321 ") == 1243
    assert candidate(s = "3 + 5 * 2 / 2 - 1") == 7
    assert candidate(s = "   1000 + 2000 * 3000 - 4000 / 5000 + 6000 - 7000 * 8000 / 9000  ") == 6000778
    assert candidate(s = " 1000 + 2000 - 3000 * (4000 / 5000) + 6000 - 7000 * (8000 / 9000)") == 378
    assert candidate(s = "10 * 10 - 9 * 9 + 8 * 8 - 7 * 7 + 6 * 6") == 70
    assert candidate(s = " 1000 * 2000 - 3000 + 4000 / 5000 * 6000") == 1997000
    assert candidate(s = " 2147483647 + 1 * 2 - 3 / 4") == 2147483649
    assert candidate(s = " (10 + (20 + (30 + (40 + (50 + (60 + (70 + (80 + (90 + 100)))))))) ") == 550
    assert candidate(s = " 100 + 200 - 300 * 400 / 500 + 600 * 700 / 800") == 585
    assert candidate(s = " 4 + 5 * 6 / 3 - 7 + 8 * 2") == 23
    assert candidate(s = " 1 + 2 * ( 3 + 4 ) / 2 - 1 ") == 8
    assert candidate(s = " 1234 + 5678 - 91011 * 121314 / 151617") == -65909
    assert candidate(s = " 999 + 1 * 1000 - 500 / 2 ") == 1749
    assert candidate(s = " 100 * 2 + 3 - 4 / 2 ") == 201
    assert candidate(s = " 0 + 0 * 0 - 0 / 1") == 0
    assert candidate(s = " 7 + 14 / 7 - 3 + 6 * 2") == 18
    assert candidate(s = "0 * 1 + 2 - 3 / 4 * 5") == 2
    assert candidate(s = " 123 + 456 * 789 / 101 - 234") == 3451
    assert candidate(s = " 12345 + 67890 - 54321 / 1234 * 5678  ") == -169597
    assert candidate(s = " 123 + 456 - 789 * 1011 / 1213") == -78
    assert candidate(s = "   3   *   5   /   15   +   10   -   7   ") == 4
    assert candidate(s = " 100 - 50 + 25 * 4 / 2 ") == 100
    assert candidate(s = "10 + 20 * (30 / 10) - 5") == 65
    assert candidate(s = " 99999 + 88888 - 77777 * 66666 / 55555") == 95555
    assert candidate(s = " 100 + 200 * (300 / 50) - 600 + 700 * 800 / 900 ") == 1322
    assert candidate(s = "999999 / 3 + 999999 / 3 - 999999 / 3") == 333333
    assert candidate(s = " 1000 / ( 500 / 250 ) - 250 + 125 * ( 500 / 250 )") == 0
    assert candidate(s = " 2 * 3 + 4 * 5 - 6 / 3 + 8") == 32
    assert candidate(s = "987654 * 321 / 1000 + 123456 - 789012 / 3") == 177488
    assert candidate(s = " 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 ") == 3628800
    assert candidate(s = "   42  *   2   -   5   /   1   +   3   ") == 82
    assert candidate(s = " 2 * ( 3 + 5 ) * 4") == 26
    assert candidate(s = "30 / 5 * 2 - 1 + 4 * 8 - 3") == 40
    assert candidate(s = " 1 + (2 + (3 + (4 + (5 + 6))))") == 21
    assert candidate(s = " 123456789 + 987654321 - 111111111 * 222222222 / 333333333") == 1037037036
    assert candidate(s = "123 + 456 * 789 / 101 - 234") == 3451
    assert candidate(s = "1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10") == 55
    assert candidate(s = " 1000 / ( 25 / 5 ) + 50 - 20") == 38
    assert candidate(s = " 5 + 3 * (2 - 8) + 4 / 2") == 5
    assert candidate(s = "987654321 - 123456789 + 111111111 * 222222222 / 333333333  ") == 938271606
    assert candidate(s = " 8 / 3 + 4 * ( 5 - 3 ) / 2 ") == 21
    assert candidate(s = " 5 * 6 + 20 / 4 - 8") == 27
    assert candidate(s = " 3 + 8 * ( 4 - 2 ) / 2") == 34
    assert candidate(s = " 5 + 3 * ( 20 / 4 ) ") == 20
    assert candidate(s = "1000000 + 500000 * 2 - 250000 / 5 + 125000") == 2075000
    assert candidate(s = "2 + 3 * 4 - 5 / 2 + 6 * 7 - 8 / 4") == 52
    assert candidate(s = " 1000 - 500 + 250 * 2 - 125 ") == 875
    assert candidate(s = "0 * 0 + 0 / 1 + 100 - 50") == 50
    assert candidate(s = " 10 + 20 + 30 + 40 + 50 - ( 10 * 5 )") == 100
    assert candidate(s = " 7 * 8 - 3 + 2 * 4 ") == 61
    assert candidate(s = "9 * 3 + 2 - 1 / 1 + 8 * 2") == 44
    assert candidate(s = "50 * 50 - 50 / 50 + 50 * 50 - 50 / 50") == 4998
    assert candidate(s = " 3 + (2 * (2 + (2 * (2 + 2))))") == 13
    assert candidate(s = "100 * 2 + 12 / 3 - 50") == 154
    assert candidate(s = "3 + 33 + 333 + 3333 + 33333 + 333333 + 3333333 + 33333333 + 333333333") == 370370367
    assert candidate(s = "1 + 2 * 3 + 4 / 2 - 5") == 4
    assert candidate(s = " 3 + 5 * ( 2 + 8 ) / 4 - 2 ") == 13
