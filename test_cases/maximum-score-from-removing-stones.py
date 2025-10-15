def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(a = 10,b = 10,c = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 10,c = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 7,c = 9) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 7,c = 9) == 10: {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 5,c = 5) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 5,c = 5) == 7: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 8,c = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 8,c = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 3,c = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 3,c = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = 100000,b = 1,c = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100000,b = 1,c = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = 100000,b = 100000,c = 100000) == 150000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100000,b = 100000,c = 100000) == 150000: {e}')
    
    total += 1
    try:
        result = candidate(a = 4,b = 4,c = 6) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 4,b = 4,c = 6) == 7: {e}')
    
    total += 1
    try:
        result = candidate(a = 30,b = 60,c = 90) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 30,b = 60,c = 90) == 90: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 1,c = 100000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 1,c = 100000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = 50000,b = 50000,c = 1) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 50000,b = 50000,c = 1) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 10,c = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 10,c = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 4,c = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 4,c = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 10,c = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 10,c = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(a = 20,b = 30,c = 40) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20,b = 30,c = 40) == 45: {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = 7,c = 14) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 7,c = 14) == 14: {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 1,c = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 1,c = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = 14,c = 10) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 14,c = 10) == 15: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 1,c = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 1,c = 2) == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = 8,c = 9) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 8,c = 9) == 12: {e}')
    
    total += 1
    try:
        result = candidate(a = 33333,b = 33333,c = 33334) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 33333,b = 33333,c = 33334) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(a = 50000,b = 50000,c = 50001) == 75000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 50000,b = 50000,c = 50001) == 75000: {e}')
    
    total += 1
    try:
        result = candidate(a = 1000,b = 1000,c = 1000) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1000,b = 1000,c = 1000) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(a = 80,b = 80,c = 40) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 80,b = 80,c = 40) == 100: {e}')
    
    total += 1
    try:
        result = candidate(a = 7,b = 14,c = 21) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 7,b = 14,c = 21) == 21: {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 15,c = 20) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 15,c = 20) == 22: {e}')
    
    total += 1
    try:
        result = candidate(a = 150000,b = 50000,c = 100000) == 150000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 150000,b = 50000,c = 100000) == 150000: {e}')
    
    total += 1
    try:
        result = candidate(a = 5000,b = 5001,c = 5002) == 7501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5000,b = 5001,c = 5002) == 7501: {e}')
    
    total += 1
    try:
        result = candidate(a = 33333,b = 66666,c = 100000) == 99999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 33333,b = 66666,c = 100000) == 99999: {e}')
    
    total += 1
    try:
        result = candidate(a = 50000,b = 1,c = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 50000,b = 1,c = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = 60000,b = 20000,c = 20000) == 40000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 60000,b = 20000,c = 20000) == 40000: {e}')
    
    total += 1
    try:
        result = candidate(a = 99999,b = 1,c = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 99999,b = 1,c = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 5,c = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 5,c = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(a = 80000,b = 80000,c = 1) == 80000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 80000,b = 80000,c = 1) == 80000: {e}')
    
    total += 1
    try:
        result = candidate(a = 99998,b = 99999,c = 100000) == 149998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 99998,b = 99999,c = 100000) == 149998: {e}')
    
    total += 1
    try:
        result = candidate(a = 20,b = 20,c = 20) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20,b = 20,c = 20) == 30: {e}')
    
    total += 1
    try:
        result = candidate(a = 50000,b = 40000,c = 30000) == 60000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 50000,b = 40000,c = 30000) == 60000: {e}')
    
    total += 1
    try:
        result = candidate(a = 10000,b = 10000,c = 1) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10000,b = 10000,c = 1) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 5,c = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 5,c = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(a = 10000,b = 10000,c = 10000) == 15000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10000,b = 10000,c = 10000) == 15000: {e}')
    
    total += 1
    try:
        result = candidate(a = 42,b = 27,c = 19) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 42,b = 27,c = 19) == 44: {e}')
    
    total += 1
    try:
        result = candidate(a = 45000,b = 45000,c = 10000) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 45000,b = 45000,c = 10000) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 2,c = 100000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 2,c = 100000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(a = 25,b = 25,c = 24) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 25,b = 25,c = 24) == 37: {e}')
    
    total += 1
    try:
        result = candidate(a = 500,b = 500,c = 1500) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 500,b = 500,c = 1500) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(a = 100,b = 200,c = 300) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100,b = 200,c = 300) == 300: {e}')
    
    total += 1
    try:
        result = candidate(a = 15,b = 15,c = 15) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 15,b = 15,c = 15) == 22: {e}')
    
    total += 1
    try:
        result = candidate(a = 25,b = 75,c = 125) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 25,b = 75,c = 125) == 100: {e}')
    
    total += 1
    try:
        result = candidate(a = 20,b = 20,c = 21) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20,b = 20,c = 21) == 30: {e}')
    
    total += 1
    try:
        result = candidate(a = 20000,b = 30000,c = 10000) == 30000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20000,b = 30000,c = 10000) == 30000: {e}')
    
    total += 1
    try:
        result = candidate(a = 20,b = 40,c = 60) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 20,b = 40,c = 60) == 60: {e}')
    
    total += 1
    try:
        result = candidate(a = 12345,b = 67890,c = 11111) == 23456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 12345,b = 67890,c = 11111) == 23456: {e}')
    
    total += 1
    try:
        result = candidate(a = 80000,b = 10000,c = 10000) == 20000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 80000,b = 10000,c = 10000) == 20000: {e}')
    
    total += 1
    try:
        result = candidate(a = 12345,b = 67890,c = 54321) == 66666
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 12345,b = 67890,c = 54321) == 66666: {e}')
    
    total += 1
    try:
        result = candidate(a = 5,b = 15,c = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5,b = 15,c = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(a = 2,b = 2,c = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 2,b = 2,c = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 1,c = 200000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 1,c = 200000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(a = 100,b = 100,c = 101) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100,b = 100,c = 101) == 150: {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 3,c = 9) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 3,c = 9) == 6: {e}')
    
    total += 1
    try:
        result = candidate(a = 15,b = 25,c = 35) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 15,b = 25,c = 35) == 37: {e}')
    
    total += 1
    try:
        result = candidate(a = 50000,b = 50000,c = 99999) == 99999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 50000,b = 50000,c = 99999) == 99999: {e}')
    
    total += 1
    try:
        result = candidate(a = 10000,b = 20000,c = 30000) == 30000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10000,b = 20000,c = 30000) == 30000: {e}')
    
    total += 1
    try:
        result = candidate(a = 10000,b = 5000,c = 5000) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10000,b = 5000,c = 5000) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(a = 25000,b = 25000,c = 50000) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 25000,b = 25000,c = 50000) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(a = 99999,b = 99998,c = 99997) == 149997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 99999,b = 99998,c = 99997) == 149997: {e}')
    
    total += 1
    try:
        result = candidate(a = 75,b = 25,c = 50) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 75,b = 25,c = 50) == 75: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 2,c = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 2,c = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(a = 10,b = 20,c = 30) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10,b = 20,c = 30) == 30: {e}')
    
    total += 1
    try:
        result = candidate(a = 3,b = 9,c = 9) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 3,b = 9,c = 9) == 10: {e}')
    
    total += 1
    try:
        result = candidate(a = 15,b = 10,c = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 15,b = 10,c = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(a = 30,b = 5,c = 25) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 30,b = 5,c = 25) == 30: {e}')
    
    total += 1
    try:
        result = candidate(a = 50,b = 50,c = 100) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 50,b = 50,c = 100) == 100: {e}')
    
    total += 1
    try:
        result = candidate(a = 100,b = 100,c = 100) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100,b = 100,c = 100) == 150: {e}')
    
    total += 1
    try:
        result = candidate(a = 99999,b = 99999,c = 99999) == 149998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 99999,b = 99999,c = 99999) == 149998: {e}')
    
    total += 1
    try:
        result = candidate(a = 100,b = 100,c = 1) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100,b = 100,c = 1) == 100: {e}')
    
    total += 1
    try:
        result = candidate(a = 50000,b = 49999,c = 49998) == 74998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 50000,b = 49999,c = 49998) == 74998: {e}')
    
    total += 1
    try:
        result = candidate(a = 50,b = 25,c = 25) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 50,b = 25,c = 25) == 50: {e}')
    
    total += 1
    try:
        result = candidate(a = 98765,b = 43210,c = 54321) == 97531
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 98765,b = 43210,c = 54321) == 97531: {e}')
    
    total += 1
    try:
        result = candidate(a = 5000,b = 5000,c = 10000) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 5000,b = 5000,c = 10000) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(a = 55,b = 15,c = 35) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 55,b = 15,c = 35) == 50: {e}')
    
    total += 1
    try:
        result = candidate(a = 33333,b = 33334,c = 33335) == 50001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 33333,b = 33334,c = 33335) == 50001: {e}')
    
    total += 1
    try:
        result = candidate(a = 10000,b = 10000,c = 5000) == 12500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 10000,b = 10000,c = 5000) == 12500: {e}')
    
    total += 1
    try:
        result = candidate(a = 30,b = 50,c = 20) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 30,b = 50,c = 20) == 50: {e}')
    
    total += 1
    try:
        result = candidate(a = 30,b = 30,c = 30) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 30,b = 30,c = 30) == 45: {e}')
    
    total += 1
    try:
        result = candidate(a = 60000,b = 40000,c = 20000) == 60000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 60000,b = 40000,c = 20000) == 60000: {e}')
    
    total += 1
    try:
        result = candidate(a = 1,b = 1,c = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 1,b = 1,c = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(a = 8,b = 8,c = 8) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 8,b = 8,c = 8) == 12: {e}')
    
    total += 1
    try:
        result = candidate(a = 100000,b = 50000,c = 50000) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(a = 100000,b = 50000,c = 50000) == 100000: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(a = 10,b = 10,c = 1) == 10
    assert candidate(a = 5,b = 7,c = 9) == 10
    assert candidate(a = 5,b = 5,c = 5) == 7
    assert candidate(a = 1,b = 8,c = 8) == 8
    assert candidate(a = 3,b = 3,c = 3) == 4
    assert candidate(a = 100000,b = 1,c = 1) == 2
    assert candidate(a = 100000,b = 100000,c = 100000) == 150000
    assert candidate(a = 4,b = 4,c = 6) == 7
    assert candidate(a = 30,b = 60,c = 90) == 90
    assert candidate(a = 1,b = 1,c = 100000) == 2
    assert candidate(a = 50000,b = 50000,c = 1) == 50000
    assert candidate(a = 10,b = 10,c = 10) == 15
    assert candidate(a = 2,b = 4,c = 6) == 6
    assert candidate(a = 5,b = 10,c = 15) == 15
    assert candidate(a = 20,b = 30,c = 40) == 45
    assert candidate(a = 7,b = 7,c = 14) == 14
    assert candidate(a = 10,b = 1,c = 1) == 2
    assert candidate(a = 7,b = 14,c = 10) == 15
    assert candidate(a = 1,b = 1,c = 2) == 2
    assert candidate(a = 7,b = 8,c = 9) == 12
    assert candidate(a = 33333,b = 33333,c = 33334) == 50000
    assert candidate(a = 50000,b = 50000,c = 50001) == 75000
    assert candidate(a = 1000,b = 1000,c = 1000) == 1500
    assert candidate(a = 80,b = 80,c = 40) == 100
    assert candidate(a = 7,b = 14,c = 21) == 21
    assert candidate(a = 10,b = 15,c = 20) == 22
    assert candidate(a = 150000,b = 50000,c = 100000) == 150000
    assert candidate(a = 5000,b = 5001,c = 5002) == 7501
    assert candidate(a = 33333,b = 66666,c = 100000) == 99999
    assert candidate(a = 50000,b = 1,c = 1) == 2
    assert candidate(a = 60000,b = 20000,c = 20000) == 40000
    assert candidate(a = 99999,b = 1,c = 1) == 2
    assert candidate(a = 5,b = 5,c = 100) == 10
    assert candidate(a = 80000,b = 80000,c = 1) == 80000
    assert candidate(a = 99998,b = 99999,c = 100000) == 149998
    assert candidate(a = 20,b = 20,c = 20) == 30
    assert candidate(a = 50000,b = 40000,c = 30000) == 60000
    assert candidate(a = 10000,b = 10000,c = 1) == 10000
    assert candidate(a = 5,b = 5,c = 10) == 10
    assert candidate(a = 10000,b = 10000,c = 10000) == 15000
    assert candidate(a = 42,b = 27,c = 19) == 44
    assert candidate(a = 45000,b = 45000,c = 10000) == 50000
    assert candidate(a = 2,b = 2,c = 100000) == 4
    assert candidate(a = 25,b = 25,c = 24) == 37
    assert candidate(a = 500,b = 500,c = 1500) == 1000
    assert candidate(a = 100,b = 200,c = 300) == 300
    assert candidate(a = 15,b = 15,c = 15) == 22
    assert candidate(a = 25,b = 75,c = 125) == 100
    assert candidate(a = 20,b = 20,c = 21) == 30
    assert candidate(a = 20000,b = 30000,c = 10000) == 30000
    assert candidate(a = 20,b = 40,c = 60) == 60
    assert candidate(a = 12345,b = 67890,c = 11111) == 23456
    assert candidate(a = 80000,b = 10000,c = 10000) == 20000
    assert candidate(a = 12345,b = 67890,c = 54321) == 66666
    assert candidate(a = 5,b = 15,c = 20) == 20
    assert candidate(a = 2,b = 2,c = 3) == 3
    assert candidate(a = 1,b = 1,c = 200000) == 2
    assert candidate(a = 100,b = 100,c = 101) == 150
    assert candidate(a = 3,b = 3,c = 9) == 6
    assert candidate(a = 15,b = 25,c = 35) == 37
    assert candidate(a = 50000,b = 50000,c = 99999) == 99999
    assert candidate(a = 10000,b = 20000,c = 30000) == 30000
    assert candidate(a = 10000,b = 5000,c = 5000) == 10000
    assert candidate(a = 25000,b = 25000,c = 50000) == 50000
    assert candidate(a = 99999,b = 99998,c = 99997) == 149997
    assert candidate(a = 75,b = 25,c = 50) == 75
    assert candidate(a = 1,b = 2,c = 3) == 3
    assert candidate(a = 10,b = 20,c = 30) == 30
    assert candidate(a = 3,b = 9,c = 9) == 10
    assert candidate(a = 15,b = 10,c = 5) == 15
    assert candidate(a = 30,b = 5,c = 25) == 30
    assert candidate(a = 50,b = 50,c = 100) == 100
    assert candidate(a = 100,b = 100,c = 100) == 150
    assert candidate(a = 99999,b = 99999,c = 99999) == 149998
    assert candidate(a = 100,b = 100,c = 1) == 100
    assert candidate(a = 50000,b = 49999,c = 49998) == 74998
    assert candidate(a = 50,b = 25,c = 25) == 50
    assert candidate(a = 98765,b = 43210,c = 54321) == 97531
    assert candidate(a = 5000,b = 5000,c = 10000) == 10000
    assert candidate(a = 55,b = 15,c = 35) == 50
    assert candidate(a = 33333,b = 33334,c = 33335) == 50001
    assert candidate(a = 10000,b = 10000,c = 5000) == 12500
    assert candidate(a = 30,b = 50,c = 20) == 50
    assert candidate(a = 30,b = 30,c = 30) == 45
    assert candidate(a = 60000,b = 40000,c = 20000) == 60000
    assert candidate(a = 1,b = 1,c = 1) == 1
    assert candidate(a = 8,b = 8,c = 8) == 12
    assert candidate(a = 100000,b = 50000,c = 50000) == 100000


