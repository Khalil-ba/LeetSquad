def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(tomatoSlices = 10000000,cheeseSlices = 5000000) == [0, 5000000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 10000000,cheeseSlices = 5000000) == [0, 5000000]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 16,cheeseSlices = 7) == [1, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 16,cheeseSlices = 7) == [1, 6]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 14,cheeseSlices = 5) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 14,cheeseSlices = 5) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 8,cheeseSlices = 2) == [2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 8,cheeseSlices = 2) == [2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 20,cheeseSlices = 5) == [5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 20,cheeseSlices = 5) == [5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 0,cheeseSlices = 0) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 0,cheeseSlices = 0) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 10,cheeseSlices = 3) == [2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 10,cheeseSlices = 3) == [2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 4,cheeseSlices = 17) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 4,cheeseSlices = 17) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 8,cheeseSlices = 4) == [0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 8,cheeseSlices = 4) == [0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 2,cheeseSlices = 1) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 2,cheeseSlices = 1) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 6,cheeseSlices = 3) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 6,cheeseSlices = 3) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 10000000,cheeseSlices = 2500000) == [2500000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 10000000,cheeseSlices = 2500000) == [2500000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 17,cheeseSlices = 4) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 17,cheeseSlices = 4) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 10,cheeseSlices = 5) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 10,cheeseSlices = 5) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 22,cheeseSlices = 5) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 22,cheeseSlices = 5) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 22,cheeseSlices = 6) == [5, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 22,cheeseSlices = 6) == [5, 1]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 20000000,cheeseSlices = 5000000) == [5000000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 20000000,cheeseSlices = 5000000) == [5000000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 1000,cheeseSlices = 250) == [250, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 1000,cheeseSlices = 250) == [250, 0]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 1,cheeseSlices = 1) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 1,cheeseSlices = 1) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 12,cheeseSlices = 3) == [3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 12,cheeseSlices = 3) == [3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 42,cheeseSlices = 14) == [7, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 42,cheeseSlices = 14) == [7, 7]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 28,cheeseSlices = 7) == [7, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 28,cheeseSlices = 7) == [7, 0]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 5000000,cheeseSlices = 2000000) == [500000, 1500000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 5000000,cheeseSlices = 2000000) == [500000, 1500000]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 30,cheeseSlices = 8) == [7, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 30,cheeseSlices = 8) == [7, 1]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 22,cheeseSlices = 11) == [0, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 22,cheeseSlices = 11) == [0, 11]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 15,cheeseSlices = 5) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 15,cheeseSlices = 5) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 7,cheeseSlices = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 7,cheeseSlices = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 88,cheeseSlices = 22) == [22, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 88,cheeseSlices = 22) == [22, 0]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 7,cheeseSlices = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 7,cheeseSlices = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 18,cheeseSlices = 5) == [4, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 18,cheeseSlices = 5) == [4, 1]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 18,cheeseSlices = 8) == [1, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 18,cheeseSlices = 8) == [1, 7]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 40,cheeseSlices = 10) == [10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 40,cheeseSlices = 10) == [10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 9,cheeseSlices = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 9,cheeseSlices = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 12,cheeseSlices = 5) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 12,cheeseSlices = 5) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 5,cheeseSlices = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 5,cheeseSlices = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 22,cheeseSlices = 9) == [2, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 22,cheeseSlices = 9) == [2, 7]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 50,cheeseSlices = 12) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 50,cheeseSlices = 12) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 32,cheeseSlices = 8) == [8, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 32,cheeseSlices = 8) == [8, 0]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 10000002,cheeseSlices = 2500000) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 10000002,cheeseSlices = 2500000) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 100,cheeseSlices = 30) == [20, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 100,cheeseSlices = 30) == [20, 10]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 24,cheeseSlices = 6) == [6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 24,cheeseSlices = 6) == [6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 32,cheeseSlices = 10) == [6, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 32,cheeseSlices = 10) == [6, 4]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 14,cheeseSlices = 7) == [0, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 14,cheeseSlices = 7) == [0, 7]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 7,cheeseSlices = 4) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 7,cheeseSlices = 4) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 80,cheeseSlices = 15) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 80,cheeseSlices = 15) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 34,cheeseSlices = 8) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 34,cheeseSlices = 8) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 20,cheeseSlices = 8) == [2, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 20,cheeseSlices = 8) == [2, 6]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 40000000,cheeseSlices = 10000000) == [10000000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 40000000,cheeseSlices = 10000000) == [10000000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 28,cheeseSlices = 6) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 28,cheeseSlices = 6) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 14,cheeseSlices = 4) == [3, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 14,cheeseSlices = 4) == [3, 1]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 40000002,cheeseSlices = 10000000) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 40000002,cheeseSlices = 10000000) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 16,cheeseSlices = 10) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 16,cheeseSlices = 10) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 123456,cheeseSlices = 65432) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 123456,cheeseSlices = 65432) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 50,cheeseSlices = 15) == [10, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 50,cheeseSlices = 15) == [10, 5]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 34,cheeseSlices = 9) == [8, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 34,cheeseSlices = 9) == [8, 1]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 10,cheeseSlices = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 10,cheeseSlices = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 12,cheeseSlices = 6) == [0, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 12,cheeseSlices = 6) == [0, 6]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 8,cheeseSlices = 3) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 8,cheeseSlices = 3) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 34,cheeseSlices = 11) == [6, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 34,cheeseSlices = 11) == [6, 5]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 25,cheeseSlices = 8) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 25,cheeseSlices = 8) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 18,cheeseSlices = 6) == [3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 18,cheeseSlices = 6) == [3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 5000000,cheeseSlices = 1250000) == [1250000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 5000000,cheeseSlices = 1250000) == [1250000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 14,cheeseSlices = 3) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 14,cheeseSlices = 3) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 9999998,cheeseSlices = 4999999) == [0, 4999999]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 9999998,cheeseSlices = 4999999) == [0, 4999999]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 22,cheeseSlices = 7) == [4, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 22,cheeseSlices = 7) == [4, 3]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 28,cheeseSlices = 10) == [4, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 28,cheeseSlices = 10) == [4, 6]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 30,cheeseSlices = 10) == [5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 30,cheeseSlices = 10) == [5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 4,cheeseSlices = 0) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 4,cheeseSlices = 0) == []: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 12,cheeseSlices = 4) == [2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 12,cheeseSlices = 4) == [2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 10,cheeseSlices = 4) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 10,cheeseSlices = 4) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 100,cheeseSlices = 25) == [25, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 100,cheeseSlices = 25) == [25, 0]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 44,cheeseSlices = 11) == [11, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 44,cheeseSlices = 11) == [11, 0]: {e}')
    
    total += 1
    try:
        result = candidate(tomatoSlices = 34,cheeseSlices = 13) == [4, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(tomatoSlices = 34,cheeseSlices = 13) == [4, 9]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(tomatoSlices = 10000000,cheeseSlices = 5000000) == [0, 5000000]
    assert candidate(tomatoSlices = 16,cheeseSlices = 7) == [1, 6]
    assert candidate(tomatoSlices = 14,cheeseSlices = 5) == [2, 3]
    assert candidate(tomatoSlices = 8,cheeseSlices = 2) == [2, 0]
    assert candidate(tomatoSlices = 20,cheeseSlices = 5) == [5, 0]
    assert candidate(tomatoSlices = 0,cheeseSlices = 0) == [0, 0]
    assert candidate(tomatoSlices = 10,cheeseSlices = 3) == [2, 1]
    assert candidate(tomatoSlices = 4,cheeseSlices = 17) == []
    assert candidate(tomatoSlices = 8,cheeseSlices = 4) == [0, 4]
    assert candidate(tomatoSlices = 2,cheeseSlices = 1) == [0, 1]
    assert candidate(tomatoSlices = 6,cheeseSlices = 3) == [0, 3]
    assert candidate(tomatoSlices = 10000000,cheeseSlices = 2500000) == [2500000, 0]
    assert candidate(tomatoSlices = 17,cheeseSlices = 4) == []
    assert candidate(tomatoSlices = 10,cheeseSlices = 5) == [0, 5]
    assert candidate(tomatoSlices = 22,cheeseSlices = 5) == []
    assert candidate(tomatoSlices = 22,cheeseSlices = 6) == [5, 1]
    assert candidate(tomatoSlices = 20000000,cheeseSlices = 5000000) == [5000000, 0]
    assert candidate(tomatoSlices = 1000,cheeseSlices = 250) == [250, 0]
    assert candidate(tomatoSlices = 1,cheeseSlices = 1) == []
    assert candidate(tomatoSlices = 12,cheeseSlices = 3) == [3, 0]
    assert candidate(tomatoSlices = 42,cheeseSlices = 14) == [7, 7]
    assert candidate(tomatoSlices = 28,cheeseSlices = 7) == [7, 0]
    assert candidate(tomatoSlices = 5000000,cheeseSlices = 2000000) == [500000, 1500000]
    assert candidate(tomatoSlices = 30,cheeseSlices = 8) == [7, 1]
    assert candidate(tomatoSlices = 22,cheeseSlices = 11) == [0, 11]
    assert candidate(tomatoSlices = 15,cheeseSlices = 5) == []
    assert candidate(tomatoSlices = 7,cheeseSlices = 2) == []
    assert candidate(tomatoSlices = 88,cheeseSlices = 22) == [22, 0]
    assert candidate(tomatoSlices = 7,cheeseSlices = 3) == []
    assert candidate(tomatoSlices = 18,cheeseSlices = 5) == [4, 1]
    assert candidate(tomatoSlices = 18,cheeseSlices = 8) == [1, 7]
    assert candidate(tomatoSlices = 40,cheeseSlices = 10) == [10, 0]
    assert candidate(tomatoSlices = 9,cheeseSlices = 3) == []
    assert candidate(tomatoSlices = 12,cheeseSlices = 5) == [1, 4]
    assert candidate(tomatoSlices = 5,cheeseSlices = 3) == []
    assert candidate(tomatoSlices = 22,cheeseSlices = 9) == [2, 7]
    assert candidate(tomatoSlices = 50,cheeseSlices = 12) == []
    assert candidate(tomatoSlices = 32,cheeseSlices = 8) == [8, 0]
    assert candidate(tomatoSlices = 10000002,cheeseSlices = 2500000) == []
    assert candidate(tomatoSlices = 100,cheeseSlices = 30) == [20, 10]
    assert candidate(tomatoSlices = 24,cheeseSlices = 6) == [6, 0]
    assert candidate(tomatoSlices = 32,cheeseSlices = 10) == [6, 4]
    assert candidate(tomatoSlices = 14,cheeseSlices = 7) == [0, 7]
    assert candidate(tomatoSlices = 7,cheeseSlices = 4) == []
    assert candidate(tomatoSlices = 80,cheeseSlices = 15) == []
    assert candidate(tomatoSlices = 34,cheeseSlices = 8) == []
    assert candidate(tomatoSlices = 20,cheeseSlices = 8) == [2, 6]
    assert candidate(tomatoSlices = 40000000,cheeseSlices = 10000000) == [10000000, 0]
    assert candidate(tomatoSlices = 28,cheeseSlices = 6) == []
    assert candidate(tomatoSlices = 14,cheeseSlices = 4) == [3, 1]
    assert candidate(tomatoSlices = 40000002,cheeseSlices = 10000000) == []
    assert candidate(tomatoSlices = 16,cheeseSlices = 10) == []
    assert candidate(tomatoSlices = 123456,cheeseSlices = 65432) == []
    assert candidate(tomatoSlices = 50,cheeseSlices = 15) == [10, 5]
    assert candidate(tomatoSlices = 34,cheeseSlices = 9) == [8, 1]
    assert candidate(tomatoSlices = 10,cheeseSlices = 2) == []
    assert candidate(tomatoSlices = 12,cheeseSlices = 6) == [0, 6]
    assert candidate(tomatoSlices = 8,cheeseSlices = 3) == [1, 2]
    assert candidate(tomatoSlices = 34,cheeseSlices = 11) == [6, 5]
    assert candidate(tomatoSlices = 25,cheeseSlices = 8) == []
    assert candidate(tomatoSlices = 18,cheeseSlices = 6) == [3, 3]
    assert candidate(tomatoSlices = 5000000,cheeseSlices = 1250000) == [1250000, 0]
    assert candidate(tomatoSlices = 14,cheeseSlices = 3) == []
    assert candidate(tomatoSlices = 9999998,cheeseSlices = 4999999) == [0, 4999999]
    assert candidate(tomatoSlices = 22,cheeseSlices = 7) == [4, 3]
    assert candidate(tomatoSlices = 28,cheeseSlices = 10) == [4, 6]
    assert candidate(tomatoSlices = 30,cheeseSlices = 10) == [5, 5]
    assert candidate(tomatoSlices = 4,cheeseSlices = 0) == []
    assert candidate(tomatoSlices = 12,cheeseSlices = 4) == [2, 2]
    assert candidate(tomatoSlices = 10,cheeseSlices = 4) == [1, 3]
    assert candidate(tomatoSlices = 100,cheeseSlices = 25) == [25, 0]
    assert candidate(tomatoSlices = 44,cheeseSlices = 11) == [11, 0]
    assert candidate(tomatoSlices = 34,cheeseSlices = 13) == [4, 9]


