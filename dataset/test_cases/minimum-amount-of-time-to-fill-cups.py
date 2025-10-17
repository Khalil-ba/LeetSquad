def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(amount = [33, 33, 34]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [33, 33, 34]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(amount = [99, 1, 1]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [99, 1, 1]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(amount = [7, 7, 7]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [7, 7, 7]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(amount = [10, 10, 10]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [10, 10, 10]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 2, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 2, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(amount = [100, 0, 0]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [100, 0, 0]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [100, 100, 100]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [100, 100, 100]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(amount = [0, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [0, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 4, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 4, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(amount = [5, 0, 0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [5, 0, 0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(amount = [99, 99, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [99, 99, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [0, 50, 50]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [0, 50, 50]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [5, 4, 4]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [5, 4, 4]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(amount = [98, 1, 1]) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [98, 1, 1]) == 98: {e}')
    
    total += 1
    try:
        result = candidate(amount = [25, 0, 75]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [25, 0, 75]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(amount = [42, 42, 41]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [42, 42, 41]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(amount = [60, 20, 20]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [60, 20, 20]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(amount = [10, 50, 25]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [10, 50, 25]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [49, 49, 49]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [49, 49, 49]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 1, 0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 1, 0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(amount = [80, 10, 10]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [80, 10, 10]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 10, 10]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 10, 10]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 1, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 1, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [10, 90, 0]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [10, 90, 0]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(amount = [10, 80, 10]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [10, 80, 10]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(amount = [0, 0, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [0, 0, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [80, 10, 10]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [80, 10, 10]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(amount = [33, 33, 34]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [33, 33, 34]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [70, 70, 60]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [70, 70, 60]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [50, 25, 25]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [50, 25, 25]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [29, 29, 42]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [29, 29, 42]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [50, 50, 49]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [50, 50, 49]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(amount = [99, 2, 99]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [99, 2, 99]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [50, 49, 51]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [50, 49, 51]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(amount = [100, 1, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [100, 1, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [80, 70, 60]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [80, 70, 60]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(amount = [100, 50, 25]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [100, 50, 25]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 0, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 0, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(amount = [40, 30, 20]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [40, 30, 20]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 2, 97]) == 97
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 2, 97]) == 97: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(amount = [49, 50, 1]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [49, 50, 1]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [30, 20, 10]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [30, 20, 10]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(amount = [100, 10, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [100, 10, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [2, 99, 99]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [2, 99, 99]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 98, 1]) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 98, 1]) == 98: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 0, 99]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 0, 99]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(amount = [80, 15, 5]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [80, 15, 5]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(amount = [45, 55, 0]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [45, 55, 0]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(amount = [100, 1, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [100, 1, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [50, 50, 1]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [50, 50, 1]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(amount = [25, 25, 25]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [25, 25, 25]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(amount = [42, 29, 29]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [42, 29, 29]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [100, 50, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [100, 50, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 90, 10]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 90, 10]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(amount = [0, 75, 25]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [0, 75, 25]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(amount = [55, 45, 5]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [55, 45, 5]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(amount = [10, 1, 90]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [10, 1, 90]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(amount = [100, 10, 0]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [100, 10, 0]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [80, 10, 1]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [80, 10, 1]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(amount = [48, 48, 48]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [48, 48, 48]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(amount = [80, 50, 30]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [80, 50, 30]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(amount = [90, 90, 1]) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [90, 90, 1]) == 91: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 50, 50]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 50, 50]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(amount = [55, 0, 45]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [55, 0, 45]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(amount = [49, 2, 49]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [49, 2, 49]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [45, 67, 23]) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [45, 67, 23]) == 68: {e}')
    
    total += 1
    try:
        result = candidate(amount = [20, 20, 60]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [20, 20, 60]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(amount = [100, 100, 99]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [100, 100, 99]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(amount = [10, 10, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [10, 10, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [50, 100, 50]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [50, 100, 50]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [10, 15, 20]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [10, 15, 20]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(amount = [0, 100, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [0, 100, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [60, 40, 20]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [60, 40, 20]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(amount = [0, 100, 0]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [0, 100, 0]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [50, 51, 50]) == 76
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [50, 51, 50]) == 76: {e}')
    
    total += 1
    try:
        result = candidate(amount = [33, 33, 33]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [33, 33, 33]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [23, 47, 29]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [23, 47, 29]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [51, 51, 51]) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [51, 51, 51]) == 77: {e}')
    
    total += 1
    try:
        result = candidate(amount = [50, 1, 50]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [50, 1, 50]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(amount = [25, 10, 50]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [25, 10, 50]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [55, 55, 45]) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [55, 55, 45]) == 78: {e}')
    
    total += 1
    try:
        result = candidate(amount = [0, 100, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [0, 100, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [90, 10, 1]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [90, 10, 1]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(amount = [33, 66, 0]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [33, 66, 0]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(amount = [99, 1, 0]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [99, 1, 0]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(amount = [50, 25, 10]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [50, 25, 10]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [49, 50, 51]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [49, 50, 51]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(amount = [60, 60, 61]) == 91
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [60, 60, 61]) == 91: {e}')
    
    total += 1
    try:
        result = candidate(amount = [29, 42, 29]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [29, 42, 29]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [50, 50, 50]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [50, 50, 50]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(amount = [25, 25, 26]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [25, 25, 26]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(amount = [34, 33, 34]) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [34, 33, 34]) == 51: {e}')
    
    total += 1
    try:
        result = candidate(amount = [2, 49, 49]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [2, 49, 49]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [25, 25, 25]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [25, 25, 25]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 1, 2]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 1, 2]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 1, 99]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 1, 99]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(amount = [60, 40, 20]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [60, 40, 20]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(amount = [60, 60, 60]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [60, 60, 60]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(amount = [33, 33, 67]) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [33, 33, 67]) == 67: {e}')
    
    total += 1
    try:
        result = candidate(amount = [10, 100, 10]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [10, 100, 10]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [5, 0, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [5, 0, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 100, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 100, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [80, 15, 5]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [80, 15, 5]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(amount = [99, 99, 99]) == 149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [99, 99, 99]) == 149: {e}')
    
    total += 1
    try:
        result = candidate(amount = [66, 33, 0]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [66, 33, 0]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(amount = [2, 3, 4]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [2, 3, 4]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(amount = [5, 15, 80]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [5, 15, 80]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(amount = [30, 0, 20]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [30, 0, 20]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(amount = [50, 25, 25]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [50, 25, 25]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [47, 23, 29]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [47, 23, 29]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [100, 99, 98]) == 149
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [100, 99, 98]) == 149: {e}')
    
    total += 1
    try:
        result = candidate(amount = [90, 85, 80]) == 128
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [90, 85, 80]) == 128: {e}')
    
    total += 1
    try:
        result = candidate(amount = [67, 33, 33]) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [67, 33, 33]) == 67: {e}')
    
    total += 1
    try:
        result = candidate(amount = [98, 99, 1]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [98, 99, 1]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(amount = [15, 80, 5]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [15, 80, 5]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(amount = [10, 10, 80]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [10, 10, 80]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(amount = [3, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [3, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(amount = [23, 45, 67]) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [23, 45, 67]) == 68: {e}')
    
    total += 1
    try:
        result = candidate(amount = [50, 50, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [50, 50, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [90, 10, 90]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [90, 10, 90]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(amount = [99, 98, 97]) == 147
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [99, 98, 97]) == 147: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 99, 1]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 99, 1]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(amount = [45, 55, 55]) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [45, 55, 55]) == 78: {e}')
    
    total += 1
    try:
        result = candidate(amount = [75, 25, 0]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [75, 25, 0]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(amount = [0, 0, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [0, 0, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 100, 1]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 100, 1]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 2, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 2, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(amount = [70, 20, 10]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [70, 20, 10]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(amount = [2, 2, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [2, 2, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(amount = [95, 3, 2]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [95, 3, 2]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 2, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 2, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(amount = [0, 99, 0]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [0, 99, 0]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(amount = [60, 40, 0]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [60, 40, 0]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(amount = [10, 10, 10]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [10, 10, 10]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(amount = [33, 34, 33]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [33, 34, 33]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [50, 50, 5]) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [50, 50, 5]) == 53: {e}')
    
    total += 1
    try:
        result = candidate(amount = [2, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [2, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(amount = [2, 1, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [2, 1, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(amount = [10, 90, 0]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [10, 90, 0]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(amount = [66, 33, 3]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [66, 33, 3]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(amount = [49, 49, 2]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [49, 49, 2]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [67, 23, 45]) == 68
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [67, 23, 45]) == 68: {e}')
    
    total += 1
    try:
        result = candidate(amount = [50, 49, 48]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [50, 49, 48]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(amount = [55, 45, 55]) == 78
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [55, 45, 55]) == 78: {e}')
    
    total += 1
    try:
        result = candidate(amount = [0, 55, 45]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [0, 55, 45]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(amount = [100, 0, 0]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [100, 0, 0]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [0, 1, 1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [0, 1, 1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 1, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 1, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 2, 2]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 2, 2]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(amount = [50, 50, 0]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [50, 50, 0]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [34, 33, 33]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [34, 33, 33]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [0, 100, 0]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [0, 100, 0]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [42, 41, 42]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [42, 41, 42]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(amount = [100, 50, 50]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [100, 50, 50]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [99, 100, 101]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [99, 100, 101]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(amount = [100, 50, 50]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [100, 50, 50]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [10, 0, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [10, 0, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [0, 99, 1]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [0, 99, 1]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(amount = [99, 99, 2]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [99, 99, 2]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [50, 0, 50]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [50, 0, 50]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [41, 42, 42]) == 63
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [41, 42, 42]) == 63: {e}')
    
    total += 1
    try:
        result = candidate(amount = [0, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [0, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 99, 98]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 99, 98]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(amount = [2, 2, 98]) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [2, 2, 98]) == 98: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 1, 98]) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 1, 98]) == 98: {e}')
    
    total += 1
    try:
        result = candidate(amount = [10, 10, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [10, 10, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(amount = [1, 99, 99]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [1, 99, 99]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [29, 47, 23]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [29, 47, 23]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [33, 67, 33]) == 67
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [33, 67, 33]) == 67: {e}')
    
    total += 1
    try:
        result = candidate(amount = [99, 98, 97]) == 147
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [99, 98, 97]) == 147: {e}')
    
    total += 1
    try:
        result = candidate(amount = [10, 20, 30]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [10, 20, 30]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(amount = [0, 50, 50]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [0, 50, 50]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(amount = [99, 1, 0]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [99, 1, 0]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(amount = [99, 1, 99]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [99, 1, 99]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(amount = [10, 90, 10]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(amount = [10, 90, 10]) == 90: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(amount = [33, 33, 34]) == 50
    assert candidate(amount = [0, 0, 0]) == 0
    assert candidate(amount = [99, 1, 1]) == 99
    assert candidate(amount = [7, 7, 7]) == 11
    assert candidate(amount = [10, 10, 10]) == 15
    assert candidate(amount = [1, 2, 3]) == 3
    assert candidate(amount = [100, 0, 0]) == 100
    assert candidate(amount = [100, 100, 100]) == 150
    assert candidate(amount = [0, 1, 2]) == 2
    assert candidate(amount = [1, 4, 2]) == 4
    assert candidate(amount = [5, 0, 0]) == 5
    assert candidate(amount = [99, 99, 1]) == 100
    assert candidate(amount = [0, 50, 50]) == 50
    assert candidate(amount = [5, 4, 4]) == 7
    assert candidate(amount = [98, 1, 1]) == 98
    assert candidate(amount = [25, 0, 75]) == 75
    assert candidate(amount = [42, 42, 41]) == 63
    assert candidate(amount = [60, 20, 20]) == 60
    assert candidate(amount = [10, 50, 25]) == 50
    assert candidate(amount = [49, 49, 49]) == 74
    assert candidate(amount = [1, 1, 0]) == 1
    assert candidate(amount = [80, 10, 10]) == 80
    assert candidate(amount = [1, 10, 10]) == 11
    assert candidate(amount = [1, 1, 100]) == 100
    assert candidate(amount = [10, 90, 0]) == 90
    assert candidate(amount = [10, 80, 10]) == 80
    assert candidate(amount = [0, 0, 100]) == 100
    assert candidate(amount = [80, 10, 10]) == 80
    assert candidate(amount = [33, 33, 34]) == 50
    assert candidate(amount = [70, 70, 60]) == 100
    assert candidate(amount = [50, 25, 25]) == 50
    assert candidate(amount = [29, 29, 42]) == 50
    assert candidate(amount = [50, 50, 49]) == 75
    assert candidate(amount = [99, 2, 99]) == 100
    assert candidate(amount = [50, 49, 51]) == 75
    assert candidate(amount = [100, 1, 1]) == 100
    assert candidate(amount = [80, 70, 60]) == 105
    assert candidate(amount = [100, 50, 25]) == 100
    assert candidate(amount = [1, 0, 1]) == 1
    assert candidate(amount = [40, 30, 20]) == 45
    assert candidate(amount = [1, 2, 97]) == 97
    assert candidate(amount = [1, 1, 1]) == 2
    assert candidate(amount = [49, 50, 1]) == 50
    assert candidate(amount = [30, 20, 10]) == 30
    assert candidate(amount = [100, 10, 10]) == 100
    assert candidate(amount = [2, 99, 99]) == 100
    assert candidate(amount = [1, 98, 1]) == 98
    assert candidate(amount = [1, 0, 99]) == 99
    assert candidate(amount = [80, 15, 5]) == 80
    assert candidate(amount = [45, 55, 0]) == 55
    assert candidate(amount = [100, 1, 1]) == 100
    assert candidate(amount = [50, 50, 1]) == 51
    assert candidate(amount = [25, 25, 25]) == 38
    assert candidate(amount = [42, 29, 29]) == 50
    assert candidate(amount = [100, 50, 1]) == 100
    assert candidate(amount = [1, 90, 10]) == 90
    assert candidate(amount = [1, 1, 1]) == 2
    assert candidate(amount = [0, 75, 25]) == 75
    assert candidate(amount = [55, 45, 5]) == 55
    assert candidate(amount = [10, 1, 90]) == 90
    assert candidate(amount = [100, 10, 0]) == 100
    assert candidate(amount = [80, 10, 1]) == 80
    assert candidate(amount = [48, 48, 48]) == 72
    assert candidate(amount = [80, 50, 30]) == 80
    assert candidate(amount = [90, 90, 1]) == 91
    assert candidate(amount = [1, 50, 50]) == 51
    assert candidate(amount = [55, 0, 45]) == 55
    assert candidate(amount = [49, 2, 49]) == 50
    assert candidate(amount = [45, 67, 23]) == 68
    assert candidate(amount = [20, 20, 60]) == 60
    assert candidate(amount = [100, 100, 99]) == 150
    assert candidate(amount = [10, 10, 100]) == 100
    assert candidate(amount = [50, 100, 50]) == 100
    assert candidate(amount = [10, 15, 20]) == 23
    assert candidate(amount = [0, 100, 100]) == 100
    assert candidate(amount = [60, 40, 20]) == 60
    assert candidate(amount = [0, 100, 0]) == 100
    assert candidate(amount = [50, 51, 50]) == 76
    assert candidate(amount = [33, 33, 33]) == 50
    assert candidate(amount = [23, 47, 29]) == 50
    assert candidate(amount = [51, 51, 51]) == 77
    assert candidate(amount = [50, 1, 50]) == 51
    assert candidate(amount = [25, 10, 50]) == 50
    assert candidate(amount = [55, 55, 45]) == 78
    assert candidate(amount = [0, 100, 10]) == 100
    assert candidate(amount = [90, 10, 1]) == 90
    assert candidate(amount = [33, 66, 0]) == 66
    assert candidate(amount = [99, 1, 0]) == 99
    assert candidate(amount = [50, 25, 10]) == 50
    assert candidate(amount = [49, 50, 51]) == 75
    assert candidate(amount = [60, 60, 61]) == 91
    assert candidate(amount = [29, 42, 29]) == 50
    assert candidate(amount = [50, 50, 50]) == 75
    assert candidate(amount = [25, 25, 26]) == 38
    assert candidate(amount = [34, 33, 34]) == 51
    assert candidate(amount = [2, 49, 49]) == 50
    assert candidate(amount = [25, 25, 25]) == 38
    assert candidate(amount = [1, 1, 2]) == 2
    assert candidate(amount = [1, 1, 99]) == 99
    assert candidate(amount = [60, 40, 20]) == 60
    assert candidate(amount = [60, 60, 60]) == 90
    assert candidate(amount = [33, 33, 67]) == 67
    assert candidate(amount = [10, 100, 10]) == 100
    assert candidate(amount = [5, 0, 5]) == 5
    assert candidate(amount = [1, 100, 1]) == 100
    assert candidate(amount = [80, 15, 5]) == 80
    assert candidate(amount = [99, 99, 99]) == 149
    assert candidate(amount = [66, 33, 0]) == 66
    assert candidate(amount = [2, 3, 4]) == 5
    assert candidate(amount = [5, 15, 80]) == 80
    assert candidate(amount = [30, 0, 20]) == 30
    assert candidate(amount = [50, 25, 25]) == 50
    assert candidate(amount = [47, 23, 29]) == 50
    assert candidate(amount = [100, 99, 98]) == 149
    assert candidate(amount = [90, 85, 80]) == 128
    assert candidate(amount = [67, 33, 33]) == 67
    assert candidate(amount = [98, 99, 1]) == 99
    assert candidate(amount = [15, 80, 5]) == 80
    assert candidate(amount = [10, 10, 80]) == 80
    assert candidate(amount = [3, 2, 1]) == 3
    assert candidate(amount = [23, 45, 67]) == 68
    assert candidate(amount = [50, 50, 100]) == 100
    assert candidate(amount = [90, 10, 90]) == 95
    assert candidate(amount = [99, 98, 97]) == 147
    assert candidate(amount = [1, 99, 1]) == 99
    assert candidate(amount = [45, 55, 55]) == 78
    assert candidate(amount = [75, 25, 0]) == 75
    assert candidate(amount = [0, 0, 100]) == 100
    assert candidate(amount = [1, 100, 1]) == 100
    assert candidate(amount = [1, 2, 1]) == 2
    assert candidate(amount = [70, 20, 10]) == 70
    assert candidate(amount = [2, 2, 1]) == 3
    assert candidate(amount = [95, 3, 2]) == 95
    assert candidate(amount = [1, 2, 3]) == 3
    assert candidate(amount = [0, 99, 0]) == 99
    assert candidate(amount = [60, 40, 0]) == 60
    assert candidate(amount = [10, 10, 10]) == 15
    assert candidate(amount = [33, 34, 33]) == 50
    assert candidate(amount = [50, 50, 5]) == 53
    assert candidate(amount = [2, 1, 1]) == 2
    assert candidate(amount = [2, 1, 2]) == 3
    assert candidate(amount = [10, 90, 0]) == 90
    assert candidate(amount = [66, 33, 3]) == 66
    assert candidate(amount = [49, 49, 2]) == 50
    assert candidate(amount = [67, 23, 45]) == 68
    assert candidate(amount = [50, 49, 48]) == 74
    assert candidate(amount = [55, 45, 55]) == 78
    assert candidate(amount = [0, 55, 45]) == 55
    assert candidate(amount = [100, 0, 0]) == 100
    assert candidate(amount = [0, 1, 1]) == 1
    assert candidate(amount = [1, 1, 100]) == 100
    assert candidate(amount = [1, 2, 2]) == 3
    assert candidate(amount = [50, 50, 0]) == 50
    assert candidate(amount = [34, 33, 33]) == 50
    assert candidate(amount = [0, 100, 0]) == 100
    assert candidate(amount = [42, 41, 42]) == 63
    assert candidate(amount = [100, 50, 50]) == 100
    assert candidate(amount = [99, 100, 101]) == 150
    assert candidate(amount = [100, 50, 50]) == 100
    assert candidate(amount = [10, 0, 100]) == 100
    assert candidate(amount = [0, 99, 1]) == 99
    assert candidate(amount = [99, 99, 2]) == 100
    assert candidate(amount = [50, 0, 50]) == 50
    assert candidate(amount = [41, 42, 42]) == 63
    assert candidate(amount = [0, 5, 5]) == 5
    assert candidate(amount = [1, 99, 98]) == 99
    assert candidate(amount = [2, 2, 98]) == 98
    assert candidate(amount = [1, 1, 98]) == 98
    assert candidate(amount = [10, 10, 1]) == 11
    assert candidate(amount = [1, 99, 99]) == 100
    assert candidate(amount = [29, 47, 23]) == 50
    assert candidate(amount = [33, 67, 33]) == 67
    assert candidate(amount = [99, 98, 97]) == 147
    assert candidate(amount = [10, 20, 30]) == 30
    assert candidate(amount = [0, 50, 50]) == 50
    assert candidate(amount = [99, 1, 0]) == 99
    assert candidate(amount = [99, 1, 99]) == 100
    assert candidate(amount = [10, 90, 10]) == 90


