def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96],target = 98) == [2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96],target = 98) == [2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],target = 50) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],target = 50) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7],target = 8) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7],target = 8) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],target = 25) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],target = 25) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],target = 0) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],target = 0) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10],target = 15) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10],target = 15) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100],target = 100) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100],target = 100) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 5, 2, 3],target = 3) == [3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 5, 2, 3],target = 3) == [3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10],target = 2) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10],target = 2) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],target = 5) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],target = 5) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],target = 1) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],target = 1) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1],target = 3) == [2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1],target = 3) == [2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],target = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],target = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 3, 4],target = 2) == [1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 3, 4],target = 2) == [1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 5, 2, 3],target = 2) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 5, 2, 3],target = 2) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50],target = 50) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50],target = 50) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],target = 6) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],target = 6) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],target = 10) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],target = 10) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 100, 1, 100],target = 1) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 100, 1, 100],target = 1) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 5, 2, 3],target = 5) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 5, 2, 3],target = 5) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],target = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],target = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],target = 4) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],target = 4) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 4) == [6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 4) == [6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 4, 3, 2, 1],target = 3) == [2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 4, 3, 2, 1],target = 3) == [2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [90, 80, 70, 60, 50, 40, 30, 20, 10],target = 45) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [90, 80, 70, 60, 50, 40, 30, 20, 10],target = 45) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 50) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 50) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],target = 95) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],target = 95) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 5) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 5) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],target = 7) == [6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],target = 7) == [6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],target = 5) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],target = 5) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],target = 27) == [8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],target = 27) == [8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 6, 5, 4, 3, 2, 1],target = 4) == [3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 6, 5, 4, 3, 2, 1],target = 4) == [3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],target = 5) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],target = 5) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],target = 35) == [6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],target = 35) == [6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 99, 99, 98, 98, 97, 97],target = 99) == [4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 99, 99, 98, 98, 97, 97],target = 99) == [4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31],target = 37) == [6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31],target = 37) == [6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 1) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 1) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 8) == [3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 8) == [3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 10) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 10) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 5) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 5) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 20) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 20) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1],target = 4) == [3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1],target = 4) == [3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 24, 36, 18, 54, 30, 48, 27, 60, 39],target = 30) == [3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 24, 36, 18, 54, 30, 48, 27, 60, 39],target = 30) == [3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1],target = 5) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1],target = 5) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 30, 70, 20],target = 30) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 30, 70, 20],target = 30) == [1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],target = 50) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],target = 50) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],target = 8) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],target = 8) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 23, 37, 23, 42, 37],target = 37) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 23, 37, 23, 42, 37],target = 37) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 4) == [7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 4) == [7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7],target = 15) == [8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7],target = 15) == [8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95],target = 98) == [3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95],target = 98) == [3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],target = 55) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],target = 55) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 15) == [7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 15) == [7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 10) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 10) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1],target = 2) == [5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1],target = 2) == [5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 55) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 55) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 1) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 1) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],target = 35) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],target = 35) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],target = 3) == [6, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],target = 3) == [6, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 20) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 20) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96],target = 97) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96],target = 97) == [1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 6, 6, 6, 8, 6, 8, 6, 8, 6, 6, 6, 6, 6],target = 6) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 6, 6, 6, 8, 6, 8, 6, 8, 6, 6, 6, 6, 6],target = 6) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 27, 89, 10, 56, 23, 50, 78, 34, 67],target = 50) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 27, 89, 10, 56, 23, 50, 78, 34, 67],target = 50) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],target = 8) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],target = 8) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 10) == [18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 10) == [18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],target = 40) == [3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],target = 40) == [3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 11) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 11) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 6, 7, 5, 3, 0, 9],target = 7) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 6, 7, 5, 3, 0, 9],target = 7) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 5) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 5) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],target = 5) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],target = 5) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 10) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 10) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],target = 13) == [12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],target = 13) == [12]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 20, 30, 40, 10],target = 30) == [2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 20, 30, 40, 10],target = 30) == [2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 50, 20, 30, 60, 40],target = 30) == [2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 50, 20, 30, 60, 40],target = 30) == [2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 6) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 6) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 15) == [14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 15) == [14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],target = 10) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],target = 10) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 15) == [14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 15) == [14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50],target = 50) == [0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50],target = 50) == [0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 8) == [7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 8) == [7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 11) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 11) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],target = 20) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],target = 20) == [1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],target = 20) == [5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],target = 20) == [5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 15) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 15) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],target = 17) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],target = 17) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],target = 95) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],target = 95) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 20, 30, 10, 40],target = 30) == [2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 20, 30, 10, 40],target = 30) == [2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],target = 50) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],target = 50) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 6) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 6) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 5, 4, 2, 3, 3, 5, 1],target = 3) == [4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 5, 4, 2, 3, 3, 5, 1],target = 3) == [4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],target = 50) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],target = 50) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1],target = 2) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1],target = 2) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 6) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 6) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],target = 18) == [8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],target = 18) == [8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 5) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 5) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1, 100, 1, 100, 1, 100],target = 1) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1, 100, 1, 100, 1, 100],target = 1) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3],target = 2) == [3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3],target = 2) == [3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],target = 5) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],target = 5) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 20, 30, 40, 10],target = 20) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 20, 30, 40, 10],target = 20) == [1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 10) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 10) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 20, 30, 40, 10, 60, 70, 80, 90, 100],target = 40) == [3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 20, 30, 40, 10, 60, 70, 80, 90, 100],target = 40) == [3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 10) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 10) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 21) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 21) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 5, 4],target = 4) == [3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 5, 4],target = 4) == [3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 15) == [8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 15) == [8]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10],target = 15) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10],target = 15) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 55) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 55) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 10, 20, 10, 20],target = 10) == [0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 10, 20, 10, 20],target = 10) == [0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10],target = 30) == [2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10],target = 30) == [2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],target = 250) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],target = 250) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10],target = 20) == [1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10],target = 20) == [1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 15) == [14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 15) == [14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 6) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 6) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],target = 25) == [12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],target = 25) == [12]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 2, 4, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 3) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 2, 4, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 3) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [42, 37, 58, 54, 19, 91, 49, 100, 65, 28, 74, 99, 96, 33, 80, 78, 60, 82, 97, 71],target = 74) == [11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [42, 37, 58, 54, 19, 91, 49, 100, 65, 28, 74, 99, 96, 33, 80, 78, 60, 82, 97, 71],target = 74) == [11]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [100, 99, 98, 97, 96],target = 98) == [2]
    assert candidate(nums = [10, 20, 30, 40, 50],target = 50) == [4]
    assert candidate(nums = [7, 7, 7, 7, 7],target = 8) == []
    assert candidate(nums = [10, 20, 30, 40, 50],target = 25) == []
    assert candidate(nums = [1, 3, 5, 7, 9],target = 0) == []
    assert candidate(nums = [50, 40, 30, 20, 10],target = 15) == []
    assert candidate(nums = [100, 100, 100],target = 100) == [0, 1, 2]
    assert candidate(nums = [1, 2, 5, 2, 3],target = 3) == [3]
    assert candidate(nums = [2, 4, 6, 8, 10],target = 2) == [0]
    assert candidate(nums = [5, 5, 5, 5, 5],target = 5) == [0, 1, 2, 3, 4]
    assert candidate(nums = [1, 1, 1, 1, 1],target = 1) == [0, 1, 2, 3, 4]
    assert candidate(nums = [5, 4, 3, 2, 1],target = 3) == [2]
    assert candidate(nums = [1, 3, 5, 7, 9],target = 2) == []
    assert candidate(nums = [1, 2, 2, 2, 3, 4],target = 2) == [1, 2, 3]
    assert candidate(nums = [1, 2, 5, 2, 3],target = 2) == [1, 2]
    assert candidate(nums = [50, 50, 50, 50, 50],target = 50) == [0, 1, 2, 3, 4]
    assert candidate(nums = [5, 5, 5, 5, 5],target = 6) == []
    assert candidate(nums = [1, 3, 5, 7, 9],target = 10) == []
    assert candidate(nums = [100, 1, 100, 1, 100],target = 1) == [0, 1]
    assert candidate(nums = [1, 2, 5, 2, 3],target = 5) == [4]
    assert candidate(nums = [1, 1, 1, 1, 1],target = 2) == []
    assert candidate(nums = [1, 3, 5, 7, 9],target = 4) == []
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 4) == [6, 7]
    assert candidate(nums = [5, 4, 3, 2, 1],target = 3) == [2]
    assert candidate(nums = [90, 80, 70, 60, 50, 40, 30, 20, 10],target = 45) == []
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 50) == [4]
    assert candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],target = 95) == [5]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 5) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(nums = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10],target = 7) == [6]
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],target = 5) == [4]
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],target = 27) == [8]
    assert candidate(nums = [7, 6, 5, 4, 3, 2, 1],target = 4) == [3]
    assert candidate(nums = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],target = 5) == [4]
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],target = 35) == [6]
    assert candidate(nums = [100, 100, 99, 99, 98, 98, 97, 97],target = 99) == [4, 5]
    assert candidate(nums = [45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31],target = 37) == [6]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 1) == [0]
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 8) == [3]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 10) == []
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 5) == [4]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 20) == []
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1],target = 4) == [3]
    assert candidate(nums = [42, 24, 36, 18, 54, 30, 48, 27, 60, 39],target = 30) == [3]
    assert candidate(nums = [5, 3, 8, 6, 2, 7, 4, 1],target = 5) == [4]
    assert candidate(nums = [100, 50, 30, 70, 20],target = 30) == [1]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],target = 50) == [4]
    assert candidate(nums = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],target = 8) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(nums = [42, 23, 37, 23, 42, 37],target = 37) == [2, 3]
    assert candidate(nums = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 4) == [7, 8, 9, 10]
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7],target = 15) == [8]
    assert candidate(nums = [100, 99, 98, 97, 96, 95],target = 98) == [3]
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],target = 55) == [5]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 15) == [7]
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 10) == [9]
    assert candidate(nums = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1],target = 2) == [5, 6, 7, 8, 9]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 55) == []
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 1) == [0]
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],target = 35) == [4]
    assert candidate(nums = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],target = 3) == [6, 7, 8]
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],target = 20) == [9]
    assert candidate(nums = [100, 99, 98, 97, 96],target = 97) == [1]
    assert candidate(nums = [8, 6, 6, 6, 8, 6, 8, 6, 8, 6, 6, 6, 6, 6],target = 6) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(nums = [42, 27, 89, 10, 56, 23, 50, 78, 34, 67],target = 50) == [5]
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],target = 8) == []
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 10) == [18, 19]
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],target = 40) == [3]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 11) == []
    assert candidate(nums = [8, 6, 7, 5, 3, 0, 9],target = 7) == [4]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 5) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10],target = 5) == [4]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 10) == [9]
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14],target = 13) == [12]
    assert candidate(nums = [50, 20, 30, 40, 10],target = 30) == [2]
    assert candidate(nums = [100, 1, 50, 20, 30, 60, 40],target = 30) == [2]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 6) == [5]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 15) == [14]
    assert candidate(nums = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10],target = 10) == [9]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 15) == [14]
    assert candidate(nums = [50, 50, 50, 50, 50, 50],target = 50) == [0, 1, 2, 3, 4, 5]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 8) == [7]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 11) == []
    assert candidate(nums = [10, 20, 30, 40, 50],target = 20) == [1]
    assert candidate(nums = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20],target = 20) == [5, 6, 7, 8, 9]
    assert candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 15) == [5]
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],target = 17) == []
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],target = 95) == [4]
    assert candidate(nums = [50, 20, 30, 10, 40],target = 30) == [2]
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],target = 50) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 6) == []
    assert candidate(nums = [3, 1, 2, 5, 4, 2, 3, 3, 5, 1],target = 3) == [4, 5, 6]
    assert candidate(nums = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],target = 50) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(nums = [1],target = 2) == []
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 6) == []
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],target = 18) == [8]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 5) == [4]
    assert candidate(nums = [100, 1, 100, 1, 100, 1, 100],target = 1) == [0, 1, 2]
    assert candidate(nums = [3, 1, 2, 3, 1, 2, 3, 1, 2, 3],target = 2) == [3, 4, 5]
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],target = 5) == [4]
    assert candidate(nums = [50, 20, 30, 40, 10],target = 20) == [1]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 10) == []
    assert candidate(nums = [50, 20, 30, 40, 10, 60, 70, 80, 90, 100],target = 40) == [3]
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 10) == [9]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 21) == []
    assert candidate(nums = [3, 1, 2, 5, 4],target = 4) == [3]
    assert candidate(nums = [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 15) == [8]
    assert candidate(nums = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10],target = 15) == [5]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 55) == []
    assert candidate(nums = [10, 20, 10, 20, 10, 20],target = 10) == [0, 1, 2]
    assert candidate(nums = [50, 40, 30, 20, 10],target = 30) == [2]
    assert candidate(nums = [100, 200, 300, 400, 500],target = 250) == []
    assert candidate(nums = [50, 40, 30, 20, 10],target = 20) == [1]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 15) == [14]
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],target = 6) == [5]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],target = 25) == [12]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5) == [4]
    assert candidate(nums = [3, 1, 2, 4, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 3) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert candidate(nums = [42, 37, 58, 54, 19, 91, 49, 100, 65, 28, 74, 99, 96, 33, 80, 78, 60, 82, 97, 71],target = 74) == [11]


