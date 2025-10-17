def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(batteryPercentages = [100, 99, 98, 97, 96]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [100, 99, 98, 97, 96]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [50, 49, 48, 47, 46]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [50, 49, 48, 47, 46]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [100, 100, 100]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [100, 100, 100]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [100, 0, 100, 0, 100]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [100, 0, 100, 0, 100]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [3, 2, 1, 0, 4, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [3, 2, 1, 0, 4, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [3, 0, 2, 0, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [3, 0, 2, 0, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1, 1, 2, 1, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1, 1, 2, 1, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 1, 0, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 1, 0, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [3, 2, 1, 0, 4, 3, 2, 1, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [3, 2, 1, 0, 4, 3, 2, 1, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [50, 40, 30, 20, 10]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [50, 40, 30, 20, 10]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [50, 0, 50, 0, 50]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [50, 0, 50, 0, 50]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [100]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [100]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [100, 99, 98, 97]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [100, 99, 98, 97]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [50, 50, 50, 50, 50]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [50, 50, 50, 50, 50]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1, 0, 1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1, 0, 1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1, 0, 1, 0, 1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1, 0, 1, 0, 1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [10, 20, 30, 40, 50]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [10, 20, 30, 40, 50]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1, 0, 2, 0, 3, 0, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1, 0, 2, 0, 3, 0, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [5, 3, 0, 2, 1, 0, 4, 0, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [5, 3, 0, 2, 1, 0, 4, 0, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [3, 0, 3, 0, 3, 0, 3, 0, 3, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [3, 0, 3, 0, 3, 0, 3, 0, 3, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [5, 0, 5, 0, 5, 0, 5, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [5, 0, 5, 0, 5, 0, 5, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 1, 0, 2, 0, 3, 0, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 1, 0, 2, 0, 3, 0, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [100, 0, 99, 1, 98, 2, 97, 3, 96, 4]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [100, 0, 99, 1, 98, 2, 97, 3, 96, 4]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [3, 2, 1, 0, 5, 4, 3, 2, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [3, 2, 1, 0, 5, 4, 3, 2, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 10, 0, 20, 0, 30, 0, 40, 0, 50]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 10, 0, 20, 0, 30, 0, 40, 0, 50]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [20, 20, 19, 19, 18, 18, 17, 17, 16, 16]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [20, 20, 19, 19, 18, 18, 17, 17, 16, 16]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [10, 0, 10, 0, 10, 0, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [10, 0, 10, 0, 10, 0, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [3, 0, 5, 2, 8, 0, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [3, 0, 5, 2, 8, 0, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [3, 2, 1, 0, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [3, 2, 1, 0, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [100, 0, 100, 0, 100, 0, 100]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [100, 0, 100, 0, 100, 0, 100]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [20, 0, 15, 5, 0, 10, 0, 0, 0, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [20, 0, 15, 5, 0, 10, 0, 0, 0, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [50, 25, 0, 75, 100, 0, 0, 25, 50, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [50, 25, 0, 75, 100, 0, 0, 25, 50, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [3, 2, 2, 1, 1, 0, 0, 1, 1, 0]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [3, 2, 2, 1, 1, 0, 0, 1, 1, 0]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [100, 99, 98, 97, 96, 95, 94]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [100, 99, 98, 97, 96, 95, 94]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 100, 0, 100, 0, 100, 0, 100]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 100, 0, 100, 0, 100, 0, 100]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [50, 25, 0, 75, 50, 25, 0, 75, 50, 25]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [50, 25, 0, 75, 50, 25, 0, 75, 50, 25]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [100, 0, 99, 0, 98, 0, 97, 0, 96, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [100, 0, 99, 0, 98, 0, 97, 0, 96, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [100, 99, 98, 97, 96, 95]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [100, 99, 98, 97, 96, 95]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 100, 100, 100, 100]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 100, 100, 100, 100]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0, 4, 0, 0, 5, 0, 0, 6, 0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0, 4, 0, 0, 5, 0, 0, 6, 0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [3, 2, 1, 0, 4, 5, 0, 6]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [3, 2, 1, 0, 4, 5, 0, 6]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [5, 0, 0, 0, 5, 0, 0, 0, 5, 0, 0, 0, 5, 0, 0, 0, 5, 0, 0, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [5, 0, 0, 0, 5, 0, 0, 0, 5, 0, 0, 0, 5, 0, 0, 0, 5, 0, 0, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70]) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70]) == 31: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [3, 2, 1, 0, 1, 2, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [3, 2, 1, 0, 1, 2, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [100, 100, 0, 0, 50, 50, 0, 0, 25, 25]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [100, 100, 0, 0, 50, 50, 0, 0, 25, 25]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [1, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [1, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(batteryPercentages = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(batteryPercentages = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(batteryPercentages = [100, 99, 98, 97, 96]) == 5
    assert candidate(batteryPercentages = [50, 49, 48, 47, 46]) == 5
    assert candidate(batteryPercentages = [100, 100, 100]) == 3
    assert candidate(batteryPercentages = [100, 0, 100, 0, 100]) == 3
    assert candidate(batteryPercentages = [3, 2, 1, 0, 4, 3, 2, 1]) == 3
    assert candidate(batteryPercentages = [3, 0, 2, 0, 1]) == 2
    assert candidate(batteryPercentages = [1, 1, 2, 1, 3]) == 3
    assert candidate(batteryPercentages = [0, 1, 0, 1, 0]) == 1
    assert candidate(batteryPercentages = [1]) == 1
    assert candidate(batteryPercentages = [1, 2, 3, 4, 5]) == 5
    assert candidate(batteryPercentages = [0, 0, 0]) == 0
    assert candidate(batteryPercentages = [3, 2, 1, 0, 4, 3, 2, 1, 0]) == 3
    assert candidate(batteryPercentages = [50, 40, 30, 20, 10]) == 5
    assert candidate(batteryPercentages = [50, 0, 50, 0, 50]) == 3
    assert candidate(batteryPercentages = [0, 1, 2]) == 2
    assert candidate(batteryPercentages = [100]) == 1
    assert candidate(batteryPercentages = [0, 0, 0, 0, 0]) == 0
    assert candidate(batteryPercentages = [100, 99, 98, 97]) == 4
    assert candidate(batteryPercentages = [50, 50, 50, 50, 50]) == 5
    assert candidate(batteryPercentages = [1, 0, 1, 0, 1]) == 1
    assert candidate(batteryPercentages = [0, 0, 0, 0]) == 0
    assert candidate(batteryPercentages = [1, 0, 1, 0, 1, 0, 1]) == 1
    assert candidate(batteryPercentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(batteryPercentages = [0]) == 0
    assert candidate(batteryPercentages = [10, 20, 30, 40, 50]) == 5
    assert candidate(batteryPercentages = [5, 5, 5, 5, 5]) == 5
    assert candidate(batteryPercentages = [1, 0, 2, 0, 3, 0, 4]) == 4
    assert candidate(batteryPercentages = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]) == 5
    assert candidate(batteryPercentages = [5, 3, 0, 2, 1, 0, 4, 0, 3]) == 3
    assert candidate(batteryPercentages = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
    assert candidate(batteryPercentages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
    assert candidate(batteryPercentages = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 1
    assert candidate(batteryPercentages = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
    assert candidate(batteryPercentages = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 10
    assert candidate(batteryPercentages = [3, 0, 3, 0, 3, 0, 3, 0, 3, 0]) == 3
    assert candidate(batteryPercentages = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(batteryPercentages = [5, 0, 5, 0, 5, 0, 5, 0]) == 4
    assert candidate(batteryPercentages = [0, 1, 0, 2, 0, 3, 0, 4]) == 4
    assert candidate(batteryPercentages = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0]) == 1
    assert candidate(batteryPercentages = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
    assert candidate(batteryPercentages = [100, 0, 99, 1, 98, 2, 97, 3, 96, 4]) == 5
    assert candidate(batteryPercentages = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 2
    assert candidate(batteryPercentages = [3, 2, 1, 0, 5, 4, 3, 2, 1]) == 4
    assert candidate(batteryPercentages = [0, 10, 0, 20, 0, 30, 0, 40, 0, 50]) == 5
    assert candidate(batteryPercentages = [20, 20, 19, 19, 18, 18, 17, 17, 16, 16]) == 10
    assert candidate(batteryPercentages = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 10
    assert candidate(batteryPercentages = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == 8
    assert candidate(batteryPercentages = [10, 0, 10, 0, 10, 0, 10]) == 4
    assert candidate(batteryPercentages = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == 10
    assert candidate(batteryPercentages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0]) == 5
    assert candidate(batteryPercentages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(batteryPercentages = [5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5]) == 5
    assert candidate(batteryPercentages = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 20
    assert candidate(batteryPercentages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(batteryPercentages = [3, 0, 5, 2, 8, 0, 6]) == 4
    assert candidate(batteryPercentages = [3, 2, 1, 0, 4, 5]) == 4
    assert candidate(batteryPercentages = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9
    assert candidate(batteryPercentages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(batteryPercentages = [100, 0, 100, 0, 100, 0, 100]) == 4
    assert candidate(batteryPercentages = [20, 0, 15, 5, 0, 10, 0, 0, 0, 5]) == 5
    assert candidate(batteryPercentages = [50, 25, 0, 75, 100, 0, 0, 25, 50, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 7
    assert candidate(batteryPercentages = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0]) == 10
    assert candidate(batteryPercentages = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(batteryPercentages = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91]) == 10
    assert candidate(batteryPercentages = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 1
    assert candidate(batteryPercentages = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(batteryPercentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(batteryPercentages = [3, 2, 2, 1, 1, 0, 0, 1, 1, 0]) == 2
    assert candidate(batteryPercentages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
    assert candidate(batteryPercentages = [100, 99, 98, 97, 96, 95, 94]) == 7
    assert candidate(batteryPercentages = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(batteryPercentages = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10
    assert candidate(batteryPercentages = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5]) == 5
    assert candidate(batteryPercentages = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(batteryPercentages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
    assert candidate(batteryPercentages = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3
    assert candidate(batteryPercentages = [0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0]) == 3
    assert candidate(batteryPercentages = [0, 100, 0, 100, 0, 100, 0, 100]) == 4
    assert candidate(batteryPercentages = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 7
    assert candidate(batteryPercentages = [50, 25, 0, 75, 50, 25, 0, 75, 50, 25]) == 8
    assert candidate(batteryPercentages = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10]) == 10
    assert candidate(batteryPercentages = [50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100, 50, 100]) == 20
    assert candidate(batteryPercentages = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0]) == 5
    assert candidate(batteryPercentages = [90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0, 90, 0]) == 15
    assert candidate(batteryPercentages = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(batteryPercentages = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6]) == 6
    assert candidate(batteryPercentages = [100, 0, 99, 0, 98, 0, 97, 0, 96, 0]) == 5
    assert candidate(batteryPercentages = [3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1, 3, 2, 1]) == 3
    assert candidate(batteryPercentages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1
    assert candidate(batteryPercentages = [2, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1]) == 2
    assert candidate(batteryPercentages = [100, 99, 98, 97, 96, 95]) == 6
    assert candidate(batteryPercentages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 100, 100, 100, 100]) == 5
    assert candidate(batteryPercentages = [0, 0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0, 4, 0, 0, 5, 0, 0, 6, 0]) == 6
    assert candidate(batteryPercentages = [3, 2, 1, 0, 4, 5, 0, 6]) == 5
    assert candidate(batteryPercentages = [5, 0, 0, 0, 5, 0, 0, 0, 5, 0, 0, 0, 5, 0, 0, 0, 5, 0, 0, 0]) == 5
    assert candidate(batteryPercentages = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70]) == 31
    assert candidate(batteryPercentages = [3, 2, 1, 0, 1, 2, 3]) == 3
    assert candidate(batteryPercentages = [100, 100, 0, 0, 50, 50, 0, 0, 25, 25]) == 6
    assert candidate(batteryPercentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 10
    assert candidate(batteryPercentages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(batteryPercentages = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]) == 5
    assert candidate(batteryPercentages = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 5
    assert candidate(batteryPercentages = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]) == 1
    assert candidate(batteryPercentages = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]) == 29
    assert candidate(batteryPercentages = [1, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 1]) == 10
    assert candidate(batteryPercentages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(batteryPercentages = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 10


