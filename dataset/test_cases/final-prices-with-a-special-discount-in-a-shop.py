def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5]) == [0, 0, 0, 0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5]) == [0, 0, 0, 0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 4, 6, 2, 3]) == [4, 2, 4, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 4, 6, 2, 3]) == [4, 2, 4, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [9, 8, 7, 6, 5]) == [1, 1, 1, 1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [9, 8, 7, 6, 5]) == [1, 1, 1, 1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17]) == [1, 3, 5, 7, 9, 11, 13, 15, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17]) == [1, 3, 5, 7, 9, 11, 13, 15, 17]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [60, 70, 80, 90, 100]) == [60, 70, 80, 90, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [60, 70, 80, 90, 100]) == [60, 70, 80, 90, 100]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 10, 10, 10, 10, 10]) == [0, 0, 0, 0, 0, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 10, 10, 10, 10, 10]) == [0, 0, 0, 0, 0, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 1, 4, 2, 3]) == [4, 1, 2, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 1, 4, 2, 3]) == [4, 1, 2, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 50, 25, 12, 6, 3, 1]) == [50, 25, 13, 6, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 50, 25, 12, 6, 3, 1]) == [50, 25, 13, 6, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 1, 1, 6]) == [9, 0, 1, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 1, 1, 6]) == [9, 0, 1, 6]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1]) == [0, 0, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1]) == [0, 0, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 1, 3, 4, 6, 2]) == [4, 1, 1, 2, 4, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 1, 3, 4, 6, 2]) == [4, 1, 1, 2, 4, 2]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 3, 2, 2, 1]) == [0, 0, 1, 0, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 3, 2, 2, 1]) == [0, 0, 1, 0, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 90, 80, 70, 60]) == [10, 10, 10, 10, 60]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 90, 80, 70, 60]) == [10, 10, 10, 10, 60]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 200, 300, 200, 100]) == [0, 0, 100, 100, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 200, 300, 200, 100]) == [0, 0, 100, 100, 100]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1]) == [0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1]) == [0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 3, 1]) == [1, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 3, 1]) == [1, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 50, 50, 100, 50, 25, 25, 100]) == [50, 0, 0, 50, 25, 0, 25, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 50, 50, 100, 50, 25, 25, 100]) == [50, 0, 0, 50, 25, 0, 25, 100]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == [5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 5, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == [5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 5, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0]) == [50, 25, 13, 6, 3, 2, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0]) == [50, 25, 13, 6, 3, 2, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 3, 4, 5, 4, 5, 6]) == [1, 0, 1, 2, 3, 0, 1, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 3, 4, 5, 4, 5, 6]) == [1, 0, 1, 2, 3, 0, 1, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == [1, 98, 2, 96, 3, 94, 4, 92, 5, 96]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == [1, 98, 2, 96, 3, 94, 4, 92, 5, 96]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10]) == [0, 0, 0, 0, 0, 0, 0, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10]) == [0, 0, 0, 0, 0, 0, 0, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 5, 15, 5, 20, 10, 25, 15, 30, 20]) == [5, 0, 10, 5, 10, 10, 10, 15, 10, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 5, 15, 5, 20, 10, 25, 15, 30, 20]) == [5, 0, 10, 5, 10, 10, 10, 15, 10, 20]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 6, 5, 4, 3, 2, 1, 2, 3, 4]) == [1, 1, 1, 1, 1, 1, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 6, 5, 4, 3, 2, 1, 2, 3, 4]) == [1, 1, 1, 1, 1, 1, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == [0, 9, 0, 9, 0, 9, 0, 9, 1, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == [0, 9, 0, 9, 0, 9, 0, 9, 1, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 5, 6, 4, 3, 2, 1, 8, 9, 10]) == [2, 1, 2, 1, 1, 1, 1, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 5, 6, 4, 3, 2, 1, 8, 9, 10]) == [2, 1, 2, 1, 1, 1, 1, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 3, 3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1]) == [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 3, 3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1]) == [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [0, 8, 1, 6, 2, 4, 3, 2, 4, 5, 1, 8, 2, 6, 3, 4, 4, 2, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [0, 8, 1, 6, 2, 4, 3, 2, 4, 5, 1, 8, 2, 6, 3, 4, 4, 2, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1000]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == [0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0, 4, 0, 0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == [0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0, 4, 0, 0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1]) == [500, 250, 125, 63, 31, 16, 8, 4, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1]) == [500, 250, 125, 63, 31, 16, 8, 4, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 40, 50, 40, 30, 20, 10]) == [0, 0, 0, 0, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 40, 50, 40, 30, 20, 10]) == [0, 0, 0, 0, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == [0, 10, 0, 10, 0, 10, 0, 10, 10, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == [0, 10, 0, 10, 0, 10, 0, 10, 10, 20]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == [0, 0, 1, 1, 0, 0, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == [0, 0, 1, 1, 0, 0, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [30, 20, 10, 10, 20, 30, 40, 50, 40, 30, 20, 10]) == [10, 10, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [30, 20, 10, 10, 20, 30, 40, 50, 40, 30, 20, 10]) == [10, 10, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == [1, 1, 1, 1, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == [1, 1, 1, 1, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 6, 7, 6, 5, 4, 3, 2, 1]) == [2, 0, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 6, 7, 6, 5, 4, 3, 2, 1]) == [2, 0, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [300, 200, 100, 50, 25, 12, 6, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [100, 100, 50, 25, 13, 6, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [300, 200, 100, 50, 25, 12, 6, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [100, 100, 50, 25, 13, 6, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 4, 6, 2, 3, 8, 4, 6, 2, 3]) == [4, 2, 4, 0, 1, 4, 2, 4, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 4, 6, 2, 3, 8, 4, 6, 2, 3]) == [4, 2, 4, 0, 1, 4, 2, 4, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 1, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 1, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == [1, 1, 2, 1, 3, 1, 4, 1, 5, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == [1, 1, 2, 1, 3, 1, 4, 1, 5, 7]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [15, 10, 5, 10, 15, 5, 10, 15, 20, 10]) == [5, 5, 0, 5, 10, 5, 0, 5, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [15, 10, 5, 10, 15, 5, 10, 15, 20, 10]) == [5, 5, 0, 5, 10, 5, 0, 5, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 10, 20, 30, 10, 20, 30]) == [0, 10, 20, 0, 10, 20, 10, 20, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 10, 20, 30, 10, 20, 30]) == [0, 10, 20, 0, 10, 20, 10, 20, 30]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 6, 5, 1, 8, 7, 9, 2, 4, 10]) == [2, 1, 4, 1, 1, 5, 7, 2, 4, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 6, 5, 1, 8, 7, 9, 2, 4, 10]) == [2, 1, 4, 1, 1, 5, 7, 2, 4, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == [0, 1, 0, 1, 0, 1, 0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == [0, 1, 0, 1, 0, 1, 0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 5, 7, 6, 4, 5, 3, 2, 1]) == [3, 1, 1, 2, 1, 2, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 5, 7, 6, 4, 5, 3, 2, 1]) == [3, 1, 1, 2, 1, 2, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [50, 25, 13, 6, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [50, 25, 13, 6, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50, 20, 30, 10, 20, 30, 40, 50, 60, 70]) == [30, 10, 20, 10, 20, 30, 40, 50, 60, 70]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50, 20, 30, 10, 20, 30, 40, 50, 60, 70]) == [30, 10, 20, 10, 20, 30, 40, 50, 60, 70]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -5]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [500, 100, 200, 300, 400, 500, 600, 700, 800, 900]) == [400, 100, 200, 300, 400, 500, 600, 700, 800, 900]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [500, 100, 200, 300, 400, 500, 600, 700, 800, 900]) == [400, 100, 200, 300, 400, 500, 600, 700, 800, 900]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5]) == [99, 1, 198, 2, 297, 3, 396, 4, 495, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5]) == [99, 1, 198, 2, 297, 3, 396, 4, 495, 5]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [999, 1000, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 980]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [999, 1000, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 980]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 200, 150, 250, 300, 220, 180, 160, 170]) == [100, 50, 150, 30, 80, 40, 20, 160, 170]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 200, 150, 250, 300, 220, 180, 160, 170]) == [100, 50, 150, 30, 80, 40, 20, 160, 170]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 10, 15, 20, 15, 10, 5, 10, 15, 20, 15, 10, 5]) == [0, 0, 0, 5, 5, 5, 0, 0, 0, 5, 5, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 10, 15, 20, 15, 10, 5, 10, 15, 20, 15, 10, 5]) == [0, 0, 0, 5, 5, 5, 0, 0, 0, 5, 5, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 3, 3, 1, 1, 1, 1, 5, 5, 5, 5]) == [0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 3, 3, 1, 1, 1, 1, 5, 5, 5, 5]) == [0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 15, 25, 10, 20, 5, 30, 25, 40, 10]) == [0, 5, 15, 5, 15, 5, 5, 15, 30, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 15, 25, 10, 20, 5, 30, 25, 40, 10]) == [0, 5, 15, 5, 15, 5, 5, 15, 30, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1000, 1000, 1000, 1000, 1000]) == [0, 0, 0, 0, 1000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1000, 1000, 1000, 1000, 1000]) == [0, 0, 0, 0, 1000]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 1, 4, 3, 2, 6, 7, 8, 10, 9]) == [4, 1, 1, 1, 2, 6, 7, 8, 1, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 1, 4, 3, 2, 6, 7, 8, 10, 9]) == [4, 1, 1, 1, 2, 6, 7, 8, 1, 9]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 4, 6, 2, 3, 5, 7, 1, 9, 10]) == [4, 2, 4, 1, 2, 4, 6, 1, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 4, 6, 2, 3, 5, 7, 1, 9, 10]) == [4, 2, 4, 1, 2, 4, 6, 1, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1]) == [100, 100, 100, 100, 50, 25, 13, 6, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1]) == [100, 100, 100, 100, 50, 25, 13, 6, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [250, 200, 150, 100, 50, 100, 150, 200, 250, 300]) == [50, 50, 50, 50, 50, 100, 150, 200, 250, 300]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [250, 200, 150, 100, 50, 100, 150, 200, 250, 300]) == [50, 50, 50, 50, 50, 100, 150, 200, 250, 300]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10]) == [0, 9, 0, 9, 0, 9, 1, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10]) == [0, 9, 0, 9, 0, 9, 1, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [30, 25, 20, 15, 10, 5, 10, 15, 20, 25]) == [5, 5, 5, 5, 5, 5, 10, 15, 20, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [30, 25, 20, 15, 10, 5, 10, 15, 20, 25]) == [5, 5, 5, 5, 5, 5, 10, 15, 20, 25]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [4, 3, 2, 1, 2, 3, 4, 5, 6, 7]) == [1, 1, 1, 1, 2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [4, 3, 2, 1, 2, 3, 4, 5, 6, 7]) == [1, 1, 1, 1, 2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == [1, 1, 1, 1, 0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == [1, 1, 1, 1, 0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 50]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 1, 0, 0, 0, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == [0, 5, 0, 5, 0, 5, 0, 5, 5, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == [0, 5, 0, 5, 0, 5, 0, 5, 5, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 6, 5, 4, 3, 2, 1, 0, 0, 0]) == [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 6, 5, 4, 3, 2, 1, 0, 0, 0]) == [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 2, 1, 1, 2, 2, 1, 1]) == [0, 0, 1, 0, 0, 0, 1, 0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 2, 1, 1, 2, 2, 1, 1]) == [0, 0, 1, 0, 0, 0, 1, 0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 50, 25, 200, 100, 50, 25, 200]) == [50, 25, 0, 100, 50, 25, 25, 200]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 50, 25, 200, 100, 50, 25, 200]) == [50, 25, 0, 100, 50, 25, 25, 200]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8]) == [1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8]) == [1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == [0, 9, 0, 9, 0, 9, 0, 9, 1, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == [0, 9, 0, 9, 0, 9, 0, 9, 1, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5]) == [0, 0, 0, 0, 10, 10, 10, 10, 5, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5]) == [0, 0, 0, 0, 10, 10, 10, 10, 5, 5]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50, 40, 30, 20, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == [10, 10, 10, 10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50, 40, 30, 20, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == [10, 10, 10, 10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == [4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == [4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50, 25, 75, 100, 50, 75, 100, 125]) == [25, 25, 25, 50, 50, 75, 100, 125]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50, 25, 75, 100, 50, 75, 100, 125]) == [25, 25, 25, 50, 50, 75, 100, 125]: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 200, 300, 400, 500, 400, 300, 200, 100]) == [0, 0, 0, 0, 100, 100, 100, 100, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 200, 300, 400, 500, 400, 300, 200, 100]) == [0, 0, 0, 0, 100, 100, 100, 100, 100]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(prices = [5, 5, 5, 5, 5]) == [0, 0, 0, 0, 5]
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(prices = [8, 4, 6, 2, 3]) == [4, 2, 4, 2, 3]
    assert candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    assert candidate(prices = [9, 8, 7, 6, 5]) == [1, 1, 1, 1, 5]
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17]) == [1, 3, 5, 7, 9, 11, 13, 15, 17]
    assert candidate(prices = [60, 70, 80, 90, 100]) == [60, 70, 80, 90, 100]
    assert candidate(prices = [10, 10, 10, 10, 10, 10]) == [0, 0, 0, 0, 0, 10]
    assert candidate(prices = [5, 1, 4, 2, 3]) == [4, 1, 2, 2, 3]
    assert candidate(prices = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]) == [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    assert candidate(prices = [100, 50, 25, 12, 6, 3, 1]) == [50, 25, 13, 6, 3, 2, 1]
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(prices = [10, 1, 1, 6]) == [9, 0, 1, 6]
    assert candidate(prices = [1, 2, 3, 2, 1]) == [0, 0, 1, 1, 1]
    assert candidate(prices = [5, 1, 3, 4, 6, 2]) == [4, 1, 1, 2, 4, 2]
    assert candidate(prices = [3, 3, 3, 2, 2, 1]) == [0, 0, 1, 0, 1, 1]
    assert candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(prices = [100, 90, 80, 70, 60]) == [10, 10, 10, 10, 60]
    assert candidate(prices = [100, 200, 300, 200, 100]) == [0, 0, 100, 100, 100]
    assert candidate(prices = [1, 1, 1, 1, 1]) == [0, 0, 0, 0, 1]
    assert candidate(prices = [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert candidate(prices = [2, 3, 1]) == [1, 2, 1]
    assert candidate(prices = [100, 50, 50, 100, 50, 25, 25, 100]) == [50, 0, 0, 50, 25, 0, 25, 100]
    assert candidate(prices = [10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == [5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 5, 10]
    assert candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0]) == [50, 25, 13, 6, 3, 2, 1, 0, 0, 0]
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5]
    assert candidate(prices = [1, 2, 3, 2, 3, 4, 5, 4, 5, 6]) == [1, 0, 1, 2, 3, 0, 1, 4, 5, 6]
    assert candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 2]
    assert candidate(prices = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    assert candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 10]
    assert candidate(prices = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == [1, 98, 2, 96, 3, 94, 4, 92, 5, 96]
    assert candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10]) == [0, 0, 0, 0, 0, 0, 0, 10]
    assert candidate(prices = [10, 5, 15, 5, 20, 10, 25, 15, 30, 20]) == [5, 0, 10, 5, 10, 10, 10, 15, 10, 20]
    assert candidate(prices = [7, 6, 5, 4, 3, 2, 1, 2, 3, 4]) == [1, 1, 1, 1, 1, 1, 1, 2, 3, 4]
    assert candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == [0, 9, 0, 9, 0, 9, 0, 9, 1, 10]
    assert candidate(prices = [7, 5, 6, 4, 3, 2, 1, 8, 9, 10]) == [2, 1, 2, 1, 1, 1, 1, 8, 9, 10]
    assert candidate(prices = [2, 3, 3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1, 1, 2, 3, 2, 1]) == [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1]
    assert candidate(prices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 1, 2, 3, 4, 5]
    assert candidate(prices = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [0, 8, 1, 6, 2, 4, 3, 2, 4, 5, 1, 8, 2, 6, 3, 4, 4, 2, 5, 6]
    assert candidate(prices = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 1000]
    assert candidate(prices = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]) == [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    assert candidate(prices = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == [0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0, 4, 0, 0, 5]
    assert candidate(prices = [5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    assert candidate(prices = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1]) == [500, 250, 125, 63, 31, 16, 8, 4, 2, 1]
    assert candidate(prices = [10, 20, 30, 40, 50, 40, 30, 20, 10]) == [0, 0, 0, 0, 10, 10, 10, 10, 10]
    assert candidate(prices = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == [0, 10, 0, 10, 0, 10, 0, 10, 10, 20]
    assert candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1]) == [0, 0, 1, 1, 0, 0, 1, 1, 1]
    assert candidate(prices = [30, 20, 10, 10, 20, 30, 40, 50, 40, 30, 20, 10]) == [10, 10, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10]
    assert candidate(prices = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == [1, 1, 1, 1, 1, 2, 3, 4, 5]
    assert candidate(prices = [8, 6, 7, 6, 5, 4, 3, 2, 1]) == [2, 0, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    assert candidate(prices = [300, 200, 100, 50, 25, 12, 6, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [100, 100, 50, 25, 13, 6, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    assert candidate(prices = [8, 4, 6, 2, 3, 8, 4, 6, 2, 3]) == [4, 2, 4, 0, 1, 4, 2, 4, 2, 3]
    assert candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == [0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 0, 9, 1, 10]
    assert candidate(prices = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == [1, 1, 2, 1, 3, 1, 4, 1, 5, 7]
    assert candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
    assert candidate(prices = [15, 10, 5, 10, 15, 5, 10, 15, 20, 10]) == [5, 5, 0, 5, 10, 5, 0, 5, 10, 10]
    assert candidate(prices = [10, 20, 30, 10, 20, 30, 10, 20, 30]) == [0, 10, 20, 0, 10, 20, 10, 20, 30]
    assert candidate(prices = [3, 6, 5, 1, 8, 7, 9, 2, 4, 10]) == [2, 1, 4, 1, 1, 5, 7, 2, 4, 10]
    assert candidate(prices = [2, 3, 2, 3, 2, 3, 2, 3, 2, 3]) == [0, 1, 0, 1, 0, 1, 0, 1, 2, 3]
    assert candidate(prices = [8, 5, 7, 6, 4, 5, 3, 2, 1]) == [3, 1, 1, 2, 1, 2, 1, 1, 1]
    assert candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [50, 25, 13, 6, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(prices = [50, 20, 30, 10, 20, 30, 40, 50, 60, 70]) == [30, 10, 20, 10, 20, 30, 40, 50, 60, 70]
    assert candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5]
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -5]
    assert candidate(prices = [500, 100, 200, 300, 400, 500, 600, 700, 800, 900]) == [400, 100, 200, 300, 400, 500, 600, 700, 800, 900]
    assert candidate(prices = [100, 1, 200, 2, 300, 3, 400, 4, 500, 5]) == [99, 1, 198, 2, 297, 3, 396, 4, 495, 5]
    assert candidate(prices = [999, 1000, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 980]
    assert candidate(prices = [100, 200, 150, 250, 300, 220, 180, 160, 170]) == [100, 50, 150, 30, 80, 40, 20, 160, 170]
    assert candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    assert candidate(prices = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(prices = [5, 10, 15, 20, 15, 10, 5, 10, 15, 20, 15, 10, 5]) == [0, 0, 0, 5, 5, 5, 0, 0, 0, 5, 5, 5, 5]
    assert candidate(prices = [3, 3, 3, 3, 1, 1, 1, 1, 5, 5, 5, 5]) == [0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 5]
    assert candidate(prices = [5, 15, 25, 10, 20, 5, 30, 25, 40, 10]) == [0, 5, 15, 5, 15, 5, 5, 15, 30, 10]
    assert candidate(prices = [5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 1]
    assert candidate(prices = [8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5]
    assert candidate(prices = [1000, 1000, 1000, 1000, 1000]) == [0, 0, 0, 0, 1000]
    assert candidate(prices = [5, 1, 4, 3, 2, 6, 7, 8, 10, 9]) == [4, 1, 1, 1, 2, 6, 7, 8, 1, 9]
    assert candidate(prices = [8, 4, 6, 2, 3, 5, 7, 1, 9, 10]) == [4, 2, 4, 1, 2, 4, 6, 1, 9, 10]
    assert candidate(prices = [500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1]) == [100, 100, 100, 100, 50, 25, 13, 6, 3, 2, 1]
    assert candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(prices = [250, 200, 150, 100, 50, 100, 150, 200, 250, 300]) == [50, 50, 50, 50, 50, 100, 150, 200, 250, 300]
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(prices = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6]
    assert candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10]) == [0, 9, 0, 9, 0, 9, 1, 10]
    assert candidate(prices = [30, 25, 20, 15, 10, 5, 10, 15, 20, 25]) == [5, 5, 5, 5, 5, 5, 10, 15, 20, 25]
    assert candidate(prices = [4, 3, 2, 1, 2, 3, 4, 5, 6, 7]) == [1, 1, 1, 1, 2, 3, 4, 5, 6, 7]
    assert candidate(prices = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == [1, 1, 1, 1, 0, 1, 2, 3, 4, 5]
    assert candidate(prices = [19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 1]
    assert candidate(prices = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 50]
    assert candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(prices = [2, 2, 2, 2, 2, 1, 1, 1, 1, 1]) == [0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    assert candidate(prices = [5, 10, 5, 10, 5, 10, 5, 10, 5, 10]) == [0, 5, 0, 5, 0, 5, 0, 5, 5, 10]
    assert candidate(prices = [7, 6, 5, 4, 3, 2, 1, 0, 0, 0]) == [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
    assert candidate(prices = [1, 2, 2, 1, 1, 2, 2, 1, 1]) == [0, 0, 1, 0, 0, 0, 1, 0, 1]
    assert candidate(prices = [100, 50, 25, 200, 100, 50, 25, 200]) == [50, 25, 0, 100, 50, 25, 25, 200]
    assert candidate(prices = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8]) == [1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8]
    assert candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3]) == [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 2, 3]
    assert candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
    assert candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    assert candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == [0, 9, 0, 9, 0, 9, 0, 9, 1, 10]
    assert candidate(prices = [3, 2, 3, 2, 3, 2, 3, 2, 3, 2]) == [1, 0, 1, 0, 1, 0, 1, 0, 1, 2]
    assert candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    assert candidate(prices = [1, 3, 2, 2, 1, 4, 3, 2, 1, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]) == [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
    assert candidate(prices = [10, 20, 30, 40, 50, 40, 30, 20, 10, 5]) == [0, 0, 0, 0, 10, 10, 10, 10, 5, 5]
    assert candidate(prices = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10]
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]
    assert candidate(prices = [50, 40, 30, 20, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == [10, 10, 10, 10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
    assert candidate(prices = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]) == [4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4]
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert candidate(prices = [50, 25, 75, 100, 50, 75, 100, 125]) == [25, 25, 25, 50, 50, 75, 100, 125]
    assert candidate(prices = [100, 200, 300, 400, 500, 400, 300, 200, 100]) == [0, 0, 0, 0, 100, 100, 100, 100, 100]


