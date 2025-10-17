def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 100) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 4) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 20) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1111111) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111111) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 19) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 19) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 7) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 489) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 489) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 789789789) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 789789789) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 130) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 130) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 49) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2147483647) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2147483647) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 32442) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32442) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 324) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 324) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 203) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 203) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 82) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 82) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 70) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 70) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 2736895) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2736895) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 44) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 44) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 190) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 190) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 58) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 58) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 28) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 289) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 289) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 444444444) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 444444444) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 14659) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14659) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 6892) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6892) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 3249671058) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3249671058) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 145) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 145) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 14657) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 14657) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 23) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 784) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 784) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 133) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 133) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 999) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 89) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 89) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 9474) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9474) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 404) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 404) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 442) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 442) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567890) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567890) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 139) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 139) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000007) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000007) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 13441) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13441) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 200) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 8989898989) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8989898989) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 3249) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3249) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 370) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 370) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 789999) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 789999) == False: {e}')
    
    total += 1
    try:
        result = candidate(n = 1111111111) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111111111) == True: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 100) == True
    assert candidate(n = 4) == False
    assert candidate(n = 20) == False
    assert candidate(n = 2) == False
    assert candidate(n = 1111111) == True
    assert candidate(n = 19) == True
    assert candidate(n = 1) == True
    assert candidate(n = 1000000000) == True
    assert candidate(n = 7) == True
    assert candidate(n = 489) == False
    assert candidate(n = 789789789) == False
    assert candidate(n = 130) == True
    assert candidate(n = 49) == True
    assert candidate(n = 2147483647) == False
    assert candidate(n = 32442) == True
    assert candidate(n = 324) == False
    assert candidate(n = 203) == True
    assert candidate(n = 82) == True
    assert candidate(n = 70) == True
    assert candidate(n = 2736895) == False
    assert candidate(n = 1000) == True
    assert candidate(n = 44) == True
    assert candidate(n = 190) == True
    assert candidate(n = 58) == False
    assert candidate(n = 28) == True
    assert candidate(n = 289) == False
    assert candidate(n = 444444444) == False
    assert candidate(n = 14659) == False
    assert candidate(n = 6892) == False
    assert candidate(n = 3249671058) == False
    assert candidate(n = 145) == False
    assert candidate(n = 14657) == False
    assert candidate(n = 10000) == True
    assert candidate(n = 23) == True
    assert candidate(n = 784) == True
    assert candidate(n = 133) == True
    assert candidate(n = 999) == False
    assert candidate(n = 89) == False
    assert candidate(n = 9474) == False
    assert candidate(n = 111111111) == False
    assert candidate(n = 404) == True
    assert candidate(n = 442) == False
    assert candidate(n = 987654321) == False
    assert candidate(n = 1234567890) == False
    assert candidate(n = 139) == True
    assert candidate(n = 1000000007) == False
    assert candidate(n = 13441) == False
    assert candidate(n = 200) == False
    assert candidate(n = 8989898989) == False
    assert candidate(n = 3249) == False
    assert candidate(n = 123456789) == False
    assert candidate(n = 370) == False
    assert candidate(n = 789999) == False
    assert candidate(n = 1111111111) == True
    assert candidate(n = 100000000) == True


