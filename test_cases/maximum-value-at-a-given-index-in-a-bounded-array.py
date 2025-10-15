def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 1,index = 0,maxSum = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,index = 0,maxSum = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,index = 5,maxSum = 50) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,index = 5,maxSum = 50) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,index = 1,maxSum = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,index = 1,maxSum = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,index = 500000000,maxSum = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,index = 500000000,maxSum = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,index = 2,maxSum = 6) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,index = 2,maxSum = 6) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,index = 10,maxSum = 210) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,index = 10,maxSum = 210) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,index = 999999999,maxSum = 2000000000) == 44721
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,index = 999999999,maxSum = 2000000000) == 44721: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,index = 3,maxSum = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,index = 3,maxSum = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,index = 1,maxSum = 1200000000) == 19999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,index = 1,maxSum = 1200000000) == 19999: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,index = 0,maxSum = 10000000) == 4450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,index = 0,maxSum = 10000000) == 4450: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,index = 4,maxSum = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,index = 4,maxSum = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,index = 500,maxSum = 500000) == 750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,index = 500,maxSum = 500000) == 750: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,index = 999999999,maxSum = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,index = 999999999,maxSum = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,index = 10,maxSum = 200) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,index = 10,maxSum = 200) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,index = 999999998,maxSum = 2000000000) == 44721
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,index = 999999998,maxSum = 2000000000) == 44721: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,index = 50,maxSum = 5000) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,index = 50,maxSum = 5000) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,index = 500000000,maxSum = 2500000000) == 38730
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,index = 500000000,maxSum = 2500000000) == 38730: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,index = 1,maxSum = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,index = 1,maxSum = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,index = 500,maxSum = 100000) == 315
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,index = 500,maxSum = 100000) == 315: {e}')
    
    total += 1
    try:
        result = candidate(n = 750000000,index = 375000000,maxSum = 1500000000) == 27387
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750000000,index = 375000000,maxSum = 1500000000) == 27387: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,index = 99999,maxSum = 10000000) == 4450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,index = 99999,maxSum = 10000000) == 4450: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,index = 500000,maxSum = 10000000) == 3001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,index = 500000,maxSum = 10000000) == 3001: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,index = 499999999,maxSum = 1500000000) == 44721
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,index = 499999999,maxSum = 1500000000) == 44721: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,index = 0,maxSum = 999999999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,index = 0,maxSum = 999999999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,index = 499999999,maxSum = 10000000000) == 94869
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,index = 499999999,maxSum = 10000000000) == 94869: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,index = 0,maxSum = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,index = 0,maxSum = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,index = 24,maxSum = 1225) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,index = 24,maxSum = 1225) == 37: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,index = 50,maxSum = 5050) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,index = 50,maxSum = 5050) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,index = 4,maxSum = 45) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,index = 4,maxSum = 45) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 35,index = 17,maxSum = 3000) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35,index = 17,maxSum = 3000) == 94: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,index = 4999,maxSum = 1000000) == 995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,index = 4999,maxSum = 1000000) == 995: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,index = 4,maxSum = 100) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,index = 4,maxSum = 100) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,index = 0,maxSum = 50) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,index = 0,maxSum = 50) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,index = 1,maxSum = 2500000000) == 54771
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,index = 1,maxSum = 2500000000) == 54771: {e}')
    
    total += 1
    try:
        result = candidate(n = 750000000,index = 375000000,maxSum = 1800000000) == 32404
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 750000000,index = 375000000,maxSum = 1800000000) == 32404: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,index = 25,maxSum = 500) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,index = 25,maxSum = 500) == 22: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,index = 250,maxSum = 150000) == 425
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,index = 250,maxSum = 150000) == 425: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000000000,index = 1000000000,maxSum = 3000000000) == 31623
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000000000,index = 1000000000,maxSum = 3000000000) == 31623: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,index = 50,maxSum = 10000) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,index = 50,maxSum = 10000) == 125: {e}')
    
    total += 1
    try:
        result = candidate(n = 300000000,index = 150000000,maxSum = 1500000000) == 34642
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 300000000,index = 150000000,maxSum = 1500000000) == 34642: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,index = 2,maxSum = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,index = 2,maxSum = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,index = 0,maxSum = 2000000000) == 44721
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,index = 0,maxSum = 2000000000) == 44721: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,index = 24,maxSum = 1275) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,index = 24,maxSum = 1275) == 38: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,index = 100,maxSum = 2000) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,index = 100,maxSum = 2000) == 43: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,index = 0,maxSum = 1000000000) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,index = 0,maxSum = 1000000000) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,index = 500000000,maxSum = 10000000000) == 94869
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,index = 500000000,maxSum = 10000000000) == 94869: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,index = 3,maxSum = 30) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,index = 3,maxSum = 30) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,index = 6,maxSum = 75) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,index = 6,maxSum = 75) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,index = 0,maxSum = 36) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,index = 0,maxSum = 36) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,index = 24,maxSum = 5000) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,index = 24,maxSum = 5000) == 112: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,index = 19,maxSum = 50) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,index = 19,maxSum = 50) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,index = 250000000,maxSum = 1000000000) == 22361
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,index = 250000000,maxSum = 1000000000) == 22361: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,index = 1,maxSum = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,index = 1,maxSum = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,index = 1,maxSum = 2000000000) == 44720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,index = 1,maxSum = 2000000000) == 44720: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,index = 7,maxSum = 120) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,index = 7,maxSum = 120) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,index = 1,maxSum = 1500000000) == 44720
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,index = 1,maxSum = 1500000000) == 44720: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,index = 250000000,maxSum = 1500000000) == 31623
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,index = 250000000,maxSum = 1500000000) == 31623: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,index = 0,maxSum = 100) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,index = 0,maxSum = 100) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,index = 7,maxSum = 500) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,index = 7,maxSum = 500) == 37: {e}')
    
    total += 1
    try:
        result = candidate(n = 50,index = 25,maxSum = 1000) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 50,index = 25,maxSum = 1000) == 32: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,index = 1,maxSum = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,index = 1,maxSum = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,index = 12,maxSum = 1500) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,index = 12,maxSum = 1500) == 66: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,index = 3,maxSum = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,index = 3,maxSum = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,index = 9,maxSum = 100) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,index = 9,maxSum = 100) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,index = 1,maxSum = 1000000000) == 333333334
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,index = 1,maxSum = 1000000000) == 333333334: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,index = 250,maxSum = 2000) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,index = 250,maxSum = 2000) == 39: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,index = 19,maxSum = 200) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,index = 19,maxSum = 200) == 19: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000,index = 250000,maxSum = 100000000) == 9975
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000,index = 250000,maxSum = 100000000) == 9975: {e}')
    
    total += 1
    try:
        result = candidate(n = 800000000,index = 400000000,maxSum = 1600000000) == 28285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 800000000,index = 400000000,maxSum = 1600000000) == 28285: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,index = 7,maxSum = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,index = 7,maxSum = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,index = 100,maxSum = 20100) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,index = 100,maxSum = 20100) == 150: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,index = 499999999,maxSum = 999999999) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,index = 499999999,maxSum = 999999999) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 200000000,index = 100000000,maxSum = 500000000) == 17321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200000000,index = 100000000,maxSum = 500000000) == 17321: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000,index = 999999,maxSum = 2000000) == 1414
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000,index = 999999,maxSum = 2000000) == 1414: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,index = 1,maxSum = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,index = 1,maxSum = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,index = 0,maxSum = 1200000000) == 37417
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,index = 0,maxSum = 1200000000) == 37417: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,index = 0,maxSum = 1500000000) == 31623
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,index = 0,maxSum = 1500000000) == 31623: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,index = 4,maxSum = 55) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,index = 4,maxSum = 55) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,index = 50,maxSum = 1000) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,index = 50,maxSum = 1000) == 31: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,index = 9,maxSum = 25) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,index = 9,maxSum = 25) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,index = 9,maxSum = 36) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,index = 9,maxSum = 36) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000,index = 50000,maxSum = 5000000) == 2214
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000,index = 50000,maxSum = 5000000) == 2214: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,index = 0,maxSum = 50) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,index = 0,maxSum = 50) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,index = 1,maxSum = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,index = 1,maxSum = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,index = 0,maxSum = 25) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,index = 0,maxSum = 25) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 150,index = 75,maxSum = 100000) == 704
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 150,index = 75,maxSum = 100000) == 704: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,index = 1,maxSum = 1000000000) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,index = 1,maxSum = 1000000000) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,index = 2,maxSum = 17) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,index = 2,maxSum = 17) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,index = 500000000,maxSum = 1000000001) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,index = 500000000,maxSum = 1000000001) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000,index = 250000000,maxSum = 800000000) == 17321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000,index = 250000000,maxSum = 800000000) == 17321: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,index = 2,maxSum = 20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,index = 2,maxSum = 20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,index = 3,maxSum = 50) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,index = 3,maxSum = 50) == 8: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 1,index = 0,maxSum = 1) == 1
    assert candidate(n = 10,index = 5,maxSum = 50) == 7
    assert candidate(n = 6,index = 1,maxSum = 10) == 3
    assert candidate(n = 1000000000,index = 500000000,maxSum = 1000000000) == 1
    assert candidate(n = 4,index = 2,maxSum = 6) == 2
    assert candidate(n = 20,index = 10,maxSum = 210) == 15
    assert candidate(n = 1000000000,index = 999999999,maxSum = 2000000000) == 44721
    assert candidate(n = 7,index = 3,maxSum = 20) == 4
    assert candidate(n = 1000000000,index = 1,maxSum = 1200000000) == 19999
    assert candidate(n = 100000,index = 0,maxSum = 10000000) == 4450
    assert candidate(n = 9,index = 4,maxSum = 25) == 5
    assert candidate(n = 1000,index = 500,maxSum = 500000) == 750
    assert candidate(n = 1000000000,index = 999999999,maxSum = 1000000000) == 1
    assert candidate(n = 20,index = 10,maxSum = 200) == 15
    assert candidate(n = 999999999,index = 999999998,maxSum = 2000000000) == 44721
    assert candidate(n = 100,index = 50,maxSum = 5000) == 75
    assert candidate(n = 1000000000,index = 500000000,maxSum = 2500000000) == 38730
    assert candidate(n = 4,index = 1,maxSum = 10) == 3
    assert candidate(n = 1000,index = 500,maxSum = 100000) == 315
    assert candidate(n = 750000000,index = 375000000,maxSum = 1500000000) == 27387
    assert candidate(n = 100000,index = 99999,maxSum = 10000000) == 4450
    assert candidate(n = 1000000,index = 500000,maxSum = 10000000) == 3001
    assert candidate(n = 500000000,index = 499999999,maxSum = 1500000000) == 44721
    assert candidate(n = 999999999,index = 0,maxSum = 999999999) == 1
    assert candidate(n = 999999999,index = 499999999,maxSum = 10000000000) == 94869
    assert candidate(n = 1000000000,index = 0,maxSum = 1000000000) == 1
    assert candidate(n = 50,index = 24,maxSum = 1225) == 37
    assert candidate(n = 100,index = 50,maxSum = 5050) == 75
    assert candidate(n = 9,index = 4,maxSum = 45) == 7
    assert candidate(n = 35,index = 17,maxSum = 3000) == 94
    assert candidate(n = 10000,index = 4999,maxSum = 1000000) == 995
    assert candidate(n = 9,index = 4,maxSum = 100) == 13
    assert candidate(n = 20,index = 0,maxSum = 50) == 8
    assert candidate(n = 1000000000,index = 1,maxSum = 2500000000) == 54771
    assert candidate(n = 750000000,index = 375000000,maxSum = 1800000000) == 32404
    assert candidate(n = 50,index = 25,maxSum = 500) == 22
    assert candidate(n = 500,index = 250,maxSum = 150000) == 425
    assert candidate(n = 2000000000,index = 1000000000,maxSum = 3000000000) == 31623
    assert candidate(n = 100,index = 50,maxSum = 10000) == 125
    assert candidate(n = 300000000,index = 150000000,maxSum = 1500000000) == 34642
    assert candidate(n = 5,index = 2,maxSum = 15) == 4
    assert candidate(n = 1000000000,index = 0,maxSum = 2000000000) == 44721
    assert candidate(n = 50,index = 24,maxSum = 1275) == 38
    assert candidate(n = 200,index = 100,maxSum = 2000) == 43
    assert candidate(n = 1,index = 0,maxSum = 1000000000) == 1000000000
    assert candidate(n = 1000000000,index = 500000000,maxSum = 10000000000) == 94869
    assert candidate(n = 8,index = 3,maxSum = 30) == 5
    assert candidate(n = 12,index = 6,maxSum = 75) == 9
    assert candidate(n = 10,index = 0,maxSum = 36) == 7
    assert candidate(n = 50,index = 24,maxSum = 5000) == 112
    assert candidate(n = 20,index = 19,maxSum = 50) == 8
    assert candidate(n = 500000000,index = 250000000,maxSum = 1000000000) == 22361
    assert candidate(n = 2,index = 1,maxSum = 3) == 2
    assert candidate(n = 1000000000,index = 1,maxSum = 2000000000) == 44720
    assert candidate(n = 15,index = 7,maxSum = 120) == 11
    assert candidate(n = 500000000,index = 1,maxSum = 1500000000) == 44720
    assert candidate(n = 500000000,index = 250000000,maxSum = 1500000000) == 31623
    assert candidate(n = 10,index = 0,maxSum = 100) == 14
    assert candidate(n = 15,index = 7,maxSum = 500) == 37
    assert candidate(n = 50,index = 25,maxSum = 1000) == 32
    assert candidate(n = 3,index = 1,maxSum = 15) == 5
    assert candidate(n = 25,index = 12,maxSum = 1500) == 66
    assert candidate(n = 7,index = 3,maxSum = 25) == 5
    assert candidate(n = 10,index = 9,maxSum = 100) == 14
    assert candidate(n = 3,index = 1,maxSum = 1000000000) == 333333334
    assert candidate(n = 500,index = 250,maxSum = 2000) == 39
    assert candidate(n = 20,index = 19,maxSum = 200) == 19
    assert candidate(n = 500000,index = 250000,maxSum = 100000000) == 9975
    assert candidate(n = 800000000,index = 400000000,maxSum = 1600000000) == 28285
    assert candidate(n = 15,index = 7,maxSum = 100) == 10
    assert candidate(n = 200,index = 100,maxSum = 20100) == 150
    assert candidate(n = 999999999,index = 499999999,maxSum = 999999999) == 1
    assert candidate(n = 200000000,index = 100000000,maxSum = 500000000) == 17321
    assert candidate(n = 1000000,index = 999999,maxSum = 2000000) == 1414
    assert candidate(n = 1000000000,index = 1,maxSum = 1000000000) == 1
    assert candidate(n = 500000000,index = 0,maxSum = 1200000000) == 37417
    assert candidate(n = 999999999,index = 0,maxSum = 1500000000) == 31623
    assert candidate(n = 10,index = 4,maxSum = 55) == 8
    assert candidate(n = 100,index = 50,maxSum = 1000) == 31
    assert candidate(n = 10,index = 9,maxSum = 25) == 6
    assert candidate(n = 10,index = 9,maxSum = 36) == 7
    assert candidate(n = 100000,index = 50000,maxSum = 5000000) == 2214
    assert candidate(n = 10,index = 0,maxSum = 50) == 9
    assert candidate(n = 2,index = 1,maxSum = 6) == 3
    assert candidate(n = 10,index = 0,maxSum = 25) == 6
    assert candidate(n = 150,index = 75,maxSum = 100000) == 704
    assert candidate(n = 2,index = 1,maxSum = 1000000000) == 500000000
    assert candidate(n = 5,index = 2,maxSum = 17) == 4
    assert candidate(n = 1000000000,index = 500000000,maxSum = 1000000001) == 2
    assert candidate(n = 500000000,index = 250000000,maxSum = 800000000) == 17321
    assert candidate(n = 5,index = 2,maxSum = 20) == 5
    assert candidate(n = 7,index = 3,maxSum = 50) == 8


