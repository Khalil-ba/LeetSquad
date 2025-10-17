def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],indexDifference = 2,valueDifference = 6) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],indexDifference = 2,valueDifference = 6) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0],indexDifference = 0,valueDifference = 0) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0],indexDifference = 0,valueDifference = 0) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],indexDifference = 1,valueDifference = 25) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],indexDifference = 1,valueDifference = 25) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0],indexDifference = 3,valueDifference = 1) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0],indexDifference = 3,valueDifference = 1) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0],indexDifference = 1,valueDifference = 1) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0],indexDifference = 1,valueDifference = 1) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 15, 20, 25],indexDifference = 2,valueDifference = 10) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 15, 20, 25],indexDifference = 2,valueDifference = 10) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 2, 3, 1, 5],indexDifference = 1,valueDifference = 2) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 2, 3, 1, 5],indexDifference = 1,valueDifference = 2) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],indexDifference = 3,valueDifference = 4) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],indexDifference = 3,valueDifference = 4) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 46, 47, 48, 49, 50],indexDifference = 2,valueDifference = 5) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 46, 47, 48, 49, 50],indexDifference = 2,valueDifference = 5) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 2, 3, 4, 5],indexDifference = 1,valueDifference = 2) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 2, 3, 4, 5],indexDifference = 1,valueDifference = 2) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10],indexDifference = 2,valueDifference = 15) == [0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10],indexDifference = 2,valueDifference = 15) == [0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3],indexDifference = 2,valueDifference = 4) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3],indexDifference = 2,valueDifference = 4) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDifference = 5,valueDifference = 5) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDifference = 5,valueDifference = 5) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 1],indexDifference = 0,valueDifference = 0) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 1],indexDifference = 0,valueDifference = 0) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10],indexDifference = 2,valueDifference = 30) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10],indexDifference = 2,valueDifference = 30) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 5, 7, 9, 11],indexDifference = 1,valueDifference = 2) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 5, 7, 9, 11],indexDifference = 1,valueDifference = 2) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],indexDifference = 1,valueDifference = 1) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],indexDifference = 1,valueDifference = 1) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3],indexDifference = 0,valueDifference = 0) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3],indexDifference = 0,valueDifference = 0) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],indexDifference = 3,valueDifference = 15) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],indexDifference = 3,valueDifference = 15) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],indexDifference = 3,valueDifference = 20) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],indexDifference = 3,valueDifference = 20) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],indexDifference = 2,valueDifference = 25) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],indexDifference = 2,valueDifference = 25) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10],indexDifference = 2,valueDifference = 25) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10],indexDifference = 2,valueDifference = 25) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],indexDifference = 3,valueDifference = 6) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],indexDifference = 3,valueDifference = 6) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 1, 4, 1],indexDifference = 2,valueDifference = 4) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 1, 4, 1],indexDifference = 2,valueDifference = 4) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1],indexDifference = 2,valueDifference = 6) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1],indexDifference = 2,valueDifference = 6) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 8, 8, 8],indexDifference = 0,valueDifference = 0) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 8, 8, 8],indexDifference = 0,valueDifference = 0) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1],indexDifference = 3,valueDifference = 4) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1],indexDifference = 3,valueDifference = 4) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 2, 3, 4, 1],indexDifference = 1,valueDifference = 2) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 2, 3, 4, 1],indexDifference = 1,valueDifference = 2) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 5,valueDifference = 1) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 5,valueDifference = 1) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],indexDifference = 15,valueDifference = 50) == [0, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],indexDifference = 15,valueDifference = 50) == [0, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 4,valueDifference = 45) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 4,valueDifference = 45) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],indexDifference = 3,valueDifference = 5) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],indexDifference = 3,valueDifference = 5) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],indexDifference = 7,valueDifference = 40) == [0, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],indexDifference = 7,valueDifference = 40) == [0, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],indexDifference = 3,valueDifference = 6) == [0, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],indexDifference = 3,valueDifference = 6) == [0, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDifference = 10,valueDifference = 10) == [0, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDifference = 10,valueDifference = 10) == [0, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDifference = 1,valueDifference = 1) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDifference = 1,valueDifference = 1) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],indexDifference = 5,valueDifference = 15) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],indexDifference = 5,valueDifference = 15) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10],indexDifference = 2,valueDifference = 4) == [2, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10],indexDifference = 2,valueDifference = 4) == [2, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],indexDifference = 4,valueDifference = 30) == [0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],indexDifference = 4,valueDifference = 30) == [0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11],indexDifference = 5,valueDifference = 10) == [0, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11],indexDifference = 5,valueDifference = 10) == [0, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],indexDifference = 2,valueDifference = 1) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],indexDifference = 2,valueDifference = 1) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],indexDifference = 5,valueDifference = 5) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],indexDifference = 5,valueDifference = 5) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 20, 20, 20, 20, 30, 30, 30, 30, 40, 40],indexDifference = 2,valueDifference = 10) == [0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 20, 20, 20, 20, 30, 30, 30, 30, 40, 40],indexDifference = 2,valueDifference = 10) == [0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 100, 50, 100, 50, 100, 50, 100],indexDifference = 2,valueDifference = 40) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 100, 50, 100, 50, 100, 50, 100],indexDifference = 2,valueDifference = 40) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDifference = 5,valueDifference = 10) == [0, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDifference = 5,valueDifference = 10) == [0, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],indexDifference = 5,valueDifference = 10) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],indexDifference = 5,valueDifference = 10) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1, 3, 5, 7, 9, 11],indexDifference = 6,valueDifference = 6) == [3, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1, 3, 5, 7, 9, 11],indexDifference = 6,valueDifference = 6) == [3, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],indexDifference = 2,valueDifference = 35) == [0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],indexDifference = 2,valueDifference = 35) == [0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31],indexDifference = 10,valueDifference = 5) == [0, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31],indexDifference = 10,valueDifference = 5) == [0, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1],indexDifference = 2,valueDifference = 2) == [0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1],indexDifference = 2,valueDifference = 2) == [0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],indexDifference = 2,valueDifference = 30) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],indexDifference = 2,valueDifference = 30) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0],indexDifference = 5,valueDifference = 55) == [0, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0],indexDifference = 5,valueDifference = 55) == [0, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDifference = 0,valueDifference = 0) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDifference = 0,valueDifference = 0) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 10, 20, 30, 40, 50, 40, 30, 20, 10, 0],indexDifference = 3,valueDifference = 20) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 10, 20, 30, 40, 50, 40, 30, 20, 10, 0],indexDifference = 3,valueDifference = 20) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, -30, -35, -40, -45],indexDifference = 4,valueDifference = 20) == [0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, -30, -35, -40, -45],indexDifference = 4,valueDifference = 20) == [0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],indexDifference = 1,valueDifference = 8) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],indexDifference = 1,valueDifference = 8) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 7,valueDifference = 40) == [0, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 7,valueDifference = 40) == [0, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],indexDifference = 12,valueDifference = 10) == [0, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],indexDifference = 12,valueDifference = 10) == [0, 12]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 4,valueDifference = 50) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 4,valueDifference = 50) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],indexDifference = 5,valueDifference = 20) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],indexDifference = 5,valueDifference = 20) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],indexDifference = 5,valueDifference = 45) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],indexDifference = 5,valueDifference = 45) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],indexDifference = 6,valueDifference = 40) == [0, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],indexDifference = 6,valueDifference = 40) == [0, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 9,valueDifference = 1) == [0, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 9,valueDifference = 1) == [0, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],indexDifference = 3,valueDifference = 25) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],indexDifference = 3,valueDifference = 25) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],indexDifference = 6,valueDifference = 7) == [0, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],indexDifference = 6,valueDifference = 7) == [0, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 25, 0, 25, 50, 75, 100, 125, 150],indexDifference = 3,valueDifference = 50) == [2, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 25, 0, 25, 50, 75, 100, 125, 150],indexDifference = 3,valueDifference = 50) == [2, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 50, 0, 50, 0, 50, 0, 50, 0, 50],indexDifference = 1,valueDifference = 50) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 50, 0, 50, 0, 50, 0, 50, 0, 50],indexDifference = 1,valueDifference = 50) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],indexDifference = 6,valueDifference = 50) == [0, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],indexDifference = 6,valueDifference = 50) == [0, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 25, 0, 25, 50, 25, 0, 25, 50, 25, 0],indexDifference = 5,valueDifference = 30) == [0, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 25, 0, 25, 50, 25, 0, 25, 50, 25, 0],indexDifference = 5,valueDifference = 30) == [0, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99],indexDifference = 3,valueDifference = 27) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99],indexDifference = 3,valueDifference = 27) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 4,valueDifference = 45) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 4,valueDifference = 45) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],indexDifference = 3,valueDifference = 60) == [0, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],indexDifference = 3,valueDifference = 60) == [0, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 1,valueDifference = 0) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 1,valueDifference = 0) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100],indexDifference = 2,valueDifference = 25) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100],indexDifference = 2,valueDifference = 25) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],indexDifference = 6,valueDifference = 300) == [0, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],indexDifference = 6,valueDifference = 300) == [0, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50],indexDifference = 4,valueDifference = 25) == [0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50],indexDifference = 4,valueDifference = 25) == [0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],indexDifference = 2,valueDifference = 8) == [0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],indexDifference = 2,valueDifference = 8) == [0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],indexDifference = 8,valueDifference = 7) == [0, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],indexDifference = 8,valueDifference = 7) == [0, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 23, 34, 12, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56],indexDifference = 8,valueDifference = 30) == [1, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 23, 34, 12, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56],indexDifference = 8,valueDifference = 30) == [1, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],indexDifference = 1,valueDifference = 1) == [0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],indexDifference = 1,valueDifference = 1) == [0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],indexDifference = 6,valueDifference = 4) == [0, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],indexDifference = 6,valueDifference = 4) == [0, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],indexDifference = 15,valueDifference = 30) == [0, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],indexDifference = 15,valueDifference = 30) == [0, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],indexDifference = 8,valueDifference = 15) == [0, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],indexDifference = 8,valueDifference = 15) == [0, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDifference = 15,valueDifference = 15) == [0, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDifference = 15,valueDifference = 15) == [0, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],indexDifference = 8,valueDifference = 30) == [0, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],indexDifference = 8,valueDifference = 30) == [0, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 1,valueDifference = 1) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 1,valueDifference = 1) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],indexDifference = 10,valueDifference = 15) == [0, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],indexDifference = 10,valueDifference = 15) == [0, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 0, 10, 20, 30, 40, 50, 60],indexDifference = 3,valueDifference = 20) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 0, 10, 20, 30, 40, 50, 60],indexDifference = 3,valueDifference = 20) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49],indexDifference = 7,valueDifference = 20) == [0, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49],indexDifference = 7,valueDifference = 20) == [0, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 6, 4, 2, 0, 2, 4, 6, 8, 10],indexDifference = 4,valueDifference = 6) == [0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 6, 4, 2, 0, 2, 4, 6, 8, 10],indexDifference = 4,valueDifference = 6) == [0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],indexDifference = 4,valueDifference = 20) == [0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],indexDifference = 4,valueDifference = 20) == [0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10],indexDifference = 3,valueDifference = 9) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10],indexDifference = 3,valueDifference = 9) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDifference = 8,valueDifference = 3) == [0, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDifference = 8,valueDifference = 3) == [0, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 0, 10, 20, 30, 40, 50, 60],indexDifference = 5,valueDifference = 25) == [2, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 0, 10, 20, 30, 40, 50, 60],indexDifference = 5,valueDifference = 25) == [2, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 2,valueDifference = 1) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 2,valueDifference = 1) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],indexDifference = 7,valueDifference = 16) == [0, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],indexDifference = 7,valueDifference = 16) == [0, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDifference = 9,valueDifference = 9) == [0, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDifference = 9,valueDifference = 9) == [0, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 40, 35, 30, 25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, -30, -35, -40, -45, -50],indexDifference = 3,valueDifference = 15) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 40, 35, 30, 25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, -30, -35, -40, -45, -50],indexDifference = 3,valueDifference = 15) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 25, 0, 25, 50, 75, 100, 125, 150, 175],indexDifference = 6,valueDifference = 75) == [1, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 25, 0, 25, 50, 75, 100, 125, 150, 175],indexDifference = 6,valueDifference = 75) == [1, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41],indexDifference = 6,valueDifference = 10) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41],indexDifference = 6,valueDifference = 10) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],indexDifference = 15,valueDifference = 15) == [0, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],indexDifference = 15,valueDifference = 15) == [0, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],indexDifference = 4,valueDifference = 8) == [0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],indexDifference = 4,valueDifference = 8) == [0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50],indexDifference = 3,valueDifference = 20) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50],indexDifference = 3,valueDifference = 20) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5],indexDifference = 4,valueDifference = 25) == [0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5],indexDifference = 4,valueDifference = 25) == [0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 24, 35, 16, 27, 38, 49, 10, 21, 32],indexDifference = 5,valueDifference = 15) == [1, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 24, 35, 16, 27, 38, 49, 10, 21, 32],indexDifference = 5,valueDifference = 15) == [1, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],indexDifference = 10,valueDifference = 10) == [0, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],indexDifference = 10,valueDifference = 10) == [0, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 35, 25, 15, 5, 0, 5, 15, 25, 35, 45],indexDifference = 6,valueDifference = 20) == [0, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 35, 25, 15, 5, 0, 5, 15, 25, 35, 45],indexDifference = 6,valueDifference = 20) == [0, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40],indexDifference = 3,valueDifference = 25) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40],indexDifference = 3,valueDifference = 25) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5],indexDifference = 3,valueDifference = 2) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5],indexDifference = 3,valueDifference = 2) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10],indexDifference = 10,valueDifference = 10) == [0, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10],indexDifference = 10,valueDifference = 10) == [0, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDifference = 7,valueDifference = 10) == [0, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDifference = 7,valueDifference = 10) == [0, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 24, 12, 36, 21, 6, 48, 30, 18, 9, 54, 33, 15, 27, 63, 45, 22, 11, 44, 39],indexDifference = 7,valueDifference = 30) == [0, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 24, 12, 36, 21, 6, 48, 30, 18, 9, 54, 33, 15, 27, 63, 45, 22, 11, 44, 39],indexDifference = 7,valueDifference = 30) == [0, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],indexDifference = 9,valueDifference = 45) == [0, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],indexDifference = 9,valueDifference = 45) == [0, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],indexDifference = 2,valueDifference = 1) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],indexDifference = 2,valueDifference = 1) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 2,valueDifference = 0) == [0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 2,valueDifference = 0) == [0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDifference = 8,valueDifference = 10) == [0, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDifference = 8,valueDifference = 10) == [0, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 8,valueDifference = 30) == [0, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 8,valueDifference = 30) == [0, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],indexDifference = 10,valueDifference = 5) == [0, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],indexDifference = 10,valueDifference = 5) == [0, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],indexDifference = 5,valueDifference = 999999999) == [0, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],indexDifference = 5,valueDifference = 999999999) == [0, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],indexDifference = 5,valueDifference = 10) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],indexDifference = 5,valueDifference = 10) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],indexDifference = 5,valueDifference = 200) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],indexDifference = 5,valueDifference = 200) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 9,valueDifference = 80) == [0, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 9,valueDifference = 80) == [0, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],indexDifference = 7,valueDifference = 50) == [0, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],indexDifference = 7,valueDifference = 50) == [0, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 30,valueDifference = 1) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 30,valueDifference = 1) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 23, 34, 56, 78, 89, 90, 87, 65, 43, 21, 2],indexDifference = 6,valueDifference = 45) == [0, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 23, 34, 56, 78, 89, 90, 87, 65, 43, 21, 2],indexDifference = 6,valueDifference = 45) == [0, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 4,valueDifference = 30) == [0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 4,valueDifference = 30) == [0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 7,valueDifference = 25) == [1, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 7,valueDifference = 25) == [1, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],indexDifference = 2,valueDifference = 1) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],indexDifference = 2,valueDifference = 1) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50],indexDifference = 5,valueDifference = 30) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50],indexDifference = 5,valueDifference = 30) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 2,valueDifference = 1) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 2,valueDifference = 1) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],indexDifference = 3,valueDifference = 3) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],indexDifference = 3,valueDifference = 3) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],indexDifference = 6,valueDifference = 50) == [0, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],indexDifference = 6,valueDifference = 50) == [0, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDifference = 5,valueDifference = 5) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDifference = 5,valueDifference = 5) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91],indexDifference = 7,valueDifference = 90) == [0, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91],indexDifference = 7,valueDifference = 90) == [0, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33],indexDifference = 6,valueDifference = 5) == [0, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33],indexDifference = 6,valueDifference = 5) == [0, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6],indexDifference = 3,valueDifference = 5) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6],indexDifference = 3,valueDifference = 5) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4],indexDifference = 3,valueDifference = 1) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4],indexDifference = 3,valueDifference = 1) == [0, 3]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [1, 3, 5, 7, 9],indexDifference = 2,valueDifference = 6) == [0, 3]
    assert candidate(nums = [0, 0, 0, 0, 0],indexDifference = 0,valueDifference = 0) == [0, 0]
    assert candidate(nums = [10, 20, 30, 40, 50],indexDifference = 1,valueDifference = 25) == [0, 3]
    assert candidate(nums = [0, 0, 0, 0],indexDifference = 3,valueDifference = 1) == [-1, -1]
    assert candidate(nums = [0, 0, 0, 0],indexDifference = 1,valueDifference = 1) == [-1, -1]
    assert candidate(nums = [10, 5, 15, 20, 25],indexDifference = 2,valueDifference = 10) == [1, 3]
    assert candidate(nums = [4, 2, 3, 1, 5],indexDifference = 1,valueDifference = 2) == [0, 1]
    assert candidate(nums = [1, 3, 5, 7, 9],indexDifference = 3,valueDifference = 4) == [0, 3]
    assert candidate(nums = [45, 46, 47, 48, 49, 50],indexDifference = 2,valueDifference = 5) == [0, 5]
    assert candidate(nums = [4, 2, 3, 4, 5],indexDifference = 1,valueDifference = 2) == [0, 1]
    assert candidate(nums = [50, 40, 30, 20, 10],indexDifference = 2,valueDifference = 15) == [0, 2]
    assert candidate(nums = [1, 2, 3],indexDifference = 2,valueDifference = 4) == [-1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDifference = 5,valueDifference = 5) == [0, 5]
    assert candidate(nums = [2, 1],indexDifference = 0,valueDifference = 0) == [0, 0]
    assert candidate(nums = [50, 40, 30, 20, 10],indexDifference = 2,valueDifference = 30) == [0, 3]
    assert candidate(nums = [3, 5, 7, 9, 11],indexDifference = 1,valueDifference = 2) == [0, 1]
    assert candidate(nums = [5, 5, 5, 5, 5],indexDifference = 1,valueDifference = 1) == [-1, -1]
    assert candidate(nums = [3, 3, 3, 3, 3],indexDifference = 0,valueDifference = 0) == [0, 0]
    assert candidate(nums = [10, 20, 30, 40, 50],indexDifference = 3,valueDifference = 15) == [0, 3]
    assert candidate(nums = [10, 20, 30, 40, 50],indexDifference = 3,valueDifference = 20) == [0, 3]
    assert candidate(nums = [10, 20, 30, 40, 50],indexDifference = 2,valueDifference = 25) == [0, 3]
    assert candidate(nums = [50, 40, 30, 20, 10],indexDifference = 2,valueDifference = 25) == [0, 3]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],indexDifference = 3,valueDifference = 6) == [0, 3]
    assert candidate(nums = [5, 1, 4, 1],indexDifference = 2,valueDifference = 4) == [0, 3]
    assert candidate(nums = [9, 7, 5, 3, 1],indexDifference = 2,valueDifference = 6) == [0, 3]
    assert candidate(nums = [8, 8, 8, 8, 8, 8],indexDifference = 0,valueDifference = 0) == [0, 0]
    assert candidate(nums = [9, 7, 5, 3, 1],indexDifference = 3,valueDifference = 4) == [0, 3]
    assert candidate(nums = [4, 2, 3, 4, 1],indexDifference = 1,valueDifference = 2) == [0, 1]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 5,valueDifference = 1) == [-1, -1]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],indexDifference = 15,valueDifference = 50) == [0, 15]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 4,valueDifference = 45) == [0, 5]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],indexDifference = 3,valueDifference = 5) == [0, 5]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],indexDifference = 7,valueDifference = 40) == [0, 7]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],indexDifference = 3,valueDifference = 6) == [0, 6]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDifference = 10,valueDifference = 10) == [0, 10]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDifference = 1,valueDifference = 1) == [-1, -1]
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],indexDifference = 5,valueDifference = 15) == [0, 5]
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 9, 1, 10],indexDifference = 2,valueDifference = 4) == [2, 4]
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],indexDifference = 4,valueDifference = 30) == [0, 4]
    assert candidate(nums = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11],indexDifference = 5,valueDifference = 10) == [0, 10]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],indexDifference = 2,valueDifference = 1) == [-1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],indexDifference = 5,valueDifference = 5) == [0, 5]
    assert candidate(nums = [10, 10, 10, 10, 20, 20, 20, 20, 30, 30, 30, 30, 40, 40],indexDifference = 2,valueDifference = 10) == [0, 4]
    assert candidate(nums = [100, 50, 100, 50, 100, 50, 100, 50, 100],indexDifference = 2,valueDifference = 40) == [0, 3]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDifference = 5,valueDifference = 10) == [0, 10]
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],indexDifference = 5,valueDifference = 10) == [-1, -1]
    assert candidate(nums = [9, 7, 5, 3, 1, 3, 5, 7, 9, 11],indexDifference = 6,valueDifference = 6) == [3, 9]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],indexDifference = 2,valueDifference = 35) == [0, 4]
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31],indexDifference = 10,valueDifference = 5) == [0, 10]
    assert candidate(nums = [1, 2, 3, 4, 5, 4, 3, 2, 1],indexDifference = 2,valueDifference = 2) == [0, 2]
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],indexDifference = 2,valueDifference = 30) == [0, 3]
    assert candidate(nums = [90, 80, 70, 60, 50, 40, 30, 20, 10, 0],indexDifference = 5,valueDifference = 55) == [0, 6]
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],indexDifference = 0,valueDifference = 0) == [0, 0]
    assert candidate(nums = [0, 10, 20, 30, 40, 50, 40, 30, 20, 10, 0],indexDifference = 3,valueDifference = 20) == [0, 3]
    assert candidate(nums = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, -30, -35, -40, -45],indexDifference = 4,valueDifference = 20) == [0, 4]
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],indexDifference = 1,valueDifference = 8) == [0, 1]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 7,valueDifference = 40) == [0, 7]
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],indexDifference = 12,valueDifference = 10) == [0, 12]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 4,valueDifference = 50) == [0, 5]
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],indexDifference = 5,valueDifference = 20) == [0, 5]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],indexDifference = 5,valueDifference = 45) == [0, 5]
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],indexDifference = 6,valueDifference = 40) == [0, 6]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 9,valueDifference = 1) == [0, 9]
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],indexDifference = 3,valueDifference = 25) == [0, 5]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],indexDifference = 6,valueDifference = 7) == [0, 7]
    assert candidate(nums = [50, 25, 0, 25, 50, 75, 100, 125, 150],indexDifference = 3,valueDifference = 50) == [2, 5]
    assert candidate(nums = [0, 50, 0, 50, 0, 50, 0, 50, 0, 50],indexDifference = 1,valueDifference = 50) == [0, 1]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],indexDifference = 6,valueDifference = 50) == [0, 6]
    assert candidate(nums = [50, 25, 0, 25, 50, 25, 0, 25, 50, 25, 0],indexDifference = 5,valueDifference = 30) == [0, 6]
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99],indexDifference = 3,valueDifference = 27) == [0, 3]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 4,valueDifference = 45) == [0, 5]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],indexDifference = 3,valueDifference = 60) == [0, 6]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 1,valueDifference = 0) == [0, 1]
    assert candidate(nums = [30, 20, 10, 0, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100],indexDifference = 2,valueDifference = 25) == [0, 3]
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],indexDifference = 6,valueDifference = 300) == [0, 6]
    assert candidate(nums = [10, 20, 30, 40, 50, 10, 20, 30, 40, 50],indexDifference = 4,valueDifference = 25) == [0, 4]
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],indexDifference = 2,valueDifference = 8) == [0, 4]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],indexDifference = 8,valueDifference = 7) == [0, 8]
    assert candidate(nums = [42, 23, 34, 12, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56, 78, 90, 12, 34, 56],indexDifference = 8,valueDifference = 30) == [1, 9]
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],indexDifference = 1,valueDifference = 1) == [0, 2]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5],indexDifference = 6,valueDifference = 4) == [0, 6]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59],indexDifference = 15,valueDifference = 30) == [0, 15]
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],indexDifference = 8,valueDifference = 15) == [0, 8]
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],indexDifference = 15,valueDifference = 15) == [0, 15]
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],indexDifference = 8,valueDifference = 30) == [0, 8]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 1,valueDifference = 1) == [-1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],indexDifference = 10,valueDifference = 15) == [0, 15]
    assert candidate(nums = [30, 20, 10, 0, 10, 20, 30, 40, 50, 60],indexDifference = 3,valueDifference = 20) == [0, 3]
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49],indexDifference = 7,valueDifference = 20) == [0, 7]
    assert candidate(nums = [8, 6, 4, 2, 0, 2, 4, 6, 8, 10],indexDifference = 4,valueDifference = 6) == [0, 4]
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],indexDifference = 4,valueDifference = 20) == [0, 4]
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10],indexDifference = 3,valueDifference = 9) == [0, 3]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDifference = 8,valueDifference = 3) == [0, 8]
    assert candidate(nums = [30, 20, 10, 0, 10, 20, 30, 40, 50, 60],indexDifference = 5,valueDifference = 25) == [2, 7]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 2,valueDifference = 1) == [-1, -1]
    assert candidate(nums = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37],indexDifference = 7,valueDifference = 16) == [0, 7]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDifference = 9,valueDifference = 9) == [0, 9]
    assert candidate(nums = [45, 40, 35, 30, 25, 20, 15, 10, 5, 0, -5, -10, -15, -20, -25, -30, -35, -40, -45, -50],indexDifference = 3,valueDifference = 15) == [0, 3]
    assert candidate(nums = [50, 25, 0, 25, 50, 75, 100, 125, 150, 175],indexDifference = 6,valueDifference = 75) == [1, 7]
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41],indexDifference = 6,valueDifference = 10) == [-1, -1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],indexDifference = 15,valueDifference = 15) == [0, 15]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],indexDifference = 4,valueDifference = 8) == [0, 4]
    assert candidate(nums = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50],indexDifference = 3,valueDifference = 20) == [0, 3]
    assert candidate(nums = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5],indexDifference = 4,valueDifference = 25) == [0, 4]
    assert candidate(nums = [42, 24, 35, 16, 27, 38, 49, 10, 21, 32],indexDifference = 5,valueDifference = 15) == [1, 6]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],indexDifference = 10,valueDifference = 10) == [0, 10]
    assert candidate(nums = [45, 35, 25, 15, 5, 0, 5, 15, 25, 35, 45],indexDifference = 6,valueDifference = 20) == [0, 6]
    assert candidate(nums = [50, 40, 30, 20, 10, 0, -10, -20, -30, -40],indexDifference = 3,valueDifference = 25) == [0, 3]
    assert candidate(nums = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5],indexDifference = 3,valueDifference = 2) == [0, 3]
    assert candidate(nums = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10],indexDifference = 10,valueDifference = 10) == [0, 10]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDifference = 7,valueDifference = 10) == [0, 10]
    assert candidate(nums = [42, 24, 12, 36, 21, 6, 48, 30, 18, 9, 54, 33, 15, 27, 63, 45, 22, 11, 44, 39],indexDifference = 7,valueDifference = 30) == [0, 9]
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],indexDifference = 9,valueDifference = 45) == [0, 9]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],indexDifference = 2,valueDifference = 1) == [-1, -1]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 2,valueDifference = 0) == [0, 2]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],indexDifference = 8,valueDifference = 10) == [0, 10]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 8,valueDifference = 30) == [0, 8]
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],indexDifference = 10,valueDifference = 5) == [0, 10]
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],indexDifference = 5,valueDifference = 999999999) == [0, 9]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],indexDifference = 5,valueDifference = 10) == [0, 5]
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],indexDifference = 5,valueDifference = 200) == [0, 5]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 9,valueDifference = 80) == [0, 9]
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],indexDifference = 7,valueDifference = 50) == [0, 7]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 30,valueDifference = 1) == [-1, -1]
    assert candidate(nums = [42, 23, 34, 56, 78, 89, 90, 87, 65, 43, 21, 2],indexDifference = 6,valueDifference = 45) == [0, 6]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 4,valueDifference = 30) == [0, 4]
    assert candidate(nums = [30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],indexDifference = 7,valueDifference = 25) == [1, 8]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],indexDifference = 2,valueDifference = 1) == [-1, -1]
    assert candidate(nums = [50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50],indexDifference = 5,valueDifference = 30) == [0, 5]
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],indexDifference = 2,valueDifference = 1) == [-1, -1]
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],indexDifference = 3,valueDifference = 3) == [0, 3]
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],indexDifference = 6,valueDifference = 50) == [0, 6]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],indexDifference = 5,valueDifference = 5) == [0, 5]
    assert candidate(nums = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91],indexDifference = 7,valueDifference = 90) == [0, 7]
    assert candidate(nums = [45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33],indexDifference = 6,valueDifference = 5) == [0, 6]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6],indexDifference = 3,valueDifference = 5) == [0, 5]
    assert candidate(nums = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4],indexDifference = 3,valueDifference = 1) == [0, 3]


