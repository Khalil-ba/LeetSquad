def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(heights = [1]) == [0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1]) == [0]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 1, 3, 1, 3, 1, 3]) == [7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 1, 3, 1, 3, 1, 3]) == [7]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [4, 3, 2, 1]) == [0, 1, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [4, 3, 2, 1]) == [0, 1, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 9]) == [11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 9]) == [11]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5]) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5]) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 2, 1]) == [2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 2, 1]) == [2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 1, 2, 1]) == [3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 1, 2, 1]) == [3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 1, 2, 1, 2, 1]) == [4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 1, 2, 1, 2, 1]) == [4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [6, 5, 5, 5, 5]) == [0, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [6, 5, 5, 5, 5]) == [0, 4]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 2, 1]) == [2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 2, 1]) == [2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 5, 5, 5]) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 5, 5, 5]) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 5, 5, 6]) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 5, 5, 6]) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [5, 7, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [5, 7, 10]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 4]) == [3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 4]) == [3]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1]) == [4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1]) == [4]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [4, 2, 3, 1]) == [0, 2, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [4, 2, 3, 1]) == [0, 2, 3]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 5, 5]) == [3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 5, 5]) == [3]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 3, 2, 1]) == [3, 4, 5, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 3, 2, 1]) == [3, 4, 5, 6]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5]) == [14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5]) == [14]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == [5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == [5]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == [15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == [15]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 90, 95, 80, 85, 75, 105, 110, 102, 98]) == [7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 90, 95, 80, 85, 75, 105, 110, 102, 98]) == [7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 8, 7, 8, 9, 10]) == [19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 8, 7, 8, 9, 10]) == [19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 10, 11, 12, 13, 14, 15, 16, 17, 18]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 4, 5, 3, 4, 5, 6, 4, 5, 6, 7, 5, 6]) == [12, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 4, 5, 3, 4, 5, 6, 4, 5, 6, 7, 5, 6]) == [12, 14]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 9, 8, 7, 6, 10, 9, 8, 7, 6]) == [5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 9, 8, 7, 6, 10, 9, 8, 7, 6]) == [5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12]) == [11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12]) == [11]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4]) == [8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4]) == [8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1]) == [18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1]) == [18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 10, 30, 10, 40, 10, 50, 10, 60]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 10, 30, 10, 40, 10, 50, 10, 60]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]) == [5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]) == [5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 30, 25, 20, 15, 10, 5]) == [2, 3, 4, 5, 6, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 30, 25, 20, 15, 10, 5]) == [2, 3, 4, 5, 6, 7]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1000000000, 1000000000, 1000000000, 999999999, 1]) == [2, 3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1000000000, 1000000000, 1000000000, 999999999, 1]) == [2, 3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 11, 10, 12, 10, 13, 10, 14, 10, 15, 10, 16, 10, 17, 10, 18]) == [15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 11, 10, 12, 10, 13, 10, 14, 10, 15, 10, 16, 10, 17, 10, 18]) == [15]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 4, 3, 5, 6, 5, 7, 8]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 4, 3, 5, 6, 5, 7, 8]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 5, 7, 9, 11, 13, 15, 14, 12, 10, 8, 6, 4, 2]) == [7, 8, 9, 10, 11, 12, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 5, 7, 9, 11, 13, 15, 14, 12, 10, 8, 6, 4, 2]) == [7, 8, 9, 10, 11, 12, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 2, 1, 2, 3, 4, 3, 3, 2, 1]) == [6, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 2, 1, 2, 3, 4, 3, 3, 2, 1]) == [6, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == [4, 5, 6, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == [4, 5, 6, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 10, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60, 7, 70, 8, 80, 9, 90, 10, 100]) == [19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 10, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60, 7, 70, 8, 80, 9, 90, 10, 100]) == [19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 2, 3, 4, 5]) == [14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 2, 3, 4, 5]) == [14]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 90, 101, 91, 102, 92, 103, 93, 104, 94]) == [8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 90, 101, 91, 102, 92, 103, 93, 104, 94]) == [8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == [9, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == [9, 14]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 5, 4, 6, 5, 7, 8, 6]) == [8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 5, 4, 6, 5, 7, 8, 6]) == [8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5, 60, 6, 70, 7, 80, 8, 90, 9, 100, 10]) == [18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5, 60, 6, 70, 7, 80, 8, 90, 9, 100, 10]) == [18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]) == [17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]) == [17]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9]) == [0, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9]) == [0, 9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == [19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == [19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 6, 7, 8, 9, 1, 2, 3, 4, 10]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 6, 7, 8, 9, 1, 2, 3, 4, 10]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == [9, 11, 13, 15, 17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == [9, 11, 13, 15, 17]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11]) == [19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11]) == [19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4]) == [8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4]) == [8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == [7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == [7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [80, 70, 60, 50, 40, 30, 20, 10, 90, 80, 70, 60, 50, 40, 30]) == [8, 9, 10, 11, 12, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [80, 70, 60, 50, 40, 30, 20, 10, 90, 80, 70, 60, 50, 40, 30]) == [8, 9, 10, 11, 12, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]) == [11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]) == [11]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [5, 6, 7, 8, 9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [5, 6, 7, 8, 9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == [8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == [8]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]) == [4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]) == [4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [1, 3, 5, 7, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [1, 3, 5, 7, 9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == [19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == [19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 90, 110, 95, 120, 85, 130, 70, 140, 60]) == [8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 90, 110, 95, 120, 85, 130, 70, 140, 60]) == [8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1000000000, 999999999, 1000000000, 999999998, 1000000000, 999999997]) == [4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1000000000, 999999999, 1000000000, 999999998, 1000000000, 999999997]) == [4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [11, 12, 13, 14, 15, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [11, 12, 13, 14, 15, 16]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [7, 14, 4, 14, 13, 2, 6, 13, 10, 5, 12, 3]) == [3, 7, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [7, 14, 4, 14, 13, 2, 6, 13, 10, 5, 12, 3]) == [3, 7, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 20, 30, 25, 35, 20, 40, 30, 50, 40, 60, 50, 70, 60, 80]) == [14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 20, 30, 25, 35, 20, 40, 30, 50, 40, 60, 50, 70, 60, 80]) == [14]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [13, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [13, 14]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [17]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [17]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996]) == [1, 3, 5, 7, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996]) == [1, 3, 5, 7, 9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 3, 2, 3, 4, 5]) == [8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 3, 2, 3, 4, 5]) == [8]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == [11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == [11]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 4, 5, 4, 3, 2, 1]) == [4, 5, 6, 7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 4, 5, 4, 3, 2, 1]) == [4, 5, 6, 7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [20, 19, 20, 18, 21, 17, 22, 16, 23, 15, 24, 14, 25, 13, 26, 12, 27, 11, 28, 10]) == [18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [20, 19, 20, 18, 21, 17, 22, 16, 23, 15, 24, 14, 25, 13, 26, 12, 27, 11, 28, 10]) == [18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [14]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 5, 4, 3, 2, 1, 1, 1, 1]) == [3, 4, 5, 6, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 5, 4, 3, 2, 1, 1, 1, 1]) == [3, 4, 5, 6, 10]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 5, 3, 4, 2, 3, 4, 5, 6, 1]) == [8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 5, 3, 4, 2, 3, 4, 5, 6, 1]) == [8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 10]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 10]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == [14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == [14]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [8, 8, 8, 8, 8, 9, 8, 8, 8, 8, 8, 8, 8]) == [5, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [8, 8, 8, 8, 8, 9, 8, 8, 8, 8, 8, 8, 8]) == [5, 12]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == [11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == [11]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 1, 2, 10, 3, 10, 4, 10, 5, 10]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 1, 2, 10, 3, 10, 4, 10, 5, 10]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == [19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == [19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [5, 10, 5, 15, 5, 20, 5, 25, 5, 30]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [5, 10, 5, 15, 5, 20, 5, 25, 5, 30]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1]) == [5, 6, 7, 8, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1]) == [5, 6, 7, 8, 14]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 4, 5, 4, 3, 2, 1, 6]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 4, 5, 4, 3, 2, 1, 6]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1]) == [17, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1]) == [17, 18]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995]) == [0, 1, 2, 3, 4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995]) == [0, 1, 2, 3, 4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 4, 6, 5, 8, 7, 10, 9]) == [8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 4, 6, 5, 8, 7, 10, 9]) == [8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == [8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == [8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 90, 95, 90, 100, 85, 80, 110, 105]) == [7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 90, 95, 90, 100, 85, 80, 110, 105]) == [7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11]) == [20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11]) == [20]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == [19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == [19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == [0, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == [0, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 3, 2, 4, 5, 3, 2, 4, 5, 3, 2, 4, 5, 3, 2, 4, 5, 3, 2, 1]) == [16, 17, 18, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 3, 2, 4, 5, 3, 2, 4, 5, 3, 2, 4, 5, 3, 2, 4, 5, 3, 2, 1]) == [16, 17, 18, 19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == [15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == [15]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 5, 3, 9, 7, 11, 8, 12, 6, 13]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 5, 3, 9, 7, 11, 8, 12, 6, 13]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1]) == [8, 9, 10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1]) == [8, 9, 10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [9]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2]) == [15, 16, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2]) == [15, 16, 19]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [19, 20, 21, 22, 23, 24, 25, 26, 27, 28]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [18]: {e}')
    
    total += 1
    try:
        result = candidate(heights = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(heights = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [8, 9]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(heights = [1]) == [0]
    assert candidate(heights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(heights = [1, 3, 1, 3, 1, 3, 1, 3]) == [7]
    assert candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(heights = [4, 3, 2, 1]) == [0, 1, 2, 3]
    assert candidate(heights = [1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 8, 9]) == [11]
    assert candidate(heights = [1, 2, 3, 4, 5]) == [4]
    assert candidate(heights = [1, 2, 3, 2, 1]) == [2, 3, 4]
    assert candidate(heights = [1, 2, 1, 2, 1]) == [3, 4]
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [9]
    assert candidate(heights = [2, 1, 2, 1, 2, 1]) == [4, 5]
    assert candidate(heights = [6, 5, 5, 5, 5]) == [0, 4]
    assert candidate(heights = [1, 2, 2, 1]) == [2, 3]
    assert candidate(heights = [5, 5, 5, 5, 5]) == [4]
    assert candidate(heights = [5, 5, 5, 5, 6]) == [4]
    assert candidate(heights = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [5, 7, 10]
    assert candidate(heights = [1, 3, 2, 4]) == [3]
    assert candidate(heights = [1, 1, 1, 1, 1]) == [4]
    assert candidate(heights = [4, 2, 3, 1]) == [0, 2, 3]
    assert candidate(heights = [5, 5, 5, 5]) == [3]
    assert candidate(heights = [5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4]
    assert candidate(heights = [1, 2, 3, 4, 3, 2, 1]) == [3, 4, 5, 6]
    assert candidate(heights = [5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5]) == [14]
    assert candidate(heights = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == [9]
    assert candidate(heights = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == [5]
    assert candidate(heights = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10]) == [15]
    assert candidate(heights = [100, 90, 95, 80, 85, 75, 105, 110, 102, 98]) == [7, 8, 9]
    assert candidate(heights = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 5, 6, 7, 8, 7, 8, 9, 10]) == [19]
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [19]
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    assert candidate(heights = [1, 3, 2, 4, 5, 3, 4, 5, 6, 4, 5, 6, 7, 5, 6]) == [12, 14]
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [19]
    assert candidate(heights = [10, 9, 8, 7, 6, 10, 9, 8, 7, 6]) == [5, 6, 7, 8, 9]
    assert candidate(heights = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11, 12]) == [11]
    assert candidate(heights = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == [9]
    assert candidate(heights = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert candidate(heights = [1, 2, 3, 2, 1, 2, 3, 4, 5, 4]) == [8, 9]
    assert candidate(heights = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 1]) == [18, 19]
    assert candidate(heights = [10, 20, 10, 30, 10, 40, 10, 50, 10, 60]) == [9]
    assert candidate(heights = [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]) == [5, 6, 7, 8, 9]
    assert candidate(heights = [10, 20, 30, 25, 20, 15, 10, 5]) == [2, 3, 4, 5, 6, 7]
    assert candidate(heights = [1000000000, 1000000000, 1000000000, 999999999, 1]) == [2, 3, 4]
    assert candidate(heights = [10, 11, 10, 12, 10, 13, 10, 14, 10, 15, 10, 16, 10, 17, 10, 18]) == [15]
    assert candidate(heights = [1, 3, 2, 4, 3, 5, 6, 5, 7, 8]) == [9]
    assert candidate(heights = [1, 3, 5, 7, 9, 11, 13, 15, 14, 12, 10, 8, 6, 4, 2]) == [7, 8, 9, 10, 11, 12, 13, 14]
    assert candidate(heights = [1, 2, 2, 1, 2, 3, 4, 3, 3, 2, 1]) == [6, 8, 9, 10]
    assert candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1]) == [4, 5, 6, 7, 8]
    assert candidate(heights = [1, 10, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60, 7, 70, 8, 80, 9, 90, 10, 100]) == [19]
    assert candidate(heights = [1, 2, 3, 4, 3, 2, 3, 4, 5, 4, 3, 2, 3, 4, 5]) == [14]
    assert candidate(heights = [100, 90, 101, 91, 102, 92, 103, 93, 104, 94]) == [8, 9]
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == [9, 14]
    assert candidate(heights = [1, 3, 2, 5, 4, 6, 5, 7, 8, 6]) == [8, 9]
    assert candidate(heights = [10, 1, 20, 2, 30, 3, 40, 4, 50, 5, 60, 6, 70, 7, 80, 8, 90, 9, 100, 10]) == [18, 19]
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [19]
    assert candidate(heights = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10]) == [17]
    assert candidate(heights = [10, 9, 8, 7, 6, 5, 6, 7, 8, 9]) == [0, 9]
    assert candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(heights = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == [19]
    assert candidate(heights = [5, 6, 7, 8, 9, 1, 2, 3, 4, 10]) == [9]
    assert candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]) == [9, 11, 13, 15, 17]
    assert candidate(heights = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11]) == [19]
    assert candidate(heights = [1, 2, 3, 2, 3, 4, 3, 4, 5, 4]) == [8, 9]
    assert candidate(heights = [1, 2, 3, 2, 1, 2, 3, 4, 3, 2, 1]) == [7, 8, 9, 10]
    assert candidate(heights = [80, 70, 60, 50, 40, 30, 20, 10, 90, 80, 70, 60, 50, 40, 30]) == [8, 9, 10, 11, 12, 13, 14]
    assert candidate(heights = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]) == [11]
    assert candidate(heights = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]) == [9]
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [5, 6, 7, 8, 9, 10]
    assert candidate(heights = [5, 4, 3, 2, 1, 2, 3, 4, 5]) == [8]
    assert candidate(heights = [2, 4, 6, 8, 10, 9, 7, 5, 3, 1]) == [4, 5, 6, 7, 8, 9]
    assert candidate(heights = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert candidate(heights = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == [9]
    assert candidate(heights = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == [1, 3, 5, 7, 9]
    assert candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == [19]
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [19]
    assert candidate(heights = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    assert candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == [19]
    assert candidate(heights = [100, 90, 110, 95, 120, 85, 130, 70, 140, 60]) == [8, 9]
    assert candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == [19]
    assert candidate(heights = [1000000000, 999999999, 1000000000, 999999998, 1000000000, 999999997]) == [4, 5]
    assert candidate(heights = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [9]
    assert candidate(heights = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]) == [11, 12, 13, 14, 15, 16]
    assert candidate(heights = [7, 14, 4, 14, 13, 2, 6, 13, 10, 5, 12, 3]) == [3, 7, 10, 11]
    assert candidate(heights = [10, 20, 30, 25, 35, 20, 40, 30, 50, 40, 60, 50, 70, 60, 80]) == [14]
    assert candidate(heights = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [13, 14]
    assert candidate(heights = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == [17]
    assert candidate(heights = [1, 1000, 2, 999, 3, 998, 4, 997, 5, 996]) == [1, 3, 5, 7, 9]
    assert candidate(heights = [1, 2, 3, 4, 3, 2, 3, 4, 5]) == [8]
    assert candidate(heights = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6, 5, 7]) == [11]
    assert candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == [9]
    assert candidate(heights = [1, 3, 2, 4, 5, 4, 3, 2, 1]) == [4, 5, 6, 7, 8]
    assert candidate(heights = [20, 19, 20, 18, 21, 17, 22, 16, 23, 15, 24, 14, 25, 13, 26, 12, 27, 11, 28, 10]) == [18, 19]
    assert candidate(heights = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == [9]
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [14]
    assert candidate(heights = [1, 2, 3, 5, 4, 3, 2, 1, 1, 1, 1]) == [3, 4, 5, 6, 10]
    assert candidate(heights = [1, 5, 3, 4, 2, 3, 4, 5, 6, 1]) == [8, 9]
    assert candidate(heights = [1, 2, 3, 4, 5, 4, 3, 2, 1, 10]) == [9]
    assert candidate(heights = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == [14]
    assert candidate(heights = [8, 8, 8, 8, 8, 9, 8, 8, 8, 8, 8, 8, 8]) == [5, 12]
    assert candidate(heights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == [19]
    assert candidate(heights = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]) == [9]
    assert candidate(heights = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == [11]
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert candidate(heights = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == [19]
    assert candidate(heights = [10, 1, 2, 10, 3, 10, 4, 10, 5, 10]) == [9]
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == [19]
    assert candidate(heights = [5, 10, 5, 15, 5, 20, 5, 25, 5, 30]) == [9]
    assert candidate(heights = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1]) == [5, 6, 7, 8, 14]
    assert candidate(heights = [1, 3, 2, 4, 5, 4, 3, 2, 1, 6]) == [9]
    assert candidate(heights = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 1, 7, 1, 8, 1, 9, 1, 10, 1]) == [17, 18]
    assert candidate(heights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]) == [9]
    assert candidate(heights = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995]) == [0, 1, 2, 3, 4, 5]
    assert candidate(heights = [1, 3, 2, 4, 6, 5, 8, 7, 10, 9]) == [8, 9]
    assert candidate(heights = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [19]
    assert candidate(heights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 1]) == [8, 9]
    assert candidate(heights = [100, 90, 95, 90, 100, 85, 80, 110, 105]) == [7, 8]
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 11]) == [20]
    assert candidate(heights = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == [19]
    assert candidate(heights = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == [0, 18, 19]
    assert candidate(heights = [1, 3, 2, 4, 5, 3, 2, 4, 5, 3, 2, 4, 5, 3, 2, 4, 5, 3, 2, 1]) == [16, 17, 18, 19]
    assert candidate(heights = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4]) == [15]
    assert candidate(heights = [1, 5, 3, 9, 7, 11, 8, 12, 6, 13]) == [9]
    assert candidate(heights = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    assert candidate(heights = [1, 2, 3, 2, 1, 3, 2, 1, 4, 3, 2, 1]) == [8, 9, 10, 11]
    assert candidate(heights = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [9]
    assert candidate(heights = [1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2]) == [15, 16, 19]
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    assert candidate(heights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == [18]
    assert candidate(heights = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == [8, 9]


