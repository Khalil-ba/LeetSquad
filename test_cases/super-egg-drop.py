def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(k = 2,n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2,n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 5,n = 1000) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5,n = 1000) == 11: {e}')
    
    total += 1
    try:
        result = candidate(k = 1,n = 100) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1,n = 100) == 100: {e}')
    
    total += 1
    try:
        result = candidate(k = 1,n = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1,n = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(k = 2,n = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2,n = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(k = 50,n = 10000) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50,n = 10000) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 10,n = 5000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10,n = 5000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 10,n = 1000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10,n = 1000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(k = 2,n = 100) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2,n = 100) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 2,n = 1000) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2,n = 1000) == 45: {e}')
    
    total += 1
    try:
        result = candidate(k = 3,n = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3,n = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(k = 100,n = 10000) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100,n = 10000) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 3,n = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3,n = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(k = 10,n = 10000) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10,n = 10000) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 3,n = 14) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3,n = 14) == 4: {e}')
    
    total += 1
    try:
        result = candidate(k = 1,n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 1,n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 8,n = 9000) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8,n = 9000) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 3,n = 20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3,n = 20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(k = 7,n = 5000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7,n = 5000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 3,n = 50) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3,n = 50) == 7: {e}')
    
    total += 1
    try:
        result = candidate(k = 2,n = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2,n = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(k = 10,n = 200) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10,n = 200) == 8: {e}')
    
    total += 1
    try:
        result = candidate(k = 3,n = 1000) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3,n = 1000) == 19: {e}')
    
    total += 1
    try:
        result = candidate(k = 4,n = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4,n = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(k = 24,n = 450) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 24,n = 450) == 9: {e}')
    
    total += 1
    try:
        result = candidate(k = 15,n = 3000) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 15,n = 3000) == 12: {e}')
    
    total += 1
    try:
        result = candidate(k = 6,n = 3000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 6,n = 3000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 10,n = 500) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10,n = 500) == 9: {e}')
    
    total += 1
    try:
        result = candidate(k = 50,n = 7500) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50,n = 7500) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 20,n = 3000) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 20,n = 3000) == 12: {e}')
    
    total += 1
    try:
        result = candidate(k = 5,n = 100) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5,n = 100) == 7: {e}')
    
    total += 1
    try:
        result = candidate(k = 5,n = 5000) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5,n = 5000) == 16: {e}')
    
    total += 1
    try:
        result = candidate(k = 50,n = 750) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50,n = 750) == 10: {e}')
    
    total += 1
    try:
        result = candidate(k = 75,n = 9000) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 75,n = 9000) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 70,n = 950) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 70,n = 950) == 10: {e}')
    
    total += 1
    try:
        result = candidate(k = 50,n = 1000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50,n = 1000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(k = 75,n = 9900) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 75,n = 9900) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 90,n = 9999) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 90,n = 9999) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 4,n = 2000) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4,n = 2000) == 16: {e}')
    
    total += 1
    try:
        result = candidate(k = 25,n = 8000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 25,n = 8000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 4,n = 20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4,n = 20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(k = 25,n = 7500) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 25,n = 7500) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 4,n = 30) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4,n = 30) == 5: {e}')
    
    total += 1
    try:
        result = candidate(k = 50,n = 7000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50,n = 7000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 20,n = 4000) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 20,n = 4000) == 12: {e}')
    
    total += 1
    try:
        result = candidate(k = 40,n = 650) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 40,n = 650) == 10: {e}')
    
    total += 1
    try:
        result = candidate(k = 60,n = 8000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 60,n = 8000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 8,n = 150) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8,n = 150) == 8: {e}')
    
    total += 1
    try:
        result = candidate(k = 90,n = 10000) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 90,n = 10000) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 3,n = 1234) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3,n = 1234) == 20: {e}')
    
    total += 1
    try:
        result = candidate(k = 5,n = 10000) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5,n = 10000) == 18: {e}')
    
    total += 1
    try:
        result = candidate(k = 3,n = 100) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3,n = 100) == 9: {e}')
    
    total += 1
    try:
        result = candidate(k = 25,n = 6000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 25,n = 6000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 25,n = 500) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 25,n = 500) == 9: {e}')
    
    total += 1
    try:
        result = candidate(k = 4,n = 4096) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4,n = 4096) == 19: {e}')
    
    total += 1
    try:
        result = candidate(k = 75,n = 10000) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 75,n = 10000) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 4,n = 256) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4,n = 256) == 10: {e}')
    
    total += 1
    try:
        result = candidate(k = 5,n = 500) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5,n = 500) == 10: {e}')
    
    total += 1
    try:
        result = candidate(k = 30,n = 550) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 30,n = 550) == 10: {e}')
    
    total += 1
    try:
        result = candidate(k = 60,n = 9500) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 60,n = 9500) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 75,n = 8000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 75,n = 8000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 10,n = 3000) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10,n = 3000) == 12: {e}')
    
    total += 1
    try:
        result = candidate(k = 50,n = 9000) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50,n = 9000) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 10,n = 2000) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 10,n = 2000) == 11: {e}')
    
    total += 1
    try:
        result = candidate(k = 60,n = 850) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 60,n = 850) == 10: {e}')
    
    total += 1
    try:
        result = candidate(k = 2,n = 32) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2,n = 32) == 8: {e}')
    
    total += 1
    try:
        result = candidate(k = 80,n = 9999) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 80,n = 9999) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 5,n = 50) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 5,n = 50) == 6: {e}')
    
    total += 1
    try:
        result = candidate(k = 20,n = 8000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 20,n = 8000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 100,n = 5000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100,n = 5000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 99,n = 9999) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 99,n = 9999) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 4,n = 100) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4,n = 100) == 8: {e}')
    
    total += 1
    try:
        result = candidate(k = 4,n = 700) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 4,n = 700) == 12: {e}')
    
    total += 1
    try:
        result = candidate(k = 100,n = 9999) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100,n = 9999) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 75,n = 7500) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 75,n = 7500) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 6,n = 2000) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 6,n = 2000) == 12: {e}')
    
    total += 1
    try:
        result = candidate(k = 8,n = 4000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8,n = 4000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 100,n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 100,n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(k = 8,n = 8192) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8,n = 8192) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 8,n = 200) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 8,n = 200) == 8: {e}')
    
    total += 1
    try:
        result = candidate(k = 50,n = 5000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 50,n = 5000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 3,n = 250) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 3,n = 250) == 12: {e}')
    
    total += 1
    try:
        result = candidate(k = 90,n = 9000) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 90,n = 9000) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 90,n = 9500) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 90,n = 9500) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 2,n = 10000) == 141
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 2,n = 10000) == 141: {e}')
    
    total += 1
    try:
        result = candidate(k = 12,n = 250) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 12,n = 250) == 8: {e}')
    
    total += 1
    try:
        result = candidate(k = 15,n = 5000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 15,n = 5000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 20,n = 9000) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 20,n = 9000) == 14: {e}')
    
    total += 1
    try:
        result = candidate(k = 18,n = 350) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 18,n = 350) == 9: {e}')
    
    total += 1
    try:
        result = candidate(k = 6,n = 70) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 6,n = 70) == 7: {e}')
    
    total += 1
    try:
        result = candidate(k = 20,n = 5000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 20,n = 5000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(k = 7,n = 3456) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(k = 7,n = 3456) == 13: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(k = 2,n = 1) == 1
    assert candidate(k = 5,n = 1000) == 11
    assert candidate(k = 1,n = 100) == 100
    assert candidate(k = 1,n = 2) == 2
    assert candidate(k = 2,n = 6) == 3
    assert candidate(k = 50,n = 10000) == 14
    assert candidate(k = 10,n = 5000) == 13
    assert candidate(k = 10,n = 1000) == 10
    assert candidate(k = 2,n = 100) == 14
    assert candidate(k = 2,n = 1000) == 45
    assert candidate(k = 3,n = 5) == 3
    assert candidate(k = 100,n = 10000) == 14
    assert candidate(k = 3,n = 25) == 5
    assert candidate(k = 10,n = 10000) == 14
    assert candidate(k = 3,n = 14) == 4
    assert candidate(k = 1,n = 1) == 1
    assert candidate(k = 8,n = 9000) == 14
    assert candidate(k = 3,n = 20) == 5
    assert candidate(k = 7,n = 5000) == 13
    assert candidate(k = 3,n = 50) == 7
    assert candidate(k = 2,n = 10) == 4
    assert candidate(k = 10,n = 200) == 8
    assert candidate(k = 3,n = 1000) == 19
    assert candidate(k = 4,n = 25) == 5
    assert candidate(k = 24,n = 450) == 9
    assert candidate(k = 15,n = 3000) == 12
    assert candidate(k = 6,n = 3000) == 13
    assert candidate(k = 10,n = 500) == 9
    assert candidate(k = 50,n = 7500) == 13
    assert candidate(k = 20,n = 3000) == 12
    assert candidate(k = 5,n = 100) == 7
    assert candidate(k = 5,n = 5000) == 16
    assert candidate(k = 50,n = 750) == 10
    assert candidate(k = 75,n = 9000) == 14
    assert candidate(k = 70,n = 950) == 10
    assert candidate(k = 50,n = 1000) == 10
    assert candidate(k = 75,n = 9900) == 14
    assert candidate(k = 90,n = 9999) == 14
    assert candidate(k = 4,n = 2000) == 16
    assert candidate(k = 25,n = 8000) == 13
    assert candidate(k = 4,n = 20) == 5
    assert candidate(k = 25,n = 7500) == 13
    assert candidate(k = 4,n = 30) == 5
    assert candidate(k = 50,n = 7000) == 13
    assert candidate(k = 20,n = 4000) == 12
    assert candidate(k = 40,n = 650) == 10
    assert candidate(k = 60,n = 8000) == 13
    assert candidate(k = 8,n = 150) == 8
    assert candidate(k = 90,n = 10000) == 14
    assert candidate(k = 3,n = 1234) == 20
    assert candidate(k = 5,n = 10000) == 18
    assert candidate(k = 3,n = 100) == 9
    assert candidate(k = 25,n = 6000) == 13
    assert candidate(k = 25,n = 500) == 9
    assert candidate(k = 4,n = 4096) == 19
    assert candidate(k = 75,n = 10000) == 14
    assert candidate(k = 4,n = 256) == 10
    assert candidate(k = 5,n = 500) == 10
    assert candidate(k = 30,n = 550) == 10
    assert candidate(k = 60,n = 9500) == 14
    assert candidate(k = 75,n = 8000) == 13
    assert candidate(k = 10,n = 3000) == 12
    assert candidate(k = 50,n = 9000) == 14
    assert candidate(k = 10,n = 2000) == 11
    assert candidate(k = 60,n = 850) == 10
    assert candidate(k = 2,n = 32) == 8
    assert candidate(k = 80,n = 9999) == 14
    assert candidate(k = 5,n = 50) == 6
    assert candidate(k = 20,n = 8000) == 13
    assert candidate(k = 100,n = 5000) == 13
    assert candidate(k = 99,n = 9999) == 14
    assert candidate(k = 4,n = 100) == 8
    assert candidate(k = 4,n = 700) == 12
    assert candidate(k = 100,n = 9999) == 14
    assert candidate(k = 75,n = 7500) == 13
    assert candidate(k = 6,n = 2000) == 12
    assert candidate(k = 8,n = 4000) == 13
    assert candidate(k = 100,n = 1) == 1
    assert candidate(k = 8,n = 8192) == 14
    assert candidate(k = 8,n = 200) == 8
    assert candidate(k = 50,n = 5000) == 13
    assert candidate(k = 3,n = 250) == 12
    assert candidate(k = 90,n = 9000) == 14
    assert candidate(k = 90,n = 9500) == 14
    assert candidate(k = 2,n = 10000) == 141
    assert candidate(k = 12,n = 250) == 8
    assert candidate(k = 15,n = 5000) == 13
    assert candidate(k = 20,n = 9000) == 14
    assert candidate(k = 18,n = 350) == 9
    assert candidate(k = 6,n = 70) == 7
    assert candidate(k = 20,n = 5000) == 13
    assert candidate(k = 7,n = 3456) == 13


