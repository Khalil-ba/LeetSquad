def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(candiesCount = [7, 4, 5, 3, 8],queries = [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]) == [True, False, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [7, 4, 5, 3, 8],queries = [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]) == [True, False, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [5, 2, 6, 4, 1],queries = [[3, 1, 2], [4, 10, 3], [3, 10, 100], [4, 100, 30], [1, 3, 1]]) == [False, True, True, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [5, 2, 6, 4, 1],queries = [[3, 1, 2], [4, 10, 3], [3, 10, 100], [4, 100, 30], [1, 3, 1]]) == [False, True, True, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 0, 1], [1, 1, 2], [2, 3, 3], [3, 6, 4], [4, 10, 5], [5, 15, 6], [6, 21, 7], [7, 28, 8], [8, 36, 9], [9, 45, 10]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 0, 1], [1, 1, 2], [2, 3, 3], [3, 6, 4], [4, 10, 5], [5, 15, 6], [6, 21, 7], [7, 28, 8], [8, 36, 9], [9, 45, 10]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1000000, 500000, 250000, 125000, 62500],queries = [[0, 999999, 1000000], [1, 1499999, 500000], [2, 1999999, 250000], [3, 2499999, 125000], [4, 2999999, 62500]]) == [True, True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1000000, 500000, 250000, 125000, 62500],queries = [[0, 999999, 1000000], [1, 1499999, 500000], [2, 1999999, 250000], [3, 2499999, 125000], [4, 2999999, 62500]]) == [True, True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [10, 20, 30, 40, 50],queries = [[0, 0, 10], [1, 1, 20], [2, 2, 30], [3, 3, 40], [4, 4, 50], [0, 5, 5], [1, 10, 10], [2, 15, 15], [3, 20, 20], [4, 25, 25]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [10, 20, 30, 40, 50],queries = [[0, 0, 10], [1, 1, 20], [2, 2, 30], [3, 3, 40], [4, 4, 50], [0, 5, 5], [1, 10, 10], [2, 15, 15], [3, 20, 20], [4, 25, 25]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],queries = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1]]) == [True, False, False, False, False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],queries = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1]]) == [True, False, False, False, False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 1, 1], [1, 3, 2], [2, 6, 3], [3, 10, 4], [4, 15, 5], [5, 21, 6], [6, 28, 7], [7, 36, 8], [8, 45, 9], [9, 55, 10]]) == [False, False, False, False, False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 1, 1], [1, 3, 2], [2, 6, 3], [3, 10, 4], [4, 15, 5], [5, 21, 6], [6, 28, 7], [7, 36, 8], [8, 45, 9], [9, 55, 10]]) == [False, False, False, False, False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [999999, 999999, 999999, 999999],queries = [[0, 100000, 999999], [1, 200000, 999999], [2, 300000, 999999], [3, 400000, 999999], [0, 300000, 333333], [1, 400000, 333333], [2, 500000, 333333], [3, 600000, 333333]]) == [True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [999999, 999999, 999999, 999999],queries = [[0, 100000, 999999], [1, 200000, 999999], [2, 300000, 999999], [3, 400000, 999999], [0, 300000, 333333], [1, 400000, 333333], [2, 500000, 333333], [3, 600000, 333333]]) == [True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 0, 10], [1, 10, 20], [2, 30, 30], [3, 60, 40], [4, 100, 50], [5, 150, 60], [6, 210, 70], [7, 280, 80], [8, 360, 90], [9, 450, 100]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 0, 10], [1, 10, 20], [2, 30, 30], [3, 60, 40], [4, 100, 50], [5, 150, 60], [6, 210, 70], [7, 280, 80], [8, 360, 90], [9, 450, 100]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [100000, 200000, 300000, 400000, 500000],queries = [[0, 50000, 1000], [1, 100000, 2000], [2, 150000, 3000], [3, 200000, 4000], [4, 250000, 5000]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [100000, 200000, 300000, 400000, 500000],queries = [[0, 50000, 1000], [1, 100000, 2000], [2, 150000, 3000], [3, 200000, 4000], [4, 250000, 5000]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 0, 1], [1, 1, 2], [2, 2, 3], [3, 3, 4], [4, 4, 5], [5, 5, 6], [6, 6, 7], [7, 7, 8], [8, 8, 9], [9, 9, 10]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 0, 1], [1, 1, 2], [2, 2, 3], [3, 3, 4], [4, 4, 5], [5, 5, 6], [6, 6, 7], [7, 7, 8], [8, 8, 9], [9, 9, 10]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [5, 4, 3, 2, 1],queries = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [0, 4, 10], [1, 3, 10], [2, 2, 10], [3, 1, 10], [4, 0, 10]]) == [True, False, False, False, False, True, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [5, 4, 3, 2, 1],queries = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [0, 4, 10], [1, 3, 10], [2, 2, 10], [3, 1, 10], [4, 0, 10]]) == [True, False, False, False, False, True, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [10, 20, 30, 40, 50],queries = [[4, 49, 50], [3, 29, 40], [2, 19, 30], [1, 9, 20], [0, 9, 10]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [10, 20, 30, 40, 50],queries = [[4, 49, 50], [3, 29, 40], [2, 19, 30], [1, 9, 20], [0, 9, 10]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 5, 5], [1, 15, 15], [2, 30, 25], [3, 45, 35], [4, 60, 45], [5, 75, 55], [6, 90, 65], [7, 105, 75], [8, 120, 85], [9, 135, 95]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 5, 5], [1, 15, 15], [2, 30, 25], [3, 45, 35], [4, 60, 45], [5, 75, 55], [6, 90, 65], [7, 105, 75], [8, 120, 85], [9, 135, 95]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [100, 200, 300, 400, 500],queries = [[0, 99, 100], [1, 199, 200], [2, 299, 300], [3, 399, 400], [4, 499, 500], [0, 1, 50], [1, 1, 100], [2, 1, 150], [3, 1, 200], [4, 1, 250]]) == [True, True, True, True, True, True, True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [100, 200, 300, 400, 500],queries = [[0, 99, 100], [1, 199, 200], [2, 299, 300], [3, 399, 400], [4, 499, 500], [0, 1, 50], [1, 1, 100], [2, 1, 150], [3, 1, 200], [4, 1, 250]]) == [True, True, True, True, True, True, True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [100, 200, 300, 400, 500],queries = [[0, 99, 100], [1, 199, 200], [2, 299, 300], [3, 399, 400], [4, 499, 500]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [100, 200, 300, 400, 500],queries = [[0, 99, 100], [1, 199, 200], [2, 299, 300], [3, 399, 400], [4, 499, 500]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [100000000, 200000000, 300000000, 400000000, 500000000],queries = [[0, 100000000, 150000000], [4, 900000000, 1000000000], [2, 500000000, 350000000]]) == [False, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [100000000, 200000000, 300000000, 400000000, 500000000],queries = [[0, 100000000, 150000000], [4, 900000000, 1000000000], [2, 500000000, 350000000]]) == [False, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1000000, 500000, 250000, 125000, 62500, 31250],queries = [[0, 500000, 100000], [5, 500000, 100000], [2, 750000, 50000], [4, 875000, 31250]]) == [True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1000000, 500000, 250000, 125000, 62500, 31250],queries = [[0, 500000, 100000], [5, 500000, 100000], [2, 750000, 50000], [4, 875000, 31250]]) == [True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],queries = [[0, 1000000000, 1000000000], [4, 4000000000, 1000000000], [2, 2500000000, 500000000]]) == [False, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],queries = [[0, 1000000000, 1000000000], [4, 4000000000, 1000000000], [2, 2500000000, 500000000]]) == [False, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],queries = [[0, 10000, 1000], [1, 20000, 2000], [2, 30000, 3000], [3, 40000, 4000], [4, 50000, 5000], [5, 60000, 6000], [6, 70000, 7000], [7, 80000, 8000], [8, 90000, 9000], [9, 100000, 10000]]) == [False, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],queries = [[0, 10000, 1000], [1, 20000, 2000], [2, 30000, 3000], [3, 40000, 4000], [4, 50000, 5000], [5, 60000, 6000], [6, 70000, 7000], [7, 80000, 8000], [8, 90000, 9000], [9, 100000, 10000]]) == [False, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 0, 10], [1, 1, 10], [2, 2, 10], [3, 3, 10], [4, 4, 10], [5, 5, 10], [6, 6, 10], [7, 7, 10], [8, 8, 10], [9, 9, 10]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 0, 10], [1, 1, 10], [2, 2, 10], [3, 3, 10], [4, 4, 10], [5, 5, 10], [6, 6, 10], [7, 7, 10], [8, 8, 10], [9, 9, 10]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000],queries = [[0, 499999, 500000], [1, 999999, 500000], [2, 1499999, 500000], [3, 1999999, 500000], [4, 2499999, 500000], [5, 2999999, 500000], [6, 3499999, 500000], [7, 3999999, 500000], [8, 4499999, 500000], [9, 4999999, 500000]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000],queries = [[0, 499999, 500000], [1, 999999, 500000], [2, 1499999, 500000], [3, 1999999, 500000], [4, 2499999, 500000], [5, 2999999, 500000], [6, 3499999, 500000], [7, 3999999, 500000], [8, 4499999, 500000], [9, 4999999, 500000]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1000000, 999999, 1000000, 999999, 1000000],queries = [[0, 1000000, 500000], [1, 1999998, 999999], [2, 2999999, 1000000], [3, 3999997, 1000000], [4, 4999999, 1000000]]) == [False, True, False, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1000000, 999999, 1000000, 999999, 1000000],queries = [[0, 1000000, 500000], [1, 1999998, 999999], [2, 2999999, 1000000], [3, 3999997, 1000000], [4, 4999999, 1000000]]) == [False, True, False, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [100000000, 200000000, 150000000, 300000000, 250000000],queries = [[0, 50000000, 50000000], [1, 100000000, 100000000], [2, 150000000, 150000000], [3, 200000000, 200000000], [4, 250000000, 250000000]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [100000000, 200000000, 150000000, 300000000, 250000000],queries = [[0, 50000000, 50000000], [1, 100000000, 100000000], [2, 150000000, 150000000], [3, 200000000, 200000000], [4, 250000000, 250000000]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000],queries = [[0, 0, 100000], [1, 100000, 200000], [2, 300000, 300000], [3, 600000, 400000], [4, 1000000, 500000], [5, 1500000, 600000], [6, 2100000, 700000], [7, 2800000, 800000], [8, 3600000, 900000], [9, 4500000, 1000000]]) == [True, True, False, False, False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000],queries = [[0, 0, 100000], [1, 100000, 200000], [2, 300000, 300000], [3, 600000, 400000], [4, 1000000, 500000], [5, 1500000, 600000], [6, 2100000, 700000], [7, 2800000, 800000], [8, 3600000, 900000], [9, 4500000, 1000000]]) == [True, True, False, False, False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],queries = [[0, 0, 1], [1, 1, 10], [2, 11, 100], [3, 111, 1000], [4, 1111, 10000], [5, 11111, 100000], [6, 111111, 1000000], [7, 1111111, 10000000], [8, 11111111, 100000000], [9, 111111111, 1000000000]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],queries = [[0, 0, 1], [1, 1, 10], [2, 11, 100], [3, 111, 1000], [4, 1111, 10000], [5, 11111, 100000], [6, 111111, 1000000], [7, 1111111, 10000000], [8, 11111111, 100000000], [9, 111111111, 1000000000]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70], [7, 8, 80], [8, 9, 90], [9, 10, 100], [0, 99, 1000], [1, 199, 1000], [2, 299, 1000], [3, 399, 1000], [4, 499, 1000], [5, 599, 1000], [6, 699, 1000], [7, 799, 1000], [8, 899, 1000], [9, 999, 1000]]) == [True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70], [7, 8, 80], [8, 9, 90], [9, 10, 100], [0, 99, 1000], [1, 199, 1000], [2, 299, 1000], [3, 399, 1000], [4, 499, 1000], [5, 599, 1000], [6, 699, 1000], [7, 799, 1000], [8, 899, 1000], [9, 999, 1000]]) == [True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [10, 20, 30, 40, 50],queries = [[0, 5, 10], [1, 15, 10], [2, 25, 10], [3, 35, 10], [4, 45, 10], [0, 9, 9], [1, 19, 9], [2, 29, 9], [3, 39, 9], [4, 49, 9], [0, 1, 1], [1, 11, 1], [2, 21, 1], [3, 31, 1], [4, 41, 1]]) == [True, True, True, True, True, True, True, True, True, True, True, True, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [10, 20, 30, 40, 50],queries = [[0, 5, 10], [1, 15, 10], [2, 25, 10], [3, 35, 10], [4, 45, 10], [0, 9, 9], [1, 19, 9], [2, 29, 9], [3, 39, 9], [4, 49, 9], [0, 1, 1], [1, 11, 1], [2, 21, 1], [3, 31, 1], [4, 41, 1]]) == [True, True, True, True, True, True, True, True, True, True, True, True, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [100000000, 200000000, 300000000, 400000000, 500000000],queries = [[0, 99999999, 100000000], [4, 1499999999, 150000000], [2, 299999999, 300000000]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [100000000, 200000000, 300000000, 400000000, 500000000],queries = [[0, 99999999, 100000000], [4, 1499999999, 150000000], [2, 299999999, 300000000]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1], [10, 10, 1], [11, 11, 1], [12, 12, 1], [13, 13, 1], [14, 14, 1], [15, 15, 1], [16, 16, 1], [17, 17, 1], [18, 18, 1], [19, 19, 1]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1], [10, 10, 1], [11, 11, 1], [12, 12, 1], [13, 13, 1], [14, 14, 1], [15, 15, 1], [16, 16, 1], [17, 17, 1], [18, 18, 1], [19, 19, 1]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1, 10, 100, 1000, 10000],queries = [[0, 0, 1], [1, 1, 10], [2, 2, 100], [3, 3, 1000], [4, 4, 10000], [0, 5, 5], [1, 10, 10], [2, 15, 15], [3, 20, 20], [4, 25, 25]]) == [True, True, True, True, True, False, True, True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1, 10, 100, 1000, 10000],queries = [[0, 0, 1], [1, 1, 10], [2, 2, 100], [3, 3, 1000], [4, 4, 10000], [0, 5, 5], [1, 10, 10], [2, 15, 15], [3, 20, 20], [4, 25, 25]]) == [True, True, True, True, True, False, True, True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1000000, 1000000, 1000000, 1000000, 1000000],queries = [[0, 100000, 200000], [1, 200000, 300000], [2, 300000, 400000], [3, 400000, 500000], [4, 500000, 600000]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1000000, 1000000, 1000000, 1000000, 1000000],queries = [[0, 100000, 200000], [1, 200000, 300000], [2, 300000, 400000], [3, 400000, 500000], [4, 500000, 600000]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1000, 1000, 1000, 1000, 1000],queries = [[0, 0, 1], [1, 500, 1000], [2, 1000, 1000], [3, 1500, 1000], [4, 2000, 1000]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1000, 1000, 1000, 1000, 1000],queries = [[0, 0, 1], [1, 500, 1000], [2, 1000, 1000], [3, 1500, 1000], [4, 2000, 1000]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],queries = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1]]) == [True, False, False, False, False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],queries = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1]]) == [True, False, False, False, False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 0, 1], [1, 1, 2], [2, 3, 3], [3, 6, 4], [4, 10, 5], [5, 15, 6], [6, 21, 7], [7, 28, 8], [8, 36, 9]]) == [True, False, False, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 0, 1], [1, 1, 2], [2, 3, 3], [3, 6, 4], [4, 10, 5], [5, 15, 6], [6, 21, 7], [7, 28, 8], [8, 36, 9]]) == [True, False, False, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 0, 1], [1, 1, 1], [2, 3, 1], [3, 6, 1], [4, 10, 1], [5, 15, 1], [6, 21, 1], [7, 28, 1], [8, 36, 1], [9, 45, 1]]) == [True, False, False, False, False, False, False, False, False, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 0, 1], [1, 1, 1], [2, 3, 1], [3, 6, 1], [4, 10, 1], [5, 15, 1], [6, 21, 1], [7, 28, 1], [8, 36, 1], [9, 45, 1]]) == [True, False, False, False, False, False, False, False, False, False]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],queries = [[0, 99, 100], [1, 199, 200], [2, 299, 300], [3, 399, 400], [4, 499, 500], [5, 599, 600], [6, 699, 700], [7, 799, 800], [8, 899, 900], [9, 999, 1000]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],queries = [[0, 99, 100], [1, 199, 200], [2, 299, 300], [3, 399, 400], [4, 499, 500], [5, 599, 600], [6, 699, 700], [7, 799, 800], [8, 899, 900], [9, 999, 1000]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 0, 10], [9, 494, 100], [5, 150, 60], [2, 30, 30], [8, 315, 90]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 0, 10], [9, 494, 100], [5, 150, 60], [2, 30, 30], [8, 315, 90]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 0, 1], [9, 44, 10], [3, 9, 4], [5, 14, 5], [8, 35, 9]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 0, 1], [9, 44, 10], [3, 9, 4], [5, 14, 5], [8, 35, 9]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1000000000, 1000000000, 1000000000],queries = [[0, 500000000, 500000000], [1, 1500000000, 500000000], [2, 2500000000, 500000000]]) == [True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1000000000, 1000000000, 1000000000],queries = [[0, 500000000, 500000000], [1, 1500000000, 500000000], [2, 2500000000, 500000000]]) == [True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [100, 200, 300, 400, 500],queries = [[0, 0, 100], [1, 100, 200], [2, 300, 300], [3, 600, 400], [4, 1000, 500]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [100, 200, 300, 400, 500],queries = [[0, 0, 100], [1, 100, 200], [2, 300, 300], [3, 600, 400], [4, 1000, 500]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],queries = [[0, 500000, 2000000], [1, 1000000, 2000000], [2, 1500000, 2000000], [3, 2000000, 2000000], [4, 2500000, 2000000], [5, 3000000, 2000000], [6, 3500000, 2000000], [7, 4000000, 2000000], [8, 4500000, 2000000], [9, 5000000, 2000000]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],queries = [[0, 500000, 2000000], [1, 1000000, 2000000], [2, 1500000, 2000000], [3, 2000000, 2000000], [4, 2500000, 2000000], [5, 3000000, 2000000], [6, 3500000, 2000000], [7, 4000000, 2000000], [8, 4500000, 2000000], [9, 5000000, 2000000]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],queries = [[0, 1, 50], [1, 51, 100], [2, 151, 150], [3, 301, 200], [4, 501, 250], [5, 751, 300], [6, 1051, 350], [7, 1401, 400], [8, 1801, 450], [9, 2251, 500]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],queries = [[0, 1, 50], [1, 51, 100], [2, 151, 150], [3, 301, 200], [4, 501, 250], [5, 751, 300], [6, 1051, 350], [7, 1401, 400], [8, 1801, 450], [9, 2251, 500]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [10, 20, 30, 40, 50],queries = [[0, 0, 5], [1, 4, 10], [2, 19, 15], [3, 34, 20], [4, 49, 25]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [10, 20, 30, 40, 50],queries = [[0, 0, 5], [1, 4, 10], [2, 19, 15], [3, 34, 20], [4, 49, 25]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1000000000, 999999999, 888888888, 777777777, 666666666],queries = [[0, 1000000000, 500000000], [4, 1000000000, 200000000], [2, 500000000, 100000000]]) == [False, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1000000000, 999999999, 888888888, 777777777, 666666666],queries = [[0, 1000000000, 500000000], [4, 1000000000, 200000000], [2, 500000000, 100000000]]) == [False, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1000000, 1000000, 1000000],queries = [[0, 100000, 1000], [1, 200000, 500000], [2, 500000, 1]]) == [True, True, False]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1000000, 1000000, 1000000],queries = [[0, 100000, 1000], [1, 200000, 500000], [2, 500000, 1]]) == [True, True, False]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [50, 50, 50, 50, 50],queries = [[0, 24, 50], [1, 49, 50], [2, 74, 50], [3, 99, 50], [4, 124, 50], [0, 25, 25], [1, 50, 25], [2, 75, 25], [3, 100, 25], [4, 125, 25]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [50, 50, 50, 50, 50],queries = [[0, 24, 50], [1, 49, 50], [2, 74, 50], [3, 99, 50], [4, 124, 50], [0, 25, 25], [1, 50, 25], [2, 75, 25], [3, 100, 25], [4, 125, 25]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],queries = [[0, 0, 100], [1, 199, 200], [2, 399, 300], [3, 599, 400], [4, 799, 500], [5, 999, 600], [6, 1199, 700], [7, 1399, 800], [8, 1599, 900], [9, 1799, 1000]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],queries = [[0, 0, 100], [1, 199, 200], [2, 399, 300], [3, 599, 400], [4, 799, 500], [5, 999, 600], [6, 1199, 700], [7, 1399, 800], [8, 1599, 900], [9, 1799, 1000]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [10, 20, 30, 40, 50],queries = [[0, 0, 10], [1, 10, 20], [2, 30, 30], [3, 60, 40], [4, 100, 50]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [10, 20, 30, 40, 50],queries = [[0, 0, 10], [1, 10, 20], [2, 30, 30], [3, 60, 40], [4, 100, 50]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1000000, 500000, 250000, 125000, 62500],queries = [[0, 999999, 1000000], [1, 1499999, 500000], [2, 374999, 250000], [3, 499999, 125000], [4, 593749, 62500]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1000000, 500000, 250000, 125000, 62500],queries = [[0, 999999, 1000000], [1, 1499999, 500000], [2, 374999, 250000], [3, 499999, 125000], [4, 593749, 62500]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [100, 200, 300, 400, 500],queries = [[0, 0, 1], [1, 100, 100], [2, 200, 150], [3, 300, 200], [4, 400, 250]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [100, 200, 300, 400, 500],queries = [[0, 0, 1], [1, 100, 100], [2, 200, 150], [3, 300, 200], [4, 400, 250]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1, 1, 1, 1, 1],queries = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1]]) == [True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1, 1, 1, 1, 1],queries = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1]]) == [True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],queries = [[0, 1000, 500], [1, 3000, 1000], [2, 5000, 1500], [3, 7000, 2000], [4, 9000, 2500], [5, 11000, 3000], [6, 13000, 3500], [7, 15000, 4000], [8, 17000, 4500], [9, 19000, 5000]]) == [False, False, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],queries = [[0, 1000, 500], [1, 3000, 1000], [2, 5000, 1500], [3, 7000, 2000], [4, 9000, 2500], [5, 11000, 3000], [6, 13000, 3500], [7, 15000, 4000], [8, 17000, 4500], [9, 19000, 5000]]) == [False, False, True, True, True, True, True, True, True, True]: {e}')
    
    total += 1
    try:
        result = candidate(candiesCount = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],queries = [[0, 0, 1], [1, 10, 10], [2, 110, 100], [3, 1110, 1000], [4, 11110, 10000], [5, 111110, 100000], [6, 1111110, 1000000], [7, 11111110, 10000000], [8, 111111110, 100000000], [9, 1111111110, 1000000000]]) == [True, True, True, True, True, True, True, True, True, True]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(candiesCount = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],queries = [[0, 0, 1], [1, 10, 10], [2, 110, 100], [3, 1110, 1000], [4, 11110, 10000], [5, 111110, 100000], [6, 1111110, 1000000], [7, 11111110, 10000000], [8, 111111110, 100000000], [9, 1111111110, 1000000000]]) == [True, True, True, True, True, True, True, True, True, True]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(candiesCount = [7, 4, 5, 3, 8],queries = [[0, 2, 2], [4, 2, 4], [2, 13, 1000000000]]) == [True, False, True]
    assert candidate(candiesCount = [5, 2, 6, 4, 1],queries = [[3, 1, 2], [4, 10, 3], [3, 10, 100], [4, 100, 30], [1, 3, 1]]) == [False, True, True, False, False]
    assert candidate(candiesCount = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 0, 1], [1, 1, 2], [2, 3, 3], [3, 6, 4], [4, 10, 5], [5, 15, 6], [6, 21, 7], [7, 28, 8], [8, 36, 9], [9, 45, 10]]) == [True, True, True, True, True, True, True, True, True, True]
    assert candidate(candiesCount = [1000000, 500000, 250000, 125000, 62500],queries = [[0, 999999, 1000000], [1, 1499999, 500000], [2, 1999999, 250000], [3, 2499999, 125000], [4, 2999999, 62500]]) == [True, True, False, False, False]
    assert candidate(candiesCount = [10, 20, 30, 40, 50],queries = [[0, 0, 10], [1, 1, 20], [2, 2, 30], [3, 3, 40], [4, 4, 50], [0, 5, 5], [1, 10, 10], [2, 15, 15], [3, 20, 20], [4, 25, 25]]) == [True, True, True, True, True, True, True, True, True, True]
    assert candidate(candiesCount = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],queries = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1]]) == [True, False, False, False, False, False, False, False, False, False]
    assert candidate(candiesCount = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 1, 1], [1, 3, 2], [2, 6, 3], [3, 10, 4], [4, 15, 5], [5, 21, 6], [6, 28, 7], [7, 36, 8], [8, 45, 9], [9, 55, 10]]) == [False, False, False, False, False, False, False, False, False, False]
    assert candidate(candiesCount = [999999, 999999, 999999, 999999],queries = [[0, 100000, 999999], [1, 200000, 999999], [2, 300000, 999999], [3, 400000, 999999], [0, 300000, 333333], [1, 400000, 333333], [2, 500000, 333333], [3, 600000, 333333]]) == [True, True, True, True, True, True, True, True]
    assert candidate(candiesCount = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 0, 10], [1, 10, 20], [2, 30, 30], [3, 60, 40], [4, 100, 50], [5, 150, 60], [6, 210, 70], [7, 280, 80], [8, 360, 90], [9, 450, 100]]) == [True, True, True, True, True, True, True, True, True, True]
    assert candidate(candiesCount = [100000, 200000, 300000, 400000, 500000],queries = [[0, 50000, 1000], [1, 100000, 2000], [2, 150000, 3000], [3, 200000, 4000], [4, 250000, 5000]]) == [True, True, True, True, True]
    assert candidate(candiesCount = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 0, 1], [1, 1, 2], [2, 2, 3], [3, 3, 4], [4, 4, 5], [5, 5, 6], [6, 6, 7], [7, 7, 8], [8, 8, 9], [9, 9, 10]]) == [True, True, True, True, True, True, True, True, True, True]
    assert candidate(candiesCount = [5, 4, 3, 2, 1],queries = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [0, 4, 10], [1, 3, 10], [2, 2, 10], [3, 1, 10], [4, 0, 10]]) == [True, False, False, False, False, True, True, True, True, False]
    assert candidate(candiesCount = [10, 20, 30, 40, 50],queries = [[4, 49, 50], [3, 29, 40], [2, 19, 30], [1, 9, 20], [0, 9, 10]]) == [True, True, True, True, True]
    assert candidate(candiesCount = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 5, 5], [1, 15, 15], [2, 30, 25], [3, 45, 35], [4, 60, 45], [5, 75, 55], [6, 90, 65], [7, 105, 75], [8, 120, 85], [9, 135, 95]]) == [True, True, True, True, True, True, True, True, True, True]
    assert candidate(candiesCount = [100, 200, 300, 400, 500],queries = [[0, 99, 100], [1, 199, 200], [2, 299, 300], [3, 399, 400], [4, 499, 500], [0, 1, 50], [1, 1, 100], [2, 1, 150], [3, 1, 200], [4, 1, 250]]) == [True, True, True, True, True, True, True, False, False, False]
    assert candidate(candiesCount = [100, 200, 300, 400, 500],queries = [[0, 99, 100], [1, 199, 200], [2, 299, 300], [3, 399, 400], [4, 499, 500]]) == [True, True, True, True, True]
    assert candidate(candiesCount = [100000000, 200000000, 300000000, 400000000, 500000000],queries = [[0, 100000000, 150000000], [4, 900000000, 1000000000], [2, 500000000, 350000000]]) == [False, True, True]
    assert candidate(candiesCount = [1000000, 500000, 250000, 125000, 62500, 31250],queries = [[0, 500000, 100000], [5, 500000, 100000], [2, 750000, 50000], [4, 875000, 31250]]) == [True, True, True, True]
    assert candidate(candiesCount = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],queries = [[0, 1000000000, 1000000000], [4, 4000000000, 1000000000], [2, 2500000000, 500000000]]) == [False, True, True]
    assert candidate(candiesCount = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],queries = [[0, 10000, 1000], [1, 20000, 2000], [2, 30000, 3000], [3, 40000, 4000], [4, 50000, 5000], [5, 60000, 6000], [6, 70000, 7000], [7, 80000, 8000], [8, 90000, 9000], [9, 100000, 10000]]) == [False, True, True, True, True, True, True, True, True, True]
    assert candidate(candiesCount = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 0, 10], [1, 1, 10], [2, 2, 10], [3, 3, 10], [4, 4, 10], [5, 5, 10], [6, 6, 10], [7, 7, 10], [8, 8, 10], [9, 9, 10]]) == [True, True, True, True, True, True, True, True, True, True]
    assert candidate(candiesCount = [500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000],queries = [[0, 499999, 500000], [1, 999999, 500000], [2, 1499999, 500000], [3, 1999999, 500000], [4, 2499999, 500000], [5, 2999999, 500000], [6, 3499999, 500000], [7, 3999999, 500000], [8, 4499999, 500000], [9, 4999999, 500000]]) == [True, True, True, True, True, True, True, True, True, True]
    assert candidate(candiesCount = [1000000, 999999, 1000000, 999999, 1000000],queries = [[0, 1000000, 500000], [1, 1999998, 999999], [2, 2999999, 1000000], [3, 3999997, 1000000], [4, 4999999, 1000000]]) == [False, True, False, True, False]
    assert candidate(candiesCount = [100000000, 200000000, 150000000, 300000000, 250000000],queries = [[0, 50000000, 50000000], [1, 100000000, 100000000], [2, 150000000, 150000000], [3, 200000000, 200000000], [4, 250000000, 250000000]]) == [True, True, True, True, True]
    assert candidate(candiesCount = [50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000],queries = [[0, 0, 100000], [1, 100000, 200000], [2, 300000, 300000], [3, 600000, 400000], [4, 1000000, 500000], [5, 1500000, 600000], [6, 2100000, 700000], [7, 2800000, 800000], [8, 3600000, 900000], [9, 4500000, 1000000]]) == [True, True, False, False, False, False, False, False, False, False]
    assert candidate(candiesCount = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],queries = [[0, 0, 1], [1, 1, 10], [2, 11, 100], [3, 111, 1000], [4, 1111, 10000], [5, 11111, 100000], [6, 111111, 1000000], [7, 1111111, 10000000], [8, 11111111, 100000000], [9, 111111111, 1000000000]]) == [True, True, True, True, True, True, True, True, True, True]
    assert candidate(candiesCount = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70], [7, 8, 80], [8, 9, 90], [9, 10, 100], [0, 99, 1000], [1, 199, 1000], [2, 299, 1000], [3, 399, 1000], [4, 499, 1000], [5, 599, 1000], [6, 699, 1000], [7, 799, 1000], [8, 899, 1000], [9, 999, 1000]]) == [True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False, False, False, False, False]
    assert candidate(candiesCount = [10, 20, 30, 40, 50],queries = [[0, 5, 10], [1, 15, 10], [2, 25, 10], [3, 35, 10], [4, 45, 10], [0, 9, 9], [1, 19, 9], [2, 29, 9], [3, 39, 9], [4, 49, 9], [0, 1, 1], [1, 11, 1], [2, 21, 1], [3, 31, 1], [4, 41, 1]]) == [True, True, True, True, True, True, True, True, True, True, True, True, False, False, False]
    assert candidate(candiesCount = [100000000, 200000000, 300000000, 400000000, 500000000],queries = [[0, 99999999, 100000000], [4, 1499999999, 150000000], [2, 299999999, 300000000]]) == [True, True, True]
    assert candidate(candiesCount = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1], [10, 10, 1], [11, 11, 1], [12, 12, 1], [13, 13, 1], [14, 14, 1], [15, 15, 1], [16, 16, 1], [17, 17, 1], [18, 18, 1], [19, 19, 1]]) == [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
    assert candidate(candiesCount = [1, 10, 100, 1000, 10000],queries = [[0, 0, 1], [1, 1, 10], [2, 2, 100], [3, 3, 1000], [4, 4, 10000], [0, 5, 5], [1, 10, 10], [2, 15, 15], [3, 20, 20], [4, 25, 25]]) == [True, True, True, True, True, False, True, True, True, False]
    assert candidate(candiesCount = [1000000, 1000000, 1000000, 1000000, 1000000],queries = [[0, 100000, 200000], [1, 200000, 300000], [2, 300000, 400000], [3, 400000, 500000], [4, 500000, 600000]]) == [True, True, True, True, True]
    assert candidate(candiesCount = [1000, 1000, 1000, 1000, 1000],queries = [[0, 0, 1], [1, 500, 1000], [2, 1000, 1000], [3, 1500, 1000], [4, 2000, 1000]]) == [True, True, True, True, True]
    assert candidate(candiesCount = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],queries = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1]]) == [True, False, False, False, False, False, False, False, False, False]
    assert candidate(candiesCount = [9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 0, 1], [1, 1, 2], [2, 3, 3], [3, 6, 4], [4, 10, 5], [5, 15, 6], [6, 21, 7], [7, 28, 8], [8, 36, 9]]) == [True, False, False, True, True, True, True, True, True]
    assert candidate(candiesCount = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 0, 1], [1, 1, 1], [2, 3, 1], [3, 6, 1], [4, 10, 1], [5, 15, 1], [6, 21, 1], [7, 28, 1], [8, 36, 1], [9, 45, 1]]) == [True, False, False, False, False, False, False, False, False, False]
    assert candidate(candiesCount = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],queries = [[0, 99, 100], [1, 199, 200], [2, 299, 300], [3, 399, 400], [4, 499, 500], [5, 599, 600], [6, 699, 700], [7, 799, 800], [8, 899, 900], [9, 999, 1000]]) == [True, True, True, True, True, True, True, True, True, True]
    assert candidate(candiesCount = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 0, 10], [9, 494, 100], [5, 150, 60], [2, 30, 30], [8, 315, 90]]) == [True, True, True, True, True]
    assert candidate(candiesCount = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 0, 1], [9, 44, 10], [3, 9, 4], [5, 14, 5], [8, 35, 9]]) == [True, True, True, True, True]
    assert candidate(candiesCount = [1000000000, 1000000000, 1000000000],queries = [[0, 500000000, 500000000], [1, 1500000000, 500000000], [2, 2500000000, 500000000]]) == [True, True, True]
    assert candidate(candiesCount = [100, 200, 300, 400, 500],queries = [[0, 0, 100], [1, 100, 200], [2, 300, 300], [3, 600, 400], [4, 1000, 500]]) == [True, True, True, True, True]
    assert candidate(candiesCount = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],queries = [[0, 500000, 2000000], [1, 1000000, 2000000], [2, 1500000, 2000000], [3, 2000000, 2000000], [4, 2500000, 2000000], [5, 3000000, 2000000], [6, 3500000, 2000000], [7, 4000000, 2000000], [8, 4500000, 2000000], [9, 5000000, 2000000]]) == [True, True, True, True, True, True, True, True, True, True]
    assert candidate(candiesCount = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],queries = [[0, 1, 50], [1, 51, 100], [2, 151, 150], [3, 301, 200], [4, 501, 250], [5, 751, 300], [6, 1051, 350], [7, 1401, 400], [8, 1801, 450], [9, 2251, 500]]) == [True, True, True, True, True, True, True, True, True, True]
    assert candidate(candiesCount = [10, 20, 30, 40, 50],queries = [[0, 0, 5], [1, 4, 10], [2, 19, 15], [3, 34, 20], [4, 49, 25]]) == [True, True, True, True, True]
    assert candidate(candiesCount = [1000000000, 999999999, 888888888, 777777777, 666666666],queries = [[0, 1000000000, 500000000], [4, 1000000000, 200000000], [2, 500000000, 100000000]]) == [False, True, True]
    assert candidate(candiesCount = [1000000, 1000000, 1000000],queries = [[0, 100000, 1000], [1, 200000, 500000], [2, 500000, 1]]) == [True, True, False]
    assert candidate(candiesCount = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1]]) == [True, True, True, True, True, True, True, True, True, True]
    assert candidate(candiesCount = [50, 50, 50, 50, 50],queries = [[0, 24, 50], [1, 49, 50], [2, 74, 50], [3, 99, 50], [4, 124, 50], [0, 25, 25], [1, 50, 25], [2, 75, 25], [3, 100, 25], [4, 125, 25]]) == [True, True, True, True, True, True, True, True, True, True]
    assert candidate(candiesCount = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],queries = [[0, 0, 100], [1, 199, 200], [2, 399, 300], [3, 599, 400], [4, 799, 500], [5, 999, 600], [6, 1199, 700], [7, 1399, 800], [8, 1599, 900], [9, 1799, 1000]]) == [True, True, True, True, True, True, True, True, True, True]
    assert candidate(candiesCount = [10, 20, 30, 40, 50],queries = [[0, 0, 10], [1, 10, 20], [2, 30, 30], [3, 60, 40], [4, 100, 50]]) == [True, True, True, True, True]
    assert candidate(candiesCount = [1000000, 500000, 250000, 125000, 62500],queries = [[0, 999999, 1000000], [1, 1499999, 500000], [2, 374999, 250000], [3, 499999, 125000], [4, 593749, 62500]]) == [True, True, True, True, True]
    assert candidate(candiesCount = [100, 200, 300, 400, 500],queries = [[0, 0, 1], [1, 100, 100], [2, 200, 150], [3, 300, 200], [4, 400, 250]]) == [True, True, True, True, True]
    assert candidate(candiesCount = [1, 1, 1, 1, 1],queries = [[0, 0, 1], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1]]) == [True, True, True, True, True]
    assert candidate(candiesCount = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],queries = [[0, 1000, 500], [1, 3000, 1000], [2, 5000, 1500], [3, 7000, 2000], [4, 9000, 2500], [5, 11000, 3000], [6, 13000, 3500], [7, 15000, 4000], [8, 17000, 4500], [9, 19000, 5000]]) == [False, False, True, True, True, True, True, True, True, True]
    assert candidate(candiesCount = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],queries = [[0, 0, 1], [1, 10, 10], [2, 110, 100], [3, 1110, 1000], [4, 11110, 10000], [5, 111110, 100000], [6, 1111110, 1000000], [7, 11111110, 10000000], [8, 111111110, 100000000], [9, 1111111110, 1000000000]]) == [True, True, True, True, True, True, True, True, True, True]


