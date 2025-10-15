def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 9) == [2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9) == [2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000001) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000001) == []: {e}')
    
    total += 1
    try:
        result = candidate(num = 0) == [-1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 0) == [-1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(num = 4) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 4) == []: {e}')
    
    total += 1
    try:
        result = candidate(num = 33) == [10, 11, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 33) == [10, 11, 12]: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000000) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000000) == []: {e}')
    
    total += 1
    try:
        result = candidate(num = 3) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(num = 15) == [4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 15) == [4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(num = 100000000000000) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100000000000000) == []: {e}')
    
    total += 1
    try:
        result = candidate(num = 300000000000003) == [100000000000000, 100000000000001, 100000000000002]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 300000000000003) == [100000000000000, 100000000000001, 100000000000002]: {e}')
    
    total += 1
    try:
        result = candidate(num = 3000000000) == [999999999, 1000000000, 1000000001]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3000000000) == [999999999, 1000000000, 1000000001]: {e}')
    
    total += 1
    try:
        result = candidate(num = 3000000000000) == [999999999999, 1000000000000, 1000000000001]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3000000000000) == [999999999999, 1000000000000, 1000000000001]: {e}')
    
    total += 1
    try:
        result = candidate(num = 999) == [332, 333, 334]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999) == [332, 333, 334]: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000003) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000003) == []: {e}')
    
    total += 1
    try:
        result = candidate(num = 27) == [8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 27) == [8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(num = 45) == [14, 15, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 45) == [14, 15, 16]: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999999999) == [333333333332, 333333333333, 333333333334]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999999999) == [333333333332, 333333333333, 333333333334]: {e}')
    
    total += 1
    try:
        result = candidate(num = 300000000000000) == [99999999999999, 100000000000000, 100000000000001]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 300000000000000) == [99999999999999, 100000000000000, 100000000000001]: {e}')
    
    total += 1
    try:
        result = candidate(num = 99) == [32, 33, 34]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 99) == [32, 33, 34]: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234567890125) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234567890125) == []: {e}')
    
    total += 1
    try:
        result = candidate(num = 3000000000001) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3000000000001) == []: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789) == [41152262, 41152263, 41152264]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789) == [41152262, 41152263, 41152264]: {e}')
    
    total += 1
    try:
        result = candidate(num = 777777777777777) == [259259259259258, 259259259259259, 259259259259260]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 777777777777777) == [259259259259258, 259259259259259, 259259259259260]: {e}')
    
    total += 1
    try:
        result = candidate(num = 2999999999997) == [999999999998, 999999999999, 1000000000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2999999999997) == [999999999998, 999999999999, 1000000000000]: {e}')
    
    total += 1
    try:
        result = candidate(num = 299999999999997) == [99999999999998, 99999999999999, 100000000000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 299999999999997) == [99999999999998, 99999999999999, 100000000000000]: {e}')
    
    total += 1
    try:
        result = candidate(num = 105) == [34, 35, 36]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 105) == [34, 35, 36]: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999999999999) == [333333333333332, 333333333333333, 333333333333334]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999999999999) == [333333333333332, 333333333333333, 333333333333334]: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000) == []: {e}')
    
    total += 1
    try:
        result = candidate(num = 81) == [26, 27, 28]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 81) == [26, 27, 28]: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000000002) == [333333333333333, 333333333333334, 333333333333335]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000000002) == [333333333333333, 333333333333334, 333333333333335]: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000002) == [333333333333, 333333333334, 333333333335]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000002) == [333333333333, 333333333334, 333333333335]: {e}')
    
    total += 1
    try:
        result = candidate(num = 987654321) == [329218106, 329218107, 329218108]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 987654321) == [329218106, 329218107, 329218108]: {e}')
    
    total += 1
    try:
        result = candidate(num = 7500000000000) == [2499999999999, 2500000000000, 2500000000001]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 7500000000000) == [2499999999999, 2500000000000, 2500000000001]: {e}')
    
    total += 1
    try:
        result = candidate(num = 1001) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1001) == []: {e}')
    
    total += 1
    try:
        result = candidate(num = 21) == [6, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 21) == [6, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(num = 123456789012345) == [41152263004114, 41152263004115, 41152263004116]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123456789012345) == [41152263004114, 41152263004115, 41152263004116]: {e}')
    
    total += 1
    try:
        result = candidate(num = 6) == [1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 6) == [1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(num = 299792458) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 299792458) == []: {e}')
    
    total += 1
    try:
        result = candidate(num = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(num = 1) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1) == []: {e}')
    
    total += 1
    try:
        result = candidate(num = 100) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100) == []: {e}')
    
    total += 1
    try:
        result = candidate(num = 1500000000000) == [499999999999, 500000000000, 500000000001]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1500000000000) == [499999999999, 500000000000, 500000000001]: {e}')
    
    total += 1
    try:
        result = candidate(num = 999999999) == [333333332, 333333333, 333333334]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999999999) == [333333332, 333333333, 333333334]: {e}')
    
    total += 1
    try:
        result = candidate(num = 500000000000001) == [166666666666666, 166666666666667, 166666666666668]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 500000000000001) == [166666666666666, 166666666666667, 166666666666668]: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000) == []: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234567890123) == [411522630040, 411522630041, 411522630042]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234567890123) == [411522630040, 411522630041, 411522630042]: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234567890124) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234567890124) == []: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000000000) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000000000) == []: {e}')
    
    total += 1
    try:
        result = candidate(num = 180) == [59, 60, 61]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 180) == [59, 60, 61]: {e}')
    
    total += 1
    try:
        result = candidate(num = 101) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 101) == []: {e}')
    
    total += 1
    try:
        result = candidate(num = 8999999999997) == [2999999999998, 2999999999999, 3000000000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8999999999997) == [2999999999998, 2999999999999, 3000000000000]: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000000000000001) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000000000000001) == []: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 9) == [2, 3, 4]
    assert candidate(num = 1000000000001) == []
    assert candidate(num = 0) == [-1, 0, 1]
    assert candidate(num = 4) == []
    assert candidate(num = 33) == [10, 11, 12]
    assert candidate(num = 1000000000000) == []
    assert candidate(num = 3) == [0, 1, 2]
    assert candidate(num = 15) == [4, 5, 6]
    assert candidate(num = 100000000000000) == []
    assert candidate(num = 300000000000003) == [100000000000000, 100000000000001, 100000000000002]
    assert candidate(num = 3000000000) == [999999999, 1000000000, 1000000001]
    assert candidate(num = 3000000000000) == [999999999999, 1000000000000, 1000000000001]
    assert candidate(num = 999) == [332, 333, 334]
    assert candidate(num = 1000000000003) == []
    assert candidate(num = 27) == [8, 9, 10]
    assert candidate(num = 45) == [14, 15, 16]
    assert candidate(num = 999999999999) == [333333333332, 333333333333, 333333333334]
    assert candidate(num = 300000000000000) == [99999999999999, 100000000000000, 100000000000001]
    assert candidate(num = 99) == [32, 33, 34]
    assert candidate(num = 1234567890125) == []
    assert candidate(num = 3000000000001) == []
    assert candidate(num = 123456789) == [41152262, 41152263, 41152264]
    assert candidate(num = 777777777777777) == [259259259259258, 259259259259259, 259259259259260]
    assert candidate(num = 2999999999997) == [999999999998, 999999999999, 1000000000000]
    assert candidate(num = 299999999999997) == [99999999999998, 99999999999999, 100000000000000]
    assert candidate(num = 105) == [34, 35, 36]
    assert candidate(num = 999999999999999) == [333333333333332, 333333333333333, 333333333333334]
    assert candidate(num = 1000) == []
    assert candidate(num = 81) == [26, 27, 28]
    assert candidate(num = 1000000000000002) == [333333333333333, 333333333333334, 333333333333335]
    assert candidate(num = 1000000000002) == [333333333333, 333333333334, 333333333335]
    assert candidate(num = 987654321) == [329218106, 329218107, 329218108]
    assert candidate(num = 7500000000000) == [2499999999999, 2500000000000, 2500000000001]
    assert candidate(num = 1001) == []
    assert candidate(num = 21) == [6, 7, 8]
    assert candidate(num = 123456789012345) == [41152263004114, 41152263004115, 41152263004116]
    assert candidate(num = 6) == [1, 2, 3]
    assert candidate(num = 299792458) == []
    assert candidate(num = 2) == []
    assert candidate(num = 1) == []
    assert candidate(num = 100) == []
    assert candidate(num = 1500000000000) == [499999999999, 500000000000, 500000000001]
    assert candidate(num = 999999999) == [333333332, 333333333, 333333334]
    assert candidate(num = 500000000000001) == [166666666666666, 166666666666667, 166666666666668]
    assert candidate(num = 1000000) == []
    assert candidate(num = 1234567890123) == [411522630040, 411522630041, 411522630042]
    assert candidate(num = 1234567890124) == []
    assert candidate(num = 1000000000000000) == []
    assert candidate(num = 180) == [59, 60, 61]
    assert candidate(num = 101) == []
    assert candidate(num = 8999999999997) == [2999999999998, 2999999999999, 3000000000000]
    assert candidate(num = 1000000000000001) == []


