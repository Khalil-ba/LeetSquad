def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 4]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 4]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 0, 2, 3, 1, 4, 2, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 0, 2, 3, 1, 4, 2, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 1, 4, 5, 2, 9, 7]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 1, 4, 5, 2, 9, 7]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 6, 5, 0, 3]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 6, 5, 0, 3]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 9, 7, 9, 10, 1, 2, 3, 4, 1, 5]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 9, 7, 9, 10, 1, 2, 3, 4, 1, 5]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 8, 3, 8, 2, 6]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 8, 3, 8, 2, 6]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 8, 4, 9]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 8, 4, 9]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [6, 1, 3, 2, 4, 7]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [6, 1, 3, 2, 4, 7]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 1, 5, 3, 6, 4]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 1, 5, 3, 6, 4]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 0, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 0, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 7, 5, 10, 3]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 7, 5, 10, 3]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 9, 2, 8, 4, 9]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 9, 2, 8, 4, 9]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 2, 3, 4, 1, 6, 7, 8, 9, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 2, 3, 4, 1, 6, 7, 8, 9, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 6, 5, 0, 3, 1, 4, 5, 4, 7, 8, 9, 3, 2, 1, 0, 12, 14, 16, 18, 20, 19, 18, 17, 16, 15, 14]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 6, 5, 0, 3, 1, 4, 5, 4, 7, 8, 9, 3, 2, 1, 0, 12, 14, 16, 18, 20, 19, 18, 17, 16, 15, 14]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 0, 0, 3, 1, 4, 0, 2, 1, 2, 0, 1, 3]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 0, 0, 3, 1, 4, 0, 2, 1, 2, 0, 1, 3]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 0, 2, 3, 4, 5, 0, 6, 7, 8, 0, 9]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 0, 2, 3, 4, 5, 0, 6, 7, 8, 0, 9]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 1, 5, 3, 6, 4, 9, 2, 5, 8]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 1, 5, 3, 6, 4, 9, 2, 5, 8]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 50, 200, 10, 150, 80, 120, 20, 180, 100, 140, 50, 250, 200, 300, 150, 350, 300, 400, 250, 450, 400, 500, 350, 550, 500, 600, 450, 650]) == 1310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 50, 200, 10, 150, 80, 120, 20, 180, 100, 140, 50, 250, 200, 300, 150, 350, 300, 400, 250, 450, 400, 500, 350, 550, 500, 600, 450, 650]) == 1310: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 5, 3, 8, 12, 6, 2, 9, 15, 10, 13, 7, 16, 11]) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 5, 3, 8, 12, 6, 2, 9, 15, 10, 13, 7, 16, 11]) == 33: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 1, 1, 2, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 1, 1, 2, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 1, 1, 6, 9, 10, 7, 12, 6, 7, 5, 18, 9]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 1, 1, 6, 9, 10, 7, 12, 6, 7, 5, 18, 9]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 8, 7, 6, 5, 4, 3, 2, 1, 9]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 8, 7, 6, 5, 4, 3, 2, 1, 9]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 0, 2, 5, 0, 6, 1, 8]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 0, 2, 5, 0, 6, 1, 8]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 10, 10, 10, 20, 30, 10, 40, 50, 10, 60, 70, 10, 80, 90, 10]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 10, 10, 10, 20, 30, 10, 40, 50, 10, 60, 70, 10, 80, 90, 10]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 4, 2, 7, 4, 8, 1, 10, 12, 20, 2]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 4, 2, 7, 4, 8, 1, 10, 12, 20, 2]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 5, 1, 3, 1, 7, 1, 9, 1, 11, 1, 13, 1, 15, 1, 17, 1, 19, 1, 21]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 5, 1, 3, 1, 7, 1, 9, 1, 11, 1, 13, 1, 15, 1, 17, 1, 19, 1, 21]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 1, 5, 3, 6, 4, 2, 8]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 1, 5, 3, 6, 4, 2, 8]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 5, 20, 1, 15, 8, 12, 2, 18, 10, 14, 5, 25, 20, 30, 15, 35, 30, 40, 25, 45, 40, 50, 35, 55, 50, 60, 45, 65]) == 131
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 5, 20, 1, 15, 8, 12, 2, 18, 10, 14, 5, 25, 20, 30, 15, 35, 30, 40, 25, 45, 40, 50, 35, 55, 50, 60, 45, 65]) == 131: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 1, 2, 1, 2, 3, 4, 1, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 1, 2, 1, 2, 3, 4, 1, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 0, 2, 3, 4, 5, 0, 6]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 0, 2, 3, 4, 5, 0, 6]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(prices = [6, 1, 3, 2, 4, 7]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [6, 1, 3, 2, 4, 7]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 1, 5, 3, 6, 4, 8, 2, 10, 3, 5]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 1, 5, 3, 6, 4, 8, 2, 10, 3, 5]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 0, 3, 2, 3, 0, 4, 2, 0, 1, 2, 3, 4, 5, 0, 0, 0, 0, 0]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 0, 3, 2, 3, 0, 4, 2, 0, 1, 2, 3, 4, 5, 0, 0, 0, 0, 0]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 5, 0, 1, 8, 0, 3, 4, 0, 5, 2, 3, 8, 9, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 5, 0, 1, 8, 0, 3, 4, 0, 5, 2, 3, 8, 9, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 4, 2, 7, 2, 8, 3, 9, 1, 10, 1, 11, 1, 12, 1, 13]) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 4, 2, 7, 2, 8, 3, 9, 1, 10, 1, 11, 1, 12, 1, 13]) == 34: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 5, 2, 3, 7, 1, 4, 2, 8, 3, 5]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 5, 2, 3, 7, 1, 4, 2, 8, 3, 5]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 5, 0, 2, 1, 2, 0, 2, 1, 0, 2, 3, 4, 5, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 5, 0, 2, 1, 2, 0, 2, 1, 0, 2, 3, 4, 5, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 180, 260, 310, 40, 535, 695, 200, 400, 310, 350, 410, 300, 500, 600, 500, 400, 600, 700, 800, 900, 1000, 500, 1100, 1200, 1300]) == 2455
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 180, 260, 310, 40, 535, 695, 200, 400, 310, 350, 410, 300, 500, 600, 500, 400, 600, 700, 800, 900, 1000, 500, 1100, 1200, 1300]) == 2455: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 2, 5, 4, 6, 9, 1, 3, 2, 8, 1, 7, 6, 3, 8, 9, 10, 5]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 2, 5, 4, 6, 9, 1, 3, 2, 8, 1, 7, 6, 3, 8, 9, 10, 5]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 1, 5, 3, 6, 4, 5, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 1, 5, 3, 6, 4, 5, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 1, 4, 8, 7, 2, 5, 10, 9, 6, 11]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 1, 4, 8, 7, 2, 5, 10, 9, 6, 11]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 1, 5, 3, 6, 4, 1, 5, 3, 6, 4, 1, 5, 3, 6, 4, 1, 5, 3, 6, 4]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 1, 5, 3, 6, 4, 1, 5, 3, 6, 4, 1, 5, 3, 6, 4, 1, 5, 3, 6, 4]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 4, 2, 10, 7, 5, 15, 13, 9, 11]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 4, 2, 10, 7, 5, 15, 13, 9, 11]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 10, 5, 2, 3, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 10, 5, 2, 3, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 58: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 14, 14, 14, 13, 10, 9, 8, 7, 6, 5, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 14, 14, 14, 13, 10, 9, 8, 7, 6, 5, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 90, 80, 50, 25, 20, 10, 5, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 90, 80, 50, 25, 20, 10, 5, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 0, 2, 1, 3, 4, 1, 5, 0, 6, 3]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 0, 2, 1, 3, 4, 1, 5, 0, 6, 3]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 6, 4, 6, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 6, 4, 6, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 3, 5, 0, 1, 8, 0, 3, 4, 0, 5, 2, 3, 8, 9, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 7]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 3, 5, 0, 1, 8, 0, 3, 4, 0, 5, 2, 3, 8, 9, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 7]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 0, 2, 5, 0, 4, 6, 0, 3, 8, 0, 10]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 0, 2, 5, 0, 4, 6, 0, 3, 8, 0, 10]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 4, 2, 7, 2, 4, 1, 6, 1, 5, 2, 7, 2, 4, 1, 6, 1, 5, 2, 7, 2, 4, 1, 6, 1, 5, 2, 7, 2, 4, 1]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 4, 2, 7, 2, 4, 1, 6, 1, 5, 2, 7, 2, 4, 1, 6, 1, 5, 2, 7, 2, 4, 1, 6, 1, 5, 2, 7, 2, 4, 1]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 2, 5, 0, 1, 8, 0, 3, 4, 0, 5, 2, 3, 8, 9, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 2, 5, 0, 1, 8, 0, 3, 4, 0, 5, 2, 3, 8, 9, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 32: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 6, 4, 3, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 6, 4, 3, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 6, 4, 6, 8, 7, 3, 5, 1, 9]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 6, 4, 6, 8, 7, 3, 5, 1, 9]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(prices = [6, 1, 3, 2, 8, 0, 4, 2, 5, 10, 1, 3]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [6, 1, 3, 2, 8, 0, 4, 2, 5, 10, 1, 3]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 1, 4, 5, 2, 9, 7, 10, 3, 12, 8, 15]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 1, 4, 5, 2, 9, 7, 10, 3, 12, 8, 15]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 1, 5, 3, 6, 4, 3, 7, 8, 2, 5, 10, 4]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 1, 5, 3, 6, 4, 3, 7, 8, 2, 5, 10, 4]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 8, 4, 9, 0, 5, 6, 7, 8, 9, 10, 11, 12]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 8, 4, 9, 0, 5, 6, 7, 8, 9, 10, 11, 12]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 1, 2, 8, 4, 9, 5, 6, 3, 10]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 1, 2, 8, 4, 9, 5, 6, 3, 10]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 5, 0, 2, 1, 7, 5, 3, 2, 8]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 5, 0, 2, 1, 7, 5, 3, 2, 8]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 6, 5, 0, 3, 8, 1, 2, 4, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 6, 5, 0, 3, 8, 1, 2, 4, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 6, 5, 0, 3, 4, 7, 8, 0, 5, 2, 3, 8, 9, 1, 2, 3, 4, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 6, 5, 0, 3, 4, 7, 8, 0, 5, 2, 3, 8, 9, 1, 2, 3, 4, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 0, 2, 5, 6, 1, 2, 3, 4, 5, 6]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 0, 2, 5, 6, 1, 2, 3, 4, 5, 6]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 1, 1, 6, 9, 1, 6, 1, 4, 7]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 1, 1, 6, 9, 1, 6, 1, 4, 7]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 1, 1, 6, 9, 10, 3, 1, 3, 9, 5, 5, 5, 4, 5, 5, 6, 6, 6, 8]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 1, 1, 6, 9, 10, 3, 1, 3, 9, 5, 5, 5, 4, 5, 5, 6, 6, 6, 8]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 0, 2, 1, 2, 0, 2, 1, 0, 2, 3, 4, 5, 0, 0, 1, 2, 3, 4]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 0, 2, 1, 2, 0, 2, 1, 0, 2, 3, 4, 5, 0, 0, 1, 2, 3, 4]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 7, 8, 5, 3, 5, 7, 8]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 7, 8, 5, 3, 5, 7, 8]) == 11: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(prices = [1, 2, 4]) == 3
    assert candidate(prices = [1, 2, 3, 0, 2, 3, 1, 4, 2, 5]) == 7
    assert candidate(prices = [2, 1, 4, 5, 2, 9, 7]) == 10
    assert candidate(prices = [1]) == 0
    assert candidate(prices = [3, 2, 6, 5, 0, 3]) == 7
    assert candidate(prices = [3, 2, 1]) == 0
    assert candidate(prices = [8, 9, 7, 9, 10, 1, 2, 3, 4, 1, 5]) == 8
    assert candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 8, 3, 8, 2, 6]) == 10
    assert candidate(prices = [1, 3, 2, 8, 4, 9]) == 8
    assert candidate(prices = [6, 1, 3, 2, 4, 7]) == 6
    assert candidate(prices = [7, 1, 5, 3, 6, 4]) == 5
    assert candidate(prices = [5, 4, 3, 2, 1]) == 0
    assert candidate(prices = [1, 2, 3, 4, 5]) == 4
    assert candidate(prices = [1, 2, 3, 0, 2]) == 3
    assert candidate(prices = [1, 3, 7, 5, 10, 3]) == 9
    assert candidate(prices = [8, 9, 2, 8, 4, 9]) == 7
    assert candidate(prices = [5, 2, 3, 4, 1, 6, 7, 8, 9, 1]) == 9
    assert candidate(prices = [3, 2, 6, 5, 0, 3, 1, 4, 5, 4, 7, 8, 9, 3, 2, 1, 0, 12, 14, 16, 18, 20, 19, 18, 17, 16, 15, 14]) == 33
    assert candidate(prices = [1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]) == 12
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 0, 0, 3, 1, 4, 0, 2, 1, 2, 0, 1, 3]) == 11
    assert candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]) == 12
    assert candidate(prices = [1, 2, 3, 0, 2, 3, 4, 5, 0, 6, 7, 8, 0, 9]) == 21
    assert candidate(prices = [7, 1, 5, 3, 6, 4, 9, 2, 5, 8]) == 12
    assert candidate(prices = [100, 50, 200, 10, 150, 80, 120, 20, 180, 100, 140, 50, 250, 200, 300, 150, 350, 300, 400, 250, 450, 400, 500, 350, 550, 500, 600, 450, 650]) == 1310
    assert candidate(prices = [1, 5, 3, 8, 12, 6, 2, 9, 15, 10, 13, 7, 16, 11]) == 33
    assert candidate(prices = [5, 1, 1, 2, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 8
    assert candidate(prices = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 8
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 19
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 19
    assert candidate(prices = [10, 1, 1, 6, 9, 10, 7, 12, 6, 7, 5, 18, 9]) == 26
    assert candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 27
    assert candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 45
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
    assert candidate(prices = [1, 2, 3, 8, 7, 6, 5, 4, 3, 2, 1, 9]) == 15
    assert candidate(prices = [1, 2, 3, 0, 2, 5, 0, 6, 1, 8]) == 13
    assert candidate(prices = [10, 20, 10, 10, 10, 20, 30, 10, 40, 50, 10, 60, 70, 10, 80, 90, 10]) == 180
    assert candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
    assert candidate(prices = [1, 4, 2, 7, 4, 8, 1, 10, 12, 20, 2]) == 25
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == 10
    assert candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 3
    assert candidate(prices = [1, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 5
    assert candidate(prices = [1, 5, 1, 3, 1, 7, 1, 9, 1, 11, 1, 13, 1, 15, 1, 17, 1, 19, 1, 21]) == 60
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(prices = [7, 1, 5, 3, 6, 4, 2, 8]) == 11
    assert candidate(prices = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]) == 2
    assert candidate(prices = [10, 5, 20, 1, 15, 8, 12, 2, 18, 10, 14, 5, 25, 20, 30, 15, 35, 30, 40, 25, 45, 40, 50, 35, 55, 50, 60, 45, 65]) == 131
    assert candidate(prices = [1, 2, 3, 4, 1, 2, 1, 2, 3, 4, 1, 2]) == 6
    assert candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 14
    assert candidate(prices = [1, 2, 3, 0, 2, 3, 4, 5, 0, 6]) == 11
    assert candidate(prices = [6, 1, 3, 2, 4, 7]) == 6
    assert candidate(prices = [7, 1, 5, 3, 6, 4, 8, 2, 10, 3, 5]) == 13
    assert candidate(prices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 15
    assert candidate(prices = [1, 2, 3, 0, 3, 2, 3, 0, 4, 2, 0, 1, 2, 3, 4, 5, 0, 0, 0, 0, 0]) == 13
    assert candidate(prices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 16
    assert candidate(prices = [1, 2, 5, 0, 1, 8, 0, 3, 4, 0, 5, 2, 3, 8, 9, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 36
    assert candidate(prices = [1, 4, 2, 7, 2, 8, 3, 9, 1, 10, 1, 11, 1, 12, 1, 13]) == 34
    assert candidate(prices = [1, 5, 2, 3, 7, 1, 4, 2, 8, 3, 5]) == 14
    assert candidate(prices = [1, 2, 5, 0, 2, 1, 2, 0, 2, 1, 0, 2, 3, 4, 5, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 21
    assert candidate(prices = [100, 180, 260, 310, 40, 535, 695, 200, 400, 310, 350, 410, 300, 500, 600, 500, 400, 600, 700, 800, 900, 1000, 500, 1100, 1200, 1300]) == 2455
    assert candidate(prices = [5, 2, 5, 4, 6, 9, 1, 3, 2, 8, 1, 7, 6, 3, 8, 9, 10, 5]) == 20
    assert candidate(prices = [1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9]) == 24
    assert candidate(prices = [7, 1, 5, 3, 6, 4, 5, 2]) == 5
    assert candidate(prices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 9
    assert candidate(prices = [3, 1, 4, 8, 7, 2, 5, 10, 9, 6, 11]) == 20
    assert candidate(prices = [7, 1, 5, 3, 6, 4, 1, 5, 3, 6, 4, 1, 5, 3, 6, 4, 1, 5, 3, 6, 4]) == 20
    assert candidate(prices = [1, 4, 2, 10, 7, 5, 15, 13, 9, 11]) == 21
    assert candidate(prices = [10, 20, 10, 5, 2, 3, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 58
    assert candidate(prices = [10, 14, 14, 14, 13, 10, 9, 8, 7, 6, 5, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
    assert candidate(prices = [100, 90, 80, 50, 25, 20, 10, 5, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(prices = [1, 2, 3, 0, 2, 1, 3, 4, 1, 5, 0, 6, 3]) == 11
    assert candidate(prices = [8, 6, 4, 6, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 4
    assert candidate(prices = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 4
    assert candidate(prices = [2, 3, 5, 0, 1, 8, 0, 3, 4, 0, 5, 2, 3, 8, 9, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 7]) == 30
    assert candidate(prices = [1, 2, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 11
    assert candidate(prices = [1, 2, 3, 0, 2, 5, 0, 4, 6, 0, 3, 8, 0, 10]) == 20
    assert candidate(prices = [1, 4, 2, 7, 2, 4, 1, 6, 1, 5, 2, 7, 2, 4, 1, 6, 1, 5, 2, 7, 2, 4, 1, 6, 1, 5, 2, 7, 2, 4, 1]) == 36
    assert candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 0
    assert candidate(prices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 12
    assert candidate(prices = [5, 2, 5, 0, 1, 8, 0, 3, 4, 0, 5, 2, 3, 8, 9, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 32
    assert candidate(prices = [7, 6, 4, 3, 1]) == 0
    assert candidate(prices = [8, 6, 4, 6, 8, 7, 3, 5, 1, 9]) == 12
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
    assert candidate(prices = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]) == 11
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 12
    assert candidate(prices = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5]) == 14
    assert candidate(prices = [6, 1, 3, 2, 8, 0, 4, 2, 5, 10, 1, 3]) == 15
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(prices = [3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert candidate(prices = [2, 1, 4, 5, 2, 9, 7, 10, 3, 12, 8, 15]) == 22
    assert candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 5
    assert candidate(prices = [7, 1, 5, 3, 6, 4, 3, 7, 8, 2, 5, 10, 4]) == 17
    assert candidate(prices = [1, 2, 3, 8, 4, 9, 0, 5, 6, 7, 8, 9, 10, 11, 12]) == 19
    assert candidate(prices = [10, 1, 2, 8, 4, 9, 5, 6, 3, 10]) == 15
    assert candidate(prices = [10, 5, 0, 2, 1, 7, 5, 3, 2, 8]) == 13
    assert candidate(prices = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]) == 5
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 18
    assert candidate(prices = [3, 2, 6, 5, 0, 3, 8, 1, 2, 4, 5]) == 15
    assert candidate(prices = [3, 2, 6, 5, 0, 3, 4, 7, 8, 0, 5, 2, 3, 8, 9, 1, 2, 3, 4, 5]) == 25
    assert candidate(prices = [1, 2, 3, 0, 2, 5, 6, 1, 2, 3, 4, 5, 6]) == 11
    assert candidate(prices = [10, 1, 1, 6, 9, 1, 6, 1, 4, 7]) == 14
    assert candidate(prices = [10, 1, 1, 6, 9, 10, 3, 1, 3, 9, 5, 5, 5, 4, 5, 5, 6, 6, 6, 8]) == 21
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert candidate(prices = [1, 2, 3, 0, 2, 1, 2, 0, 2, 1, 0, 2, 3, 4, 5, 0, 0, 1, 2, 3, 4]) == 14
    assert candidate(prices = [8, 6, 4, 3, 3, 2, 3, 5, 7, 8, 5, 3, 5, 7, 8]) == 11


