def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 1,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,k = 3) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,k = 3) == 49: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 17,k = 2) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17,k = 2) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 15) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 15) == 500: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 36,k = 6) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 36,k = 6) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 10) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 10) == 50: {e}')
    
    total += 1
    try:
        result = candidate(n = 84,k = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 84,k = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 7) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 7) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 9) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 9) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 97,k = 2) == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 97,k = 2) == 97: {e}')
    
    total += 1
    try:
        result = candidate(n = 17,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 4) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 4) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 37,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 60,k = 8) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60,k = 8) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 81,k = 4) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 81,k = 4) == 27: {e}')
    
    total += 1
    try:
        result = candidate(n = 60,k = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 60,k = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 11) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 11) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 120,k = 12) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120,k = 12) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 144,k = 9) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 144,k = 9) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 841,k = 3) == 841
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 841,k = 3) == 841: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,k = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,k = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 36,k = 8) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 36,k = 8) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 121,k = 3) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 121,k = 3) == 121: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 7) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 7) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 256,k = 7) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256,k = 7) == 64: {e}')
    
    total += 1
    try:
        result = candidate(n = 360,k = 15) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 360,k = 15) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 20) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 20) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 64,k = 7) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 64,k = 7) == 64: {e}')
    
    total += 1
    try:
        result = candidate(n = 504,k = 8) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 504,k = 8) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 625,k = 5) == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 625,k = 5) == 625: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 120,k = 7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 120,k = 7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 997,k = 2) == 997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 997,k = 2) == 997: {e}')
    
    total += 1
    try:
        result = candidate(n = 256,k = 8) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 256,k = 8) == 128: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 15) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 15) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 15) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 15) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 810,k = 16) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 810,k = 16) == 135: {e}')
    
    total += 1
    try:
        result = candidate(n = 841,k = 7) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 841,k = 7) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 441,k = 4) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 441,k = 4) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024,k = 9) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024,k = 9) == 256: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 3) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 3) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 18) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 18) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 16) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 16) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(n = 450,k = 15) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450,k = 15) == 90: {e}')
    
    total += 1
    try:
        result = candidate(n = 600,k = 15) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 600,k = 15) == 40: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,k = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,k = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 225,k = 8) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 225,k = 8) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 8) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 8) == 50: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,k = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,k = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 729,k = 6) == 243
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 729,k = 6) == 243: {e}')
    
    total += 1
    try:
        result = candidate(n = 504,k = 10) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 504,k = 10) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,k = 12) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,k = 12) == 500: {e}')
    
    total += 1
    try:
        result = candidate(n = 96,k = 10) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 96,k = 10) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 5) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 5) == 37: {e}')
    
    total += 1
    try:
        result = candidate(n = 343,k = 3) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 343,k = 3) == 49: {e}')
    
    total += 1
    try:
        result = candidate(n = 72,k = 9) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 72,k = 9) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 450,k = 20) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 450,k = 20) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1024,k = 10) == 512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1024,k = 10) == 512: {e}')
    
    total += 1
    try:
        result = candidate(n = 36,k = 11) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 36,k = 11) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 441,k = 5) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 441,k = 5) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 729,k = 12) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 729,k = 12) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,k = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,k = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 36,k = 7) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 36,k = 7) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 225,k = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 225,k = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,k = 20) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,k = 20) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,k = 9) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,k = 9) == 100: {e}')
    
    total += 1
    try:
        result = candidate(n = 16,k = 5) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16,k = 5) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 625,k = 6) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 625,k = 6) == -1: {e}')
    
    total += 1
    try:
        result = candidate(n = 840,k = 10) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 840,k = 10) == 12: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 1,k = 1) == 1
    assert candidate(n = 49,k = 3) == 49
    assert candidate(n = 100,k = 5) == 10
    assert candidate(n = 7,k = 2) == 7
    assert candidate(n = 17,k = 2) == 17
    assert candidate(n = 1000,k = 15) == 500
    assert candidate(n = 30,k = 5) == 6
    assert candidate(n = 12,k = 3) == 3
    assert candidate(n = 30,k = 1) == 1
    assert candidate(n = 100,k = 10) == -1
    assert candidate(n = 36,k = 6) == 9
    assert candidate(n = 1000,k = 10) == 50
    assert candidate(n = 84,k = 5) == 6
    assert candidate(n = 500,k = 7) == 25
    assert candidate(n = 999,k = 9) == -1
    assert candidate(n = 97,k = 2) == 97
    assert candidate(n = 17,k = 1) == 1
    assert candidate(n = 4,k = 4) == -1
    assert candidate(n = 50,k = 5) == 25
    assert candidate(n = 37,k = 1) == 1
    assert candidate(n = 60,k = 8) == 12
    assert candidate(n = 81,k = 4) == 27
    assert candidate(n = 60,k = 6) == 6
    assert candidate(n = 100,k = 11) == -1
    assert candidate(n = 120,k = 12) == 24
    assert candidate(n = 144,k = 9) == 16
    assert candidate(n = 841,k = 3) == 841
    assert candidate(n = 49,k = 2) == 7
    assert candidate(n = 36,k = 8) == 18
    assert candidate(n = 121,k = 3) == 121
    assert candidate(n = 100,k = 7) == 25
    assert candidate(n = 256,k = 7) == 64
    assert candidate(n = 360,k = 15) == 30
    assert candidate(n = 999,k = 20) == -1
    assert candidate(n = 64,k = 7) == 64
    assert candidate(n = 504,k = 8) == 9
    assert candidate(n = 625,k = 5) == 625
    assert candidate(n = 15,k = 3) == 5
    assert candidate(n = 120,k = 7) == 8
    assert candidate(n = 997,k = 2) == 997
    assert candidate(n = 256,k = 8) == 128
    assert candidate(n = 999,k = 15) == -1
    assert candidate(n = 500,k = 15) == -1
    assert candidate(n = 810,k = 16) == 135
    assert candidate(n = 841,k = 7) == -1
    assert candidate(n = 45,k = 5) == 15
    assert candidate(n = 441,k = 4) == 9
    assert candidate(n = 1024,k = 9) == 256
    assert candidate(n = 200,k = 1) == 1
    assert candidate(n = 999,k = 3) == 9
    assert candidate(n = 25,k = 3) == 25
    assert candidate(n = 1000,k = 18) == -1
    assert candidate(n = 1000,k = 16) == 1000
    assert candidate(n = 450,k = 15) == 90
    assert candidate(n = 600,k = 15) == 40
    assert candidate(n = 6,k = 4) == 6
    assert candidate(n = 225,k = 8) == 75
    assert candidate(n = 500,k = 8) == 50
    assert candidate(n = 9,k = 3) == 9
    assert candidate(n = 729,k = 6) == 243
    assert candidate(n = 504,k = 10) == 14
    assert candidate(n = 500,k = 12) == 500
    assert candidate(n = 96,k = 10) == 32
    assert candidate(n = 999,k = 5) == 37
    assert candidate(n = 343,k = 3) == 49
    assert candidate(n = 72,k = 9) == 18
    assert candidate(n = 450,k = 20) == -1
    assert candidate(n = 1000,k = 1) == 1
    assert candidate(n = 1024,k = 10) == 512
    assert candidate(n = 36,k = 11) == -1
    assert candidate(n = 441,k = 5) == 21
    assert candidate(n = 729,k = 12) == -1
    assert candidate(n = 999,k = 10) == -1
    assert candidate(n = 36,k = 7) == 12
    assert candidate(n = 50,k = 3) == 5
    assert candidate(n = 225,k = 5) == 15
    assert candidate(n = 200,k = 20) == -1
    assert candidate(n = 100,k = 9) == 100
    assert candidate(n = 16,k = 5) == 16
    assert candidate(n = 625,k = 6) == -1
    assert candidate(n = 840,k = 10) == 12


