def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(cost = [999, 999, 999, 999]) == 1998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [999, 999, 999, 999]) == 1998: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 2, 3, 4, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 2, 3, 4, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(cost = [0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(cost = [999, 999, 999, 999, 999, 999]) == 2997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [999, 999, 999, 999, 999, 999]) == 2997: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 2, 3, 4, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 2, 3, 4, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(cost = [10, 15, 20, 25, 30]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [10, 15, 20, 25, 30]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(cost = [10, 15]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [10, 15]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(cost = [10, 20, 10, 5]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [10, 20, 10, 5]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(cost = [10, 5, 20, 25, 30, 35, 40]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [10, 5, 20, 25, 30, 35, 40]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(cost = [10, 20, 15, 20, 30]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [10, 20, 15, 20, 30]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(cost = [10, 15]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [10, 15]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(cost = [5, 8, 6, 3, 4, 2, 8, 5, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [5, 8, 6, 3, 4, 2, 8, 5, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(cost = [999, 999]) == 999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [999, 999]) == 999: {e}')
    
    total += 1
    try:
        result = candidate(cost = [10, 15, 20]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [10, 15, 20]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(cost = [10, 15, 20, 10, 15, 20]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [10, 15, 20, 10, 15, 20]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 100, 100, 1]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 100, 100, 1]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(cost = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 900: {e}')
    
    total += 1
    try:
        result = candidate(cost = [10, 15, 20, 30, 40, 50, 60, 70, 80, 90]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [10, 15, 20, 30, 40, 50, 60, 70, 80, 90]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(cost = [3, 5, 2, 1, 8, 9, 3, 5, 6, 2, 1, 4, 7, 3, 2, 8, 6, 4, 1, 7]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [3, 5, 2, 1, 8, 9, 3, 5, 6, 2, 1, 4, 7, 3, 2, 8, 6, 4, 1, 7]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(cost = [50, 10, 20, 100, 30, 40, 10, 20, 30, 40]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [50, 10, 20, 100, 30, 40, 10, 20, 30, 40]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(cost = [3, 2, 4, 3, 2, 5, 1, 2, 4, 3, 2, 5, 1, 2, 4]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [3, 2, 4, 3, 2, 5, 1, 2, 4, 3, 2, 5, 1, 2, 4]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(cost = [5, 8, 3, 12, 2, 7, 6, 10, 1, 4, 9, 11, 13, 14, 15]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [5, 8, 3, 12, 2, 7, 6, 10, 1, 4, 9, 11, 13, 14, 15]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 100, 2, 100, 3, 100, 4, 100, 5, 100, 6, 100, 7, 100, 8]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 100, 2, 100, 3, 100, 4, 100, 5, 100, 6, 100, 7, 100, 8]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(cost = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(cost = [5, 8, 2, 3, 7, 1, 4, 6, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [5, 8, 2, 3, 7, 1, 4, 6, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 92: {e}')
    
    total += 1
    try:
        result = candidate(cost = [50, 10, 5, 100, 20, 15, 10, 5, 20, 10, 5, 100, 20, 15, 10, 5, 20, 10, 5, 100, 20, 15, 10, 5, 20]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [50, 10, 5, 100, 20, 15, 10, 5, 20, 10, 5, 100, 20, 15, 10, 5, 20, 10, 5, 100, 20, 15, 10, 5, 20]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(cost = [10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]) == 495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]) == 495: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999]) == 8992
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999]) == 8992: {e}')
    
    total += 1
    try:
        result = candidate(cost = [3, 2, 10, 2, 3, 5, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 52
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [3, 2, 10, 2, 3, 5, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 52: {e}')
    
    total += 1
    try:
        result = candidate(cost = [999, 0, 999, 0, 999, 0, 999, 0, 999, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [999, 0, 999, 0, 999, 0, 999, 0, 999, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(cost = [999, 999, 1, 999, 999, 2, 999, 999, 3, 999]) == 3001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [999, 999, 1, 999, 999, 2, 999, 999, 3, 999]) == 3001: {e}')
    
    total += 1
    try:
        result = candidate(cost = [999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(cost = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(cost = [5, 8, 10, 2, 9, 1, 3, 7, 4, 6, 11, 12]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [5, 8, 10, 2, 9, 1, 3, 7, 4, 6, 11, 12]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(cost = [999, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0]) == 999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [999, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0]) == 999: {e}')
    
    total += 1
    try:
        result = candidate(cost = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 475
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 475: {e}')
    
    total += 1
    try:
        result = candidate(cost = [5, 8, 3, 7, 2, 8, 3, 7, 2, 8, 3, 7, 2, 8, 3, 7, 2]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [5, 8, 3, 7, 2, 8, 3, 7, 2, 8, 3, 7, 2, 8, 3, 7, 2]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 156: {e}')
    
    total += 1
    try:
        result = candidate(cost = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(cost = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 5600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 5600: {e}')
    
    total += 1
    try:
        result = candidate(cost = [30, 5, 20, 10, 25, 15, 40, 35, 50, 45, 60, 55, 70, 65, 80, 75]) == 305
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [30, 5, 20, 10, 25, 15, 40, 35, 50, 45, 60, 55, 70, 65, 80, 75]) == 305: {e}')
    
    total += 1
    try:
        result = candidate(cost = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 100, 100, 1, 100, 100, 1, 100, 100, 1]) == 302
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 100, 100, 1, 100, 100, 1, 100, 100, 1]) == 302: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(cost = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]) == 315
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]) == 315: {e}')
    
    total += 1
    try:
        result = candidate(cost = [5, 3, 8, 6, 7, 2, 4, 9, 1, 10]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [5, 3, 8, 6, 7, 2, 4, 9, 1, 10]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(cost = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(cost = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == 4970
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == 4970: {e}')
    
    total += 1
    try:
        result = candidate(cost = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999]) == 75924
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999]) == 75924: {e}')
    
    total += 1
    try:
        result = candidate(cost = [50, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 570
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [50, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 570: {e}')
    
    total += 1
    try:
        result = candidate(cost = [5, 2, 7, 4, 9, 6, 11, 8, 13, 10, 15, 12, 17, 14, 19]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [5, 2, 7, 4, 9, 6, 11, 8, 13, 10, 15, 12, 17, 14, 19]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(cost = [999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(cost = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(cost = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 9890
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 9890: {e}')
    
    total += 1
    try:
        result = candidate(cost = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1, 2, 3, 4, 5]) == 2507
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1, 2, 3, 4, 5]) == 2507: {e}')
    
    total += 1
    try:
        result = candidate(cost = [999, 999, 0, 0, 999, 999, 0, 0, 999, 999, 0, 0]) == 2997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [999, 999, 0, 0, 999, 999, 0, 0, 999, 999, 0, 0]) == 2997: {e}')
    
    total += 1
    try:
        result = candidate(cost = [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(cost = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(cost = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 560: {e}')
    
    total += 1
    try:
        result = candidate(cost = [400, 5, 3, 10, 1, 1, 1, 1, 1, 1, 1, 1]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [400, 5, 3, 10, 1, 1, 1, 1, 1, 1, 1, 1]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(cost = [20, 1, 3, 2, 4, 2, 5, 3, 6, 4, 7, 5, 8, 6, 9, 7, 10]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [20, 1, 3, 2, 4, 2, 5, 3, 6, 4, 7, 5, 8, 6, 9, 7, 10]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 2500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 2500: {e}')
    
    total += 1
    try:
        result = candidate(cost = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1, 1, 1, 1, 1]) == 2503
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1, 1, 1, 1, 1]) == 2503: {e}')
    
    total += 1
    try:
        result = candidate(cost = [10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20]) == 760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20]) == 760: {e}')
    
    total += 1
    try:
        result = candidate(cost = [999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(cost = [20, 1, 5, 10, 1, 1, 5, 10, 1, 1, 5, 10, 1, 1, 5, 10, 1, 1, 5, 10]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [20, 1, 5, 10, 1, 1, 5, 10, 1, 1, 5, 10, 1, 1, 5, 10, 1, 1, 5, 10]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(cost = [10, 15, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [10, 15, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(cost = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(cost = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(cost = [5, 8, 2, 3, 6, 1, 4, 7, 9, 10]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [5, 8, 2, 3, 6, 1, 4, 7, 9, 10]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(cost = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(cost = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 495
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 495: {e}')
    
    total += 1
    try:
        result = candidate(cost = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(cost = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(cost = [2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4]) == 165
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4]) == 165: {e}')
    
    total += 1
    try:
        result = candidate(cost = [10, 20, 30, 40, 50, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [10, 20, 30, 40, 50, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(cost = [100, 150, 100, 150, 100, 150, 100, 150, 100, 150]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [100, 150, 100, 150, 100, 150, 100, 150, 100, 150]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 225: {e}')
    
    total += 1
    try:
        result = candidate(cost = [3, 2, 1, 5, 4, 1, 3, 2, 1, 5, 4, 1, 3, 2, 1, 5, 4, 1]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [3, 2, 1, 5, 4, 1, 3, 2, 1, 5, 4, 1, 3, 2, 1, 5, 4, 1]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(cost = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(cost = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 156
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 156: {e}')
    
    total += 1
    try:
        result = candidate(cost = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10]) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10]) == 130: {e}')
    
    total += 1
    try:
        result = candidate(cost = [100, 200, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 106
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [100, 200, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 106: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(cost = [100, 50, 25, 12, 6, 3, 1, 0, 0, 1, 3, 6, 12, 25, 50, 100, 150, 200, 250, 300]) == 530
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [100, 50, 25, 12, 6, 3, 1, 0, 0, 1, 3, 6, 12, 25, 50, 100, 150, 200, 250, 300]) == 530: {e}')
    
    total += 1
    try:
        result = candidate(cost = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(cost = [4, 2, 6, 7, 8, 1, 3, 5, 10, 2, 6, 7, 8, 1, 3, 5]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [4, 2, 6, 7, 8, 1, 3, 5, 10, 2, 6, 7, 8, 1, 3, 5]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(cost = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]) == 832039
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]) == 832039: {e}')
    
    total += 1
    try:
        result = candidate(cost = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 2150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 2150: {e}')
    
    total += 1
    try:
        result = candidate(cost = [999, 999, 999, 999, 999, 0, 0, 0, 0, 0]) == 1998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [999, 999, 999, 999, 999, 0, 0, 0, 0, 0]) == 1998: {e}')
    
    total += 1
    try:
        result = candidate(cost = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(cost = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(cost = [999, 999, 999, 999]) == 1998
    assert candidate(cost = [1, 2, 3, 4, 5]) == 6
    assert candidate(cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    assert candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 25
    assert candidate(cost = [0, 0, 0, 0]) == 0
    assert candidate(cost = [1, 2]) == 1
    assert candidate(cost = [999, 999, 999, 999, 999, 999]) == 2997
    assert candidate(cost = [1, 2, 3, 4, 5]) == 6
    assert candidate(cost = [10, 15, 20, 25, 30]) == 40
    assert candidate(cost = [10, 15]) == 10
    assert candidate(cost = [10, 20, 10, 5]) == 20
    assert candidate(cost = [10, 5, 20, 25, 30, 35, 40]) == 65
    assert candidate(cost = [10, 20, 15, 20, 30]) == 40
    assert candidate(cost = [10, 15]) == 10
    assert candidate(cost = [5, 8, 6, 3, 4, 2, 8, 5, 1]) == 18
    assert candidate(cost = [999, 999]) == 999
    assert candidate(cost = [10, 15, 20]) == 15
    assert candidate(cost = [10, 15, 20, 10, 15, 20]) == 40
    assert candidate(cost = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5
    assert candidate(cost = [1, 100, 100, 1]) == 101
    assert candidate(cost = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81]) == 900
    assert candidate(cost = [10, 15, 20, 30, 40, 50, 60, 70, 80, 90]) == 210
    assert candidate(cost = [3, 5, 2, 1, 8, 9, 3, 5, 6, 2, 1, 4, 7, 3, 2, 8, 6, 4, 1, 7]) == 38
    assert candidate(cost = [50, 10, 20, 100, 30, 40, 10, 20, 30, 40]) == 100
    assert candidate(cost = [3, 2, 4, 3, 2, 5, 1, 2, 4, 3, 2, 5, 1, 2, 4]) == 17
    assert candidate(cost = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 13
    assert candidate(cost = [5, 8, 3, 12, 2, 7, 6, 10, 1, 4, 9, 11, 13, 14, 15]) == 46
    assert candidate(cost = [1, 100, 2, 100, 3, 100, 4, 100, 5, 100, 6, 100, 7, 100, 8]) == 36
    assert candidate(cost = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]) == 450
    assert candidate(cost = [1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2]) == 13
    assert candidate(cost = [5, 8, 2, 3, 7, 1, 4, 6, 9, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 92
    assert candidate(cost = [50, 10, 5, 100, 20, 15, 10, 5, 20, 10, 5, 100, 20, 15, 10, 5, 20, 10, 5, 100, 20, 15, 10, 5, 20]) == 150
    assert candidate(cost = [10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]) == 495
    assert candidate(cost = [1, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999]) == 8992
    assert candidate(cost = [3, 2, 10, 2, 3, 5, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 52
    assert candidate(cost = [999, 0, 999, 0, 999, 0, 999, 0, 999, 0]) == 0
    assert candidate(cost = [999, 999, 1, 999, 999, 2, 999, 999, 3, 999]) == 3001
    assert candidate(cost = [999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999]) == 0
    assert candidate(cost = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 12
    assert candidate(cost = [5, 8, 10, 2, 9, 1, 3, 7, 4, 6, 11, 12]) == 29
    assert candidate(cost = [999, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0]) == 999
    assert candidate(cost = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]) == 475
    assert candidate(cost = [5, 8, 3, 7, 2, 8, 3, 7, 2, 8, 3, 7, 2, 8, 3, 7, 2]) == 25
    assert candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) == 156
    assert candidate(cost = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 125
    assert candidate(cost = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 5600
    assert candidate(cost = [30, 5, 20, 10, 25, 15, 40, 35, 50, 45, 60, 55, 70, 65, 80, 75]) == 305
    assert candidate(cost = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 60
    assert candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 50
    assert candidate(cost = [1, 100, 100, 1, 100, 100, 1, 100, 100, 1]) == 302
    assert candidate(cost = [1, 100, 2, 99, 3, 98, 4, 97, 5, 96]) == 15
    assert candidate(cost = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]) == 315
    assert candidate(cost = [5, 3, 8, 6, 7, 2, 4, 9, 1, 10]) == 16
    assert candidate(cost = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]) == 150
    assert candidate(cost = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990]) == 4970
    assert candidate(cost = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999, 999]) == 75924
    assert candidate(cost = [50, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 570
    assert candidate(cost = [5, 2, 7, 4, 9, 6, 11, 8, 13, 10, 15, 12, 17, 14, 19]) == 56
    assert candidate(cost = [999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0]) == 0
    assert candidate(cost = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 100
    assert candidate(cost = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980]) == 9890
    assert candidate(cost = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1, 2, 3, 4, 5]) == 2507
    assert candidate(cost = [999, 999, 0, 0, 999, 999, 0, 0, 999, 999, 0, 0]) == 2997
    assert candidate(cost = [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(cost = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 56
    assert candidate(cost = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 560
    assert candidate(cost = [400, 5, 3, 10, 1, 1, 1, 1, 1, 1, 1, 1]) == 12
    assert candidate(cost = [20, 1, 3, 2, 4, 2, 5, 3, 6, 4, 7, 5, 8, 6, 9, 7, 10]) == 30
    assert candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 2500
    assert candidate(cost = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1, 1, 1, 1, 1]) == 2503
    assert candidate(cost = [10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20]) == 760
    assert candidate(cost = [999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0, 999, 0]) == 0
    assert candidate(cost = [20, 1, 5, 10, 1, 1, 5, 10, 1, 1, 5, 10, 1, 1, 5, 10, 1, 1, 5, 10]) == 30
    assert candidate(cost = [1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000]) == 5
    assert candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 100
    assert candidate(cost = [10, 15, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 36
    assert candidate(cost = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 7
    assert candidate(cost = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1]) == 10
    assert candidate(cost = [5, 8, 2, 3, 6, 1, 4, 7, 9, 10]) == 24
    assert candidate(cost = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]) == 0
    assert candidate(cost = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == 495
    assert candidate(cost = [999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999]) == 12
    assert candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 56
    assert candidate(cost = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 75
    assert candidate(cost = [2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4, 3, 2, 1, 4, 5, 6, 3, 2, 5, 4, 3, 1, 2, 4]) == 165
    assert candidate(cost = [10, 20, 30, 40, 50, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 65
    assert candidate(cost = [100, 150, 100, 150, 100, 150, 100, 150, 100, 150]) == 500
    assert candidate(cost = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 225
    assert candidate(cost = [3, 2, 1, 5, 4, 1, 3, 2, 1, 5, 4, 1, 3, 2, 1, 5, 4, 1]) == 23
    assert candidate(cost = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 50
    assert candidate(cost = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 156
    assert candidate(cost = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10]) == 130
    assert candidate(cost = [100, 200, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 106
    assert candidate(cost = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 14
    assert candidate(cost = [100, 50, 25, 12, 6, 3, 1, 0, 0, 1, 3, 6, 12, 25, 50, 100, 150, 200, 250, 300]) == 530
    assert candidate(cost = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
    assert candidate(cost = [4, 2, 6, 7, 8, 1, 3, 5, 10, 2, 6, 7, 8, 1, 3, 5]) == 28
    assert candidate(cost = [1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999, 1, 999]) == 10
    assert candidate(cost = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]) == 832039
    assert candidate(cost = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 2150
    assert candidate(cost = [999, 999, 999, 999, 999, 0, 0, 0, 0, 0]) == 1998
    assert candidate(cost = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0


