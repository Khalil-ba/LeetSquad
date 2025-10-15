def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(prices = [99, 99],money = 198) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [99, 99],money = 198) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [99, 1],money = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [99, 1],money = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1],money = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1],money = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1],money = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1],money = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1],money = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1],money = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 2],money = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 2],money = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1],money = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1],money = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1],money = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1],money = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50, 50],money = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50, 50],money = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5],money = 8) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5],money = 8) == 5: {e}')
    
    total += 1
    try:
        result = candidate(prices = [99, 99],money = 198) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [99, 99],money = 198) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5],money = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5],money = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 5, 7, 3],money = 15) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 5, 7, 3],money = 15) == 7: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 1, 100],money = 199) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 1, 100],money = 199) == 98: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30],money = 50) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30],money = 50) == 20: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 40],money = 60) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 40],money = 60) == 30: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 1, 1, 1, 1],money = 101) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 1, 1, 1, 1],money = 101) == 99: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 3],money = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 3],money = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30],money = 50) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30],money = 50) == 20: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30],money = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30],money = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5],money = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5],money = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 2, 2, 2, 2],money = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 2, 2, 2, 2],money = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],money = 98) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],money = 98) == 87: {e}')
    
    total += 1
    try:
        result = candidate(prices = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],money = 8) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],money = 8) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [4, 1, 2, 3, 5, 6, 7, 8, 9, 10],money = 11) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [4, 1, 2, 3, 5, 6, 7, 8, 9, 10],money = 11) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50, 50, 50, 50, 50],money = 99) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50, 50, 50, 50, 50],money = 99) == 99: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],money = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],money = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],money = 199) == 199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],money = 199) == 199: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 3, 7, 9, 2, 6, 8, 1, 4, 10],money = 12) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 3, 7, 9, 2, 6, 8, 1, 4, 10],money = 12) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50, 1, 50, 2, 3, 4, 5],money = 52) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50, 1, 50, 2, 3, 4, 5],money = 52) == 49: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],money = 11) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],money = 11) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 110) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 110) == 80: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],money = 50) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],money = 50) == 45: {e}')
    
    total += 1
    try:
        result = candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],money = 180) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],money = 180) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150],money = 300) == 285
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150],money = 300) == 285: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1],money = 10) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1],money = 10) == 7: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],money = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],money = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 190) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 190) == 160: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 99, 1, 98, 1, 97, 1, 96, 1, 95],money = 100) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 99, 1, 98, 1, 97, 1, 96, 1, 95],money = 100) == 98: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],money = 150) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],money = 150) == 150: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1],money = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1],money = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],money = 11) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],money = 11) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],money = 199) == 199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],money = 199) == 199: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50, 50, 50, 50, 50],money = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50, 50, 50, 50, 50],money = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [45, 23, 67, 89, 12, 34, 56, 78, 90, 100],money = 140) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [45, 23, 67, 89, 12, 34, 56, 78, 90, 100],money = 140) == 105: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],money = 16) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],money = 16) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],money = 29) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],money = 29) == 26: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],money = 150) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],money = 150) == 90: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50, 25, 75, 100, 20],money = 100) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50, 25, 75, 100, 20],money = 100) == 55: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],money = 18) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],money = 18) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],money = 90) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],money = 90) == 75: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19],money = 200) == 197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19],money = 200) == 197: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1],money = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1],money = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],money = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],money = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],money = 100) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],money = 100) == 100: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],money = 99) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],money = 99) == 99: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50, 51, 49, 48, 52, 53, 47, 46, 54, 55],money = 100) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50, 51, 49, 48, 52, 53, 47, 46, 54, 55],money = 100) == 7: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],money = 10) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],money = 10) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99],money = 198) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99],money = 198) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],money = 101) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],money = 101) == 99: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],money = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],money = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 105) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 105) == 75: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50, 10, 15, 20, 25],money = 55) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50, 10, 15, 20, 25],money = 55) == 30: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 150) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 150) == 120: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],money = 60) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],money = 60) == 51: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],money = 30) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],money = 30) == 27: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81],money = 179) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81],money = 179) == 16: {e}')
    
    total += 1
    try:
        result = candidate(prices = [40, 30, 20, 10, 5, 15, 25, 35, 45, 50],money = 60) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [40, 30, 20, 10, 5, 15, 25, 35, 45, 50],money = 60) == 45: {e}')
    
    total += 1
    try:
        result = candidate(prices = [99, 100, 99, 100],money = 199) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [99, 100, 99, 100],money = 199) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],money = 150) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],money = 150) == 150: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],money = 101) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],money = 101) == 98: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 150) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 150) == 120: {e}')
    
    total += 1
    try:
        result = candidate(prices = [45, 22, 13, 8, 3],money = 60) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [45, 22, 13, 8, 3],money = 60) == 49: {e}')
    
    total += 1
    try:
        result = candidate(prices = [80, 10, 50, 20, 30],money = 60) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [80, 10, 50, 20, 30],money = 60) == 30: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],money = 101) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],money = 101) == 98: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 15, 20, 25, 30, 35, 40],money = 60) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 15, 20, 25, 30, 35, 40],money = 60) == 35: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],money = 39) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],money = 39) == 36: {e}')
    
    total += 1
    try:
        result = candidate(prices = [75, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],money = 100) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [75, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],money = 100) == 50: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 99, 1, 98],money = 100) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 99, 1, 98],money = 100) == 98: {e}')
    
    total += 1
    try:
        result = candidate(prices = [33, 33, 33, 33, 33, 33, 33, 33, 33, 33],money = 66) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [33, 33, 33, 33, 33, 33, 33, 33, 33, 33],money = 66) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],money = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],money = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],money = 15) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],money = 15) == 12: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],money = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],money = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],money = 100) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],money = 100) == 80: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],money = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],money = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 99, 98, 97, 96, 95],money = 193) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 99, 98, 97, 96, 95],money = 193) == 2: {e}')
    
    total += 1
    try:
        result = candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],money = 180) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],money = 180) == 180: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10],money = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10],money = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],money = 100) == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],money = 100) == 97: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],money = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],money = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],money = 80) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],money = 80) == 65: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],money = 31) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],money = 31) == 28: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 190) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 190) == 160: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],money = 105) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],money = 105) == 90: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 200) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 200) == 170: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 1, 100, 2, 100, 3, 100, 4, 100, 5],money = 200) == 197
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 1, 100, 2, 100, 3, 100, 4, 100, 5],money = 200) == 197: {e}')
    
    total += 1
    try:
        result = candidate(prices = [99, 50, 50, 1, 1],money = 100) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [99, 50, 50, 1, 1],money = 100) == 98: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],money = 11) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],money = 11) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],money = 180) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],money = 180) == 180: {e}')
    
    total += 1
    try:
        result = candidate(prices = [49, 50, 51, 52, 53, 54, 55, 56, 57, 58],money = 108) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [49, 50, 51, 52, 53, 54, 55, 56, 57, 58],money = 108) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],money = 100) == 96
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],money = 100) == 96: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 8, 12, 18, 22, 25],money = 40) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 8, 12, 18, 22, 25],money = 40) == 27: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 6, 5, 8, 9, 2, 4, 7, 1, 10],money = 12) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 6, 5, 8, 9, 2, 4, 7, 1, 10],money = 12) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],money = 198) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],money = 198) == 15: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(prices = [99, 99],money = 198) == 0
    assert candidate(prices = [99, 1],money = 100) == 0
    assert candidate(prices = [5, 4, 3, 2, 1],money = 10) == 7
    assert candidate(prices = [1, 1, 1, 1],money = 2) == 0
    assert candidate(prices = [1, 1],money = 3) == 1
    assert candidate(prices = [1, 2, 2],money = 3) == 0
    assert candidate(prices = [1, 1, 1, 1, 1],money = 1) == 1
    assert candidate(prices = [1, 1, 1, 1, 1],money = 1) == 1
    assert candidate(prices = [50, 50],money = 100) == 0
    assert candidate(prices = [1, 2, 3, 4, 5],money = 8) == 5
    assert candidate(prices = [99, 99],money = 198) == 0
    assert candidate(prices = [5, 5, 5, 5],money = 10) == 0
    assert candidate(prices = [10, 5, 7, 3],money = 15) == 7
    assert candidate(prices = [100, 1, 100],money = 199) == 98
    assert candidate(prices = [10, 20, 30],money = 50) == 20
    assert candidate(prices = [10, 20, 30, 40],money = 60) == 30
    assert candidate(prices = [100, 1, 1, 1, 1],money = 101) == 99
    assert candidate(prices = [3, 2, 3],money = 3) == 3
    assert candidate(prices = [10, 20, 30],money = 50) == 20
    assert candidate(prices = [10, 20, 30],money = 25) == 25
    assert candidate(prices = [5, 5, 5, 5],money = 10) == 0
    assert candidate(prices = [2, 2, 2, 2, 2],money = 5) == 1
    assert candidate(prices = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],money = 98) == 87
    assert candidate(prices = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],money = 8) == 0
    assert candidate(prices = [4, 1, 2, 3, 5, 6, 7, 8, 9, 10],money = 11) == 8
    assert candidate(prices = [50, 50, 50, 50, 50],money = 99) == 99
    assert candidate(prices = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],money = 100) == 0
    assert candidate(prices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],money = 199) == 199
    assert candidate(prices = [5, 3, 7, 9, 2, 6, 8, 1, 4, 10],money = 12) == 9
    assert candidate(prices = [50, 1, 50, 2, 3, 4, 5],money = 52) == 49
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],money = 11) == 8
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 110) == 80
    assert candidate(prices = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],money = 50) == 45
    assert candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],money = 180) == 19
    assert candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150],money = 300) == 285
    assert candidate(prices = [5, 4, 3, 2, 1],money = 10) == 7
    assert candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],money = 10) == 0
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 190) == 160
    assert candidate(prices = [1, 99, 1, 98, 1, 97, 1, 96, 1, 95],money = 100) == 98
    assert candidate(prices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],money = 150) == 150
    assert candidate(prices = [1, 1, 1, 1],money = 2) == 0
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],money = 11) == 8
    assert candidate(prices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],money = 199) == 199
    assert candidate(prices = [50, 50, 50, 50, 50],money = 100) == 0
    assert candidate(prices = [45, 23, 67, 89, 12, 34, 56, 78, 90, 100],money = 140) == 105
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0
    assert candidate(prices = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],money = 16) == 0
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],money = 29) == 26
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0
    assert candidate(prices = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200],money = 150) == 90
    assert candidate(prices = [50, 25, 75, 100, 20],money = 100) == 55
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],money = 18) == 15
    assert candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],money = 90) == 75
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19],money = 200) == 197
    assert candidate(prices = [5, 4, 3, 2, 1],money = 3) == 0
    assert candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],money = 10) == 10
    assert candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],money = 100) == 100
    assert candidate(prices = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],money = 99) == 99
    assert candidate(prices = [50, 51, 49, 48, 52, 53, 47, 46, 54, 55],money = 100) == 7
    assert candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],money = 10) == 0
    assert candidate(prices = [99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99],money = 198) == 0
    assert candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],money = 101) == 99
    assert candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],money = 5) == 5
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 105) == 75
    assert candidate(prices = [50, 10, 15, 20, 25],money = 55) == 30
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 150) == 120
    assert candidate(prices = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60],money = 60) == 51
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],money = 30) == 27
    assert candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81],money = 179) == 16
    assert candidate(prices = [40, 30, 20, 10, 5, 15, 25, 35, 45, 50],money = 60) == 45
    assert candidate(prices = [99, 100, 99, 100],money = 199) == 1
    assert candidate(prices = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],money = 150) == 150
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],money = 101) == 98
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 150) == 120
    assert candidate(prices = [45, 22, 13, 8, 3],money = 60) == 49
    assert candidate(prices = [80, 10, 50, 20, 30],money = 60) == 30
    assert candidate(prices = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96],money = 101) == 98
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0
    assert candidate(prices = [10, 15, 20, 25, 30, 35, 40],money = 60) == 35
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],money = 39) == 36
    assert candidate(prices = [75, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],money = 100) == 50
    assert candidate(prices = [1, 99, 1, 98],money = 100) == 98
    assert candidate(prices = [33, 33, 33, 33, 33, 33, 33, 33, 33, 33],money = 66) == 0
    assert candidate(prices = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],money = 5) == 1
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],money = 15) == 12
    assert candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],money = 20) == 0
    assert candidate(prices = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],money = 100) == 80
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0
    assert candidate(prices = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],money = 100) == 0
    assert candidate(prices = [100, 99, 98, 97, 96, 95],money = 193) == 2
    assert candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],money = 180) == 180
    assert candidate(prices = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10],money = 3) == 1
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],money = 100) == 97
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],money = 3) == 1
    assert candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],money = 80) == 65
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],money = 31) == 28
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 190) == 160
    assert candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],money = 105) == 90
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],money = 200) == 170
    assert candidate(prices = [100, 1, 100, 2, 100, 3, 100, 4, 100, 5],money = 200) == 197
    assert candidate(prices = [99, 50, 50, 1, 1],money = 100) == 98
    assert candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],money = 11) == 1
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],money = 2) == 0
    assert candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],money = 180) == 180
    assert candidate(prices = [49, 50, 51, 52, 53, 54, 55, 56, 57, 58],money = 108) == 9
    assert candidate(prices = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],money = 100) == 96
    assert candidate(prices = [5, 8, 12, 18, 22, 25],money = 40) == 27
    assert candidate(prices = [3, 6, 5, 8, 9, 2, 4, 7, 1, 10],money = 12) == 9
    assert candidate(prices = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91],money = 198) == 15


