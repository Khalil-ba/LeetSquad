def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 50,k = 50) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 50) == 48: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,k = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,k = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,k = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,k = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,k = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,k = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,k = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,k = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,k = 50) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,k = 50) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,k = 75) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,k = 75) == 21: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 36) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 36) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 300) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 300) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 270) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 270) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 101) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 101) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 99) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 99) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 33,k = 231) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 33,k = 231) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 23,k = 60) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23,k = 60) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 47) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 47) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 85) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 85) == 27: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,k = 150) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,k = 150) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 199) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 199) == 35: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,k = 99) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,k = 99) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 90) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 90) == 26: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,k = 99) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,k = 99) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 17,k = 75) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17,k = 75) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 60) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 60) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 100) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 100) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 23,k = 115) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 23,k = 115) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 29,k = 87) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 29,k = 87) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 75) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 75) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 200) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 200) == 34: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,k = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,k = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 49) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 49) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 32,k = 150) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 32,k = 150) == 26: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 80) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 80) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 37,k = 110) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 37,k = 110) == 34: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 250) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 250) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 85) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 85) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 17,k = 85) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 17,k = 85) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 225) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 225) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 41,k = 90) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 41,k = 90) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 140) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 140) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 150) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 150) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 100) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 100) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 180) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 180) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 22,k = 55) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 22,k = 55) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 123) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 123) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 60) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 60) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,k = 63) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,k = 63) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,k = 49) == 47
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,k = 49) == 47: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 120) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 120) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,k = 100) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,k = 100) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 250) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 250) == 44: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,k = 196) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,k = 196) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,k = 90) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,k = 90) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 125) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 125) == 27: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 225) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 225) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 98) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 98) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 70) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 70) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,k = 48) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,k = 48) == 48: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 350) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 350) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 120) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 120) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,k = 140) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,k = 140) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 200) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 200) == 24: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 99) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 99) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 49) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 49) == 49: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 49) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 49) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 13,k = 195) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 13,k = 195) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 45,k = 180) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 45,k = 180) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,k = 199) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,k = 199) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 40,k = 400) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 40,k = 400) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,k = 225) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,k = 225) == 33: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,k = 175) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,k = 175) == 29: {e}')
    
    total += 1
    try:
        result = candidate(n = 27,k = 70) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 27,k = 70) == 18: {e}')
    
    total += 1
    try:
        result = candidate(n = 49,k = 98) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 49,k = 98) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,k = 120) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,k = 120) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 28,k = 120) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 28,k = 120) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,k = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,k = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 100) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 100) == 16: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,k = 180) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,k = 180) == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 50,k = 50) == 48
    assert candidate(n = 3,k = 5) == 1
    assert candidate(n = 2,k = 1) == 1
    assert candidate(n = 40,k = 20) == 20
    assert candidate(n = 5,k = 6) == 2
    assert candidate(n = 10,k = 15) == 3
    assert candidate(n = 2,k = 2) == 0
    assert candidate(n = 2,k = 50) == 0
    assert candidate(n = 4,k = 2) == 2
    assert candidate(n = 25,k = 50) == 2
    assert candidate(n = 49,k = 75) == 21
    assert candidate(n = 18,k = 36) == 2
    assert candidate(n = 20,k = 300) == 4
    assert candidate(n = 45,k = 270) == 6
    assert candidate(n = 45,k = 101) == 13
    assert candidate(n = 35,k = 99) == 31
    assert candidate(n = 33,k = 231) == 25
    assert candidate(n = 23,k = 60) == 16
    assert candidate(n = 15,k = 47) == 9
    assert candidate(n = 30,k = 85) == 27
    assert candidate(n = 12,k = 150) == 4
    assert candidate(n = 40,k = 199) == 35
    assert candidate(n = 49,k = 99) == 3
    assert candidate(n = 30,k = 90) == 26
    assert candidate(n = 50,k = 100) == 2
    assert candidate(n = 28,k = 99) == 9
    assert candidate(n = 17,k = 75) == 11
    assert candidate(n = 20,k = 60) == 16
    assert candidate(n = 45,k = 100) == 12
    assert candidate(n = 23,k = 115) == 17
    assert candidate(n = 29,k = 87) == 25
    assert candidate(n = 20,k = 75) == 1
    assert candidate(n = 40,k = 200) == 34
    assert candidate(n = 8,k = 100) == 2
    assert candidate(n = 35,k = 49) == 19
    assert candidate(n = 32,k = 150) == 26
    assert candidate(n = 18,k = 80) == 12
    assert candidate(n = 37,k = 110) == 34
    assert candidate(n = 30,k = 250) == 18
    assert candidate(n = 40,k = 85) == 7
    assert candidate(n = 17,k = 85) == 11
    assert candidate(n = 15,k = 225) == 1
    assert candidate(n = 41,k = 90) == 10
    assert candidate(n = 35,k = 140) == 4
    assert candidate(n = 15,k = 150) == 10
    assert candidate(n = 35,k = 100) == 32
    assert candidate(n = 18,k = 180) == 10
    assert candidate(n = 22,k = 55) == 13
    assert candidate(n = 50,k = 123) == 25
    assert candidate(n = 15,k = 60) == 4
    assert candidate(n = 28,k = 63) == 9
    assert candidate(n = 49,k = 49) == 47
    assert candidate(n = 35,k = 120) == 16
    assert candidate(n = 28,k = 100) == 8
    assert candidate(n = 50,k = 250) == 44
    assert candidate(n = 28,k = 196) == 20
    assert candidate(n = 18,k = 90) == 12
    assert candidate(n = 50,k = 125) == 27
    assert candidate(n = 30,k = 225) == 7
    assert candidate(n = 30,k = 98) == 18
    assert candidate(n = 35,k = 70) == 2
    assert candidate(n = 49,k = 48) == 48
    assert candidate(n = 35,k = 350) == 10
    assert candidate(n = 45,k = 120) == 32
    assert candidate(n = 28,k = 140) == 22
    assert candidate(n = 45,k = 200) == 24
    assert candidate(n = 20,k = 99) == 15
    assert candidate(n = 50,k = 49) == 49
    assert candidate(n = 20,k = 49) == 11
    assert candidate(n = 13,k = 195) == 3
    assert candidate(n = 45,k = 180) == 4
    assert candidate(n = 20,k = 199) == 9
    assert candidate(n = 40,k = 400) == 10
    assert candidate(n = 49,k = 225) == 33
    assert candidate(n = 35,k = 175) == 29
    assert candidate(n = 27,k = 70) == 18
    assert candidate(n = 49,k = 98) == 2
    assert candidate(n = 15,k = 120) == 8
    assert candidate(n = 28,k = 120) == 12
    assert candidate(n = 50,k = 25) == 25
    assert candidate(n = 30,k = 100) == 16
    assert candidate(n = 30,k = 180) == 6


