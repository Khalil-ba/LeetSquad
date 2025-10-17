def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(low = 3,high = 7) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 3,high = 7) == 3: {e}')
    
    total += 1
    try:
        result = candidate(low = 0,high = 1000000000) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 0,high = 1000000000) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(low = 0,high = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 0,high = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 500000000,high = 500000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 500000000,high = 500000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 1000000000) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 1000000000) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(low = 8,high = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 8,high = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000000000,high = 1000000000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000000000,high = 1000000000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 2,high = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 2,high = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 0,high = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 0,high = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 2,high = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 2,high = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 450000000,high = 450000010) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 450000000,high = 450000010) == 5: {e}')
    
    total += 1
    try:
        result = candidate(low = 3,high = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 3,high = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = 16,high = 17) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 16,high = 17) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 500000001,high = 1000000000) == 250000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 500000001,high = 1000000000) == 250000000: {e}')
    
    total += 1
    try:
        result = candidate(low = 2,high = 999999999) == 499999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 2,high = 999999999) == 499999999: {e}')
    
    total += 1
    try:
        result = candidate(low = 2,high = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 2,high = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 500000000,high = 1500000000) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 500000000,high = 1500000000) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(low = 2,high = 1999999999) == 999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 2,high = 1999999999) == 999999999: {e}')
    
    total += 1
    try:
        result = candidate(low = 15,high = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 15,high = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 14,high = 24) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 14,high = 24) == 5: {e}')
    
    total += 1
    try:
        result = candidate(low = 499999998,high = 500000002) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 499999998,high = 500000002) == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = 234567890,high = 987654321) == 376543216
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 234567890,high = 987654321) == 376543216: {e}')
    
    total += 1
    try:
        result = candidate(low = 20,high = 29) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 20,high = 29) == 5: {e}')
    
    total += 1
    try:
        result = candidate(low = 100000000,high = 999999999) == 450000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100000000,high = 999999999) == 450000000: {e}')
    
    total += 1
    try:
        result = candidate(low = 99,high = 101) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 99,high = 101) == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 1000000001) == 500000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 1000000001) == 500000001: {e}')
    
    total += 1
    try:
        result = candidate(low = 800000000,high = 850000000) == 25000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 800000000,high = 850000000) == 25000000: {e}')
    
    total += 1
    try:
        result = candidate(low = 300,high = 400) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 300,high = 400) == 50: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000000000,high = 1000000001) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000000000,high = 1000000001) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 25,high = 75) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 25,high = 75) == 26: {e}')
    
    total += 1
    try:
        result = candidate(low = 100,high = 200) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100,high = 200) == 50: {e}')
    
    total += 1
    try:
        result = candidate(low = 123456,high = 654321) == 265433
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 123456,high = 654321) == 265433: {e}')
    
    total += 1
    try:
        result = candidate(low = 500000001,high = 1500000001) == 500000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 500000001,high = 1500000001) == 500000001: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000000001,high = 9999999999) == 4500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000000001,high = 9999999999) == 4500000000: {e}')
    
    total += 1
    try:
        result = candidate(low = 45,high = 100) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 45,high = 100) == 28: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 999999999) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 999999999) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 2000000000) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 2000000000) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(low = 9,high = 11) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 9,high = 11) == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = 8,high = 1000000008) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 8,high = 1000000008) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(low = 15,high = 25) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 15,high = 25) == 6: {e}')
    
    total += 1
    try:
        result = candidate(low = 333333333,high = 666666666) == 166666667
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 333333333,high = 666666666) == 166666667: {e}')
    
    total += 1
    try:
        result = candidate(low = 2,high = 21) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 2,high = 21) == 10: {e}')
    
    total += 1
    try:
        result = candidate(low = 0,high = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 0,high = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 25,high = 35) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 25,high = 35) == 6: {e}')
    
    total += 1
    try:
        result = candidate(low = 11,high = 21) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 11,high = 21) == 6: {e}')
    
    total += 1
    try:
        result = candidate(low = 123456789,high = 987654321) == 432098767
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 123456789,high = 987654321) == 432098767: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(low = 21,high = 31) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 21,high = 31) == 6: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000000000,high = 1000000002) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000000000,high = 1000000002) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 100000001,high = 100000001) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100000001,high = 100000001) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 3,high = 1800000001) == 900000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 3,high = 1800000001) == 900000000: {e}')
    
    total += 1
    try:
        result = candidate(low = 500000000,high = 500000002) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 500000000,high = 500000002) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 10,high = 20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10,high = 20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(low = 999999998,high = 999999999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 999999998,high = 999999999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 5,high = 99) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5,high = 99) == 48: {e}')
    
    total += 1
    try:
        result = candidate(low = 789012345,high = 789012345) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 789012345,high = 789012345) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 15,high = 16) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 15,high = 16) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 20,high = 30) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 20,high = 30) == 5: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000000001,high = 2000000000) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000000001,high = 2000000000) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(low = 5,high = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5,high = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = 4,high = 1700000002) == 849999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 4,high = 1700000002) == 849999999: {e}')
    
    total += 1
    try:
        result = candidate(low = 999999999,high = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 999999999,high = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 500,high = 1500) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 500,high = 1500) == 500: {e}')
    
    total += 1
    try:
        result = candidate(low = 500,high = 500000005) == 249999753
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 500,high = 500000005) == 249999753: {e}')
    
    total += 1
    try:
        result = candidate(low = 4,high = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 4,high = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 100000000,high = 100000010) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100000000,high = 100000010) == 5: {e}')
    
    total += 1
    try:
        result = candidate(low = 12,high = 22) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 12,high = 22) == 5: {e}')
    
    total += 1
    try:
        result = candidate(low = 9,high = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 9,high = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 100000000,high = 900000000) == 400000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100000000,high = 900000000) == 400000000: {e}')
    
    total += 1
    try:
        result = candidate(low = 100,high = 1000) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100,high = 1000) == 450: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000000,high = 2000000) == 500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000000,high = 2000000) == 500000: {e}')
    
    total += 1
    try:
        result = candidate(low = 5,high = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5,high = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 500000001,high = 500000005) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 500000001,high = 500000005) == 3: {e}')
    
    total += 1
    try:
        result = candidate(low = 123456,high = 789012) == 332778
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 123456,high = 789012) == 332778: {e}')
    
    total += 1
    try:
        result = candidate(low = 5,high = 500000005) == 250000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5,high = 500000005) == 250000001: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000000001,high = 1000000001) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000000001,high = 1000000001) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 500,high = 600) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 500,high = 600) == 50: {e}')
    
    total += 1
    try:
        result = candidate(low = 888888888,high = 999999999) == 55555556
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 888888888,high = 999999999) == 55555556: {e}')
    
    total += 1
    try:
        result = candidate(low = 100000000,high = 200000000) == 50000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100000000,high = 200000000) == 50000000: {e}')
    
    total += 1
    try:
        result = candidate(low = 13,high = 23) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 13,high = 23) == 6: {e}')
    
    total += 1
    try:
        result = candidate(low = 500000001,high = 600000000) == 50000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 500000001,high = 600000000) == 50000000: {e}')
    
    total += 1
    try:
        result = candidate(low = 10,high = 19) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10,high = 19) == 5: {e}')
    
    total += 1
    try:
        result = candidate(low = 2000000000,high = 3000000000) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 2000000000,high = 3000000000) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(low = 500000000,high = 1000000000) == 250000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 500000000,high = 1000000000) == 250000000: {e}')
    
    total += 1
    try:
        result = candidate(low = 999999998,high = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 999999998,high = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 250000000,high = 750000000) == 250000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 250000000,high = 750000000) == 250000000: {e}')
    
    total += 1
    try:
        result = candidate(low = 499999999,high = 500000001) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 499999999,high = 500000001) == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000000000,high = 2000000000) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000000000,high = 2000000000) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(low = 500000001,high = 500000001) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 500000001,high = 500000001) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(low = 3,high = 7) == 3
    assert candidate(low = 0,high = 1000000000) == 500000000
    assert candidate(low = 0,high = 1) == 1
    assert candidate(low = 500000000,high = 500000000) == 0
    assert candidate(low = 1,high = 1000000000) == 500000000
    assert candidate(low = 8,high = 10) == 1
    assert candidate(low = 1000000000,high = 1000000000) == 0
    assert candidate(low = 1,high = 2) == 1
    assert candidate(low = 2,high = 3) == 1
    assert candidate(low = 0,high = 0) == 0
    assert candidate(low = 2,high = 2) == 0
    assert candidate(low = 1,high = 1) == 1
    assert candidate(low = 450000000,high = 450000010) == 5
    assert candidate(low = 3,high = 5) == 2
    assert candidate(low = 16,high = 17) == 1
    assert candidate(low = 500000001,high = 1000000000) == 250000000
    assert candidate(low = 2,high = 999999999) == 499999999
    assert candidate(low = 2,high = 4) == 1
    assert candidate(low = 500000000,high = 1500000000) == 500000000
    assert candidate(low = 2,high = 1999999999) == 999999999
    assert candidate(low = 15,high = 15) == 1
    assert candidate(low = 14,high = 24) == 5
    assert candidate(low = 499999998,high = 500000002) == 2
    assert candidate(low = 234567890,high = 987654321) == 376543216
    assert candidate(low = 20,high = 29) == 5
    assert candidate(low = 100000000,high = 999999999) == 450000000
    assert candidate(low = 99,high = 101) == 2
    assert candidate(low = 1,high = 10) == 5
    assert candidate(low = 1,high = 1000000001) == 500000001
    assert candidate(low = 800000000,high = 850000000) == 25000000
    assert candidate(low = 300,high = 400) == 50
    assert candidate(low = 1000000000,high = 1000000001) == 1
    assert candidate(low = 25,high = 75) == 26
    assert candidate(low = 100,high = 200) == 50
    assert candidate(low = 123456,high = 654321) == 265433
    assert candidate(low = 500000001,high = 1500000001) == 500000001
    assert candidate(low = 1000000001,high = 9999999999) == 4500000000
    assert candidate(low = 45,high = 100) == 28
    assert candidate(low = 1,high = 999999999) == 500000000
    assert candidate(low = 1,high = 2000000000) == 1000000000
    assert candidate(low = 9,high = 11) == 2
    assert candidate(low = 8,high = 1000000008) == 500000000
    assert candidate(low = 15,high = 25) == 6
    assert candidate(low = 333333333,high = 666666666) == 166666667
    assert candidate(low = 2,high = 21) == 10
    assert candidate(low = 0,high = 2) == 1
    assert candidate(low = 25,high = 35) == 6
    assert candidate(low = 11,high = 21) == 6
    assert candidate(low = 123456789,high = 987654321) == 432098767
    assert candidate(low = 1,high = 20) == 10
    assert candidate(low = 21,high = 31) == 6
    assert candidate(low = 1000000000,high = 1000000002) == 1
    assert candidate(low = 100000001,high = 100000001) == 1
    assert candidate(low = 3,high = 1800000001) == 900000000
    assert candidate(low = 500000000,high = 500000002) == 1
    assert candidate(low = 10,high = 20) == 5
    assert candidate(low = 999999998,high = 999999999) == 1
    assert candidate(low = 5,high = 99) == 48
    assert candidate(low = 789012345,high = 789012345) == 1
    assert candidate(low = 15,high = 16) == 1
    assert candidate(low = 20,high = 30) == 5
    assert candidate(low = 1000000001,high = 2000000000) == 500000000
    assert candidate(low = 5,high = 7) == 2
    assert candidate(low = 1,high = 3) == 2
    assert candidate(low = 4,high = 1700000002) == 849999999
    assert candidate(low = 999999999,high = 1000000000) == 1
    assert candidate(low = 500,high = 1500) == 500
    assert candidate(low = 500,high = 500000005) == 249999753
    assert candidate(low = 4,high = 6) == 1
    assert candidate(low = 100000000,high = 100000010) == 5
    assert candidate(low = 12,high = 22) == 5
    assert candidate(low = 9,high = 9) == 1
    assert candidate(low = 100000000,high = 900000000) == 400000000
    assert candidate(low = 100,high = 1000) == 450
    assert candidate(low = 1000000,high = 2000000) == 500000
    assert candidate(low = 5,high = 5) == 1
    assert candidate(low = 500000001,high = 500000005) == 3
    assert candidate(low = 123456,high = 789012) == 332778
    assert candidate(low = 5,high = 500000005) == 250000001
    assert candidate(low = 1000000001,high = 1000000001) == 1
    assert candidate(low = 500,high = 600) == 50
    assert candidate(low = 888888888,high = 999999999) == 55555556
    assert candidate(low = 100000000,high = 200000000) == 50000000
    assert candidate(low = 13,high = 23) == 6
    assert candidate(low = 500000001,high = 600000000) == 50000000
    assert candidate(low = 10,high = 19) == 5
    assert candidate(low = 2000000000,high = 3000000000) == 500000000
    assert candidate(low = 500000000,high = 1000000000) == 250000000
    assert candidate(low = 999999998,high = 1000000000) == 1
    assert candidate(low = 250000000,high = 750000000) == 250000000
    assert candidate(low = 499999999,high = 500000001) == 2
    assert candidate(low = 1000000000,high = 2000000000) == 500000000
    assert candidate(low = 500000001,high = 500000001) == 1


