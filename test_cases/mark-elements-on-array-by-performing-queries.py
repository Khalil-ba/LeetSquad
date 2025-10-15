def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],queries = [[4, 1], [0, 2], [2, 2]]) == [90, 40, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],queries = [[4, 1], [0, 2], [2, 2]]) == [90, 40, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],queries = [[0, 2], [1, 1]]) == [90, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],queries = [[0, 2], [1, 1]]) == [90, 50]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 1, 4],queries = [[2, 1], [4, 2], [0, 2]]) == [12, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 1, 4],queries = [[2, 1], [4, 2], [0, 2]]) == [12, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [3, 3], [1, 1]]) == [4, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [3, 3], [1, 1]]) == [4, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 2, 3],queries = [[0, 1]]) == [7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 2, 3],queries = [[0, 1]]) == [7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 2, 3, 1],queries = [[1, 2], [3, 3], [4, 2]]) == [8, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 2, 3, 1],queries = [[1, 2], [3, 3], [4, 2]]) == [8, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7],queries = [[0, 3], [2, 2]]) == [7, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7],queries = [[0, 3], [2, 2]]) == [7, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],queries = [[1, 2], [2, 1], [4, 2]]) == [90, 50, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],queries = [[1, 2], [2, 1], [4, 2]]) == [90, 50, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],queries = [[0, 3], [1, 1], [2, 1]]) == [1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],queries = [[0, 3], [1, 1], [2, 1]]) == [1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],queries = [[0, 5], [1, 1]]) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],queries = [[0, 5], [1, 1]]) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],queries = [[0, 2], [1, 1], [3, 2]]) == [2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],queries = [[0, 2], [1, 1], [3, 2]]) == [2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],queries = [[0, 3], [1, 2], [2, 1]]) == [50, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],queries = [[0, 3], [1, 2], [2, 1]]) == [50, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 2, 4],queries = [[2, 1], [0, 2], [3, 3]]) == [12, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 2, 4],queries = [[2, 1], [0, 2], [3, 3]]) == [12, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],queries = [[0, 3], [1, 1], [4, 1]]) == [50, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],queries = [[0, 3], [1, 1], [4, 1]]) == [50, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 1, 9],queries = [[2, 1], [4, 2]]) == [17, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 1, 9],queries = [[2, 1], [4, 2]]) == [17, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],queries = [[2, 1], [0, 2], [1, 2]]) == [15, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],queries = [[2, 1], [0, 2], [1, 2]]) == [15, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],queries = [[0, 2], [1, 1], [2, 3]]) == [10, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],queries = [[0, 2], [1, 1], [2, 3]]) == [10, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 5, 3, 8, 1, 4, 6, 2],queries = [[6, 2], [3, 1], [0, 3], [5, 2]]) == [27, 16, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 5, 3, 8, 1, 4, 6, 2],queries = [[6, 2], [3, 1], [0, 3], [5, 2]]) == [27, 16, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],queries = [[0, 5], [2, 3], [4, 2], [8, 1]]) == [12, 3, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],queries = [[0, 5], [2, 3], [4, 2], [8, 1]]) == [12, 3, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == [5200, 4900, 4500, 4000, 3400, 2700, 1900, 1000, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == [5200, 4900, 4500, 4000, 3400, 2700, 1900, 1000, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 7, 3, 4, 1, 6, 8, 9, 10],queries = [[4, 2], [1, 1], [7, 3], [9, 2]]) == [48, 45, 19, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 7, 3, 4, 1, 6, 8, 9, 10],queries = [[4, 2], [1, 1], [7, 3], [9, 2]]) == [48, 45, 19, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 10], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5]]) == [70, 27, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 10], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5]]) == [70, 27, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[9, 3], [8, 2], [7, 1], [6, 4], [5, 5]]) == [39, 21, 7, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[9, 3], [8, 2], [7, 1], [6, 4], [5, 5]]) == [39, 21, 7, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],queries = [[0, 5], [1, 3], [2, 1], [3, 1], [4, 2]]) == [1111000000, 1000000000, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],queries = [[0, 5], [1, 3], [2, 1], [3, 1], [4, 2]]) == [1111000000, 1000000000, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 9, 1, 5, 2, 8, 4, 6, 10],queries = [[0, 2], [5, 3], [8, 2], [3, 1]]) == [45, 33, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 9, 1, 5, 2, 8, 4, 6, 10],queries = [[0, 2], [5, 3], [8, 2], [3, 1]]) == [45, 33, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],queries = [[0, 10], [1, 5], [2, 3], [3, 2], [4, 1]]) == [144, 74, 20, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],queries = [[0, 10], [1, 5], [2, 3], [3, 2], [4, 1]]) == [144, 74, 20, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 6, 5, 7, 9, 8, 10],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == [52, 45, 40, 34, 27, 19, 10, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 6, 5, 7, 9, 8, 10],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == [52, 45, 40, 34, 27, 19, 10, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [2, 3], [4, 2], [9, 1]]) == [4, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [2, 3], [4, 2], [9, 1]]) == [4, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 10], [1, 5], [9, 3], [3, 2]]) == [0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 10], [1, 5], [9, 3], [3, 2]]) == [0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 2, 3, 6, 7, 8, 9, 10],queries = [[0, 1], [1, 2], [2, 3], [3, 4]]) == [49, 44, 19, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 2, 3, 6, 7, 8, 9, 10],queries = [[0, 1], [1, 2], [2, 3], [3, 4]]) == [49, 44, 19, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 3], [1, 2], [2, 1], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == [450, 340, 270, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 3], [1, 2], [2, 1], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == [450, 340, 270, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],queries = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5]]) == [990, 540, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],queries = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5]]) == [990, 540, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1]]) == [28, 26, 24, 21, 18, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1]]) == [28, 26, 24, 21, 18, 14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],queries = [[9, 4], [5, 3], [1, 2], [7, 1]]) == [35, 17, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],queries = [[9, 4], [5, 3], [1, 2], [7, 1]]) == [35, 17, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],queries = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5]]) == [189, 144, 74, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],queries = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5]]) == [189, 144, 74, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[9, 1], [8, 2], [7, 3], [6, 4], [5, 5]]) == [44, 30, 7, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[9, 1], [8, 2], [7, 3], [6, 4], [5, 5]]) == [44, 30, 7, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1],queries = [[1, 3], [3, 2], [5, 1], [7, 4]]) == [51, 40, 30, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1],queries = [[1, 3], [3, 2], [5, 1], [7, 4]]) == [51, 40, 30, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6, 0],queries = [[9, 2], [3, 3], [5, 2], [0, 1], [7, 4]]) == [42, 30, 17, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6, 0],queries = [[9, 2], [3, 3], [5, 2], [0, 1], [7, 4]]) == [42, 30, 17, 9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],queries = [[0, 5], [5, 5], [10, 5], [15, 5]]) == [189, 144, 74, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],queries = [[0, 5], [5, 5], [10, 5], [15, 5]]) == [189, 144, 74, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 2, 4, 5, 3, 1, 2, 4, 5, 3, 1, 2, 4, 5, 3, 1, 2, 4],queries = [[2, 1], [0, 2], [3, 3], [1, 4], [4, 5]]) == [58, 51, 43, 27, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 2, 4, 5, 3, 1, 2, 4, 5, 3, 1, 2, 4, 5, 3, 1, 2, 4],queries = [[2, 1], [0, 2], [3, 3], [1, 4], [4, 5]]) == [58, 51, 43, 27, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1],queries = [[0, 3], [1, 3], [2, 3], [3, 3], [4, 3]]) == [22, 15, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1],queries = [[0, 3], [1, 3], [2, 3], [3, 3], [4, 3]]) == [22, 15, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 12, 18, 14, 16, 17, 13, 19, 20, 11],queries = [[3, 2], [0, 1], [8, 4], [2, 3]]) == [118, 90, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 12, 18, 14, 16, 17, 13, 19, 20, 11],queries = [[3, 2], [0, 1], [8, 4], [2, 3]]) == [118, 90, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 5], [5, 3], [9, 2]]) == [340, 100, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 5], [5, 3], [9, 2]]) == [340, 100, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 100, 100],queries = [[0, 2], [1, 1], [2, 2], [3, 1], [4, 1]]) == [200, 100, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 100, 100],queries = [[0, 2], [1, 1], [2, 2], [3, 1], [4, 1]]) == [200, 100, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [5, 4], [6, 3], [7, 2], [8, 1], [9, 0]]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [5, 4], [6, 3], [7, 2], [8, 1], [9, 0]]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 2, 4, 6, 8, 7, 9],queries = [[2, 3], [0, 1], [3, 2], [5, 2]]) == [35, 24, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 2, 4, 6, 8, 7, 9],queries = [[2, 3], [0, 1], [3, 2], [5, 2]]) == [35, 24, 9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == [54, 49, 34, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == [54, 49, 34, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 10], [1, 5], [2, 2], [3, 3], [4, 1]]) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 10], [1, 5], [2, 2], [3, 3], [4, 1]]) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 99999, 99998, 99997, 99996],queries = [[4, 2], [3, 1], [2, 2], [1, 1], [0, 1]]) == [199999, 100000, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 99999, 99998, 99997, 99996],queries = [[4, 2], [3, 1], [2, 2], [1, 1], [0, 1]]) == [199999, 100000, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[9, 1], [8, 1], [7, 1], [6, 1], [5, 1], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1]]) == [44, 33, 22, 11, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[9, 1], [8, 1], [7, 1], [6, 1], [5, 1], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1]]) == [44, 33, 22, 11, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[9, 5], [3, 3], [1, 2]]) == [34, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[9, 5], [3, 3], [1, 2]]) == [34, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],queries = [[0, 10], [10, 5], [15, 3], [19, 2], [0, 5]]) == [144, 74, 20, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],queries = [[0, 10], [10, 5], [15, 3], [19, 2], [0, 5]]) == [144, 74, 20, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],queries = [[0, 5], [5, 5], [10, 5]]) == [990, 540, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],queries = [[0, 5], [5, 5], [10, 5]]) == [990, 540, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 7], [2, 5], [4, 4], [6, 3], [8, 2]]) == [77, 14, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 7], [2, 5], [4, 4], [6, 3], [8, 2]]) == [77, 14, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [1, 3], [2, 1], [3, 1]]) == [4, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [1, 3], [2, 1], [3, 1]]) == [4, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],queries = [[0, 1], [1, 2], [2, 3], [3, 4]]) == [52, 35, 17, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],queries = [[0, 1], [1, 2], [2, 3], [3, 4]]) == [52, 35, 17, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 3], [1, 2], [2, 1], [3, 3], [4, 1]]) == [450, 340, 270, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 3], [1, 2], [2, 1], [3, 3], [4, 1]]) == [450, 340, 270, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1], [14, 1], [15, 1], [16, 1], [17, 1], [18, 1], [19, 1]]) == [189, 168, 147, 126, 105, 84, 63, 42, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1], [14, 1], [15, 1], [16, 1], [17, 1], [18, 1], [19, 1]]) == [189, 168, 147, 126, 105, 84, 63, 42, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 2, 3, 1],queries = [[1, 2], [3, 3], [4, 2], [5, 1], [6, 0], [0, 1]]) == [8, 3, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 2, 3, 1],queries = [[1, 2], [3, 3], [4, 2], [5, 1], [6, 0], [0, 1]]) == [8, 3, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],queries = [[0, 2], [3, 2], [5, 1], [7, 3], [9, 1]]) == [420, 280, 170, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],queries = [[0, 2], [3, 2], [5, 1], [7, 3], [9, 1]]) == [420, 280, 170, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 1, 2, 4, 1, 2, 3, 4, 5],queries = [[0, 2], [3, 3], [5, 1], [2, 2], [7, 4]]) == [23, 13, 9, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 1, 2, 4, 1, 2, 3, 4, 5],queries = [[0, 2], [3, 3], [5, 1], [2, 2], [7, 4]]) == [23, 13, 9, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 10], [1, 5], [2, 3], [3, 2], [4, 1]]) == [135, 51, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 10], [1, 5], [2, 3], [3, 2], [4, 1]]) == [135, 51, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],queries = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) == [114, 99, 65, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],queries = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) == [114, 99, 65, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [5, 3], [2, 2]]) == [4, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [5, 3], [2, 2]]) == [4, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],queries = [[0, 5], [1, 2], [2, 3], [3, 1]]) == [12, 6, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],queries = [[0, 5], [1, 2], [2, 3], [3, 1]]) == [12, 6, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[9, 5], [8, 4], [7, 3], [6, 2], [5, 1]]) == [30, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[9, 5], [8, 4], [7, 3], [6, 2], [5, 1]]) == [30, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 1], [2, 1], [4, 1], [6, 1], [8, 1], [1, 1], [3, 1], [5, 1], [7, 1], [9, 1]]) == [52, 45, 34, 19, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 1], [2, 1], [4, 1], [6, 1], [8, 1], [1, 1], [3, 1], [5, 1], [7, 1], [9, 1]]) == [52, 45, 34, 19, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 5], [1, 3], [2, 2], [3, 1], [4, 0]]) == [34, 10, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 5], [1, 3], [2, 2], [3, 1], [4, 0]]) == [34, 10, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],queries = [[0, 5], [2, 2], [4, 3], [6, 2], [8, 1]]) == [80, 40, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],queries = [[0, 5], [2, 2], [4, 3], [6, 2], [8, 1]]) == [80, 40, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],queries = [[0, 10], [5, 5], [9, 1]]) == [0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],queries = [[0, 10], [5, 5], [9, 1]]) == [0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 5], [1, 2], [2, 2], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == [34, 19, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 5], [1, 2], [2, 2], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == [34, 19, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 5], [2, 3], [8, 2], [5, 1], [7, 1]]) == [30, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 5], [2, 3], [8, 2], [5, 1], [7, 1]]) == [30, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],queries = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]) == [140, 120, 90, 50, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],queries = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]) == [140, 120, 90, 50, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [2, 2], [4, 3]]) == [4, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [2, 2], [4, 3]]) == [4, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 99999, 99998, 99997, 99996],queries = [[2, 2], [0, 1], [4, 2]]) == [199999, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 99999, 99998, 99997, 99996],queries = [[2, 2], [0, 1], [4, 2]]) == [199999, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == [52, 49, 45, 40, 34, 27, 19, 10, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == [52, 49, 45, 40, 34, 27, 19, 10, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],queries = [[0, 3], [1, 3], [2, 3], [3, 3], [4, 3]]) == [110, 92, 65, 29, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],queries = [[0, 3], [1, 3], [2, 3], [3, 3], [4, 3]]) == [110, 92, 65, 29, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],queries = [[0, 5], [5, 3], [9, 2], [4, 4]]) == [26, 8, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],queries = [[0, 5], [5, 3], [9, 2], [4, 4]]) == [26, 8, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 10], [1, 10], [2, 10], [3, 10], [4, 10]]) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 10], [1, 10], [2, 10], [3, 10], [4, 10]]) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],queries = [[0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3]]) == [55, 40, 25, 10, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],queries = [[0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3]]) == [55, 40, 25, 10, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995],queries = [[0, 1], [1, 2], [2, 3], [3, 1]]) == [399990, 99998, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995],queries = [[0, 1], [1, 2], [2, 3], [3, 1]]) == [399990, 99998, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],queries = [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2]]) == [25, 19, 12, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],queries = [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2]]) == [25, 19, 12, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 5], [2, 2], [4, 1], [6, 3], [8, 1]]) == [34, 19, 10, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 5], [2, 2], [4, 1], [6, 3], [8, 1]]) == [34, 19, 10, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],queries = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == [440, 300, 70, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],queries = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == [440, 300, 70, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [2, 3], [4, 2], [8, 1]]) == [4, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [2, 3], [4, 2], [8, 1]]) == [4, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],queries = [[9, 5], [8, 3], [7, 2], [6, 1], [5, 4]]) == [340, 100, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],queries = [[9, 5], [8, 3], [7, 2], [6, 1], [5, 4]]) == [340, 100, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 1], [1, 2], [2, 3], [3, 2], [4, 1]]) == [8, 6, 3, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 1], [1, 2], [2, 3], [3, 2], [4, 1]]) == [8, 6, 3, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == [8, 7, 6, 5, 4, 3, 2, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == [8, 7, 6, 5, 4, 3, 2, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],queries = [[0, 5], [2, 4], [4, 3], [6, 2], [8, 1]]) == [99, 65, 29, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],queries = [[0, 5], [2, 4], [4, 3], [6, 2], [8, 1]]) == [99, 65, 29, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 3, 4, 2, 5, 4, 3, 2, 1],queries = [[4, 2], [0, 2], [9, 1], [2, 3]]) == [26, 16, 13, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 3, 4, 2, 5, 4, 3, 2, 1],queries = [[4, 2], [0, 2], [9, 1], [2, 3]]) == [26, 16, 13, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 1, 2, 3, 4, 10],queries = [[0, 4], [5, 2], [9, 3], [2, 1]]) == [40, 27, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 1, 2, 3, 4, 10],queries = [[0, 4], [5, 2], [9, 3], [2, 1]]) == [40, 27, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],queries = [[0, 5], [1, 3], [4, 2], [7, 1], [9, 1]]) == [3400, 1000, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],queries = [[0, 5], [1, 3], [4, 2], [7, 1], [9, 1]]) == [3400, 1000, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[9, 1], [8, 2], [7, 3], [6, 4]]) == [52, 45, 27, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[9, 1], [8, 2], [7, 3], [6, 4]]) == [52, 45, 27, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],queries = [[0, 5], [1, 3], [2, 2], [3, 1], [4, 1]]) == [300000, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],queries = [[0, 5], [1, 3], [2, 2], [3, 1], [4, 1]]) == [300000, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],queries = [[0, 2], [2, 2], [4, 2], [6, 2], [8, 2]]) == [35, 25, 15, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],queries = [[0, 2], [2, 2], [4, 2], [6, 2], [8, 2]]) == [35, 25, 15, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 10], [5, 5], [9, 3], [4, 2], [2, 1]]) == [0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 10], [5, 5], [9, 3], [4, 2], [2, 1]]) == [0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],queries = [[1, 4], [3, 3], [5, 2], [7, 1], [9, 1]]) == [75, 36, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],queries = [[1, 4], [3, 3], [5, 2], [7, 1], [9, 1]]) == [75, 36, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 3, 2, 4, 6, 8, 7, 10, 9],queries = [[0, 5], [3, 3], [8, 2]]) == [34, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 3, 2, 4, 6, 8, 7, 10, 9],queries = [[0, 5], [3, 3], [8, 2]]) == [34, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],queries = [[4, 3], [0, 2], [9, 4]]) == [24, 13, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],queries = [[4, 3], [0, 2], [9, 4]]) == [24, 13, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [1, 3], [5, 2], [8, 1]]) == [4, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [1, 3], [5, 2], [8, 1]]) == [4, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [2, 3], [8, 2], [1, 1]]) == [4, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [2, 3], [8, 2], [1, 1]]) == [4, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 1, 2, 3, 1, 3, 2, 2],queries = [[1, 2], [3, 3], [4, 2], [0, 1], [5, 1]]) == [15, 10, 6, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 1, 2, 3, 1, 3, 2, 2],queries = [[1, 2], [3, 3], [4, 2], [0, 1], [5, 1]]) == [15, 10, 6, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 5], [5, 3], [9, 2], [4, 1], [2, 1]]) == [34, 10, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 5], [5, 3], [9, 2], [4, 1], [2, 1]]) == [34, 10, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],queries = [[0, 2], [1, 3], [2, 4], [3, 1], [4, 1]]) == [35, 18, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],queries = [[0, 2], [1, 3], [2, 4], [3, 1], [4, 1]]) == [35, 18, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 5], [5, 5], [10, 5], [15, 5]]) == [175, 120, 54, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 5], [5, 5], [10, 5], [15, 5]]) == [175, 120, 54, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 20, 30, 10, 40],queries = [[4, 2], [3, 1], [2, 1], [1, 1], [0, 1]]) == [80, 50, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 20, 30, 10, 40],queries = [[4, 2], [3, 1], [2, 1], [1, 1], [0, 1]]) == [80, 50, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == [36, 27, 18, 9, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == [36, 27, 18, 9, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],queries = [[9, 5], [4, 2], [0, 3], [8, 4]]) == [340, 190, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],queries = [[9, 5], [4, 2], [0, 3], [8, 4]]) == [340, 190, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],queries = [[0, 3], [2, 2], [5, 1]]) == [599979, 299992, 199996]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],queries = [[0, 3], [2, 2], [5, 1]]) == [599979, 299992, 199996]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[9, 3], [0, 2], [5, 4]]) == [39, 30, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[9, 3], [0, 2], [5, 4]]) == [39, 30, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [1, 2], [5, 3]]) == [4, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [1, 2], [5, 3]]) == [4, 2, 0]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [10, 20, 30, 40, 50],queries = [[4, 1], [0, 2], [2, 2]]) == [90, 40, 0]
    assert candidate(nums = [10, 20, 30, 40, 50],queries = [[0, 2], [1, 1]]) == [90, 50]
    assert candidate(nums = [5, 3, 8, 1, 4],queries = [[2, 1], [4, 2], [0, 2]]) == [12, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [3, 3], [1, 1]]) == [4, 1, 0]
    assert candidate(nums = [1, 4, 2, 3],queries = [[0, 1]]) == [7]
    assert candidate(nums = [1, 2, 2, 1, 2, 3, 1],queries = [[1, 2], [3, 3], [4, 2]]) == [8, 3, 0]
    assert candidate(nums = [7, 7, 7, 7, 7],queries = [[0, 3], [2, 2]]) == [7, 0]
    assert candidate(nums = [10, 20, 30, 40, 50],queries = [[1, 2], [2, 1], [4, 2]]) == [90, 50, 0]
    assert candidate(nums = [1, 1, 1, 1, 1],queries = [[0, 3], [1, 1], [2, 1]]) == [1, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 1],queries = [[0, 5], [1, 1]]) == [0, 0]
    assert candidate(nums = [1, 1, 1, 1, 1],queries = [[0, 2], [1, 1], [3, 2]]) == [2, 1, 0]
    assert candidate(nums = [10, 20, 30, 40, 50],queries = [[0, 3], [1, 2], [2, 1]]) == [50, 0, 0]
    assert candidate(nums = [5, 3, 1, 2, 4],queries = [[2, 1], [0, 2], [3, 3]]) == [12, 0, 0]
    assert candidate(nums = [10, 20, 30, 40, 50],queries = [[0, 3], [1, 1], [4, 1]]) == [50, 0, 0]
    assert candidate(nums = [5, 3, 8, 1, 9],queries = [[2, 1], [4, 2]]) == [17, 0]
    assert candidate(nums = [5, 5, 5, 5, 5],queries = [[2, 1], [0, 2], [1, 2]]) == [15, 5, 0]
    assert candidate(nums = [5, 5, 5, 5, 5],queries = [[0, 2], [1, 1], [2, 3]]) == [10, 5, 0]
    assert candidate(nums = [7, 5, 3, 8, 1, 4, 6, 2],queries = [[6, 2], [3, 1], [0, 3], [5, 2]]) == [27, 16, 0, 0]
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],queries = [[0, 5], [2, 3], [4, 2], [8, 1]]) == [12, 3, 0, 0]
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == [5200, 4900, 4500, 4000, 3400, 2700, 1900, 1000, 0, 0]
    assert candidate(nums = [5, 2, 7, 3, 4, 1, 6, 8, 9, 10],queries = [[4, 2], [1, 1], [7, 3], [9, 2]]) == [48, 45, 19, 0]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 10], [1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5]]) == [70, 27, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[9, 3], [8, 2], [7, 1], [6, 4], [5, 5]]) == [39, 21, 7, 0, 0]
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],queries = [[0, 5], [1, 3], [2, 1], [3, 1], [4, 2]]) == [1111000000, 1000000000, 0, 0, 0]
    assert candidate(nums = [7, 3, 9, 1, 5, 2, 8, 4, 6, 10],queries = [[0, 2], [5, 3], [8, 2], [3, 1]]) == [45, 33, 10, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],queries = [[0, 10], [1, 5], [2, 3], [3, 2], [4, 1]]) == [144, 74, 20, 0, 0]
    assert candidate(nums = [1, 3, 2, 4, 6, 5, 7, 9, 8, 10],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == [52, 45, 40, 34, 27, 19, 10, 0, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [2, 3], [4, 2], [9, 1]]) == [4, 1, 0, 0]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 10], [1, 5], [9, 3], [3, 2]]) == [0, 0, 0, 0]
    assert candidate(nums = [5, 1, 4, 2, 3, 6, 7, 8, 9, 10],queries = [[0, 1], [1, 2], [2, 3], [3, 4]]) == [49, 44, 19, 0]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 3], [1, 2], [2, 1], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]) == [450, 340, 270, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],queries = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5]]) == [990, 540, 0, 0, 0]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1]]) == [28, 26, 24, 21, 18, 14]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],queries = [[9, 4], [5, 3], [1, 2], [7, 1]]) == [35, 17, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],queries = [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5]]) == [189, 144, 74, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[9, 1], [8, 2], [7, 3], [6, 4], [5, 5]]) == [44, 30, 7, 0, 0]
    assert candidate(nums = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1],queries = [[1, 3], [3, 2], [5, 1], [7, 4]]) == [51, 40, 30, 0]
    assert candidate(nums = [5, 1, 9, 2, 8, 3, 7, 4, 6, 0],queries = [[9, 2], [3, 3], [5, 2], [0, 1], [7, 4]]) == [42, 30, 17, 9, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],queries = [[0, 5], [5, 5], [10, 5], [15, 5]]) == [189, 144, 74, 0]
    assert candidate(nums = [5, 3, 1, 2, 4, 5, 3, 1, 2, 4, 5, 3, 1, 2, 4, 5, 3, 1, 2, 4],queries = [[2, 1], [0, 2], [3, 3], [1, 4], [4, 5]]) == [58, 51, 43, 27, 5]
    assert candidate(nums = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1],queries = [[0, 3], [1, 3], [2, 3], [3, 3], [4, 3]]) == [22, 15, 0, 0, 0]
    assert candidate(nums = [15, 12, 18, 14, 16, 17, 13, 19, 20, 11],queries = [[3, 2], [0, 1], [8, 4], [2, 3]]) == [118, 90, 0, 0]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 5], [5, 3], [9, 2]]) == [340, 100, 0]
    assert candidate(nums = [100, 100, 100, 100, 100],queries = [[0, 2], [1, 1], [2, 2], [3, 1], [4, 1]]) == [200, 100, 0, 0, 0]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5], [5, 4], [6, 3], [7, 2], [8, 1], [9, 0]]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [5, 3, 1, 2, 4, 6, 8, 7, 9],queries = [[2, 3], [0, 1], [3, 2], [5, 2]]) == [35, 24, 9, 0]
    assert candidate(nums = [100000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == [54, 49, 34, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 10], [1, 5], [2, 2], [3, 3], [4, 1]]) == [0, 0, 0, 0, 0]
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996],queries = [[4, 2], [3, 1], [2, 2], [1, 1], [0, 1]]) == [199999, 100000, 0, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[9, 1], [8, 1], [7, 1], [6, 1], [5, 1], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1]]) == [44, 33, 22, 11, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[9, 5], [3, 3], [1, 2]]) == [34, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],queries = [[0, 10], [10, 5], [15, 3], [19, 2], [0, 5]]) == [144, 74, 20, 0, 0]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],queries = [[0, 5], [5, 5], [10, 5]]) == [990, 540, 0]
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 7], [2, 5], [4, 4], [6, 3], [8, 2]]) == [77, 14, 0, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [1, 3], [2, 1], [3, 1]]) == [4, 1, 0, 0]
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],queries = [[0, 1], [1, 2], [2, 3], [3, 4]]) == [52, 35, 17, 0]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 3], [1, 2], [2, 1], [3, 3], [4, 1]]) == [450, 340, 270, 0, 0]
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [11, 1], [12, 1], [13, 1], [14, 1], [15, 1], [16, 1], [17, 1], [18, 1], [19, 1]]) == [189, 168, 147, 126, 105, 84, 63, 42, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 2, 1, 2, 3, 1],queries = [[1, 2], [3, 3], [4, 2], [5, 1], [6, 0], [0, 1]]) == [8, 3, 0, 0, 0, 0]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],queries = [[0, 2], [3, 2], [5, 1], [7, 3], [9, 1]]) == [420, 280, 170, 0, 0]
    assert candidate(nums = [5, 3, 1, 2, 4, 1, 2, 3, 4, 5],queries = [[0, 2], [3, 3], [5, 1], [2, 2], [7, 4]]) == [23, 13, 9, 0, 0]
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 10], [1, 5], [2, 3], [3, 2], [4, 1]]) == [135, 51, 0, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],queries = [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]) == [114, 99, 65, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [5, 3], [2, 2]]) == [4, 1, 0]
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],queries = [[0, 5], [1, 2], [2, 3], [3, 1]]) == [12, 6, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[9, 5], [8, 4], [7, 3], [6, 2], [5, 1]]) == [30, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 1], [2, 1], [4, 1], [6, 1], [8, 1], [1, 1], [3, 1], [5, 1], [7, 1], [9, 1]]) == [52, 45, 34, 19, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 5], [1, 3], [2, 2], [3, 1], [4, 0]]) == [34, 10, 0, 0, 0]
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],queries = [[0, 5], [2, 2], [4, 3], [6, 2], [8, 1]]) == [80, 40, 0, 0, 0]
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],queries = [[0, 10], [5, 5], [9, 1]]) == [0, 0, 0]
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 5], [1, 2], [2, 2], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == [34, 19, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 5], [2, 3], [8, 2], [5, 1], [7, 1]]) == [30, 0, 0, 0, 0]
    assert candidate(nums = [10, 20, 30, 40, 50],queries = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0]]) == [140, 120, 90, 50, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [2, 2], [4, 3]]) == [4, 2, 0]
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996],queries = [[2, 2], [0, 1], [4, 2]]) == [199999, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == [52, 49, 45, 40, 34, 27, 19, 10, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],queries = [[0, 3], [1, 3], [2, 3], [3, 3], [4, 3]]) == [110, 92, 65, 29, 0]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],queries = [[0, 5], [5, 3], [9, 2], [4, 4]]) == [26, 8, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 10], [1, 10], [2, 10], [3, 10], [4, 10]]) == [0, 0, 0, 0, 0]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],queries = [[0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3]]) == [55, 40, 25, 10, 0, 0]
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995],queries = [[0, 1], [1, 2], [2, 3], [3, 1]]) == [399990, 99998, 0, 0]
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4],queries = [[0, 2], [1, 2], [2, 2], [3, 2], [4, 2]]) == [25, 19, 12, 4, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 5], [2, 2], [4, 1], [6, 3], [8, 1]]) == [34, 19, 10, 0, 0]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],queries = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]) == [440, 300, 70, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [2, 3], [4, 2], [8, 1]]) == [4, 1, 0, 0]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],queries = [[9, 5], [8, 3], [7, 2], [6, 1], [5, 4]]) == [340, 100, 0, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 1], [1, 2], [2, 3], [3, 2], [4, 1]]) == [8, 6, 3, 1, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == [8, 7, 6, 5, 4, 3, 2, 1, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],queries = [[0, 5], [2, 4], [4, 3], [6, 2], [8, 1]]) == [99, 65, 29, 0, 0]
    assert candidate(nums = [5, 1, 3, 4, 2, 5, 4, 3, 2, 1],queries = [[4, 2], [0, 2], [9, 1], [2, 3]]) == [26, 16, 13, 0]
    assert candidate(nums = [5, 6, 7, 8, 9, 1, 2, 3, 4, 10],queries = [[0, 4], [5, 2], [9, 3], [2, 1]]) == [40, 27, 0, 0]
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],queries = [[0, 5], [1, 3], [4, 2], [7, 1], [9, 1]]) == [3400, 1000, 0, 0, 0]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[9, 1], [8, 2], [7, 3], [6, 4]]) == [52, 45, 27, 0]
    assert candidate(nums = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000],queries = [[0, 5], [1, 3], [2, 2], [3, 1], [4, 1]]) == [300000, 0, 0, 0, 0]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],queries = [[0, 2], [2, 2], [4, 2], [6, 2], [8, 2]]) == [35, 25, 15, 5, 0]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],queries = [[0, 10], [5, 5], [9, 3], [4, 2], [2, 1]]) == [0, 0, 0, 0, 0]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],queries = [[1, 4], [3, 3], [5, 2], [7, 1], [9, 1]]) == [75, 36, 0, 0, 0]
    assert candidate(nums = [5, 1, 3, 2, 4, 6, 8, 7, 10, 9],queries = [[0, 5], [3, 3], [8, 2]]) == [34, 10, 0]
    assert candidate(nums = [5, 4, 3, 2, 1, 5, 4, 3, 2, 1],queries = [[4, 3], [0, 2], [9, 4]]) == [24, 13, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [1, 3], [5, 2], [8, 1]]) == [4, 1, 0, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [2, 3], [8, 2], [1, 1]]) == [4, 1, 0, 0]
    assert candidate(nums = [1, 2, 2, 1, 2, 3, 1, 3, 2, 2],queries = [[1, 2], [3, 3], [4, 2], [0, 1], [5, 1]]) == [15, 10, 6, 3, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[0, 5], [5, 3], [9, 2], [4, 1], [2, 1]]) == [34, 10, 0, 0, 0]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],queries = [[0, 2], [1, 3], [2, 4], [3, 1], [4, 1]]) == [35, 18, 0, 0, 0]
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],queries = [[0, 5], [5, 5], [10, 5], [15, 5]]) == [175, 120, 54, 0]
    assert candidate(nums = [50, 20, 30, 10, 40],queries = [[4, 2], [3, 1], [2, 1], [1, 1], [0, 1]]) == [80, 50, 0, 0, 0]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],queries = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]) == [36, 27, 18, 9, 0, 0, 0, 0, 0, 0]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],queries = [[9, 5], [4, 2], [0, 3], [8, 4]]) == [340, 190, 0, 0]
    assert candidate(nums = [100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991],queries = [[0, 3], [2, 2], [5, 1]]) == [599979, 299992, 199996]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],queries = [[9, 3], [0, 2], [5, 4]]) == [39, 30, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],queries = [[0, 5], [1, 2], [5, 3]]) == [4, 2, 0]


