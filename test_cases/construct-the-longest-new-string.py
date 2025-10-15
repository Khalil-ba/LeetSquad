def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(x = 1,y = 10,z = 10) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1,y = 10,z = 10) == 26: {e}')
    
    total += 1
    try:
        result = candidate(x = 50,y = 50,z = 50) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 50,y = 50,z = 50) == 300: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 1,z = 10) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 1,z = 10) == 26: {e}')
    
    total += 1
    try:
        result = candidate(x = 20,y = 10,z = 5) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,y = 10,z = 5) == 52: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 10,z = 100) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 10,z = 100) == 240: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 10,z = 1) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 10,z = 1) == 42: {e}')
    
    total += 1
    try:
        result = candidate(x = 2,y = 5,z = 1) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2,y = 5,z = 1) == 12: {e}')
    
    total += 1
    try:
        result = candidate(x = 1,y = 1,z = 1) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1,y = 1,z = 1) == 6: {e}')
    
    total += 1
    try:
        result = candidate(x = 3,y = 2,z = 2) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 3,y = 2,z = 2) == 14: {e}')
    
    total += 1
    try:
        result = candidate(x = 49,y = 50,z = 1) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 49,y = 50,z = 1) == 200: {e}')
    
    total += 1
    try:
        result = candidate(x = 40,y = 1,z = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 40,y = 1,z = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(x = 40,y = 40,z = 30) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 40,y = 40,z = 30) == 220: {e}')
    
    total += 1
    try:
        result = candidate(x = 50,y = 49,z = 49) == 296
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 50,y = 49,z = 49) == 296: {e}')
    
    total += 1
    try:
        result = candidate(x = 5,y = 1,z = 5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,y = 1,z = 5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(x = 50,y = 1,z = 1) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 50,y = 1,z = 1) == 8: {e}')
    
    total += 1
    try:
        result = candidate(x = 2,y = 1,z = 10) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2,y = 1,z = 10) == 26: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 10,z = 30) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 10,z = 30) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = 25,y = 25,z = 10) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,y = 25,z = 10) == 120: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 15,z = 8) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 15,z = 8) == 58: {e}')
    
    total += 1
    try:
        result = candidate(x = 2,y = 10,z = 0) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2,y = 10,z = 0) == 10: {e}')
    
    total += 1
    try:
        result = candidate(x = 0,y = 5,z = 10) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 0,y = 5,z = 10) == 22: {e}')
    
    total += 1
    try:
        result = candidate(x = 35,y = 15,z = 5) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 35,y = 15,z = 5) == 72: {e}')
    
    total += 1
    try:
        result = candidate(x = 25,y = 1,z = 25) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,y = 1,z = 25) == 56: {e}')
    
    total += 1
    try:
        result = candidate(x = 2,y = 50,z = 25) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2,y = 50,z = 25) == 60: {e}')
    
    total += 1
    try:
        result = candidate(x = 7,y = 7,z = 14) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 7,y = 7,z = 14) == 56: {e}')
    
    total += 1
    try:
        result = candidate(x = 30,y = 30,z = 25) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 30,y = 30,z = 25) == 170: {e}')
    
    total += 1
    try:
        result = candidate(x = 25,y = 20,z = 10) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,y = 20,z = 10) == 102: {e}')
    
    total += 1
    try:
        result = candidate(x = 5,y = 5,z = 45) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,y = 5,z = 45) == 110: {e}')
    
    total += 1
    try:
        result = candidate(x = 5,y = 5,z = 10) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,y = 5,z = 10) == 40: {e}')
    
    total += 1
    try:
        result = candidate(x = 30,y = 20,z = 10) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 30,y = 20,z = 10) == 102: {e}')
    
    total += 1
    try:
        result = candidate(x = 33,y = 33,z = 34) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 33,y = 33,z = 34) == 200: {e}')
    
    total += 1
    try:
        result = candidate(x = 30,y = 15,z = 25) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 30,y = 15,z = 25) == 112: {e}')
    
    total += 1
    try:
        result = candidate(x = 40,y = 10,z = 30) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 40,y = 10,z = 30) == 102: {e}')
    
    total += 1
    try:
        result = candidate(x = 15,y = 15,z = 25) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 15,y = 15,z = 25) == 110: {e}')
    
    total += 1
    try:
        result = candidate(x = 30,y = 25,z = 30) == 162
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 30,y = 25,z = 30) == 162: {e}')
    
    total += 1
    try:
        result = candidate(x = 1,y = 30,z = 5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1,y = 30,z = 5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 5,z = 15) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 5,z = 15) == 52: {e}')
    
    total += 1
    try:
        result = candidate(x = 15,y = 15,z = 5) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 15,y = 15,z = 5) == 70: {e}')
    
    total += 1
    try:
        result = candidate(x = 20,y = 20,z = 1) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,y = 20,z = 1) == 82: {e}')
    
    total += 1
    try:
        result = candidate(x = 50,y = 10,z = 1) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 50,y = 10,z = 1) == 44: {e}')
    
    total += 1
    try:
        result = candidate(x = 20,y = 1,z = 30) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,y = 1,z = 30) == 66: {e}')
    
    total += 1
    try:
        result = candidate(x = 20,y = 15,z = 20) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,y = 15,z = 20) == 102: {e}')
    
    total += 1
    try:
        result = candidate(x = 40,y = 30,z = 20) == 162
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 40,y = 30,z = 20) == 162: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 15,z = 20) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 15,z = 20) == 82: {e}')
    
    total += 1
    try:
        result = candidate(x = 20,y = 30,z = 40) == 162
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,y = 30,z = 40) == 162: {e}')
    
    total += 1
    try:
        result = candidate(x = 5,y = 5,z = 50) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,y = 5,z = 50) == 120: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 10,z = 10) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 10,z = 10) == 60: {e}')
    
    total += 1
    try:
        result = candidate(x = 40,y = 10,z = 1) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 40,y = 10,z = 1) == 44: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 35,z = 5) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 35,z = 5) == 52: {e}')
    
    total += 1
    try:
        result = candidate(x = 1,y = 1,z = 50) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1,y = 1,z = 50) == 104: {e}')
    
    total += 1
    try:
        result = candidate(x = 30,y = 20,z = 30) == 142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 30,y = 20,z = 30) == 142: {e}')
    
    total += 1
    try:
        result = candidate(x = 15,y = 25,z = 30) == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 15,y = 25,z = 30) == 122: {e}')
    
    total += 1
    try:
        result = candidate(x = 5,y = 5,z = 40) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,y = 5,z = 40) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = 2,y = 2,z = 4) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2,y = 2,z = 4) == 16: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 1,z = 50) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 1,z = 50) == 106: {e}')
    
    total += 1
    try:
        result = candidate(x = 45,y = 40,z = 45) == 252
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 45,y = 40,z = 45) == 252: {e}')
    
    total += 1
    try:
        result = candidate(x = 45,y = 5,z = 5) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 45,y = 5,z = 5) == 32: {e}')
    
    total += 1
    try:
        result = candidate(x = 45,y = 30,z = 25) == 172
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 45,y = 30,z = 25) == 172: {e}')
    
    total += 1
    try:
        result = candidate(x = 5,y = 10,z = 40) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 5,y = 10,z = 40) == 102: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 10,z = 15) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 10,z = 15) == 70: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 10,z = 40) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 10,z = 40) == 120: {e}')
    
    total += 1
    try:
        result = candidate(x = 2,y = 2,z = 3) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 2,y = 2,z = 3) == 14: {e}')
    
    total += 1
    try:
        result = candidate(x = 20,y = 20,z = 30) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,y = 20,z = 30) == 140: {e}')
    
    total += 1
    try:
        result = candidate(x = 40,y = 10,z = 10) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 40,y = 10,z = 10) == 62: {e}')
    
    total += 1
    try:
        result = candidate(x = 25,y = 25,z = 1) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,y = 25,z = 1) == 102: {e}')
    
    total += 1
    try:
        result = candidate(x = 49,y = 50,z = 49) == 296
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 49,y = 50,z = 49) == 296: {e}')
    
    total += 1
    try:
        result = candidate(x = 15,y = 15,z = 30) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 15,y = 15,z = 30) == 120: {e}')
    
    total += 1
    try:
        result = candidate(x = 4,y = 3,z = 6) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 4,y = 3,z = 6) == 26: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 10,z = 5) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 10,z = 5) == 50: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 40,z = 20) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 40,z = 20) == 82: {e}')
    
    total += 1
    try:
        result = candidate(x = 1,y = 50,z = 1) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1,y = 50,z = 1) == 8: {e}')
    
    total += 1
    try:
        result = candidate(x = 20,y = 15,z = 25) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,y = 15,z = 25) == 112: {e}')
    
    total += 1
    try:
        result = candidate(x = 1,y = 50,z = 49) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1,y = 50,z = 49) == 104: {e}')
    
    total += 1
    try:
        result = candidate(x = 25,y = 25,z = 25) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,y = 25,z = 25) == 150: {e}')
    
    total += 1
    try:
        result = candidate(x = 20,y = 20,z = 20) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,y = 20,z = 20) == 120: {e}')
    
    total += 1
    try:
        result = candidate(x = 20,y = 20,z = 10) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,y = 20,z = 10) == 100: {e}')
    
    total += 1
    try:
        result = candidate(x = 25,y = 20,z = 30) == 142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 25,y = 20,z = 30) == 142: {e}')
    
    total += 1
    try:
        result = candidate(x = 1,y = 50,z = 50) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 1,y = 50,z = 50) == 106: {e}')
    
    total += 1
    try:
        result = candidate(x = 30,y = 40,z = 35) == 192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 30,y = 40,z = 35) == 192: {e}')
    
    total += 1
    try:
        result = candidate(x = 30,y = 30,z = 1) == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 30,y = 30,z = 1) == 122: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 30,z = 10) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 30,z = 10) == 62: {e}')
    
    total += 1
    try:
        result = candidate(x = 30,y = 10,z = 20) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 30,y = 10,z = 20) == 82: {e}')
    
    total += 1
    try:
        result = candidate(x = 20,y = 25,z = 30) == 142
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 20,y = 25,z = 30) == 142: {e}')
    
    total += 1
    try:
        result = candidate(x = 15,y = 15,z = 1) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 15,y = 15,z = 1) == 62: {e}')
    
    total += 1
    try:
        result = candidate(x = 35,y = 5,z = 10) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 35,y = 5,z = 10) == 42: {e}')
    
    total += 1
    try:
        result = candidate(x = 40,y = 10,z = 20) == 82
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 40,y = 10,z = 20) == 82: {e}')
    
    total += 1
    try:
        result = candidate(x = 50,y = 1,z = 50) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 50,y = 1,z = 50) == 106: {e}')
    
    total += 1
    try:
        result = candidate(x = 10,y = 20,z = 15) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(x = 10,y = 20,z = 15) == 72: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(x = 1,y = 10,z = 10) == 26
    assert candidate(x = 50,y = 50,z = 50) == 300
    assert candidate(x = 10,y = 1,z = 10) == 26
    assert candidate(x = 20,y = 10,z = 5) == 52
    assert candidate(x = 10,y = 10,z = 100) == 240
    assert candidate(x = 10,y = 10,z = 1) == 42
    assert candidate(x = 2,y = 5,z = 1) == 12
    assert candidate(x = 1,y = 1,z = 1) == 6
    assert candidate(x = 3,y = 2,z = 2) == 14
    assert candidate(x = 49,y = 50,z = 1) == 200
    assert candidate(x = 40,y = 1,z = 2) == 10
    assert candidate(x = 40,y = 40,z = 30) == 220
    assert candidate(x = 50,y = 49,z = 49) == 296
    assert candidate(x = 5,y = 1,z = 5) == 16
    assert candidate(x = 50,y = 1,z = 1) == 8
    assert candidate(x = 2,y = 1,z = 10) == 26
    assert candidate(x = 10,y = 10,z = 30) == 100
    assert candidate(x = 25,y = 25,z = 10) == 120
    assert candidate(x = 10,y = 15,z = 8) == 58
    assert candidate(x = 2,y = 10,z = 0) == 10
    assert candidate(x = 0,y = 5,z = 10) == 22
    assert candidate(x = 35,y = 15,z = 5) == 72
    assert candidate(x = 25,y = 1,z = 25) == 56
    assert candidate(x = 2,y = 50,z = 25) == 60
    assert candidate(x = 7,y = 7,z = 14) == 56
    assert candidate(x = 30,y = 30,z = 25) == 170
    assert candidate(x = 25,y = 20,z = 10) == 102
    assert candidate(x = 5,y = 5,z = 45) == 110
    assert candidate(x = 5,y = 5,z = 10) == 40
    assert candidate(x = 30,y = 20,z = 10) == 102
    assert candidate(x = 33,y = 33,z = 34) == 200
    assert candidate(x = 30,y = 15,z = 25) == 112
    assert candidate(x = 40,y = 10,z = 30) == 102
    assert candidate(x = 15,y = 15,z = 25) == 110
    assert candidate(x = 30,y = 25,z = 30) == 162
    assert candidate(x = 1,y = 30,z = 5) == 16
    assert candidate(x = 10,y = 5,z = 15) == 52
    assert candidate(x = 15,y = 15,z = 5) == 70
    assert candidate(x = 20,y = 20,z = 1) == 82
    assert candidate(x = 50,y = 10,z = 1) == 44
    assert candidate(x = 20,y = 1,z = 30) == 66
    assert candidate(x = 20,y = 15,z = 20) == 102
    assert candidate(x = 40,y = 30,z = 20) == 162
    assert candidate(x = 10,y = 15,z = 20) == 82
    assert candidate(x = 20,y = 30,z = 40) == 162
    assert candidate(x = 5,y = 5,z = 50) == 120
    assert candidate(x = 10,y = 10,z = 10) == 60
    assert candidate(x = 40,y = 10,z = 1) == 44
    assert candidate(x = 10,y = 35,z = 5) == 52
    assert candidate(x = 1,y = 1,z = 50) == 104
    assert candidate(x = 30,y = 20,z = 30) == 142
    assert candidate(x = 15,y = 25,z = 30) == 122
    assert candidate(x = 5,y = 5,z = 40) == 100
    assert candidate(x = 2,y = 2,z = 4) == 16
    assert candidate(x = 10,y = 1,z = 50) == 106
    assert candidate(x = 45,y = 40,z = 45) == 252
    assert candidate(x = 45,y = 5,z = 5) == 32
    assert candidate(x = 45,y = 30,z = 25) == 172
    assert candidate(x = 5,y = 10,z = 40) == 102
    assert candidate(x = 10,y = 10,z = 15) == 70
    assert candidate(x = 10,y = 10,z = 40) == 120
    assert candidate(x = 2,y = 2,z = 3) == 14
    assert candidate(x = 20,y = 20,z = 30) == 140
    assert candidate(x = 40,y = 10,z = 10) == 62
    assert candidate(x = 25,y = 25,z = 1) == 102
    assert candidate(x = 49,y = 50,z = 49) == 296
    assert candidate(x = 15,y = 15,z = 30) == 120
    assert candidate(x = 4,y = 3,z = 6) == 26
    assert candidate(x = 10,y = 10,z = 5) == 50
    assert candidate(x = 10,y = 40,z = 20) == 82
    assert candidate(x = 1,y = 50,z = 1) == 8
    assert candidate(x = 20,y = 15,z = 25) == 112
    assert candidate(x = 1,y = 50,z = 49) == 104
    assert candidate(x = 25,y = 25,z = 25) == 150
    assert candidate(x = 20,y = 20,z = 20) == 120
    assert candidate(x = 20,y = 20,z = 10) == 100
    assert candidate(x = 25,y = 20,z = 30) == 142
    assert candidate(x = 1,y = 50,z = 50) == 106
    assert candidate(x = 30,y = 40,z = 35) == 192
    assert candidate(x = 30,y = 30,z = 1) == 122
    assert candidate(x = 10,y = 30,z = 10) == 62
    assert candidate(x = 30,y = 10,z = 20) == 82
    assert candidate(x = 20,y = 25,z = 30) == 142
    assert candidate(x = 15,y = 15,z = 1) == 62
    assert candidate(x = 35,y = 5,z = 10) == 42
    assert candidate(x = 40,y = 10,z = 20) == 82
    assert candidate(x = 50,y = 1,z = 50) == 106
    assert candidate(x = 10,y = 20,z = 15) == 72


