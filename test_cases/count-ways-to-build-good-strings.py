def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(low = 5,high = 7,zero = 1,one = 1) == 224
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5,high = 7,zero = 1,one = 1) == 224: {e}')
    
    total += 1
    try:
        result = candidate(low = 100,high = 200,zero = 10,one = 20) == 28513
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100,high = 200,zero = 10,one = 20) == 28513: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 5,zero = 2,one = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 5,zero = 2,one = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(low = 5,high = 10,zero = 2,one = 4) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5,high = 10,zero = 2,one = 4) == 16: {e}')
    
    total += 1
    try:
        result = candidate(low = 10,high = 15,zero = 3,one = 2) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10,high = 15,zero = 3,one = 2) == 93: {e}')
    
    total += 1
    try:
        result = candidate(low = 5,high = 5,zero = 2,one = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5,high = 5,zero = 2,one = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = 5,high = 10,zero = 3,one = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5,high = 10,zero = 3,one = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 5,zero = 1,one = 1) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 5,zero = 1,one = 1) == 62: {e}')
    
    total += 1
    try:
        result = candidate(low = 5,high = 5,zero = 2,one = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5,high = 5,zero = 2,one = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 4,high = 6,zero = 2,one = 2) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 4,high = 6,zero = 2,one = 2) == 12: {e}')
    
    total += 1
    try:
        result = candidate(low = 4,high = 4,zero = 2,one = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 4,high = 4,zero = 2,one = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(low = 2,high = 3,zero = 1,one = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 2,high = 3,zero = 1,one = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(low = 3,high = 7,zero = 3,one = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 3,high = 7,zero = 3,one = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(low = 50000,high = 50000,zero = 5000,one = 5000) == 1024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 50000,high = 50000,zero = 5000,one = 5000) == 1024: {e}')
    
    total += 1
    try:
        result = candidate(low = 7,high = 9,zero = 3,one = 2) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 7,high = 9,zero = 3,one = 2) == 12: {e}')
    
    total += 1
    try:
        result = candidate(low = 50,high = 100,zero = 5,one = 7) == 177635
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 50,high = 100,zero = 5,one = 7) == 177635: {e}')
    
    total += 1
    try:
        result = candidate(low = 4,high = 6,zero = 2,one = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 4,high = 6,zero = 2,one = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(low = 6,high = 10,zero = 2,one = 3) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 6,high = 10,zero = 2,one = 3) == 21: {e}')
    
    total += 1
    try:
        result = candidate(low = 20,high = 25,zero = 5,one = 6) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 20,high = 25,zero = 5,one = 6) == 17: {e}')
    
    total += 1
    try:
        result = candidate(low = 10,high = 15,zero = 2,one = 2) == 224
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10,high = 15,zero = 2,one = 2) == 224: {e}')
    
    total += 1
    try:
        result = candidate(low = 10,high = 100,zero = 5,one = 7) == 178096
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10,high = 100,zero = 5,one = 7) == 178096: {e}')
    
    total += 1
    try:
        result = candidate(low = 4,high = 8,zero = 2,one = 2) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 4,high = 8,zero = 2,one = 2) == 28: {e}')
    
    total += 1
    try:
        result = candidate(low = 6,high = 10,zero = 3,one = 4) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 6,high = 10,zero = 3,one = 4) == 8: {e}')
    
    total += 1
    try:
        result = candidate(low = 5,high = 10,zero = 2,one = 3) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5,high = 10,zero = 2,one = 3) == 23: {e}')
    
    total += 1
    try:
        result = candidate(low = 20,high = 30,zero = 3,one = 5) == 283
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 20,high = 30,zero = 3,one = 5) == 283: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 5,zero = 1,one = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 5,zero = 1,one = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(low = 3,high = 9,zero = 2,one = 2) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 3,high = 9,zero = 2,one = 2) == 28: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 10,zero = 1,one = 1) == 2046
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 10,zero = 1,one = 1) == 2046: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 5,zero = 2,one = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 5,zero = 2,one = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(low = 10,high = 15,zero = 3,one = 4) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10,high = 15,zero = 3,one = 4) == 23: {e}')
    
    total += 1
    try:
        result = candidate(low = 10,high = 15,zero = 5,one = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10,high = 15,zero = 5,one = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(low = 10,high = 15,zero = 4,one = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10,high = 15,zero = 4,one = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(low = 5,high = 7,zero = 2,one = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5,high = 7,zero = 2,one = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(low = 10,high = 15,zero = 2,one = 3) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10,high = 15,zero = 2,one = 3) == 93: {e}')
    
    total += 1
    try:
        result = candidate(low = 10,high = 10,zero = 3,one = 4) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10,high = 10,zero = 3,one = 4) == 3: {e}')
    
    total += 1
    try:
        result = candidate(low = 10,high = 15,zero = 1,one = 1) == 64512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10,high = 15,zero = 1,one = 1) == 64512: {e}')
    
    total += 1
    try:
        result = candidate(low = 2,high = 5,zero = 1,one = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 2,high = 5,zero = 1,one = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(low = 10,high = 10,zero = 5,one = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10,high = 10,zero = 5,one = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(low = 50,high = 100,zero = 10,one = 15) == 444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 50,high = 100,zero = 10,one = 15) == 444: {e}')
    
    total += 1
    try:
        result = candidate(low = 3,high = 3,zero = 1,one = 1) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 3,high = 3,zero = 1,one = 1) == 8: {e}')
    
    total += 1
    try:
        result = candidate(low = 10,high = 15,zero = 5,one = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10,high = 15,zero = 5,one = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(low = 6,high = 8,zero = 4,one = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 6,high = 8,zero = 4,one = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 4,zero = 1,one = 1) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 4,zero = 1,one = 1) == 30: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 100,zero = 1,one = 1) == 952742561
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 100,zero = 1,one = 1) == 952742561: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 100,zero = 25,one = 25) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 100,zero = 25,one = 25) == 30: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(low = 5,high = 7,zero = 1,one = 1) == 224
    assert candidate(low = 100,high = 200,zero = 10,one = 20) == 28513
    assert candidate(low = 1,high = 5,zero = 2,one = 3) == 5
    assert candidate(low = 5,high = 10,zero = 2,one = 4) == 16
    assert candidate(low = 10,high = 15,zero = 3,one = 2) == 93
    assert candidate(low = 5,high = 5,zero = 2,one = 3) == 2
    assert candidate(low = 5,high = 10,zero = 3,one = 4) == 8
    assert candidate(low = 1,high = 5,zero = 1,one = 1) == 62
    assert candidate(low = 5,high = 5,zero = 2,one = 2) == 0
    assert candidate(low = 4,high = 6,zero = 2,one = 2) == 12
    assert candidate(low = 4,high = 4,zero = 2,one = 2) == 4
    assert candidate(low = 2,high = 3,zero = 1,one = 2) == 5
    assert candidate(low = 3,high = 7,zero = 3,one = 3) == 6
    assert candidate(low = 50000,high = 50000,zero = 5000,one = 5000) == 1024
    assert candidate(low = 7,high = 9,zero = 3,one = 2) == 12
    assert candidate(low = 50,high = 100,zero = 5,one = 7) == 177635
    assert candidate(low = 4,high = 6,zero = 2,one = 3) == 5
    assert candidate(low = 6,high = 10,zero = 2,one = 3) == 21
    assert candidate(low = 20,high = 25,zero = 5,one = 6) == 17
    assert candidate(low = 10,high = 15,zero = 2,one = 2) == 224
    assert candidate(low = 10,high = 100,zero = 5,one = 7) == 178096
    assert candidate(low = 4,high = 8,zero = 2,one = 2) == 28
    assert candidate(low = 6,high = 10,zero = 3,one = 4) == 8
    assert candidate(low = 5,high = 10,zero = 2,one = 3) == 23
    assert candidate(low = 20,high = 30,zero = 3,one = 5) == 283
    assert candidate(low = 1,high = 5,zero = 1,one = 5) == 6
    assert candidate(low = 3,high = 9,zero = 2,one = 2) == 28
    assert candidate(low = 1,high = 10,zero = 1,one = 1) == 2046
    assert candidate(low = 1,high = 5,zero = 2,one = 2) == 6
    assert candidate(low = 10,high = 15,zero = 3,one = 4) == 23
    assert candidate(low = 10,high = 15,zero = 5,one = 6) == 5
    assert candidate(low = 10,high = 15,zero = 4,one = 5) == 9
    assert candidate(low = 5,high = 7,zero = 2,one = 3) == 7
    assert candidate(low = 10,high = 15,zero = 2,one = 3) == 93
    assert candidate(low = 10,high = 10,zero = 3,one = 4) == 3
    assert candidate(low = 10,high = 15,zero = 1,one = 1) == 64512
    assert candidate(low = 2,high = 5,zero = 1,one = 3) == 10
    assert candidate(low = 10,high = 10,zero = 5,one = 5) == 4
    assert candidate(low = 50,high = 100,zero = 10,one = 15) == 444
    assert candidate(low = 3,high = 3,zero = 1,one = 1) == 8
    assert candidate(low = 10,high = 15,zero = 5,one = 5) == 12
    assert candidate(low = 6,high = 8,zero = 4,one = 5) == 1
    assert candidate(low = 1,high = 4,zero = 1,one = 1) == 30
    assert candidate(low = 1,high = 100,zero = 1,one = 1) == 952742561
    assert candidate(low = 1,high = 100,zero = 25,one = 25) == 30


