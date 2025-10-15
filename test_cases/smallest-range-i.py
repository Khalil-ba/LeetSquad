def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400],k = 100) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400],k = 100) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 4, 200, 1, 3, 2],k = 3) == 193
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 4, 200, 1, 3, 2],k = 3) == 193: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10000],k = 10000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10000],k = 10000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 8, 15, 16, 23, 42],k = 10) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 8, 15, 16, 23, 42],k = 10) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [4, 7, 8, 9],k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [4, 7, 8, 9],k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],k = 150) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],k = 150) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],k = 10000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],k = 10000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1000, 10000],k = 500) == 8900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1000, 10000],k = 500) == 8900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10000],k = 5000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10000],k = 5000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30],k = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30],k = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 10],k = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 10],k = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],k = 100) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],k = 100) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 0) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 0) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 25) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 25) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 9, 13, 17],k = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 9, 13, 17],k = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 200, 300, 400, 500],k = 150) == 199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 200, 300, 400, 500],k = 150) == 199: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900],k = 200) == 499
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900],k = 200) == 499: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10000, 20000, 30000, 40000],k = 5000) == 29999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10000, 20000, 30000, 40000],k = 5000) == 29999: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 15) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 15) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800],k = 100) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800],k = 100) == 500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],k = 0) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],k = 0) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 350) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 350) == 200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 10000, 10000, 10000, 10000],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 10000, 10000, 10000, 10000],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 2],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 2],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 300) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 300) == 300: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 10) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 10) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5000, 5000, 5000, 5000, 5000],k = 2500) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5000, 5000, 5000, 5000, 5000],k = 2500) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000, 2000, 3000, 4000],k = 500) == 2999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000, 2000, 3000, 4000],k = 500) == 2999: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900],k = 250) == 399
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900],k = 250) == 399: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],k = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],k = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10],k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10],k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 9999, 9998, 9997, 9996, 9995],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 9999, 9998, 9997, 9996, 9995],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 2500) == 4000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 2500) == 4000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70],k = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70],k = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 12) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 12) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 150) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 150) == 600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],k = 500) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],k = 500) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 450) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 450) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30],k = 5) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30],k = 5) == 15: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 20) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 20) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 1) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 1) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000],k = 5000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000],k = 5000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 80: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 2, 5, 10, 8, 12, 4, 6],k = 3) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 2, 5, 10, 8, 12, 4, 6],k = 3) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70],k = 15) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70],k = 15) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000, 10000, 100000, 1000000],k = 50000) == 899999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000, 10000, 100000, 1000000],k = 50000) == 899999: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 50) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 50) == 800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 2) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 2) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25],k = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25],k = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000],k = 2500) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000],k = 2500) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500],k = 250) == 1900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500],k = 250) == 1900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 10000, 10000, 10000, 10000],k = 10000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 10000, 10000, 10000, 10000],k = 10000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10],k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10],k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30],k = 3) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30],k = 3) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 1000) == 7000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 1000) == 7000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 50: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 2) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 2) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5000, 5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009],k = 500) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5000, 5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009],k = 500) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10000, 20000, 30000, 40000],k = 9999) == 20001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10000, 20000, 30000, 40000],k = 9999) == 20001: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5],k = 1000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5],k = 1000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10],k = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10],k = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 10000, 10000, 10000, 10000],k = 5000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 10000, 10000, 10000, 10000],k = 5000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10000],k = 5000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10000],k = 5000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 300) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 300) == 800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1000, 2000, 3000, 4000, 5000],k = 2500) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1000, 2000, 3000, 4000, 5000],k = 2500) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 25) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 25) == 140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 9999, 99999, 999999, 9999999],k = 500000) == 8999000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 9999, 99999, 999999, 9999999],k = 500000) == 8999000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, 0, 5, 10],k = 3) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, 0, 5, 10],k = 3) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000],k = 1000) == 7999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000],k = 1000) == 7999: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 20) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 20) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000],k = 500) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000],k = 500) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 10) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 10) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000],k = 2000) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000],k = 2000) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 500) == 8000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 500) == 8000: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [100, 200, 300, 400],k = 100) == 100
    assert candidate(nums = [100, 4, 200, 1, 3, 2],k = 3) == 193
    assert candidate(nums = [1, 10000],k = 10000) == 0
    assert candidate(nums = [5, 5, 5, 5],k = 1) == 0
    assert candidate(nums = [5, 5, 5, 5],k = 5) == 0
    assert candidate(nums = [1, 3, 6],k = 3) == 0
    assert candidate(nums = [5, 5, 5, 5, 5],k = 10) == 0
    assert candidate(nums = [0, 0, 0, 0, 0],k = 0) == 0
    assert candidate(nums = [5, 5, 5],k = 5) == 0
    assert candidate(nums = [1, 2, 3, 4, 5],k = 5) == 0
    assert candidate(nums = [4, 8, 15, 16, 23, 42],k = 10) == 18
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 3) == 3
    assert candidate(nums = [10, 10, 10, 10],k = 5) == 0
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],k = 1) == 7
    assert candidate(nums = [1],k = 0) == 0
    assert candidate(nums = [4, 7, 8, 9],k = 2) == 1
    assert candidate(nums = [10, 10, 10],k = 5) == 0
    assert candidate(nums = [100, 200, 300, 400, 500],k = 150) == 100
    assert candidate(nums = [5, 5, 5, 5, 5],k = 10000) == 0
    assert candidate(nums = [100, 1000, 10000],k = 500) == 8900
    assert candidate(nums = [1, 10000],k = 5000) == 0
    assert candidate(nums = [10, 15, 20, 25, 30],k = 5) == 10
    assert candidate(nums = [10, 15, 20],k = 5) == 0
    assert candidate(nums = [0, 10],k = 2) == 6
    assert candidate(nums = [100, 200, 300, 400, 500],k = 100) == 200
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 0) == 9
    assert candidate(nums = [1, 2, 3, 4, 5],k = 1) == 2
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 100) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1],k = 5) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 7) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 0
    assert candidate(nums = [10, 20, 30, 40, 50],k = 25) == 0
    assert candidate(nums = [1, 5, 9, 13, 17],k = 3) == 10
    assert candidate(nums = [1, 100, 200, 300, 400, 500],k = 150) == 199
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 5) == 0
    assert candidate(nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],k = 1000) == 0
    assert candidate(nums = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900],k = 200) == 499
    assert candidate(nums = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4],k = 1) == 1
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 10) == 8
    assert candidate(nums = [1, 10000, 20000, 30000, 40000],k = 5000) == 29999
    assert candidate(nums = [1, 3, 5, 7, 9],k = 4) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 3) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 15) == 60
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800],k = 100) == 500
    assert candidate(nums = [10, 20, 30, 40, 50],k = 0) == 40
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 350) == 200
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5],k = 3) == 0
    assert candidate(nums = [10000, 10000, 10000, 10000, 10000],k = 1) == 0
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 1) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 20) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 10) == 0
    assert candidate(nums = [1, 1, 1, 1, 2],k = 1) == 0
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 300) == 300
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],k = 10) == 8
    assert candidate(nums = [5000, 5000, 5000, 5000, 5000],k = 2500) == 0
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],k = 5) == 0
    assert candidate(nums = [1, 2, 2, 3, 3, 4, 4, 5, 5],k = 2) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 0) == 0
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 3) == 0
    assert candidate(nums = [1, 1000, 2000, 3000, 4000],k = 500) == 2999
    assert candidate(nums = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900],k = 250) == 399
    assert candidate(nums = [5, 5, 5, 5, 5],k = 100) == 0
    assert candidate(nums = [2, 4, 6, 8, 10],k = 2) == 4
    assert candidate(nums = [10000, 9999, 9998, 9997, 9996, 9995],k = 5) == 0
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 2500) == 4000
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 5) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70],k = 20) == 20
    assert candidate(nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],k = 2) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 12) == 5
    assert candidate(nums = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 1) == 0
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 150) == 600
    assert candidate(nums = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],k = 500) == 0
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 450) == 0
    assert candidate(nums = [5, 10, 15, 20, 25, 30],k = 5) == 15
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 20) == 100
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 1) == 17
    assert candidate(nums = [1, 10000, 1, 10000, 1, 10000, 1, 10000, 1, 10000],k = 5000) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 5) == 80
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 5) == 8
    assert candidate(nums = [7, 2, 5, 10, 8, 12, 4, 6],k = 3) == 4
    assert candidate(nums = [5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000],k = 0) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 50
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70],k = 15) == 30
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 1
    assert candidate(nums = [1, 1000, 10000, 100000, 1000000],k = 50000) == 899999
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 50) == 800
    assert candidate(nums = [5, 5, 5, 5, 5],k = 2) == 0
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 2) == 14
    assert candidate(nums = [5, 10, 15, 20, 25],k = 12) == 0
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 1) == 0
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1000) == 0
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000],k = 2500) == 0
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500],k = 250) == 1900
    assert candidate(nums = [1, 1, 1, 1, 1],k = 10) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 5) == 9
    assert candidate(nums = [10000, 10000, 10000, 10000, 10000],k = 10000) == 0
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10],k = 2) == 5
    assert candidate(nums = [5, 10, 15, 20, 25, 30],k = 3) == 19
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 1000) == 7000
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 50
    assert candidate(nums = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],k = 5) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 2) == 10
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],k = 5) == 0
    assert candidate(nums = [5000, 5001, 5002, 5003, 5004, 5005, 5006, 5007, 5008, 5009],k = 500) == 0
    assert candidate(nums = [1, 10000, 20000, 30000, 40000],k = 9999) == 20001
    assert candidate(nums = [5, 5, 5, 5, 5],k = 1000) == 0
    assert candidate(nums = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10],k = 1) == 7
    assert candidate(nums = [10000, 10000, 10000, 10000, 10000],k = 5000) == 0
    assert candidate(nums = [1, 10000],k = 5000) == 0
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],k = 300) == 800
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 0
    assert candidate(nums = [1, 1000, 2000, 3000, 4000, 5000],k = 2500) == 0
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 25) == 140
    assert candidate(nums = [1, 3, 5, 7, 9],k = 4) == 0
    assert candidate(nums = [999, 9999, 99999, 999999, 9999999],k = 500000) == 8999000
    assert candidate(nums = [-10, -5, 0, 5, 10],k = 3) == 14
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],k = 1) == 2
    assert candidate(nums = [1, 10, 100, 1000, 10000],k = 1000) == 7999
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 2) == 5
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 20) == 150
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000],k = 500) == 3000
    assert candidate(nums = [1, 2, 3, 4, 5],k = 10) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],k = 10) == 4
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000],k = 2000) == 0
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 4) == 1
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 500) == 8000


