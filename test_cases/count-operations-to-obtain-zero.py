def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num1 = 0,num2 = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 0,num2 = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 100,num2 = 1) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 100,num2 = 1) == 100: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 123,num2 = 456) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 123,num2 = 456) == 12: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 8,num2 = 12) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 8,num2 = 12) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1,num2 = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1,num2 = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 100000,num2 = 100000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 100000,num2 = 100000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 100000,num2 = 1) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 100000,num2 = 1) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 100,num2 = 50) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 100,num2 = 50) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 5,num2 = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 5,num2 = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2,num2 = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2,num2 = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 10,num2 = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 10,num2 = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 7,num2 = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 7,num2 = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 81,num2 = 27) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 81,num2 = 27) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 99999,num2 = 1) == 99999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 99999,num2 = 1) == 99999: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 333,num2 = 111) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 333,num2 = 111) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 10000,num2 = 9999) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 10000,num2 = 9999) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2020,num2 = 1870) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2020,num2 = 1870) == 22: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 60,num2 = 20) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 60,num2 = 20) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 101,num2 = 100) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 101,num2 = 100) == 101: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 42,num2 = 29) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 42,num2 = 29) == 10: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 100000,num2 = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 100000,num2 = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 45678,num2 = 45678) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 45678,num2 = 45678) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 88888,num2 = 22222) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 88888,num2 = 22222) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 618,num2 = 359) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 618,num2 = 359) == 15: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 100000,num2 = 99999) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 100000,num2 = 99999) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 42,num2 = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 42,num2 = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 98765,num2 = 43210) == 1241
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 98765,num2 = 43210) == 1241: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2,num2 = 34567) == 17285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2,num2 = 34567) == 17285: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1,num2 = 99999) == 99999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1,num2 = 99999) == 99999: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1000,num2 = 333) == 336
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1000,num2 = 333) == 336: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 88888,num2 = 11111) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 88888,num2 = 11111) == 8: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 9,num2 = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 9,num2 = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1000,num2 = 1) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1000,num2 = 1) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 55555,num2 = 22222) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 55555,num2 = 22222) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 87,num2 = 3) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 87,num2 = 3) == 29: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 15,num2 = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 15,num2 = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 60000,num2 = 30000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 60000,num2 = 30000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 22222,num2 = 11111) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 22222,num2 = 11111) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 65536,num2 = 1) == 65536
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 65536,num2 = 1) == 65536: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 65432,num2 = 12345) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 65432,num2 = 12345) == 80: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 20,num2 = 30) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 20,num2 = 30) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 50000,num2 = 25000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 50000,num2 = 25000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 13579,num2 = 24680) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 13579,num2 = 24680) == 39: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 777,num2 = 111) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 777,num2 = 111) == 7: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 88888,num2 = 44444) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 88888,num2 = 44444) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 12345,num2 = 54321) == 177
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 12345,num2 = 54321) == 177: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 5000,num2 = 7500) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 5000,num2 = 7500) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 25,num2 = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 25,num2 = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 23456,num2 = 65432) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 23456,num2 = 65432) == 44: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 45678,num2 = 87654) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 45678,num2 = 87654) == 45: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 12345,num2 = 67890) == 418
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 12345,num2 = 67890) == 418: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 42,num2 = 30) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 42,num2 = 30) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 789,num2 = 987) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 789,num2 = 987) == 70: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 99999,num2 = 99999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 99999,num2 = 99999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 456,num2 = 123) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 456,num2 = 123) == 12: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 0,num2 = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 0,num2 = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 55,num2 = 20) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 55,num2 = 20) == 6: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 33333,num2 = 22222) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 33333,num2 = 22222) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 54321,num2 = 12345) == 177
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 54321,num2 = 12345) == 177: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1,num2 = 100000) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1,num2 = 100000) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 32768,num2 = 16384) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 32768,num2 = 16384) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 1000,num2 = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 1000,num2 = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 2,num2 = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 2,num2 = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 101010,num2 = 10101) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 101010,num2 = 10101) == 10: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 75,num2 = 25) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 75,num2 = 25) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 83456,num2 = 37821) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 83456,num2 = 37821) == 38: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 23456,num2 = 12345) == 262
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 23456,num2 = 12345) == 262: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 123,num2 = 321) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 123,num2 = 321) == 11: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 8,num2 = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 8,num2 = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 50,num2 = 25) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 50,num2 = 25) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 13,num2 = 13) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 13,num2 = 13) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 12345,num2 = 1) == 12345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 12345,num2 = 1) == 12345: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 55555,num2 = 55555) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 55555,num2 = 55555) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 3,num2 = 8) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 3,num2 = 8) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 30000,num2 = 15000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 30000,num2 = 15000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 999,num2 = 999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 999,num2 = 999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 56789,num2 = 12345) == 260
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 56789,num2 = 12345) == 260: {e}')
    
    total += 1
    try:
        result = candidate(num1 = 25,num2 = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num1 = 25,num2 = 15) == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num1 = 0,num2 = 5) == 0
    assert candidate(num1 = 100,num2 = 1) == 100
    assert candidate(num1 = 123,num2 = 456) == 12
    assert candidate(num1 = 8,num2 = 12) == 3
    assert candidate(num1 = 1,num2 = 1) == 1
    assert candidate(num1 = 100000,num2 = 100000) == 1
    assert candidate(num1 = 100000,num2 = 1) == 100000
    assert candidate(num1 = 100,num2 = 50) == 2
    assert candidate(num1 = 5,num2 = 0) == 0
    assert candidate(num1 = 2,num2 = 3) == 3
    assert candidate(num1 = 10,num2 = 10) == 1
    assert candidate(num1 = 7,num2 = 3) == 5
    assert candidate(num1 = 81,num2 = 27) == 3
    assert candidate(num1 = 99999,num2 = 1) == 99999
    assert candidate(num1 = 333,num2 = 111) == 3
    assert candidate(num1 = 10000,num2 = 9999) == 10000
    assert candidate(num1 = 2020,num2 = 1870) == 22
    assert candidate(num1 = 60,num2 = 20) == 3
    assert candidate(num1 = 101,num2 = 100) == 101
    assert candidate(num1 = 42,num2 = 29) == 10
    assert candidate(num1 = 100000,num2 = 0) == 0
    assert candidate(num1 = 45678,num2 = 45678) == 1
    assert candidate(num1 = 88888,num2 = 22222) == 4
    assert candidate(num1 = 618,num2 = 359) == 15
    assert candidate(num1 = 100000,num2 = 99999) == 100000
    assert candidate(num1 = 42,num2 = 7) == 6
    assert candidate(num1 = 98765,num2 = 43210) == 1241
    assert candidate(num1 = 2,num2 = 34567) == 17285
    assert candidate(num1 = 1,num2 = 99999) == 99999
    assert candidate(num1 = 1000,num2 = 333) == 336
    assert candidate(num1 = 88888,num2 = 11111) == 8
    assert candidate(num1 = 9,num2 = 1) == 9
    assert candidate(num1 = 1000,num2 = 1) == 1000
    assert candidate(num1 = 55555,num2 = 22222) == 4
    assert candidate(num1 = 87,num2 = 3) == 29
    assert candidate(num1 = 15,num2 = 10) == 3
    assert candidate(num1 = 60000,num2 = 30000) == 2
    assert candidate(num1 = 22222,num2 = 11111) == 2
    assert candidate(num1 = 65536,num2 = 1) == 65536
    assert candidate(num1 = 65432,num2 = 12345) == 80
    assert candidate(num1 = 20,num2 = 30) == 3
    assert candidate(num1 = 50000,num2 = 25000) == 2
    assert candidate(num1 = 13579,num2 = 24680) == 39
    assert candidate(num1 = 777,num2 = 111) == 7
    assert candidate(num1 = 88888,num2 = 44444) == 2
    assert candidate(num1 = 12345,num2 = 54321) == 177
    assert candidate(num1 = 5000,num2 = 7500) == 3
    assert candidate(num1 = 25,num2 = 5) == 5
    assert candidate(num1 = 23456,num2 = 65432) == 44
    assert candidate(num1 = 45678,num2 = 87654) == 45
    assert candidate(num1 = 12345,num2 = 67890) == 418
    assert candidate(num1 = 42,num2 = 30) == 5
    assert candidate(num1 = 789,num2 = 987) == 70
    assert candidate(num1 = 99999,num2 = 99999) == 1
    assert candidate(num1 = 456,num2 = 123) == 12
    assert candidate(num1 = 0,num2 = 0) == 0
    assert candidate(num1 = 55,num2 = 20) == 6
    assert candidate(num1 = 33333,num2 = 22222) == 3
    assert candidate(num1 = 54321,num2 = 12345) == 177
    assert candidate(num1 = 1,num2 = 100000) == 100000
    assert candidate(num1 = 32768,num2 = 16384) == 2
    assert candidate(num1 = 1000,num2 = 100) == 10
    assert candidate(num1 = 2,num2 = 8) == 4
    assert candidate(num1 = 101010,num2 = 10101) == 10
    assert candidate(num1 = 75,num2 = 25) == 3
    assert candidate(num1 = 83456,num2 = 37821) == 38
    assert candidate(num1 = 23456,num2 = 12345) == 262
    assert candidate(num1 = 123,num2 = 321) == 11
    assert candidate(num1 = 8,num2 = 3) == 5
    assert candidate(num1 = 50,num2 = 25) == 2
    assert candidate(num1 = 13,num2 = 13) == 1
    assert candidate(num1 = 12345,num2 = 1) == 12345
    assert candidate(num1 = 55555,num2 = 55555) == 1
    assert candidate(num1 = 3,num2 = 8) == 5
    assert candidate(num1 = 30000,num2 = 15000) == 2
    assert candidate(num1 = 999,num2 = 999) == 1
    assert candidate(num1 = 56789,num2 = 12345) == 260
    assert candidate(num1 = 25,num2 = 15) == 4


