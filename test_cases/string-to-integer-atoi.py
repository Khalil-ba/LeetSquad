# Import the utils module for prompts
from utils import *

def check(candidate):
    assert candidate(s = "2147483647") == 2147483647
    assert candidate(s = "42 with words") == 42
    assert candidate(s = "20000000000000000000000000000000000000000") == 2147483647
    assert candidate(s = "-2147483649") == -2147483648
    assert candidate(s = "-21474836480") == -2147483648
    assert candidate(s = "  000000000000   ") == 0
    assert candidate(s = "+1") == 1
    assert candidate(s = "   -  42") == 0
    assert candidate(s = "words with 42") == 0
    assert candidate(s = "   -042") == -42
    assert candidate(s = "0-1") == 0
    assert candidate(s = "   0") == 0
    assert candidate(s = "-5") == -5
    assert candidate(s = "      -119197303367810844   ") == -2147483648
    assert candidate(s = "   -12345") == -12345
    assert candidate(s = " ") == 0
    assert candidate(s = " -042") == -42
    assert candidate(s = "    -88827   5655  U") == -88827
    assert candidate(s = "+-12") == 0
    assert candidate(s = "   +0 123") == 0
    assert candidate(s = "+2") == 2
    assert candidate(s = "   +0 91283472332") == 0
    assert candidate(s = "   - 42") == 0
    assert candidate(s = "words and 987") == 0
    assert candidate(s = "3.14159") == 3
    assert candidate(s = "   20000000000000000000") == 2147483647
    assert candidate(s = "0000000000012345678") == 12345678
    assert candidate(s = ".") == 0
    assert candidate(s = "2147483648") == 2147483647
    assert candidate(s = "") == 0
    assert candidate(s = "    0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000") == 0
    assert candidate(s = "-") == 0
    assert candidate(s = "42") == 42
    assert candidate(s = "-91283472332") == -2147483648
    assert candidate(s = "4193 with words") == 4193
    assert candidate(s = "   3.14159") == 3
    assert candidate(s = "  +0 123") == 0
    assert candidate(s = "   +123") == 123
    assert candidate(s = "     +42") == 42
    assert candidate(s = "   +12345") == 12345
    assert candidate(s = "    +42") == 42
    assert candidate(s = "0000000000000") == 0
    assert candidate(s = "     ") == 0
    assert candidate(s = "00000000000000") == 0
    assert candidate(s = "   +42") == 42
    assert candidate(s = "1337c0d3") == 1337
    assert candidate(s = "   +0 91283472332 456") == 0
    assert candidate(s = " 21474836460") == 2147483647
    assert candidate(s = "+") == 0
    assert candidate(s = "    -00130") == -130
    assert candidate(s = "00000000000123456789") == 123456789
    assert candidate(s = "  -0012a42") == -12
    assert candidate(s = "  +3.14") == 3
    assert candidate(s = "21474836478") == 2147483647
    assert candidate(s = "-2147483648") == -2147483648
    assert candidate(s = "-21474836489") == -2147483648
    assert candidate(s = "  +  413") == 0
    assert candidate(s = "    -2147483649") == -2147483648
    assert candidate(s = "    21474836470000000000000000") == 2147483647
    assert candidate(s = "    9223372036854775808") == 2147483647
    assert candidate(s = "   2147483647abc") == 2147483647
    assert candidate(s = "    -123 456") == -123
    assert candidate(s = "    0000123") == 123
    assert candidate(s = "    21474836470000000000000000000000") == 2147483647
    assert candidate(s = "    2147483647000000000000000") == 2147483647
    assert candidate(s = "   2147483647 -") == 2147483647
    assert candidate(s = "    214748364700000000000000000000") == 2147483647
    assert candidate(s = "   abcdefghijklmnopqrstuvwxyz") == 0
    assert candidate(s = "    21474836470000000000000000000") == 2147483647
    assert candidate(s = "    000000000000000000000000000000000000000000000000000   -123") == 0
    assert candidate(s = "    +2147483649") == 2147483647
    assert candidate(s = "   +0") == 0
    assert candidate(s = "   2147483648") == 2147483647
    assert candidate(s = "    2147483647000000000000000000000") == 2147483647
    assert candidate(s = "    -21474836480000") == -2147483648
    assert candidate(s = "    -214748364800000000000000000") == -2147483648
    assert candidate(s = "    9223372036854775807") == 2147483647
    assert candidate(s = "    -214748364800000") == -2147483648
    assert candidate(s = "    -21474836480000000000000000000000") == -2147483648
    assert candidate(s = "    -21474836480000000") == -2147483648
    assert candidate(s = "   -12345678901234567890123456789012345678901234567890") == -2147483648
    assert candidate(s = "    -214748364800") == -2147483648
    assert candidate(s = "    2147483647000000000000000000000000000") == 2147483647
    assert candidate(s = "  0000000000000   +123abc") == 0
    assert candidate(s = "    -214748364800000000") == -2147483648
    assert candidate(s = "    -21474836480000000000000000000000000000") == -2147483648
    assert candidate(s = "    21474836470000000") == 2147483647
    assert candidate(s = "   +000000000000000000000000000000123") == 123
    assert candidate(s = "    2147483647000000000000000000000000") == 2147483647
    assert candidate(s = "   -0000000000000000000000000000000000000000000000000000000000000001") == -1
    assert candidate(s = "    000000000000000000000000000000000000000000000000000   123") == 0
    assert candidate(s = "    -21474836480") == -2147483648
    assert candidate(s = "    -2147483648000000000000") == -2147483648
    assert candidate(s = "   -2147483648 0") == -2147483648
    assert candidate(s = "    -214748364800000000000000000000") == -2147483648
    assert candidate(s = "    -214748364800000000000000000000000000") == -2147483648
    assert candidate(s = "    -9223372036854775808") == -2147483648
    assert candidate(s = "    -214748364800000000000000000000000000000") == -2147483648
    assert candidate(s = "    21474836470000000000000000000000000") == 2147483647
    assert candidate(s = "    -2147483648000") == -2147483648
    assert candidate(s = "    -2147483648") == -2147483648
    assert candidate(s = "   -2147483648extra") == -2147483648
    assert candidate(s = "    -2147483648000000000000000000000000") == -2147483648
    assert candidate(s = "    214748364700000000000") == 2147483647
    assert candidate(s = "   +2147483647extra") == 2147483647
    assert candidate(s = "   -2147483648abc") == -2147483648
    assert candidate(s = "   -2147483648") == -2147483648
    assert candidate(s = "    214748364700000000000000000000000") == 2147483647
    assert candidate(s = "   +000") == 0
    assert candidate(s = "    -9223372036854775809") == -2147483648
    assert candidate(s = "    214748364700000000000000") == 2147483647
    assert candidate(s = " 0000000000000000000000000000000000000000000000000001") == 1
    assert candidate(s = "   -0") == 0
    assert candidate(s = "   +0000000000000000000000000000000000000000000000000000000000000001") == 1
    assert candidate(s = "    010") == 10
    assert candidate(s = "    2147483647000000") == 2147483647
    assert candidate(s = "    -21474836480000000000000000000") == -2147483648
    assert candidate(s = "000000000000000000000000000000000000000000000000000") == 0
    assert candidate(s = "    -2147483648000000000000000") == -2147483648
    assert candidate(s = "-0000000000000000000000000000000000000000000000000001") == -1
    assert candidate(s = "    -2147483648000000000000000000") == -2147483648
    assert candidate(s = "    2147483646") == 2147483646
    assert candidate(s = "    214748364700000000000000000000000000000") == 2147483647
    assert candidate(s = "    2147483647000") == 2147483647
    assert candidate(s = "   12345678901234567890123456789012345678901234567890") == 2147483647
    assert candidate(s = "    0000-123") == 0
    assert candidate(s = "   -2147483648 -") == -2147483648
    assert candidate(s = "    000000000000000000000000000000000000000000000000000   +123") == 0
    assert candidate(s = "    123 456") == 123
    assert candidate(s = "   +2147483647 0") == 2147483647
    assert candidate(s = "    2147483648") == 2147483647
    assert candidate(s = "   2147483647extra") == 2147483647
    assert candidate(s = "    2147483647000000000000") == 2147483647
    assert candidate(s = "    214748364700000000000000000") == 2147483647
    assert candidate(s = "    21474836470000") == 2147483647
    assert candidate(s = "   0000000000000000000000000000000000000000000000000000000000000000+1") == 0
    assert candidate(s = "    -214748364800000000000000") == -2147483648
    assert candidate(s = "    -2147483648000000") == -2147483648
    assert candidate(s = "    -2147483648000000000000000000000") == -2147483648
    assert candidate(s = "   -000000000000000000000000000000123") == -123
    assert candidate(s = "    +2147483648") == 2147483647
    assert candidate(s = "    214748364700") == 2147483647
    assert candidate(s = "   +2147483647 +") == 2147483647
    assert candidate(s = "   00000000000000000000000000000000000000000000000000000000000000001") == 1
    assert candidate(s = "   +1234567890123456789012345678901234567890") == 2147483647
    assert candidate(s = "    -214748364800000000000000000000000") == -2147483648
    assert candidate(s = "    -2147483648000000000") == -2147483648
    assert candidate(s = "   !@#$%^&*()_+") == 0
    assert candidate(s = "    0000+123") == 0
    assert candidate(s = "    -21474836480000000000") == -2147483648
    assert candidate(s = "   -1234567890123456789012345678901234567890") == -2147483648
    assert candidate(s = "    -2147483646") == -2147483646
    assert candidate(s = "    -21474836480000000000000000000000000") == -2147483648
    assert candidate(s = "    2147483647") == 2147483647
    assert candidate(s = "    214748364700000000000000000000000000") == 2147483647
    assert candidate(s = "    -214748364800000000000") == -2147483648
    assert candidate(s = "   +2147483647abc") == 2147483647
    assert candidate(s = "    21474836470") == 2147483647
    assert candidate(s = "  0000000000000   123abc") == 0
    assert candidate(s = "    21474836470000000000") == 2147483647
    assert candidate(s = "    +123 456") == 123
    assert candidate(s = "    2147483647000000000000000000") == 2147483647
    assert candidate(s = "   0000000000000000000000000000000000000000000000000000000000000000-1") == 0
    assert candidate(s = "   ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 0
    assert candidate(s = "    -2147483648000000000000000000000000000") == -2147483648
    assert candidate(s = "   -2147483649") == -2147483648
    assert candidate(s = "-+12") == 0
    assert candidate(s = "    +2147483647") == 2147483647
    assert candidate(s = "    18446744073709551616") == 2147483647
    assert candidate(s = "   +0000000000000000000000000000000000000000000123") == 123
    assert candidate(s = "   00000000000000000000000000000000000000000000000000000000000000000") == 0
    assert candidate(s = "    21474836470000000000000") == 2147483647
    assert candidate(s = "    214748364700000") == 2147483647
    assert candidate(s = "    2147483647000000000") == 2147483647
    assert candidate(s = "  0000000000000   -123abc") == 0
    assert candidate(s = "  0000000000000   -00001") == 0
    assert candidate(s = "   -000") == 0
    assert candidate(s = "    214748364700000000") == 2147483647
    assert candidate(s = "    -2147483647") == -2147483647
    assert candidate(s = "    21474836470000000000000000000000000000") == 2147483647
    assert candidate(s = "    -21474836480000000000000") == -2147483648
    assert candidate(s = "    -21474836480000000000000000") == -2147483648
    assert candidate(s = "   -2147483648 +") == -2147483648
    assert candidate(s = "  0000000000000   +00001") == 0
    assert candidate(s = "   2147483647") == 2147483647
