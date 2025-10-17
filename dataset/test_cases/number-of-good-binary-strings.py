def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(minLength = 3,maxLength = 7,oneGroup = 3,zeroGroup = 3) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 3,maxLength = 7,oneGroup = 3,zeroGroup = 3) == 6: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 4,maxLength = 4,oneGroup = 4,zeroGroup = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 4,maxLength = 4,oneGroup = 4,zeroGroup = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 5,maxLength = 10,oneGroup = 5,zeroGroup = 5) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 5,maxLength = 10,oneGroup = 5,zeroGroup = 5) == 6: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 3,maxLength = 7,oneGroup = 3,zeroGroup = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 3,maxLength = 7,oneGroup = 3,zeroGroup = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 2,maxLength = 3,oneGroup = 1,zeroGroup = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 2,maxLength = 3,oneGroup = 1,zeroGroup = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 3,maxLength = 10,oneGroup = 3,zeroGroup = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 3,maxLength = 10,oneGroup = 3,zeroGroup = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 5,maxLength = 5,oneGroup = 1,zeroGroup = 1) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 5,maxLength = 5,oneGroup = 1,zeroGroup = 1) == 32: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 5,maxLength = 10,oneGroup = 5,zeroGroup = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 5,maxLength = 10,oneGroup = 5,zeroGroup = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 1,maxLength = 5,oneGroup = 2,zeroGroup = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 1,maxLength = 5,oneGroup = 2,zeroGroup = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 3,maxLength = 7,oneGroup = 3,zeroGroup = 4) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 3,maxLength = 7,oneGroup = 3,zeroGroup = 4) == 5: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 3,maxLength = 6,oneGroup = 3,zeroGroup = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 3,maxLength = 6,oneGroup = 3,zeroGroup = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 20,maxLength = 30,oneGroup = 7,zeroGroup = 3) == 113
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 20,maxLength = 30,oneGroup = 7,zeroGroup = 3) == 113: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 20,maxLength = 80,oneGroup = 6,zeroGroup = 4) == 128780
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 20,maxLength = 80,oneGroup = 6,zeroGroup = 4) == 128780: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 8,maxLength = 12,oneGroup = 5,zeroGroup = 6) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 8,maxLength = 12,oneGroup = 5,zeroGroup = 6) == 4: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 1000,maxLength = 2000,oneGroup = 10,zeroGroup = 2) == 352490699
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 1000,maxLength = 2000,oneGroup = 10,zeroGroup = 2) == 352490699: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 50000,maxLength = 100000,oneGroup = 10,zeroGroup = 5) == 566857578
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 50000,maxLength = 100000,oneGroup = 10,zeroGroup = 5) == 566857578: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 500,maxLength = 1500,oneGroup = 7,zeroGroup = 11) == 894054205
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 500,maxLength = 1500,oneGroup = 7,zeroGroup = 11) == 894054205: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 6,maxLength = 10,oneGroup = 5,zeroGroup = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 6,maxLength = 10,oneGroup = 5,zeroGroup = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 10,maxLength = 100,oneGroup = 5,zeroGroup = 5) == 2097148
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 10,maxLength = 100,oneGroup = 5,zeroGroup = 5) == 2097148: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 10,maxLength = 15,oneGroup = 4,zeroGroup = 2) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 10,maxLength = 15,oneGroup = 4,zeroGroup = 2) == 42: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 5,maxLength = 10,oneGroup = 2,zeroGroup = 3) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 5,maxLength = 10,oneGroup = 2,zeroGroup = 3) == 23: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 30,maxLength = 90,oneGroup = 3,zeroGroup = 5) == 13571760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 30,maxLength = 90,oneGroup = 3,zeroGroup = 5) == 13571760: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 5000,maxLength = 6000,oneGroup = 1000,zeroGroup = 1200) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 5000,maxLength = 6000,oneGroup = 1000,zeroGroup = 1200) == 33: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 8,maxLength = 12,oneGroup = 2,zeroGroup = 2) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 8,maxLength = 12,oneGroup = 2,zeroGroup = 2) == 112: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 25,maxLength = 75,oneGroup = 8,zeroGroup = 12) == 256
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 25,maxLength = 75,oneGroup = 8,zeroGroup = 12) == 256: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 10,maxLength = 50,oneGroup = 5,zeroGroup = 1) == 2630338
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 10,maxLength = 50,oneGroup = 5,zeroGroup = 1) == 2630338: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 50,maxLength = 100,oneGroup = 25,zeroGroup = 20) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 50,maxLength = 100,oneGroup = 25,zeroGroup = 20) == 26: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 10,maxLength = 20,oneGroup = 5,zeroGroup = 6) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 10,maxLength = 20,oneGroup = 5,zeroGroup = 6) == 13: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 100,maxLength = 200,oneGroup = 25,zeroGroup = 30) == 233
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 100,maxLength = 200,oneGroup = 25,zeroGroup = 30) == 233: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 200,maxLength = 500,oneGroup = 50,zeroGroup = 25) == 28602
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 200,maxLength = 500,oneGroup = 50,zeroGroup = 25) == 28602: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 50000,maxLength = 100000,oneGroup = 25000,zeroGroup = 30000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 50000,maxLength = 100000,oneGroup = 25000,zeroGroup = 30000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 1000,maxLength = 1500,oneGroup = 100,zeroGroup = 200) == 2440
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 1000,maxLength = 1500,oneGroup = 100,zeroGroup = 200) == 2440: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 1,maxLength = 100000,oneGroup = 5,zeroGroup = 7) == 809265852
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 1,maxLength = 100000,oneGroup = 5,zeroGroup = 7) == 809265852: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 1,maxLength = 100000,oneGroup = 1,zeroGroup = 1) == 215447031
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 1,maxLength = 100000,oneGroup = 1,zeroGroup = 1) == 215447031: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 30000,maxLength = 40000,oneGroup = 15,zeroGroup = 10) == 620090248
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 30000,maxLength = 40000,oneGroup = 15,zeroGroup = 10) == 620090248: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 20,maxLength = 30,oneGroup = 5,zeroGroup = 6) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 20,maxLength = 30,oneGroup = 5,zeroGroup = 6) == 49: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 12,maxLength = 25,oneGroup = 7,zeroGroup = 9) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 12,maxLength = 25,oneGroup = 7,zeroGroup = 9) == 11: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 1000,maxLength = 5000,oneGroup = 100,zeroGroup = 200) == 316290658
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 1000,maxLength = 5000,oneGroup = 100,zeroGroup = 200) == 316290658: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 5,maxLength = 15,oneGroup = 2,zeroGroup = 4) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 5,maxLength = 15,oneGroup = 2,zeroGroup = 4) == 50: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 30,maxLength = 150,oneGroup = 6,zeroGroup = 4) == 422361979
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 30,maxLength = 150,oneGroup = 6,zeroGroup = 4) == 422361979: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 20,maxLength = 50,oneGroup = 10,zeroGroup = 8) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 20,maxLength = 50,oneGroup = 10,zeroGroup = 8) == 64: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 10,maxLength = 20,oneGroup = 5,zeroGroup = 5) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 10,maxLength = 20,oneGroup = 5,zeroGroup = 5) == 28: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 50,maxLength = 50,oneGroup = 5,zeroGroup = 10) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 50,maxLength = 50,oneGroup = 5,zeroGroup = 10) == 89: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 50,maxLength = 75,oneGroup = 10,zeroGroup = 15) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 50,maxLength = 75,oneGroup = 10,zeroGroup = 15) == 93: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 500,maxLength = 700,oneGroup = 50,zeroGroup = 75) == 4059
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 500,maxLength = 700,oneGroup = 50,zeroGroup = 75) == 4059: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 50000,maxLength = 100000,oneGroup = 25000,zeroGroup = 25000) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 50000,maxLength = 100000,oneGroup = 25000,zeroGroup = 25000) == 28: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 15,maxLength = 100,oneGroup = 8,zeroGroup = 5) == 80400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 15,maxLength = 100,oneGroup = 8,zeroGroup = 5) == 80400: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 10,maxLength = 20,oneGroup = 4,zeroGroup = 6) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 10,maxLength = 20,oneGroup = 4,zeroGroup = 6) == 23: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 10,maxLength = 20,oneGroup = 4,zeroGroup = 5) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 10,maxLength = 20,oneGroup = 4,zeroGroup = 5) == 26: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 2,maxLength = 2,oneGroup = 1,zeroGroup = 1) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 2,maxLength = 2,oneGroup = 1,zeroGroup = 1) == 4: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 30000,maxLength = 50000,oneGroup = 5,zeroGroup = 8) == 106251649
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 30000,maxLength = 50000,oneGroup = 5,zeroGroup = 8) == 106251649: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 100,maxLength = 200,oneGroup = 15,zeroGroup = 20) == 4602
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 100,maxLength = 200,oneGroup = 15,zeroGroup = 20) == 4602: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 50000,maxLength = 100000,oneGroup = 10,zeroGroup = 15) == 945515466
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 50000,maxLength = 100000,oneGroup = 10,zeroGroup = 15) == 945515466: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 7,maxLength = 40,oneGroup = 3,zeroGroup = 7) == 597
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 7,maxLength = 40,oneGroup = 3,zeroGroup = 7) == 597: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 10,maxLength = 20,oneGroup = 4,zeroGroup = 7) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 10,maxLength = 20,oneGroup = 4,zeroGroup = 7) == 16: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 15,maxLength = 25,oneGroup = 3,zeroGroup = 9) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 15,maxLength = 25,oneGroup = 3,zeroGroup = 9) == 32: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 8,maxLength = 30,oneGroup = 5,zeroGroup = 4) == 153
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 8,maxLength = 30,oneGroup = 5,zeroGroup = 4) == 153: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 6,maxLength = 25,oneGroup = 3,zeroGroup = 3) == 508
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 6,maxLength = 25,oneGroup = 3,zeroGroup = 3) == 508: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 20,maxLength = 50,oneGroup = 7,zeroGroup = 10) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 20,maxLength = 50,oneGroup = 7,zeroGroup = 10) == 80: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 100,maxLength = 1000,oneGroup = 10,zeroGroup = 20) == 252403212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 100,maxLength = 1000,oneGroup = 10,zeroGroup = 20) == 252403212: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 30000,maxLength = 40000,oneGroup = 5000,zeroGroup = 2500) == 3804
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 30000,maxLength = 40000,oneGroup = 5000,zeroGroup = 2500) == 3804: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 7,maxLength = 14,oneGroup = 3,zeroGroup = 7) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 7,maxLength = 14,oneGroup = 3,zeroGroup = 7) == 9: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 20,maxLength = 50,oneGroup = 7,zeroGroup = 11) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 20,maxLength = 50,oneGroup = 7,zeroGroup = 11) == 74: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 50000,maxLength = 100000,oneGroup = 25,zeroGroup = 20) == 165911007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 50000,maxLength = 100000,oneGroup = 25,zeroGroup = 20) == 165911007: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 120,maxLength = 250,oneGroup = 9,zeroGroup = 18) == 831053
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 120,maxLength = 250,oneGroup = 9,zeroGroup = 18) == 831053: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 15,maxLength = 30,oneGroup = 5,zeroGroup = 5) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 15,maxLength = 30,oneGroup = 5,zeroGroup = 5) == 120: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 60,maxLength = 70,oneGroup = 12,zeroGroup = 18) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 60,maxLength = 70,oneGroup = 12,zeroGroup = 18) == 16: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 1,maxLength = 1000,oneGroup = 1,zeroGroup = 1) == 376846411
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 1,maxLength = 1000,oneGroup = 1,zeroGroup = 1) == 376846411: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 7,maxLength = 14,oneGroup = 3,zeroGroup = 4) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 7,maxLength = 14,oneGroup = 3,zeroGroup = 4) == 22: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 10,maxLength = 20,oneGroup = 2,zeroGroup = 3) == 444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 10,maxLength = 20,oneGroup = 2,zeroGroup = 3) == 444: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 70000,maxLength = 80000,oneGroup = 10000,zeroGroup = 15000) == 86
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 70000,maxLength = 80000,oneGroup = 10000,zeroGroup = 15000) == 86: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 3000,maxLength = 3500,oneGroup = 500,zeroGroup = 600) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 3000,maxLength = 3500,oneGroup = 500,zeroGroup = 600) == 65: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 20,maxLength = 30,oneGroup = 6,zeroGroup = 7) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 20,maxLength = 30,oneGroup = 6,zeroGroup = 7) == 21: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 100,maxLength = 120,oneGroup = 20,zeroGroup = 25) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 100,maxLength = 120,oneGroup = 20,zeroGroup = 25) == 33: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 10000,maxLength = 100000,oneGroup = 100,zeroGroup = 50) == 816036866
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 10000,maxLength = 100000,oneGroup = 100,zeroGroup = 50) == 816036866: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 25,maxLength = 70,oneGroup = 11,zeroGroup = 10) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 25,maxLength = 70,oneGroup = 11,zeroGroup = 10) == 121: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 40,maxLength = 80,oneGroup = 8,zeroGroup = 16) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 40,maxLength = 80,oneGroup = 8,zeroGroup = 16) == 220: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 1,maxLength = 10,oneGroup = 3,zeroGroup = 4) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 1,maxLength = 10,oneGroup = 3,zeroGroup = 4) == 10: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 50,maxLength = 100,oneGroup = 10,zeroGroup = 15) == 444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 50,maxLength = 100,oneGroup = 10,zeroGroup = 15) == 444: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 5,maxLength = 100000,oneGroup = 1,zeroGroup = 1) == 215447001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 5,maxLength = 100000,oneGroup = 1,zeroGroup = 1) == 215447001: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 20,maxLength = 30,oneGroup = 7,zeroGroup = 14) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 20,maxLength = 30,oneGroup = 7,zeroGroup = 14) == 8: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 1,maxLength = 100,oneGroup = 1,zeroGroup = 1) == 952742561
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 1,maxLength = 100,oneGroup = 1,zeroGroup = 1) == 952742561: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 10,maxLength = 50,oneGroup = 5,zeroGroup = 2) == 70067
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 10,maxLength = 50,oneGroup = 5,zeroGroup = 2) == 70067: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 1,maxLength = 100000,oneGroup = 50000,zeroGroup = 50000) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 1,maxLength = 100000,oneGroup = 50000,zeroGroup = 50000) == 6: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 15,maxLength = 25,oneGroup = 5,zeroGroup = 5) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 15,maxLength = 25,oneGroup = 5,zeroGroup = 5) == 56: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 15,maxLength = 60,oneGroup = 5,zeroGroup = 6) == 3065
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 15,maxLength = 60,oneGroup = 5,zeroGroup = 6) == 3065: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 25,maxLength = 50,oneGroup = 10,zeroGroup = 20) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 25,maxLength = 50,oneGroup = 10,zeroGroup = 20) == 16: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 25000,maxLength = 75000,oneGroup = 12,zeroGroup = 20) == 285553317
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 25000,maxLength = 75000,oneGroup = 12,zeroGroup = 20) == 285553317: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 50,maxLength = 70,oneGroup = 10,zeroGroup = 15) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 50,maxLength = 70,oneGroup = 10,zeroGroup = 15) == 65: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 1000,maxLength = 10000,oneGroup = 500,zeroGroup = 750) == 128797
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 1000,maxLength = 10000,oneGroup = 500,zeroGroup = 750) == 128797: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 2000,maxLength = 2500,oneGroup = 300,zeroGroup = 400) == 166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 2000,maxLength = 2500,oneGroup = 300,zeroGroup = 400) == 166: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 25000,maxLength = 75000,oneGroup = 50,zeroGroup = 60) == 547461537
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 25000,maxLength = 75000,oneGroup = 50,zeroGroup = 60) == 547461537: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 5,maxLength = 15,oneGroup = 2,zeroGroup = 5) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 5,maxLength = 15,oneGroup = 2,zeroGroup = 5) == 37: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 10000,maxLength = 100000,oneGroup = 5,zeroGroup = 10) == 444309034
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 10000,maxLength = 100000,oneGroup = 5,zeroGroup = 10) == 444309034: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 5,maxLength = 15,oneGroup = 2,zeroGroup = 3) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 5,maxLength = 15,oneGroup = 2,zeroGroup = 3) == 109: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 5000,maxLength = 10000,oneGroup = 20,zeroGroup = 15) == 627599613
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 5000,maxLength = 10000,oneGroup = 20,zeroGroup = 15) == 627599613: {e}')
    
    total += 1
    try:
        result = candidate(minLength = 5,maxLength = 5,oneGroup = 5,zeroGroup = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(minLength = 5,maxLength = 5,oneGroup = 5,zeroGroup = 5) == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(minLength = 3,maxLength = 7,oneGroup = 3,zeroGroup = 3) == 6
    assert candidate(minLength = 4,maxLength = 4,oneGroup = 4,zeroGroup = 3) == 1
    assert candidate(minLength = 5,maxLength = 10,oneGroup = 5,zeroGroup = 5) == 6
    assert candidate(minLength = 3,maxLength = 7,oneGroup = 3,zeroGroup = 5) == 3
    assert candidate(minLength = 2,maxLength = 3,oneGroup = 1,zeroGroup = 2) == 5
    assert candidate(minLength = 3,maxLength = 10,oneGroup = 3,zeroGroup = 4) == 10
    assert candidate(minLength = 5,maxLength = 5,oneGroup = 1,zeroGroup = 1) == 32
    assert candidate(minLength = 5,maxLength = 10,oneGroup = 5,zeroGroup = 4) == 5
    assert candidate(minLength = 1,maxLength = 5,oneGroup = 2,zeroGroup = 2) == 6
    assert candidate(minLength = 3,maxLength = 7,oneGroup = 3,zeroGroup = 4) == 5
    assert candidate(minLength = 3,maxLength = 6,oneGroup = 3,zeroGroup = 2) == 6
    assert candidate(minLength = 20,maxLength = 30,oneGroup = 7,zeroGroup = 3) == 113
    assert candidate(minLength = 20,maxLength = 80,oneGroup = 6,zeroGroup = 4) == 128780
    assert candidate(minLength = 8,maxLength = 12,oneGroup = 5,zeroGroup = 6) == 4
    assert candidate(minLength = 1000,maxLength = 2000,oneGroup = 10,zeroGroup = 2) == 352490699
    assert candidate(minLength = 50000,maxLength = 100000,oneGroup = 10,zeroGroup = 5) == 566857578
    assert candidate(minLength = 500,maxLength = 1500,oneGroup = 7,zeroGroup = 11) == 894054205
    assert candidate(minLength = 6,maxLength = 10,oneGroup = 5,zeroGroup = 4) == 4
    assert candidate(minLength = 10,maxLength = 100,oneGroup = 5,zeroGroup = 5) == 2097148
    assert candidate(minLength = 10,maxLength = 15,oneGroup = 4,zeroGroup = 2) == 42
    assert candidate(minLength = 5,maxLength = 10,oneGroup = 2,zeroGroup = 3) == 23
    assert candidate(minLength = 30,maxLength = 90,oneGroup = 3,zeroGroup = 5) == 13571760
    assert candidate(minLength = 5000,maxLength = 6000,oneGroup = 1000,zeroGroup = 1200) == 33
    assert candidate(minLength = 8,maxLength = 12,oneGroup = 2,zeroGroup = 2) == 112
    assert candidate(minLength = 25,maxLength = 75,oneGroup = 8,zeroGroup = 12) == 256
    assert candidate(minLength = 10,maxLength = 50,oneGroup = 5,zeroGroup = 1) == 2630338
    assert candidate(minLength = 50,maxLength = 100,oneGroup = 25,zeroGroup = 20) == 26
    assert candidate(minLength = 10,maxLength = 20,oneGroup = 5,zeroGroup = 6) == 13
    assert candidate(minLength = 100,maxLength = 200,oneGroup = 25,zeroGroup = 30) == 233
    assert candidate(minLength = 200,maxLength = 500,oneGroup = 50,zeroGroup = 25) == 28602
    assert candidate(minLength = 50000,maxLength = 100000,oneGroup = 25000,zeroGroup = 30000) == 13
    assert candidate(minLength = 1000,maxLength = 1500,oneGroup = 100,zeroGroup = 200) == 2440
    assert candidate(minLength = 1,maxLength = 100000,oneGroup = 5,zeroGroup = 7) == 809265852
    assert candidate(minLength = 1,maxLength = 100000,oneGroup = 1,zeroGroup = 1) == 215447031
    assert candidate(minLength = 30000,maxLength = 40000,oneGroup = 15,zeroGroup = 10) == 620090248
    assert candidate(minLength = 20,maxLength = 30,oneGroup = 5,zeroGroup = 6) == 49
    assert candidate(minLength = 12,maxLength = 25,oneGroup = 7,zeroGroup = 9) == 11
    assert candidate(minLength = 1000,maxLength = 5000,oneGroup = 100,zeroGroup = 200) == 316290658
    assert candidate(minLength = 5,maxLength = 15,oneGroup = 2,zeroGroup = 4) == 50
    assert candidate(minLength = 30,maxLength = 150,oneGroup = 6,zeroGroup = 4) == 422361979
    assert candidate(minLength = 20,maxLength = 50,oneGroup = 10,zeroGroup = 8) == 64
    assert candidate(minLength = 10,maxLength = 20,oneGroup = 5,zeroGroup = 5) == 28
    assert candidate(minLength = 50,maxLength = 50,oneGroup = 5,zeroGroup = 10) == 89
    assert candidate(minLength = 50,maxLength = 75,oneGroup = 10,zeroGroup = 15) == 93
    assert candidate(minLength = 500,maxLength = 700,oneGroup = 50,zeroGroup = 75) == 4059
    assert candidate(minLength = 50000,maxLength = 100000,oneGroup = 25000,zeroGroup = 25000) == 28
    assert candidate(minLength = 15,maxLength = 100,oneGroup = 8,zeroGroup = 5) == 80400
    assert candidate(minLength = 10,maxLength = 20,oneGroup = 4,zeroGroup = 6) == 23
    assert candidate(minLength = 10,maxLength = 20,oneGroup = 4,zeroGroup = 5) == 26
    assert candidate(minLength = 2,maxLength = 2,oneGroup = 1,zeroGroup = 1) == 4
    assert candidate(minLength = 30000,maxLength = 50000,oneGroup = 5,zeroGroup = 8) == 106251649
    assert candidate(minLength = 100,maxLength = 200,oneGroup = 15,zeroGroup = 20) == 4602
    assert candidate(minLength = 50000,maxLength = 100000,oneGroup = 10,zeroGroup = 15) == 945515466
    assert candidate(minLength = 7,maxLength = 40,oneGroup = 3,zeroGroup = 7) == 597
    assert candidate(minLength = 10,maxLength = 20,oneGroup = 4,zeroGroup = 7) == 16
    assert candidate(minLength = 15,maxLength = 25,oneGroup = 3,zeroGroup = 9) == 32
    assert candidate(minLength = 8,maxLength = 30,oneGroup = 5,zeroGroup = 4) == 153
    assert candidate(minLength = 6,maxLength = 25,oneGroup = 3,zeroGroup = 3) == 508
    assert candidate(minLength = 20,maxLength = 50,oneGroup = 7,zeroGroup = 10) == 80
    assert candidate(minLength = 100,maxLength = 1000,oneGroup = 10,zeroGroup = 20) == 252403212
    assert candidate(minLength = 30000,maxLength = 40000,oneGroup = 5000,zeroGroup = 2500) == 3804
    assert candidate(minLength = 7,maxLength = 14,oneGroup = 3,zeroGroup = 7) == 9
    assert candidate(minLength = 20,maxLength = 50,oneGroup = 7,zeroGroup = 11) == 74
    assert candidate(minLength = 50000,maxLength = 100000,oneGroup = 25,zeroGroup = 20) == 165911007
    assert candidate(minLength = 120,maxLength = 250,oneGroup = 9,zeroGroup = 18) == 831053
    assert candidate(minLength = 15,maxLength = 30,oneGroup = 5,zeroGroup = 5) == 120
    assert candidate(minLength = 60,maxLength = 70,oneGroup = 12,zeroGroup = 18) == 16
    assert candidate(minLength = 1,maxLength = 1000,oneGroup = 1,zeroGroup = 1) == 376846411
    assert candidate(minLength = 7,maxLength = 14,oneGroup = 3,zeroGroup = 4) == 22
    assert candidate(minLength = 10,maxLength = 20,oneGroup = 2,zeroGroup = 3) == 444
    assert candidate(minLength = 70000,maxLength = 80000,oneGroup = 10000,zeroGroup = 15000) == 86
    assert candidate(minLength = 3000,maxLength = 3500,oneGroup = 500,zeroGroup = 600) == 65
    assert candidate(minLength = 20,maxLength = 30,oneGroup = 6,zeroGroup = 7) == 21
    assert candidate(minLength = 100,maxLength = 120,oneGroup = 20,zeroGroup = 25) == 33
    assert candidate(minLength = 10000,maxLength = 100000,oneGroup = 100,zeroGroup = 50) == 816036866
    assert candidate(minLength = 25,maxLength = 70,oneGroup = 11,zeroGroup = 10) == 121
    assert candidate(minLength = 40,maxLength = 80,oneGroup = 8,zeroGroup = 16) == 220
    assert candidate(minLength = 1,maxLength = 10,oneGroup = 3,zeroGroup = 4) == 10
    assert candidate(minLength = 50,maxLength = 100,oneGroup = 10,zeroGroup = 15) == 444
    assert candidate(minLength = 5,maxLength = 100000,oneGroup = 1,zeroGroup = 1) == 215447001
    assert candidate(minLength = 20,maxLength = 30,oneGroup = 7,zeroGroup = 14) == 8
    assert candidate(minLength = 1,maxLength = 100,oneGroup = 1,zeroGroup = 1) == 952742561
    assert candidate(minLength = 10,maxLength = 50,oneGroup = 5,zeroGroup = 2) == 70067
    assert candidate(minLength = 1,maxLength = 100000,oneGroup = 50000,zeroGroup = 50000) == 6
    assert candidate(minLength = 15,maxLength = 25,oneGroup = 5,zeroGroup = 5) == 56
    assert candidate(minLength = 15,maxLength = 60,oneGroup = 5,zeroGroup = 6) == 3065
    assert candidate(minLength = 25,maxLength = 50,oneGroup = 10,zeroGroup = 20) == 16
    assert candidate(minLength = 25000,maxLength = 75000,oneGroup = 12,zeroGroup = 20) == 285553317
    assert candidate(minLength = 50,maxLength = 70,oneGroup = 10,zeroGroup = 15) == 65
    assert candidate(minLength = 1000,maxLength = 10000,oneGroup = 500,zeroGroup = 750) == 128797
    assert candidate(minLength = 2000,maxLength = 2500,oneGroup = 300,zeroGroup = 400) == 166
    assert candidate(minLength = 25000,maxLength = 75000,oneGroup = 50,zeroGroup = 60) == 547461537
    assert candidate(minLength = 5,maxLength = 15,oneGroup = 2,zeroGroup = 5) == 37
    assert candidate(minLength = 10000,maxLength = 100000,oneGroup = 5,zeroGroup = 10) == 444309034
    assert candidate(minLength = 5,maxLength = 15,oneGroup = 2,zeroGroup = 3) == 109
    assert candidate(minLength = 5000,maxLength = 10000,oneGroup = 20,zeroGroup = 15) == 627599613
    assert candidate(minLength = 5,maxLength = 5,oneGroup = 5,zeroGroup = 5) == 2


