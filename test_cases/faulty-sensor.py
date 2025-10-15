def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5],sensor2 = [1, 2, 4, 5, 6]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5],sensor2 = [1, 2, 4, 5, 6]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [3, 4, 5, 6],sensor2 = [4, 5, 6, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [3, 4, 5, 6],sensor2 = [4, 5, 6, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5],sensor2 = [1, 2, 3, 4, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5],sensor2 = [1, 2, 3, 4, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [10, 20, 30, 40],sensor2 = [10, 20, 35, 40]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [10, 20, 30, 40],sensor2 = [10, 20, 35, 40]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [5, 4, 3, 2, 1],sensor2 = [5, 4, 2, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [5, 4, 3, 2, 1],sensor2 = [5, 4, 2, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [10, 20, 30, 40, 50],sensor2 = [10, 20, 30, 50, 45]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [10, 20, 30, 40, 50],sensor2 = [10, 20, 30, 50, 45]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5],sensor2 = [1, 2, 4, 5, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5],sensor2 = [1, 2, 4, 5, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [5, 4, 3, 2, 1],sensor2 = [5, 4, 2, 1, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [5, 4, 3, 2, 1],sensor2 = [5, 4, 2, 1, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [5, 6, 7, 8],sensor2 = [5, 6, 7, 9]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [5, 6, 7, 8],sensor2 = [5, 6, 7, 9]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [9, 8, 7, 6],sensor2 = [9, 8, 6, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [9, 8, 7, 6],sensor2 = [9, 8, 6, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5],sensor2 = [1, 2, 3, 4, 8]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5],sensor2 = [1, 2, 3, 4, 8]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [2, 3, 4, 5],sensor2 = [2, 1, 3, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [2, 3, 4, 5],sensor2 = [2, 1, 3, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [2, 3, 2, 2, 3, 2],sensor2 = [2, 3, 2, 3, 2, 7]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [2, 3, 2, 2, 3, 2],sensor2 = [2, 3, 2, 3, 2, 7]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [2, 2, 2, 2, 2],sensor2 = [2, 2, 2, 2, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [2, 2, 2, 2, 2],sensor2 = [2, 2, 2, 2, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 1, 1, 1],sensor2 = [1, 1, 1, 1]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 1, 1, 1],sensor2 = [1, 1, 1, 1]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [5, 6, 7, 8],sensor2 = [5, 6, 8, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [5, 6, 7, 8],sensor2 = [5, 6, 8, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 3, 4],sensor2 = [1, 2, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 3, 4],sensor2 = [1, 2, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 3, 5, 7, 9],sensor2 = [1, 3, 4, 7, 8]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 3, 5, 7, 9],sensor2 = [1, 3, 4, 7, 8]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3],sensor2 = [1, 3, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3],sensor2 = [1, 3, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [5, 6, 7, 8, 9, 10],sensor2 = [5, 6, 8, 9, 10, 12]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [5, 6, 7, 8, 9, 10],sensor2 = [5, 6, 8, 9, 10, 12]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [10, 20, 30, 40, 50, 60, 70],sensor2 = [10, 20, 30, 40, 50, 60, 80]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [10, 20, 30, 40, 50, 60, 70],sensor2 = [10, 20, 30, 40, 50, 60, 80]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [3, 3, 3, 3, 3, 3, 3, 3],sensor2 = [3, 3, 3, 3, 3, 3, 3, 7]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [3, 3, 3, 3, 3, 3, 3, 3],sensor2 = [3, 3, 3, 3, 3, 3, 3, 7]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [9, 8, 7, 6, 5, 4],sensor2 = [9, 8, 7, 6, 4, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [9, 8, 7, 6, 5, 4],sensor2 = [9, 8, 7, 6, 4, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],sensor2 = [4, 8, 12, 16, 20, 24, 28, 36, 40, 32]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],sensor2 = [4, 8, 12, 16, 20, 24, 28, 36, 40, 32]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 3, 5, 6, 7, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 3, 5, 6, 7, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],sensor2 = [10, 20, 30, 40, 50, 60, 70, 80, 95, 100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],sensor2 = [10, 20, 30, 40, 50, 60, 70, 80, 95, 100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 99]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 99]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 3, 2, 4, 5, 6, 7, 8, 9],sensor2 = [1, 3, 2, 4, 5, 6, 7, 8, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 3, 2, 4, 5, 6, 7, 8, 9],sensor2 = [1, 3, 2, 4, 5, 6, 7, 8, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [20, 19, 18, 17, 16],sensor2 = [20, 19, 18, 16, 17]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [20, 19, 18, 17, 16],sensor2 = [20, 19, 18, 16, 17]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 2, 3, 4, 4, 5],sensor2 = [1, 2, 2, 4, 4, 5, 6]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 2, 3, 4, 4, 5],sensor2 = [1, 2, 2, 4, 4, 5, 6]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],sensor2 = [10, 11, 12, 14, 15, 16, 17, 18, 19, 20]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],sensor2 = [10, 11, 12, 14, 15, 16, 17, 18, 19, 20]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [5, 10, 15, 20, 25, 30],sensor2 = [5, 10, 20, 25, 30, 40]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [5, 10, 15, 20, 25, 30],sensor2 = [5, 10, 20, 25, 30, 40]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [5, 6, 7, 8, 9, 10],sensor2 = [5, 6, 7, 9, 10, 11]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [5, 6, 7, 8, 9, 10],sensor2 = [5, 6, 7, 9, 10, 11]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [3, 3, 3, 1, 3, 3, 3],sensor2 = [3, 3, 3, 3, 3, 3, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [3, 3, 3, 1, 3, 3, 3],sensor2 = [3, 3, 3, 3, 3, 3, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 7, 6, 5, 4, 3, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 7, 6, 5, 4, 3, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [100, 99, 98, 97, 96, 95],sensor2 = [100, 99, 98, 97, 95, 94]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [100, 99, 98, 97, 96, 95],sensor2 = [100, 99, 98, 97, 95, 94]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [10, 20, 30, 40, 50, 60],sensor2 = [10, 20, 30, 40, 60, 65]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [10, 20, 30, 40, 50, 60],sensor2 = [10, 20, 30, 40, 60, 65]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [5, 6, 7, 8, 9, 10],sensor2 = [5, 6, 8, 9, 10, 15]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [5, 6, 7, 8, 9, 10],sensor2 = [5, 6, 8, 9, 10, 15]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [5, 15, 25, 35, 45, 55, 65],sensor2 = [5, 15, 25, 35, 45, 55, 75]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [5, 15, 25, 35, 45, 55, 65],sensor2 = [5, 15, 25, 35, 45, 55, 75]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 7, 6, 5, 4, 3, 2, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 7, 6, 5, 4, 3, 2, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 1, 2, 2, 3, 3, 4, 4],sensor2 = [1, 1, 2, 2, 3, 4, 4, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 1, 2, 2, 3, 3, 4, 4],sensor2 = [1, 1, 2, 2, 3, 4, 4, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],sensor2 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 4]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],sensor2 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 4]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [7, 8, 9, 10, 11, 12, 13, 14, 15],sensor2 = [7, 8, 10, 11, 12, 13, 14, 15, 16]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [7, 8, 9, 10, 11, 12, 13, 14, 15],sensor2 = [7, 8, 10, 11, 12, 13, 14, 15, 16]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [3, 5, 7, 9, 11, 13, 15, 17],sensor2 = [3, 5, 8, 9, 11, 13, 15, 18]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [3, 5, 7, 9, 11, 13, 15, 17],sensor2 = [3, 5, 8, 9, 11, 13, 15, 18]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 7, 6, 4, 3, 2, 1, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 7, 6, 4, 3, 2, 1, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 6, 5, 4, 3, 2, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 6, 5, 4, 3, 2, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [100, 99, 98, 97, 96],sensor2 = [100, 99, 98, 96, 95]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [100, 99, 98, 97, 96],sensor2 = [100, 99, 98, 96, 95]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [25, 50, 75, 100, 125, 150, 175, 200],sensor2 = [25, 50, 100, 125, 150, 175, 200, 225]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [25, 50, 75, 100, 125, 150, 175, 200],sensor2 = [25, 50, 100, 125, 150, 175, 200, 225]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 1, 1, 1, 2, 1],sensor2 = [1, 1, 1, 1, 1, 3]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 1, 1, 1, 2, 1],sensor2 = [1, 1, 1, 1, 1, 3]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [7, 8, 9, 10, 11, 12, 13],sensor2 = [7, 8, 10, 11, 12, 13, 14]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [7, 8, 9, 10, 11, 12, 13],sensor2 = [7, 8, 10, 11, 12, 13, 14]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],sensor2 = [1, 3, 5, 7, 8, 10, 12, 14, 16, 18]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],sensor2 = [1, 3, 5, 7, 8, 10, 12, 14, 16, 18]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [10, 20, 30, 40, 50, 60, 70, 80, 90],sensor2 = [10, 20, 30, 50, 60, 70, 80, 90, 100]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [10, 20, 30, 40, 50, 60, 70, 80, 90],sensor2 = [10, 20, 30, 50, 60, 70, 80, 90, 100]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 6, 7, 8, 9, 10, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 6, 7, 8, 9, 10, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 5, 6, 7, 8, 9, 10, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 5, 6, 7, 8, 9, 10, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [5, 15, 25, 35, 45, 55],sensor2 = [5, 15, 25, 35, 45, 65]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [5, 15, 25, 35, 45, 55],sensor2 = [5, 15, 25, 35, 45, 65]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81],sensor2 = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 82, 83, 80]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81],sensor2 = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 82, 83, 80]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [100, 99, 98, 97, 96, 95, 94, 93],sensor2 = [100, 99, 97, 96, 95, 94, 93, 92]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [100, 99, 98, 97, 96, 95, 94, 93],sensor2 = [100, 99, 97, 96, 95, 94, 93, 92]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],sensor2 = [10, 20, 30, 40, 60, 70, 80, 90, 100, 110]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],sensor2 = [10, 20, 30, 40, 60, 70, 80, 90, 100, 110]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 7, 6, 5, 4, 2, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 7, 6, 5, 4, 2, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],sensor2 = [3, 6, 9, 12, 15, 18, 21, 24, 30, 28]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],sensor2 = [3, 6, 9, 12, 15, 18, 21, 24, 30, 28]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],sensor2 = [7, 14, 21, 28, 35, 42, 49, 63, 56, 71]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],sensor2 = [7, 14, 21, 28, 35, 42, 49, 63, 56, 71]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],sensor2 = [2, 4, 6, 8, 10, 12, 14, 18, 20, 16]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],sensor2 = [2, 4, 6, 8, 10, 12, 14, 18, 20, 16]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 3, 4, 5, 6, 7, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 3, 4, 5, 6, 7, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [7, 8, 9, 10, 11, 12, 13],sensor2 = [7, 8, 9, 10, 12, 13, 14]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [7, 8, 9, 10, 11, 12, 13],sensor2 = [7, 8, 9, 10, 12, 13, 14]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 1, 2, 3, 1, 1],sensor2 = [1, 1, 2, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 1, 2, 3, 1, 1],sensor2 = [1, 1, 2, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],sensor2 = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],sensor2 = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [5, 6, 7, 8, 9, 10],sensor2 = [5, 6, 7, 9, 10, 11]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [5, 6, 7, 8, 9, 10],sensor2 = [5, 6, 7, 9, 10, 11]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [7, 8, 9, 10, 11, 12, 13, 14, 15],sensor2 = [7, 8, 9, 11, 12, 13, 14, 15, 16]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [7, 8, 9, 10, 11, 12, 13, 14, 15],sensor2 = [7, 8, 9, 11, 12, 13, 14, 15, 16]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],sensor2 = [5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],sensor2 = [5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 1, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 1, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],sensor2 = [3, 5, 7, 9, 11, 14, 15, 17, 19, 21]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],sensor2 = [3, 5, 7, 9, 11, 14, 15, 17, 19, 21]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 7, 6, 4, 3, 2, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 7, 6, 4, 3, 2, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 7, 6, 5, 4, 3, 1, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 7, 6, 5, 4, 3, 1, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [42, 42, 42, 42, 42, 42, 42, 42],sensor2 = [42, 42, 42, 42, 42, 42, 42, 99]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [42, 42, 42, 42, 42, 42, 42, 42],sensor2 = [42, 42, 42, 42, 42, 42, 42, 99]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],sensor2 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],sensor2 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],sensor2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 22]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],sensor2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 22]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 3, 2, 4, 5, 6],sensor2 = [1, 2, 3, 4, 5, 7]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 3, 2, 4, 5, 6],sensor2 = [1, 2, 3, 4, 5, 7]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 3, 5, 6, 7, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 3, 5, 6, 7, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [10, 20, 30, 40, 50, 60],sensor2 = [10, 20, 30, 50, 60, 70]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [10, 20, 30, 40, 50, 60],sensor2 = [10, 20, 30, 50, 60, 70]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],sensor2 = [1, 1, 2, 2, 3, 3, 4, 4, 4, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],sensor2 = [1, 1, 2, 2, 3, 3, 4, 4, 4, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 3, 4, 5, 7, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 3, 4, 5, 7, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [3, 5, 7, 9, 11, 13],sensor2 = [3, 5, 7, 11, 13, 15]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [3, 5, 7, 9, 11, 13],sensor2 = [3, 5, 7, 11, 13, 15]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],sensor2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],sensor2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sensor2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 6]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sensor2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 6]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 4, 5, 6, 7, 8, 9, 11]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 4, 5, 6, 7, 8, 9, 11]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 2, 2, 3, 2, 2, 2, 4, 5, 6],sensor2 = [1, 2, 2, 2, 3, 2, 2, 3, 2, 2, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 2, 2, 3, 2, 2, 2, 4, 5, 6],sensor2 = [1, 2, 2, 2, 3, 2, 2, 3, 2, 2, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [100, 99, 98, 97, 96, 95],sensor2 = [100, 99, 98, 97, 96, 94]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [100, 99, 98, 97, 96, 95],sensor2 = [100, 99, 98, 97, 96, 94]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [42, 43, 44, 45, 46, 47, 48],sensor2 = [42, 43, 45, 46, 47, 48, 49]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [42, 43, 44, 45, 46, 47, 48],sensor2 = [42, 43, 45, 46, 47, 48, 49]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],sensor2 = [1, 2, 3, 4, 4, 3, 2, 1, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],sensor2 = [1, 2, 3, 4, 4, 3, 2, 1, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 3, 4, 5, 6, 8, 9, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 3, 4, 5, 6, 8, 9, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [7, 14, 21, 28, 35, 42],sensor2 = [7, 14, 21, 28, 42, 49]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [7, 14, 21, 28, 35, 42],sensor2 = [7, 14, 21, 28, 42, 49]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],sensor2 = [1, 3, 5, 7, 9, 11, 13, 15, 18, 19]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],sensor2 = [1, 3, 5, 7, 9, 11, 13, 15, 18, 19]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 20]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 20]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 3, 2, 3, 4, 5, 6],sensor2 = [1, 3, 2, 3, 4, 5, 7]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 3, 2, 3, 4, 5, 6],sensor2 = [1, 3, 2, 3, 4, 5, 7]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8],sensor2 = [1, 2, 3, 4, 6, 7, 8, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8],sensor2 = [1, 2, 3, 4, 6, 7, 8, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 5, 6, 7, 8, 9, 10, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 5, 6, 7, 8, 9, 10, 9]) == 2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(sensor1 = [1, 2, 3, 4, 5],sensor2 = [1, 2, 4, 5, 6]) == 2
    assert candidate(sensor1 = [3, 4, 5, 6],sensor2 = [4, 5, 6, 3]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5],sensor2 = [1, 2, 3, 4, 5]) == -1
    assert candidate(sensor1 = [10, 20, 30, 40],sensor2 = [10, 20, 35, 40]) == 1
    assert candidate(sensor1 = [5, 4, 3, 2, 1],sensor2 = [5, 4, 2, 1, 1]) == 2
    assert candidate(sensor1 = [1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1]) == -1
    assert candidate(sensor1 = [10, 20, 30, 40, 50],sensor2 = [10, 20, 30, 50, 45]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5],sensor2 = [1, 2, 4, 5, 7]) == 2
    assert candidate(sensor1 = [5, 4, 3, 2, 1],sensor2 = [5, 4, 2, 1, 3]) == 2
    assert candidate(sensor1 = [5, 6, 7, 8],sensor2 = [5, 6, 7, 9]) == -1
    assert candidate(sensor1 = [9, 8, 7, 6],sensor2 = [9, 8, 6, 5]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5],sensor2 = [1, 2, 3, 4, 8]) == -1
    assert candidate(sensor1 = [2, 3, 4, 5],sensor2 = [2, 1, 3, 4]) == 1
    assert candidate(sensor1 = [2, 3, 2, 2, 3, 2],sensor2 = [2, 3, 2, 3, 2, 7]) == 2
    assert candidate(sensor1 = [2, 2, 2, 2, 2],sensor2 = [2, 2, 2, 2, 5]) == -1
    assert candidate(sensor1 = [1, 1, 1, 1],sensor2 = [1, 1, 1, 1]) == -1
    assert candidate(sensor1 = [5, 6, 7, 8],sensor2 = [5, 6, 8, 9]) == 2
    assert candidate(sensor1 = [1, 3, 4],sensor2 = [1, 2, 4]) == 1
    assert candidate(sensor1 = [1, 3, 5, 7, 9],sensor2 = [1, 3, 4, 7, 8]) == 1
    assert candidate(sensor1 = [1, 2, 3],sensor2 = [1, 3, 4]) == 2
    assert candidate(sensor1 = [5, 6, 7, 8, 9, 10],sensor2 = [5, 6, 8, 9, 10, 12]) == 2
    assert candidate(sensor1 = [10, 20, 30, 40, 50, 60, 70],sensor2 = [10, 20, 30, 40, 50, 60, 80]) == -1
    assert candidate(sensor1 = [3, 3, 3, 3, 3, 3, 3, 3],sensor2 = [3, 3, 3, 3, 3, 3, 3, 7]) == -1
    assert candidate(sensor1 = [9, 8, 7, 6, 5, 4],sensor2 = [9, 8, 7, 6, 4, 5]) == -1
    assert candidate(sensor1 = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40],sensor2 = [4, 8, 12, 16, 20, 24, 28, 36, 40, 32]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 3, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(sensor1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],sensor2 = [10, 20, 30, 40, 50, 60, 70, 80, 95, 100]) == 1
    assert candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 99]) == -1
    assert candidate(sensor1 = [1, 3, 2, 4, 5, 6, 7, 8, 9],sensor2 = [1, 3, 2, 4, 5, 6, 7, 8, 10]) == -1
    assert candidate(sensor1 = [20, 19, 18, 17, 16],sensor2 = [20, 19, 18, 16, 17]) == -1
    assert candidate(sensor1 = [1, 2, 2, 3, 4, 4, 5],sensor2 = [1, 2, 2, 4, 4, 5, 6]) == 2
    assert candidate(sensor1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],sensor2 = [10, 11, 12, 14, 15, 16, 17, 18, 19, 20]) == 2
    assert candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == -1
    assert candidate(sensor1 = [5, 10, 15, 20, 25, 30],sensor2 = [5, 10, 20, 25, 30, 40]) == 2
    assert candidate(sensor1 = [5, 6, 7, 8, 9, 10],sensor2 = [5, 6, 7, 9, 10, 11]) == 2
    assert candidate(sensor1 = [3, 3, 3, 1, 3, 3, 3],sensor2 = [3, 3, 3, 3, 3, 3, 9]) == 2
    assert candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 7, 6, 5, 4, 3, 1, 1]) == 2
    assert candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == -1
    assert candidate(sensor1 = [100, 99, 98, 97, 96, 95],sensor2 = [100, 99, 98, 97, 95, 94]) == 2
    assert candidate(sensor1 = [10, 20, 30, 40, 50, 60],sensor2 = [10, 20, 30, 40, 60, 65]) == 2
    assert candidate(sensor1 = [5, 6, 7, 8, 9, 10],sensor2 = [5, 6, 8, 9, 10, 15]) == 2
    assert candidate(sensor1 = [5, 15, 25, 35, 45, 55, 65],sensor2 = [5, 15, 25, 35, 45, 55, 75]) == -1
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
    assert candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 7, 6, 5, 4, 3, 2, 10]) == -1
    assert candidate(sensor1 = [1, 1, 2, 2, 3, 3, 4, 4],sensor2 = [1, 1, 2, 2, 3, 4, 4, 5]) == 2
    assert candidate(sensor1 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],sensor2 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 4]) == -1
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 9]) == -1
    assert candidate(sensor1 = [7, 8, 9, 10, 11, 12, 13, 14, 15],sensor2 = [7, 8, 10, 11, 12, 13, 14, 15, 16]) == 2
    assert candidate(sensor1 = [3, 5, 7, 9, 11, 13, 15, 17],sensor2 = [3, 5, 8, 9, 11, 13, 15, 18]) == 1
    assert candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 7, 6, 4, 3, 2, 1, 10]) == 2
    assert candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 6, 5, 4, 3, 2, 1, 0]) == 2
    assert candidate(sensor1 = [100, 99, 98, 97, 96],sensor2 = [100, 99, 98, 96, 95]) == 2
    assert candidate(sensor1 = [25, 50, 75, 100, 125, 150, 175, 200],sensor2 = [25, 50, 100, 125, 150, 175, 200, 225]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21]) == 2
    assert candidate(sensor1 = [1, 1, 1, 1, 2, 1],sensor2 = [1, 1, 1, 1, 1, 3]) == 2
    assert candidate(sensor1 = [7, 8, 9, 10, 11, 12, 13],sensor2 = [7, 8, 10, 11, 12, 13, 14]) == 2
    assert candidate(sensor1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],sensor2 = [1, 3, 5, 7, 8, 10, 12, 14, 16, 18]) == 1
    assert candidate(sensor1 = [10, 20, 30, 40, 50, 60, 70, 80, 90],sensor2 = [10, 20, 30, 50, 60, 70, 80, 90, 100]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 6, 7, 8, 9, 10, 10]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 5, 6, 7, 8, 9, 10, 10]) == 2
    assert candidate(sensor1 = [5, 15, 25, 35, 45, 55],sensor2 = [5, 15, 25, 35, 45, 65]) == -1
    assert candidate(sensor1 = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81],sensor2 = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 82, 83, 80]) == 1
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]) == 2
    assert candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 2]) == -1
    assert candidate(sensor1 = [100, 99, 98, 97, 96, 95, 94, 93],sensor2 = [100, 99, 97, 96, 95, 94, 93, 92]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]) == 2
    assert candidate(sensor1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],sensor2 = [10, 20, 30, 40, 60, 70, 80, 90, 100, 110]) == 2
    assert candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 7, 6, 5, 4, 2, 1, 0]) == 2
    assert candidate(sensor1 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],sensor2 = [3, 6, 9, 12, 15, 18, 21, 24, 30, 28]) == 2
    assert candidate(sensor1 = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],sensor2 = [7, 14, 21, 28, 35, 42, 49, 63, 56, 71]) == 1
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11]) == 2
    assert candidate(sensor1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],sensor2 = [2, 4, 6, 8, 10, 12, 14, 18, 20, 16]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 3, 4, 5, 6, 7, 9, 10]) == 2
    assert candidate(sensor1 = [7, 8, 9, 10, 11, 12, 13],sensor2 = [7, 8, 9, 10, 12, 13, 14]) == 2
    assert candidate(sensor1 = [1, 1, 2, 3, 1, 1],sensor2 = [1, 1, 2, 1, 1, 1]) == 2
    assert candidate(sensor1 = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],sensor2 = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5]) == -1
    assert candidate(sensor1 = [5, 6, 7, 8, 9, 10],sensor2 = [5, 6, 7, 9, 10, 11]) == 2
    assert candidate(sensor1 = [7, 8, 9, 10, 11, 12, 13, 14, 15],sensor2 = [7, 8, 9, 11, 12, 13, 14, 15, 16]) == 2
    assert candidate(sensor1 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],sensor2 = [5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16]) == 2
    assert candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 1, 2]) == -1
    assert candidate(sensor1 = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21],sensor2 = [3, 5, 7, 9, 11, 14, 15, 17, 19, 21]) == 1
    assert candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 7, 6, 4, 3, 2, 1, 0]) == 2
    assert candidate(sensor1 = [9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [9, 8, 7, 6, 5, 4, 3, 1, 2]) == -1
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == -1
    assert candidate(sensor1 = [42, 42, 42, 42, 42, 42, 42, 42],sensor2 = [42, 42, 42, 42, 42, 42, 42, 99]) == -1
    assert candidate(sensor1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],sensor2 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6]) == -1
    assert candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == -1
    assert candidate(sensor1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 10]) == -1
    assert candidate(sensor1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],sensor2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 22]) == -1
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]) == 2
    assert candidate(sensor1 = [1, 3, 2, 4, 5, 6],sensor2 = [1, 2, 3, 4, 5, 7]) == 1
    assert candidate(sensor1 = [1, 2, 3, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
    assert candidate(sensor1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],sensor2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5]) == -1
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21]) == -1
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 3, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(sensor1 = [10, 20, 30, 40, 50, 60],sensor2 = [10, 20, 30, 50, 60, 70]) == 2
    assert candidate(sensor1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],sensor2 = [1, 1, 2, 2, 3, 3, 4, 4, 4, 6]) == 1
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 3, 4, 5, 7, 8, 9, 10]) == 2
    assert candidate(sensor1 = [3, 5, 7, 9, 11, 13],sensor2 = [3, 5, 7, 11, 13, 15]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],sensor2 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 2
    assert candidate(sensor1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],sensor2 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 6]) == -1
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 4, 5, 6, 7, 8, 9, 11]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11]) == 2
    assert candidate(sensor1 = [1, 2, 2, 2, 3, 2, 2, 2, 4, 5, 6],sensor2 = [1, 2, 2, 2, 3, 2, 2, 3, 2, 2, 9]) == 1
    assert candidate(sensor1 = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2
    assert candidate(sensor1 = [100, 99, 98, 97, 96, 95],sensor2 = [100, 99, 98, 97, 96, 94]) == -1
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]) == 2
    assert candidate(sensor1 = [42, 43, 44, 45, 46, 47, 48],sensor2 = [42, 43, 45, 46, 47, 48, 49]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1],sensor2 = [1, 2, 3, 4, 4, 3, 2, 1, 0, 0]) == 1
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9],sensor2 = [1, 2, 3, 4, 5, 6, 8, 9, 10]) == 2
    assert candidate(sensor1 = [7, 14, 21, 28, 35, 42],sensor2 = [7, 14, 21, 28, 42, 49]) == 2
    assert candidate(sensor1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],sensor2 = [1, 3, 5, 7, 9, 11, 13, 15, 18, 19]) == 1
    assert candidate(sensor1 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],sensor2 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 20]) == -1
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]) == 2
    assert candidate(sensor1 = [1, 3, 2, 3, 4, 5, 6],sensor2 = [1, 3, 2, 3, 4, 5, 7]) == -1
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8],sensor2 = [1, 2, 3, 4, 6, 7, 8, 9]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 4, 5, 6, 7, 8, 10, 10]) == 2
    assert candidate(sensor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],sensor2 = [1, 2, 3, 5, 6, 7, 8, 9, 10, 9]) == 2


