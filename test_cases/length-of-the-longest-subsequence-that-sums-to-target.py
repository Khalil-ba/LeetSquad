def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 7, 8, 10],target = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 7, 8, 10],target = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 6, 7, 8, 9, 10],target = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 6, 7, 8, 9, 10],target = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],target = 50) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],target = 50) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 1],target = 1000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 1],target = 1000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300],target = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300],target = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3],target = 7) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3],target = 7) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 1, 3, 2, 1, 5],target = 7) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 1, 3, 2, 1, 5],target = 7) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1],target = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1],target = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],target = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],target = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],target = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],target = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],target = 9) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],target = 9) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],target = 60) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],target = 60) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],target = 15) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],target = 15) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 500, 500, 500],target = 1000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 500, 500, 500],target = 1000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3],target = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3],target = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],target = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],target = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000],target = 1000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000],target = 1000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 5, 4, 5],target = 3) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 5, 4, 5],target = 3) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],target = 15) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],target = 15) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],target = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],target = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 25) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 25) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],target = 9995) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],target = 9995) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],target = 1998) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],target = 1998) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],target = 600) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],target = 600) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 30) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 30) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 75) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 75) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],target = 210) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],target = 210) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],target = 700) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],target = 700) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980],target = 990) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980],target = 990) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],target = 2970) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],target = 2970) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],target = 500) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],target = 500) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],target = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],target = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [333, 334, 333, 334, 333, 334, 333, 334, 333, 334, 333, 334, 333, 334, 333, 334, 333, 334, 333, 334],target = 1000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [333, 334, 333, 334, 333, 334, 333, 334, 333, 334, 333, 334, 333, 334, 333, 334, 333, 334, 333, 334],target = 1000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 1000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 1000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 50) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 50) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 2500) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 2500) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],target = 400) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],target = 400) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90],target = 900) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90],target = 900) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],target = 500) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],target = 500) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],target = 210) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],target = 210) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 550) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 550) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 50) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 50) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 300) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 300) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 3000) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 3000) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 500, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 1000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 500, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 1000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 100) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 100) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],target = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],target = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 28, 56, 112, 224, 448],target = 500) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 28, 56, 112, 224, 448],target = 500) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 900) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 900) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135],target = 675) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135],target = 675) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 234, 567, 890, 345, 678, 901, 12, 34, 56, 78, 90],target = 2500) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 234, 567, 890, 345, 678, 901, 12, 34, 56, 78, 90],target = 2500) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],target = 1500) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],target = 1500) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 100) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 100) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],target = 1500) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],target = 1500) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],target = 1500) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],target = 1500) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 150) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 150) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 30) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 30) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 27) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 27) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 190) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 190) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 250, 125, 62, 31, 15, 7, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 999) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 250, 125, 62, 31, 15, 7, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 999) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1023) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1023) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],target = 1000) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],target = 1000) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],target = 210) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],target = 210) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 225) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 225) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5],target = 2000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5],target = 2000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],target = 600) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],target = 600) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 300) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 300) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160],target = 600) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160],target = 600) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946],target = 10000) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946],target = 10000) == 12: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],target = 750) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],target = 750) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456, 789, 101, 202, 303, 404, 505, 606, 707],target = 1825) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456, 789, 101, 202, 303, 404, 505, 606, 707],target = 1825) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [250, 125, 62, 31, 15, 7, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 499) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [250, 125, 62, 31, 15, 7, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 499) == 27: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 150) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 150) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],target = 150) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],target = 150) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],target = 100) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],target = 100) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 150) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 150) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 500) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 500) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [333, 334, 333, 334, 333, 334, 333, 334],target = 1000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [333, 334, 333, 334, 333, 334, 333, 334],target = 1000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],target = 420) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],target = 420) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],target = 143) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],target = 143) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509],target = 1500) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509],target = 1500) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 150) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 150) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 20) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 20) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],target = 200) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],target = 200) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1024) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1024) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 20) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120],target = 600) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120],target = 600) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1023) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1023) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986],target = 4950) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986],target = 4950) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 5000) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 5000) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 20) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 20) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],target = 300) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],target = 300) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 50) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 50) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 55) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 55) == 13: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],target = 150) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],target = 150) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],target = 105) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],target = 105) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 300, 200, 100, 50, 25, 10, 5, 1],target = 1000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 300, 200, 100, 50, 25, 10, 5, 1],target = 1000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 15) == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [2, 3, 7, 8, 10],target = 15) == 3
    assert candidate(nums = [1, 2, 3, 5, 6, 7, 8, 9, 10],target = 15) == 4
    assert candidate(nums = [10, 20, 30, 40, 50],target = 50) == 2
    assert candidate(nums = [999, 1],target = 1000) == 2
    assert candidate(nums = [100, 200, 300],target = 100) == 1
    assert candidate(nums = [1, 2, 3],target = 7) == -1
    assert candidate(nums = [4, 1, 3, 2, 1, 5],target = 7) == 4
    assert candidate(nums = [1],target = 1) == 1
    assert candidate(nums = [10, 20, 30, 40, 50],target = 100) == 4
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 5
    assert candidate(nums = [1, 1, 1, 1, 1],target = 3) == 3
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 25) == 5
    assert candidate(nums = [1, 2, 3, 4, 5],target = 9) == 3
    assert candidate(nums = [10, 20, 30, 40, 50],target = 60) == 3
    assert candidate(nums = [5, 5, 5, 5, 5],target = 15) == 3
    assert candidate(nums = [500, 500, 500, 500],target = 1000) == 2
    assert candidate(nums = [1, 2, 3],target = 6) == 3
    assert candidate(nums = [1, 2, 3, 4, 5],target = 1) == 1
    assert candidate(nums = [1000],target = 1000) == 1
    assert candidate(nums = [1, 1, 5, 4, 5],target = 3) == -1
    assert candidate(nums = [1, 2, 3, 4, 5],target = 15) == 5
    assert candidate(nums = [1, 1, 1, 1, 1],target = 5) == 5
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 25) == -1
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 15) == 15
    assert candidate(nums = [999, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 1000) == 2
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],target = 9995) == -1
    assert candidate(nums = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1],target = 1998) == -1
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50],target = 600) == 24
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 30) == 6
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 75) == 7
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],target = 210) == 11
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],target = 700) == 13
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980],target = 990) == 1
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],target = 2970) == -1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],target = 500) == 22
    assert candidate(nums = [10, 20, 30, 40, 50],target = 100) == 4
    assert candidate(nums = [333, 334, 333, 334, 333, 334, 333, 334, 333, 334, 333, 334, 333, 334, 333, 334, 333, 334, 333, 334],target = 1000) == 3
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 1000) == 13
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],target = 50) == 9
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 2500) == 6
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80],target = 400) == 9
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 100) == 5
    assert candidate(nums = [10, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90],target = 900) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],target = 500) == 9
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],target = 210) == 7
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 550) == 10
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 50) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 300) == 7
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 3000) == 7
    assert candidate(nums = [999, 500, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 1000) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 100) == 13
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],target = 100) == 5
    assert candidate(nums = [7, 14, 28, 56, 112, 224, 448],target = 500) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 900) == 12
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 5
    assert candidate(nums = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126, 135],target = 675) == 11
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 10
    assert candidate(nums = [123, 456, 789, 234, 567, 890, 345, 678, 901, 12, 34, 56, 78, 90],target = 2500) == -1
    assert candidate(nums = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],target = 1500) == 7
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 5
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],target = 100) == 10
    assert candidate(nums = [100, 200, 300, 400, 500],target = 1500) == 5
    assert candidate(nums = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],target = 1500) == 7
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 150) == 5
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 30) == 10
    assert candidate(nums = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],target = 27) == 9
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],target = 190) == 19
    assert candidate(nums = [500, 250, 125, 62, 31, 15, 7, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 999) == 16
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1023) == 10
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],target = 1000) == 13
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105],target = 210) == 7
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],target = 225) == 15
    assert candidate(nums = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5],target = 2000) == 5
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45],target = 600) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 300) == 7
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160],target = 600) == 11
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 7) == 7
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946],target = 10000) == 12
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],target = 750) == -1
    assert candidate(nums = [123, 456, 789, 101, 202, 303, 404, 505, 606, 707],target = 1825) == -1
    assert candidate(nums = [250, 125, 62, 31, 15, 7, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 499) == 27
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 150) == 7
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],target = 150) == 16
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 5) == 5
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],target = 100) == 9
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 150) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],target = 500) == 9
    assert candidate(nums = [333, 334, 333, 334, 333, 334, 333, 334],target = 1000) == 3
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140],target = 420) == 10
    assert candidate(nums = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],target = 143) == 5
    assert candidate(nums = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509],target = 1500) == -1
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 150) == 7
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 20) == 8
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],target = 200) == 13
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1024) == -1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 20) == 4
    assert candidate(nums = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120],target = 600) == 11
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1023) == 10
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 10
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986],target = 4950) == 5
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 5000) == 9
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],target = 25) == 5
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 20) == 8
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],target = 300) == 10
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],target = 50) == 6
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],target = 55) == 13
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],target = 150) == 11
    assert candidate(nums = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],target = 105) == 5
    assert candidate(nums = [500, 300, 200, 100, 50, 25, 10, 5, 1],target = 1000) == 3
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],target = 15) == 6


