def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(receiver = [4, 3, 2, 1, 0],k = 10) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [4, 3, 2, 1, 0],k = 10) == 24: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [4, 3, 2, 1, 0],k = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [4, 3, 2, 1, 0],k = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [3, 3, 3, 3],k = 10) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [3, 3, 3, 3],k = 10) == 33: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 2, 1, 0],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 2, 1, 0],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 1, 1, 2, 3],k = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 1, 1, 2, 3],k = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 2, 1, 3],k = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 2, 1, 3],k = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [2, 0, 1],k = 4) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [2, 0, 1],k = 4) == 6: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 2, 3, 4, 0],k = 2) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 2, 3, 4, 0],k = 2) == 9: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [3, 2, 1, 0],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [3, 2, 1, 0],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 2, 3, 4, 0],k = 10) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 2, 3, 4, 0],k = 10) == 24: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1000000000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1000000000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 2, 0, 3, 4, 5],k = 15) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 2, 0, 3, 4, 5],k = 15) == 80: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 5000000000) == 2500000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 5000000000) == 2500000009: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4],k = 1000000000) == 11500000019
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4],k = 1000000000) == 11500000019: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 100000) == 1900019
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 100000) == 1900019: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 0, 0, 0, 0],k = 1000000000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 0, 0, 0, 0],k = 1000000000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [2, 0, 1, 3, 4, 5, 3, 2],k = 100) == 505
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [2, 0, 1, 3, 4, 5, 3, 2],k = 100) == 505: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [5, 4, 3, 2, 1, 0, 9, 8, 7, 6],k = 875000000) == 6562500009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [5, 4, 3, 2, 1, 0, 9, 8, 7, 6],k = 875000000) == 6562500009: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0],k = 1000000) == 9500019
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0],k = 1000000) == 9500019: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 0, 3, 2, 5, 4],k = 999999999) == 4500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 0, 3, 2, 5, 4],k = 999999999) == 4500000000: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [2, 3, 4, 5, 0, 1],k = 123456789) == 370370372
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [2, 3, 4, 5, 0, 1],k = 123456789) == 370370372: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0],k = 1000000000) == 9500000019
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0],k = 1000000000) == 9500000019: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10000000000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10000000000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 5) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 5) == 54: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 1, 0, 1, 0, 1],k = 5000000000) == 5000000005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 1, 0, 1, 0, 1],k = 5000000000) == 5000000005: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8],k = 200) == 1709
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8],k = 200) == 1709: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 20) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 20) == 99: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5],k = 1000) == 5011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5],k = 1000) == 5011: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [3, 0, 1, 2, 7, 8, 9, 10, 5, 6, 11, 4],k = 500) == 4011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [3, 0, 1, 2, 7, 8, 9, 10, 5, 6, 11, 4],k = 500) == 4011: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 0],k = 8765432109) == 43827160558
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 0],k = 8765432109) == 43827160558: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [5, 6, 0, 1, 3, 2, 4],k = 100) == 356
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [5, 6, 0, 1, 3, 2, 4],k = 100) == 356: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1000000) == 9500019
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1000000) == 9500019: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4],k = 100000) == 200016
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4],k = 100000) == 200016: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 0, 2, 4, 3, 5, 6, 7, 8, 9],k = 50) == 459
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 0, 2, 4, 3, 5, 6, 7, 8, 9],k = 50) == 459: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 10],k = 1000000000) == 12500000015
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 10],k = 1000000000) == 12500000015: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1000000000) == 3000000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1000000000) == 3000000009: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [2, 3, 4, 5, 6, 0, 1, 7, 8, 9],k = 20) == 189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [2, 3, 4, 5, 6, 0, 1, 7, 8, 9],k = 20) == 189: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2],k = 1000000) == 1000020
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2],k = 1000000) == 1000020: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 0, 0, 0, 0, 0],k = 999999999) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 0, 0, 0, 0, 0],k = 999999999) == 5: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0],k = 10000000000) == 80000000008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0],k = 10000000000) == 80000000008: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1000) == 4509
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1000) == 4509: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [4, 3, 2, 1, 0, 4, 3, 2, 1, 0],k = 10000000000) == 20000000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [4, 3, 2, 1, 0, 4, 3, 2, 1, 0],k = 10000000000) == 20000000009: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [2, 3, 4, 5, 6, 7, 8, 9, 0, 1],k = 10000000) == 50000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [2, 3, 4, 5, 6, 7, 8, 9, 0, 1],k = 10000000) == 50000009: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 5) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 5) == 27: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 1000000000) == 500000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 1000000000) == 500000009: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [2, 3, 4, 5, 6, 1, 0],k = 10000000000) == 30000000006
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [2, 3, 4, 5, 6, 1, 0],k = 10000000000) == 30000000006: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [5, 4, 3, 2, 1, 0, 6, 7, 8, 9],k = 10000000000) == 90000000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [5, 4, 3, 2, 1, 0, 6, 7, 8, 9],k = 10000000000) == 90000000009: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [3, 1, 2, 0, 5, 4, 7, 6, 9, 8],k = 1000) == 8509
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [3, 1, 2, 0, 5, 4, 7, 6, 9, 8],k = 1000) == 8509: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [2, 3, 4, 5, 6, 7, 8, 9, 0, 1],k = 1500000000) == 7500000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [2, 3, 4, 5, 6, 7, 8, 9, 0, 1],k = 1500000000) == 7500000009: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8],k = 50) == 434
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8],k = 50) == 434: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18],k = 100000000) == 1850000019
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18],k = 100000000) == 1850000019: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [5, 3, 0, 1, 4, 2],k = 500000000) == 2000000004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [5, 3, 0, 1, 4, 2],k = 500000000) == 2000000004: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 999999999) == 4000000005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 999999999) == 4000000005: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0],k = 100000) == 800008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0],k = 100000) == 800008: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 50) == 260
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 50) == 260: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [3, 2, 1, 0, 7, 6, 5, 4],k = 10000000000) == 55000000007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [3, 2, 1, 0, 7, 6, 5, 4],k = 10000000000) == 55000000007: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 0, 1, 2, 3, 4],k = 1000000000) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 0, 1, 2, 3, 4],k = 1000000000) == 15: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0],k = 1250000000) == 10000000008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0],k = 1250000000) == 10000000008: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9],k = 625000000) == 5625000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9],k = 625000000) == 5625000009: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [3, 0, 1, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18],k = 1000000000) == 18500000019
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [3, 0, 1, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18],k = 1000000000) == 18500000019: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [5, 3, 0, 2, 1, 4],k = 10000000000) == 25000000005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [5, 3, 0, 2, 1, 4],k = 10000000000) == 25000000005: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 14, 13, 12, 11, 10, 19, 18, 17, 16, 15],k = 900000000) == 15300000019
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 14, 13, 12, 11, 10, 19, 18, 17, 16, 15],k = 900000000) == 15300000019: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 500000000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 500000000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [2, 4, 6, 8, 10, 12, 14, 16, 18, 0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 9999999999) == 190000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [2, 4, 6, 8, 10, 12, 14, 16, 18, 0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 9999999999) == 190000000000: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18],k = 1000) == 13022
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18],k = 1000) == 13022: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [2, 3, 4, 5, 6, 7, 8, 9, 0, 1],k = 25) == 134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [2, 3, 4, 5, 6, 7, 8, 9, 0, 1],k = 25) == 134: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49],k = 10000000000) == 490000000049
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49],k = 10000000000) == 490000000049: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],k = 10000000000) == 45000000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],k = 10000000000) == 45000000009: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 500000000) == 9500000019
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 500000000) == 9500000019: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 1000000000) == 19000000019
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 1000000000) == 19000000019: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1000000000) == 9500000019
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1000000000) == 9500000019: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [7, 6, 5, 4, 3, 2, 1, 0, 8, 9, 10, 11, 12, 13, 14, 15],k = 9876543210) == 148148148165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [7, 6, 5, 4, 3, 2, 1, 0, 8, 9, 10, 11, 12, 13, 14, 15],k = 9876543210) == 148148148165: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [5, 4, 3, 2, 1, 0],k = 15) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [5, 4, 3, 2, 1, 0],k = 15) == 40: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 500000000) == 2250000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 500000000) == 2250000009: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 0, 0, 0, 0],k = 100000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 0, 0, 0, 0],k = 100000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [5, 6, 0, 1, 4, 3, 2],k = 15) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [5, 6, 0, 1, 4, 3, 2],k = 15) == 64: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5000) == 25009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5000) == 25009: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1000000000) == 5000000010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1000000000) == 5000000010: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 11, 10, 15, 14, 13, 12],k = 100000000) == 1350000015
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 11, 10, 15, 14, 13, 12],k = 100000000) == 1350000015: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 50) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 50) == 34: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 109: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4],k = 750000000) == 4875000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4],k = 750000000) == 4875000009: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [5, 4, 3, 2, 1, 0],k = 500000000) == 1250000005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [5, 4, 3, 2, 1, 0],k = 500000000) == 1250000005: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0],k = 5000000000) == 10000000008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0],k = 5000000000) == 10000000008: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [2, 0, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 0],k = 1000000000) == 17500000018
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [2, 0, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 0],k = 1000000000) == 17500000018: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5000000000) == 5000000019
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5000000000) == 5000000019: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [2, 0, 3, 1, 6, 4, 5, 7, 8, 9],k = 100000000000) == 900000000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [2, 0, 3, 1, 6, 4, 5, 7, 8, 9],k = 100000000000) == 900000000009: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 9999999999) == 45000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 9999999999) == 45000000000: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [5, 4, 3, 2, 1, 0],k = 100) == 255
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [5, 4, 3, 2, 1, 0],k = 100) == 255: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 1000000000) == 9000000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 1000000000) == 9000000009: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0],k = 50) == 408
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0],k = 50) == 408: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [2, 1, 0, 3, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],k = 100000000) == 1450000015
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [2, 1, 0, 3, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],k = 100000000) == 1450000015: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [5, 4, 3, 2, 1, 0],k = 10000000000) == 25000000005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [5, 4, 3, 2, 1, 0],k = 10000000000) == 25000000005: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 3, 6, 9, 2, 5, 8, 1, 4, 7],k = 50) == 259
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 3, 6, 9, 2, 5, 8, 1, 4, 7],k = 50) == 259: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10],k = 999999999) == 14500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10],k = 999999999) == 14500000000: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [6, 5, 4, 3, 2, 1, 0, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 100000) == 1500015
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [6, 5, 4, 3, 2, 1, 0, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 100000) == 1500015: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1],k = 1000) == 3009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1],k = 1000) == 3009: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [5, 4, 3, 2, 1, 0],k = 1000000000) == 2500000005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [5, 4, 3, 2, 1, 0],k = 1000000000) == 2500000005: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1000000000) == 4500000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1000000000) == 4500000009: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 2, 3, 4, 5, 6, 7, 8, 9, 1],k = 100) == 512
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 2, 3, 4, 5, 6, 7, 8, 9, 1],k = 100) == 512: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [3, 0, 1, 2, 5, 4],k = 100) == 455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [3, 0, 1, 2, 5, 4],k = 100) == 455: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [3, 2, 1, 0, 7, 6, 5, 4, 9, 8],k = 50) == 434
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [3, 2, 1, 0, 7, 6, 5, 4, 9, 8],k = 50) == 434: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 2, 0, 4, 5, 3, 6, 7, 8, 9],k = 50) == 459
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 2, 0, 4, 5, 3, 6, 7, 8, 9],k = 50) == 459: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10000000000) == 10000000019
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10000000000) == 10000000019: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 1000000000) == 1000000009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 1000000000) == 1000000009: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 999999999) == 500000008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 999999999) == 500000008: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4],k = 9999999999) == 25000000010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4],k = 9999999999) == 25000000010: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1000000000) == 18500000019
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1000000000) == 18500000019: {e}')
    
    total += 1
    try:
        result = candidate(receiver = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8],k = 100000) == 850009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(receiver = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8],k = 100000) == 850009: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(receiver = [4, 3, 2, 1, 0],k = 10) == 24
    assert candidate(receiver = [4, 3, 2, 1, 0],k = 5) == 12
    assert candidate(receiver = [3, 3, 3, 3],k = 10) == 33
    assert candidate(receiver = [0, 2, 1, 0],k = 5) == 9
    assert candidate(receiver = [1, 1, 1, 2, 3],k = 3) == 10
    assert candidate(receiver = [0, 2, 1, 3],k = 2) == 9
    assert candidate(receiver = [2, 0, 1],k = 4) == 6
    assert candidate(receiver = [1, 2, 3, 4, 0],k = 2) == 9
    assert candidate(receiver = [3, 2, 1, 0],k = 5) == 9
    assert candidate(receiver = [1, 2, 3, 4, 0],k = 10) == 24
    assert candidate(receiver = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1000000000) == 9
    assert candidate(receiver = [1, 2, 0, 3, 4, 5],k = 15) == 80
    assert candidate(receiver = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 5000000000) == 2500000009
    assert candidate(receiver = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4],k = 1000000000) == 11500000019
    assert candidate(receiver = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 100000) == 1900019
    assert candidate(receiver = [0, 0, 0, 0, 0],k = 1000000000) == 4
    assert candidate(receiver = [2, 0, 1, 3, 4, 5, 3, 2],k = 100) == 505
    assert candidate(receiver = [5, 4, 3, 2, 1, 0, 9, 8, 7, 6],k = 875000000) == 6562500009
    assert candidate(receiver = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0],k = 1000000) == 9500019
    assert candidate(receiver = [1, 0, 3, 2, 5, 4],k = 999999999) == 4500000000
    assert candidate(receiver = [2, 3, 4, 5, 0, 1],k = 123456789) == 370370372
    assert candidate(receiver = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0],k = 1000000000) == 9500000019
    assert candidate(receiver = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 10000000000) == 9
    assert candidate(receiver = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 5) == 54
    assert candidate(receiver = [0, 1, 0, 1, 0, 1],k = 5000000000) == 5000000005
    assert candidate(receiver = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8],k = 200) == 1709
    assert candidate(receiver = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 20) == 99
    assert candidate(receiver = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5],k = 1000) == 5011
    assert candidate(receiver = [3, 0, 1, 2, 7, 8, 9, 10, 5, 6, 11, 4],k = 500) == 4011
    assert candidate(receiver = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 0],k = 8765432109) == 43827160558
    assert candidate(receiver = [5, 6, 0, 1, 3, 2, 4],k = 100) == 356
    assert candidate(receiver = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1000000) == 9500019
    assert candidate(receiver = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4],k = 100000) == 200016
    assert candidate(receiver = [1, 0, 2, 4, 3, 5, 6, 7, 8, 9],k = 50) == 459
    assert candidate(receiver = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 10],k = 1000000000) == 12500000015
    assert candidate(receiver = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1000000000) == 3000000009
    assert candidate(receiver = [2, 3, 4, 5, 6, 0, 1, 7, 8, 9],k = 20) == 189
    assert candidate(receiver = [1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2],k = 1000000) == 1000020
    assert candidate(receiver = [0, 0, 0, 0, 0, 0],k = 999999999) == 5
    assert candidate(receiver = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0],k = 10000000000) == 80000000008
    assert candidate(receiver = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1000) == 4509
    assert candidate(receiver = [4, 3, 2, 1, 0, 4, 3, 2, 1, 0],k = 10000000000) == 20000000009
    assert candidate(receiver = [2, 3, 4, 5, 6, 7, 8, 9, 0, 1],k = 10000000) == 50000009
    assert candidate(receiver = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 5) == 27
    assert candidate(receiver = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 1000000000) == 500000009
    assert candidate(receiver = [2, 3, 4, 5, 6, 1, 0],k = 10000000000) == 30000000006
    assert candidate(receiver = [5, 4, 3, 2, 1, 0, 6, 7, 8, 9],k = 10000000000) == 90000000009
    assert candidate(receiver = [3, 1, 2, 0, 5, 4, 7, 6, 9, 8],k = 1000) == 8509
    assert candidate(receiver = [2, 3, 4, 5, 6, 7, 8, 9, 0, 1],k = 1500000000) == 7500000009
    assert candidate(receiver = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8],k = 50) == 434
    assert candidate(receiver = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18],k = 100000000) == 1850000019
    assert candidate(receiver = [5, 3, 0, 1, 4, 2],k = 500000000) == 2000000004
    assert candidate(receiver = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],k = 999999999) == 4000000005
    assert candidate(receiver = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0],k = 100000) == 800008
    assert candidate(receiver = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 50) == 260
    assert candidate(receiver = [3, 2, 1, 0, 7, 6, 5, 4],k = 10000000000) == 55000000007
    assert candidate(receiver = [0, 0, 1, 2, 3, 4],k = 1000000000) == 15
    assert candidate(receiver = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0],k = 1250000000) == 10000000008
    assert candidate(receiver = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9],k = 625000000) == 5625000009
    assert candidate(receiver = [3, 0, 1, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18],k = 1000000000) == 18500000019
    assert candidate(receiver = [5, 3, 0, 2, 1, 4],k = 10000000000) == 25000000005
    assert candidate(receiver = [4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 14, 13, 12, 11, 10, 19, 18, 17, 16, 15],k = 900000000) == 15300000019
    assert candidate(receiver = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 500000000) == 9
    assert candidate(receiver = [2, 4, 6, 8, 10, 12, 14, 16, 18, 0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 9999999999) == 190000000000
    assert candidate(receiver = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18],k = 1000) == 13022
    assert candidate(receiver = [2, 3, 4, 5, 6, 7, 8, 9, 0, 1],k = 25) == 134
    assert candidate(receiver = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49],k = 10000000000) == 490000000049
    assert candidate(receiver = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],k = 10000000000) == 45000000009
    assert candidate(receiver = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 500000000) == 9500000019
    assert candidate(receiver = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],k = 1000000000) == 19000000019
    assert candidate(receiver = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1000000000) == 9500000019
    assert candidate(receiver = [7, 6, 5, 4, 3, 2, 1, 0, 8, 9, 10, 11, 12, 13, 14, 15],k = 9876543210) == 148148148165
    assert candidate(receiver = [5, 4, 3, 2, 1, 0],k = 15) == 40
    assert candidate(receiver = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 500000000) == 2250000009
    assert candidate(receiver = [0, 0, 0, 0, 0],k = 100000) == 4
    assert candidate(receiver = [5, 6, 0, 1, 4, 3, 2],k = 15) == 64
    assert candidate(receiver = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5000) == 25009
    assert candidate(receiver = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1000000000) == 5000000010
    assert candidate(receiver = [7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 11, 10, 15, 14, 13, 12],k = 100000000) == 1350000015
    assert candidate(receiver = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 50) == 34
    assert candidate(receiver = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 109
    assert candidate(receiver = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4],k = 750000000) == 4875000009
    assert candidate(receiver = [5, 4, 3, 2, 1, 0],k = 500000000) == 1250000005
    assert candidate(receiver = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0],k = 5000000000) == 10000000008
    assert candidate(receiver = [2, 0, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 0],k = 1000000000) == 17500000018
    assert candidate(receiver = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 5000000000) == 5000000019
    assert candidate(receiver = [2, 0, 3, 1, 6, 4, 5, 7, 8, 9],k = 100000000000) == 900000000009
    assert candidate(receiver = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 9999999999) == 45000000000
    assert candidate(receiver = [5, 4, 3, 2, 1, 0],k = 100) == 255
    assert candidate(receiver = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 1000000000) == 9000000009
    assert candidate(receiver = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0],k = 50) == 408
    assert candidate(receiver = [2, 1, 0, 3, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],k = 100000000) == 1450000015
    assert candidate(receiver = [5, 4, 3, 2, 1, 0],k = 10000000000) == 25000000005
    assert candidate(receiver = [0, 3, 6, 9, 2, 5, 8, 1, 4, 7],k = 50) == 259
    assert candidate(receiver = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10],k = 999999999) == 14500000000
    assert candidate(receiver = [6, 5, 4, 3, 2, 1, 0, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 100000) == 1500015
    assert candidate(receiver = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1],k = 1000) == 3009
    assert candidate(receiver = [5, 4, 3, 2, 1, 0],k = 1000000000) == 2500000005
    assert candidate(receiver = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1000000000) == 4500000009
    assert candidate(receiver = [0, 2, 3, 4, 5, 6, 7, 8, 9, 1],k = 100) == 512
    assert candidate(receiver = [3, 0, 1, 2, 5, 4],k = 100) == 455
    assert candidate(receiver = [3, 2, 1, 0, 7, 6, 5, 4, 9, 8],k = 50) == 434
    assert candidate(receiver = [1, 2, 0, 4, 5, 3, 6, 7, 8, 9],k = 50) == 459
    assert candidate(receiver = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 10000000000) == 10000000019
    assert candidate(receiver = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],k = 1000000000) == 1000000009
    assert candidate(receiver = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],k = 999999999) == 500000008
    assert candidate(receiver = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4],k = 9999999999) == 25000000010
    assert candidate(receiver = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],k = 1000000000) == 18500000019
    assert candidate(receiver = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8],k = 100000) == 850009


