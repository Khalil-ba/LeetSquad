def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3],h = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3],h = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(piles = [805306400, 805306400, 805306400],h = 3000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [805306400, 805306400, 805306400],h = 3000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1000000000],h = 1000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1000000000],h = 1000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(piles = [805306457, 805306457, 805306457],h = 1000000000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [805306457, 805306457, 805306457],h = 1000000000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(piles = [30, 11, 23, 4, 20],h = 5) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [30, 11, 23, 4, 20],h = 5) == 30: {e}')
    
    total += 1
    try:
        result = candidate(piles = [805306457, 933693859, 908256970, 820324087, 610103336],h = 5) == 933693859
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [805306457, 933693859, 908256970, 820324087, 610103336],h = 5) == 933693859: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 1, 1],h = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 1, 1],h = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 10, 10, 10],h = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 10, 10, 10],h = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 3, 3, 3, 3],h = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 3, 3, 3, 3],h = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 3, 3, 3, 3],h = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 3, 3, 3, 3],h = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 6, 7, 11],h = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 6, 7, 11],h = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1],h = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1],h = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 6, 7, 11],h = 8) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 6, 7, 11],h = 8) == 4: {e}')
    
    total += 1
    try:
        result = candidate(piles = [8, 9, 7, 4, 2],h = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [8, 9, 7, 4, 2],h = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 999999999],h = 2) == 999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 999999999],h = 2) == 999999999: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3],h = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3],h = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(piles = [805306368, 805306368, 805306368],h = 1000000000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [805306368, 805306368, 805306368],h = 1000000000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1000000000, 1000000000, 1000000000],h = 3) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1000000000, 1000000000, 1000000000],h = 3) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(piles = [30, 11, 23, 4, 20],h = 6) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [30, 11, 23, 4, 20],h = 6) == 23: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],h = 10) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],h = 10) == 3: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 1, 1, 1],h = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 1, 1, 1],h = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(piles = [30, 11, 23, 4, 20, 35],h = 7) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [30, 11, 23, 4, 20, 35],h = 7) == 30: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],h = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],h = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],h = 20) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],h = 20) == 35: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],h = 5) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],h = 5) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],h = 10) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],h = 10) == 19: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],h = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],h = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 8, 6, 29, 33, 12],h = 9) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 8, 6, 29, 33, 12],h = 9) == 15: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 8, 6, 12, 20],h = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 8, 6, 12, 20],h = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 8, 10, 12, 15, 17, 20, 23, 25, 28, 30, 33, 35, 38, 40],h = 15) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 8, 10, 12, 15, 17, 20, 23, 25, 28, 30, 33, 35, 38, 40],h = 15) == 40: {e}')
    
    total += 1
    try:
        result = candidate(piles = [332484035, 524908576, 855865114, 632739624, 265801521],h = 8) == 427932557
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [332484035, 524908576, 855865114, 632739624, 265801521],h = 8) == 427932557: {e}')
    
    total += 1
    try:
        result = candidate(piles = [312884470],h = 312884469) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [312884470],h = 312884469) == 2: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 6, 7, 11, 30, 20],h = 15) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 6, 7, 11, 30, 20],h = 15) == 6: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 8, 6, 3],h = 15) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 8, 6, 3],h = 15) == 2: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],h = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],h = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1000000000, 999999999, 888888888, 777777777],h = 10) == 444444444
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1000000000, 999999999, 888888888, 777777777],h = 10) == 444444444: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000],h = 9) == 100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000],h = 9) == 100000000: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 10, 100, 1000, 10000, 100000],h = 6) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 10, 100, 1000, 10000, 100000],h = 6) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],h = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],h = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 6, 7, 11, 20, 25, 30],h = 15) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 6, 7, 11, 20, 25, 30],h = 15) == 9: {e}')
    
    total += 1
    try:
        result = candidate(piles = [50, 25, 75, 25, 100, 50, 25, 75, 25, 100, 50, 25, 75, 25, 100, 50, 25, 75, 25, 100],h = 50) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [50, 25, 75, 25, 100, 50, 25, 75, 25, 100, 50, 25, 75, 25, 100, 50, 25, 75, 25, 100],h = 50) == 25: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],h = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],h = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(piles = [9, 8, 7, 6, 5, 4, 3, 2, 1],h = 9) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [9, 8, 7, 6, 5, 4, 3, 2, 1],h = 9) == 9: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],h = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],h = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 10, 100, 1000, 10000, 100000, 1000000],h = 14) == 125000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 10, 100, 1000, 10000, 100000, 1000000],h = 14) == 125000: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],h = 25) == 66666667
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],h = 25) == 66666667: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 20, 30, 40, 50],h = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 20, 30, 40, 50],h = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],h = 15) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],h = 15) == 26: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1000000000, 1, 1000000000, 1, 1000000000],h = 1000000000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1000000000, 1, 1000000000, 1, 1000000000],h = 1000000000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 6, 7, 11, 11, 11, 11, 11, 11, 11],h = 10) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 6, 7, 11, 11, 11, 11, 11, 11, 11],h = 10) == 11: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 6, 7, 11, 20, 30, 40, 50, 60, 70, 80, 90, 100],h = 15) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 6, 7, 11, 20, 30, 40, 50, 60, 70, 80, 90, 100],h = 15) == 80: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 8, 6, 7, 1, 2, 3, 4, 5],h = 9) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 8, 6, 7, 1, 2, 3, 4, 5],h = 9) == 8: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],h = 100) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],h = 100) == 3: {e}')
    
    total += 1
    try:
        result = candidate(piles = [9, 8, 7, 6, 5, 4, 3, 2, 1],h = 5) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [9, 8, 7, 6, 5, 4, 3, 2, 1],h = 5) == 10: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],h = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],h = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(piles = [100, 200, 300, 400, 500],h = 50) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [100, 200, 300, 400, 500],h = 50) == 32: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1000000000, 1000000000, 1000000000],h = 3) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1000000000, 1000000000, 1000000000],h = 3) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],h = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],h = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 10) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 10) == 2: {e}')
    
    total += 1
    try:
        result = candidate(piles = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],h = 100) == 234
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],h = 100) == 234: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],h = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],h = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(piles = [300000000, 100000000, 200000000, 400000000, 500000000],h = 1000000000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [300000000, 100000000, 200000000, 400000000, 500000000],h = 1000000000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],h = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],h = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 4, 3, 2, 1],h = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 4, 3, 2, 1],h = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],h = 10) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],h = 10) == 100: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],h = 9) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],h = 9) == 20: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 10, 100, 1000, 10000],h = 10) == 1667
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 10, 100, 1000, 10000],h = 10) == 1667: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(piles = [100, 150, 200, 250, 300, 350, 400],h = 15) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [100, 150, 200, 250, 300, 350, 400],h = 15) == 150: {e}')
    
    total += 1
    try:
        result = candidate(piles = [100000000, 200000000, 300000000, 400000000, 500000000],h = 5) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [100000000, 200000000, 300000000, 400000000, 500000000],h = 5) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 6, 7, 11, 100, 101, 200],h = 20) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 6, 7, 11, 100, 101, 200],h = 20) == 26: {e}')
    
    total += 1
    try:
        result = candidate(piles = [8, 5, 6, 10, 12],h = 7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [8, 5, 6, 10, 12],h = 7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(piles = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],h = 10) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],h = 10) == 100: {e}')
    
    total += 1
    try:
        result = candidate(piles = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],h = 50) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],h = 50) == 120: {e}')
    
    total += 1
    try:
        result = candidate(piles = [100, 100, 100, 100, 100],h = 10) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [100, 100, 100, 100, 100],h = 10) == 50: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1000000000, 1000000000, 1000000000],h = 1000000000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1000000000, 1000000000, 1000000000],h = 1000000000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 19) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 19) == 2: {e}')
    
    total += 1
    try:
        result = candidate(piles = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],h = 100) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],h = 100) == 5: {e}')
    
    total += 1
    try:
        result = candidate(piles = [332484035, 524900671, 855865114, 632088198, 232463062],h = 8) == 427932557
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [332484035, 524900671, 855865114, 632088198, 232463062],h = 8) == 427932557: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],h = 10) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],h = 10) == 5: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],h = 15) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],h = 15) == 10: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],h = 9) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],h = 9) == 11: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 15, 20, 25, 30, 35, 40],h = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 15, 20, 25, 30, 35, 40],h = 20) == 10: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],h = 10000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],h = 10000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],h = 5) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],h = 5) == 101: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],h = 15) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],h = 15) == 50: {e}')
    
    total += 1
    try:
        result = candidate(piles = [805306368, 805306368, 805306368],h = 1000000000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [805306368, 805306368, 805306368],h = 1000000000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(piles = [900000000, 800000000, 700000000, 600000000, 500000000],h = 5) == 900000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [900000000, 800000000, 700000000, 600000000, 500000000],h = 5) == 900000000: {e}')
    
    total += 1
    try:
        result = candidate(piles = [8, 5, 4, 10, 7, 9, 6],h = 15) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [8, 5, 4, 10, 7, 9, 6],h = 15) == 4: {e}')
    
    total += 1
    try:
        result = candidate(piles = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],h = 15) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],h = 15) == 25: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 15, 7, 30],h = 6) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 15, 7, 30],h = 6) == 15: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 6, 7, 11, 33, 45, 55],h = 25) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 6, 7, 11, 33, 45, 55],h = 25) == 7: {e}')
    
    total += 1
    try:
        result = candidate(piles = [8, 12, 15, 18, 22],h = 12) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [8, 12, 15, 18, 22],h = 12) == 8: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 6, 7, 11, 11, 11, 11, 11, 11, 11],h = 20) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 6, 7, 11, 11, 11, 11, 11, 11, 11],h = 20) == 6: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 20, 30, 40, 50],h = 20) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 20, 30, 40, 50],h = 20) == 9: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],h = 9) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],h = 9) == 11: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1000000000, 1000000000, 1000000000],h = 3000000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1000000000, 1000000000, 1000000000],h = 3000000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 20) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 20) == 1: {e}')
    
    total += 1
    try:
        result = candidate(piles = [3, 6, 7, 11, 20, 25, 30],h = 25) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [3, 6, 7, 11, 20, 25, 30],h = 25) == 5: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],h = 32) == 250000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],h = 32) == 250000000: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],h = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],h = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(piles = [999999999, 999999998, 999999997, 999999996, 999999995],h = 10) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [999999999, 999999998, 999999997, 999999996, 999999995],h = 10) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],h = 15) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],h = 15) == 21: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],h = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],h = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(piles = [33, 41, 17, 29, 38, 36, 40, 9, 66, 27],h = 13) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [33, 41, 17, 29, 38, 36, 40, 9, 66, 27],h = 13) == 38: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 10) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 10) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],h = 9) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],h = 9) == 20: {e}')
    
    total += 1
    try:
        result = candidate(piles = [30, 11, 23, 4, 20],h = 7) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [30, 11, 23, 4, 20],h = 7) == 20: {e}')
    
    total += 1
    try:
        result = candidate(piles = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],h = 5) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],h = 5) == 9: {e}')
    
    total += 1
    try:
        result = candidate(piles = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],h = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],h = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],h = 5) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],h = 5) == 11: {e}')
    
    total += 1
    try:
        result = candidate(piles = [987654321, 123456789, 987654321, 123456789, 987654321],h = 5) == 987654321
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [987654321, 123456789, 987654321, 123456789, 987654321],h = 5) == 987654321: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],h = 1) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],h = 1) == 11: {e}')
    
    total += 1
    try:
        result = candidate(piles = [2, 4, 9, 16, 25, 36, 49, 64, 81, 100],h = 15) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [2, 4, 9, 16, 25, 36, 49, 64, 81, 100],h = 15) == 41: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],h = 25) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],h = 25) == 27: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100],h = 20) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100],h = 20) == 100: {e}')
    
    total += 1
    try:
        result = candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],h = 1) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],h = 1) == 11: {e}')
    
    total += 1
    try:
        result = candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],h = 20) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],h = 20) == 4: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(piles = [1, 2, 3],h = 5) == 2
    assert candidate(piles = [805306400, 805306400, 805306400],h = 3000000000) == 1
    assert candidate(piles = [1000000000],h = 1000000000) == 1
    assert candidate(piles = [805306457, 805306457, 805306457],h = 1000000000) == 3
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 5) == 2
    assert candidate(piles = [30, 11, 23, 4, 20],h = 5) == 30
    assert candidate(piles = [805306457, 933693859, 908256970, 820324087, 610103336],h = 5) == 933693859
    assert candidate(piles = [1, 1, 1, 1],h = 4) == 1
    assert candidate(piles = [10, 10, 10, 10],h = 10) == 5
    assert candidate(piles = [3, 3, 3, 3, 3],h = 5) == 3
    assert candidate(piles = [3, 3, 3, 3, 3],h = 10) == 2
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 10) == 1
    assert candidate(piles = [3, 6, 7, 11],h = 10) == 3
    assert candidate(piles = [1],h = 1) == 1
    assert candidate(piles = [3, 6, 7, 11],h = 8) == 4
    assert candidate(piles = [8, 9, 7, 4, 2],h = 3) == 10
    assert candidate(piles = [1, 999999999],h = 2) == 999999999
    assert candidate(piles = [1, 2, 3],h = 3) == 3
    assert candidate(piles = [805306368, 805306368, 805306368],h = 1000000000) == 3
    assert candidate(piles = [1000000000, 1000000000, 1000000000],h = 3) == 1000000000
    assert candidate(piles = [30, 11, 23, 4, 20],h = 6) == 23
    assert candidate(piles = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],h = 10) == 3
    assert candidate(piles = [1, 1, 1, 1, 1],h = 5) == 1
    assert candidate(piles = [30, 11, 23, 4, 20, 35],h = 7) == 30
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],h = 10) == 10
    assert candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],h = 20) == 35
    assert candidate(piles = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000],h = 5) == 1000000000
    assert candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],h = 10) == 19
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],h = 10) == 10
    assert candidate(piles = [5, 8, 6, 29, 33, 12],h = 9) == 15
    assert candidate(piles = [5, 8, 6, 12, 20],h = 5) == 20
    assert candidate(piles = [5, 8, 10, 12, 15, 17, 20, 23, 25, 28, 30, 33, 35, 38, 40],h = 15) == 40
    assert candidate(piles = [332484035, 524908576, 855865114, 632739624, 265801521],h = 8) == 427932557
    assert candidate(piles = [312884470],h = 312884469) == 2
    assert candidate(piles = [3, 6, 7, 11, 30, 20],h = 15) == 6
    assert candidate(piles = [5, 8, 6, 3],h = 15) == 2
    assert candidate(piles = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],h = 5) == 11
    assert candidate(piles = [1000000000, 999999999, 888888888, 777777777],h = 10) == 444444444
    assert candidate(piles = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000],h = 9) == 100000000
    assert candidate(piles = [1, 10, 100, 1000, 10000, 100000],h = 6) == 100000
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 100) == 1
    assert candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],h = 10) == 10
    assert candidate(piles = [3, 6, 7, 11, 20, 25, 30],h = 15) == 9
    assert candidate(piles = [50, 25, 75, 25, 100, 50, 25, 75, 25, 100, 50, 25, 75, 25, 100, 50, 25, 75, 25, 100],h = 50) == 25
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],h = 15) == 15
    assert candidate(piles = [9, 8, 7, 6, 5, 4, 3, 2, 1],h = 9) == 9
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],h = 20) == 20
    assert candidate(piles = [1, 10, 100, 1000, 10000, 100000, 1000000],h = 14) == 125000
    assert candidate(piles = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],h = 25) == 66666667
    assert candidate(piles = [10, 20, 30, 40, 50],h = 100) == 2
    assert candidate(piles = [5, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],h = 15) == 26
    assert candidate(piles = [1000000000, 1, 1000000000, 1, 1000000000],h = 1000000000) == 4
    assert candidate(piles = [3, 6, 7, 11, 11, 11, 11, 11, 11, 11],h = 10) == 11
    assert candidate(piles = [3, 6, 7, 11, 20, 30, 40, 50, 60, 70, 80, 90, 100],h = 15) == 80
    assert candidate(piles = [5, 8, 6, 7, 1, 2, 3, 4, 5],h = 9) == 8
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],h = 100) == 3
    assert candidate(piles = [9, 8, 7, 6, 5, 4, 3, 2, 1],h = 5) == 10
    assert candidate(piles = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],h = 20) == 10
    assert candidate(piles = [100, 200, 300, 400, 500],h = 50) == 32
    assert candidate(piles = [1000000000, 1000000000, 1000000000],h = 3) == 1000000000
    assert candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],h = 10) == 10
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 10) == 2
    assert candidate(piles = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],h = 100) == 234
    assert candidate(piles = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],h = 10) == 6
    assert candidate(piles = [300000000, 100000000, 200000000, 400000000, 500000000],h = 1000000000) == 2
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 100) == 1
    assert candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],h = 5) == 11
    assert candidate(piles = [5, 4, 3, 2, 1],h = 15) == 1
    assert candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],h = 10) == 100
    assert candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],h = 9) == 20
    assert candidate(piles = [1, 10, 100, 1000, 10000],h = 10) == 1667
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 1) == 2
    assert candidate(piles = [100, 150, 200, 250, 300, 350, 400],h = 15) == 150
    assert candidate(piles = [100000000, 200000000, 300000000, 400000000, 500000000],h = 5) == 500000000
    assert candidate(piles = [3, 6, 7, 11, 100, 101, 200],h = 20) == 26
    assert candidate(piles = [8, 5, 6, 10, 12],h = 7) == 8
    assert candidate(piles = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],h = 10) == 100
    assert candidate(piles = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],h = 50) == 120
    assert candidate(piles = [100, 100, 100, 100, 100],h = 10) == 50
    assert candidate(piles = [1000000000, 1000000000, 1000000000],h = 1000000000) == 4
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 19) == 2
    assert candidate(piles = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],h = 100) == 5
    assert candidate(piles = [332484035, 524900671, 855865114, 632088198, 232463062],h = 8) == 427932557
    assert candidate(piles = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],h = 10) == 5
    assert candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],h = 15) == 10
    assert candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],h = 9) == 11
    assert candidate(piles = [10, 15, 20, 25, 30, 35, 40],h = 20) == 10
    assert candidate(piles = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],h = 10000) == 1
    assert candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],h = 5) == 101
    assert candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],h = 15) == 50
    assert candidate(piles = [805306368, 805306368, 805306368],h = 1000000000) == 3
    assert candidate(piles = [900000000, 800000000, 700000000, 600000000, 500000000],h = 5) == 900000000
    assert candidate(piles = [8, 5, 4, 10, 7, 9, 6],h = 15) == 4
    assert candidate(piles = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],h = 15) == 25
    assert candidate(piles = [10, 15, 7, 30],h = 6) == 15
    assert candidate(piles = [3, 6, 7, 11, 33, 45, 55],h = 25) == 7
    assert candidate(piles = [8, 12, 15, 18, 22],h = 12) == 8
    assert candidate(piles = [3, 6, 7, 11, 11, 11, 11, 11, 11, 11],h = 20) == 6
    assert candidate(piles = [10, 20, 30, 40, 50],h = 20) == 9
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],h = 9) == 11
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 5) == 2
    assert candidate(piles = [1000000000, 1000000000, 1000000000],h = 3000000000) == 1
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 20) == 1
    assert candidate(piles = [3, 6, 7, 11, 20, 25, 30],h = 25) == 5
    assert candidate(piles = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000],h = 32) == 250000000
    assert candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],h = 5) == 20
    assert candidate(piles = [999999999, 999999998, 999999997, 999999996, 999999995],h = 10) == 500000000
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],h = 15) == 21
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],h = 5) == 11
    assert candidate(piles = [33, 41, 17, 29, 38, 36, 40, 9, 66, 27],h = 13) == 38
    assert candidate(piles = [1000000000, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 10) == 1000000000
    assert candidate(piles = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],h = 9) == 20
    assert candidate(piles = [30, 11, 23, 4, 20],h = 7) == 20
    assert candidate(piles = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8],h = 5) == 9
    assert candidate(piles = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],h = 20) == 20
    assert candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],h = 5) == 11
    assert candidate(piles = [987654321, 123456789, 987654321, 123456789, 987654321],h = 5) == 987654321
    assert candidate(piles = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],h = 1) == 11
    assert candidate(piles = [2, 4, 9, 16, 25, 36, 49, 64, 81, 100],h = 15) == 41
    assert candidate(piles = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],h = 25) == 27
    assert candidate(piles = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],h = 10) == 1
    assert candidate(piles = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100],h = 20) == 100
    assert candidate(piles = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],h = 1) == 11
    assert candidate(piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],h = 20) == 4


