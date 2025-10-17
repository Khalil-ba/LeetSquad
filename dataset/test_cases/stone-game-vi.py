def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(aliceValues = [1, 2],bobValues = [3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [1, 2],bobValues = [3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [1, 2, 3, 4, 5],bobValues = [5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [1, 2, 3, 4, 5],bobValues = [5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [9, 9, 9, 9, 9],bobValues = [1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [9, 9, 9, 9, 9],bobValues = [1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [5, 3, 1, 4],bobValues = [4, 1, 2, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [5, 3, 1, 4],bobValues = [4, 1, 2, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [10, 20, 30],bobValues = [30, 20, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [10, 20, 30],bobValues = [30, 20, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [1, 3],bobValues = [2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [1, 3],bobValues = [2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [2, 2, 2, 2, 2],bobValues = [3, 3, 3, 3, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [2, 2, 2, 2, 2],bobValues = [3, 3, 3, 3, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [1, 1, 1, 1],bobValues = [1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [1, 1, 1, 1],bobValues = [1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [1, 1, 1, 1, 1],bobValues = [9, 9, 9, 9, 9]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [1, 1, 1, 1, 1],bobValues = [9, 9, 9, 9, 9]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [7, 8, 9],bobValues = [9, 8, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [7, 8, 9],bobValues = [9, 8, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [2, 4, 3],bobValues = [1, 6, 7]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [2, 4, 3],bobValues = [1, 6, 7]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [10, 10, 10, 10],bobValues = [10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [10, 10, 10, 10],bobValues = [10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [5, 3, 8, 2],bobValues = [4, 1, 7, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [5, 3, 8, 2],bobValues = [4, 1, 7, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [100, 100, 100],bobValues = [100, 100, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [100, 100, 100],bobValues = [100, 100, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [99, 98, 97],bobValues = [1, 2, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [99, 98, 97],bobValues = [1, 2, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [100, 1, 1, 1],bobValues = [1, 100, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [100, 1, 1, 1],bobValues = [1, 100, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [30, 20, 10],bobValues = [10, 20, 30]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [30, 20, 10],bobValues = [10, 20, 30]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [5, 5, 5, 5],bobValues = [5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [5, 5, 5, 5],bobValues = [5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [1, 1, 1, 1, 1],bobValues = [1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [1, 1, 1, 1, 1],bobValues = [1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [99, 1, 99, 1, 99, 1],bobValues = [1, 99, 1, 99, 1, 99]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [99, 1, 99, 1, 99, 1],bobValues = [1, 99, 1, 99, 1, 99]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],bobValues = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],bobValues = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [80, 70, 60, 50, 40, 30, 20, 10],bobValues = [10, 20, 30, 40, 50, 60, 70, 80]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [80, 70, 60, 50, 40, 30, 20, 10],bobValues = [10, 20, 30, 40, 50, 60, 70, 80]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [99, 50, 25, 10, 5],bobValues = [1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [99, 50, 25, 10, 5],bobValues = [1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [100, 50, 25, 12, 6],bobValues = [5, 20, 40, 60, 80]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [100, 50, 25, 12, 6],bobValues = [5, 20, 40, 60, 80]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [100, 1, 100, 1, 100],bobValues = [1, 100, 1, 100, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [100, 1, 100, 1, 100],bobValues = [1, 100, 1, 100, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [5, 8, 7, 12, 9],bobValues = [4, 6, 5, 10, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [5, 8, 7, 12, 9],bobValues = [4, 6, 5, 10, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],bobValues = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],bobValues = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],bobValues = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],bobValues = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [3, 2, 3, 4, 5],bobValues = [5, 4, 3, 2, 3]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [3, 2, 3, 4, 5],bobValues = [5, 4, 3, 2, 3]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],bobValues = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],bobValues = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1],bobValues = [1, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1],bobValues = [1, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [50, 30, 20],bobValues = [1, 20, 30]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [50, 30, 20],bobValues = [1, 20, 30]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [100, 99, 98, 97, 96],bobValues = [95, 94, 93, 92, 91]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [100, 99, 98, 97, 96],bobValues = [95, 94, 93, 92, 91]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],bobValues = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],bobValues = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [5, 5, 5, 5],bobValues = [6, 6, 6, 6]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [5, 5, 5, 5],bobValues = [6, 6, 6, 6]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [1, 5, 9, 13, 17],bobValues = [16, 12, 8, 4, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [1, 5, 9, 13, 17],bobValues = [16, 12, 8, 4, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [23, 45, 67, 89, 10],bobValues = [10, 89, 67, 45, 23]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [23, 45, 67, 89, 10],bobValues = [10, 89, 67, 45, 23]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [23, 45, 67, 89, 12],bobValues = [12, 89, 67, 45, 23]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [23, 45, 67, 89, 12],bobValues = [12, 89, 67, 45, 23]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],bobValues = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],bobValues = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [50, 30, 20, 10, 1],bobValues = [10, 20, 30, 40, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [50, 30, 20, 10, 1],bobValues = [10, 20, 30, 40, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],bobValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],bobValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [99, 98, 97, 96, 95],bobValues = [1, 2, 3, 4, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [99, 98, 97, 96, 95],bobValues = [1, 2, 3, 4, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [50, 50, 50, 50, 50],bobValues = [50, 50, 50, 50, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [50, 50, 50, 50, 50],bobValues = [50, 50, 50, 50, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],bobValues = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],bobValues = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [5, 2, 3, 3, 4],bobValues = [4, 3, 2, 3, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [5, 2, 3, 3, 4],bobValues = [4, 3, 2, 3, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],bobValues = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],bobValues = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],bobValues = [75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],bobValues = [75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [100, 50, 25, 10, 5],bobValues = [5, 10, 25, 50, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [100, 50, 25, 10, 5],bobValues = [5, 10, 25, 50, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [30, 20, 10, 50, 40, 60, 70],bobValues = [70, 60, 50, 40, 30, 20, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [30, 20, 10, 50, 40, 60, 70],bobValues = [70, 60, 50, 40, 30, 20, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [50, 50, 50],bobValues = [100, 100, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [50, 50, 50],bobValues = [100, 100, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [99, 1, 98, 2, 97, 3, 96, 4, 95, 5],bobValues = [5, 95, 4, 96, 3, 97, 2, 98, 1, 99]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [99, 1, 98, 2, 97, 3, 96, 4, 95, 5],bobValues = [5, 95, 4, 96, 3, 97, 2, 98, 1, 99]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86],bobValues = [86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86],bobValues = [86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],bobValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],bobValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [100, 100, 100, 100, 100],bobValues = [99, 99, 99, 99, 99]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [100, 100, 100, 100, 100],bobValues = [99, 99, 99, 99, 99]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [80, 20, 60, 40, 100, 50, 70],bobValues = [70, 50, 100, 60, 20, 40, 80]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [80, 20, 60, 40, 100, 50, 70],bobValues = [70, 50, 100, 60, 20, 40, 80]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [7, 14, 21, 28, 35, 42],bobValues = [6, 12, 18, 24, 30, 36]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [7, 14, 21, 28, 35, 42],bobValues = [6, 12, 18, 24, 30, 36]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [10, 10, 10, 10],bobValues = [20, 20, 20, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [10, 10, 10, 10],bobValues = [20, 20, 20, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],bobValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],bobValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bobValues = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bobValues = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [100, 90, 80, 70, 60],bobValues = [60, 70, 80, 90, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [100, 90, 80, 70, 60],bobValues = [60, 70, 80, 90, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [100, 100, 1, 1, 1],bobValues = [1, 1, 100, 100, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [100, 100, 1, 1, 1],bobValues = [1, 1, 100, 100, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [2, 4, 6, 8, 10],bobValues = [1, 3, 5, 7, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [2, 4, 6, 8, 10],bobValues = [1, 3, 5, 7, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [5, 15, 25, 35, 45, 55],bobValues = [55, 45, 35, 25, 15, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [5, 15, 25, 35, 45, 55],bobValues = [55, 45, 35, 25, 15, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],bobValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],bobValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],bobValues = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],bobValues = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [100, 100, 100, 100, 100],bobValues = [50, 50, 50, 50, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [100, 100, 100, 100, 100],bobValues = [50, 50, 50, 50, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [90, 20, 30, 10, 50],bobValues = [50, 90, 10, 30, 20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [90, 20, 30, 10, 50],bobValues = [50, 90, 10, 30, 20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [10, 10, 10, 10, 10, 10],bobValues = [9, 9, 9, 9, 9, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [10, 10, 10, 10, 10, 10],bobValues = [9, 9, 9, 9, 9, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],bobValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],bobValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],bobValues = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],bobValues = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],bobValues = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],bobValues = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],bobValues = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],bobValues = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [100, 1, 2, 3, 4],bobValues = [1, 100, 2, 3, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [100, 1, 2, 3, 4],bobValues = [1, 100, 2, 3, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [100, 1, 50, 25, 75],bobValues = [90, 99, 5, 20, 70]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [100, 1, 50, 25, 75],bobValues = [90, 99, 5, 20, 70]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],bobValues = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],bobValues = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [90, 90, 90, 90, 90, 90, 90, 90, 90, 90],bobValues = [91, 91, 91, 91, 91, 91, 91, 91, 91, 91]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [90, 90, 90, 90, 90, 90, 90, 90, 90, 90],bobValues = [91, 91, 91, 91, 91, 91, 91, 91, 91, 91]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [2, 3, 5, 7, 11],bobValues = [11, 7, 5, 3, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [2, 3, 5, 7, 11],bobValues = [11, 7, 5, 3, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],bobValues = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],bobValues = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [30, 30, 30, 30, 30],bobValues = [30, 30, 30, 30, 30]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [30, 30, 30, 30, 30],bobValues = [30, 30, 30, 30, 30]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [30, 20, 10],bobValues = [10, 20, 30]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [30, 20, 10],bobValues = [10, 20, 30]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [10, 1, 10, 1, 10, 1, 10, 1],bobValues = [1, 10, 1, 10, 1, 10, 1, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [10, 1, 10, 1, 10, 1, 10, 1],bobValues = [1, 10, 1, 10, 1, 10, 1, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],bobValues = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],bobValues = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [1, 3, 5, 7, 9, 11, 13],bobValues = [2, 4, 6, 8, 10, 12, 14]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [1, 3, 5, 7, 9, 11, 13],bobValues = [2, 4, 6, 8, 10, 12, 14]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bobValues = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bobValues = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [10, 20, 30, 40, 50],bobValues = [50, 40, 30, 20, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [10, 20, 30, 40, 50],bobValues = [50, 40, 30, 20, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [50, 50, 50, 50, 50],bobValues = [40, 40, 40, 40, 60]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [50, 50, 50, 50, 50],bobValues = [40, 40, 40, 40, 60]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50],bobValues = [10, 20, 30, 40, 50, 50, 40, 30, 20, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50],bobValues = [10, 20, 30, 40, 50, 50, 40, 30, 20, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [99, 1, 2, 3, 4],bobValues = [4, 3, 2, 1, 99]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [99, 1, 2, 3, 4],bobValues = [4, 3, 2, 1, 99]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [50, 40, 30, 20, 10],bobValues = [10, 20, 30, 40, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [50, 40, 30, 20, 10],bobValues = [10, 20, 30, 40, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [10, 30, 20, 50, 40],bobValues = [40, 20, 30, 10, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [10, 30, 20, 50, 40],bobValues = [40, 20, 30, 10, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [50, 50, 50, 50, 50],bobValues = [50, 50, 50, 50, 51]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [50, 50, 50, 50, 50],bobValues = [50, 50, 50, 50, 51]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [5, 15, 25, 35, 45, 55, 65],bobValues = [65, 55, 45, 35, 25, 15, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [5, 15, 25, 35, 45, 55, 65],bobValues = [65, 55, 45, 35, 25, 15, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [10, 20, 30, 40, 50],bobValues = [50, 40, 30, 20, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [10, 20, 30, 40, 50],bobValues = [50, 40, 30, 20, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [50, 25, 50, 75, 25],bobValues = [75, 50, 25, 25, 50]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [50, 25, 50, 75, 25],bobValues = [75, 50, 25, 25, 50]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [1, 1, 1, 2, 2, 2, 3, 3, 3],bobValues = [3, 3, 3, 2, 2, 2, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [1, 1, 1, 2, 2, 2, 3, 3, 3],bobValues = [3, 3, 3, 2, 2, 2, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [100, 1, 1, 1, 1],bobValues = [1, 1, 1, 1, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [100, 1, 1, 1, 1],bobValues = [1, 1, 1, 1, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [90, 80, 70, 60, 50, 40, 30, 20, 10],bobValues = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [90, 80, 70, 60, 50, 40, 30, 20, 10],bobValues = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],bobValues = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],bobValues = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [90, 10, 90, 10, 90],bobValues = [10, 90, 10, 90, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [90, 10, 90, 10, 90],bobValues = [10, 90, 10, 90, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],bobValues = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],bobValues = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [42, 23, 17, 5, 99],bobValues = [99, 5, 17, 23, 42]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [42, 23, 17, 5, 99],bobValues = [99, 5, 17, 23, 42]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [100, 50, 1, 1, 1, 1, 1, 1, 1, 1],bobValues = [1, 1, 99, 99, 99, 99, 99, 99, 99, 99]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [100, 50, 1, 1, 1, 1, 1, 1, 1, 1],bobValues = [1, 1, 99, 99, 99, 99, 99, 99, 99, 99]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120],bobValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120],bobValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [70, 60, 50, 40, 30, 20, 10],bobValues = [10, 20, 30, 40, 50, 60, 70]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [70, 60, 50, 40, 30, 20, 10],bobValues = [10, 20, 30, 40, 50, 60, 70]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [90, 10, 20, 30, 40, 50, 60, 70, 80],bobValues = [10, 90, 80, 70, 60, 50, 40, 30, 20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [90, 10, 20, 30, 40, 50, 60, 70, 80],bobValues = [10, 90, 80, 70, 60, 50, 40, 30, 20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(aliceValues = [100],bobValues = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(aliceValues = [100],bobValues = [1]) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(aliceValues = [1, 2],bobValues = [3, 1]) == 0
    assert candidate(aliceValues = [1, 2, 3, 4, 5],bobValues = [5, 4, 3, 2, 1]) == 1
    assert candidate(aliceValues = [9, 9, 9, 9, 9],bobValues = [1, 1, 1, 1, 1]) == 1
    assert candidate(aliceValues = [5, 3, 1, 4],bobValues = [4, 1, 2, 3]) == 1
    assert candidate(aliceValues = [10, 20, 30],bobValues = [30, 20, 10]) == 1
    assert candidate(aliceValues = [1, 3],bobValues = [2, 1]) == 1
    assert candidate(aliceValues = [2, 2, 2, 2, 2],bobValues = [3, 3, 3, 3, 3]) == 0
    assert candidate(aliceValues = [1, 1, 1, 1],bobValues = [1, 1, 1, 1]) == 0
    assert candidate(aliceValues = [1, 1, 1, 1, 1],bobValues = [9, 9, 9, 9, 9]) == -1
    assert candidate(aliceValues = [7, 8, 9],bobValues = [9, 8, 7]) == 1
    assert candidate(aliceValues = [2, 4, 3],bobValues = [1, 6, 7]) == -1
    assert candidate(aliceValues = [10, 10, 10, 10],bobValues = [10, 10, 10, 10]) == 0
    assert candidate(aliceValues = [5, 3, 8, 2],bobValues = [4, 1, 7, 3]) == 1
    assert candidate(aliceValues = [100, 100, 100],bobValues = [100, 100, 100]) == 1
    assert candidate(aliceValues = [99, 98, 97],bobValues = [1, 2, 3]) == 1
    assert candidate(aliceValues = [100, 1, 1, 1],bobValues = [1, 100, 1, 1]) == 0
    assert candidate(aliceValues = [30, 20, 10],bobValues = [10, 20, 30]) == 1
    assert candidate(aliceValues = [5, 5, 5, 5],bobValues = [5, 5, 5, 5]) == 0
    assert candidate(aliceValues = [1, 1, 1, 1, 1],bobValues = [1, 1, 1, 1, 1]) == 1
    assert candidate(aliceValues = [99, 1, 99, 1, 99, 1],bobValues = [1, 99, 1, 99, 1, 99]) == 0
    assert candidate(aliceValues = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100],bobValues = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 0
    assert candidate(aliceValues = [80, 70, 60, 50, 40, 30, 20, 10],bobValues = [10, 20, 30, 40, 50, 60, 70, 80]) == 0
    assert candidate(aliceValues = [99, 50, 25, 10, 5],bobValues = [1, 1, 1, 1, 1]) == 1
    assert candidate(aliceValues = [100, 50, 25, 12, 6],bobValues = [5, 20, 40, 60, 80]) == 1
    assert candidate(aliceValues = [100, 1, 100, 1, 100],bobValues = [1, 100, 1, 100, 1]) == 1
    assert candidate(aliceValues = [5, 8, 7, 12, 9],bobValues = [4, 6, 5, 10, 7]) == 1
    assert candidate(aliceValues = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],bobValues = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(aliceValues = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],bobValues = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 1
    assert candidate(aliceValues = [3, 2, 3, 4, 5],bobValues = [5, 4, 3, 2, 3]) == 1
    assert candidate(aliceValues = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],bobValues = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(aliceValues = [100, 1, 1, 1, 1, 1, 1, 1, 1, 1],bobValues = [1, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == 0
    assert candidate(aliceValues = [50, 30, 20],bobValues = [1, 20, 30]) == 1
    assert candidate(aliceValues = [100, 99, 98, 97, 96],bobValues = [95, 94, 93, 92, 91]) == 1
    assert candidate(aliceValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],bobValues = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(aliceValues = [5, 5, 5, 5],bobValues = [6, 6, 6, 6]) == -1
    assert candidate(aliceValues = [1, 5, 9, 13, 17],bobValues = [16, 12, 8, 4, 0]) == 1
    assert candidate(aliceValues = [23, 45, 67, 89, 10],bobValues = [10, 89, 67, 45, 23]) == 1
    assert candidate(aliceValues = [23, 45, 67, 89, 12],bobValues = [12, 89, 67, 45, 23]) == 1
    assert candidate(aliceValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],bobValues = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(aliceValues = [50, 30, 20, 10, 1],bobValues = [10, 20, 30, 40, 50]) == 1
    assert candidate(aliceValues = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],bobValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(aliceValues = [99, 98, 97, 96, 95],bobValues = [1, 2, 3, 4, 5]) == 1
    assert candidate(aliceValues = [50, 50, 50, 50, 50],bobValues = [50, 50, 50, 50, 50]) == 1
    assert candidate(aliceValues = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6],bobValues = [10, 1, 9, 2, 8, 3, 7, 4, 6, 5]) == 0
    assert candidate(aliceValues = [5, 2, 3, 3, 4],bobValues = [4, 3, 2, 3, 5]) == 1
    assert candidate(aliceValues = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],bobValues = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1
    assert candidate(aliceValues = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],bobValues = [75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == 1
    assert candidate(aliceValues = [100, 50, 25, 10, 5],bobValues = [5, 10, 25, 50, 100]) == 1
    assert candidate(aliceValues = [30, 20, 10, 50, 40, 60, 70],bobValues = [70, 60, 50, 40, 30, 20, 10]) == 1
    assert candidate(aliceValues = [50, 50, 50],bobValues = [100, 100, 100]) == 0
    assert candidate(aliceValues = [99, 1, 98, 2, 97, 3, 96, 4, 95, 5],bobValues = [5, 95, 4, 96, 3, 97, 2, 98, 1, 99]) == 0
    assert candidate(aliceValues = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86],bobValues = [86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 1
    assert candidate(aliceValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],bobValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(aliceValues = [100, 100, 100, 100, 100],bobValues = [99, 99, 99, 99, 99]) == 1
    assert candidate(aliceValues = [80, 20, 60, 40, 100, 50, 70],bobValues = [70, 50, 100, 60, 20, 40, 80]) == 1
    assert candidate(aliceValues = [7, 14, 21, 28, 35, 42],bobValues = [6, 12, 18, 24, 30, 36]) == 1
    assert candidate(aliceValues = [10, 10, 10, 10],bobValues = [20, 20, 20, 20]) == -1
    assert candidate(aliceValues = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],bobValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0
    assert candidate(aliceValues = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bobValues = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(aliceValues = [100, 90, 80, 70, 60],bobValues = [60, 70, 80, 90, 100]) == 1
    assert candidate(aliceValues = [100, 100, 1, 1, 1],bobValues = [1, 1, 100, 100, 100]) == 1
    assert candidate(aliceValues = [2, 4, 6, 8, 10],bobValues = [1, 3, 5, 7, 9]) == 1
    assert candidate(aliceValues = [5, 15, 25, 35, 45, 55],bobValues = [55, 45, 35, 25, 15, 5]) == 0
    assert candidate(aliceValues = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],bobValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(aliceValues = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],bobValues = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 0
    assert candidate(aliceValues = [100, 100, 100, 100, 100],bobValues = [50, 50, 50, 50, 50]) == 1
    assert candidate(aliceValues = [90, 20, 30, 10, 50],bobValues = [50, 90, 10, 30, 20]) == 1
    assert candidate(aliceValues = [10, 10, 10, 10, 10, 10],bobValues = [9, 9, 9, 9, 9, 9]) == 1
    assert candidate(aliceValues = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],bobValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 1
    assert candidate(aliceValues = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],bobValues = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 0
    assert candidate(aliceValues = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],bobValues = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(aliceValues = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],bobValues = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 1
    assert candidate(aliceValues = [100, 1, 2, 3, 4],bobValues = [1, 100, 2, 3, 4]) == 1
    assert candidate(aliceValues = [100, 1, 50, 25, 75],bobValues = [90, 99, 5, 20, 70]) == 1
    assert candidate(aliceValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],bobValues = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0
    assert candidate(aliceValues = [90, 90, 90, 90, 90, 90, 90, 90, 90, 90],bobValues = [91, 91, 91, 91, 91, 91, 91, 91, 91, 91]) == -1
    assert candidate(aliceValues = [2, 3, 5, 7, 11],bobValues = [11, 7, 5, 3, 2]) == 1
    assert candidate(aliceValues = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],bobValues = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 0
    assert candidate(aliceValues = [30, 30, 30, 30, 30],bobValues = [30, 30, 30, 30, 30]) == 1
    assert candidate(aliceValues = [30, 20, 10],bobValues = [10, 20, 30]) == 1
    assert candidate(aliceValues = [10, 1, 10, 1, 10, 1, 10, 1],bobValues = [1, 10, 1, 10, 1, 10, 1, 10]) == 0
    assert candidate(aliceValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],bobValues = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 0
    assert candidate(aliceValues = [1, 3, 5, 7, 9, 11, 13],bobValues = [2, 4, 6, 8, 10, 12, 14]) == 1
    assert candidate(aliceValues = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],bobValues = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == -1
    assert candidate(aliceValues = [10, 20, 30, 40, 50],bobValues = [50, 40, 30, 20, 10]) == 1
    assert candidate(aliceValues = [50, 50, 50, 50, 50],bobValues = [40, 40, 40, 40, 60]) == 1
    assert candidate(aliceValues = [50, 40, 30, 20, 10, 10, 20, 30, 40, 50],bobValues = [10, 20, 30, 40, 50, 50, 40, 30, 20, 10]) == 0
    assert candidate(aliceValues = [99, 1, 2, 3, 4],bobValues = [4, 3, 2, 1, 99]) == 1
    assert candidate(aliceValues = [50, 40, 30, 20, 10],bobValues = [10, 20, 30, 40, 50]) == 1
    assert candidate(aliceValues = [10, 30, 20, 50, 40],bobValues = [40, 20, 30, 10, 50]) == 1
    assert candidate(aliceValues = [50, 50, 50, 50, 50],bobValues = [50, 50, 50, 50, 51]) == 1
    assert candidate(aliceValues = [5, 15, 25, 35, 45, 55, 65],bobValues = [65, 55, 45, 35, 25, 15, 5]) == 1
    assert candidate(aliceValues = [10, 20, 30, 40, 50],bobValues = [50, 40, 30, 20, 10]) == 1
    assert candidate(aliceValues = [50, 25, 50, 75, 25],bobValues = [75, 50, 25, 25, 50]) == 1
    assert candidate(aliceValues = [1, 1, 1, 2, 2, 2, 3, 3, 3],bobValues = [3, 3, 3, 2, 2, 2, 1, 1, 1]) == 1
    assert candidate(aliceValues = [100, 1, 1, 1, 1],bobValues = [1, 1, 1, 1, 100]) == 1
    assert candidate(aliceValues = [90, 80, 70, 60, 50, 40, 30, 20, 10],bobValues = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 1
    assert candidate(aliceValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],bobValues = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(aliceValues = [90, 10, 90, 10, 90],bobValues = [10, 90, 10, 90, 10]) == 1
    assert candidate(aliceValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],bobValues = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 1
    assert candidate(aliceValues = [42, 23, 17, 5, 99],bobValues = [99, 5, 17, 23, 42]) == 1
    assert candidate(aliceValues = [100, 50, 1, 1, 1, 1, 1, 1, 1, 1],bobValues = [1, 1, 99, 99, 99, 99, 99, 99, 99, 99]) == -1
    assert candidate(aliceValues = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120],bobValues = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 1
    assert candidate(aliceValues = [70, 60, 50, 40, 30, 20, 10],bobValues = [10, 20, 30, 40, 50, 60, 70]) == 1
    assert candidate(aliceValues = [90, 10, 20, 30, 40, 50, 60, 70, 80],bobValues = [10, 90, 80, 70, 60, 50, 40, 30, 20]) == 1
    assert candidate(aliceValues = [100],bobValues = [1]) == 1


