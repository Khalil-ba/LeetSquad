def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [3, 4, 5],head = list_node([1, 2, 3, 4, 5])), list_node([1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [3, 4, 5],head = list_node([1, 2, 3, 4, 5])), list_node([1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [10],head = list_node([1, 10, 100, 1000])), list_node([1, 100, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [10],head = list_node([1, 10, 100, 1000])), list_node([1, 100, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1],head = list_node([1, 2, 1, 2, 1, 2])), list_node([2, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1],head = list_node([1, 2, 1, 2, 1, 2])), list_node([2, 2, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 2, 3],head = list_node([1, 2, 3, 4, 5])), list_node([4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 2, 3],head = list_node([1, 2, 3, 4, 5])), list_node([4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [2, 4, 6, 8, 10],head = list_node([1, 3, 5, 7, 9])), list_node([1, 3, 5, 7, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [2, 4, 6, 8, 10],head = list_node([1, 3, 5, 7, 9])), list_node([1, 3, 5, 7, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [100000],head = list_node([1, 2, 3, 4, 100000])), list_node([1, 2, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [100000],head = list_node([1, 2, 3, 4, 100000])), list_node([1, 2, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 3, 5, 7, 9],head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([0, 2, 4, 6, 8, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 3, 5, 7, 9],head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([0, 2, 4, 6, 8, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [2, 4],head = list_node([1, 2, 3, 4, 5])), list_node([1, 3, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [2, 4],head = list_node([1, 2, 3, 4, 5])), list_node([1, 3, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [5],head = list_node([1, 2, 3, 4])), list_node([1, 2, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [5],head = list_node([1, 2, 3, 4])), list_node([1, 2, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [10, 20, 30],head = list_node([5, 10, 15, 20, 25, 30, 35])), list_node([5, 15, 25, 35]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [10, 20, 30],head = list_node([5, 10, 15, 20, 25, 30, 35])), list_node([5, 15, 25, 35])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [10, 20, 30],head = list_node([5, 10, 15, 20, 25, 30])), list_node([5, 15, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [10, 20, 30],head = list_node([5, 10, 15, 20, 25, 30])), list_node([5, 15, 25])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [100000],head = list_node([99999, 100000, 100001])), list_node([99999, 100001]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [100000],head = list_node([99999, 100000, 100001])), list_node([99999, 100001])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 3, 5, 7, 9],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([2, 4, 6, 8, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 3, 5, 7, 9],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([2, 4, 6, 8, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [7, 8, 9],head = list_node([7, 8, 9, 10, 11, 12])), list_node([10, 11, 12]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [7, 8, 9],head = list_node([7, 8, 9, 10, 11, 12])), list_node([10, 11, 12])): {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [5, 10, 15, 20, 25, 30],head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])), list_node([35, 40, 45, 50, 55, 60]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [5, 10, 15, 20, 25, 30],head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])), list_node([35, 40, 45, 50, 55, 60])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])), list_node([1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49, 51, 52, 53, 54, 56, 57, 58, 59, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 73, 74, 76, 77, 78, 79, 81, 82, 83, 84, 86, 87, 88, 89, 91, 92, 93, 94, 96, 97, 98, 99]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])), list_node([1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49, 51, 52, 53, 54, 56, 57, 58, 59, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 73, 74, 76, 77, 78, 79, 81, 82, 83, 84, 86, 87, 88, 89, 91, 92, 93, 94, 96, 97, 98, 99])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [100000],head = list_node([50000, 100000, 150000, 200000])), list_node([50000, 150000, 200000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [100000],head = list_node([50000, 100000, 150000, 200000])), list_node([50000, 150000, 200000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 3, 5, 7, 9],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([2, 4, 6, 8, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 3, 5, 7, 9],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([2, 4, 6, 8, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 3, 5, 7, 9],head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 3, 5, 7, 9],head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1000, 2000, 3000, 4000, 5000],head = list_node([5000, 4000, 3000, 2000, 1000, 500, 400, 300, 200, 100])), list_node([500, 400, 300, 200, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1000, 2000, 3000, 4000, 5000],head = list_node([5000, 4000, 3000, 2000, 1000, 500, 400, 300, 200, 100])), list_node([500, 400, 300, 200, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])), list_node([110, 120, 130, 140, 150, 160, 170, 180, 190, 200]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])), list_node([110, 120, 130, 140, 150, 160, 170, 180, 190, 200])): {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 3, 5, 7, 9],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([2, 4, 6, 8, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 3, 5, 7, 9],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([2, 4, 6, 8, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [5, 10, 15, 20, 25],head = list_node([1, 5, 10, 15, 20, 25, 30, 35])), list_node([1, 30, 35]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [5, 10, 15, 20, 25],head = list_node([1, 5, 10, 15, 20, 25, 30, 35])), list_node([1, 30, 35])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],head = list_node([1, 10, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60, 7, 70, 8, 80, 9, 90, 10, 100, 11])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],head = list_node([1, 10, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60, 7, 70, 8, 80, 9, 90, 10, 100, 11])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 11])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [7, 8, 9],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])), list_node([1, 2, 3, 4, 5, 6, 10, 11, 12, 13]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [7, 8, 9],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])), list_node([1, 2, 3, 4, 5, 6, 10, 11, 12, 13])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [5, 15, 25, 35, 45, 55],head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])), list_node([10, 20, 30, 40, 50, 60]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [5, 15, 25, 35, 45, 55],head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])), list_node([10, 20, 30, 40, 50, 60])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [2],head = list_node([1, 2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 2, 8, 2, 9, 2, 10, 2])), list_node([1, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [2],head = list_node([1, 2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 2, 8, 2, 9, 2, 10, 2])), list_node([1, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 5, 10, 15, 20],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 5, 10, 15, 20],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],head = list_node([1, 90, 2, 91, 3, 92, 4, 93, 5, 94, 6, 95, 7, 96, 8, 97, 9, 98, 10, 99])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],head = list_node([1, 90, 2, 91, 3, 92, 4, 93, 5, 94, 6, 95, 7, 96, 8, 97, 9, 98, 10, 99])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])), list_node([31, 32, 33, 34, 35, 36, 37, 38, 39, 40]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])), list_node([31, 32, 33, 34, 35, 36, 37, 38, 39, 40])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 4, 9, 16, 25],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])), list_node([2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 4, 9, 16, 25],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])), list_node([2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])), list_node([110, 120, 130, 140, 150]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])), list_node([110, 120, 130, 140, 150])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])), list_node([1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])), list_node([1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],head = list_node([10, 100, 20, 200, 30, 300, 40, 400, 50, 500, 60, 600, 70, 700, 80, 800, 90, 900, 100, 1000])), list_node([200, 300, 400, 500, 600, 700, 800, 900, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],head = list_node([10, 100, 20, 200, 30, 300, 40, 400, 50, 500, 60, 600, 70, 700, 80, 800, 90, 900, 100, 1000])), list_node([200, 300, 400, 500, 600, 700, 800, 900, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 101]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 101])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [3, 5, 7, 9, 11],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])), list_node([1, 2, 4, 6, 8, 10, 12]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [3, 5, 7, 9, 11],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])), list_node([1, 2, 4, 6, 8, 10, 12])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([21, 22, 23, 24, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([21, 22, 23, 24, 25])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 11, 21, 31, 41, 51],head = list_node([1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151])), list_node([61, 71, 81, 91, 101, 111, 121, 131, 141, 151]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 11, 21, 31, 41, 51],head = list_node([1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151])), list_node([61, 71, 81, 91, 101, 111, 121, 131, 141, 151])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [100, 200, 300, 400, 500],head = list_node([100, 150, 200, 250, 300, 350, 400, 450, 500, 550])), list_node([150, 250, 350, 450, 550]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [100, 200, 300, 400, 500],head = list_node([100, 150, 200, 250, 300, 350, 400, 450, 500, 550])), list_node([150, 250, 350, 450, 550])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [100000],head = list_node([1, 50000, 100000, 150000, 200000])), list_node([1, 50000, 150000, 200000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [100000],head = list_node([1, 50000, 100000, 150000, 200000])), list_node([1, 50000, 150000, 200000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70])), list_node([1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 57, 58, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70])), list_node([1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 57, 58, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [100, 200, 300, 400, 500],head = list_node([50, 100, 150, 200, 250, 300, 350, 400, 450, 500])), list_node([50, 150, 250, 350, 450]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [100, 200, 300, 400, 500],head = list_node([50, 100, 150, 200, 250, 300, 350, 400, 450, 500])), list_node([50, 150, 250, 350, 450])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [5, 10, 15],head = list_node([1, 5, 10, 15, 20, 25, 30])), list_node([1, 20, 25, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [5, 10, 15],head = list_node([1, 5, 10, 15, 20, 25, 30])), list_node([1, 20, 25, 30])): {e}')
    
    total += 1
    try:
        result = candidate(nums = [5],head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5],head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [15, 16, 17, 18, 19],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [15, 16, 17, 18, 19],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [2, 4, 6, 8],head = list_node([2, 4, 6, 8, 10, 12, 14, 16])), list_node([10, 12, 14, 16]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [2, 4, 6, 8],head = list_node([2, 4, 6, 8, 10, 12, 14, 16])), list_node([10, 12, 14, 16])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])), list_node([2, 4, 6, 8, 10, 12, 14, 16]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])), list_node([2, 4, 6, 8, 10, 12, 14, 16])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [2, 5, 7, 10],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])), list_node([1, 3, 4, 6, 8, 9, 11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [2, 5, 7, 10],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])), list_node([1, 3, 4, 6, 8, 9, 11])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [100000],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100000])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [100000],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100000])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 100, 1000, 10000, 100000],head = list_node([1, 10, 100, 1000, 10000, 100000])), list_node([10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 100, 1000, 10000, 100000],head = list_node([1, 10, 100, 1000, 10000, 100000])), list_node([10])): {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3],head = list_node([3, 2, 1, 3, 2, 1, 3, 2, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3],head = list_node([3, 2, 1, 3, 2, 1, 3, 2, 1])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 5, 10, 15, 20, 25, 30],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 5, 10, 15, 20, 25, 30],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 10, 100, 1000, 10000],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100, 1000, 10000])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 10, 100, 1000, 10000],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100, 1000, 10000])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 100, 10000, 100000],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100, 200, 300, 400, 500, 10000, 20000, 30000, 40000, 50000, 100000])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 200, 300, 400, 500, 20000, 30000, 40000, 50000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 100, 10000, 100000],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100, 200, 300, 400, 500, 10000, 20000, 30000, 40000, 50000, 100000])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 200, 300, 400, 500, 20000, 30000, 40000, 50000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [10, 20, 30, 40, 50],head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])), list_node([5, 15, 25, 35, 45, 55]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [10, 20, 30, 40, 50],head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])), list_node([5, 15, 25, 35, 45, 55])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])), list_node([55, 60, 65, 70, 75, 80, 85, 90, 95, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])), list_node([55, 60, 65, 70, 75, 80, 85, 90, 95, 100])): {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3],head = list_node([3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3],head = list_node([3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],head = list_node([1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])), list_node([1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],head = list_node([1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])), list_node([1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [5, 10, 15, 20, 25],head = list_node([5, 10, 15, 20, 25, 30, 35, 40])), list_node([30, 35, 40]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [5, 10, 15, 20, 25],head = list_node([5, 10, 15, 20, 25, 30, 35, 40])), list_node([30, 35, 40])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [10, 20, 30, 40, 50],head = list_node([50, 40, 30, 20, 10, 0, -10, -20, -30])), list_node([0, -10, -20, -30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [10, 20, 30, 40, 50],head = list_node([50, 40, 30, 20, 10, 0, -10, -20, -30])), list_node([0, -10, -20, -30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])), list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])), list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 100, 1000, 10000, 100000],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100, 101, 102, 103, 104, 105, 1000, 1001, 1002, 10000, 10001])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 101, 102, 103, 104, 105, 1001, 1002, 10001]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 100, 1000, 10000, 100000],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100, 101, 102, 103, 104, 105, 1000, 1001, 1002, 10000, 10001])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 101, 102, 103, 104, 105, 1001, 1002, 10001])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [5],head = list_node([1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [5],head = list_node([1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])), list_node([110, 120, 130, 140, 150]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])), list_node([110, 120, 130, 140, 150])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [15, 16, 17, 18, 19, 20],head = list_node([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([10, 11, 12, 13, 14, 21, 22, 23, 24, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [15, 16, 17, 18, 19, 20],head = list_node([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([10, 11, 12, 13, 14, 21, 22, 23, 24, 25])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],head = list_node([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000])), list_node([110000, 120000, 130000, 140000, 150000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],head = list_node([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000])), list_node([110000, 120000, 130000, 140000, 150000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [2, 5, 7, 11, 13],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 3, 4, 6, 8, 9, 10, 12, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [2, 5, 7, 11, 13],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 3, 4, 6, 8, 9, 10, 12, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19],head = list_node([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])), list_node([23, 29, 31]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19],head = list_node([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])), list_node([23, 29, 31])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])), list_node([2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])), list_node([2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [100, 200, 300, 400, 500],head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900])), list_node([600, 700, 800, 900]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [100, 200, 300, 400, 500],head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900])), list_node([600, 700, 800, 900])): {e}')
    
    total += 1
    try:
        result = candidate(nums = [5],head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5],head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])), list_node([6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])), list_node([6, 6, 7, 7, 8, 8, 9, 9, 10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 22, 23, 24, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 22, 23, 24, 25])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [50000, 50001, 50002, 50003, 50004, 50005],head = list_node([49999, 50000, 50001, 50002, 50003, 50004, 50005, 50006])), list_node([49999, 50006]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [50000, 50001, 50002, 50003, 50004, 50005],head = list_node([49999, 50000, 50001, 50002, 50003, 50004, 50005, 50006])), list_node([49999, 50006])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [5, 25, 45, 65, 85, 105],head = list_node([5, 20, 25, 40, 45, 60, 65, 80, 85, 100, 105, 120, 130, 140, 150])), list_node([20, 40, 60, 80, 100, 120, 130, 140, 150]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [5, 25, 45, 65, 85, 105],head = list_node([5, 20, 25, 40, 45, 60, 65, 80, 85, 100, 105, 120, 130, 140, 150])), list_node([20, 40, 60, 80, 100, 120, 130, 140, 150])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [100000],head = list_node([100000, 99999, 99998, 99997, 99996])), list_node([99999, 99998, 99997, 99996]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [100000],head = list_node([100000, 99999, 99998, 99997, 99996])), list_node([99999, 99998, 99997, 99996])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [5, 10, 15, 20, 25],head = list_node([1, 5, 9, 10, 14, 19, 20, 24, 25])), list_node([1, 9, 14, 19, 24]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [5, 10, 15, 20, 25],head = list_node([1, 5, 9, 10, 14, 19, 20, 24, 25])), list_node([1, 9, 14, 19, 24])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [20, 40, 60, 80, 100],head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])), list_node([10, 30, 50, 70, 90, 110]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [20, 40, 60, 80, 100],head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])), list_node([10, 30, 50, 70, 90, 110])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 10, 100, 1000, 10000, 100000],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 200000])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 200, 300, 400, 500, 600, 700, 800, 900, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 200000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 10, 100, 1000, 10000, 100000],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 200000])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 200, 300, 400, 500, 600, 700, 800, 900, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 200000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 3, 5, 7, 9, 11],head = list_node([2, 4, 6, 8, 10, 12, 14])), list_node([2, 4, 6, 8, 10, 12, 14]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 3, 5, 7, 9, 11],head = list_node([2, 4, 6, 8, 10, 12, 14])), list_node([2, 4, 6, 8, 10, 12, 14])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_list(candidate(nums = [3, 4, 5],head = list_node([1, 2, 3, 4, 5])), list_node([1, 2]))
    assert is_same_list(candidate(nums = [10],head = list_node([1, 10, 100, 1000])), list_node([1, 100, 1000]))
    assert is_same_list(candidate(nums = [1],head = list_node([1, 2, 1, 2, 1, 2])), list_node([2, 2, 2]))
    assert is_same_list(candidate(nums = [1, 2, 3],head = list_node([1, 2, 3, 4, 5])), list_node([4, 5]))
    assert is_same_list(candidate(nums = [2, 4, 6, 8, 10],head = list_node([1, 3, 5, 7, 9])), list_node([1, 3, 5, 7, 9]))
    assert is_same_list(candidate(nums = [100000],head = list_node([1, 2, 3, 4, 100000])), list_node([1, 2, 3, 4]))
    assert is_same_list(candidate(nums = [1, 3, 5, 7, 9],head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([0, 2, 4, 6, 8, 10]))
    assert is_same_list(candidate(nums = [2, 4],head = list_node([1, 2, 3, 4, 5])), list_node([1, 3, 5]))
    assert is_same_list(candidate(nums = [5],head = list_node([1, 2, 3, 4])), list_node([1, 2, 3, 4]))
    assert is_same_list(candidate(nums = [10, 20, 30],head = list_node([5, 10, 15, 20, 25, 30, 35])), list_node([5, 15, 25, 35]))
    assert is_same_list(candidate(nums = [10, 20, 30],head = list_node([5, 10, 15, 20, 25, 30])), list_node([5, 15, 25]))
    assert is_same_list(candidate(nums = [100000],head = list_node([99999, 100000, 100001])), list_node([99999, 100001]))
    assert is_same_list(candidate(nums = [1, 3, 5, 7, 9],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([2, 4, 6, 8, 10]))
    assert is_same_list(candidate(nums = [7, 8, 9],head = list_node([7, 8, 9, 10, 11, 12])), list_node([10, 11, 12]))
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
    assert is_same_list(candidate(nums = [5, 10, 15, 20, 25, 30],head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])), list_node([35, 40, 45, 50, 55, 60]))
    assert is_same_list(candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))
    assert is_same_list(candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])), list_node([1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49, 51, 52, 53, 54, 56, 57, 58, 59, 61, 62, 63, 64, 66, 67, 68, 69, 71, 72, 73, 74, 76, 77, 78, 79, 81, 82, 83, 84, 86, 87, 88, 89, 91, 92, 93, 94, 96, 97, 98, 99]))
    assert is_same_list(candidate(nums = [100000],head = list_node([50000, 100000, 150000, 200000])), list_node([50000, 150000, 200000]))
    assert is_same_list(candidate(nums = [1, 3, 5, 7, 9],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([2, 4, 6, 8, 10]))
    assert is_same_list(candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))
    assert is_same_list(candidate(nums = [1, 3, 5, 7, 9],head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))
    assert is_same_list(candidate(nums = [1000, 2000, 3000, 4000, 5000],head = list_node([5000, 4000, 3000, 2000, 1000, 500, 400, 300, 200, 100])), list_node([500, 400, 300, 200, 100]))
    assert is_same_list(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([16, 17, 18, 19, 20]))
    assert is_same_list(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])), list_node([110, 120, 130, 140, 150, 160, 170, 180, 190, 200]))
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == None
    assert is_same_list(candidate(nums = [1, 3, 5, 7, 9],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([2, 4, 6, 8, 10]))
    assert is_same_list(candidate(nums = [5, 10, 15, 20, 25],head = list_node([1, 5, 10, 15, 20, 25, 30, 35])), list_node([1, 30, 35]))
    assert is_same_list(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],head = list_node([1, 10, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60, 7, 70, 8, 80, 9, 90, 10, 100, 11])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 11]))
    assert is_same_list(candidate(nums = [7, 8, 9],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])), list_node([1, 2, 3, 4, 5, 6, 10, 11, 12, 13]))
    assert is_same_list(candidate(nums = [5, 15, 25, 35, 45, 55],head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])), list_node([10, 20, 30, 40, 50, 60]))
    assert is_same_list(candidate(nums = [2],head = list_node([1, 2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 2, 8, 2, 9, 2, 10, 2])), list_node([1, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(nums = [1, 5, 10, 15, 20],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19]))
    assert is_same_list(candidate(nums = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],head = list_node([1, 90, 2, 91, 3, 92, 4, 93, 5, 94, 6, 95, 7, 96, 8, 97, 9, 98, 10, 99])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])), list_node([31, 32, 33, 34, 35, 36, 37, 38, 39, 40]))
    assert is_same_list(candidate(nums = [1, 4, 9, 16, 25],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])), list_node([2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])), list_node([110, 120, 130, 140, 150]))
    assert is_same_list(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([11, 12, 13, 14, 15]))
    assert is_same_list(candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])), list_node([1, 5, 7, 11, 13, 17, 19, 23, 25, 29, 31]))
    assert is_same_list(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],head = list_node([10, 100, 20, 200, 30, 300, 40, 400, 50, 500, 60, 600, 70, 700, 80, 800, 90, 900, 100, 1000])), list_node([200, 300, 400, 500, 600, 700, 800, 900, 1000]))
    assert is_same_list(candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]))
    assert is_same_list(candidate(nums = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 101]))
    assert is_same_list(candidate(nums = [3, 5, 7, 9, 11],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])), list_node([1, 2, 4, 6, 8, 10, 12]))
    assert is_same_list(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([21, 22, 23, 24, 25]))
    assert is_same_list(candidate(nums = [1, 11, 21, 31, 41, 51],head = list_node([1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151])), list_node([61, 71, 81, 91, 101, 111, 121, 131, 141, 151]))
    assert is_same_list(candidate(nums = [100, 200, 300, 400, 500],head = list_node([100, 150, 200, 250, 300, 350, 400, 450, 500, 550])), list_node([150, 250, 350, 450, 550]))
    assert is_same_list(candidate(nums = [100000],head = list_node([1, 50000, 100000, 150000, 200000])), list_node([1, 50000, 150000, 200000]))
    assert is_same_list(candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70])), list_node([1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 57, 58, 59, 60, 61, 62, 64, 65, 66, 67, 68, 69]))
    assert is_same_list(candidate(nums = [100, 200, 300, 400, 500],head = list_node([50, 100, 150, 200, 250, 300, 350, 400, 450, 500])), list_node([50, 150, 250, 350, 450]))
    assert is_same_list(candidate(nums = [5, 10, 15],head = list_node([1, 5, 10, 15, 20, 25, 30])), list_node([1, 20, 25, 30]))
    assert candidate(nums = [5],head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == None
    assert is_same_list(candidate(nums = [15, 16, 17, 18, 19],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 20]))
    assert is_same_list(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))
    assert is_same_list(candidate(nums = [2, 4, 6, 8],head = list_node([2, 4, 6, 8, 10, 12, 14, 16])), list_node([10, 12, 14, 16]))
    assert is_same_list(candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29]))
    assert is_same_list(candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])), list_node([2, 4, 6, 8, 10, 12, 14, 16]))
    assert is_same_list(candidate(nums = [2, 5, 7, 10],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])), list_node([1, 3, 4, 6, 8, 9, 11]))
    assert is_same_list(candidate(nums = [100000],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100000])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(nums = [1, 100, 1000, 10000, 100000],head = list_node([1, 10, 100, 1000, 10000, 100000])), list_node([10]))
    assert candidate(nums = [1, 2, 3],head = list_node([3, 2, 1, 3, 2, 1, 3, 2, 1])) == None
    assert is_same_list(candidate(nums = [1, 5, 10, 15, 20, 25, 30],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19]))
    assert is_same_list(candidate(nums = [1, 10, 100, 1000, 10000],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100, 1000, 10000])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([11, 12, 13, 14, 15]))
    assert is_same_list(candidate(nums = [1, 100, 10000, 100000],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100, 200, 300, 400, 500, 10000, 20000, 30000, 40000, 50000, 100000])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 200, 300, 400, 500, 20000, 30000, 40000, 50000]))
    assert is_same_list(candidate(nums = [10, 20, 30, 40, 50],head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])), list_node([5, 15, 25, 35, 45, 55]))
    assert is_same_list(candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])), list_node([55, 60, 65, 70, 75, 80, 85, 90, 95, 100]))
    assert candidate(nums = [1, 2, 3],head = list_node([3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1])) == None
    assert is_same_list(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],head = list_node([1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])), list_node([1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]))
    assert is_same_list(candidate(nums = [5, 10, 15, 20, 25],head = list_node([5, 10, 15, 20, 25, 30, 35, 40])), list_node([30, 35, 40]))
    assert is_same_list(candidate(nums = [10, 20, 30, 40, 50],head = list_node([50, 40, 30, 20, 10, 0, -10, -20, -30])), list_node([0, -10, -20, -30]))
    assert is_same_list(candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])), list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))
    assert is_same_list(candidate(nums = [1, 100, 1000, 10000, 100000],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100, 101, 102, 103, 104, 105, 1000, 1001, 1002, 10000, 10001])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 101, 102, 103, 104, 105, 1001, 1002, 10001]))
    assert is_same_list(candidate(nums = [5],head = list_node([1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])), list_node([110, 120, 130, 140, 150]))
    assert is_same_list(candidate(nums = [15, 16, 17, 18, 19, 20],head = list_node([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([10, 11, 12, 13, 14, 21, 22, 23, 24, 25]))
    assert is_same_list(candidate(nums = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],head = list_node([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000])), list_node([110000, 120000, 130000, 140000, 150000]))
    assert is_same_list(candidate(nums = [2, 5, 7, 11, 13],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 3, 4, 6, 8, 9, 10, 12, 14, 15]))
    assert is_same_list(candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19],head = list_node([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])), list_node([23, 29, 31]))
    assert is_same_list(candidate(nums = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])), list_node([2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49]))
    assert is_same_list(candidate(nums = [100, 200, 300, 400, 500],head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900])), list_node([600, 700, 800, 900]))
    assert candidate(nums = [5],head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == None
    assert is_same_list(candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])), list_node([6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
    assert is_same_list(candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 22, 23, 24, 25]))
    assert is_same_list(candidate(nums = [50000, 50001, 50002, 50003, 50004, 50005],head = list_node([49999, 50000, 50001, 50002, 50003, 50004, 50005, 50006])), list_node([49999, 50006]))
    assert is_same_list(candidate(nums = [5, 25, 45, 65, 85, 105],head = list_node([5, 20, 25, 40, 45, 60, 65, 80, 85, 100, 105, 120, 130, 140, 150])), list_node([20, 40, 60, 80, 100, 120, 130, 140, 150]))
    assert is_same_list(candidate(nums = [100000],head = list_node([100000, 99999, 99998, 99997, 99996])), list_node([99999, 99998, 99997, 99996]))
    assert is_same_list(candidate(nums = [5, 10, 15, 20, 25],head = list_node([1, 5, 9, 10, 14, 19, 20, 24, 25])), list_node([1, 9, 14, 19, 24]))
    assert is_same_list(candidate(nums = [20, 40, 60, 80, 100],head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])), list_node([10, 30, 50, 70, 90, 110]))
    assert is_same_list(candidate(nums = [1, 10, 100, 1000, 10000, 100000],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 200000])), list_node([2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 200, 300, 400, 500, 600, 700, 800, 900, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 200000]))
    assert is_same_list(candidate(nums = [1, 3, 5, 7, 9, 11],head = list_node([2, 4, 6, 8, 10, 12, 14])), list_node([2, 4, 6, 8, 10, 12, 14]))
    assert is_same_list(candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]))


