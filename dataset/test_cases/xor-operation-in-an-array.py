def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 4,start = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,start = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,start = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,start = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,start = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,start = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,start = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,start = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,start = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,start = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,start = 0) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,start = 0) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,start = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,start = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,start = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,start = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,start = 2) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,start = 2) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,start = 5) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,start = 5) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,start = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,start = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,start = 999) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,start = 999) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,start = 25) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,start = 25) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,start = 200) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,start = 200) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,start = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,start = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 33,start = 17) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33,start = 17) == 81: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,start = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,start = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,start = 10) == 1518
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,start = 10) == 1518: {e}')
    
    total += 1
    try:
        result = candidate(n = 750,start = 50) == 1598
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750,start = 50) == 1598: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,start = 333) == 339
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,start = 333) == 339: {e}')
    
    total += 1
    try:
        result = candidate(n = 666,start = 333) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 666,start = 333) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,start = 250) == 1048
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,start = 250) == 1048: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,start = 3) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,start = 3) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,start = 1) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,start = 1) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,start = 10) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,start = 10) == 102: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,start = 999) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,start = 999) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,start = 11) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,start = 11) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 64,start = 42) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64,start = 42) == 128: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,start = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,start = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 80,start = 600) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80,start = 600) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,start = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,start = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,start = 10) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,start = 10) == 56: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,start = 42) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,start = 42) == 78: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,start = 25) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,start = 25) == 39: {e}')
    
    total += 1
    try:
        result = candidate(n = 256,start = 128) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256,start = 128) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 400,start = 400) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 400,start = 400) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 11,start = 8) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 11,start = 8) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,start = 250) == 312
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,start = 250) == 312: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,start = 11) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,start = 11) == 56: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,start = 750) == 1080
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,start = 750) == 1080: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,start = 500) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,start = 500) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 700,start = 600) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 700,start = 600) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 60,start = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60,start = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,start = 999) == 1864
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,start = 999) == 1864: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,start = 250) == 534
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,start = 250) == 534: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,start = 15) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,start = 15) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,start = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,start = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,start = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,start = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 333,start = 256) == 920
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 333,start = 256) == 920: {e}')
    
    total += 1
    try:
        result = candidate(n = 75,start = 300) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 75,start = 300) == 450: {e}')
    
    total += 1
    try:
        result = candidate(n = 128,start = 99) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 128,start = 99) == 256: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,start = 999) == 1064
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,start = 999) == 1064: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,start = 50) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,start = 50) == 200: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,start = 50) == 166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,start = 50) == 166: {e}')
    
    total += 1
    try:
        result = candidate(n = 250,start = 123) == 534
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 250,start = 123) == 534: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,start = 0) == 1998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,start = 0) == 1998: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,start = 500) == 2498
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,start = 500) == 2498: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,start = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,start = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 64,start = 32) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64,start = 32) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,start = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,start = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,start = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,start = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,start = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,start = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,start = 15) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,start = 15) == 70: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,start = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,start = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 13,start = 11) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,start = 11) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,start = 3) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,start = 3) == 40: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,start = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,start = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,start = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,start = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 120,start = 750) == 304
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120,start = 750) == 304: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,start = 1) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,start = 1) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,start = 12) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,start = 12) == 42: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,start = 0) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,start = 0) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,start = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,start = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 333,start = 222) == 222
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 333,start = 222) == 222: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,start = 15) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,start = 15) == 56: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,start = 14) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,start = 14) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,start = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,start = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 800,start = 150) == 1600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800,start = 150) == 1600: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,start = 300) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,start = 300) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,start = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,start = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,start = 17) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,start = 17) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,start = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,start = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 666,start = 128) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 666,start = 128) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,start = 2) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,start = 2) == 40: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,start = 600) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,start = 600) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,start = 42) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,start = 42) == 104: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,start = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,start = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,start = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,start = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 80,start = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 80,start = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 300,start = 450) == 1496
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300,start = 450) == 1496: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,start = 1) == 1999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,start = 1) == 1999: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,start = 300) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,start = 300) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 4,start = 3) == 8
    assert candidate(n = 8,start = 12) == 0
    assert candidate(n = 7,start = 2) == 0
    assert candidate(n = 3,start = 2) == 0
    assert candidate(n = 10,start = 1) == 2
    assert candidate(n = 5,start = 0) == 8
    assert candidate(n = 1,start = 7) == 7
    assert candidate(n = 10,start = 5) == 2
    assert candidate(n = 8,start = 2) == 16
    assert candidate(n = 7,start = 5) == 19
    assert candidate(n = 1,start = 5) == 5
    assert candidate(n = 10,start = 999) == 30
    assert candidate(n = 50,start = 25) == 2
    assert candidate(n = 100,start = 200) == 0
    assert candidate(n = 15,start = 2) == 0
    assert candidate(n = 33,start = 17) == 81
    assert candidate(n = 12,start = 8) == 0
    assert candidate(n = 750,start = 10) == 1518
    assert candidate(n = 750,start = 50) == 1598
    assert candidate(n = 3,start = 333) == 339
    assert candidate(n = 666,start = 333) == 2
    assert candidate(n = 500,start = 250) == 1048
    assert candidate(n = 12,start = 3) == 24
    assert candidate(n = 9,start = 1) == 17
    assert candidate(n = 50,start = 10) == 102
    assert candidate(n = 6,start = 999) == 22
    assert candidate(n = 8,start = 11) == 16
    assert candidate(n = 64,start = 42) == 128
    assert candidate(n = 15,start = 7) == 5
    assert candidate(n = 80,start = 600) == 0
    assert candidate(n = 250,start = 100) == 2
    assert candidate(n = 20,start = 10) == 56
    assert candidate(n = 30,start = 42) == 78
    assert candidate(n = 7,start = 25) == 39
    assert candidate(n = 256,start = 128) == 0
    assert candidate(n = 400,start = 400) == 0
    assert candidate(n = 11,start = 8) == 30
    assert candidate(n = 100,start = 250) == 312
    assert candidate(n = 20,start = 11) == 56
    assert candidate(n = 500,start = 750) == 1080
    assert candidate(n = 500,start = 500) == 0
    assert candidate(n = 700,start = 600) == 0
    assert candidate(n = 60,start = 8) == 0
    assert candidate(n = 100,start = 999) == 1864
    assert candidate(n = 250,start = 250) == 534
    assert candidate(n = 8,start = 15) == 16
    assert candidate(n = 18,start = 4) == 2
    assert candidate(n = 1000,start = 0) == 0
    assert candidate(n = 333,start = 256) == 920
    assert candidate(n = 75,start = 300) == 450
    assert candidate(n = 128,start = 99) == 256
    assert candidate(n = 500,start = 999) == 1064
    assert candidate(n = 100,start = 50) == 200
    assert candidate(n = 50,start = 50) == 166
    assert candidate(n = 250,start = 123) == 534
    assert candidate(n = 999,start = 0) == 1998
    assert candidate(n = 999,start = 500) == 2498
    assert candidate(n = 25,start = 6) == 6
    assert candidate(n = 64,start = 32) == 0
    assert candidate(n = 20,start = 12) == 0
    assert candidate(n = 50,start = 100) == 2
    assert candidate(n = 8,start = 1) == 0
    assert candidate(n = 30,start = 15) == 70
    assert candidate(n = 9,start = 7) == 7
    assert candidate(n = 13,start = 11) == 11
    assert candidate(n = 20,start = 3) == 40
    assert candidate(n = 100,start = 25) == 0
    assert candidate(n = 500,start = 0) == 0
    assert candidate(n = 120,start = 750) == 304
    assert candidate(n = 7,start = 1) == 15
    assert candidate(n = 15,start = 12) == 42
    assert candidate(n = 50,start = 0) == 2
    assert candidate(n = 1000,start = 1) == 0
    assert candidate(n = 333,start = 222) == 222
    assert candidate(n = 20,start = 15) == 56
    assert candidate(n = 7,start = 14) == 12
    assert candidate(n = 1000,start = 1000) == 0
    assert candidate(n = 800,start = 150) == 1600
    assert candidate(n = 300,start = 300) == 0
    assert candidate(n = 8,start = 100) == 0
    assert candidate(n = 7,start = 17) == 31
    assert candidate(n = 7,start = 10) == 8
    assert candidate(n = 666,start = 128) == 2
    assert candidate(n = 20,start = 2) == 40
    assert candidate(n = 300,start = 600) == 0
    assert candidate(n = 12,start = 42) == 104
    assert candidate(n = 40,start = 0) == 0
    assert candidate(n = 20,start = 0) == 0
    assert candidate(n = 80,start = 12) == 0
    assert candidate(n = 300,start = 450) == 1496
    assert candidate(n = 999,start = 1) == 1999
    assert candidate(n = 600,start = 300) == 0


