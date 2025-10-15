def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 5, 6, 1],removeQueries = [0, 3, 2, 4, 1]) == [14, 7, 2, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 5, 6, 1],removeQueries = [0, 3, 2, 4, 1]) == [14, 7, 2, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 3, 2],removeQueries = [2, 0, 4, 1, 3]) == [6, 5, 3, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 3, 2],removeQueries = [2, 0, 4, 1, 3]) == [6, 5, 3, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000],removeQueries = [0, 1, 2]) == [2000000000, 1000000000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000],removeQueries = [0, 1, 2]) == [2000000000, 1000000000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],removeQueries = [4, 3, 2, 1, 0]) == [100, 60, 30, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],removeQueries = [4, 3, 2, 1, 0]) == [100, 60, 30, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 3],removeQueries = [1, 2, 0, 3]) == [7, 5, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 3],removeQueries = [1, 2, 0, 3]) == [7, 5, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 2, 11, 1],removeQueries = [3, 2, 1, 0]) == [16, 5, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 2, 11, 1],removeQueries = [3, 2, 1, 0]) == [16, 5, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],removeQueries = [0, 1, 2, 3, 4]) == [140, 120, 90, 50, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],removeQueries = [0, 1, 2, 3, 4]) == [140, 120, 90, 50, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],removeQueries = [2, 4, 0, 1, 3]) == [90, 40, 40, 40, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],removeQueries = [2, 4, 0, 1, 3]) == [90, 40, 40, 40, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 3, 1, 4],removeQueries = [2, 0, 4, 3, 1]) == [7, 5, 2, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 3, 1, 4],removeQueries = [2, 0, 4, 3, 1]) == [7, 5, 2, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],removeQueries = [0, 1, 2, 3, 4]) == [4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],removeQueries = [0, 1, 2, 3, 4]) == [4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000],removeQueries = [0, 1, 2]) == [2000000000, 1000000000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000],removeQueries = [0, 1, 2]) == [2000000000, 1000000000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 3, 2, 4],removeQueries = [2, 0, 1, 3, 4]) == [6, 6, 6, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 3, 2, 4],removeQueries = [2, 0, 1, 3, 4]) == [6, 6, 6, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],removeQueries = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [45, 36, 28, 21, 15, 10, 6, 3, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],removeQueries = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [45, 36, 28, 21, 15, 10, 6, 3, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 3, 1, 4],removeQueries = [2, 0, 3, 4, 1]) == [7, 5, 4, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 3, 1, 4],removeQueries = [2, 0, 3, 4, 1]) == [7, 5, 4, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9000000000, 8000000000, 7000000000, 6000000000, 5000000000, 4000000000, 3000000000, 2000000000, 1000000000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9000000000, 8000000000, 7000000000, 6000000000, 5000000000, 4000000000, 3000000000, 2000000000, 1000000000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 100, 1000, 10000, 100000, 1000000],removeQueries = [5, 4, 3, 2, 1, 0]) == [111110, 11110, 1110, 110, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 100, 1000, 10000, 100000, 1000000],removeQueries = [5, 4, 3, 2, 1, 0]) == [111110, 11110, 1110, 110, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],removeQueries = [24, 12, 6, 0, 2, 10, 14, 20, 22, 8, 16, 18, 4, 15, 11, 13, 7, 19, 17, 3, 5, 9, 1, 21, 23, 25]) == [300, 209, 209, 209, 209, 209, 180, 90, 90, 90, 57, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],removeQueries = [24, 12, 6, 0, 2, 10, 14, 20, 22, 8, 16, 18, 4, 15, 11, 13, 7, 19, 17, 3, 5, 9, 1, 21, 23, 25]) == [300, 209, 209, 209, 209, 209, 180, 90, 90, 90, 57, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 1, 5, 3, 2, 4, 8, 6, 7, 10],removeQueries = [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]) == [46, 36, 35, 28, 23, 17, 14, 6, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 1, 5, 3, 2, 4, 8, 6, 7, 10],removeQueries = [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]) == [46, 36, 35, 28, 23, 17, 14, 6, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],removeQueries = [0, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [324, 299, 275, 252, 230, 209, 189, 170, 152, 135, 119, 104, 90, 77, 65, 54, 44, 35, 27, 20, 14, 9, 5, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],removeQueries = [0, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [324, 299, 275, 252, 230, 209, 189, 170, 152, 135, 119, 104, 90, 77, 65, 54, 44, 35, 27, 20, 14, 9, 5, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],removeQueries = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]) == [5400, 4900, 4000, 2700, 1000, 1000, 1000, 1000, 1000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],removeQueries = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]) == [5400, 4900, 4000, 2700, 1000, 1000, 1000, 1000, 1000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40],removeQueries = [3, 6, 0, 5, 1, 7, 2, 4]) == [130, 55, 55, 40, 40, 25, 25, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40],removeQueries = [3, 6, 0, 5, 1, 7, 2, 4]) == [130, 55, 55, 40, 40, 25, 25, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],removeQueries = [14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == [105, 104, 102, 99, 95, 90, 84, 77, 69, 60, 50, 39, 27, 14, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],removeQueries = [14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == [105, 104, 102, 99, 95, 90, 84, 77, 69, 60, 50, 39, 27, 14, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [4, 2, 6, 8, 0, 1, 3, 5, 7, 9]) == [400, 400, 270, 100, 100, 100, 100, 100, 100, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [4, 2, 6, 8, 0, 1, 3, 5, 7, 9]) == [400, 400, 270, 100, 100, 100, 100, 100, 100, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],removeQueries = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [380, 342, 306, 272, 240, 210, 182, 156, 132, 110, 90, 72, 56, 42, 30, 20, 12, 6, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],removeQueries = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [380, 342, 306, 272, 240, 210, 182, 156, 132, 110, 90, 72, 56, 42, 30, 20, 12, 6, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],removeQueries = [19, 0, 18, 1, 17, 2, 16, 3, 15, 4, 14, 5, 13, 6, 12, 7, 11, 8, 10, 9]) == [45, 45, 36, 36, 28, 28, 21, 21, 15, 15, 10, 10, 6, 6, 3, 3, 1, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],removeQueries = [19, 0, 18, 1, 17, 2, 16, 3, 15, 4, 14, 5, 13, 6, 12, 7, 11, 8, 10, 9]) == [45, 45, 36, 36, 28, 28, 21, 21, 15, 15, 10, 10, 6, 6, 3, 3, 1, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [190, 171, 153, 136, 120, 105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [190, 171, 153, 136, 120, 105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],removeQueries = [14, 0, 7, 2, 9, 4, 12, 6, 11, 3, 8, 13, 5, 10, 1]) == [196, 195, 132, 132, 96, 96, 44, 44, 27, 27, 27, 21, 21, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],removeQueries = [14, 0, 7, 2, 9, 4, 12, 6, 11, 3, 8, 13, 5, 10, 1]) == [196, 195, 132, 132, 96, 96, 44, 44, 27, 27, 27, 21, 21, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],removeQueries = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 3, 4, 0, 1]) == [65, 61, 58, 56, 55, 54, 52, 49, 45, 40, 40, 40, 40, 40, 40, 19, 19, 19, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],removeQueries = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 3, 4, 0, 1]) == [65, 61, 58, 56, 55, 54, 52, 49, 45, 40, 40, 40, 40, 40, 40, 19, 19, 19, 9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000],removeQueries = [2, 0, 1, 3]) == [2000000000, 1000000000, 1000000000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000],removeQueries = [2, 0, 1, 3]) == [2000000000, 1000000000, 1000000000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],removeQueries = [4, 3, 2, 1, 0]) == [1000, 600, 300, 100, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],removeQueries = [4, 3, 2, 1, 0]) == [1000, 600, 300, 100, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [5, 2, 8, 0, 4, 7, 1, 9, 6, 3]) == [340, 340, 150, 150, 150, 100, 100, 70, 40, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [5, 2, 8, 0, 4, 7, 1, 9, 6, 3]) == [340, 340, 150, 150, 150, 100, 100, 70, 40, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [5, 2, 8, 1, 7, 4, 3, 9, 6, 0]) == [340, 340, 150, 150, 100, 100, 100, 70, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [5, 2, 8, 1, 7, 4, 3, 9, 6, 0]) == [340, 340, 150, 150, 100, 100, 100, 70, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [190, 153, 120, 91, 66, 45, 28, 19, 19, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [190, 153, 120, 91, 66, 45, 28, 19, 19, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],removeQueries = [14, 1, 2, 12, 0, 3, 4, 13, 5, 6, 11, 7, 8, 9, 10]) == [10500, 10200, 9900, 7200, 7200, 6800, 6300, 6300, 5700, 5000, 3800, 3000, 2100, 1100, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],removeQueries = [14, 1, 2, 12, 0, 3, 4, 13, 5, 6, 11, 7, 8, 9, 10]) == [10500, 10200, 9900, 7200, 7200, 6800, 6300, 6300, 5700, 5000, 3800, 3000, 2100, 1100, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],removeQueries = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],removeQueries = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],removeQueries = [19, 9, 18, 8, 17, 7, 16, 6, 15, 5, 14, 4, 13, 3, 12, 2, 11, 1, 10, 0]) == [1900, 1350, 1160, 1160, 980, 980, 810, 810, 650, 650, 500, 500, 360, 360, 230, 230, 110, 110, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],removeQueries = [19, 9, 18, 8, 17, 7, 16, 6, 15, 5, 14, 4, 13, 3, 12, 2, 11, 1, 10, 0]) == [1900, 1350, 1160, 1160, 980, 980, 810, 810, 650, 650, 500, 500, 360, 360, 230, 230, 110, 110, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 41, 59, 26, 53, 58, 97, 93, 23, 84, 62, 64, 33, 83, 27, 95, 28, 84, 19, 71],removeQueries = [10, 18, 8, 12, 17, 19, 16, 7, 5, 0, 14, 2, 15, 9, 6, 13, 3, 4, 11, 1]) == [565, 565, 458, 458, 458, 458, 458, 365, 210, 205, 179, 97, 97, 97, 83, 79, 64, 64, 41, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 41, 59, 26, 53, 58, 97, 93, 23, 84, 62, 64, 33, 83, 27, 95, 28, 84, 19, 71],removeQueries = [10, 18, 8, 12, 17, 19, 16, 7, 5, 0, 14, 2, 15, 9, 6, 13, 3, 4, 11, 1]) == [565, 565, 458, 458, 458, 458, 458, 365, 210, 205, 179, 97, 97, 97, 83, 79, 64, 64, 41, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1, 3, 4, 2, 3, 4, 1, 5, 6, 7, 8, 9, 10],removeQueries = [1, 3, 5, 7, 9, 11, 13, 0, 2, 4, 6, 8, 10, 12]) == [62, 55, 50, 45, 34, 19, 9, 9, 9, 9, 9, 9, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1, 3, 4, 2, 3, 4, 1, 5, 6, 7, 8, 9, 10],removeQueries = [1, 3, 5, 7, 9, 11, 13, 0, 2, 4, 6, 8, 10, 12]) == [62, 55, 50, 45, 34, 19, 9, 9, 9, 9, 9, 9, 9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]) == [540, 490, 400, 270, 100, 100, 100, 100, 100, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]) == [540, 490, 400, 270, 100, 100, 100, 100, 100, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000],removeQueries = [4, 2, 0, 3, 1]) == [10000000000, 4000000000, 4000000000, 2000000000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000],removeQueries = [4, 2, 0, 3, 1]) == [10000000000, 4000000000, 4000000000, 2000000000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18]) == [190, 153, 120, 91, 66, 45, 28, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18]) == [190, 153, 120, 91, 66, 45, 28, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [5, 3, 7, 1, 9, 4, 0, 6, 8, 2]) == [340, 340, 190, 190, 90, 90, 90, 90, 30, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [5, 3, 7, 1, 9, 4, 0, 6, 8, 2]) == [340, 340, 190, 190, 90, 90, 90, 90, 30, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],removeQueries = [4, 2, 6, 8, 0, 3, 5, 7, 9, 1]) == [4000, 4000, 2700, 1000, 1000, 1000, 1000, 1000, 200, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],removeQueries = [4, 2, 6, 8, 0, 3, 5, 7, 9, 1]) == [4000, 4000, 2700, 1000, 1000, 1000, 1000, 1000, 200, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6],removeQueries = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [89, 85, 77, 74, 72, 69, 60, 53, 44, 39, 36, 31, 25, 23, 14, 9, 8, 4, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6],removeQueries = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [89, 85, 77, 74, 72, 69, 60, 53, 44, 39, 36, 31, 25, 23, 14, 9, 8, 4, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]) == [190, 153, 120, 91, 66, 45, 28, 19, 19, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]) == [190, 153, 120, 91, 66, 45, 28, 19, 19, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],removeQueries = [2, 4, 6, 8, 10, 12, 14, 0, 1, 3, 5, 7, 9, 11, 13]) == [11400, 10500, 9200, 7500, 5400, 2900, 1400, 1400, 1400, 1400, 1400, 1400, 1400, 1400, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],removeQueries = [2, 4, 6, 8, 10, 12, 14, 0, 1, 3, 5, 7, 9, 11, 13]) == [11400, 10500, 9200, 7500, 5400, 2900, 1400, 1400, 1400, 1400, 1400, 1400, 1400, 1400, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],removeQueries = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1996093750, 1992187500, 1984375000, 1968750000, 1937500000, 1875000000, 1750000000, 1500000000, 1000000000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],removeQueries = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1996093750, 1992187500, 1984375000, 1968750000, 1937500000, 1875000000, 1750000000, 1500000000, 1000000000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [46, 39, 34, 31, 30, 28, 24, 18, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [46, 39, 34, 31, 30, 28, 24, 18, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 3, 9, 8, 7, 2, 6],removeQueries = [2, 5, 0, 3, 4, 8, 6, 7, 1]) == [35, 15, 15, 15, 15, 9, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 3, 9, 8, 7, 2, 6],removeQueries = [2, 5, 0, 3, 4, 8, 6, 7, 1]) == [35, 15, 15, 15, 15, 9, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [190, 171, 153, 136, 120, 105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [190, 171, 153, 136, 120, 105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [4, 8, 3, 7, 2, 6, 1, 5, 0]) == [30, 30, 24, 24, 17, 17, 9, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [4, 8, 3, 7, 2, 6, 1, 5, 0]) == [30, 30, 24, 24, 17, 17, 9, 9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [45, 36, 28, 21, 15, 10, 6, 3, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [45, 36, 28, 21, 15, 10, 6, 3, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [144, 144, 144, 144, 144, 144, 144, 144, 144, 144, 144, 132, 119, 105, 90, 74, 57, 39, 20, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [144, 144, 144, 144, 144, 144, 144, 144, 144, 144, 144, 132, 119, 105, 90, 74, 57, 39, 20, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [5, 7, 3, 1, 9, 0, 8, 6, 2, 4]) == [340, 190, 190, 190, 90, 90, 70, 50, 50, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [5, 7, 3, 1, 9, 0, 8, 6, 2, 4]) == [340, 190, 190, 190, 90, 90, 70, 50, 50, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],removeQueries = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9000000000, 8000000000, 7000000000, 6000000000, 5000000000, 4000000000, 3000000000, 2000000000, 1000000000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],removeQueries = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9000000000, 8000000000, 7000000000, 6000000000, 5000000000, 4000000000, 3000000000, 2000000000, 1000000000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],removeQueries = [5, 0, 4, 9, 2, 8, 6, 3, 7, 1]) == [25, 24, 22, 21, 16, 11, 10, 10, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],removeQueries = [5, 0, 4, 9, 2, 8, 6, 3, 7, 1]) == [25, 24, 22, 21, 16, 11, 10, 10, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],removeQueries = [14, 1, 2, 12, 0, 3, 4, 13, 5, 6, 11, 7, 8, 9, 10]) == [105, 102, 99, 72, 72, 68, 63, 63, 57, 50, 38, 30, 21, 11, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],removeQueries = [14, 1, 2, 12, 0, 3, 4, 13, 5, 6, 11, 7, 8, 9, 10]) == [105, 102, 99, 72, 72, 68, 63, 63, 57, 50, 38, 30, 21, 11, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],removeQueries = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9000000000, 8000000000, 7000000000, 6000000000, 5000000000, 4000000000, 3000000000, 2000000000, 1000000000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],removeQueries = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9000000000, 8000000000, 7000000000, 6000000000, 5000000000, 4000000000, 3000000000, 2000000000, 1000000000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],removeQueries = [7, 14, 0, 13, 1, 12, 2, 11, 3, 10, 4, 9, 5, 8, 6]) == [840, 690, 690, 550, 550, 420, 420, 300, 300, 190, 190, 130, 90, 70, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],removeQueries = [7, 14, 0, 13, 1, 12, 2, 11, 3, 10, 4, 9, 5, 8, 6]) == [840, 690, 690, 550, 550, 420, 420, 300, 300, 190, 190, 130, 90, 70, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],removeQueries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18]) == [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],removeQueries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18]) == [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035, 30517, 15258, 7629, 3814, 1907],removeQueries = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1999996181, 1999992367, 1999984738, 1999969480, 1999938963, 1999877928, 1999755858, 1999511718, 1999023437, 1998046875, 1996093750, 1992187500, 1984375000, 1968750000, 1937500000, 1875000000, 1750000000, 1500000000, 1000000000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035, 30517, 15258, 7629, 3814, 1907],removeQueries = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1999996181, 1999992367, 1999984738, 1999969480, 1999938963, 1999877928, 1999755858, 1999511718, 1999023437, 1998046875, 1996093750, 1992187500, 1984375000, 1968750000, 1937500000, 1875000000, 1750000000, 1500000000, 1000000000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],removeQueries = [11, 5, 3, 7, 9, 1, 8, 10, 4, 2, 6, 0]) == [6600, 4500, 4500, 3000, 1100, 1100, 1100, 700, 700, 700, 100, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],removeQueries = [11, 5, 3, 7, 9, 1, 8, 10, 4, 2, 6, 0]) == [6600, 4500, 4500, 3000, 1100, 1100, 1100, 700, 700, 700, 100, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8]) == [36, 28, 21, 15, 10, 6, 3, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8]) == [36, 28, 21, 15, 10, 6, 3, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 8, 1, 7, 2, 6, 3, 5, 4]) == [36, 35, 27, 25, 18, 15, 9, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 8, 1, 7, 2, 6, 3, 5, 4]) == [36, 35, 27, 25, 18, 15, 9, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],removeQueries = [0, 2, 4, 6, 8, 10, 12, 14, 1, 3, 5, 7, 9, 11, 13]) == [54, 50, 44, 37, 29, 20, 10, 5, 5, 5, 5, 5, 5, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],removeQueries = [0, 2, 4, 6, 8, 10, 12, 14, 1, 3, 5, 7, 9, 11, 13]) == [54, 50, 44, 37, 29, 20, 10, 5, 5, 5, 5, 5, 5, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],removeQueries = [7, 15, 3, 11, 13, 5, 9, 1, 12, 14, 8, 10, 6, 2, 4, 0]) == [892, 777, 777, 339, 327, 327, 303, 114, 114, 110, 110, 106, 104, 104, 100, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],removeQueries = [7, 15, 3, 11, 13, 5, 9, 1, 12, 14, 8, 10, 6, 2, 4, 0]) == [892, 777, 777, 339, 327, 327, 303, 114, 114, 110, 110, 106, 104, 104, 100, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],removeQueries = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],removeQueries = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],removeQueries = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],removeQueries = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 8, 1, 7, 2, 6, 3, 5, 4]) == [36, 35, 27, 25, 18, 15, 9, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 8, 1, 7, 2, 6, 3, 5, 4]) == [36, 35, 27, 25, 18, 15, 9, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [190, 171, 153, 136, 120, 105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [190, 171, 153, 136, 120, 105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [209, 206, 204, 199, 195, 189, 182, 174, 165, 155, 144, 132, 119, 105, 90, 74, 57, 39, 20, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [209, 206, 204, 199, 195, 189, 182, 174, 165, 155, 144, 132, 119, 105, 90, 74, 57, 39, 20, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [15, 10, 5, 0, 19, 14, 9, 4, 18, 13, 8, 3, 17, 12, 7, 2, 16, 11, 6, 1]) == [120, 74, 74, 74, 54, 54, 54, 54, 39, 35, 35, 35, 25, 17, 17, 17, 12, 7, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [15, 10, 5, 0, 19, 14, 9, 4, 18, 13, 8, 3, 17, 12, 7, 2, 16, 11, 6, 1]) == [120, 74, 74, 74, 54, 54, 54, 54, 39, 35, 35, 35, 25, 17, 17, 17, 12, 7, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [10, 5, 15, 2, 18, 8, 0, 17, 3, 14, 9, 11, 7, 1, 12, 6, 13, 4, 16, 19]) == [10, 9, 5, 4, 4, 4, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [10, 5, 15, 2, 18, 8, 0, 17, 3, 14, 9, 11, 7, 1, 12, 6, 13, 4, 16, 19]) == [10, 9, 5, 4, 4, 4, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6],removeQueries = [10, 2, 16, 14, 18, 6, 8, 12, 4, 1, 13, 7, 15, 3, 9, 19, 11, 5, 17, 0]) == [47, 47, 31, 31, 31, 17, 17, 15, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6],removeQueries = [10, 2, 16, 14, 18, 6, 8, 12, 4, 1, 13, 7, 15, 3, 9, 19, 11, 5, 17, 0]) == [47, 47, 31, 31, 31, 17, 17, 15, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 2, 5, 4, 6, 3, 9, 8, 1, 0, 8, 1, 0, 8, 1, 0, 8, 1, 0, 8],removeQueries = [15, 11, 5, 13, 3, 19, 9, 17, 7, 1, 0, 12, 4, 8, 16, 2, 14, 6, 10, 18]) == [54, 53, 26, 26, 26, 26, 18, 18, 14, 9, 9, 9, 9, 9, 9, 9, 9, 8, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 2, 5, 4, 6, 3, 9, 8, 1, 0, 8, 1, 0, 8, 1, 0, 8, 1, 0, 8],removeQueries = [15, 11, 5, 13, 3, 19, 9, 17, 7, 1, 0, 12, 4, 8, 16, 2, 14, 6, 10, 18]) == [54, 53, 26, 26, 26, 26, 18, 18, 14, 9, 9, 9, 9, 9, 9, 9, 9, 8, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [5, 7, 9, 1, 3, 8, 2, 6, 4, 0]) == [340, 190, 150, 120, 90, 70, 70, 50, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [5, 7, 9, 1, 3, 8, 2, 6, 4, 0]) == [340, 190, 150, 120, 90, 70, 70, 50, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],removeQueries = [29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [435, 406, 378, 351, 325, 300, 276, 253, 231, 210, 190, 171, 153, 136, 120, 105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],removeQueries = [29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [435, 406, 378, 351, 325, 300, 276, 253, 231, 210, 190, 171, 153, 136, 120, 105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],removeQueries = [7, 3, 9, 13, 5, 11, 1, 6, 2, 14, 8, 0, 12, 10, 4]) == [840, 840, 650, 360, 360, 150, 150, 150, 150, 130, 130, 130, 110, 50, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],removeQueries = [7, 3, 9, 13, 5, 11, 1, 6, 2, 14, 8, 0, 12, 10, 4]) == [840, 840, 650, 360, 360, 150, 150, 150, 150, 130, 130, 130, 110, 50, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 2, 3, 1, 4, 6, 8, 7, 9, 10],removeQueries = [4, 0, 3, 2, 5, 1, 8, 9, 7, 6]) == [40, 40, 40, 40, 34, 34, 15, 15, 8, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 2, 3, 1, 4, 6, 8, 7, 9, 10],removeQueries = [4, 0, 3, 2, 5, 1, 8, 9, 7, 6]) == [40, 40, 40, 40, 34, 34, 15, 15, 8, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 2, 4, 6, 8, 1, 3, 5, 7]) == [36, 21, 10, 8, 8, 6, 4, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 2, 4, 6, 8, 1, 3, 5, 7]) == [36, 21, 10, 8, 8, 6, 4, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],removeQueries = [0, 1, 2, 3, 4]) == [4000000000, 3000000000, 2000000000, 1000000000, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],removeQueries = [0, 1, 2, 3, 4]) == [4000000000, 3000000000, 2000000000, 1000000000, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],removeQueries = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1225, 1176, 1128, 1081, 1035, 990, 946, 903, 861, 820, 780, 741, 703, 666, 630, 595, 561, 528, 496, 465, 435, 406, 378, 351, 325, 300, 276, 253, 231, 210, 190, 171, 153, 136, 120, 105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],removeQueries = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1225, 1176, 1128, 1081, 1035, 990, 946, 903, 861, 820, 780, 741, 703, 666, 630, 595, 561, 528, 496, 465, 435, 406, 378, 351, 325, 300, 276, 253, 231, 210, 190, 171, 153, 136, 120, 105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [4, 2, 7, 5, 8, 1, 0, 9, 3, 6]) == [400, 400, 190, 190, 100, 100, 100, 70, 70, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [4, 2, 7, 5, 8, 1, 0, 9, 3, 6]) == [400, 400, 190, 190, 100, 100, 100, 70, 70, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],removeQueries = [5, 7, 3, 9, 1, 6, 0, 8, 2, 4]) == [64, 36, 36, 17, 17, 17, 17, 9, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],removeQueries = [5, 7, 3, 9, 1, 6, 0, 8, 2, 4]) == [64, 36, 36, 17, 17, 17, 17, 9, 9, 0]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 2, 5, 6, 1],removeQueries = [0, 3, 2, 4, 1]) == [14, 7, 2, 2, 0]
    assert candidate(nums = [5, 1, 4, 3, 2],removeQueries = [2, 0, 4, 1, 3]) == [6, 5, 3, 3, 0]
    assert candidate(nums = [1000000000, 1000000000, 1000000000],removeQueries = [0, 1, 2]) == [2000000000, 1000000000, 0]
    assert candidate(nums = [10, 20, 30, 40, 50],removeQueries = [4, 3, 2, 1, 0]) == [100, 60, 30, 10, 0]
    assert candidate(nums = [5, 1, 4, 3],removeQueries = [1, 2, 0, 3]) == [7, 5, 3, 0]
    assert candidate(nums = [3, 2, 11, 1],removeQueries = [3, 2, 1, 0]) == [16, 5, 3, 0]
    assert candidate(nums = [10, 20, 30, 40, 50],removeQueries = [0, 1, 2, 3, 4]) == [140, 120, 90, 50, 0]
    assert candidate(nums = [10, 20, 30, 40, 50],removeQueries = [2, 4, 0, 1, 3]) == [90, 40, 40, 40, 0]
    assert candidate(nums = [5, 2, 3, 1, 4],removeQueries = [2, 0, 4, 3, 1]) == [7, 5, 2, 2, 0]
    assert candidate(nums = [1, 1, 1, 1, 1],removeQueries = [0, 1, 2, 3, 4]) == [4, 3, 2, 1, 0]
    assert candidate(nums = [1000000000, 1000000000, 1000000000],removeQueries = [0, 1, 2]) == [2000000000, 1000000000, 0]
    assert candidate(nums = [5, 1, 3, 2, 4],removeQueries = [2, 0, 1, 3, 4]) == [6, 6, 6, 4, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],removeQueries = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [45, 36, 28, 21, 15, 10, 6, 3, 1, 0]
    assert candidate(nums = [5, 2, 3, 1, 4],removeQueries = [2, 0, 3, 4, 1]) == [7, 5, 4, 2, 0]
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9000000000, 8000000000, 7000000000, 6000000000, 5000000000, 4000000000, 3000000000, 2000000000, 1000000000, 0]
    assert candidate(nums = [10, 100, 1000, 10000, 100000, 1000000],removeQueries = [5, 4, 3, 2, 1, 0]) == [111110, 11110, 1110, 110, 10, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],removeQueries = [24, 12, 6, 0, 2, 10, 14, 20, 22, 8, 16, 18, 4, 15, 11, 13, 7, 19, 17, 3, 5, 9, 1, 21, 23, 25]) == [300, 209, 209, 209, 209, 209, 180, 90, 90, 90, 57, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 0]
    assert candidate(nums = [9, 1, 5, 3, 2, 4, 8, 6, 7, 10],removeQueries = [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]) == [46, 36, 35, 28, 23, 17, 14, 6, 4, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],removeQueries = [0, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [324, 299, 275, 252, 230, 209, 189, 170, 152, 135, 119, 104, 90, 77, 65, 54, 44, 35, 27, 20, 14, 9, 5, 2, 0]
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],removeQueries = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]) == [5400, 4900, 4000, 2700, 1000, 1000, 1000, 1000, 1000, 0]
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40],removeQueries = [3, 6, 0, 5, 1, 7, 2, 4]) == [130, 55, 55, 40, 40, 25, 25, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],removeQueries = [14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == [105, 104, 102, 99, 95, 90, 84, 77, 69, 60, 50, 39, 27, 14, 0]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [4, 2, 6, 8, 0, 1, 3, 5, 7, 9]) == [400, 400, 270, 100, 100, 100, 100, 100, 100, 0]
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],removeQueries = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [380, 342, 306, 272, 240, 210, 182, 156, 132, 110, 90, 72, 56, 42, 30, 20, 12, 6, 2, 0]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],removeQueries = [19, 0, 18, 1, 17, 2, 16, 3, 15, 4, 14, 5, 13, 6, 12, 7, 11, 8, 10, 9]) == [45, 45, 36, 36, 28, 28, 21, 21, 15, 15, 10, 10, 6, 6, 3, 3, 1, 1, 0, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [190, 171, 153, 136, 120, 105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],removeQueries = [14, 0, 7, 2, 9, 4, 12, 6, 11, 3, 8, 13, 5, 10, 1]) == [196, 195, 132, 132, 96, 96, 44, 44, 27, 27, 27, 21, 21, 3, 0]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],removeQueries = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 3, 4, 0, 1]) == [65, 61, 58, 56, 55, 54, 52, 49, 45, 40, 40, 40, 40, 40, 40, 19, 19, 19, 9, 0]
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000],removeQueries = [2, 0, 1, 3]) == [2000000000, 1000000000, 1000000000, 0]
    assert candidate(nums = [100, 200, 300, 400, 500],removeQueries = [4, 3, 2, 1, 0]) == [1000, 600, 300, 100, 0]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [5, 2, 8, 0, 4, 7, 1, 9, 6, 3]) == [340, 340, 150, 150, 150, 100, 100, 70, 40, 0]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [5, 2, 8, 1, 7, 4, 3, 9, 6, 0]) == [340, 340, 150, 150, 100, 100, 100, 70, 10, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [190, 153, 120, 91, 66, 45, 28, 19, 19, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 0]
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],removeQueries = [14, 1, 2, 12, 0, 3, 4, 13, 5, 6, 11, 7, 8, 9, 10]) == [10500, 10200, 9900, 7200, 7200, 6800, 6300, 6300, 5700, 5000, 3800, 3000, 2100, 1100, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],removeQueries = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],removeQueries = [19, 9, 18, 8, 17, 7, 16, 6, 15, 5, 14, 4, 13, 3, 12, 2, 11, 1, 10, 0]) == [1900, 1350, 1160, 1160, 980, 980, 810, 810, 650, 650, 500, 500, 360, 360, 230, 230, 110, 110, 10, 0]
    assert candidate(nums = [31, 41, 59, 26, 53, 58, 97, 93, 23, 84, 62, 64, 33, 83, 27, 95, 28, 84, 19, 71],removeQueries = [10, 18, 8, 12, 17, 19, 16, 7, 5, 0, 14, 2, 15, 9, 6, 13, 3, 4, 11, 1]) == [565, 565, 458, 458, 458, 458, 458, 365, 210, 205, 179, 97, 97, 97, 83, 79, 64, 64, 41, 0]
    assert candidate(nums = [2, 1, 3, 4, 2, 3, 4, 1, 5, 6, 7, 8, 9, 10],removeQueries = [1, 3, 5, 7, 9, 11, 13, 0, 2, 4, 6, 8, 10, 12]) == [62, 55, 50, 45, 34, 19, 9, 9, 9, 9, 9, 9, 9, 0]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]) == [540, 490, 400, 270, 100, 100, 100, 100, 100, 0]
    assert candidate(nums = [1000000000, 2000000000, 3000000000, 4000000000, 5000000000],removeQueries = [4, 2, 0, 3, 1]) == [10000000000, 4000000000, 4000000000, 2000000000, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18]) == [190, 153, 120, 91, 66, 45, 28, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 0]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [5, 3, 7, 1, 9, 4, 0, 6, 8, 2]) == [340, 340, 190, 190, 90, 90, 90, 90, 30, 0]
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],removeQueries = [4, 2, 6, 8, 0, 3, 5, 7, 9, 1]) == [4000, 4000, 2700, 1000, 1000, 1000, 1000, 1000, 200, 0]
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6],removeQueries = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [89, 85, 77, 74, 72, 69, 60, 53, 44, 39, 36, 31, 25, 23, 14, 9, 8, 4, 3, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 18, 16, 14, 12, 10, 8, 6, 4, 2, 0]) == [190, 153, 120, 91, 66, 45, 28, 19, 19, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 0]
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],removeQueries = [2, 4, 6, 8, 10, 12, 14, 0, 1, 3, 5, 7, 9, 11, 13]) == [11400, 10500, 9200, 7500, 5400, 2900, 1400, 1400, 1400, 1400, 1400, 1400, 1400, 1400, 0]
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125],removeQueries = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1996093750, 1992187500, 1984375000, 1968750000, 1937500000, 1875000000, 1750000000, 1500000000, 1000000000, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [19, 17, 15, 13, 11, 9, 7, 5, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [46, 39, 34, 31, 30, 28, 24, 18, 10, 0]
    assert candidate(nums = [5, 1, 4, 3, 9, 8, 7, 2, 6],removeQueries = [2, 5, 0, 3, 4, 8, 6, 7, 1]) == [35, 15, 15, 15, 15, 9, 2, 1, 0]
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [190, 171, 153, 136, 120, 105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [4, 8, 3, 7, 2, 6, 1, 5, 0]) == [30, 30, 24, 24, 17, 17, 9, 9, 0]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [45, 36, 28, 21, 15, 10, 6, 3, 1, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [144, 144, 144, 144, 144, 144, 144, 144, 144, 144, 144, 132, 119, 105, 90, 74, 57, 39, 20, 0]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [5, 7, 3, 1, 9, 0, 8, 6, 2, 4]) == [340, 190, 190, 190, 90, 90, 70, 50, 50, 0]
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],removeQueries = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9000000000, 8000000000, 7000000000, 6000000000, 5000000000, 4000000000, 3000000000, 2000000000, 1000000000, 0]
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],removeQueries = [5, 0, 4, 9, 2, 8, 6, 3, 7, 1]) == [25, 24, 22, 21, 16, 11, 10, 10, 10, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],removeQueries = [14, 1, 2, 12, 0, 3, 4, 13, 5, 6, 11, 7, 8, 9, 10]) == [105, 102, 99, 72, 72, 68, 63, 63, 57, 50, 38, 30, 21, 11, 0]
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],removeQueries = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9000000000, 8000000000, 7000000000, 6000000000, 5000000000, 4000000000, 3000000000, 2000000000, 1000000000, 0]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],removeQueries = [7, 14, 0, 13, 1, 12, 2, 11, 3, 10, 4, 9, 5, 8, 6]) == [840, 690, 690, 550, 550, 420, 420, 300, 300, 190, 190, 130, 90, 70, 0]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],removeQueries = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18]) == [90, 80, 70, 60, 50, 40, 30, 20, 10, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125, 976562, 488281, 244140, 122070, 61035, 30517, 15258, 7629, 3814, 1907],removeQueries = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1999996181, 1999992367, 1999984738, 1999969480, 1999938963, 1999877928, 1999755858, 1999511718, 1999023437, 1998046875, 1996093750, 1992187500, 1984375000, 1968750000, 1937500000, 1875000000, 1750000000, 1500000000, 1000000000, 0]
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],removeQueries = [11, 5, 3, 7, 9, 1, 8, 10, 4, 2, 6, 0]) == [6600, 4500, 4500, 3000, 1100, 1100, 1100, 700, 700, 700, 100, 0]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8]) == [36, 28, 21, 15, 10, 6, 3, 1, 0]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 8, 1, 7, 2, 6, 3, 5, 4]) == [36, 35, 27, 25, 18, 15, 9, 5, 0]
    assert candidate(nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5],removeQueries = [0, 2, 4, 6, 8, 10, 12, 14, 1, 3, 5, 7, 9, 11, 13]) == [54, 50, 44, 37, 29, 20, 10, 5, 5, 5, 5, 5, 5, 5, 0]
    assert candidate(nums = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],removeQueries = [7, 15, 3, 11, 13, 5, 9, 1, 12, 14, 8, 10, 6, 2, 4, 0]) == [892, 777, 777, 339, 327, 327, 303, 114, 114, 110, 110, 106, 104, 104, 100, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],removeQueries = [14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],removeQueries = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 0]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 8, 1, 7, 2, 6, 3, 5, 4]) == [36, 35, 27, 25, 18, 15, 9, 5, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [190, 171, 153, 136, 120, 105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]
    assert candidate(nums = [1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == [209, 206, 204, 199, 195, 189, 182, 174, 165, 155, 144, 132, 119, 105, 90, 74, 57, 39, 20, 0]
    assert candidate(nums = [5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],removeQueries = [15, 10, 5, 0, 19, 14, 9, 4, 18, 13, 8, 3, 17, 12, 7, 2, 16, 11, 6, 1]) == [120, 74, 74, 74, 54, 54, 54, 54, 39, 35, 35, 35, 25, 17, 17, 17, 12, 7, 4, 0]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],removeQueries = [10, 5, 15, 2, 18, 8, 0, 17, 3, 14, 9, 11, 7, 1, 12, 6, 13, 4, 16, 19]) == [10, 9, 5, 4, 4, 4, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0]
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6, 5, 3, 5, 9, 2, 6],removeQueries = [10, 2, 16, 14, 18, 6, 8, 12, 4, 1, 13, 7, 15, 3, 9, 19, 11, 5, 17, 0]) == [47, 47, 31, 31, 31, 17, 17, 15, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 3, 0]
    assert candidate(nums = [7, 2, 5, 4, 6, 3, 9, 8, 1, 0, 8, 1, 0, 8, 1, 0, 8, 1, 0, 8],removeQueries = [15, 11, 5, 13, 3, 19, 9, 17, 7, 1, 0, 12, 4, 8, 16, 2, 14, 6, 10, 18]) == [54, 53, 26, 26, 26, 26, 18, 18, 14, 9, 9, 9, 9, 9, 9, 9, 9, 8, 0, 0]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [5, 7, 9, 1, 3, 8, 2, 6, 4, 0]) == [340, 190, 150, 120, 90, 70, 70, 50, 10, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],removeQueries = [29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [435, 406, 378, 351, 325, 300, 276, 253, 231, 210, 190, 171, 153, 136, 120, 105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],removeQueries = [7, 3, 9, 13, 5, 11, 1, 6, 2, 14, 8, 0, 12, 10, 4]) == [840, 840, 650, 360, 360, 150, 150, 150, 150, 130, 130, 130, 110, 50, 0]
    assert candidate(nums = [5, 2, 3, 1, 4, 6, 8, 7, 9, 10],removeQueries = [4, 0, 3, 2, 5, 1, 8, 9, 7, 6]) == [40, 40, 40, 40, 34, 34, 15, 15, 8, 0]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],removeQueries = [0, 2, 4, 6, 8, 1, 3, 5, 7]) == [36, 21, 10, 8, 8, 6, 4, 2, 0]
    assert candidate(nums = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],removeQueries = [0, 1, 2, 3, 4]) == [4000000000, 3000000000, 2000000000, 1000000000, 0]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],removeQueries = [49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1225, 1176, 1128, 1081, 1035, 990, 946, 903, 861, 820, 780, 741, 703, 666, 630, 595, 561, 528, 496, 465, 435, 406, 378, 351, 325, 300, 276, 253, 231, 210, 190, 171, 153, 136, 120, 105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1, 0]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],removeQueries = [4, 2, 7, 5, 8, 1, 0, 9, 3, 6]) == [400, 400, 190, 190, 100, 100, 100, 70, 70, 0]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],removeQueries = [5, 7, 3, 9, 1, 6, 0, 8, 2, 4]) == [64, 36, 36, 17, 17, 17, 17, 9, 9, 0]


