def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(arr = [3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1000000000, 2, 3, 4]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1000000000, 2, 3, 4]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 7, 5, 3, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 7, 5, 3, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000000000, 1, 1000000000, 1, 1000000000]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000000000, 1, 1000000000, 1, 1000000000]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 20, 30, 40]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 20, 30, 40]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1000000000, 2, 1000000000, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1000000000, 2, 1000000000, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 1, 1000]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 1, 1000]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 100, 1000, 10000]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 100, 1000, 10000]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 4, 5, 6]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 4, 5, 6]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 1, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 1, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [999999999, 1, 999999998, 2, 999999997, 3, 999999996, 4, 999999995, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [999999999, 1, 999999998, 2, 999999997, 3, 999999996, 4, 999999995, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 6, 10, 15, 21]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 6, 10, 15, 21]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 50, 25, 12, 6, 3, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 50, 25, 12, 6, 3, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000000000, 1, 1000000000, 1, 1000000000]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000000000, 1, 1000000000, 1, 1000000000]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 100, 2, 101, 3, 102, 4, 103, 5, 104]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 100, 2, 101, 3, 102, 4, 103, 5, 104]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 100, 100, 100, 100, 100, 100]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 100, 100, 100, 100, 100, 100]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 25, 75, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 25, 75, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000000000, 1000000000, 1000000000, 1000000000, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000000000, 1000000000, 1000000000, 1000000000, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1000000000, 2, 999999999, 3, 999999998]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1000000000, 2, 999999999, 3, 999999998]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 3, 1, 4, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 3, 1, 4, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 50, 20, 10, 5, 2, 1, 2, 5, 10, 20, 50, 100, 150, 200, 250, 300]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 50, 20, 10, 5, 2, 1, 2, 5, 10, 20, 50, 100, 150, 200, 250, 300]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 1, 2, 2, 3, 4, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 1, 2, 2, 3, 4, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 40, 30, 20, 10, 5, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 40, 30, 20, 10, 5, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8, 7]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8, 7]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [50, 40, 30, 20, 10, 1, 2, 3, 4, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [50, 40, 30, 20, 10, 1, 2, 3, 4, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 999999999, 999999998, 999999997, 999999996, 999999995]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 999999999, 999999998, 999999997, 999999996, 999999995]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000, 1000, 1000, 1000, 1000]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000, 1000, 1000, 1000, 1000]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000000000, 1000000000, 1000000000, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000000000, 1000000000, 1000000000, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000000000, 999999999, 1000000001, 2, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000000000, 999999999, 1000000001, 2, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [999999999, 999999998, 999999997, 999999996, 999999995, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [999999999, 999999998, 999999997, 999999996, 999999995, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1, 1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1, 1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 10, 100, 1000]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 10, 100, 1000]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 5, 15, 20, 1, 3, 8]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 5, 15, 20, 1, 3, 8]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000000000, 1, 1000000000, 2, 1000000000, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000000000, 1, 1000000000, 2, 1000000000, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 4, 4, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 4, 4, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [3, 3, 3, 3, 3, 2, 2, 2, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [3, 3, 3, 3, 3, 2, 2, 2, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1, 1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1, 1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1000000000, 2, 999999999, 3]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1000000000, 2, 999999999, 3]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1000000000, 2, 999999999, 3, 999999998]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1000000000, 2, 999999999, 3, 999999998]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [5, 4, 3, 2, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [5, 4, 3, 2, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(arr = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(arr = [1, 2, 3, 100, 200, 300, 400, 500]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(arr = [1, 2, 3, 100, 200, 300, 400, 500]) == 8: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(arr = [3, 2, 1]) == 3
    assert candidate(arr = [5, 4, 3, 2, 1]) == 5
    assert candidate(arr = [1, 1000000000, 2, 3, 4]) == 5
    assert candidate(arr = [9, 7, 5, 3, 1]) == 5
    assert candidate(arr = [5, 5, 5, 5, 5]) == 5
    assert candidate(arr = [1000000000, 1, 1000000000, 1, 1000000000]) == 4
    assert candidate(arr = [1, 10, 20, 30, 40]) == 5
    assert candidate(arr = [1, 1000000000, 2, 1000000000, 3]) == 5
    assert candidate(arr = [1]) == 1
    assert candidate(arr = [100, 1, 1000]) == 3
    assert candidate(arr = [1, 1, 1, 1, 1]) == 1
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(arr = [1, 10, 100, 1000, 10000]) == 5
    assert candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4
    assert candidate(arr = [1, 2, 3, 4, 5]) == 5
    assert candidate(arr = [2, 3, 4, 5, 6]) == 5
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
    assert candidate(arr = [2, 2, 1, 2, 1]) == 2
    assert candidate(arr = [1, 3, 5, 7, 9]) == 5
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(arr = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 4
    assert candidate(arr = [999999999, 1, 999999998, 2, 999999997, 3, 999999996, 4, 999999995, 5]) == 10
    assert candidate(arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 4
    assert candidate(arr = [1, 3, 6, 10, 15, 21]) == 6
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 10]) == 10
    assert candidate(arr = [100, 50, 25, 12, 6, 3, 1]) == 7
    assert candidate(arr = [1000000000, 1, 1000000000, 1, 1000000000]) == 4
    assert candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 6
    assert candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3
    assert candidate(arr = [1, 100, 2, 101, 3, 102, 4, 103, 5, 104]) == 10
    assert candidate(arr = [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 5
    assert candidate(arr = [100, 100, 100, 100, 100, 100, 100]) == 7
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10]) == 10
    assert candidate(arr = [1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 9]) == 9
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
    assert candidate(arr = [50, 25, 75, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 13
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
    assert candidate(arr = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 5
    assert candidate(arr = [1000000000, 1000000000, 1000000000, 1000000000, 1]) == 5
    assert candidate(arr = [1, 1000000000, 2, 999999999, 3, 999999998, 4, 999999997]) == 8
    assert candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 5
    assert candidate(arr = [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 16
    assert candidate(arr = [1, 1000000000, 2, 999999999, 3, 999999998]) == 6
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 20
    assert candidate(arr = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 10
    assert candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
    assert candidate(arr = [39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 20
    assert candidate(arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 10
    assert candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
    assert candidate(arr = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]) == 20
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 10
    assert candidate(arr = [5, 3, 1, 4, 2]) == 5
    assert candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 15
    assert candidate(arr = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 5
    assert candidate(arr = [100, 50, 20, 10, 5, 2, 1, 2, 5, 10, 20, 50, 100, 150, 200, 250, 300]) == 16
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 12
    assert candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
    assert candidate(arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1]) == 20
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == 13
    assert candidate(arr = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120]) == 15
    assert candidate(arr = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3
    assert candidate(arr = [10, 1, 2, 2, 3, 4, 5]) == 6
    assert candidate(arr = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == 10
    assert candidate(arr = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == 20
    assert candidate(arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 15
    assert candidate(arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 2
    assert candidate(arr = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
    assert candidate(arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 10
    assert candidate(arr = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == 20
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 5
    assert candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91]) == 20
    assert candidate(arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(arr = [50, 40, 30, 20, 10, 5, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 9
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 2
    assert candidate(arr = [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
    assert candidate(arr = [2, 1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 6, 7, 8, 7]) == 8
    assert candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == 10
    assert candidate(arr = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 3
    assert candidate(arr = [50, 40, 30, 20, 10, 1, 2, 3, 4, 5]) == 10
    assert candidate(arr = [1, 999999999, 999999998, 999999997, 999999996, 999999995]) == 6
    assert candidate(arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 10
    assert candidate(arr = [1000, 1000, 1000, 1000, 1000]) == 5
    assert candidate(arr = [1000000000, 1000000000, 1000000000, 1, 1, 1]) == 4
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 10
    assert candidate(arr = [1000000000, 999999999, 1000000001, 2, 3]) == 5
    assert candidate(arr = [999999999, 999999998, 999999997, 999999996, 999999995, 1]) == 6
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]) == 10
    assert candidate(arr = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 30
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(arr = [5, 4, 3, 2, 1, 1, 1, 1, 1, 1]) == 5
    assert candidate(arr = [1000000000, 1, 1000000000, 1, 1000000000, 1, 1000000000, 1]) == 5
    assert candidate(arr = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]) == 10
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 20
    assert candidate(arr = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 5
    assert candidate(arr = [5, 4, 3, 2, 1, 1, 1]) == 5
    assert candidate(arr = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11]) == 11
    assert candidate(arr = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(arr = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 20
    assert candidate(arr = [1, 2, 3, 4, 5, 10, 100, 1000]) == 8
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 30
    assert candidate(arr = [10, 5, 15, 20, 1, 3, 8]) == 7
    assert candidate(arr = [5, 4, 3, 2, 1]) == 5
    assert candidate(arr = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900]) == 10
    assert candidate(arr = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
    assert candidate(arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5]) == 15
    assert candidate(arr = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 20
    assert candidate(arr = [1000000000, 1, 1000000000, 2, 1000000000, 3]) == 6
    assert candidate(arr = [1000000000, 999999999, 999999998, 999999997, 999999996]) == 5
    assert candidate(arr = [1, 2, 2, 3, 3, 4, 4, 5, 5]) == 5
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 10
    assert candidate(arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 10
    assert candidate(arr = [3, 3, 3, 3, 3, 2, 2, 2, 1, 1]) == 3
    assert candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
    assert candidate(arr = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 10
    assert candidate(arr = [5, 4, 3, 2, 1, 1, 1, 1, 1, 1]) == 5
    assert candidate(arr = [1, 1000000000, 2, 999999999, 3]) == 5
    assert candidate(arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 20
    assert candidate(arr = [1, 1000000000, 2, 999999999, 3, 999999998]) == 6
    assert candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == 2
    assert candidate(arr = [5, 4, 3, 2, 1, 1, 1]) == 5
    assert candidate(arr = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]) == 15
    assert candidate(arr = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 2
    assert candidate(arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]) == 5
    assert candidate(arr = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 15
    assert candidate(arr = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80]) == 21
    assert candidate(arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 2
    assert candidate(arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15]) == 15
    assert candidate(arr = [1, 2, 3, 100, 200, 300, 400, 500]) == 8


