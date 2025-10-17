def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "2147483647") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2147483647") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "42 with words") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "42 with words") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "20000000000000000000000000000000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "20000000000000000000000000000000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "-2147483649") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "-2147483649") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "-21474836480") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "-21474836480") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "  000000000000   ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "  000000000000   ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "+1") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "+1") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "   -  42") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   -  42") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "words with 42") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "words with 42") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "   -042") == -42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   -042") == -42: {e}')
    
    total += 1
    try:
        result = candidate(s = "0-1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0-1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "   0") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   0") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "-5") == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "-5") == -5: {e}')
    
    total += 1
    try:
        result = candidate(s = "      -119197303367810844   ") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "      -119197303367810844   ") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "   -12345") == -12345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   -12345") == -12345: {e}')
    
    total += 1
    try:
        result = candidate(s = " ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = " -042") == -42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " -042") == -42: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -88827   5655  U") == -88827
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -88827   5655  U") == -88827: {e}')
    
    total += 1
    try:
        result = candidate(s = "+-12") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "+-12") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "   +0 123") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   +0 123") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "+2") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "+2") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "   +0 91283472332") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   +0 91283472332") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "   - 42") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   - 42") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "words and 987") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "words and 987") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "3.14159") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3.14159") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "   20000000000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   20000000000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000012345678") == 12345678
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000012345678") == 12345678: {e}')
    
    total += 1
    try:
        result = candidate(s = ".") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = ".") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "2147483648") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2147483648") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "    0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "-") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "-") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "42") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "42") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "-91283472332") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "-91283472332") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "4193 with words") == 4193
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "4193 with words") == 4193: {e}')
    
    total += 1
    try:
        result = candidate(s = "   3.14159") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   3.14159") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "  +0 123") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "  +0 123") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "   +123") == 123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   +123") == 123: {e}')
    
    total += 1
    try:
        result = candidate(s = "     +42") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "     +42") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "   +12345") == 12345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   +12345") == 12345: {e}')
    
    total += 1
    try:
        result = candidate(s = "    +42") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    +42") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "0000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "0000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "     ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "     ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "   +42") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   +42") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "1337c0d3") == 1337
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1337c0d3") == 1337: {e}')
    
    total += 1
    try:
        result = candidate(s = "   +0 91283472332 456") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   +0 91283472332 456") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = " 21474836460") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 21474836460") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "+") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "+") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -00130") == -130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -00130") == -130: {e}')
    
    total += 1
    try:
        result = candidate(s = "00000000000123456789") == 123456789
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "00000000000123456789") == 123456789: {e}')
    
    total += 1
    try:
        result = candidate(s = "  -0012a42") == -12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "  -0012a42") == -12: {e}')
    
    total += 1
    try:
        result = candidate(s = "  +3.14") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "  +3.14") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "21474836478") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "21474836478") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "-2147483648") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "-2147483648") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "-21474836489") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "-21474836489") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "  +  413") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "  +  413") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -2147483649") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -2147483649") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    21474836470000000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    21474836470000000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    9223372036854775808") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    9223372036854775808") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "   2147483647abc") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   2147483647abc") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -123 456") == -123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -123 456") == -123: {e}')
    
    total += 1
    try:
        result = candidate(s = "    0000123") == 123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    0000123") == 123: {e}')
    
    total += 1
    try:
        result = candidate(s = "    21474836470000000000000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    21474836470000000000000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    2147483647000000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    2147483647000000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "   2147483647 -") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   2147483647 -") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    214748364700000000000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    214748364700000000000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "   abcdefghijklmnopqrstuvwxyz") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   abcdefghijklmnopqrstuvwxyz") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "    21474836470000000000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    21474836470000000000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    000000000000000000000000000000000000000000000000000   -123") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    000000000000000000000000000000000000000000000000000   -123") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "    +2147483649") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    +2147483649") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "   +0") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   +0") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "   2147483648") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   2147483648") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    2147483647000000000000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    2147483647000000000000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -21474836480000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -21474836480000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -214748364800000000000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -214748364800000000000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    9223372036854775807") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    9223372036854775807") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -214748364800000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -214748364800000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -21474836480000000000000000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -21474836480000000000000000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -21474836480000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -21474836480000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "   -12345678901234567890123456789012345678901234567890") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   -12345678901234567890123456789012345678901234567890") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -214748364800") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -214748364800") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    2147483647000000000000000000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    2147483647000000000000000000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "  0000000000000   +123abc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "  0000000000000   +123abc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -214748364800000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -214748364800000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -21474836480000000000000000000000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -21474836480000000000000000000000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    21474836470000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    21474836470000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "   +000000000000000000000000000000123") == 123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   +000000000000000000000000000000123") == 123: {e}')
    
    total += 1
    try:
        result = candidate(s = "    2147483647000000000000000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    2147483647000000000000000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "   -0000000000000000000000000000000000000000000000000000000000000001") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   -0000000000000000000000000000000000000000000000000000000000000001") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "    000000000000000000000000000000000000000000000000000   123") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    000000000000000000000000000000000000000000000000000   123") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -21474836480") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -21474836480") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -2147483648000000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -2147483648000000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "   -2147483648 0") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   -2147483648 0") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -214748364800000000000000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -214748364800000000000000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -214748364800000000000000000000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -214748364800000000000000000000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -9223372036854775808") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -9223372036854775808") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -214748364800000000000000000000000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -214748364800000000000000000000000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    21474836470000000000000000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    21474836470000000000000000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -2147483648000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -2147483648000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -2147483648") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -2147483648") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "   -2147483648extra") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   -2147483648extra") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -2147483648000000000000000000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -2147483648000000000000000000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    214748364700000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    214748364700000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "   +2147483647extra") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   +2147483647extra") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "   -2147483648abc") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   -2147483648abc") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "   -2147483648") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   -2147483648") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    214748364700000000000000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    214748364700000000000000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "   +000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   +000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -9223372036854775809") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -9223372036854775809") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    214748364700000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    214748364700000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = " 0000000000000000000000000000000000000000000000000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 0000000000000000000000000000000000000000000000000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "   -0") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   -0") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "   +0000000000000000000000000000000000000000000000000000000000000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   +0000000000000000000000000000000000000000000000000000000000000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "    010") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    010") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "    2147483647000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    2147483647000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -21474836480000000000000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -21474836480000000000000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "000000000000000000000000000000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "000000000000000000000000000000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -2147483648000000000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -2147483648000000000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "-0000000000000000000000000000000000000000000000000001") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "-0000000000000000000000000000000000000000000000000001") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -2147483648000000000000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -2147483648000000000000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    2147483646") == 2147483646
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    2147483646") == 2147483646: {e}')
    
    total += 1
    try:
        result = candidate(s = "    214748364700000000000000000000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    214748364700000000000000000000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    2147483647000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    2147483647000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "   12345678901234567890123456789012345678901234567890") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   12345678901234567890123456789012345678901234567890") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    0000-123") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    0000-123") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "   -2147483648 -") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   -2147483648 -") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    000000000000000000000000000000000000000000000000000   +123") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    000000000000000000000000000000000000000000000000000   +123") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "    123 456") == 123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    123 456") == 123: {e}')
    
    total += 1
    try:
        result = candidate(s = "   +2147483647 0") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   +2147483647 0") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    2147483648") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    2147483648") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "   2147483647extra") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   2147483647extra") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    2147483647000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    2147483647000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    214748364700000000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    214748364700000000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    21474836470000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    21474836470000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "   0000000000000000000000000000000000000000000000000000000000000000+1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   0000000000000000000000000000000000000000000000000000000000000000+1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -214748364800000000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -214748364800000000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -2147483648000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -2147483648000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -2147483648000000000000000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -2147483648000000000000000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "   -000000000000000000000000000000123") == -123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   -000000000000000000000000000000123") == -123: {e}')
    
    total += 1
    try:
        result = candidate(s = "    +2147483648") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    +2147483648") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    214748364700") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    214748364700") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "   +2147483647 +") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   +2147483647 +") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "   00000000000000000000000000000000000000000000000000000000000000001") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   00000000000000000000000000000000000000000000000000000000000000001") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "   +1234567890123456789012345678901234567890") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   +1234567890123456789012345678901234567890") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -214748364800000000000000000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -214748364800000000000000000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -2147483648000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -2147483648000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "   !@#$%^&*()_+") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   !@#$%^&*()_+") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "    0000+123") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    0000+123") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -21474836480000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -21474836480000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "   -1234567890123456789012345678901234567890") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   -1234567890123456789012345678901234567890") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -2147483646") == -2147483646
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -2147483646") == -2147483646: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -21474836480000000000000000000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -21474836480000000000000000000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    2147483647") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    2147483647") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    214748364700000000000000000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    214748364700000000000000000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -214748364800000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -214748364800000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "   +2147483647abc") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   +2147483647abc") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    21474836470") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    21474836470") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "  0000000000000   123abc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "  0000000000000   123abc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "    21474836470000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    21474836470000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    +123 456") == 123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    +123 456") == 123: {e}')
    
    total += 1
    try:
        result = candidate(s = "    2147483647000000000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    2147483647000000000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "   0000000000000000000000000000000000000000000000000000000000000000-1") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   0000000000000000000000000000000000000000000000000000000000000000-1") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "   ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -2147483648000000000000000000000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -2147483648000000000000000000000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "   -2147483649") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   -2147483649") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "-+12") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "-+12") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "    +2147483647") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    +2147483647") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    18446744073709551616") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    18446744073709551616") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "   +0000000000000000000000000000000000000000000123") == 123
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   +0000000000000000000000000000000000000000000123") == 123: {e}')
    
    total += 1
    try:
        result = candidate(s = "   00000000000000000000000000000000000000000000000000000000000000000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   00000000000000000000000000000000000000000000000000000000000000000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "    21474836470000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    21474836470000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    214748364700000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    214748364700000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    2147483647000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    2147483647000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "  0000000000000   -123abc") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "  0000000000000   -123abc") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "  0000000000000   -00001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "  0000000000000   -00001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "   -000") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   -000") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "    214748364700000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    214748364700000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -2147483647") == -2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -2147483647") == -2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    21474836470000000000000000000000000000") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    21474836470000000000000000000000000000") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -21474836480000000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -21474836480000000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "    -21474836480000000000000000") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "    -21474836480000000000000000") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "   -2147483648 +") == -2147483648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   -2147483648 +") == -2147483648: {e}')
    
    total += 1
    try:
        result = candidate(s = "  0000000000000   +00001") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "  0000000000000   +00001") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "   2147483647") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "   2147483647") == 2147483647: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

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


