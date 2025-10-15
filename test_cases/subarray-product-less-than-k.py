def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [10, 2, 5, 6, 1],k = 100) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2, 5, 6, 1],k = 100) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 100) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 100) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 5, 1, 2, 3],k = 100) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 5, 1, 2, 3],k = 100) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],k = 20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],k = 20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5],k = 30) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5],k = 30) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 4, 9, 1, 3, 6],k = 100) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 4, 9, 1, 3, 6],k = 100) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 4, 5],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 4, 5],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 3, 2, 2, 1],k = 12) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 3, 2, 2, 1],k = 12) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 5, 8, 9],k = 100) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 5, 8, 9],k = 100) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2, 5, 1],k = 16) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2, 5, 1],k = 16) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 4, 5],k = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 4, 5],k = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2, 5, 3],k = 100) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2, 5, 3],k = 100) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1],k = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1],k = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4],k = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4],k = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 7, 3, 5],k = 25) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 7, 3, 5],k = 25) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 10000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 10000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [6, 6, 6, 6],k = 100) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [6, 6, 6, 6],k = 100) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 1000],k = 1000000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 1000],k = 1000000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 2, 6],k = 100) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 2, 6],k = 100) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],k = 30) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],k = 30) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 1000, 1000],k = 1000000000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 1000, 1000],k = 1000000000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2, 5, 6],k = 100) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2, 5, 6],k = 100) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2, 5, 3, 8],k = 160) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2, 5, 3, 8],k = 160) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5, 6, 10],k = 100) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5, 6, 10],k = 100) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5],k = 25) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5],k = 25) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3],k = 19) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3],k = 19) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],k = 1000000000) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],k = 1000000000) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 1, 10, 100, 1000],k = 500000) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 1, 10, 100, 1000],k = 500000) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10000) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10000) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 15625) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 15625) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 997, 996, 995],k = 1000000) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 997, 996, 995],k = 1000000) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 1000) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 1000) == 99: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3000) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3000) == 36: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 6, 7, 9],k = 50) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 6, 7, 9],k = 50) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128],k = 256) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128],k = 256) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 997, 996],k = 1000000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 997, 996],k = 1000000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 3, 2, 1],k = 20) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 3, 2, 1],k = 20) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1000) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1000) == 26: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1000000) == 174
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1000000) == 174: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 2, 3, 5, 7, 11, 13, 17, 19, 23],k = 1000) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 2, 3, 5, 7, 11, 13, 17, 19, 23],k = 1000) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 4, 5, 6, 7, 8, 9, 10],k = 500) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 4, 5, 6, 7, 8, 9, 10],k = 500) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10000) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10000) == 72: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 500) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 500) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999],k = 998001) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999],k = 998001) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 100) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 100) == 105: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 73, 5, 26, 32, 8, 34, 61, 100],k = 10000) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 73, 5, 26, 32, 8, 34, 61, 100],k = 10000) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 2, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 192
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 2, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 192: {e}')
    
    total += 1
    try:
        result = candidate(nums = [31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 1000000) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 1000000) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 1000000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 1000000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500],k = 1000000000) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500],k = 1000000000) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 2, 6, 1, 1, 1, 1, 1],k = 100) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 2, 6, 1, 1, 1, 1, 1],k = 100) == 38: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999],k = 1000000) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999],k = 1000000) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10000) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10000) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1000) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1000) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 20, 60, 10, 30],k = 1000) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 20, 60, 10, 30],k = 1000) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19],k = 200) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19],k = 200) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 27) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 27) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 1000, 1000, 1000],k = 1000000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 1000, 1000, 1000],k = 1000000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 100000) == 88
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 100000) == 88: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 2, 6, 1, 3, 7, 5, 8, 9],k = 200) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 2, 6, 1, 3, 7, 5, 8, 9],k = 200) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1000) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1000) == 75: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 10000) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 10000) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 100000) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 100000) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128],k = 500) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128],k = 500) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 1000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 1000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 10000) == 182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 10000) == 182: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 2, 6, 1, 3, 7, 5, 8, 9],k = 100) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 2, 6, 1, 3, 7, 5, 8, 9],k = 100) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10, 5, 2, 1, 1, 2, 5, 10, 20, 30, 40, 50],k = 1000) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10, 5, 2, 1, 1, 2, 5, 10, 20, 30, 40, 50],k = 1000) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 1000000) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 1000000) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 1000000000) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 1000000000) == 106: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10000) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10000) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1000000) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1000000) == 28: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 1000000000) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 1000000000) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 2, 6, 1, 3, 7, 5, 8, 9],k = 10) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 2, 6, 1, 3, 7, 5, 8, 9],k = 10) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 2, 6, 3, 4, 1, 7],k = 150) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 2, 6, 3, 4, 1, 7],k = 150) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1000) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1000) == 34: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 100) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 100) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 2, 6, 5, 1, 2, 3, 4, 5, 6, 7],k = 100) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 2, 6, 5, 1, 2, 3, 4, 5, 6, 7],k = 100) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 1000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 1000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 1000) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 1000) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 9, 10, 4, 3, 8, 3, 10, 26, 100, 8],k = 200) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 9, 10, 4, 3, 8, 3, 10, 26, 100, 8],k = 200) == 21: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 100000) == 155
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 100000) == 155: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 500, 250, 125, 62, 31, 15],k = 1000000) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 500, 250, 125, 62, 31, 15],k = 1000000) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 2000) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 2000) == 58: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 10, 1, 0.1, 0.01],k = 1000) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 10, 1, 0.1, 0.01],k = 1000) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995],k = 900000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995],k = 900000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 999, 999, 999, 999],k = 1000000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 999, 999, 999, 999],k = 1000000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 500) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 500) == 61: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 1024) == 234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 1024) == 234: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 2, 6, 1, 3],k = 100) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 2, 6, 1, 3],k = 100) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],k = 1000000) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],k = 1000000) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 1000000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 1000000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 210: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 2, 6, 1, 1],k = 100) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 2, 6, 1, 1],k = 100) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1000000) == 174
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1000000) == 174: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 1000000000) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 1000000000) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 2, 6, 1, 3, 7, 5, 8, 9],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 2, 6, 1, 3, 7, 5, 8, 9],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 2, 6, 3, 8, 1, 9, 4, 7],k = 100) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 2, 6, 3, 8, 1, 9, 4, 7],k = 100) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 243) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 243) == 74: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 25) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 25) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 100) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 100) == 52: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 999, 999, 999],k = 1000000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 999, 999, 999],k = 1000000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 5, 2, 6, 1, 8, 9, 3, 7],k = 100) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 5, 2, 6, 1, 8, 9, 3, 7],k = 100) == 23: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5],k = 20) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5],k = 20) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 16) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 16) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 10000) == 212
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 10000) == 212: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 500) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 500) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 27) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 27) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 500) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 500) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1000) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1000) == 45: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],k = 1000000) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],k = 1000000) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5],k = 1000) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5],k = 1000) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10],k = 10000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10],k = 10000) == 9: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [10, 2, 5, 6, 1],k = 100) == 12
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],k = 100) == 21
    assert candidate(nums = [6, 5, 1, 2, 3],k = 100) == 14
    assert candidate(nums = [5, 5, 5, 5, 5],k = 20) == 5
    assert candidate(nums = [5, 5, 5, 5],k = 30) == 7
    assert candidate(nums = [7, 3, 4, 9, 1, 3, 6],k = 100) == 17
    assert candidate(nums = [2, 3, 4, 5],k = 1) == 0
    assert candidate(nums = [7, 3, 2, 2, 1],k = 12) == 9
    assert candidate(nums = [1, 2, 3],k = 0) == 0
    assert candidate(nums = [1, 3, 7, 5, 8, 9],k = 100) == 12
    assert candidate(nums = [1, 1, 1, 1],k = 1) == 0
    assert candidate(nums = [10, 2, 5, 1],k = 16) == 7
    assert candidate(nums = [2, 3, 4, 5],k = 10) == 5
    assert candidate(nums = [10, 2, 5, 3],k = 100) == 8
    assert candidate(nums = [1, 1, 1, 1],k = 2) == 10
    assert candidate(nums = [1, 2, 3, 4],k = 10) == 7
    assert candidate(nums = [9, 7, 3, 5],k = 25) == 6
    assert candidate(nums = [1, 1, 1],k = 1) == 0
    assert candidate(nums = [10, 20, 30, 40, 50],k = 10000) == 10
    assert candidate(nums = [6, 6, 6, 6],k = 100) == 7
    assert candidate(nums = [1000, 1000, 1000],k = 1000000) == 3
    assert candidate(nums = [10, 5, 2, 6],k = 100) == 8
    assert candidate(nums = [1, 1, 1, 1, 1],k = 1) == 0
    assert candidate(nums = [5, 5, 5, 5, 5],k = 30) == 9
    assert candidate(nums = [1000, 1000, 1000, 1000],k = 1000000000) == 7
    assert candidate(nums = [1, 2, 3, 4, 5],k = 10) == 8
    assert candidate(nums = [10, 2, 5, 6],k = 100) == 8
    assert candidate(nums = [10, 2, 5, 3, 8],k = 160) == 12
    assert candidate(nums = [2, 5, 6, 10],k = 100) == 8
    assert candidate(nums = [5, 5, 5, 5],k = 25) == 4
    assert candidate(nums = [10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3],k = 19) == 18
    assert candidate(nums = [1, 2, 3, 4, 5],k = 1) == 0
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],k = 1000000000) == 27
    assert candidate(nums = [1, 10, 100, 1000, 1, 10, 100, 1000],k = 500000) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10000) == 72
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 15625) == 40
    assert candidate(nums = [1000, 999, 998, 997, 996, 995],k = 1000000) == 11
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 1000) == 99
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
    assert candidate(nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 3000) == 36
    assert candidate(nums = [2, 3, 6, 7, 9],k = 50) == 9
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 210
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128],k = 256) == 11
    assert candidate(nums = [1000, 999, 998, 997, 996],k = 1000000) == 9
    assert candidate(nums = [10, 5, 3, 2, 1],k = 20) == 9
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1000) == 26
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1000000) == 174
    assert candidate(nums = [10, 2, 3, 5, 7, 11, 13, 17, 19, 23],k = 1000) == 25
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
    assert candidate(nums = [3, 4, 5, 6, 7, 8, 9, 10],k = 500) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10000) == 72
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 500) == 29
    assert candidate(nums = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999],k = 998001) == 10
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 100) == 105
    assert candidate(nums = [9, 73, 5, 26, 32, 8, 34, 61, 100],k = 10000) == 22
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 1) == 0
    assert candidate(nums = [10, 5, 2, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 100) == 192
    assert candidate(nums = [31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 1000000) == 27
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1) == 0
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 1000000) == 10
    assert candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500],k = 1000000000) == 27
    assert candidate(nums = [10, 5, 2, 6, 1, 1, 1, 1, 1],k = 100) == 38
    assert candidate(nums = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999],k = 1000000) == 19
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10000) == 20
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1000) == 45
    assert candidate(nums = [100, 50, 20, 60, 10, 30],k = 1000) == 8
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19],k = 200) == 15
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 27) == 19
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 14
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000],k = 1000000) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 100000) == 88
    assert candidate(nums = [10, 5, 2, 6, 1, 3, 7, 5, 8, 9],k = 200) == 30
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1000) == 75
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 10000) == 30
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 100000) == 22
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128],k = 500) == 15
    assert candidate(nums = [10, 20, 30, 40, 50],k = 1000) == 7
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 10000) == 182
    assert candidate(nums = [10, 5, 2, 6, 1, 3, 7, 5, 8, 9],k = 100) == 25
    assert candidate(nums = [50, 40, 30, 20, 10, 5, 2, 1, 1, 2, 5, 10, 20, 30, 40, 50],k = 1000) == 45
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 1000000) == 32
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],k = 1000000000) == 106
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10000) == 41
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],k = 1000000) == 28
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 1000000000) == 34
    assert candidate(nums = [10, 5, 2, 6, 1, 3, 7, 5, 8, 9],k = 10) == 11
    assert candidate(nums = [10, 5, 2, 6, 3, 4, 1, 7],k = 150) == 25
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 1000) == 34
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 100) == 19
    assert candidate(nums = [8, 2, 6, 5, 1, 2, 3, 4, 5, 6, 7],k = 100) == 32
    assert candidate(nums = [10, 20, 30, 40, 50],k = 1000) == 7
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 1000) == 19
    assert candidate(nums = [10, 9, 10, 4, 3, 8, 3, 10, 26, 100, 8],k = 200) == 21
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 100000) == 155
    assert candidate(nums = [1000, 500, 250, 125, 62, 31, 15],k = 1000000) == 15
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 2000) == 58
    assert candidate(nums = [100, 10, 1, 0.1, 0.01],k = 1000) == 11
    assert candidate(nums = [999, 998, 997, 996, 995],k = 900000) == 5
    assert candidate(nums = [999, 999, 999, 999, 999],k = 1000000) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 500) == 61
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 1024) == 234
    assert candidate(nums = [10, 5, 2, 6, 1, 3],k = 100) == 16
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],k = 1000000) == 19
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 1000000) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 2) == 210
    assert candidate(nums = [10, 5, 2, 6, 1, 1],k = 100) == 17
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 50) == 19
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 1000000) == 174
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],k = 1000000000) == 19
    assert candidate(nums = [10, 5, 2, 6, 1, 3, 7, 5, 8, 9],k = 1) == 0
    assert candidate(nums = [10, 5, 2, 6, 3, 8, 1, 9, 4, 7],k = 100) == 24
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 243) == 74
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 25) == 10
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 100) == 52
    assert candidate(nums = [999, 999, 999, 999],k = 1000000) == 7
    assert candidate(nums = [10, 5, 2, 6, 1, 8, 9, 3, 7],k = 100) == 23
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5],k = 20) == 19
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 16) == 27
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 10000) == 212
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],k = 500) == 22
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],k = 27) == 29
    assert candidate(nums = [10, 20, 30, 40, 50],k = 500) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 1000) == 45
    assert candidate(nums = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],k = 1000000) == 30
    assert candidate(nums = [9, 8, 7, 6, 5],k = 1000) == 12
    assert candidate(nums = [10, 10, 10, 10],k = 10000) == 9


