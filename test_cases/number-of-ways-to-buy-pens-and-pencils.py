def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(total = 20,cost1 = 10,cost2 = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 20,cost1 = 10,cost2 = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(total = 1000,cost1 = 1,cost2 = 1) == 501501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1000,cost1 = 1,cost2 = 1) == 501501: {e}')
    
    total += 1
    try:
        result = candidate(total = 5,cost1 = 10,cost2 = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 5,cost1 = 10,cost2 = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(total = 5,cost1 = 10,cost2 = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 5,cost1 = 10,cost2 = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(total = 100,cost1 = 1,cost2 = 1) == 5151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 100,cost1 = 1,cost2 = 1) == 5151: {e}')
    
    total += 1
    try:
        result = candidate(total = 50,cost1 = 7,cost2 = 11) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 50,cost1 = 7,cost2 = 11) == 23: {e}')
    
    total += 1
    try:
        result = candidate(total = 100,cost1 = 20,cost2 = 30) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 100,cost1 = 20,cost2 = 30) == 14: {e}')
    
    total += 1
    try:
        result = candidate(total = 50,cost1 = 10,cost2 = 20) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 50,cost1 = 10,cost2 = 20) == 12: {e}')
    
    total += 1
    try:
        result = candidate(total = 1000000,cost1 = 500000,cost2 = 500000) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1000000,cost1 = 500000,cost2 = 500000) == 6: {e}')
    
    total += 1
    try:
        result = candidate(total = 20,cost1 = 10,cost2 = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 20,cost1 = 10,cost2 = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(total = 1000000,cost1 = 500000,cost2 = 500000) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1000000,cost1 = 500000,cost2 = 500000) == 6: {e}')
    
    total += 1
    try:
        result = candidate(total = 1000000,cost1 = 500000,cost2 = 300000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1000000,cost1 = 500000,cost2 = 300000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(total = 10,cost1 = 3,cost2 = 7) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 10,cost1 = 3,cost2 = 7) == 6: {e}')
    
    total += 1
    try:
        result = candidate(total = 10,cost1 = 5,cost2 = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 10,cost1 = 5,cost2 = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(total = 1,cost1 = 1,cost2 = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1,cost1 = 1,cost2 = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(total = 50,cost1 = 25,cost2 = 20) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 50,cost1 = 25,cost2 = 20) == 6: {e}')
    
    total += 1
    try:
        result = candidate(total = 100,cost1 = 1,cost2 = 1) == 5151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 100,cost1 = 1,cost2 = 1) == 5151: {e}')
    
    total += 1
    try:
        result = candidate(total = 500,cost1 = 250,cost2 = 250) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 500,cost1 = 250,cost2 = 250) == 6: {e}')
    
    total += 1
    try:
        result = candidate(total = 1,cost1 = 2,cost2 = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1,cost1 = 2,cost2 = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(total = 500,cost1 = 5,cost2 = 7) == 3665
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 500,cost1 = 5,cost2 = 7) == 3665: {e}')
    
    total += 1
    try:
        result = candidate(total = 150,cost1 = 25,cost2 = 15) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 150,cost1 = 25,cost2 = 15) == 40: {e}')
    
    total += 1
    try:
        result = candidate(total = 100,cost1 = 100,cost2 = 100) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 100,cost1 = 100,cost2 = 100) == 3: {e}')
    
    total += 1
    try:
        result = candidate(total = 1234,cost1 = 123,cost2 = 456) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1234,cost1 = 123,cost2 = 456) == 21: {e}')
    
    total += 1
    try:
        result = candidate(total = 800,cost1 = 120,cost2 = 30) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 800,cost1 = 120,cost2 = 30) == 105: {e}')
    
    total += 1
    try:
        result = candidate(total = 100,cost1 = 50,cost2 = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 100,cost1 = 50,cost2 = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(total = 100,cost1 = 50,cost2 = 50) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 100,cost1 = 50,cost2 = 50) == 6: {e}')
    
    total += 1
    try:
        result = candidate(total = 1000,cost1 = 100,cost2 = 200) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1000,cost1 = 100,cost2 = 200) == 36: {e}')
    
    total += 1
    try:
        result = candidate(total = 100000,cost1 = 1000,cost2 = 500) == 10201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 100000,cost1 = 1000,cost2 = 500) == 10201: {e}')
    
    total += 1
    try:
        result = candidate(total = 999999,cost1 = 99999,cost2 = 1) == 5500055
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 999999,cost1 = 99999,cost2 = 1) == 5500055: {e}')
    
    total += 1
    try:
        result = candidate(total = 80,cost1 = 8,cost2 = 5) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 80,cost1 = 8,cost2 = 5) == 95: {e}')
    
    total += 1
    try:
        result = candidate(total = 200,cost1 = 15,cost2 = 4) == 368
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 200,cost1 = 15,cost2 = 4) == 368: {e}')
    
    total += 1
    try:
        result = candidate(total = 1000,cost1 = 150,cost2 = 100) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1000,cost1 = 150,cost2 = 100) == 44: {e}')
    
    total += 1
    try:
        result = candidate(total = 100,cost1 = 7,cost2 = 3) == 265
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 100,cost1 = 7,cost2 = 3) == 265: {e}')
    
    total += 1
    try:
        result = candidate(total = 1000,cost1 = 150,cost2 = 75) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1000,cost1 = 150,cost2 = 75) == 56: {e}')
    
    total += 1
    try:
        result = candidate(total = 1000000,cost1 = 999999,cost2 = 999999) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1000000,cost1 = 999999,cost2 = 999999) == 3: {e}')
    
    total += 1
    try:
        result = candidate(total = 123456,cost1 = 11111,cost2 = 22222) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 123456,cost1 = 11111,cost2 = 22222) == 42: {e}')
    
    total += 1
    try:
        result = candidate(total = 100000,cost1 = 33333,cost2 = 33333) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 100000,cost1 = 33333,cost2 = 33333) == 10: {e}')
    
    total += 1
    try:
        result = candidate(total = 999999,cost1 = 1000,cost2 = 999) == 501501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 999999,cost1 = 1000,cost2 = 999) == 501501: {e}')
    
    total += 1
    try:
        result = candidate(total = 10000,cost1 = 100,cost2 = 50) == 10201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 10000,cost1 = 100,cost2 = 50) == 10201: {e}')
    
    total += 1
    try:
        result = candidate(total = 200,cost1 = 50,cost2 = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 200,cost1 = 50,cost2 = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(total = 500000,cost1 = 999999,cost2 = 1) == 500001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 500000,cost1 = 999999,cost2 = 1) == 500001: {e}')
    
    total += 1
    try:
        result = candidate(total = 150,cost1 = 5,cost2 = 3) == 796
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 150,cost1 = 5,cost2 = 3) == 796: {e}')
    
    total += 1
    try:
        result = candidate(total = 999999,cost1 = 100000,cost2 = 50000) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 999999,cost1 = 100000,cost2 = 50000) == 110: {e}')
    
    total += 1
    try:
        result = candidate(total = 123456,cost1 = 12345,cost2 = 6543) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 123456,cost1 = 12345,cost2 = 6543) == 109: {e}')
    
    total += 1
    try:
        result = candidate(total = 10000,cost1 = 50,cost2 = 30) == 33634
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 10000,cost1 = 50,cost2 = 30) == 33634: {e}')
    
    total += 1
    try:
        result = candidate(total = 500,cost1 = 250,cost2 = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 500,cost1 = 250,cost2 = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(total = 100000,cost1 = 1,cost2 = 1) == 5000150001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 100000,cost1 = 1,cost2 = 1) == 5000150001: {e}')
    
    total += 1
    try:
        result = candidate(total = 250,cost1 = 75,cost2 = 25) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 250,cost1 = 75,cost2 = 25) == 26: {e}')
    
    total += 1
    try:
        result = candidate(total = 500,cost1 = 150,cost2 = 125) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 500,cost1 = 150,cost2 = 125) == 11: {e}')
    
    total += 1
    try:
        result = candidate(total = 1000,cost1 = 10,cost2 = 1) == 50601
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1000,cost1 = 10,cost2 = 1) == 50601: {e}')
    
    total += 1
    try:
        result = candidate(total = 999,cost1 = 1,cost2 = 1) == 500500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 999,cost1 = 1,cost2 = 1) == 500500: {e}')
    
    total += 1
    try:
        result = candidate(total = 1000,cost1 = 500,cost2 = 250) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1000,cost1 = 500,cost2 = 250) == 9: {e}')
    
    total += 1
    try:
        result = candidate(total = 200,cost1 = 10,cost2 = 100) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 200,cost1 = 10,cost2 = 100) == 33: {e}')
    
    total += 1
    try:
        result = candidate(total = 120,cost1 = 30,cost2 = 20) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 120,cost1 = 30,cost2 = 20) == 19: {e}')
    
    total += 1
    try:
        result = candidate(total = 60,cost1 = 20,cost2 = 30) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 60,cost1 = 20,cost2 = 30) == 7: {e}')
    
    total += 1
    try:
        result = candidate(total = 999999,cost1 = 1,cost2 = 2) == 250000500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 999999,cost1 = 1,cost2 = 2) == 250000500000: {e}')
    
    total += 1
    try:
        result = candidate(total = 300,cost1 = 150,cost2 = 100) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 300,cost1 = 150,cost2 = 100) == 7: {e}')
    
    total += 1
    try:
        result = candidate(total = 150,cost1 = 50,cost2 = 50) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 150,cost1 = 50,cost2 = 50) == 10: {e}')
    
    total += 1
    try:
        result = candidate(total = 1000,cost1 = 333,cost2 = 111) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1000,cost1 = 333,cost2 = 111) == 22: {e}')
    
    total += 1
    try:
        result = candidate(total = 100,cost1 = 25,cost2 = 30) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 100,cost1 = 25,cost2 = 30) == 11: {e}')
    
    total += 1
    try:
        result = candidate(total = 500,cost1 = 150,cost2 = 50) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 500,cost1 = 150,cost2 = 50) == 26: {e}')
    
    total += 1
    try:
        result = candidate(total = 999999,cost1 = 99999,cost2 = 99999) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 999999,cost1 = 99999,cost2 = 99999) == 66: {e}')
    
    total += 1
    try:
        result = candidate(total = 800,cost1 = 400,cost2 = 200) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 800,cost1 = 400,cost2 = 200) == 9: {e}')
    
    total += 1
    try:
        result = candidate(total = 120,cost1 = 40,cost2 = 60) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 120,cost1 = 40,cost2 = 60) == 7: {e}')
    
    total += 1
    try:
        result = candidate(total = 600,cost1 = 100,cost2 = 150) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 600,cost1 = 100,cost2 = 150) == 19: {e}')
    
    total += 1
    try:
        result = candidate(total = 500,cost1 = 250,cost2 = 200) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 500,cost1 = 250,cost2 = 200) == 6: {e}')
    
    total += 1
    try:
        result = candidate(total = 500000,cost1 = 1,cost2 = 2) == 62500500001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 500000,cost1 = 1,cost2 = 2) == 62500500001: {e}')
    
    total += 1
    try:
        result = candidate(total = 999999,cost1 = 1,cost2 = 1) == 500000500000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 999999,cost1 = 1,cost2 = 1) == 500000500000: {e}')
    
    total += 1
    try:
        result = candidate(total = 1500000,cost1 = 300000,cost2 = 400000) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1500000,cost1 = 300000,cost2 = 400000) == 15: {e}')
    
    total += 1
    try:
        result = candidate(total = 75,cost1 = 15,cost2 = 10) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 75,cost1 = 15,cost2 = 10) == 27: {e}')
    
    total += 1
    try:
        result = candidate(total = 200,cost1 = 1,cost2 = 1) == 20301
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 200,cost1 = 1,cost2 = 1) == 20301: {e}')
    
    total += 1
    try:
        result = candidate(total = 1000,cost1 = 500,cost2 = 100) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1000,cost1 = 500,cost2 = 100) == 18: {e}')
    
    total += 1
    try:
        result = candidate(total = 100,cost1 = 1,cost2 = 2) == 2601
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 100,cost1 = 1,cost2 = 2) == 2601: {e}')
    
    total += 1
    try:
        result = candidate(total = 70,cost1 = 5,cost2 = 3) == 185
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 70,cost1 = 5,cost2 = 3) == 185: {e}')
    
    total += 1
    try:
        result = candidate(total = 300,cost1 = 100,cost2 = 150) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 300,cost1 = 100,cost2 = 150) == 7: {e}')
    
    total += 1
    try:
        result = candidate(total = 1000,cost1 = 300,cost2 = 500) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1000,cost1 = 300,cost2 = 500) == 7: {e}')
    
    total += 1
    try:
        result = candidate(total = 999999,cost1 = 999999,cost2 = 1) == 1000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 999999,cost1 = 999999,cost2 = 1) == 1000001: {e}')
    
    total += 1
    try:
        result = candidate(total = 1000000,cost1 = 1,cost2 = 1) == 500001500001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1000000,cost1 = 1,cost2 = 1) == 500001500001: {e}')
    
    total += 1
    try:
        result = candidate(total = 1000000,cost1 = 1,cost2 = 1000000) == 1000002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1000000,cost1 = 1,cost2 = 1000000) == 1000002: {e}')
    
    total += 1
    try:
        result = candidate(total = 1000,cost1 = 5,cost2 = 3) == 33634
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1000,cost1 = 5,cost2 = 3) == 33634: {e}')
    
    total += 1
    try:
        result = candidate(total = 5000,cost1 = 50,cost2 = 100) == 2601
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 5000,cost1 = 50,cost2 = 100) == 2601: {e}')
    
    total += 1
    try:
        result = candidate(total = 100000,cost1 = 20000,cost2 = 30000) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 100000,cost1 = 20000,cost2 = 30000) == 14: {e}')
    
    total += 1
    try:
        result = candidate(total = 1000,cost1 = 100,cost2 = 10) == 561
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1000,cost1 = 100,cost2 = 10) == 561: {e}')
    
    total += 1
    try:
        result = candidate(total = 100,cost1 = 30,cost2 = 70) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 100,cost1 = 30,cost2 = 70) == 6: {e}')
    
    total += 1
    try:
        result = candidate(total = 100,cost1 = 30,cost2 = 7) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 100,cost1 = 30,cost2 = 7) == 34: {e}')
    
    total += 1
    try:
        result = candidate(total = 123456,cost1 = 123,cost2 = 456) == 136511
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 123456,cost1 = 123,cost2 = 456) == 136511: {e}')
    
    total += 1
    try:
        result = candidate(total = 300,cost1 = 50,cost2 = 25) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 300,cost1 = 50,cost2 = 25) == 49: {e}')
    
    total += 1
    try:
        result = candidate(total = 100,cost1 = 5,cost2 = 3) == 364
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 100,cost1 = 5,cost2 = 3) == 364: {e}')
    
    total += 1
    try:
        result = candidate(total = 10000,cost1 = 100,cost2 = 10) == 50601
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 10000,cost1 = 100,cost2 = 10) == 50601: {e}')
    
    total += 1
    try:
        result = candidate(total = 200,cost1 = 150,cost2 = 50) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 200,cost1 = 150,cost2 = 50) == 7: {e}')
    
    total += 1
    try:
        result = candidate(total = 500,cost1 = 100,cost2 = 50) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 500,cost1 = 100,cost2 = 50) == 36: {e}')
    
    total += 1
    try:
        result = candidate(total = 999999,cost1 = 100000,cost2 = 10000) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 999999,cost1 = 100000,cost2 = 10000) == 550: {e}')
    
    total += 1
    try:
        result = candidate(total = 500,cost1 = 100,cost2 = 10) == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 500,cost1 = 100,cost2 = 10) == 156: {e}')
    
    total += 1
    try:
        result = candidate(total = 300,cost1 = 50,cost2 = 75) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 300,cost1 = 50,cost2 = 75) == 19: {e}')
    
    total += 1
    try:
        result = candidate(total = 100,cost1 = 99,cost2 = 1) == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 100,cost1 = 99,cost2 = 1) == 103: {e}')
    
    total += 1
    try:
        result = candidate(total = 100,cost1 = 25,cost2 = 7) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 100,cost1 = 25,cost2 = 7) == 39: {e}')
    
    total += 1
    try:
        result = candidate(total = 200,cost1 = 7,cost2 = 11) == 285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 200,cost1 = 7,cost2 = 11) == 285: {e}')
    
    total += 1
    try:
        result = candidate(total = 300,cost1 = 150,cost2 = 50) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 300,cost1 = 150,cost2 = 50) == 12: {e}')
    
    total += 1
    try:
        result = candidate(total = 100,cost1 = 50,cost2 = 25) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 100,cost1 = 50,cost2 = 25) == 9: {e}')
    
    total += 1
    try:
        result = candidate(total = 120,cost1 = 20,cost2 = 15) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 120,cost1 = 20,cost2 = 15) == 33: {e}')
    
    total += 1
    try:
        result = candidate(total = 500,cost1 = 200,cost2 = 150) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 500,cost1 = 200,cost2 = 150) == 8: {e}')
    
    total += 1
    try:
        result = candidate(total = 1,cost1 = 1,cost2 = 2) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(total = 1,cost1 = 1,cost2 = 2) == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(total = 20,cost1 = 10,cost2 = 5) == 9
    assert candidate(total = 1000,cost1 = 1,cost2 = 1) == 501501
    assert candidate(total = 5,cost1 = 10,cost2 = 10) == 1
    assert candidate(total = 5,cost1 = 10,cost2 = 10) == 1
    assert candidate(total = 100,cost1 = 1,cost2 = 1) == 5151
    assert candidate(total = 50,cost1 = 7,cost2 = 11) == 23
    assert candidate(total = 100,cost1 = 20,cost2 = 30) == 14
    assert candidate(total = 50,cost1 = 10,cost2 = 20) == 12
    assert candidate(total = 1000000,cost1 = 500000,cost2 = 500000) == 6
    assert candidate(total = 20,cost1 = 10,cost2 = 5) == 9
    assert candidate(total = 1000000,cost1 = 500000,cost2 = 500000) == 6
    assert candidate(total = 1000000,cost1 = 500000,cost2 = 300000) == 7
    assert candidate(total = 10,cost1 = 3,cost2 = 7) == 6
    assert candidate(total = 10,cost1 = 5,cost2 = 2) == 10
    assert candidate(total = 1,cost1 = 1,cost2 = 1) == 3
    assert candidate(total = 50,cost1 = 25,cost2 = 20) == 6
    assert candidate(total = 100,cost1 = 1,cost2 = 1) == 5151
    assert candidate(total = 500,cost1 = 250,cost2 = 250) == 6
    assert candidate(total = 1,cost1 = 2,cost2 = 3) == 1
    assert candidate(total = 500,cost1 = 5,cost2 = 7) == 3665
    assert candidate(total = 150,cost1 = 25,cost2 = 15) == 40
    assert candidate(total = 100,cost1 = 100,cost2 = 100) == 3
    assert candidate(total = 1234,cost1 = 123,cost2 = 456) == 21
    assert candidate(total = 800,cost1 = 120,cost2 = 30) == 105
    assert candidate(total = 100,cost1 = 50,cost2 = 100) == 4
    assert candidate(total = 100,cost1 = 50,cost2 = 50) == 6
    assert candidate(total = 1000,cost1 = 100,cost2 = 200) == 36
    assert candidate(total = 100000,cost1 = 1000,cost2 = 500) == 10201
    assert candidate(total = 999999,cost1 = 99999,cost2 = 1) == 5500055
    assert candidate(total = 80,cost1 = 8,cost2 = 5) == 95
    assert candidate(total = 200,cost1 = 15,cost2 = 4) == 368
    assert candidate(total = 1000,cost1 = 150,cost2 = 100) == 44
    assert candidate(total = 100,cost1 = 7,cost2 = 3) == 265
    assert candidate(total = 1000,cost1 = 150,cost2 = 75) == 56
    assert candidate(total = 1000000,cost1 = 999999,cost2 = 999999) == 3
    assert candidate(total = 123456,cost1 = 11111,cost2 = 22222) == 42
    assert candidate(total = 100000,cost1 = 33333,cost2 = 33333) == 10
    assert candidate(total = 999999,cost1 = 1000,cost2 = 999) == 501501
    assert candidate(total = 10000,cost1 = 100,cost2 = 50) == 10201
    assert candidate(total = 200,cost1 = 50,cost2 = 25) == 25
    assert candidate(total = 500000,cost1 = 999999,cost2 = 1) == 500001
    assert candidate(total = 150,cost1 = 5,cost2 = 3) == 796
    assert candidate(total = 999999,cost1 = 100000,cost2 = 50000) == 110
    assert candidate(total = 123456,cost1 = 12345,cost2 = 6543) == 109
    assert candidate(total = 10000,cost1 = 50,cost2 = 30) == 33634
    assert candidate(total = 500,cost1 = 250,cost2 = 100) == 10
    assert candidate(total = 100000,cost1 = 1,cost2 = 1) == 5000150001
    assert candidate(total = 250,cost1 = 75,cost2 = 25) == 26
    assert candidate(total = 500,cost1 = 150,cost2 = 125) == 11
    assert candidate(total = 1000,cost1 = 10,cost2 = 1) == 50601
    assert candidate(total = 999,cost1 = 1,cost2 = 1) == 500500
    assert candidate(total = 1000,cost1 = 500,cost2 = 250) == 9
    assert candidate(total = 200,cost1 = 10,cost2 = 100) == 33
    assert candidate(total = 120,cost1 = 30,cost2 = 20) == 19
    assert candidate(total = 60,cost1 = 20,cost2 = 30) == 7
    assert candidate(total = 999999,cost1 = 1,cost2 = 2) == 250000500000
    assert candidate(total = 300,cost1 = 150,cost2 = 100) == 7
    assert candidate(total = 150,cost1 = 50,cost2 = 50) == 10
    assert candidate(total = 1000,cost1 = 333,cost2 = 111) == 22
    assert candidate(total = 100,cost1 = 25,cost2 = 30) == 11
    assert candidate(total = 500,cost1 = 150,cost2 = 50) == 26
    assert candidate(total = 999999,cost1 = 99999,cost2 = 99999) == 66
    assert candidate(total = 800,cost1 = 400,cost2 = 200) == 9
    assert candidate(total = 120,cost1 = 40,cost2 = 60) == 7
    assert candidate(total = 600,cost1 = 100,cost2 = 150) == 19
    assert candidate(total = 500,cost1 = 250,cost2 = 200) == 6
    assert candidate(total = 500000,cost1 = 1,cost2 = 2) == 62500500001
    assert candidate(total = 999999,cost1 = 1,cost2 = 1) == 500000500000
    assert candidate(total = 1500000,cost1 = 300000,cost2 = 400000) == 15
    assert candidate(total = 75,cost1 = 15,cost2 = 10) == 27
    assert candidate(total = 200,cost1 = 1,cost2 = 1) == 20301
    assert candidate(total = 1000,cost1 = 500,cost2 = 100) == 18
    assert candidate(total = 100,cost1 = 1,cost2 = 2) == 2601
    assert candidate(total = 70,cost1 = 5,cost2 = 3) == 185
    assert candidate(total = 300,cost1 = 100,cost2 = 150) == 7
    assert candidate(total = 1000,cost1 = 300,cost2 = 500) == 7
    assert candidate(total = 999999,cost1 = 999999,cost2 = 1) == 1000001
    assert candidate(total = 1000000,cost1 = 1,cost2 = 1) == 500001500001
    assert candidate(total = 1000000,cost1 = 1,cost2 = 1000000) == 1000002
    assert candidate(total = 1000,cost1 = 5,cost2 = 3) == 33634
    assert candidate(total = 5000,cost1 = 50,cost2 = 100) == 2601
    assert candidate(total = 100000,cost1 = 20000,cost2 = 30000) == 14
    assert candidate(total = 1000,cost1 = 100,cost2 = 10) == 561
    assert candidate(total = 100,cost1 = 30,cost2 = 70) == 6
    assert candidate(total = 100,cost1 = 30,cost2 = 7) == 34
    assert candidate(total = 123456,cost1 = 123,cost2 = 456) == 136511
    assert candidate(total = 300,cost1 = 50,cost2 = 25) == 49
    assert candidate(total = 100,cost1 = 5,cost2 = 3) == 364
    assert candidate(total = 10000,cost1 = 100,cost2 = 10) == 50601
    assert candidate(total = 200,cost1 = 150,cost2 = 50) == 7
    assert candidate(total = 500,cost1 = 100,cost2 = 50) == 36
    assert candidate(total = 999999,cost1 = 100000,cost2 = 10000) == 550
    assert candidate(total = 500,cost1 = 100,cost2 = 10) == 156
    assert candidate(total = 300,cost1 = 50,cost2 = 75) == 19
    assert candidate(total = 100,cost1 = 99,cost2 = 1) == 103
    assert candidate(total = 100,cost1 = 25,cost2 = 7) == 39
    assert candidate(total = 200,cost1 = 7,cost2 = 11) == 285
    assert candidate(total = 300,cost1 = 150,cost2 = 50) == 12
    assert candidate(total = 100,cost1 = 50,cost2 = 25) == 9
    assert candidate(total = 120,cost1 = 20,cost2 = 15) == 33
    assert candidate(total = 500,cost1 = 200,cost2 = 150) == 8
    assert candidate(total = 1,cost1 = 1,cost2 = 2) == 2


