def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQWWWWEEEEEEEERRRRRRRR") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQWWWWEEEEEEEERRRRRRRR") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWWER") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWWER") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "WQQQQQERQQ") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "WQQQQQERQQ") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "WWEERRQQQWEEERRQQQWEEERRQQQWEEERR") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "WWEERRQQQWEEERRQQQWEEERRQQQWEEERR") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQWQWQQWEEWEEWRRWRRWRRW") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQWQWQQWEEWEEWRRWRRWRRW") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWWWWEEEERRRR") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWWWWEEEERRRR") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "WQWRQQQWQWQQQQRRWEWRRWQQQWQRWEQWQWRRRRWQQQWRRQWEQWQQWRWRRWQQWEWRRQWQWQWQWQW") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "WQWRQQQWQWQQQQRRWEWRRWQQQWQRWEQWQWRRRRWQQQWRRQWEQWQQWRWRRWQQWEWRRQWQWQWQWQW") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQWWRRER") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQWWRRER") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWWWEERRR") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWWWEERRR") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEERRRRRRRR") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEERRRRRRRR") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEERRRQQQWEEERRR") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEERRRQQQWEEERRR") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "QWERQWERQWERQWER") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QWERQWERQWERQWER") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEEERRRQ") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEEERRRQ") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQWE") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQWE") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQW") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQW") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQWEQRQQQQEEEEWWRR") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQWEQRQQQQEEEEWWRR") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "QWER") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QWER") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQEEEERRRR") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQEEEERRRR") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "WQEEWRQQQWEEEERRR") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "WQEEWRQQQWEEEERRR") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQWWEERRRR") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQWWEERRRR") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "WQWRQQQW") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "WQWRQQQW") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEWWRR") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEWWRR") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "QWQWQWQW") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QWQWQWQW") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQEEEEWWWWRRRR") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQEEEEWWWWRRRR") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWWEERR") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWWEERR") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEERRR") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEERRR") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWWRRRRWWRRRQQQ") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWWRRRRWWRRRQQQ") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWWEERRRRQQQQ") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWWEERRRRQQQQ") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEEERRRR") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEEERRRR") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQQQWWWWWWWWQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRR") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQQQWWWWWWWWQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRR") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQWWEERRRRQQWWEERRRRQQWWEERRRR") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQWWEERRRRQQWWEERRRRQQWWEERRRR") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWWWEEERRRR") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWWWEEERRRR") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEEQQQQRRRRWWWWEEEEQQQQ") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEEQQQQRRRRWWWWEEEEQQQQ") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 42: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWWEERRQQWWEERRQQWWEERRQQWWEERR") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWWEERRQQWWEERRQQWWEERRQQWWEERR") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEEEERRRRQQQ") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEEEERRRRQQQ") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEEEERRRRRRRRRRRRRRRRRRRR") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEEEERRRRRRRRRRRRRRRRRRRR") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEEERRRRQQ") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEEERRRRQQ") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQWWEERRRQQ") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQWWEERRRQQ") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 87: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQ") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQ") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "QWEQRWEQRWEQRWEQWEQRWEQRWEQRWE") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QWEQRWEQRWEQRWEQWEQRWEQRWEQRWE") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQWWEERRQQWWEERRQQWWEERR") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQWWEERRQQWWEERRQQWWEERR") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQQQWWWWWWWWWWEEEEEEEEEEERRRRRRRRRR") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQQQWWWWWWWWWWEEEEEEEEEEERRRRRRRRRR") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQWEEEEERRRRR") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQWEEEEERRRRR") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEERRRR") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEERRRR") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "WWWWWWWWQQQQEEEERRRR") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "WWWWWWWWQQQQEEEERRRR") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQQQWWWWWWWWWWWEEEEEEEEEEEERRRRRRRRRRRRRRRR") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQQQWWWWWWWWWWWEEEEEEEEEEEERRRRRRRRRRRRRRRR") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "QWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQW") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQW") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "EEEEWWRRQQQQEEEEWWRRQQQQ") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "EEEEWWRRQQQQEEEEWWRRQQQQ") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWW") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWW") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWWWWEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRR") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWWWWEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRR") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEEEERRRRWWW") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEEEERRRRWWW") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "EEEEEEEEWWWWWWWWRRRRRRRRQQQQQQQQ") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "EEEEEEEEWWWWWWWWRRRRRRRRQQQQQQQQ") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEE") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEE") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWW") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWW") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "WWWWWWWWWWEEEEEEEEQQQQQQQQQQRRRRRRRRRR") == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "WWWWWWWWWWEEEEEEEEQQQQQQQQQQRRRRRRRRRR") == 20: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEEQQQQ") == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEEQQQQ") == 13: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEEERRRRRRRRR") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEEERRRRRRRRR") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "QWQWQWQWQWQWQWQW") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QWQWQWQWQWQWQWQW") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERR") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERR") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEERRRRRRRRRRRR") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEERRRRRRRRRRRR") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQWWEERRRRWWWWRRRRQQQQQQWWEERRRRWWWWRRRRQQQQQQWWEERRRRWWWWRRRR") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQWWEERRRRWWWWRRRRQQQQQQWWEERRRRWWWWRRRRQQQQQQWWEERRRRWWWWRRRR") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQQQQQQQEEEEWWRR") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQQQQQQQEEEEWWRR") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQWWWWWWWWWEEEEEEEEEEEEEEEEERRRRRRRRRRRRRR") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQWWWWWWWWWEEEEEEEEEEEEEEEEERRRRRRRRRRRRRR") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQ") == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQ") == 15: {e}')
    
    total += 1
    try:
        result = candidate(s = "QWEQQWEQQWEQQWEQQWEQQWEQQWEQQWE") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QWEQQWEQQWEQQWEQQWEQQWEQQWEQQWE") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQQQWWWWWWWWWWEEEEEEEEERRRRRRRRRR") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQQQWWWWWWWWWWEEEEEEEEERRRRRRRRRR") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRR") == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRR") == 32: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEERRRRRRRRRRRRRRRRRRRR") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEERRRRRRRRRRRRRRRRRRRR") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEEEEEERRRR") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEEEEEERRRR") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQWWWWWWWWQQQQQQQQWWWWWWWWQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQWWWWWWWWQQQQQQQQWWWWWWWWQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQWWEERRRRWWWWRRRRWWWWRRRRWWWWRRRR") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQWWEERRRRWWWWRRRRWWWWRRRRWWWWRRRR") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "WWWWQQQEEEERRR") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "WWWWQQQEEEERRR") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQQQQQQQQQWWWWWWWWWWWWWWWWEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRR") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQQQQQQQQQWWWWWWWWWWWWWWWWEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRR") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQWEEEEERRRRRR") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQWEEEEERRRRRR") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWWEERRRRQQQWWEERRRR") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWWEERRRRQQQWWEERRRR") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQWWWEEEEEEEEEERRRRRRRR") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQWWWEEEEEEEEEERRRRRRRR") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "WWWWWQQQQQQQQQQQQQQQQQQEEEERRRRRRRRRRRRRRRRRRRRRRRR") == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "WWWWWQQQQQQQQQQQQQQQQQQEEEERRRRRRRRRRRRRRRRRRRRRRRR") == 22: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWW") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWW") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWWWWWWWWEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRR") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWWWWWWWWEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRR") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQWWEERRRRWWWWRRRRWWWWRRRRWWWWRRRRQQQWEEERRRRWWWWRRRR") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQWWEERRRRWWWWRRRRWWWWRRRRWWWWRRRRQQQWEEERRRRWWWWRRRR") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "WQQQWEWQERWREWER") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "WQQQWEWQERWREWER") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "QWQWQWQWQQQQQQQQEEEEWWRRQQQQ") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QWQWQWQWQQQQQQQQEEEEWWRRQQQQ") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQQQQQQQQQWWEERRRRRRRRRRRRRR") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQQQQQQQQQWWEERRRRRRRRRRRRRR") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 23: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQWEEEEEEEEEERRRRRRRRR") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQWEEEEEEEEEERRRRRRRRR") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQWWEEEERRRR") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQWWEEEERRRR") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEERRRRRR") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEERRRRRR") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 102: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWWEEREEE") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWWEEREEE") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQWWEERRQQWWEERR") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQWWEERRQQWWEERR") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWWWWWEEEEERRRRRQQQWWWWWEEEEERRRRRQQQWWWWWEEEEERRRRR") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWWWWWEEEEERRRRRQQQWWWWWEEEEERRRRRQQQWWWWWEEEEERRRRR") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWWWWEEEERRRRQQQQWWWWEEEE") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWWWWEEEERRRRQQQQWWWWEEEE") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWWEERRRRQQQQWWEERRRRQQQQWWEERRRR") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWWEERRRRQQQQWWEERRRRQQQQWWEERRRR") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "QWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQW") == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQW") == 18: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEERRRRRRRRRRRRRRRRRR") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEERRRRRRRRRRRRRRRRRR") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEEERRRRQQQWEEEERRRR") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEEERRRRQQQWEEEERRRR") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQQQQQQQEEEEWWRRQQQQQQQQQQQQ") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQQQQQQQEEEEWWRRQQQQQQQQQQQQ") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEERRRRWWWWQQQQWEEEERRRRWWWW") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEERRRRWWWWQQQQWEEEERRRRWWWW") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWQQQQQQQQQQEEEEWWRRQQQQ") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWQQQQQQQQQQEEEEWWRRQQQQ") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWWWWWWWWEEEEERRRRRRRR") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWWWWWWWWEEEEERRRRRRRR") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEERQQQWEEERRQQQWEEERRQQQWEEERR") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEERQQQWEEERRQQQWEEERRQQQWEEERR") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQWEEEEEEEEEEEEEERRRRRRRRRRRR") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQWEEEEEEEEEEEEEERRRRRRRRRRRR") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERR") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERR") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEERRQQQWEEERRQQQWEEERRQQQWEEEERR") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEERRQQQWEEERRQQQWEEERRQQQWEEEERR") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRR") == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRR") == 26: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQQQQQWWWWWWWWWWWWEEEEEEEEEEEEERRRRRRRRRRRR") == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQQQQQWWWWWWWWWWWWEEEEEEEEEEEEERRRRRRRRRRRR") == 1: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRR") == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRR") == 24: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRR") == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRR") == 14: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEEQQQQRRRR") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEEQQQQRRRR") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEERRRRRRRRR") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEERRRRRRRRR") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQWWEERRRRRR") == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQWWEERRRRRR") == 10: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWQWQWQWQWQWQWQWQWQWQWQWQWQW") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWQWQWQWQWQWQWQWQWQWQWQWQWQW") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWWEERRRRQQQQWWEERRRR") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWWEERRRRQQQQWWEERRRR") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "WQQQWQQQWQQQWQQQEEEEWWRRQQQQ") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "WQQQWQQQWQQQWQQQEEEEWWRRQQQQ") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEEERRRRRR") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEEERRRRRR") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 31: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEEEEERRRR") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEEEEERRRR") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQWEEEEEEEEEEEEERRRRRRRRRR") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQWEEEEEEEEEEEEERRRRRRRRRR") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEEQQQQRRRRWWWWEEEE") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEEQQQQRRRRWWWWEEEE") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEEEWWRRQQQQEEEEWWRR") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEEEWWRRQQQQEEEEWWRR") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "QWQWQWQWQWQWQQQQWWRRQQQQ") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QWQWQWQWQWQWQQQQWWRRQQQQ") == 12: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQWWWWWWEEEEEEEEEERRRRRRRRRRRRRR") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQWWWWWWEEEEEEEEEERRRRRRRRRRRRRR") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWQQQQWQQQQEEEEWWRRQQQQEEEEWWRR") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWQQQQWQQQQEEEEWWRRQQQQEEEEWWRR") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQWEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRR") == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQWEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRR") == 17: {e}')
    
    total += 1
    try:
        result = candidate(s = "WWWWQQQEEERRRR") == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "WWWWQQQEEERRRR") == 8: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEEQQQQRRRRWWWWEEEEQQQQRRRR") == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEEQQQQRRRRWWWWEEEEQQQQRRRR") == 11: {e}')
    
    total += 1
    try:
        result = candidate(s = "QWQQQQQQQQQWEWEWEWRR") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QWQQQQQQQQQWEWEWEWRR") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEEERRR") == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEEERRR") == 7: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 68: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWWEERQQRRQWRE") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWWEERQQRRQWRE") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQEEEEWWRR") == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQEEEEWWRR") == 2: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 30: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERR") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERR") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 28: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWWEERRRRQQQQWWEERRRR") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWWEERRRRQQQQWWEERRRR") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQWWWEEEEERRRR") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQWWWEEEEERRRR") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWWEERRRRQQQQWWEERRRRQQQQWWEERRRR") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWWEERRRRQQQQWWEERRRRQQQQWWEERRRR") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEEEERRRRR") == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEEEERRRRR") == 3: {e}')
    
    total += 1
    try:
        result = candidate(s = "WQWRQQQQEERRRR") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "WQWRQQQQEERRRR") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQWWWWWWWWWWWWWWWWWWEEEEEERRRR") == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQWWWWWWWWWWWWWWWWWWEEEEEERRRR") == 9: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEEQQQQRRRRWWWW") == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEEQQQQRRRRWWWW") == 5: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEEEEERRRRQQ") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEEEEERRRRQQ") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEERRRRRRRRRR") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEERRRRRRRRRR") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "RRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEE") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "RRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEE") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQWWWWQQQQWWWWEEEEEEEEEEEEEEEERRRRRRRRRRRRRR") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQWWWWQQQQWWWWEEEEEEEEEEEEEEEERRRRRRRRRRRRRR") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQWWEERRRRWWWWRRRRQQQWEEERRRRWWWWRRRRQQQWEEERRRRWWWWRRRR") == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQWWEERRRRWWWWRRRRQQQWEEERRRRWWWWRRRRQQQWEEERRRRWWWWRRRR") == 21: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQWWWWWWEEEERRRRRRRRRRRR") == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQWWWWWWEEEERRRRRRRRRRRR") == 16: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQWWEERRRRWWWWRRRRWWWWRRRRWWWWRRRRQQWWEERRRRWWWWRRRR") == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQWWEERRRRWWWWRRRRWWWWRRRRWWWWRRRRQQWWEERRRRWWWWRRRR") == 19: {e}')
    
    total += 1
    try:
        result = candidate(s = "WWWWQQQQEEEERRRRWWWWQQQQEEEERRRR") == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "WWWWQQQQEEEERRRRWWWWQQQQEEEERRRR") == 0: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQQQQQQWWEERRRR") == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQQQQQQWWEERRRR") == 4: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQWWEERRWWEERRWWEERRWWEERR") == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQWWEERRWWEERRWWEERRWWEERR") == 6: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQWWEERRRRWWWWRRRRQQQWEEERRRRWWWWRRRRQQQWEEERRRRWWWWRRRRQQQWEEERRRRWWWWRRRR") == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQWWEERRRRWWWWRRRRQQQWEEERRRRWWWWRRRRQQQWEEERRRRWWWWRRRRQQQWEEERRRRWWWWRRRR") == 29: {e}')
    
    total += 1
    try:
        result = candidate(s = "QQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERR") == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(s = "QQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERR") == 12: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(s = "QQQQQQQQWWWWEEEEEEEERRRRRRRR") == 14
    assert candidate(s = "QQQQWWER") == 2
    assert candidate(s = "WQQQQQERQQ") == 5
    assert candidate(s = "WWEERRQQQWEEERRQQQWEEERRQQQWEEERR") == 5
    assert candidate(s = "QQWQWQQWEEWEEWRRWRRWRRW") == 7
    assert candidate(s = "QQQQWWWWEEEERRRR") == 0
    assert candidate(s = "WQWRQQQWQWQQQQRRWEWRRWQQQWQRWEQWQWRRRRWQQQWRRQWEQWQQWRWRRWQQWEWRRQWQWQWQWQW") == 24
    assert candidate(s = "QQWWRRER") == 1
    assert candidate(s = "QQQQWWWEERRR") == 1
    assert candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEERRRRRRRR") == 0
    assert candidate(s = "QQQWEEERRRQQQWEEERRR") == 5
    assert candidate(s = "QWERQWERQWERQWER") == 0
    assert candidate(s = "QQQWEEEERRRQ") == 3
    assert candidate(s = "QQWE") == 1
    assert candidate(s = "QQQW") == 2
    assert candidate(s = "QQWEQRQQQQEEEEWWRR") == 4
    assert candidate(s = "QWER") == 0
    assert candidate(s = "QQQQEEEERRRR") == 6
    assert candidate(s = "WQEEWRQQQWEEEERRR") == 2
    assert candidate(s = "QQWWEERRRR") == 2
    assert candidate(s = "WQWRQQQW") == 3
    assert candidate(s = "QQQQWEEEWWRR") == 1
    assert candidate(s = "QWQWQWQW") == 4
    assert candidate(s = "QQQQEEEEWWWWRRRR") == 0
    assert candidate(s = "QQQQWWEERR") == 2
    assert candidate(s = "QQQQWEEEERRR") == 3
    assert candidate(s = "QQQQWWRRRRWWRRRQQQ") == 6
    assert candidate(s = "QQQQWWEERRRRQQQQ") == 4
    assert candidate(s = "QQQWEEEERRRR") == 2
    assert candidate(s = "QQQQQQQQQQWWWWWWWWQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRR") == 4
    assert candidate(s = "QQWWEERRRRQQWWEERRRRQQWWEERRRR") == 11
    assert candidate(s = "QQQQWWWEEERRRR") == 8
    assert candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEEQQQQRRRRWWWWEEEEQQQQ") == 13
    assert candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 42
    assert candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 32
    assert candidate(s = "QQQQWWEERRQQWWEERRQQWWEERRQQWWEERR") == 2
    assert candidate(s = "QQQQWEEEEEERRRRQQQ") == 6
    assert candidate(s = "QQQWEEEEERRRRRRRRRRRRRRRRRRRR") == 13
    assert candidate(s = "QQQWEEEERRRRQQ") == 7
    assert candidate(s = "QQQQQWWEERRRQQ") == 4
    assert candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 87
    assert candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQ") == 6
    assert candidate(s = "QWEQRWEQRWEQRWEQWEQRWEQRWEQRWE") == 3
    assert candidate(s = "QQWWEERRQQWWEERRQQWWEERR") == 0
    assert candidate(s = "QQQQQQQQQQWWWWWWWWWWEEEEEEEEEEERRRRRRRRRR") == 1
    assert candidate(s = "QQQQQWEEEEERRRRR") == 8
    assert candidate(s = "QQQQWEEEERRRR") == 7
    assert candidate(s = "WWWWWWWWQQQQEEEERRRR") == 3
    assert candidate(s = "QQQQQQQQQQWWWWWWWWWWWEEEEEEEEEEEERRRRRRRRRRRRRRRR") == 4
    assert candidate(s = "QWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQW") == 16
    assert candidate(s = "EEEEWWRRQQQQEEEEWWRRQQQQ") == 4
    assert candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWW") == 5
    assert candidate(s = "QQQQWWWWEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRR") == 14
    assert candidate(s = "QQQQWEEEEEERRRRWWW") == 2
    assert candidate(s = "EEEEEEEEWWWWWWWWRRRRRRRRQQQQQQQQ") == 0
    assert candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEE") == 8
    assert candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWW") == 4
    assert candidate(s = "WWWWWWWWWWEEEEEEEEQQQQQQQQQQRRRRRRRRRR") == 20
    assert candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEEQQQQ") == 13
    assert candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEEERRRRRRRRR") == 2
    assert candidate(s = "QWQWQWQWQWQWQWQW") == 8
    assert candidate(s = "QQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERR") == 14
    assert candidate(s = "QQQQWEEEERRRRRRRRRRRR") == 7
    assert candidate(s = "QQQQQQWWEERRRRWWWWRRRRQQQQQQWWEERRRRWWWWRRRRQQQQQQWWEERRRRWWWWRRRR") == 14
    assert candidate(s = "QQQQQQQQQQQQQQEEEEWWRR") == 9
    assert candidate(s = "QQQQQQQQWWWWWWWWWEEEEEEEEEEEEEEEEERRRRRRRRRRRRRR") == 7
    assert candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQ") == 15
    assert candidate(s = "QWEQQWEQQWEQQWEQQWEQQWEQQWEQQWE") == 14
    assert candidate(s = "QQQQQQQQQQWWWWWWWWWWEEEEEEEEERRRRRRRRRR") == 21
    assert candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRR") == 32
    assert candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEERRRRRRRRRRRRRRRRRRRR") == 9
    assert candidate(s = "QQQWEEEEEEERRRR") == 5
    assert candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 31
    assert candidate(s = "QQQQQQQQWWWWWWWWQQQQQQQQWWWWWWWWQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 10
    assert candidate(s = "QQWWEERRRRWWWWRRRRWWWWRRRRWWWWRRRR") == 14
    assert candidate(s = "WWWWQQQEEEERRR") == 5
    assert candidate(s = "QQQQQQQQQQQQQQQQWWWWWWWWWWWWWWWWEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRR") == 5
    assert candidate(s = "QQQQQWEEEEERRRRRR") == 9
    assert candidate(s = "QQQQWWEERRRRQQQWWEERRRR") == 5
    assert candidate(s = "QQQQQQWWWEEEEEEEEEERRRRRRRR") == 6
    assert candidate(s = "WWWWWQQQQQQQQQQQQQQQQQQEEEERRRRRRRRRRRRRRRRRRRRRRRR") == 22
    assert candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWW") == 4
    assert candidate(s = "QQQWWWWWWWWEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRR") == 11
    assert candidate(s = "QQWWEERRRRWWWWRRRRWWWWRRRRWWWWRRRRQQQWEEERRRRWWWWRRRR") == 19
    assert candidate(s = "WQQQWEWQERWREWER") == 1
    assert candidate(s = "QWQWQWQWQQQQQQQQEEEEWWRRQQQQ") == 10
    assert candidate(s = "QQQQQQQQQQQQQQQQWWEERRRRRRRRRRRRRR") == 18
    assert candidate(s = "QQQWEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 23
    assert candidate(s = "QQQQQQQQWEEEEEEEEEERRRRRRRRR") == 14
    assert candidate(s = "QQQQQQWWEEEERRRR") == 2
    assert candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEERRRRRR") == 10
    assert candidate(s = "QQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 102
    assert candidate(s = "QQQQWWEEREEE") == 5
    assert candidate(s = "QQWWEERRQQWWEERR") == 0
    assert candidate(s = "QQQWWWWWEEEEERRRRRQQQWWWWWEEEEERRRRRQQQWWWWWEEEEERRRRR") == 9
    assert candidate(s = "QQQQWWWWEEEERRRRQQQQWWWWEEEE") == 6
    assert candidate(s = "QQQWWEERRRRQQQQWWEERRRRQQQQWWEERRRR") == 7
    assert candidate(s = "QWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQWQW") == 18
    assert candidate(s = "QQQWEEERRRRRRRRRRRRRRRRRR") == 12
    assert candidate(s = "QQQWEEEERRRRQQQWEEEERRRR") == 4
    assert candidate(s = "QQQQQQQQQQQQQQEEEEWWRRQQQQQQQQQQQQ") == 26
    assert candidate(s = "QQQQWEEEERRRRWWWWQQQQWEEEERRRRWWWW") == 2
    assert candidate(s = "QQQWQQQQQQQQQQEEEEWWRRQQQQ") == 12
    assert candidate(s = "QQQQWWWWWWWWEEEEERRRRRRRR") == 9
    assert candidate(s = "QQQWEEERQQQWEEERRQQQWEEERRQQQWEEERR") == 11
    assert candidate(s = "QQQQQQQQWEEEEEEEEEEEEEERRRRRRRRRRRR") == 10
    assert candidate(s = "QQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERR") == 16
    assert candidate(s = "QQQWEEERRQQQWEEERRQQQWEEERRQQQWEEEERR") == 8
    assert candidate(s = "QQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRR") == 26
    assert candidate(s = "QQQQQQQQQQQQWWWWWWWWWWWWEEEEEEEEEEEEERRRRRRRRRRRR") == 1
    assert candidate(s = "QQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRRQQQWEEERRRR") == 24
    assert candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 31
    assert candidate(s = "QQQQQQQQEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRR") == 14
    assert candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEEQQQQRRRR") == 11
    assert candidate(s = "QQQQWEEEERRRRRRRRR") == 5
    assert candidate(s = "QQQQQQQQWWEERRRRRR") == 10
    assert candidate(s = "QQQWQWQWQWQWQWQWQWQWQWQWQWQWQW") == 16
    assert candidate(s = "QQQWWEERRRRQQQQWWEERRRR") == 5
    assert candidate(s = "WQQQWQQQWQQQWQQQEEEEWWRRQQQQ") == 11
    assert candidate(s = "QQQWEEEERRRRRR") == 4
    assert candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 31
    assert candidate(s = "QQQWEEEEEERRRR") == 4
    assert candidate(s = "QQQQQQWEEEEEEEEEEEEERRRRRRRRRR") == 9
    assert candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEEQQQQRRRRWWWWEEEE") == 7
    assert candidate(s = "QQQWEEEEWWRRQQQQEEEEWWRR") == 3
    assert candidate(s = "QWQWQWQWQWQWQQQQWWRRQQQQ") == 12
    assert candidate(s = "QQQQQQWWWWWWEEEEEEEEEERRRRRRRRRRRRRR") == 6
    assert candidate(s = "QQQQWQQQQWQQQQEEEEWWRRQQQQEEEEWWRR") == 9
    assert candidate(s = "QQQQQQQWEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRR") == 17
    assert candidate(s = "WWWWQQQEEERRRR") == 8
    assert candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEEQQQQRRRRWWWWEEEEQQQQRRRR") == 11
    assert candidate(s = "QWQQQQQQQQQWEWEWEWRR") == 5
    assert candidate(s = "QQQWEEEERRR") == 7
    assert candidate(s = "QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 68
    assert candidate(s = "QQQWWEERQQRRQWRE") == 2
    assert candidate(s = "QQQQEEEEWWRR") == 2
    assert candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 30
    assert candidate(s = "QQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERR") == 16
    assert candidate(s = "QQQQQQQQQQQQQQQQEEEEEEEERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR") == 28
    assert candidate(s = "QQQQWWEERRRRQQQQWWEERRRR") == 4
    assert candidate(s = "QQQQQQWWWEEEEERRRR") == 6
    assert candidate(s = "QQQQWWEERRRRQQQQWWEERRRRQQQQWWEERRRR") == 6
    assert candidate(s = "QQQQWEEEEEERRRRR") == 3
    assert candidate(s = "WQWRQQQQEERRRR") == 6
    assert candidate(s = "QQQQQQQQWWWWWWWWWWWWWWWWWWEEEEEERRRR") == 9
    assert candidate(s = "QQQQWEEEEEERRRRQQQWEEEERRRRWWWWQQQQQQQQWWWWEEEEQQQQRRRRWWWW") == 5
    assert candidate(s = "QQQWEEEEEERRRRQQ") == 4
    assert candidate(s = "QQQWEEERRRRRRRRRR") == 6
    assert candidate(s = "RRRRRRRRQQQQQQQQWWWWWWWWEEEEEEEE") == 0
    assert candidate(s = "QQQQQQQQWWWWQQQQWWWWEEEEEEEEEEEEEEEERRRRRRRRRRRRRR") == 6
    assert candidate(s = "QQWWEERRRRWWWWRRRRQQQWEEERRRRWWWWRRRRQQQWEEERRRRWWWWRRRR") == 21
    assert candidate(s = "QQQQQQQQWWWWWWEEEERRRRRRRRRRRR") == 16
    assert candidate(s = "QQWWEERRRRWWWWRRRRWWWWRRRRWWWWRRRRQQWWEERRRRWWWWRRRR") == 19
    assert candidate(s = "WWWWQQQQEEEERRRRWWWWQQQQEEEERRRR") == 0
    assert candidate(s = "QQQQQQQQWWEERRRR") == 4
    assert candidate(s = "QQWWEERRWWEERRWWEERRWWEERR") == 6
    assert candidate(s = "QQWWEERRRRWWWWRRRRQQQWEEERRRRWWWWRRRRQQQWEEERRRRWWWWRRRRQQQWEEERRRRWWWWRRRR") == 29
    assert candidate(s = "QQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERRQQQWEEERR") == 12


