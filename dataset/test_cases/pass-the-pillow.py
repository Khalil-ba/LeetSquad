def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 2,time = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,time = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,time = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,time = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,time = 750) == 249
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,time = 750) == 249: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,time = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,time = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,time = 20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,time = 20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,time = 20) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,time = 20) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,time = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,time = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,time = 2) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,time = 2) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,time = 12) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,time = 12) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,time = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,time = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,time = 1000) == 999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,time = 1000) == 999: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,time = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,time = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,time = 12) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,time = 12) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,time = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,time = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,time = 800) == 399
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,time = 800) == 399: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,time = 49) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,time = 49) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,time = 500) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,time = 500) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,time = 50) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,time = 50) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,time = 120) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,time = 120) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,time = 100) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,time = 100) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,time = 800) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,time = 800) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,time = 1000) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,time = 1000) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 499,time = 1002) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 499,time = 1002) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,time = 45) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,time = 45) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,time = 150) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,time = 150) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 550,time = 725) == 374
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 550,time = 725) == 374: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,time = 2500) == 495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,time = 2500) == 495: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,time = 25) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,time = 25) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,time = 150) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,time = 150) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 499,time = 500) == 497
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 499,time = 500) == 497: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,time = 60) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,time = 60) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,time = 225) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,time = 225) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,time = 400) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,time = 400) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,time = 999) == 998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,time = 999) == 998: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,time = 1000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,time = 1000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,time = 1250) == 253
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,time = 1250) == 253: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,time = 100) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,time = 100) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,time = 500) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,time = 500) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,time = 998) == 999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,time = 998) == 999: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,time = 11) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,time = 11) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,time = 1000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,time = 1000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,time = 150) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,time = 150) == 49: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,time = 1000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,time = 1000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,time = 2000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,time = 2000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,time = 30) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,time = 30) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 850,time = 1500) == 199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 850,time = 1500) == 199: {e}')
    
    total += 1
    try:
        result = candidate(n = 450,time = 999) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450,time = 999) == 102: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,time = 1250) == 245
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,time = 1250) == 245: {e}')
    
    total += 1
    try:
        result = candidate(n = 450,time = 675) == 224
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450,time = 675) == 224: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,time = 250) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,time = 250) == 53: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,time = 9) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,time = 9) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 450,time = 500) == 399
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450,time = 500) == 399: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,time = 500) == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,time = 500) == 97: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,time = 90) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,time = 90) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,time = 13) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,time = 13) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,time = 100) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,time = 100) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,time = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,time = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,time = 750) == 247
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,time = 750) == 247: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,time = 150) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,time = 150) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,time = 1000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,time = 1000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,time = 30) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,time = 30) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,time = 199) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,time = 199) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,time = 500) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,time = 500) == 95: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,time = 40) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,time = 40) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,time = 31) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,time = 31) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,time = 25) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,time = 25) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,time = 50) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,time = 50) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,time = 2000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,time = 2000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 333,time = 998) == 331
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 333,time = 998) == 331: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,time = 24) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,time = 24) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,time = 25) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,time = 25) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,time = 150) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,time = 150) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,time = 999) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,time = 999) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,time = 1998) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,time = 1998) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,time = 81) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,time = 81) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,time = 550) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,time = 550) == 49: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,time = 600) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,time = 600) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,time = 101) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,time = 101) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,time = 625) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,time = 625) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,time = 1001) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,time = 1001) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,time = 18) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,time = 18) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,time = 999) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,time = 999) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,time = 25) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,time = 25) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,time = 25) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,time = 25) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,time = 999) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,time = 999) == 200: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,time = 27) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,time = 27) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,time = 1000) == 997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,time = 1000) == 997: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,time = 100) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,time = 100) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,time = 2001) == 504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,time = 2001) == 504: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,time = 500) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,time = 500) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,time = 30) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,time = 30) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,time = 900) == 299
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,time = 900) == 299: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,time = 250) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,time = 250) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,time = 1001) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,time = 1001) == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 2,time = 5) == 2
    assert candidate(n = 10,time = 15) == 4
    assert candidate(n = 500,time = 750) == 249
    assert candidate(n = 2,time = 1) == 2
    assert candidate(n = 7,time = 20) == 5
    assert candidate(n = 8,time = 20) == 7
    assert candidate(n = 5,time = 7) == 2
    assert candidate(n = 3,time = 2) == 3
    assert candidate(n = 6,time = 12) == 3
    assert candidate(n = 2,time = 2) == 1
    assert candidate(n = 1000,time = 1000) == 999
    assert candidate(n = 6,time = 1) == 2
    assert candidate(n = 8,time = 12) == 3
    assert candidate(n = 4,time = 5) == 2
    assert candidate(n = 600,time = 800) == 399
    assert candidate(n = 7,time = 49) == 2
    assert candidate(n = 15,time = 500) == 5
    assert candidate(n = 9,time = 50) == 3
    assert candidate(n = 15,time = 120) == 9
    assert candidate(n = 15,time = 100) == 13
    assert candidate(n = 100,time = 800) == 9
    assert candidate(n = 50,time = 1000) == 21
    assert candidate(n = 499,time = 1002) == 7
    assert candidate(n = 8,time = 45) == 4
    assert candidate(n = 20,time = 150) == 3
    assert candidate(n = 550,time = 725) == 374
    assert candidate(n = 500,time = 2500) == 495
    assert candidate(n = 15,time = 25) == 4
    assert candidate(n = 12,time = 150) == 5
    assert candidate(n = 499,time = 500) == 497
    assert candidate(n = 12,time = 60) == 7
    assert candidate(n = 15,time = 225) == 2
    assert candidate(n = 200,time = 400) == 3
    assert candidate(n = 999,time = 999) == 998
    assert candidate(n = 7,time = 1000) == 5
    assert candidate(n = 500,time = 1250) == 253
    assert candidate(n = 10,time = 100) == 9
    assert candidate(n = 20,time = 500) == 7
    assert candidate(n = 999,time = 998) == 999
    assert candidate(n = 6,time = 11) == 2
    assert candidate(n = 250,time = 1000) == 5
    assert candidate(n = 100,time = 150) == 49
    assert candidate(n = 2,time = 1000) == 1
    assert candidate(n = 1000,time = 2000) == 3
    assert candidate(n = 12,time = 30) == 9
    assert candidate(n = 850,time = 1500) == 199
    assert candidate(n = 450,time = 999) == 102
    assert candidate(n = 250,time = 1250) == 245
    assert candidate(n = 450,time = 675) == 224
    assert candidate(n = 100,time = 250) == 53
    assert candidate(n = 3,time = 9) == 2
    assert candidate(n = 450,time = 500) == 399
    assert candidate(n = 150,time = 500) == 97
    assert candidate(n = 18,time = 90) == 13
    assert candidate(n = 6,time = 13) == 4
    assert candidate(n = 12,time = 100) == 11
    assert candidate(n = 2,time = 100) == 1
    assert candidate(n = 250,time = 750) == 247
    assert candidate(n = 9,time = 150) == 7
    assert candidate(n = 20,time = 1000) == 13
    assert candidate(n = 6,time = 30) == 1
    assert candidate(n = 20,time = 199) == 10
    assert candidate(n = 100,time = 500) == 95
    assert candidate(n = 9,time = 40) == 9
    assert candidate(n = 8,time = 31) == 4
    assert candidate(n = 9,time = 25) == 8
    assert candidate(n = 20,time = 50) == 13
    assert candidate(n = 2,time = 2000) == 1
    assert candidate(n = 333,time = 998) == 331
    assert candidate(n = 8,time = 24) == 5
    assert candidate(n = 10,time = 25) == 8
    assert candidate(n = 30,time = 150) == 25
    assert candidate(n = 3,time = 999) == 2
    assert candidate(n = 999,time = 1998) == 3
    assert candidate(n = 9,time = 81) == 2
    assert candidate(n = 300,time = 550) == 49
    assert candidate(n = 300,time = 600) == 3
    assert candidate(n = 6,time = 101) == 2
    assert candidate(n = 25,time = 625) == 2
    assert candidate(n = 250,time = 1001) == 6
    assert candidate(n = 9,time = 18) == 3
    assert candidate(n = 1000,time = 999) == 1000
    assert candidate(n = 5,time = 25) == 2
    assert candidate(n = 12,time = 25) == 4
    assert candidate(n = 600,time = 999) == 200
    assert candidate(n = 8,time = 27) == 2
    assert candidate(n = 999,time = 1000) == 997
    assert candidate(n = 8,time = 100) == 3
    assert candidate(n = 750,time = 2001) == 504
    assert candidate(n = 2,time = 500) == 1
    assert candidate(n = 8,time = 30) == 3
    assert candidate(n = 600,time = 900) == 299
    assert candidate(n = 25,time = 250) == 11
    assert candidate(n = 500,time = 1001) == 4


