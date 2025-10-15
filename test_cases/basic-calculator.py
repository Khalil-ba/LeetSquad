def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "30 - (5 + (10 - 15) + 20)") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "30 - (5 + (10 - 15) + 20)") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "2147483647") == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2147483647") == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "-2147483647") == -2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "-2147483647") == -2147483647: {e}')
    
    total += 1
    try:
        result = candidate(s = "- (3 + (2 - 1))") == -4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "- (3 + (2 - 1))") == -4: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 + (2 + 3) + (4 + (5 + 6))") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 + (2 + 3) + (4 + (5 + 6))") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "5 - (3 - (1 + 2))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5 - (3 - (1 + 2))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1-2+(3-(4-5)))") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1-2+(3-(4-5)))") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = " 2-1 + 2 ") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = " 2-1 + 2 ") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1+(4+5+2)-3)+(6+8)") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1+(4+5+2)-3)+(6+8)") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "- (3 + (2 - 1) )") == -4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "- (3 + (2 - 1) )") == -4: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 * 2 + 12") == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 * 2 + 12") == 114: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1+(2+(3+(4+(5+(6+(7+(8+(9+(10)))))))))") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1+(2+(3+(4+(5+(6+(7+(8+(9+(10)))))))))") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "((100 - 50) + (25 - 10))") == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((100 - 50) + (25 - 10))") == 65: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 + 2 * 6") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 + 2 * 6") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 + 20 - 5") == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 + 20 - 5") == 25: {e}')
    
    total += 1
    try:
        result = candidate(s = "- (5 - (- (1 + 1)))") == -7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "- (5 - (- (1 + 1)))") == -7: {e}')
    
    total += 1
    try:
        result = candidate(s = "-1 + (2 - (-3 + 4))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "-1 + (2 - (-3 + 4))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 + (2 - 6)") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 + (2 - 6)") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "-1 + (3-5)") == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "-1 + (3-5)") == -3: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 - (-5 + 3)") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 - (-5 + 3)") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "(123 + (456 - 789))") == -210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(123 + (456 - 789))") == -210: {e}')
    
    total += 1
    try:
        result = candidate(s = "(10 - (5 + 3))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(10 - (5 + 3))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + (2 + (3 + (4 + 5))))") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + (2 + (3 + (4 + 5))))") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 - (2 - (3 - 4))") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 - (2 - (3 - 4))") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 * ( 2 + 12 )") == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 * ( 2 + 12 )") == 114: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 + (2 - 3)") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 + (2 - 3)") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "(5 + 15) - (10 + 20)") == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(5 + 15) - (10 + 20)") == -10: {e}')
    
    total += 1
    try:
        result = candidate(s = "(123 + 456) - 789") == -210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(123 + 456) - 789") == -210: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 - (2 - (3 - (4 - (5 - (6 - (7 - (8 - 9)))))))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 - (2 - (3 - (4 - (5 - (6 - (7 - (8 - 9)))))))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "- (5 + 10 + (15 - 20))") == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "- (5 + 10 + (15 - 20))") == -10: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 - (-1)") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 - (-1)") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "((1 + 3) + (5 + 7))") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((1 + 3) + (5 + 7))") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 + 1") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 + 1") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + ((2 + 3) * (4 / 2)))") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + ((2 + 3) * (4 / 2)))") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "(100 - (50 + (25 - (12 + (6 - (3 + (1 - 1)))))))") == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(100 - (50 + (25 - (12 + (6 - (3 + (1 - 1)))))))") == 40: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 / ((5 + (5 - (5 + (5 - 5)))) * 2)") == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 / ((5 + (5 - (5 + (5 - 5)))) * 2)") == 103: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 - (5 - (3 - (2 - (1 - 0))))") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 - (5 - (3 - (2 - (1 - 0))))") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "-1 + (2 - (3 + (4 - (5 + (6 - (7 + (8 - 9)))))))") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "-1 + (2 - (3 + (4 - (5 + (6 - (7 + (8 - 9)))))))") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "5 + (8 * 3 + 9 + (3 * 5))") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5 + (8 * 3 + 9 + (3 * 5))") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "((10 + 20) * (30 / 5)) - (40 + (50 - 60))") == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((10 + 20) * (30 / 5)) - (40 + (50 - 60))") == 35: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + 2) * (3 + 4) * (5 + 6) * (7 + 8)") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + 2) * (3 + 4) * (5 + 6) * (7 + 8)") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 + (2 + (3 + (4 + (5 + (6 + (7 + (8 + (9 + 10))))))))") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 + (2 + (3 + (4 + (5 + (6 + (7 + (8 + (9 + 10))))))))") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 - (50 + ((25 * 2) - (10 + 5)))") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 - (50 + ((25 * 2) - (10 + 5)))") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "(3 + (2 * 2) - (1 + 3) + (4 - (5 + 6)))") == -4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(3 + (2 * 2) - (1 + 3) + (4 - (5 + 6)))") == -4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 - (2 - (3 - (4 - (5 - (6 - (7 - 8)))))))") == -4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 - (2 - (3 - (4 - (5 - (6 - (7 - 8)))))))") == -4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + (2 - (3 + (4 - (5 + 6)))))") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + (2 - (3 + (4 - (5 + 6)))))") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((1 + 2) + 3) + 4) + 5) + 6)") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((1 + 2) + 3) + 4) + 5) + 6)") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 + 20 * (30 + 40 / 5) + 5 * (6 + 7 * (8 + 9))") == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 + 20 * (30 + 40 / 5) + 5 * (6 + 7 * (8 + 9))") == 140: {e}')
    
    total += 1
    try:
        result = candidate(s = "(10 + 20) - (30 - 40) + (50 * 60) / (70 - 80)") == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(10 + 20) - (30 - 40) + (50 * 60) / (70 - 80)") == 140: {e}')
    
    total += 1
    try:
        result = candidate(s = "123 + (456 - 789) * (10 - 5)") == -215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123 + (456 - 789) * (10 - 5)") == -215: {e}')
    
    total += 1
    try:
        result = candidate(s = "3 * (5 + 2 * (2 + 3)) + 4 * (2 + (3 - 1))") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3 * (5 + 2 * (2 + 3)) + 4 * (2 + (3 - 1))") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "((5 - 3) * (6 + 2) - (4 + 1) * (3 - 8)) + 10") == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((5 - 3) * (6 + 2) - (4 + 1) * (3 - 8)) + 10") == -6: {e}')
    
    total += 1
    try:
        result = candidate(s = "((1 + 2) * (3 + (4 * (5 + 6))))") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((1 + 2) * (3 + (4 * (5 + 6))))") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "( 10 - ( 20 - ( 30 - ( 40 - ( 50 - 60 ) ) ) ) )") == -30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "( 10 - ( 20 - ( 30 - ( 40 - ( 50 - 60 ) ) ) ) )") == -30: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + (2 + (3 + (4 + (5 + 6)))))") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + (2 + (3 + (4 + (5 + 6)))))") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "((1 + 2) * (3 - 4) + (5 * 6) - 7)") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((1 + 2) * (3 - 4) + (5 * 6) - 7)") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 + (2 * (2 + 2) - (3 - 4) * (3 + (2 - 1)))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 + (2 * (2 + 2) - (3 - 4) * (3 + (2 - 1)))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(9 + (8 + (7 + (6 + (5 + (4 + (3 + (2 + 1))))))))") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(9 + (8 + (7 + (6 + (5 + (4 + (3 + (2 + 1))))))))") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 - (20 + (30 - (40 + (50 - 60))))") == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 - (20 + (30 - (40 + (50 - 60))))") == -10: {e}')
    
    total += 1
    try:
        result = candidate(s = "(9 - (8 + 7 - (6 + 5 - 4))) * (3 + (2 - (1 + 0 - (-1))))") == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(9 - (8 + 7 - (6 + 5 - 4))) * (3 + (2 - (1 + 0 - (-1))))") == -2: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 - (25 + 3 * (4 + 5))") == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 - (25 + 3 * (4 + 5))") == 63: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 - (50 + (25 - (10 + (5 - (2 + (1 - (0 + 1)))))))") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 - (50 + (25 - (10 + (5 - (2 + (1 - (0 + 1)))))))") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + (2 + (3 + (4 + (5 + (6 + (7 + (8 + 9))))))))") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + (2 + (3 + (4 + (5 + (6 + (7 + (8 + 9))))))))") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 + ((-200 + (300 - (400 + (500 - (600 + (700 - (800 + (900 - 1000))))))))") == -200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 + ((-200 + (300 - (400 + (500 - (600 + (700 - (800 + (900 - 1000))))))))") == -200: {e}')
    
    total += 1
    try:
        result = candidate(s = "(100 - (50 - (25 - (10 - (5 - 1)))))") == 69
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(100 - (50 - (25 - (10 - (5 - 1)))))") == 69: {e}')
    
    total += 1
    try:
        result = candidate(s = "5 + 3 * (10 - 2) / 4 - 1") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5 + 3 * (10 - 2) / 4 - 1") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 + 2 * (3 + (4 * (5 + (6 * (7 + 8)))))") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 + 2 * (3 + (4 * (5 + (6 * (7 + 8)))))") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "(9 + (8 - (7 + (6 - (5 + (4 - (3 + (2 - 1))))))))") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(9 + (8 - (7 + (6 - (5 + (4 - (3 + (2 - 1))))))))") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "( 1 + 2 ) * ( 3 + 4 ) - ( 5 + 6 ) * ( 7 + 8 )") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "( 1 + 2 ) * ( 3 + 4 ) - ( 5 + 6 ) * ( 7 + 8 )") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "(100 - 50) + ((25 * 2) - (10 + 5))") == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(100 - 50) + ((25 * 2) - (10 + 5))") == 62: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 - (20 - (30 - (40 - 50)))") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 - (20 - (30 - (40 - 50)))") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "5 + ((1 + (2 * 2) + (3 * (4 + 5))) * 6)") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5 + ((1 + (2 * 2) + (3 * (4 + 5))) * 6)") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((1 + 2) * 3) + 4) - 5) * 6) - 7") == -8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((1 + 2) * 3) + 4) - 5) * 6) - 7") == -8: {e}')
    
    total += 1
    try:
        result = candidate(s = "((2 + 3) * (5 - 1) + 7)") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((2 + 3) * (5 - 1) + 7)") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "((10 + 2) - (5 + 3) * (2 - 8)) + 4") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((10 + 2) - (5 + 3) * (2 - 8)) + 4") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "((1 + (2 + (3 + (4 + (5 + (6 + (7 + (8 + (9 + 0)))))))))") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((1 + (2 + (3 + (4 + (5 + (6 + (7 + (8 + (9 + 0)))))))))") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((10 - 2) * 3) / 2) + (((4 + 5) * 6) / 3)") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((10 - 2) * 3) / 2) + (((4 + 5) * 6) / 3)") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 - (2 + (3 - (4 + (5 - (6 + (7 - (8 + 9))))))))") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 - (2 + (3 - (4 + (5 - (6 + (7 - (8 + 9))))))))") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + (2 * (2 + 3) - 4) + 5)") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + (2 * (2 + 3) - 4) + 5)") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "((1 + 2) * (3 + 4) - 5) * 2") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((1 + 2) * (3 + 4) - 5) * 2") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "((10 + 20) - (30 + 40)) + (50 + (60 - (70 + (80 - (90 + (100 - (110 + (120 - 130))))))))") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((10 + 20) - (30 + 40)) + (50 + (60 - (70 + (80 - (90 + (100 - (110 + (120 - 130))))))))") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "((1 + 2) * (3 + 4)) - ((5 + 6) * (7 + 8))") == -16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((1 + 2) * (3 + 4)) - ((5 + 6) * (7 + 8))") == -16: {e}')
    
    total += 1
    try:
        result = candidate(s = "(2 + 6 * (25 - (3 + 3) * 2 ) ) + 5") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(2 + 6 * (25 - (3 + 3) * 2 ) ) + 5") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + (4 + (5 + (2 - 3)) - 3)) + (6 + 8)") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + (4 + (5 + (2 - 3)) - 3)) + (6 + 8)") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "((22 + (2 * (3 + 5))) - (7 + 3))") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((22 + (2 * (3 + 5))) - (7 + 3))") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + (2 - 3) * (4 + 5) - 6)") == -15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + (2 - 3) * (4 + 5) - 6)") == -15: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + (2 - (3 + (4 - (5 + (6 - (7 + (8 - 9))))))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + (2 - (3 + (4 - (5 + (6 - (7 + (8 - 9))))))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + 2) * (3 + 4) - (5 + 6) * (7 + 8) + (9 * 10)") == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + 2) * (3 + 4) - (5 + 6) * (7 + 8) + (9 * 10)") == 33: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 - (2 + (3 - (4 - (5 - 6))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 - (2 + (3 - (4 - (5 - 6))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + (2 + (3 + (4 + (5 + (6 + (7 + 8)))))))") == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + (2 + (3 + (4 + (5 + (6 + (7 + 8)))))))") == 36: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + 2) + (3 + 4) + (5 + 6) + (7 + 8) + (9 + 10)") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + 2) + (3 + 4) + (5 + 6) + (7 + 8) + (9 + 10)") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "30 - (10 + 20) + (5 * (2 + 3))") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "30 - (10 + 20) + (5 * (2 + 3))") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "(123 - (45 + (67 - (89 + 10))) + 21)") == 131
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(123 - (45 + (67 - (89 + 10))) + 21)") == 131: {e}')
    
    total += 1
    try:
        result = candidate(s = "- ( - ( - ( - ( - 1 ) ) ) )") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "- ( - ( - ( - ( - 1 ) ) ) )") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "- (3 + (4 - 5))") == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "- (3 + (4 - 5))") == -2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((((1 + 2) * 3) - 4) + 5) * (6 - (7 + 8)))") == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((((1 + 2) * 3) - 4) + 5) * (6 - (7 + 8)))") == -2: {e}')
    
    total += 1
    try:
        result = candidate(s = "3 * (2 + (1 - 5) * (3 + 7)) - 2") == -11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3 * (2 + (1 - 5) * (3 + 7)) - 2") == -11: {e}')
    
    total += 1
    try:
        result = candidate(s = "( ( 1 + 2 ) * ( 3 + 4 ) ) - ( ( 5 + 6 ) * ( 7 + 8 ) )") == -16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "( ( 1 + 2 ) * ( 3 + 4 ) ) - ( ( 5 + 6 ) * ( 7 + 8 ) )") == -16: {e}')
    
    total += 1
    try:
        result = candidate(s = "(3 * (4 - (5 + 2)) / (1 - 2))") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(3 * (4 - (5 + 2)) / (1 - 2))") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "((((-1 + 2) - 3) + 4) - 5)") == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((((-1 + 2) - 3) + 4) - 5)") == -3: {e}')
    
    total += 1
    try:
        result = candidate(s = "(12 - (4 + 3) * (2 - 1)) + 7") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(12 - (4 + 3) * (2 - 1)) + 7") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "( 123 + ( 456 - ( 789 + ( 12 - 34 ) ) ) )") == -188
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "( 123 + ( 456 - ( 789 + ( 12 - 34 ) ) ) )") == -188: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 + 20 * (30 - 20 / 2) + 5") == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 + 20 * (30 - 20 / 2) + 5") == 43: {e}')
    
    total += 1
    try:
        result = candidate(s = "((2 + 3) * (4 + 5) - 6) + 7 * (8 - 9)") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((2 + 3) * (4 + 5) - 6) + 7 * (8 - 9)") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + (2 * (2 + 3)) - (4 * (5 - 6))) + (7 * (8 - (9 + 1)))") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + (2 * (2 + 3)) - (4 * (5 - 6))) + (7 * (8 - (9 + 1)))") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((1 + 2) * 3) + ((4 + 5) * 6) + ((7 + 8) * 9))") == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((1 + 2) * 3) + ((4 + 5) * 6) + ((7 + 8) * 9))") == 45: {e}')
    
    total += 1
    try:
        result = candidate(s = "(10 + 20) - (30 + 40) + (50 - 60)") == -50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(10 + 20) - (30 + 40) + (50 - 60)") == -50: {e}')
    
    total += 1
    try:
        result = candidate(s = "(5 + (10 + (15 + (20 + (25 + (30 + (35 + (40 + (45 + 50)))))))))") == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(5 + (10 + (15 + (20 + (25 + (30 + (35 + (40 + (45 + 50)))))))))") == 275: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 - 2 * (6 / (3 + 1))") == -2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 - 2 * (6 / (3 + 1))") == -2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(10 + 2) * 6 - (3 + (4 - 5))") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(10 + 2) * 6 - (3 + (4 - 5))") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 + ( 50 - ( 25 * ( 4 + 1 ) ) ) + ( 10 - ( 2 * 3 ) )") == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 + ( 50 - ( 25 * ( 4 + 1 ) ) ) + ( 10 - ( 2 * 3 ) )") == 125: {e}')
    
    total += 1
    try:
        result = candidate(s = "((2 + 3) * (4 + 5)) - (6 * (7 + 8))") == -7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((2 + 3) * (4 + 5)) - (6 * (7 + 8))") == -7: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 - ((99 - (98 - (97 - (96 - (95 - (94 - (93 - (92 - (91 - 90)))))))))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 - ((99 - (98 - (97 - (96 - (95 - (94 - (93 - (92 - (91 - 90)))))))))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "((3 + 5) - (2 * (8 / 4)) + 1)") == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((3 + 5) - (2 * (8 / 4)) + 1)") == -5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(123 - (456 + 789) + (101 - 202))") == -1223
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(123 - (456 + 789) + (101 - 202))") == -1223: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 - ( 3 * ( 2 + 4 ) ) + 5") == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 - ( 3 * ( 2 + 4 ) ) + 5") == 96: {e}')
    
    total += 1
    try:
        result = candidate(s = "-1 + (-2 + (-3 * (-4 - (-5))))") == -7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "-1 + (-2 + (-3 * (-4 - (-5))))") == -7: {e}')
    
    total += 1
    try:
        result = candidate(s = "- ( 2 + 3 ) + ( 4 - 5 )") == -6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "- ( 2 + 3 ) + ( 4 - 5 )") == -6: {e}')
    
    total += 1
    try:
        result = candidate(s = "(100 - (50 + (25 - (10 + (5 - 2)))))") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(100 - (50 + (25 - (10 + (5 - 2)))))") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "(10 + 2 * 6) / ((5 - 3) * 2)") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(10 + 2 * 6) / ((5 - 3) * 2)") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 + (2 * (6 / 3))") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 + (2 * (6 / 3))") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "5 * (3 + (2 * (2 + (1 + (0 - (-1))))))") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "5 * (3 + (2 * (2 + (1 + (0 - (-1))))))") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 - (2 + 3) * (4 - 5) + (6 / 3)") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 - (2 + 3) * (4 - 5) + (6 / 3)") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 - (2 + (3 * (4 + (5 * (6 + (7 * (8 + (9 * (10 + 11)))))))))") == -64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 - (2 + (3 * (4 + (5 * (6 + (7 * (8 + (9 * (10 + 11)))))))))") == -64: {e}')
    
    total += 1
    try:
        result = candidate(s = "(100 - 50) - ((25 * 2) - (10 + 5))") == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(100 - 50) - ((25 * 2) - (10 + 5))") == 38: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 + (2 + (3 + (4 + (5 + 6))))") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 + (2 + (3 + (4 + (5 + 6))))") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "((22 + (2 * 3)) * (4 + 3))") == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((22 + (2 * 3)) * (4 + 3))") == 34: {e}')
    
    total += 1
    try:
        result = candidate(s = "(10 + 20) - ((30 + 40) - (50 + (60 - (70 + (80 - (90 + (100 - 110)))))))") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(10 + 20) - ((30 + 40) - (50 + (60 - (70 + (80 - (90 + (100 - 110)))))))") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "(8 - (4 + (1 - 3) + (2 - (5 + 7))))") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(8 - (4 + (1 - 3) + (2 - (5 + 7))))") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 - (25 * (2 + 3))") == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 - (25 * (2 + 3))") == 70: {e}')
    
    total += 1
    try:
        result = candidate(s = "-((1 + 2) + (3 + 4)) + ((5 + 6) + (7 + 8))") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "-((1 + 2) + (3 + 4)) + ((5 + 6) + (7 + 8))") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "(100 + 200 + (300 + (400 + (500 + (600 + (700 + (800 + 900)))))))") == 4500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(100 + 200 + (300 + (400 + (500 + (600 + (700 + (800 + 900)))))))") == 4500: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 - (9 - (8 - (7 - (6 - (5 - (4 - (3 - (2 - 1))))))))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 - (9 - (8 - (7 - (6 - (5 - (4 - (3 - (2 - 1))))))))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "100 + (200 * (300 + 400) - 500)") == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "100 + (200 * (300 + 400) - 500)") == 500: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 - (-2 - (-3 - (-4)))") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 - (-2 - (-3 - (-4)))") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 + 20 - 30 + (40 - 50)") == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 + 20 - 30 + (40 - 50)") == -10: {e}')
    
    total += 1
    try:
        result = candidate(s = "((1 + 2) * (3 - 4)) + (5 + 6)") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((1 + 2) * (3 - 4)) + (5 + 6)") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "12 - (4 * (2 + 3)) + 15") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "12 - (4 * (2 + 3)) + 15") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "3 + 5 / 2") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3 + 5 / 2") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 + (2 * (2 + 2) - (3 - 4) * 3)") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 + (2 * (2 + 2) - (3 - 4) * 3)") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(5 + 3) * (7 - (2 + 3))") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(5 + 3) * (7 - (2 + 3))") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "10 + 2 * (6 / (3 + 1)) - (8 - 4) * (2 + 1)") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "10 + 2 * (6 / (3 + 1)) - (8 - 4) * (2 + 1)") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "2 * ((3 + 4) * (5 - 6) + 7) - 8") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "2 * ((3 + 4) * (5 - 6) + 7) - 8") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + (2 * (2 + (3 * (4 + (5 * (6 + 7)))))))") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + (2 * (2 + (3 * (4 + (5 * (6 + 7)))))))") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "123 + (456 - (789 + (101 - 202) ) )") == -109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "123 + (456 - (789 + (101 - 202) ) )") == -109: {e}')
    
    total += 1
    try:
        result = candidate(s = "3 + (2 * (2 + (2 * (2 + (2 * 2)))))") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3 + (2 * (2 + (2 * (2 + (2 * 2)))))") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "-1 + (-2 + (-3 + (-4 + (-5))))") == -15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "-1 + (-2 + (-3 + (-4 + (-5))))") == -15: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((1 + 2) * (3 + 4)) - 5) * (6 + 7)") == -8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((1 + 2) * (3 + 4)) - 5) * (6 + 7)") == -8: {e}')
    
    total += 1
    try:
        result = candidate(s = "(3 + (2 * (2 + 1)))") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(3 + (2 * (2 + 1)))") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "20 * ((1 + 2) * (3 + 4) - (5 * 6)) / 10") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "20 * ((1 + 2) * (3 + 4) - (5 * 6)) / 10") == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "((100 - (50 + (25 - (10 + (5 - (2 + (1 - 0))))))) + (10 - 5))") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((100 - (50 + (25 - (10 + (5 - (2 + (1 - 0))))))) + (10 - 5))") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "(5 - 3) * (10 - (4 + 2) * (3 - 1))") == -4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(5 - 3) * (10 - (4 + 2) * (3 - 1))") == -4: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + 2) * 3 - 4 * (5 + 6)") == -9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + 2) * 3 - 4 * (5 + 6)") == -9: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 - (2 + (3 - (4 + (5 - 6)))))") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 - (2 + (3 - (4 + (5 - 6)))))") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 - (2 - (3 - (4 - (5 - (6 - (7 - (8 - 9)))))))") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 - (2 - (3 - (4 - (5 - (6 - (7 - (8 - 9)))))))") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(3 - 4) * (5 - (6 - (7 - (8 - (9 - 10)))))") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(3 - 4) * (5 - (6 - (7 - (8 - (9 - 10)))))") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(10 + ((20 + 30) - (40 + (50 - (60 + (70 - 80))))))") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(10 + ((20 + 30) - (40 + (50 - (60 + (70 - 80))))))") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((1 + 2) * (3 + 4)) - (5 + 6)) * (7 - (8 + 9))") == -11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((1 + 2) * (3 + 4)) - (5 + 6)) * (7 - (8 + 9))") == -11: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + (2 * (3 + (4 * (5 + (6 * (7 + (8 * (9 + 10))))))))") == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + (2 * (3 + (4 * (5 + (6 * (7 + (8 * (9 + 10))))))))") == 55: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 + (2 - (3 + (4 - (5 + (6 - (7 + (8 - 9)))))))") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 + (2 - (3 + (4 - (5 + (6 - (7 + (8 - 9)))))))") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "(3 * (5 - (2 + 1)) + 4) - (6 * (8 - (7 + 1)))") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(3 * (5 - (2 + 1)) + 4) - (6 * (8 - (7 + 1)))") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "((1 + 2) * (3 + 4) - (5 + 6)) * (7 + 8) - (9 + 10)") == -5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((1 + 2) * (3 + 4) - (5 + 6)) * (7 + 8) - (9 + 10)") == -5: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + 2) * (3 - 4) * (5 + 6) * (7 - 8)") == -10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + 2) * (3 - 4) * (5 + 6) * (7 - 8)") == -10: {e}')
    
    total += 1
    try:
        result = candidate(s = "1 + 2 - 3 * (4 - 5) / (6 - 7) + 8") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1 + 2 - 3 * (4 - 5) / (6 - 7) + 8") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + (2 * 3)) - (4 + (5 * 6))") == -9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + (2 * 3)) - (4 + (5 * 6))") == -9: {e}')
    
    total += 1
    try:
        result = candidate(s = "(((3 + 2) * (4 + 5)) - (6 + (7 * 8) - 9)) + 10") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(((3 + 2) * (4 + 5)) - (6 + (7 * 8) - 9)) + 10") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "(100 - (50 + 25 - (10 * 2 + 5)) + 15)") == 57
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(100 - (50 + 25 - (10 * 2 + 5)) + 15)") == 57: {e}')
    
    total += 1
    try:
        result = candidate(s = "1000 + (2000 - (3000 - (4000 - (5000 - (6000 - (7000 - 8000))))))") == 6000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "1000 + (2000 - (3000 - (4000 - (5000 - (6000 - (7000 - 8000))))))") == 6000: {e}')
    
    total += 1
    try:
        result = candidate(s = "( ( ( 1 + 2 ) * 3 ) - ( 4 + 5 ) )") == -3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "( ( ( 1 + 2 ) * 3 ) - ( 4 + 5 ) )") == -3: {e}')
    
    total += 1
    try:
        result = candidate(s = "(1 + (2 * (3 + (4 * (5 + 6))))) - (7 + (8 * (9 + 10)))") == -13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(1 + (2 * (3 + (4 * (5 + 6))))) - (7 + (8 * (9 + 10)))") == -13: {e}')
    
    total += 1
    try:
        result = candidate(s = "((1 + 2) * (3 + 4) - (5 * 6))") == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "((1 + 2) * (3 + 4) - (5 * 6))") == -1: {e}')
    
    total += 1
    try:
        result = candidate(s = "(10 - 5) + (3 * 2) + (8 / 4)") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(10 - 5) + (3 * 2) + (8 / 4)") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "3 + 5 * ( 2 - 8 )") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "3 + 5 * ( 2 - 8 )") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "(3 - (5 - (7 - (9 - (11 - (13 - (15 - 17))))))") == -8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "(3 - (5 - (7 - (9 - (11 - (13 - (15 - 17))))))") == -8: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

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


