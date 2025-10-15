def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 2,queries = [[0, 0, 1], [1, 0, 2], [0, 1, 3], [1, 1, 4]]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,queries = [[0, 0, 1], [1, 0, 2], [0, 1, 3], [1, 1, 4]]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,queries = [[0, 1, 10], [1, 2, 5], [0, 4, 7], [1, 0, 3]]) == 93
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,queries = [[0, 1, 10], [1, 2, 5], [0, 4, 7], [1, 0, 3]]) == 93: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,queries = [[1, 3, 2], [0, 1, 5], [1, 0, 3], [0, 2, 4]]) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,queries = [[1, 3, 2], [0, 1, 5], [1, 0, 3], [0, 2, 4]]) == 44: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,queries = [[0, 0, 10], [1, 0, 20]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,queries = [[0, 0, 10], [1, 0, 20]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,queries = [[0, 0, 1], [0, 1, 2], [1, 0, 3], [1, 1, 4]]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,queries = [[0, 0, 1], [0, 1, 2], [1, 0, 3], [1, 1, 4]]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,queries = [[0, 0, 100]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,queries = [[0, 0, 100]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,queries = [[0, 0, 4], [0, 1, 2], [1, 0, 1], [0, 2, 3], [1, 2, 1]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,queries = [[0, 0, 4], [0, 1, 2], [1, 0, 1], [0, 2, 3], [1, 2, 1]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,queries = [[1, 0, 5], [1, 1, 10], [0, 0, 15], [0, 1, 20]]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,queries = [[1, 0, 5], [1, 1, 10], [0, 0, 15], [0, 1, 20]]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,queries = [[1, 0, 10], [0, 2, 3], [1, 4, 5]]) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,queries = [[1, 0, 10], [0, 2, 3], [1, 4, 5]]) == 77: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,queries = [[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4]]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,queries = [[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4]]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,queries = [[0, 1, 5], [1, 3, 2], [0, 3, 1]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,queries = [[0, 1, 5], [1, 3, 2], [0, 3, 1]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,queries = [[0, 1, 5], [1, 3, 4], [0, 2, 6], [1, 0, 2], [0, 0, 3]]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,queries = [[0, 1, 5], [1, 3, 4], [0, 2, 6], [1, 0, 2], [0, 0, 3]]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,queries = [[0, 0, 1], [1, 0, 2], [0, 1, 3], [1, 1, 4], [0, 2, 5], [1, 2, 6], [0, 3, 7], [1, 3, 8], [0, 4, 9], [1, 4, 10]]) == 549905
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,queries = [[0, 0, 1], [1, 0, 2], [0, 1, 3], [1, 1, 4], [0, 2, 5], [1, 2, 6], [0, 3, 7], [1, 3, 8], [0, 4, 9], [1, 4, 10]]) == 549905: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,queries = [[1, 0, 10], [0, 0, 5], [1, 1, 20], [0, 1, 10], [1, 2, 30], [0, 2, 15], [1, 3, 40], [0, 3, 20], [1, 4, 50], [0, 4, 25]]) == 675
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,queries = [[1, 0, 10], [0, 0, 5], [1, 1, 20], [0, 1, 10], [1, 2, 30], [0, 2, 15], [1, 3, 40], [0, 3, 20], [1, 4, 50], [0, 4, 25]]) == 675: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,queries = [[0, 0, 10], [1, 0, 20], [0, 1, 30], [1, 1, 40], [0, 2, 50], [1, 2, 60], [0, 3, 70], [1, 3, 80], [0, 4, 90], [1, 4, 100], [0, 5, 110], [1, 5, 120], [0, 6, 130], [1, 6, 140], [0, 7, 150], [1, 7, 160], [0, 8, 170], [1, 8, 180], [0, 9, 190], [1, 9, 200]]) == 13850
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,queries = [[0, 0, 10], [1, 0, 20], [0, 1, 30], [1, 1, 40], [0, 2, 50], [1, 2, 60], [0, 3, 70], [1, 3, 80], [0, 4, 90], [1, 4, 100], [0, 5, 110], [1, 5, 120], [0, 6, 130], [1, 6, 140], [0, 7, 150], [1, 7, 160], [0, 8, 170], [1, 8, 180], [0, 9, 190], [1, 9, 200]]) == 13850: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [0, 6, 7], [0, 7, 8], [1, 0, 9], [1, 1, 10], [1, 2, 11], [1, 3, 12], [1, 4, 13], [1, 5, 14], [1, 6, 15], [1, 7, 16]]) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [0, 6, 7], [0, 7, 8], [1, 0, 9], [1, 1, 10], [1, 2, 11], [1, 3, 12], [1, 4, 13], [1, 5, 14], [1, 6, 15], [1, 7, 16]]) == 800: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,queries = [[0, 0, 5], [1, 1, 3], [0, 2, 2], [1, 3, 1], [0, 0, 4], [1, 2, 6]]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,queries = [[0, 0, 5], [1, 1, 3], [0, 2, 2], [1, 3, 1], [0, 0, 4], [1, 2, 6]]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [1, 0, 1], [1, 1, 2], [1, 2, 3], [1, 3, 4], [1, 4, 5], [1, 5, 6]]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [1, 0, 1], [1, 1, 2], [1, 2, 3], [1, 3, 4], [1, 4, 5], [1, 5, 6]]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,queries = [[0, 0, 100000], [1, 0, 100000], [0, 1, 100000], [1, 1, 100000], [0, 2, 100000], [1, 2, 100000]]) == 599100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,queries = [[0, 0, 100000], [1, 0, 100000], [0, 1, 100000], [1, 1, 100000], [0, 2, 100000], [1, 2, 100000]]) == 599100000: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,queries = [[0, 0, 1], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 4, 5]]) == 62
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,queries = [[0, 0, 1], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 4, 5]]) == 62: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,queries = [[0, 0, 1], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 4, 5], [1, 5, 6], [0, 6, 7], [1, 7, 8], [0, 8, 9], [1, 9, 10]]) == 455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,queries = [[0, 0, 1], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 4, 5], [1, 5, 6], [0, 6, 7], [1, 7, 8], [0, 8, 9], [1, 9, 10]]) == 455: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [0, 6, 7], [0, 7, 8], [0, 8, 9], [0, 9, 10], [1, 0, 10], [1, 1, 9], [1, 2, 8], [1, 3, 7], [1, 4, 6], [1, 5, 5], [1, 6, 4], [1, 7, 3], [1, 8, 2], [1, 9, 1]]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [0, 6, 7], [0, 7, 8], [0, 8, 9], [0, 9, 10], [1, 0, 10], [1, 1, 9], [1, 2, 8], [1, 3, 7], [1, 4, 6], [1, 5, 5], [1, 6, 4], [1, 7, 3], [1, 8, 2], [1, 9, 1]]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,queries = [[0, 0, 100], [1, 1, 200], [0, 2, 300], [1, 3, 400], [0, 4, 500], [1, 0, 600], [0, 5, 700], [1, 2, 800], [0, 6, 900], [1, 3, 1000]]) == 43100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,queries = [[0, 0, 100], [1, 1, 200], [0, 2, 300], [1, 3, 400], [0, 4, 500], [1, 0, 600], [0, 5, 700], [1, 2, 800], [0, 6, 900], [1, 3, 1000]]) == 43100: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,queries = [[0, 6, 1], [0, 5, 2], [0, 4, 3], [0, 3, 4], [0, 2, 5], [0, 1, 6], [0, 0, 7], [1, 0, 8], [1, 1, 9], [1, 2, 10], [1, 3, 11], [1, 4, 12], [1, 5, 13], [1, 6, 14]]) == 539
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,queries = [[0, 6, 1], [0, 5, 2], [0, 4, 3], [0, 3, 4], [0, 2, 5], [0, 1, 6], [0, 0, 7], [1, 0, 8], [1, 1, 9], [1, 2, 10], [1, 3, 11], [1, 4, 12], [1, 5, 13], [1, 6, 14]]) == 539: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,queries = [[0, 3, 7], [1, 4, 9], [0, 2, 5], [1, 1, 3], [0, 5, 6], [1, 8, 2], [0, 9, 8], [1, 0, 4]]) == 342
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,queries = [[0, 3, 7], [1, 4, 9], [0, 2, 5], [1, 1, 3], [0, 5, 6], [1, 8, 2], [0, 9, 8], [1, 0, 4]]) == 342: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,queries = [[0, 0, 5], [1, 0, 5], [0, 1, 10], [1, 1, 10], [0, 2, 15], [1, 2, 15], [0, 3, 20], [1, 3, 20]]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,queries = [[0, 0, 5], [1, 0, 5], [0, 1, 10], [1, 1, 10], [0, 2, 15], [1, 2, 15], [0, 3, 20], [1, 3, 20]]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,queries = [[0, 0, 10], [1, 1, 20], [0, 2, 30], [1, 3, 40], [0, 4, 50], [1, 0, 60], [0, 1, 70], [1, 2, 80], [0, 3, 90], [1, 4, 100]]) == 1800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,queries = [[0, 0, 10], [1, 1, 20], [0, 2, 30], [1, 3, 40], [0, 4, 50], [1, 0, 60], [0, 1, 70], [1, 2, 80], [0, 3, 90], [1, 4, 100]]) == 1800: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,queries = [[0, 0, 1], [1, 0, 2], [0, 1, 3], [1, 1, 4], [0, 2, 5], [1, 2, 6], [0, 3, 7], [1, 3, 8], [0, 4, 9], [1, 4, 10]]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,queries = [[0, 0, 1], [1, 0, 2], [0, 1, 3], [1, 1, 4], [0, 2, 5], [1, 2, 6], [0, 3, 7], [1, 3, 8], [0, 4, 9], [1, 4, 10]]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,queries = [[1, 0, 1], [1, 1, 2], [1, 2, 3], [1, 3, 4], [1, 4, 5], [1, 5, 6], [1, 6, 7], [1, 7, 8], [0, 0, 10], [0, 1, 20], [0, 2, 30], [0, 3, 40], [0, 4, 50], [0, 5, 60], [0, 6, 70], [0, 7, 80]]) == 2880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,queries = [[1, 0, 1], [1, 1, 2], [1, 2, 3], [1, 3, 4], [1, 4, 5], [1, 5, 6], [1, 6, 7], [1, 7, 8], [0, 0, 10], [0, 1, 20], [0, 2, 30], [0, 3, 40], [0, 4, 50], [0, 5, 60], [0, 6, 70], [0, 7, 80]]) == 2880: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,queries = [[0, 1, 3], [1, 2, 4], [0, 3, 5], [1, 4, 6], [0, 0, 7], [1, 0, 8], [0, 2, 9]]) == 152
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,queries = [[0, 1, 3], [1, 2, 4], [0, 3, 5], [1, 4, 6], [0, 0, 7], [1, 0, 8], [0, 2, 9]]) == 152: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,queries = [[0, 0, 1], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 1, 5], [1, 0, 6], [0, 3, 7], [1, 2, 8]]) == 94
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,queries = [[0, 0, 1], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 1, 5], [1, 0, 6], [0, 3, 7], [1, 2, 8]]) == 94: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,queries = [[0, 0, 1], [1, 0, 2], [0, 1, 3], [1, 1, 4], [0, 2, 5], [1, 2, 6], [0, 3, 7], [1, 3, 8], [0, 4, 9], [1, 4, 10], [0, 5, 11], [1, 5, 12], [0, 6, 13], [1, 6, 14], [0, 7, 15], [1, 7, 16]]) == 716
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,queries = [[0, 0, 1], [1, 0, 2], [0, 1, 3], [1, 1, 4], [0, 2, 5], [1, 2, 6], [0, 3, 7], [1, 3, 8], [0, 4, 9], [1, 4, 10], [0, 5, 11], [1, 5, 12], [0, 6, 13], [1, 6, 14], [0, 7, 15], [1, 7, 16]]) == 716: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,queries = [[0, 0, 20], [1, 0, 21], [0, 1, 22], [1, 1, 23], [0, 2, 24], [1, 2, 25], [0, 3, 26], [1, 3, 27], [0, 4, 28], [1, 4, 29], [0, 5, 30], [1, 5, 31], [0, 6, 32], [1, 6, 33], [0, 7, 34], [1, 7, 35]]) == 1932
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,queries = [[0, 0, 20], [1, 0, 21], [0, 1, 22], [1, 1, 23], [0, 2, 24], [1, 2, 25], [0, 3, 26], [1, 3, 27], [0, 4, 28], [1, 4, 29], [0, 5, 30], [1, 5, 31], [0, 6, 32], [1, 6, 33], [0, 7, 34], [1, 7, 35]]) == 1932: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,queries = [[0, 1, 100], [1, 3, 200], [0, 2, 50], [1, 1, 150], [0, 4, 250], [1, 0, 300]]) == 5100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,queries = [[0, 1, 100], [1, 3, 200], [0, 2, 50], [1, 1, 150], [0, 4, 250], [1, 0, 300]]) == 5100: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,queries = [[1, 0, 10], [0, 0, 20], [1, 1, 30], [0, 1, 40], [1, 2, 50], [0, 2, 60], [1, 3, 70], [0, 3, 80]]) == 940
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,queries = [[1, 0, 10], [0, 0, 20], [1, 1, 30], [0, 1, 40], [1, 2, 50], [0, 2, 60], [1, 3, 70], [0, 3, 80]]) == 940: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,queries = [[0, 1, 5], [1, 2, 8], [0, 3, 9], [1, 0, 4], [0, 2, 6], [1, 1, 7]]) == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,queries = [[0, 1, 5], [1, 2, 8], [0, 3, 9], [1, 0, 4], [0, 2, 6], [1, 1, 7]]) == 97: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,queries = [[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4], [0, 1, 5], [1, 1, 6]]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,queries = [[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4], [0, 1, 5], [1, 1, 6]]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,queries = [[0, 0, 10], [1, 0, 20], [0, 1, 30], [1, 1, 40], [0, 2, 50], [1, 2, 60]]) == 410
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,queries = [[0, 0, 10], [1, 0, 20], [0, 1, 30], [1, 1, 40], [0, 2, 50], [1, 2, 60]]) == 410: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,queries = [[0, 0, 10], [1, 1, 5], [0, 2, 3], [1, 3, 7], [0, 4, 2], [1, 0, 8]]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,queries = [[0, 0, 10], [1, 1, 5], [0, 2, 3], [1, 3, 7], [0, 4, 2], [1, 0, 8]]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,queries = [[0, 7, 5], [1, 6, 4], [0, 5, 3], [1, 4, 2], [0, 3, 1], [1, 2, 6], [0, 1, 7], [1, 0, 8], [0, 6, 9], [1, 7, 10]]) == 335
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,queries = [[0, 7, 5], [1, 6, 4], [0, 5, 3], [1, 4, 2], [0, 3, 1], [1, 2, 6], [0, 1, 7], [1, 0, 8], [0, 6, 9], [1, 7, 10]]) == 335: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,queries = [[0, 6, 11], [1, 5, 12], [0, 4, 13], [1, 3, 14], [0, 2, 15], [1, 1, 16], [0, 0, 17], [1, 6, 18], [0, 5, 19], [1, 4, 20]]) == 740
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,queries = [[0, 6, 11], [1, 5, 12], [0, 4, 13], [1, 3, 14], [0, 2, 15], [1, 1, 16], [0, 0, 17], [1, 6, 18], [0, 5, 19], [1, 4, 20]]) == 740: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,queries = [[0, 9, 1], [1, 8, 2], [0, 7, 3], [1, 6, 4], [0, 5, 5], [1, 4, 6], [0, 3, 7], [1, 2, 8], [0, 1, 9], [1, 0, 10], [0, 8, 11], [1, 7, 12], [0, 6, 13], [1, 5, 14], [0, 4, 15], [1, 3, 16], [0, 2, 17], [1, 1, 18], [0, 0, 19], [1, 9, 20]]) == 1385
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,queries = [[0, 9, 1], [1, 8, 2], [0, 7, 3], [1, 6, 4], [0, 5, 5], [1, 4, 6], [0, 3, 7], [1, 2, 8], [0, 1, 9], [1, 0, 10], [0, 8, 11], [1, 7, 12], [0, 6, 13], [1, 5, 14], [0, 4, 15], [1, 3, 16], [0, 2, 17], [1, 1, 18], [0, 0, 19], [1, 9, 20]]) == 1385: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,queries = [[0, 0, 2], [1, 0, 3], [0, 1, 4], [1, 1, 5], [0, 2, 6], [1, 2, 7], [0, 3, 8], [1, 3, 9], [0, 4, 10], [1, 4, 11], [0, 5, 12], [1, 5, 13], [0, 6, 14], [1, 6, 15], [0, 7, 16], [1, 7, 17], [0, 8, 18], [1, 8, 19]]) == 1095
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,queries = [[0, 0, 2], [1, 0, 3], [0, 1, 4], [1, 1, 5], [0, 2, 6], [1, 2, 7], [0, 3, 8], [1, 3, 9], [0, 4, 10], [1, 4, 11], [0, 5, 12], [1, 5, 13], [0, 6, 14], [1, 6, 15], [0, 7, 16], [1, 7, 17], [0, 8, 18], [1, 8, 19]]) == 1095: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,queries = [[0, 0, 5], [1, 1, 3], [0, 2, 8], [1, 3, 2], [0, 4, 1], [1, 0, 4]]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,queries = [[0, 0, 5], [1, 1, 3], [0, 2, 8], [1, 3, 2], [0, 4, 1], [1, 0, 4]]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,queries = [[0, 2, 100], [1, 3, 200], [0, 0, 300], [1, 1, 400], [0, 4, 500], [1, 5, 600], [0, 5, 700], [1, 0, 800]]) == 16600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,queries = [[0, 2, 100], [1, 3, 200], [0, 0, 300], [1, 1, 400], [0, 4, 500], [1, 5, 600], [0, 5, 700], [1, 0, 800]]) == 16600: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,queries = [[0, 0, 1], [0, 0, 2], [0, 0, 3], [1, 0, 4], [1, 0, 5], [1, 0, 6], [0, 1, 7], [1, 1, 8], [0, 2, 9], [1, 2, 10], [0, 3, 11], [1, 3, 12]]) == 158
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,queries = [[0, 0, 1], [0, 0, 2], [0, 0, 3], [1, 0, 4], [1, 0, 5], [1, 0, 6], [0, 1, 7], [1, 1, 8], [0, 2, 9], [1, 2, 10], [0, 3, 11], [1, 3, 12]]) == 158: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,queries = [[0, 0, 5], [1, 1, 6], [0, 2, 7], [1, 3, 8], [0, 1, 9]]) == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,queries = [[0, 0, 5], [1, 1, 6], [0, 2, 7], [1, 3, 8], [0, 1, 9]]) == 103: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,queries = [[0, 0, 1], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 4, 5], [1, 0, 6], [0, 3, 7], [1, 2, 8], [0, 1, 9], [1, 4, 10]]) == 274905
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,queries = [[0, 0, 1], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 4, 5], [1, 0, 6], [0, 3, 7], [1, 2, 8], [0, 1, 9], [1, 4, 10]]) == 274905: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,queries = [[0, 0, 1], [1, 5, 2], [0, 4, 3], [1, 3, 4], [0, 2, 5], [1, 1, 6], [0, 1, 7], [1, 0, 8]]) == 166
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,queries = [[0, 0, 1], [1, 5, 2], [0, 4, 3], [1, 3, 4], [0, 2, 5], [1, 1, 6], [0, 1, 7], [1, 0, 8]]) == 166: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,queries = [[1, 0, 1], [0, 0, 2], [1, 1, 3], [0, 1, 4], [1, 2, 5], [0, 2, 6]]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,queries = [[1, 0, 1], [0, 0, 2], [1, 1, 3], [0, 1, 4], [1, 2, 5], [0, 2, 6]]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,queries = [[0, 0, 5], [1, 1, 10], [0, 2, 20], [1, 3, 30], [0, 1, 50], [1, 0, 60]]) == 545
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,queries = [[0, 0, 5], [1, 1, 10], [0, 2, 20], [1, 3, 30], [0, 1, 50], [1, 0, 60]]) == 545: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,queries = [[0, 0, 5], [0, 1, 5], [0, 2, 5], [1, 0, 5], [1, 1, 5], [1, 2, 5]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,queries = [[0, 0, 5], [0, 1, 5], [0, 2, 5], [1, 0, 5], [1, 1, 5], [1, 2, 5]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,queries = [[0, 6, 70], [1, 5, 60], [0, 4, 50], [1, 3, 40], [0, 2, 30], [1, 1, 20], [0, 0, 10], [1, 0, 0], [0, 1, 1], [1, 2, 2], [0, 3, 3], [1, 4, 4], [0, 5, 5], [1, 6, 6]]) == 465
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,queries = [[0, 6, 70], [1, 5, 60], [0, 4, 50], [1, 3, 40], [0, 2, 30], [1, 1, 20], [0, 0, 10], [1, 0, 0], [0, 1, 1], [1, 2, 2], [0, 3, 3], [1, 4, 4], [0, 5, 5], [1, 6, 6]]) == 465: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [1, 0, 6], [1, 1, 7], [1, 2, 8], [1, 3, 9], [1, 4, 10], [0, 0, 11], [0, 1, 12], [0, 2, 13], [0, 3, 14], [0, 4, 15], [1, 0, 16], [1, 1, 17], [1, 2, 18], [1, 3, 19], [1, 4, 20]]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [1, 0, 6], [1, 1, 7], [1, 2, 8], [1, 3, 9], [1, 4, 10], [0, 0, 11], [0, 1, 12], [0, 2, 13], [0, 3, 14], [0, 4, 15], [1, 0, 16], [1, 1, 17], [1, 2, 18], [1, 3, 19], [1, 4, 20]]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,queries = [[1, 0, 1], [1, 1, 2], [1, 2, 3], [1, 3, 4], [1, 4, 5], [1, 5, 6], [1, 6, 7], [1, 7, 8], [1, 8, 9], [1, 9, 10]]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,queries = [[1, 0, 1], [1, 1, 2], [1, 2, 3], [1, 3, 4], [1, 4, 5], [1, 5, 6], [1, 6, 7], [1, 7, 8], [1, 8, 9], [1, 9, 10]]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,queries = [[0, 500, 1], [1, 500, 2], [0, 499, 3], [1, 499, 4], [0, 498, 5], [1, 498, 6], [0, 497, 7], [1, 497, 8], [0, 496, 9], [1, 496, 10]]) == 54905
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,queries = [[0, 500, 1], [1, 500, 2], [0, 499, 3], [1, 499, 4], [0, 498, 5], [1, 498, 6], [0, 497, 7], [1, 497, 8], [0, 496, 9], [1, 496, 10]]) == 54905: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,queries = [[0, 2500, 1], [1, 2500, 2], [0, 2499, 3], [1, 2499, 4], [0, 2498, 5], [1, 2498, 6], [0, 2497, 7], [1, 2497, 8], [0, 2496, 9], [1, 2496, 10]]) == 274905
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,queries = [[0, 2500, 1], [1, 2500, 2], [0, 2499, 3], [1, 2499, 4], [0, 2498, 5], [1, 2498, 6], [0, 2497, 7], [1, 2497, 8], [0, 2496, 9], [1, 2496, 10]]) == 274905: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,queries = [[0, 500, 5], [1, 250, 10], [0, 750, 20], [1, 0, 30], [0, 999, 50], [1, 500, 60]]) == 174845
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,queries = [[0, 500, 5], [1, 250, 10], [0, 750, 20], [1, 0, 30], [0, 999, 50], [1, 500, 60]]) == 174845: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,queries = [[0, 0, 10], [1, 0, 20], [0, 1, 30], [1, 1, 40], [0, 2, 50], [1, 2, 60], [0, 0, 70], [1, 0, 80]]) == 590
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,queries = [[0, 0, 10], [1, 0, 20], [0, 1, 30], [1, 1, 40], [0, 2, 50], [1, 2, 60], [0, 0, 70], [1, 0, 80]]) == 590: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [1, 0, 6], [1, 1, 7], [1, 2, 8], [1, 3, 9], [1, 4, 10]]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [1, 0, 6], [1, 1, 7], [1, 2, 8], [1, 3, 9], [1, 4, 10]]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,queries = [[0, 0, 10], [1, 2, 5], [0, 3, 3], [1, 1, 7], [0, 2, 8], [1, 3, 2]]) == 79
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,queries = [[0, 0, 10], [1, 2, 5], [0, 3, 3], [1, 1, 7], [0, 2, 8], [1, 3, 2]]) == 79: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,queries = [[0, 50, 10], [1, 50, 20], [0, 25, 15], [1, 75, 25], [0, 75, 30], [1, 25, 35], [0, 0, 5], [1, 99, 50]]) == 18705
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,queries = [[0, 50, 10], [1, 50, 20], [0, 25, 15], [1, 75, 25], [0, 75, 30], [1, 25, 35], [0, 0, 5], [1, 99, 50]]) == 18705: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,queries = [[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4], [0, 1, 5], [1, 1, 6], [0, 0, 7], [1, 2, 8]]) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,queries = [[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4], [0, 1, 5], [1, 1, 6], [0, 0, 7], [1, 2, 8]]) == 59: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,queries = [[0, 5, 9], [1, 4, 8], [0, 9, 7], [1, 3, 6], [0, 2, 5], [1, 1, 4], [0, 0, 3], [1, 8, 2], [0, 7, 1], [1, 6, 0]]) == 295
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,queries = [[0, 5, 9], [1, 4, 8], [0, 9, 7], [1, 3, 6], [0, 2, 5], [1, 1, 4], [0, 0, 3], [1, 8, 2], [0, 7, 1], [1, 6, 0]]) == 295: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,queries = [[0, 0, 10], [1, 0, 10], [0, 1, 20], [1, 1, 20], [0, 2, 30], [1, 2, 30], [0, 3, 40], [1, 3, 40], [0, 4, 50], [1, 4, 50], [0, 5, 60], [1, 5, 60], [0, 6, 70], [1, 6, 70], [0, 7, 80], [1, 7, 80], [0, 8, 90], [1, 8, 90], [0, 9, 100], [1, 9, 100]]) == 7150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,queries = [[0, 0, 10], [1, 0, 10], [0, 1, 20], [1, 1, 20], [0, 2, 30], [1, 2, 30], [0, 3, 40], [1, 3, 40], [0, 4, 50], [1, 4, 50], [0, 5, 60], [1, 5, 60], [0, 6, 70], [1, 6, 70], [0, 7, 80], [1, 7, 80], [0, 8, 90], [1, 8, 90], [0, 9, 100], [1, 9, 100]]) == 7150: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,queries = [[0, 0, 1], [0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [1, 0, 1], [1, 1, 1], [1, 2, 1], [1, 3, 1], [1, 4, 1]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,queries = [[0, 0, 1], [0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [1, 0, 1], [1, 1, 1], [1, 2, 1], [1, 3, 1], [1, 4, 1]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,queries = [[0, 0, 1], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 4, 5], [1, 5, 6], [0, 6, 7], [1, 6, 8], [0, 5, 9], [1, 4, 10]]) == 290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,queries = [[0, 0, 1], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 4, 5], [1, 5, 6], [0, 6, 7], [1, 6, 8], [0, 5, 9], [1, 4, 10]]) == 290: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [1, 0, 6], [1, 1, 5], [1, 2, 4], [1, 3, 3], [1, 4, 2], [1, 5, 1]]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [1, 0, 6], [1, 1, 5], [1, 2, 4], [1, 3, 3], [1, 4, 2], [1, 5, 1]]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,queries = [[0, 5, 50], [1, 4, 40], [0, 3, 30], [1, 2, 20], [0, 1, 10], [1, 0, 0], [0, 4, 400], [1, 5, 500], [0, 2, 200], [1, 3, 300]]) == 7180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,queries = [[0, 5, 50], [1, 4, 40], [0, 3, 30], [1, 2, 20], [0, 1, 10], [1, 0, 0], [0, 4, 400], [1, 5, 500], [0, 2, 200], [1, 3, 300]]) == 7180: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,queries = [[0, 0, 10], [1, 1, 20], [0, 2, 30], [1, 3, 40], [0, 4, 50]]) == 620
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,queries = [[0, 0, 10], [1, 1, 20], [0, 2, 30], [1, 3, 40], [0, 4, 50]]) == 620: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,queries = [[1, 0, 1], [1, 1, 2], [1, 2, 3], [1, 3, 4], [1, 4, 5], [0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5]]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,queries = [[1, 0, 1], [1, 1, 2], [1, 2, 3], [1, 3, 4], [1, 4, 5], [0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5]]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,queries = [[0, 0, 1], [0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [0, 5, 1], [0, 6, 1], [1, 0, 1], [1, 1, 1], [1, 2, 1], [1, 3, 1], [1, 4, 1], [1, 5, 1], [1, 6, 1]]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,queries = [[0, 0, 1], [0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [0, 5, 1], [0, 6, 1], [1, 0, 1], [1, 1, 1], [1, 2, 1], [1, 3, 1], [1, 4, 1], [1, 5, 1], [1, 6, 1]]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,queries = [[0, 9, 100], [1, 8, 90], [0, 7, 80], [1, 6, 70], [0, 5, 60], [1, 4, 50], [0, 3, 40], [1, 2, 30], [0, 1, 20], [1, 0, 10]]) == 3700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,queries = [[0, 9, 100], [1, 8, 90], [0, 7, 80], [1, 6, 70], [0, 5, 60], [1, 4, 50], [0, 3, 40], [1, 2, 30], [0, 1, 20], [1, 0, 10]]) == 3700: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,queries = [[0, 500, 1], [1, 500, 2], [0, 499, 3], [1, 499, 4], [0, 501, 5], [1, 501, 6], [0, 0, 10], [1, 999, 20]]) == 50947
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,queries = [[0, 500, 1], [1, 500, 2], [0, 499, 3], [1, 499, 4], [0, 501, 5], [1, 501, 6], [0, 0, 10], [1, 999, 20]]) == 50947: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,queries = [[0, 0, 1], [1, 0, 2], [0, 1, 3], [1, 1, 4], [0, 2, 5], [1, 2, 6], [0, 3, 7], [1, 3, 8], [0, 4, 9], [1, 4, 10], [0, 5, 11], [1, 5, 12], [0, 6, 13], [1, 6, 14]]) == 483
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,queries = [[0, 0, 1], [1, 0, 2], [0, 1, 3], [1, 1, 4], [0, 2, 5], [1, 2, 6], [0, 3, 7], [1, 3, 8], [0, 4, 9], [1, 4, 10], [0, 5, 11], [1, 5, 12], [0, 6, 13], [1, 6, 14]]) == 483: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,queries = [[0, 0, 5], [1, 1, 10], [0, 2, 15], [1, 3, 20], [0, 3, 25]]) == 235
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,queries = [[0, 0, 5], [1, 1, 10], [0, 2, 15], [1, 3, 20], [0, 3, 25]]) == 235: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,queries = [[0, 0, 1], [0, 1, 2], [1, 0, 3], [1, 1, 4], [0, 2, 5], [1, 2, 6], [0, 3, 7], [1, 3, 8], [0, 4, 9], [1, 4, 10]]) == 456
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,queries = [[0, 0, 1], [0, 1, 2], [1, 0, 3], [1, 1, 4], [0, 2, 5], [1, 2, 6], [0, 3, 7], [1, 3, 8], [0, 4, 9], [1, 4, 10]]) == 456: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,queries = [[0, 0, 1], [1, 1, 1], [0, 2, 1], [1, 3, 1], [0, 4, 1], [1, 5, 1], [0, 5, 1], [1, 0, 1], [0, 1, 1], [1, 2, 1], [0, 3, 1], [1, 4, 1]]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,queries = [[0, 0, 1], [1, 1, 1], [0, 2, 1], [1, 3, 1], [0, 4, 1], [1, 5, 1], [0, 5, 1], [1, 0, 1], [0, 1, 1], [1, 2, 1], [0, 3, 1], [1, 4, 1]]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,queries = [[0, 0, 10], [1, 1, 20], [0, 2, 30], [1, 3, 40], [0, 4, 50], [1, 5, 60], [0, 6, 70], [1, 7, 80], [0, 8, 90], [1, 9, 100]]) == 4550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,queries = [[0, 0, 10], [1, 1, 20], [0, 2, 30], [1, 3, 40], [0, 4, 50], [1, 5, 60], [0, 6, 70], [1, 7, 80], [0, 8, 90], [1, 9, 100]]) == 4550: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,queries = [[0, 0, 1], [1, 8, 9], [0, 1, 2], [1, 7, 8], [0, 2, 3], [1, 6, 7], [0, 3, 4], [1, 5, 6], [0, 4, 5]]) == 305
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,queries = [[0, 0, 1], [1, 8, 9], [0, 1, 2], [1, 7, 8], [0, 2, 3], [1, 6, 7], [0, 3, 4], [1, 5, 6], [0, 4, 5]]) == 305: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,queries = [[0, 0, 1], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 4, 5], [1, 5, 6], [0, 6, 7], [1, 0, 8], [0, 1, 9], [1, 2, 10], [0, 3, 11], [1, 4, 12], [0, 5, 13], [1, 6, 14], [0, 0, 15], [1, 1, 16], [0, 2, 17], [1, 3, 18], [0, 4, 19], [1, 5, 20], [0, 6, 21], [1, 0, 22]]) == 875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,queries = [[0, 0, 1], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 4, 5], [1, 5, 6], [0, 6, 7], [1, 0, 8], [0, 1, 9], [1, 2, 10], [0, 3, 11], [1, 4, 12], [0, 5, 13], [1, 6, 14], [0, 0, 15], [1, 1, 16], [0, 2, 17], [1, 3, 18], [0, 4, 19], [1, 5, 20], [0, 6, 21], [1, 0, 22]]) == 875: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,queries = [[0, 0, 1], [1, 0, 2], [0, 0, 3], [1, 0, 4], [0, 0, 5], [1, 0, 6], [0, 0, 7], [1, 0, 8]]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,queries = [[0, 0, 1], [1, 0, 2], [0, 0, 3], [1, 0, 4], [0, 0, 5], [1, 0, 6], [0, 0, 7], [1, 0, 8]]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,queries = [[0, 2, 5], [1, 1, 3], [0, 0, 2], [1, 2, 8], [0, 3, 1]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,queries = [[0, 2, 5], [1, 1, 3], [0, 0, 2], [1, 2, 8], [0, 3, 1]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,queries = [[0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 0, 4], [0, 0, 5], [1, 0, 1], [1, 0, 2], [1, 0, 3], [1, 0, 4], [1, 0, 5]]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,queries = [[0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 0, 4], [0, 0, 5], [1, 0, 1], [1, 0, 2], [1, 0, 3], [1, 0, 4], [1, 0, 5]]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [1, 0, 10], [1, 1, 20], [1, 2, 30], [1, 3, 40], [1, 4, 50], [1, 5, 60]]) == 1260
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [1, 0, 10], [1, 1, 20], [1, 2, 30], [1, 3, 40], [1, 4, 50], [1, 5, 60]]) == 1260: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [0, 6, 7], [0, 7, 8], [0, 8, 9], [0, 9, 10]]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [0, 6, 7], [0, 7, 8], [0, 8, 9], [0, 9, 10]]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,queries = [[0, 0, 1], [1, 0, 2], [0, 1, 3], [1, 1, 4], [0, 2, 5], [1, 2, 6], [0, 0, 7], [1, 0, 8], [0, 1, 9], [1, 1, 10]]) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,queries = [[0, 0, 1], [1, 0, 2], [0, 1, 3], [1, 1, 4], [0, 2, 5], [1, 2, 6], [0, 0, 7], [1, 0, 8], [0, 1, 9], [1, 1, 10]]) == 77: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,queries = [[0, 0, 100], [0, 0, 200], [0, 0, 300], [1, 1, 100], [1, 1, 200], [1, 1, 300], [0, 1, 100], [0, 2, 200], [1, 0, 300], [1, 2, 400]]) == 2700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,queries = [[0, 0, 100], [0, 0, 200], [0, 0, 300], [1, 1, 100], [1, 1, 200], [1, 1, 300], [0, 1, 100], [0, 2, 200], [1, 0, 300], [1, 2, 400]]) == 2700: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,queries = [[0, 2500, 5], [1, 1250, 10], [0, 3750, 20], [1, 0, 30], [0, 4999, 50], [1, 2500, 60]]) == 874845
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,queries = [[0, 2500, 5], [1, 1250, 10], [0, 3750, 20], [1, 0, 30], [0, 4999, 50], [1, 2500, 60]]) == 874845: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,queries = [[0, 0, 5], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 3, 1], [1, 0, 6]]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,queries = [[0, 0, 5], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 3, 1], [1, 0, 6]]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,queries = [[0, 0, 100], [1, 0, 200], [0, 100, 150], [1, 200, 250], [0, 300, 300], [1, 400, 400], [0, 1, 10], [1, 2, 20], [0, 3, 30], [1, 4, 40]]) == 745580
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,queries = [[0, 0, 100], [1, 0, 200], [0, 100, 150], [1, 200, 250], [0, 300, 300], [1, 400, 400], [0, 1, 10], [1, 2, 20], [0, 3, 30], [1, 4, 40]]) == 745580: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 2,queries = [[0, 0, 1], [1, 0, 2], [0, 1, 3], [1, 1, 4]]) == 13
    assert candidate(n = 5,queries = [[0, 1, 10], [1, 2, 5], [0, 4, 7], [1, 0, 3]]) == 93
    assert candidate(n = 4,queries = [[1, 3, 2], [0, 1, 5], [1, 0, 3], [0, 2, 4]]) == 44
    assert candidate(n = 1,queries = [[0, 0, 10], [1, 0, 20]]) == 20
    assert candidate(n = 2,queries = [[0, 0, 1], [0, 1, 2], [1, 0, 3], [1, 1, 4]]) == 14
    assert candidate(n = 1,queries = [[0, 0, 100]]) == 100
    assert candidate(n = 3,queries = [[0, 0, 4], [0, 1, 2], [1, 0, 1], [0, 2, 3], [1, 2, 1]]) == 17
    assert candidate(n = 2,queries = [[1, 0, 5], [1, 1, 10], [0, 0, 15], [0, 1, 20]]) == 70
    assert candidate(n = 5,queries = [[1, 0, 10], [0, 2, 3], [1, 4, 5]]) == 77
    assert candidate(n = 3,queries = [[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4]]) == 23
    assert candidate(n = 4,queries = [[0, 1, 5], [1, 3, 2], [0, 3, 1]]) == 25
    assert candidate(n = 5,queries = [[0, 1, 5], [1, 3, 4], [0, 2, 6], [1, 0, 2], [0, 0, 3]]) == 74
    assert candidate(n = 10000,queries = [[0, 0, 1], [1, 0, 2], [0, 1, 3], [1, 1, 4], [0, 2, 5], [1, 2, 6], [0, 3, 7], [1, 3, 8], [0, 4, 9], [1, 4, 10]]) == 549905
    assert candidate(n = 5,queries = [[1, 0, 10], [0, 0, 5], [1, 1, 20], [0, 1, 10], [1, 2, 30], [0, 2, 15], [1, 3, 40], [0, 3, 20], [1, 4, 50], [0, 4, 25]]) == 675
    assert candidate(n = 10,queries = [[0, 0, 10], [1, 0, 20], [0, 1, 30], [1, 1, 40], [0, 2, 50], [1, 2, 60], [0, 3, 70], [1, 3, 80], [0, 4, 90], [1, 4, 100], [0, 5, 110], [1, 5, 120], [0, 6, 130], [1, 6, 140], [0, 7, 150], [1, 7, 160], [0, 8, 170], [1, 8, 180], [0, 9, 190], [1, 9, 200]]) == 13850
    assert candidate(n = 8,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [0, 6, 7], [0, 7, 8], [1, 0, 9], [1, 1, 10], [1, 2, 11], [1, 3, 12], [1, 4, 13], [1, 5, 14], [1, 6, 15], [1, 7, 16]]) == 800
    assert candidate(n = 4,queries = [[0, 0, 5], [1, 1, 3], [0, 2, 2], [1, 3, 1], [0, 0, 4], [1, 2, 6]]) == 49
    assert candidate(n = 6,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [1, 0, 1], [1, 1, 2], [1, 2, 3], [1, 3, 4], [1, 4, 5], [1, 5, 6]]) == 126
    assert candidate(n = 1000,queries = [[0, 0, 100000], [1, 0, 100000], [0, 1, 100000], [1, 1, 100000], [0, 2, 100000], [1, 2, 100000]]) == 599100000
    assert candidate(n = 5,queries = [[0, 0, 1], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 4, 5]]) == 62
    assert candidate(n = 10,queries = [[0, 0, 1], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 4, 5], [1, 5, 6], [0, 6, 7], [1, 7, 8], [0, 8, 9], [1, 9, 10]]) == 455
    assert candidate(n = 10,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [0, 6, 7], [0, 7, 8], [0, 8, 9], [0, 9, 10], [1, 0, 10], [1, 1, 9], [1, 2, 8], [1, 3, 7], [1, 4, 6], [1, 5, 5], [1, 6, 4], [1, 7, 3], [1, 8, 2], [1, 9, 1]]) == 550
    assert candidate(n = 10,queries = [[0, 0, 100], [1, 1, 200], [0, 2, 300], [1, 3, 400], [0, 4, 500], [1, 0, 600], [0, 5, 700], [1, 2, 800], [0, 6, 900], [1, 3, 1000]]) == 43100
    assert candidate(n = 7,queries = [[0, 6, 1], [0, 5, 2], [0, 4, 3], [0, 3, 4], [0, 2, 5], [0, 1, 6], [0, 0, 7], [1, 0, 8], [1, 1, 9], [1, 2, 10], [1, 3, 11], [1, 4, 12], [1, 5, 13], [1, 6, 14]]) == 539
    assert candidate(n = 10,queries = [[0, 3, 7], [1, 4, 9], [0, 2, 5], [1, 1, 3], [0, 5, 6], [1, 8, 2], [0, 9, 8], [1, 0, 4]]) == 342
    assert candidate(n = 4,queries = [[0, 0, 5], [1, 0, 5], [0, 1, 10], [1, 1, 10], [0, 2, 15], [1, 2, 15], [0, 3, 20], [1, 3, 20]]) == 250
    assert candidate(n = 5,queries = [[0, 0, 10], [1, 1, 20], [0, 2, 30], [1, 3, 40], [0, 4, 50], [1, 0, 60], [0, 1, 70], [1, 2, 80], [0, 3, 90], [1, 4, 100]]) == 1800
    assert candidate(n = 5,queries = [[0, 0, 1], [1, 0, 2], [0, 1, 3], [1, 1, 4], [0, 2, 5], [1, 2, 6], [0, 3, 7], [1, 3, 8], [0, 4, 9], [1, 4, 10]]) == 180
    assert candidate(n = 8,queries = [[1, 0, 1], [1, 1, 2], [1, 2, 3], [1, 3, 4], [1, 4, 5], [1, 5, 6], [1, 6, 7], [1, 7, 8], [0, 0, 10], [0, 1, 20], [0, 2, 30], [0, 3, 40], [0, 4, 50], [0, 5, 60], [0, 6, 70], [0, 7, 80]]) == 2880
    assert candidate(n = 5,queries = [[0, 1, 3], [1, 2, 4], [0, 3, 5], [1, 4, 6], [0, 0, 7], [1, 0, 8], [0, 2, 9]]) == 152
    assert candidate(n = 4,queries = [[0, 0, 1], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 1, 5], [1, 0, 6], [0, 3, 7], [1, 2, 8]]) == 94
    assert candidate(n = 8,queries = [[0, 0, 1], [1, 0, 2], [0, 1, 3], [1, 1, 4], [0, 2, 5], [1, 2, 6], [0, 3, 7], [1, 3, 8], [0, 4, 9], [1, 4, 10], [0, 5, 11], [1, 5, 12], [0, 6, 13], [1, 6, 14], [0, 7, 15], [1, 7, 16]]) == 716
    assert candidate(n = 8,queries = [[0, 0, 20], [1, 0, 21], [0, 1, 22], [1, 1, 23], [0, 2, 24], [1, 2, 25], [0, 3, 26], [1, 3, 27], [0, 4, 28], [1, 4, 29], [0, 5, 30], [1, 5, 31], [0, 6, 32], [1, 6, 33], [0, 7, 34], [1, 7, 35]]) == 1932
    assert candidate(n = 6,queries = [[0, 1, 100], [1, 3, 200], [0, 2, 50], [1, 1, 150], [0, 4, 250], [1, 0, 300]]) == 5100
    assert candidate(n = 4,queries = [[1, 0, 10], [0, 0, 20], [1, 1, 30], [0, 1, 40], [1, 2, 50], [0, 2, 60], [1, 3, 70], [0, 3, 80]]) == 940
    assert candidate(n = 4,queries = [[0, 1, 5], [1, 2, 8], [0, 3, 9], [1, 0, 4], [0, 2, 6], [1, 1, 7]]) == 97
    assert candidate(n = 3,queries = [[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4], [0, 1, 5], [1, 1, 6]]) == 41
    assert candidate(n = 3,queries = [[0, 0, 10], [1, 0, 20], [0, 1, 30], [1, 1, 40], [0, 2, 50], [1, 2, 60]]) == 410
    assert candidate(n = 5,queries = [[0, 0, 10], [1, 1, 5], [0, 2, 3], [1, 3, 7], [0, 4, 2], [1, 0, 8]]) == 120
    assert candidate(n = 8,queries = [[0, 7, 5], [1, 6, 4], [0, 5, 3], [1, 4, 2], [0, 3, 1], [1, 2, 6], [0, 1, 7], [1, 0, 8], [0, 6, 9], [1, 7, 10]]) == 335
    assert candidate(n = 7,queries = [[0, 6, 11], [1, 5, 12], [0, 4, 13], [1, 3, 14], [0, 2, 15], [1, 1, 16], [0, 0, 17], [1, 6, 18], [0, 5, 19], [1, 4, 20]]) == 740
    assert candidate(n = 10,queries = [[0, 9, 1], [1, 8, 2], [0, 7, 3], [1, 6, 4], [0, 5, 5], [1, 4, 6], [0, 3, 7], [1, 2, 8], [0, 1, 9], [1, 0, 10], [0, 8, 11], [1, 7, 12], [0, 6, 13], [1, 5, 14], [0, 4, 15], [1, 3, 16], [0, 2, 17], [1, 1, 18], [0, 0, 19], [1, 9, 20]]) == 1385
    assert candidate(n = 9,queries = [[0, 0, 2], [1, 0, 3], [0, 1, 4], [1, 1, 5], [0, 2, 6], [1, 2, 7], [0, 3, 8], [1, 3, 9], [0, 4, 10], [1, 4, 11], [0, 5, 12], [1, 5, 13], [0, 6, 14], [1, 6, 15], [0, 7, 16], [1, 7, 17], [0, 8, 18], [1, 8, 19]]) == 1095
    assert candidate(n = 5,queries = [[0, 0, 5], [1, 1, 3], [0, 2, 8], [1, 3, 2], [0, 4, 1], [1, 0, 4]]) == 75
    assert candidate(n = 6,queries = [[0, 2, 100], [1, 3, 200], [0, 0, 300], [1, 1, 400], [0, 4, 500], [1, 5, 600], [0, 5, 700], [1, 0, 800]]) == 16600
    assert candidate(n = 4,queries = [[0, 0, 1], [0, 0, 2], [0, 0, 3], [1, 0, 4], [1, 0, 5], [1, 0, 6], [0, 1, 7], [1, 1, 8], [0, 2, 9], [1, 2, 10], [0, 3, 11], [1, 3, 12]]) == 158
    assert candidate(n = 4,queries = [[0, 0, 5], [1, 1, 6], [0, 2, 7], [1, 3, 8], [0, 1, 9]]) == 103
    assert candidate(n = 5000,queries = [[0, 0, 1], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 4, 5], [1, 0, 6], [0, 3, 7], [1, 2, 8], [0, 1, 9], [1, 4, 10]]) == 274905
    assert candidate(n = 6,queries = [[0, 0, 1], [1, 5, 2], [0, 4, 3], [1, 3, 4], [0, 2, 5], [1, 1, 6], [0, 1, 7], [1, 0, 8]]) == 166
    assert candidate(n = 3,queries = [[1, 0, 1], [0, 0, 2], [1, 1, 3], [0, 1, 4], [1, 2, 5], [0, 2, 6]]) == 41
    assert candidate(n = 4,queries = [[0, 0, 5], [1, 1, 10], [0, 2, 20], [1, 3, 30], [0, 1, 50], [1, 0, 60]]) == 545
    assert candidate(n = 3,queries = [[0, 0, 5], [0, 1, 5], [0, 2, 5], [1, 0, 5], [1, 1, 5], [1, 2, 5]]) == 45
    assert candidate(n = 7,queries = [[0, 6, 70], [1, 5, 60], [0, 4, 50], [1, 3, 40], [0, 2, 30], [1, 1, 20], [0, 0, 10], [1, 0, 0], [0, 1, 1], [1, 2, 2], [0, 3, 3], [1, 4, 4], [0, 5, 5], [1, 6, 6]]) == 465
    assert candidate(n = 5,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [1, 0, 6], [1, 1, 7], [1, 2, 8], [1, 3, 9], [1, 4, 10], [0, 0, 11], [0, 1, 12], [0, 2, 13], [0, 3, 14], [0, 4, 15], [1, 0, 16], [1, 1, 17], [1, 2, 18], [1, 3, 19], [1, 4, 20]]) == 450
    assert candidate(n = 10,queries = [[1, 0, 1], [1, 1, 2], [1, 2, 3], [1, 3, 4], [1, 4, 5], [1, 5, 6], [1, 6, 7], [1, 7, 8], [1, 8, 9], [1, 9, 10]]) == 550
    assert candidate(n = 1000,queries = [[0, 500, 1], [1, 500, 2], [0, 499, 3], [1, 499, 4], [0, 498, 5], [1, 498, 6], [0, 497, 7], [1, 497, 8], [0, 496, 9], [1, 496, 10]]) == 54905
    assert candidate(n = 5000,queries = [[0, 2500, 1], [1, 2500, 2], [0, 2499, 3], [1, 2499, 4], [0, 2498, 5], [1, 2498, 6], [0, 2497, 7], [1, 2497, 8], [0, 2496, 9], [1, 2496, 10]]) == 274905
    assert candidate(n = 1000,queries = [[0, 500, 5], [1, 250, 10], [0, 750, 20], [1, 0, 30], [0, 999, 50], [1, 500, 60]]) == 174845
    assert candidate(n = 3,queries = [[0, 0, 10], [1, 0, 20], [0, 1, 30], [1, 1, 40], [0, 2, 50], [1, 2, 60], [0, 0, 70], [1, 0, 80]]) == 590
    assert candidate(n = 5,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [1, 0, 6], [1, 1, 7], [1, 2, 8], [1, 3, 9], [1, 4, 10]]) == 200
    assert candidate(n = 4,queries = [[0, 0, 10], [1, 2, 5], [0, 3, 3], [1, 1, 7], [0, 2, 8], [1, 3, 2]]) == 79
    assert candidate(n = 100,queries = [[0, 50, 10], [1, 50, 20], [0, 25, 15], [1, 75, 25], [0, 75, 30], [1, 25, 35], [0, 0, 5], [1, 99, 50]]) == 18705
    assert candidate(n = 3,queries = [[0, 0, 1], [1, 2, 2], [0, 2, 3], [1, 0, 4], [0, 1, 5], [1, 1, 6], [0, 0, 7], [1, 2, 8]]) == 59
    assert candidate(n = 10,queries = [[0, 5, 9], [1, 4, 8], [0, 9, 7], [1, 3, 6], [0, 2, 5], [1, 1, 4], [0, 0, 3], [1, 8, 2], [0, 7, 1], [1, 6, 0]]) == 295
    assert candidate(n = 10,queries = [[0, 0, 10], [1, 0, 10], [0, 1, 20], [1, 1, 20], [0, 2, 30], [1, 2, 30], [0, 3, 40], [1, 3, 40], [0, 4, 50], [1, 4, 50], [0, 5, 60], [1, 5, 60], [0, 6, 70], [1, 6, 70], [0, 7, 80], [1, 7, 80], [0, 8, 90], [1, 8, 90], [0, 9, 100], [1, 9, 100]]) == 7150
    assert candidate(n = 5,queries = [[0, 0, 1], [0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [1, 0, 1], [1, 1, 1], [1, 2, 1], [1, 3, 1], [1, 4, 1]]) == 25
    assert candidate(n = 7,queries = [[0, 0, 1], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 4, 5], [1, 5, 6], [0, 6, 7], [1, 6, 8], [0, 5, 9], [1, 4, 10]]) == 290
    assert candidate(n = 6,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [1, 0, 6], [1, 1, 5], [1, 2, 4], [1, 3, 3], [1, 4, 2], [1, 5, 1]]) == 126
    assert candidate(n = 6,queries = [[0, 5, 50], [1, 4, 40], [0, 3, 30], [1, 2, 20], [0, 1, 10], [1, 0, 0], [0, 4, 400], [1, 5, 500], [0, 2, 200], [1, 3, 300]]) == 7180
    assert candidate(n = 5,queries = [[0, 0, 10], [1, 1, 20], [0, 2, 30], [1, 3, 40], [0, 4, 50]]) == 620
    assert candidate(n = 5,queries = [[1, 0, 1], [1, 1, 2], [1, 2, 3], [1, 3, 4], [1, 4, 5], [0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5]]) == 75
    assert candidate(n = 7,queries = [[0, 0, 1], [0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [0, 5, 1], [0, 6, 1], [1, 0, 1], [1, 1, 1], [1, 2, 1], [1, 3, 1], [1, 4, 1], [1, 5, 1], [1, 6, 1]]) == 49
    assert candidate(n = 10,queries = [[0, 9, 100], [1, 8, 90], [0, 7, 80], [1, 6, 70], [0, 5, 60], [1, 4, 50], [0, 3, 40], [1, 2, 30], [0, 1, 20], [1, 0, 10]]) == 3700
    assert candidate(n = 1000,queries = [[0, 500, 1], [1, 500, 2], [0, 499, 3], [1, 499, 4], [0, 501, 5], [1, 501, 6], [0, 0, 10], [1, 999, 20]]) == 50947
    assert candidate(n = 7,queries = [[0, 0, 1], [1, 0, 2], [0, 1, 3], [1, 1, 4], [0, 2, 5], [1, 2, 6], [0, 3, 7], [1, 3, 8], [0, 4, 9], [1, 4, 10], [0, 5, 11], [1, 5, 12], [0, 6, 13], [1, 6, 14]]) == 483
    assert candidate(n = 4,queries = [[0, 0, 5], [1, 1, 10], [0, 2, 15], [1, 3, 20], [0, 3, 25]]) == 235
    assert candidate(n = 10,queries = [[0, 0, 1], [0, 1, 2], [1, 0, 3], [1, 1, 4], [0, 2, 5], [1, 2, 6], [0, 3, 7], [1, 3, 8], [0, 4, 9], [1, 4, 10]]) == 456
    assert candidate(n = 6,queries = [[0, 0, 1], [1, 1, 1], [0, 2, 1], [1, 3, 1], [0, 4, 1], [1, 5, 1], [0, 5, 1], [1, 0, 1], [0, 1, 1], [1, 2, 1], [0, 3, 1], [1, 4, 1]]) == 36
    assert candidate(n = 10,queries = [[0, 0, 10], [1, 1, 20], [0, 2, 30], [1, 3, 40], [0, 4, 50], [1, 5, 60], [0, 6, 70], [1, 7, 80], [0, 8, 90], [1, 9, 100]]) == 4550
    assert candidate(n = 9,queries = [[0, 0, 1], [1, 8, 9], [0, 1, 2], [1, 7, 8], [0, 2, 3], [1, 6, 7], [0, 3, 4], [1, 5, 6], [0, 4, 5]]) == 305
    assert candidate(n = 7,queries = [[0, 0, 1], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 4, 5], [1, 5, 6], [0, 6, 7], [1, 0, 8], [0, 1, 9], [1, 2, 10], [0, 3, 11], [1, 4, 12], [0, 5, 13], [1, 6, 14], [0, 0, 15], [1, 1, 16], [0, 2, 17], [1, 3, 18], [0, 4, 19], [1, 5, 20], [0, 6, 21], [1, 0, 22]]) == 875
    assert candidate(n = 3,queries = [[0, 0, 1], [1, 0, 2], [0, 0, 3], [1, 0, 4], [0, 0, 5], [1, 0, 6], [0, 0, 7], [1, 0, 8]]) == 38
    assert candidate(n = 4,queries = [[0, 2, 5], [1, 1, 3], [0, 0, 2], [1, 2, 8], [0, 3, 1]]) == 50
    assert candidate(n = 5,queries = [[0, 0, 1], [0, 0, 2], [0, 0, 3], [0, 0, 4], [0, 0, 5], [1, 0, 1], [1, 0, 2], [1, 0, 3], [1, 0, 4], [1, 0, 5]]) == 45
    assert candidate(n = 6,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [1, 0, 10], [1, 1, 20], [1, 2, 30], [1, 3, 40], [1, 4, 50], [1, 5, 60]]) == 1260
    assert candidate(n = 10,queries = [[0, 0, 1], [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 6], [0, 6, 7], [0, 7, 8], [0, 8, 9], [0, 9, 10]]) == 550
    assert candidate(n = 3,queries = [[0, 0, 1], [1, 0, 2], [0, 1, 3], [1, 1, 4], [0, 2, 5], [1, 2, 6], [0, 0, 7], [1, 0, 8], [0, 1, 9], [1, 1, 10]]) == 77
    assert candidate(n = 3,queries = [[0, 0, 100], [0, 0, 200], [0, 0, 300], [1, 1, 100], [1, 1, 200], [1, 1, 300], [0, 1, 100], [0, 2, 200], [1, 0, 300], [1, 2, 400]]) == 2700
    assert candidate(n = 5000,queries = [[0, 2500, 5], [1, 1250, 10], [0, 3750, 20], [1, 0, 30], [0, 4999, 50], [1, 2500, 60]]) == 874845
    assert candidate(n = 4,queries = [[0, 0, 5], [1, 1, 2], [0, 2, 3], [1, 3, 4], [0, 3, 1], [1, 0, 6]]) == 54
    assert candidate(n = 500,queries = [[0, 0, 100], [1, 0, 200], [0, 100, 150], [1, 200, 250], [0, 300, 300], [1, 400, 400], [0, 1, 10], [1, 2, 20], [0, 3, 30], [1, 4, 40]]) == 745580


