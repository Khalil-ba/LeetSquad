def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(orders = [[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]) == 999999984
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]) == 999999984: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 10, 0], [1, 10, 1], [1, 10, 0], [1, 10, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 10, 0], [1, 10, 1], [1, 10, 0], [1, 10, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 1, 0], [200, 2, 0], [300, 3, 1], [400, 4, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 1, 0], [200, 2, 0], [300, 3, 1], [400, 4, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1, 0], [1, 1, 1], [1, 1, 0], [1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1, 0], [1, 1, 1], [1, 1, 0], [1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[5, 5, 0], [5, 5, 1], [5, 5, 0], [5, 5, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[5, 5, 0], [5, 5, 1], [5, 5, 0], [5, 5, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 100, 0], [100, 100, 1], [101, 100, 0], [99, 100, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 100, 0], [100, 100, 1], [101, 100, 0], [99, 100, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 10, 0], [2, 10, 0], [3, 10, 1], [4, 10, 1]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 10, 0], [2, 10, 0], [3, 10, 1], [4, 10, 1]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[5, 5, 0], [4, 4, 1], [3, 3, 0], [2, 2, 1], [1, 1, 0]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[5, 5, 0], [4, 4, 1], [3, 3, 0], [2, 2, 1], [1, 1, 0]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 10, 0], [200, 15, 0], [100, 5, 1], [200, 20, 1]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 10, 0], [200, 15, 0], [100, 5, 1], [200, 20, 1]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[5, 5, 0], [5, 5, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[5, 5, 0], [5, 5, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 1, 0], [99, 2, 0], [98, 3, 0], [97, 4, 1], [96, 5, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 1, 0], [99, 2, 0], [98, 3, 0], [97, 4, 1], [96, 5, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[5, 10, 0], [5, 5, 1], [5, 5, 0], [5, 3, 1]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[5, 10, 0], [5, 5, 1], [5, 5, 0], [5, 3, 1]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 10, 0], [2, 20, 1], [3, 30, 0], [4, 40, 1]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 10, 0], [2, 20, 1], [3, 30, 0], [4, 40, 1]]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 10, 0], [99, 9, 1], [98, 8, 0], [97, 7, 1], [96, 6, 0]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 10, 0], [99, 9, 1], [98, 8, 0], [97, 7, 1], [96, 6, 0]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 10, 0], [10, 10, 0], [10, 10, 1], [10, 10, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 10, 0], [10, 10, 0], [10, 10, 1], [10, 10, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[50, 10, 0], [40, 15, 0], [30, 20, 0], [20, 25, 1], [10, 30, 1], [5, 35, 1], [3, 40, 1], [2, 45, 1], [1, 50, 1]]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[50, 10, 0], [40, 15, 0], [30, 20, 0], [20, 25, 1], [10, 30, 1], [5, 35, 1], [3, 40, 1], [2, 45, 1], [1, 50, 1]]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 5, 0], [20, 5, 0], [30, 5, 0], [40, 5, 0], [10, 5, 1], [20, 5, 1], [30, 5, 1], [40, 5, 1], [5, 5, 0], [35, 5, 1]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 5, 0], [20, 5, 0], [30, 5, 0], [40, 5, 0], [10, 5, 1], [20, 5, 1], [30, 5, 1], [40, 5, 1], [5, 5, 0], [35, 5, 1]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1000000000, 0], [1, 1000000000, 0], [1, 1000000000, 1], [1, 1000000000, 1], [1, 1000000000, 0], [1, 1000000000, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1000000000, 0], [1, 1000000000, 0], [1, 1000000000, 1], [1, 1000000000, 1], [1, 1000000000, 0], [1, 1000000000, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1000000000, 1, 0], [1000000000, 1, 0], [1000000000, 1, 0], [1000000000, 1, 1], [1000000000, 1, 1], [1000000000, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1000000000, 1, 0], [1000000000, 1, 0], [1000000000, 1, 0], [1000000000, 1, 1], [1000000000, 1, 1], [1000000000, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 5, 0], [9, 5, 0], [8, 5, 0], [7, 5, 0], [6, 5, 0], [6, 5, 1], [7, 5, 1], [8, 5, 1], [9, 5, 1], [10, 5, 1]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 5, 0], [9, 5, 0], [8, 5, 0], [7, 5, 0], [6, 5, 0], [6, 5, 1], [7, 5, 1], [8, 5, 1], [9, 5, 1], [10, 5, 1]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1000000000, 1, 0], [999999999, 2, 0], [999999998, 3, 0], [999999997, 4, 1], [999999996, 5, 1], [999999995, 6, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1000000000, 1, 0], [999999999, 2, 0], [999999998, 3, 0], [999999997, 4, 1], [999999996, 5, 1], [999999995, 6, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1000000000, 0], [1000000000, 1, 1], [2, 999999999, 0], [999999999, 2, 1], [3, 999999998, 0], [999999998, 3, 1], [4, 999999997, 0], [999999997, 4, 1]]) == 999999983
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1000000000, 0], [1000000000, 1, 1], [2, 999999999, 0], [999999999, 2, 1], [3, 999999998, 0], [999999998, 3, 1], [4, 999999997, 0], [999999997, 4, 1]]) == 999999983: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1000000000, 1, 0], [999999999, 2, 0], [999999998, 3, 0], [999999997, 4, 1], [999999996, 5, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1000000000, 1, 0], [999999999, 2, 0], [999999998, 3, 0], [999999997, 4, 1], [999999996, 5, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1000, 0], [2, 2000, 1], [3, 3000, 0], [4, 4000, 1], [5, 5000, 0], [6, 6000, 1], [7, 7000, 0], [8, 8000, 1], [9, 9000, 0], [10, 10000, 1]]) == 15000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1000, 0], [2, 2000, 1], [3, 3000, 0], [4, 4000, 1], [5, 5000, 0], [6, 6000, 1], [7, 7000, 0], [8, 8000, 1], [9, 9000, 0], [10, 10000, 1]]) == 15000: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1000, 1, 0], [1000, 2, 0], [1000, 3, 0], [1000, 1, 1], [1000, 2, 1], [1000, 3, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1000, 1, 0], [1000, 2, 0], [1000, 3, 0], [1000, 1, 1], [1000, 2, 1], [1000, 3, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 100, 0], [20, 50, 1], [15, 30, 0], [25, 20, 1], [5, 10, 0], [30, 5, 1]]) == 215
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 100, 0], [20, 50, 1], [15, 30, 0], [25, 20, 1], [5, 10, 0], [30, 5, 1]]) == 215: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 10, 0], [90, 5, 1], [80, 15, 0], [70, 20, 1], [60, 25, 0], [50, 30, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 10, 0], [90, 5, 1], [80, 15, 0], [70, 20, 1], [60, 25, 0], [50, 30, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[999999999, 50000, 0], [1, 50000, 1], [999999998, 50000, 0], [2, 50000, 1], [999999997, 50000, 0], [3, 50000, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[999999999, 50000, 0], [1, 50000, 1], [999999998, 50000, 0], [2, 50000, 1], [999999997, 50000, 0], [3, 50000, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1000000000, 0], [2, 999999999, 0], [3, 999999998, 0], [4, 999999997, 0], [5, 999999996, 0], [5, 999999996, 1], [4, 999999997, 1], [3, 999999998, 1], [2, 999999999, 1], [1, 1000000000, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1000000000, 0], [2, 999999999, 0], [3, 999999998, 0], [4, 999999997, 0], [5, 999999996, 0], [5, 999999996, 1], [4, 999999997, 1], [3, 999999998, 1], [2, 999999999, 1], [1, 1000000000, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 10, 0], [20, 20, 1], [15, 15, 0], [16, 16, 1], [14, 14, 0], [17, 17, 1]]) == 92
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 10, 0], [20, 20, 1], [15, 15, 0], [16, 16, 1], [14, 14, 0], [17, 17, 1]]) == 92: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 1, 0], [9, 2, 0], [8, 3, 0], [7, 4, 0], [6, 5, 1], [5, 6, 1], [4, 7, 1], [3, 8, 1], [2, 9, 1], [1, 10, 1]]) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 1, 0], [9, 2, 0], [8, 3, 0], [7, 4, 0], [6, 5, 1], [5, 6, 1], [4, 7, 1], [3, 8, 1], [2, 9, 1], [1, 10, 1]]) == 35: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1000, 1000000, 0], [1001, 1000000, 0], [1002, 1000000, 0], [999, 1000000, 1], [998, 1000000, 1], [997, 1000000, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1000, 1000000, 0], [1001, 1000000, 0], [1002, 1000000, 0], [999, 1000000, 1], [998, 1000000, 1], [997, 1000000, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 10, 0], [20, 10, 1], [15, 10, 0], [25, 10, 1], [10, 10, 0], [20, 10, 1], [15, 10, 0], [25, 10, 1], [10, 10, 0], [20, 10, 1], [15, 10, 0], [25, 10, 1], [10, 10, 0], [20, 10, 1], [15, 10, 0], [25, 10, 1]]) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 10, 0], [20, 10, 1], [15, 10, 0], [25, 10, 1], [10, 10, 0], [20, 10, 1], [15, 10, 0], [25, 10, 1], [10, 10, 0], [20, 10, 1], [15, 10, 0], [25, 10, 1], [10, 10, 0], [20, 10, 1], [15, 10, 0], [25, 10, 1]]) == 160: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1000000000, 0], [2, 1000000000, 1], [3, 1000000000, 0], [4, 1000000000, 1], [5, 1000000000, 0], [6, 1000000000, 1]]) == 999999993
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1000000000, 0], [2, 1000000000, 1], [3, 1000000000, 0], [4, 1000000000, 1], [5, 1000000000, 0], [6, 1000000000, 1]]) == 999999993: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 1000, 0], [20, 1000, 0], [30, 1000, 0], [40, 1000, 1], [50, 1000, 1], [60, 1000, 1], [70, 1000, 0], [80, 1000, 1], [90, 1000, 0]]) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 1000, 0], [20, 1000, 0], [30, 1000, 0], [40, 1000, 1], [50, 1000, 1], [60, 1000, 1], [70, 1000, 0], [80, 1000, 1], [90, 1000, 0]]) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 5, 0], [20, 10, 0], [30, 15, 0], [40, 20, 0], [50, 25, 0], [10, 5, 1], [20, 10, 1], [30, 15, 1], [40, 20, 1], [50, 25, 1]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 5, 0], [20, 10, 0], [30, 15, 0], [40, 20, 0], [50, 25, 0], [10, 5, 1], [20, 10, 1], [30, 15, 1], [40, 20, 1], [50, 25, 1]]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 5, 0], [20, 5, 0], [30, 5, 0], [40, 5, 0], [15, 5, 1], [25, 5, 1], [35, 5, 1], [45, 5, 1]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 5, 0], [20, 5, 0], [30, 5, 0], [40, 5, 0], [15, 5, 1], [25, 5, 1], [35, 5, 1], [45, 5, 1]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1000000000, 0], [2, 1000000000, 0], [3, 1000000000, 0], [1, 1000000000, 1], [2, 1000000000, 1], [3, 1000000000, 1]]) == 999999993
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1000000000, 0], [2, 1000000000, 0], [3, 1000000000, 0], [1, 1000000000, 1], [2, 1000000000, 1], [3, 1000000000, 1]]) == 999999993: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 1, 0], [11, 2, 0], [12, 3, 0], [13, 4, 1], [14, 5, 1], [15, 6, 1], [16, 7, 1], [17, 8, 0], [18, 9, 0], [19, 10, 0]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 1, 0], [11, 2, 0], [12, 3, 0], [13, 4, 1], [14, 5, 1], [15, 6, 1], [16, 7, 1], [17, 8, 0], [18, 9, 0], [19, 10, 0]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 1, 0], [10, 2, 0], [10, 3, 0], [10, 4, 1], [10, 5, 1], [10, 6, 1], [10, 7, 1], [10, 8, 0], [10, 9, 0], [10, 10, 0]]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 1, 0], [10, 2, 0], [10, 3, 0], [10, 4, 1], [10, 5, 1], [10, 6, 1], [10, 7, 1], [10, 8, 0], [10, 9, 0], [10, 10, 0]]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[5, 1, 0], [5, 2, 0], [5, 3, 0], [5, 4, 0], [5, 5, 1], [5, 4, 1], [5, 3, 1], [5, 2, 1], [5, 1, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[5, 1, 0], [5, 2, 0], [5, 3, 0], [5, 4, 0], [5, 5, 1], [5, 4, 1], [5, 3, 1], [5, 2, 1], [5, 1, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 5, 0], [90, 10, 0], [80, 15, 0], [70, 20, 0], [60, 25, 0], [50, 30, 1], [40, 35, 1], [30, 40, 1], [20, 45, 1], [10, 50, 1]]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 5, 0], [90, 10, 0], [80, 15, 0], [70, 20, 0], [60, 25, 0], [50, 30, 1], [40, 35, 1], [30, 40, 1], [20, 45, 1], [10, 50, 1]]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 1000, 0], [10, 900, 0], [10, 800, 0], [10, 700, 1], [10, 600, 1], [10, 500, 1], [10, 400, 1]]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 1000, 0], [10, 900, 0], [10, 800, 0], [10, 700, 1], [10, 600, 1], [10, 500, 1], [10, 400, 1]]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 5, 0], [10, 5, 1], [10, 5, 0], [10, 5, 1], [10, 5, 0], [10, 5, 1], [10, 5, 0], [10, 5, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 5, 0], [10, 5, 1], [10, 5, 0], [10, 5, 1], [10, 5, 0], [10, 5, 1], [10, 5, 0], [10, 5, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 999999999, 0], [1, 999999999, 0], [1, 999999999, 0], [1, 999999999, 0], [2, 999999999, 1], [2, 999999999, 1], [2, 999999999, 1], [2, 999999999, 1]]) == 999999943
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 999999999, 0], [1, 999999999, 0], [1, 999999999, 0], [1, 999999999, 0], [2, 999999999, 1], [2, 999999999, 1], [2, 999999999, 1], [2, 999999999, 1]]) == 999999943: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 1, 0], [9, 2, 0], [8, 3, 0], [7, 4, 1], [6, 5, 1], [5, 6, 0], [4, 7, 0], [3, 8, 1], [2, 9, 1], [1, 10, 0]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 1, 0], [9, 2, 0], [8, 3, 0], [7, 4, 1], [6, 5, 1], [5, 6, 0], [4, 7, 0], [3, 8, 1], [2, 9, 1], [1, 10, 0]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[5, 100, 0], [10, 100, 1], [15, 100, 0], [20, 100, 1], [25, 100, 0], [30, 100, 1]]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[5, 100, 0], [10, 100, 1], [15, 100, 0], [20, 100, 1], [25, 100, 0], [30, 100, 1]]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 5, 0], [10, 5, 0], [10, 5, 0], [10, 5, 1], [10, 5, 1], [10, 5, 1], [10, 5, 0], [10, 5, 1], [10, 5, 0], [10, 5, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 5, 0], [10, 5, 0], [10, 5, 0], [10, 5, 1], [10, 5, 1], [10, 5, 1], [10, 5, 0], [10, 5, 1], [10, 5, 0], [10, 5, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 100, 1], [90, 200, 1], [80, 300, 1], [70, 400, 0], [60, 500, 0], [50, 600, 0]]) == 2100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 100, 1], [90, 200, 1], [80, 300, 1], [70, 400, 0], [60, 500, 0], [50, 600, 0]]) == 2100: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1000000000, 1, 0], [999999999, 1, 0], [999999998, 1, 0], [999999997, 1, 1], [999999996, 1, 1], [999999995, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1000000000, 1, 0], [999999999, 1, 0], [999999998, 1, 0], [999999997, 1, 1], [999999996, 1, 1], [999999995, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 1, 0], [20, 2, 0], [30, 3, 0], [40, 4, 0], [50, 5, 0], [10, 1, 1], [20, 2, 1], [30, 3, 1], [40, 4, 1], [50, 5, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 1, 0], [20, 2, 0], [30, 3, 0], [40, 4, 0], [50, 5, 0], [10, 1, 1], [20, 2, 1], [30, 3, 1], [40, 4, 1], [50, 5, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1000000000, 0], [1000000000, 1, 1], [500000000, 2, 0], [1000000000, 999999999, 1], [1, 1, 0]]) == 999999996
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1000000000, 0], [1000000000, 1, 1], [500000000, 2, 0], [1000000000, 999999999, 1], [1, 1, 0]]) == 999999996: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1000000000, 0], [2, 1000000000, 1], [3, 1000000000, 0], [4, 1000000000, 1], [5, 1000000000, 0], [6, 1000000000, 1]]) == 999999993
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1000000000, 0], [2, 1000000000, 1], [3, 1000000000, 0], [4, 1000000000, 1], [5, 1000000000, 0], [6, 1000000000, 1]]) == 999999993: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 1000, 0], [999, 500, 1], [998, 750, 1], [1000, 1000, 0], [999, 250, 0]]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 1000, 0], [999, 500, 1], [998, 750, 1], [1000, 1000, 0], [999, 250, 0]]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 1, 0], [99, 2, 0], [98, 3, 0], [97, 4, 1], [96, 5, 1], [95, 6, 0], [94, 7, 1], [93, 8, 0], [92, 9, 1]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 1, 0], [99, 2, 0], [98, 3, 0], [97, 4, 1], [96, 5, 1], [95, 6, 0], [94, 7, 1], [93, 8, 0], [92, 9, 1]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1000000000, 0], [1, 1000000000, 0], [1, 1000000000, 0], [1, 1000000000, 1], [1, 1000000000, 1], [1, 1000000000, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1000000000, 0], [1, 1000000000, 0], [1, 1000000000, 0], [1, 1000000000, 1], [1, 1000000000, 1], [1, 1000000000, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 1, 0], [99, 2, 0], [98, 3, 0], [97, 4, 1], [96, 5, 1], [95, 6, 0], [94, 7, 0], [93, 8, 1], [92, 9, 1]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 1, 0], [99, 2, 0], [98, 3, 0], [97, 4, 1], [96, 5, 1], [95, 6, 0], [94, 7, 0], [93, 8, 1], [92, 9, 1]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 100, 0], [200, 200, 0], [300, 300, 0], [400, 400, 0], [500, 500, 1], [600, 600, 1], [700, 700, 1], [800, 800, 1], [900, 900, 1], [1000, 1000, 1]]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 100, 0], [200, 200, 0], [300, 300, 0], [400, 400, 0], [500, 500, 1], [600, 600, 1], [700, 700, 1], [800, 800, 1], [900, 900, 1], [1000, 1000, 1]]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 5, 0], [20, 10, 0], [30, 15, 0], [5, 1, 1], [15, 2, 1], [25, 3, 1]]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 5, 0], [20, 10, 0], [30, 15, 0], [5, 1, 1], [15, 2, 1], [25, 3, 1]]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 100, 0], [99, 150, 0], [98, 200, 0], [97, 250, 1], [96, 300, 1], [95, 350, 1]]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 100, 0], [99, 150, 0], [98, 200, 0], [97, 250, 1], [96, 300, 1], [95, 350, 1]]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1, 0], [2, 1, 0], [3, 1, 0], [4, 1, 0], [5, 1, 0], [6, 1, 0], [7, 1, 0], [8, 1, 0], [9, 1, 0], [10, 1, 0], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 1, 1], [5, 1, 1], [6, 1, 1], [7, 1, 1], [8, 1, 1], [9, 1, 1], [10, 1, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1, 0], [2, 1, 0], [3, 1, 0], [4, 1, 0], [5, 1, 0], [6, 1, 0], [7, 1, 0], [8, 1, 0], [9, 1, 0], [10, 1, 0], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 1, 1], [5, 1, 1], [6, 1, 1], [7, 1, 1], [8, 1, 1], [9, 1, 1], [10, 1, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1000000000, 1, 0], [1, 1, 1], [500000000, 1, 0], [500000000, 1, 1], [1000000000, 1, 0], [1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1000000000, 1, 0], [1, 1, 1], [500000000, 1, 0], [500000000, 1, 1], [1000000000, 1, 0], [1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 100, 0], [90, 200, 0], [80, 300, 0], [70, 400, 1], [60, 500, 1], [50, 600, 1]]) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 100, 0], [90, 200, 0], [80, 300, 0], [70, 400, 1], [60, 500, 1], [50, 600, 1]]) == 900: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 1, 0], [20, 2, 0], [10, 1, 1], [20, 2, 1], [30, 3, 0], [25, 2, 1], [15, 1, 0], [5, 1, 1]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 1, 0], [20, 2, 0], [10, 1, 1], [20, 2, 1], [30, 3, 0], [25, 2, 1], [15, 1, 0], [5, 1, 1]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 5, 0], [200, 10, 0], [150, 5, 1], [160, 5, 1], [200, 20, 0], [150, 10, 1]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 5, 0], [200, 10, 0], [150, 5, 1], [160, 5, 1], [200, 20, 0], [150, 10, 1]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 10, 0], [20, 10, 0], [30, 10, 0], [40, 10, 0], [50, 10, 0], [10, 10, 1], [20, 10, 1], [30, 10, 1], [40, 10, 1], [50, 10, 1], [10, 10, 0], [20, 10, 0], [30, 10, 0], [40, 10, 0], [50, 10, 0], [10, 10, 1], [20, 10, 1], [30, 10, 1], [40, 10, 1], [50, 10, 1]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 10, 0], [20, 10, 0], [30, 10, 0], [40, 10, 0], [50, 10, 0], [10, 10, 1], [20, 10, 1], [30, 10, 1], [40, 10, 1], [50, 10, 1], [10, 10, 0], [20, 10, 0], [30, 10, 0], [40, 10, 0], [50, 10, 0], [10, 10, 1], [20, 10, 1], [30, 10, 1], [40, 10, 1], [50, 10, 1]]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 1, 0], [90, 2, 0], [80, 3, 0], [70, 4, 1], [60, 5, 1], [50, 6, 1], [40, 7, 1], [30, 8, 1], [20, 9, 1], [10, 10, 1]]) == 43
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 1, 0], [90, 2, 0], [80, 3, 0], [70, 4, 1], [60, 5, 1], [50, 6, 1], [40, 7, 1], [30, 8, 1], [20, 9, 1], [10, 10, 1]]) == 43: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1, 0], [2, 1, 0], [3, 1, 0], [4, 1, 0], [5, 1, 0], [5, 1, 1], [4, 1, 1], [3, 1, 1], [2, 1, 1], [1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1, 0], [2, 1, 0], [3, 1, 0], [4, 1, 0], [5, 1, 0], [5, 1, 1], [4, 1, 1], [3, 1, 1], [2, 1, 1], [1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1000000000, 1, 0], [999999999, 2, 0], [999999998, 3, 0], [999999997, 4, 1], [999999996, 5, 1], [999999995, 6, 0], [999999994, 7, 0], [999999993, 8, 1], [999999992, 9, 1]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1000000000, 1, 0], [999999999, 2, 0], [999999998, 3, 0], [999999997, 4, 1], [999999996, 5, 1], [999999995, 6, 0], [999999994, 7, 0], [999999993, 8, 1], [999999992, 9, 1]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 100, 0], [20, 50, 0], [30, 200, 1], [15, 150, 1], [25, 100, 0], [35, 100, 1]]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 100, 0], [20, 50, 0], [30, 200, 1], [15, 150, 1], [25, 100, 0], [35, 100, 1]]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1, 0], [1, 1, 1], [1, 1, 0], [1, 1, 1], [1, 1, 0], [1, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1, 0], [1, 1, 1], [1, 1, 0], [1, 1, 1], [1, 1, 0], [1, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1, 0], [2, 2, 0], [3, 3, 0], [4, 4, 0], [5, 5, 0], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1, 0], [2, 2, 0], [3, 3, 0], [4, 4, 0], [5, 5, 0], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 5, 0], [100, 5, 0], [100, 5, 1], [100, 5, 1], [100, 5, 0], [100, 5, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 5, 0], [100, 5, 0], [100, 5, 1], [100, 5, 1], [100, 5, 0], [100, 5, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[5, 1, 0], [6, 1, 0], [7, 1, 0], [8, 1, 0], [9, 1, 0], [10, 1, 1], [11, 1, 1], [12, 1, 1], [13, 1, 1], [14, 1, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[5, 1, 0], [6, 1, 0], [7, 1, 0], [8, 1, 0], [9, 1, 0], [10, 1, 1], [11, 1, 1], [12, 1, 1], [13, 1, 1], [14, 1, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 10, 0], [20, 20, 0], [30, 30, 0], [40, 40, 0], [50, 50, 0], [10, 1, 1], [20, 2, 1], [30, 3, 1], [40, 4, 1], [50, 5, 1]]) == 135
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 10, 0], [20, 20, 0], [30, 30, 0], [40, 40, 0], [50, 50, 0], [10, 1, 1], [20, 2, 1], [30, 3, 1], [40, 4, 1], [50, 5, 1]]) == 135: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[50, 10, 0], [50, 15, 0], [50, 20, 0], [50, 25, 1], [50, 30, 1], [50, 35, 1], [50, 40, 1], [50, 45, 1], [50, 50, 1]]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[50, 10, 0], [50, 15, 0], [50, 20, 0], [50, 25, 1], [50, 30, 1], [50, 35, 1], [50, 40, 1], [50, 45, 1], [50, 50, 1]]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 50, 0], [100, 50, 0], [100, 50, 0], [100, 50, 1], [100, 50, 1], [100, 50, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 50, 0], [100, 50, 0], [100, 50, 0], [100, 50, 1], [100, 50, 1], [100, 50, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 5, 0], [20, 5, 0], [30, 5, 0], [10, 5, 1], [20, 5, 1], [30, 5, 1], [15, 5, 0], [25, 5, 0], [35, 5, 0]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 5, 0], [20, 5, 0], [30, 5, 0], [10, 5, 1], [20, 5, 1], [30, 5, 1], [15, 5, 0], [25, 5, 0], [35, 5, 0]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 1, 0], [10, 1, 1], [11, 1, 0], [9, 1, 1], [12, 1, 0], [8, 1, 1], [13, 1, 0], [7, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 1, 0], [10, 1, 1], [11, 1, 0], [9, 1, 1], [12, 1, 0], [8, 1, 1], [13, 1, 0], [7, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1000000000, 0], [2, 1000000000, 0], [3, 1000000000, 0], [4, 1000000000, 1], [5, 1000000000, 1], [6, 1000000000, 1]]) == 999999965
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1000000000, 0], [2, 1000000000, 0], [3, 1000000000, 0], [4, 1000000000, 1], [5, 1000000000, 1], [6, 1000000000, 1]]) == 999999965: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 10, 0], [10, 10, 1], [10, 10, 0], [10, 10, 1], [10, 10, 0], [10, 10, 1], [10, 10, 0], [10, 10, 1], [10, 10, 0], [10, 10, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 10, 0], [10, 10, 1], [10, 10, 0], [10, 10, 1], [10, 10, 0], [10, 10, 1], [10, 10, 0], [10, 10, 1], [10, 10, 0], [10, 10, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1000000000, 0], [2, 999999999, 0], [3, 999999998, 0], [4, 999999997, 1], [5, 999999996, 1], [6, 999999995, 1], [7, 999999994, 1], [8, 999999993, 0], [9, 999999992, 0], [10, 999999991, 0]]) == 999999982
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1000000000, 0], [2, 999999999, 0], [3, 999999998, 0], [4, 999999997, 1], [5, 999999996, 1], [6, 999999995, 1], [7, 999999994, 1], [8, 999999993, 0], [9, 999999992, 0], [10, 999999991, 0]]) == 999999982: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[50, 10, 0], [40, 20, 0], [30, 30, 0], [20, 40, 0], [10, 50, 0], [10, 60, 1], [20, 70, 1], [30, 80, 1], [40, 90, 1], [50, 100, 1], [15, 5, 0], [25, 5, 0], [35, 5, 0], [45, 5, 0], [55, 5, 0]]) == 335
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[50, 10, 0], [40, 20, 0], [30, 30, 0], [20, 40, 0], [10, 50, 0], [10, 60, 1], [20, 70, 1], [30, 80, 1], [40, 90, 1], [50, 100, 1], [15, 5, 0], [25, 5, 0], [35, 5, 0], [45, 5, 0], [55, 5, 0]]) == 335: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 10, 0], [90, 10, 0], [80, 10, 0], [70, 10, 0], [60, 10, 0], [50, 10, 1], [40, 10, 1], [30, 10, 1], [20, 10, 1], [10, 10, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 10, 0], [90, 10, 0], [80, 10, 0], [70, 10, 0], [60, 10, 0], [50, 10, 1], [40, 10, 1], [30, 10, 1], [20, 10, 1], [10, 10, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 5, 0], [20, 5, 0], [30, 5, 0], [15, 10, 1], [25, 10, 1], [35, 10, 1], [10, 5, 0], [20, 5, 0], [30, 5, 0], [15, 10, 1], [25, 10, 1], [35, 10, 1]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 5, 0], [20, 5, 0], [30, 5, 0], [15, 10, 1], [25, 10, 1], [35, 10, 1], [10, 5, 0], [20, 5, 0], [30, 5, 0], [15, 10, 1], [25, 10, 1], [35, 10, 1]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 100000000, 0], [90, 200000000, 0], [80, 300000000, 1], [70, 400000000, 1], [60, 500000000, 0]]) == 900000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 100000000, 0], [90, 200000000, 0], [80, 300000000, 1], [70, 400000000, 1], [60, 500000000, 0]]) == 900000000: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 500, 0], [90, 500, 0], [80, 500, 0], [70, 500, 1], [60, 500, 1], [50, 500, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 500, 0], [90, 500, 0], [80, 500, 0], [70, 500, 1], [60, 500, 1], [50, 500, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 1, 0], [10, 2, 1], [10, 3, 0], [10, 4, 1], [10, 5, 0]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 1, 0], [10, 2, 1], [10, 3, 0], [10, 4, 1], [10, 5, 0]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1000000000, 0], [2, 500000000, 1], [3, 300000000, 0], [4, 200000000, 1], [5, 400000000, 0]]) == 1000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1000000000, 0], [2, 500000000, 1], [3, 300000000, 0], [4, 200000000, 1], [5, 400000000, 0]]) == 1000000000: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 5, 0], [101, 3, 0], [102, 2, 0], [99, 5, 1], [98, 6, 1], [97, 7, 1]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 5, 0], [101, 3, 0], [102, 2, 0], [99, 5, 1], [98, 6, 1], [97, 7, 1]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[500, 10, 0], [500, 10, 1], [500, 5, 0], [500, 5, 1], [500, 3, 0], [500, 3, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[500, 10, 0], [500, 10, 1], [500, 5, 0], [500, 5, 1], [500, 3, 0], [500, 3, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[50, 10, 0], [60, 15, 0], [70, 20, 0], [40, 5, 1], [55, 10, 1], [65, 15, 1], [50, 10, 1], [60, 15, 1], [70, 20, 1]]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[50, 10, 0], [60, 15, 0], [70, 20, 0], [40, 5, 1], [55, 10, 1], [65, 15, 1], [50, 10, 1], [60, 15, 1], [70, 20, 1]]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 1, 0], [20, 1, 1], [30, 1, 0], [40, 1, 1], [50, 1, 0], [60, 1, 1], [70, 1, 0], [80, 1, 1], [90, 1, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 1, 0], [20, 1, 1], [30, 1, 0], [40, 1, 1], [50, 1, 0], [60, 1, 1], [70, 1, 0], [80, 1, 1], [90, 1, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 10, 0], [9, 20, 0], [8, 30, 0], [7, 40, 1], [6, 50, 1], [5, 60, 1]]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 10, 0], [9, 20, 0], [8, 30, 0], [7, 40, 1], [6, 50, 1], [5, 60, 1]]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[20, 5, 0], [15, 3, 0], [10, 2, 1], [5, 1, 1], [15, 4, 0], [10, 6, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[20, 5, 0], [15, 3, 0], [10, 2, 1], [5, 1, 1], [15, 4, 0], [10, 6, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 1, 0], [200, 1, 0], [300, 1, 0], [400, 1, 0], [500, 1, 0], [150, 1, 1], [250, 1, 1], [350, 1, 1], [450, 1, 1], [550, 1, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 1, 0], [200, 1, 0], [300, 1, 0], [400, 1, 0], [500, 1, 0], [150, 1, 1], [250, 1, 1], [350, 1, 1], [450, 1, 1], [550, 1, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[999999999, 1, 0], [999999998, 2, 0], [999999997, 3, 0], [999999996, 4, 1], [999999995, 5, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[999999999, 1, 0], [999999998, 2, 0], [999999997, 3, 0], [999999996, 4, 1], [999999995, 5, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 1, 0], [10, 1, 1], [10, 1, 0], [10, 1, 1], [10, 1, 0], [10, 1, 1], [10, 1, 0], [10, 1, 1], [10, 1, 0], [10, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 1, 0], [10, 1, 1], [10, 1, 0], [10, 1, 1], [10, 1, 0], [10, 1, 1], [10, 1, 0], [10, 1, 1], [10, 1, 0], [10, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 500, 0], [90, 400, 0], [80, 300, 0], [70, 200, 1], [60, 100, 1], [50, 50, 1], [40, 50, 1], [30, 100, 1], [20, 200, 1]]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 500, 0], [90, 400, 0], [80, 300, 0], [70, 200, 1], [60, 100, 1], [50, 50, 1], [40, 50, 1], [30, 100, 1], [20, 200, 1]]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 100000, 0], [200, 200000, 0], [150, 50000, 1], [175, 75000, 1]]) == 175000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 100000, 0], [200, 200000, 0], [150, 50000, 1], [175, 75000, 1]]) == 175000: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1000000000, 1, 0], [999999999, 1, 0], [999999998, 1, 0], [999999997, 1, 0], [999999996, 1, 0], [999999995, 1, 1], [999999994, 1, 1], [999999993, 1, 1], [999999992, 1, 1], [999999991, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1000000000, 1, 0], [999999999, 1, 0], [999999998, 1, 0], [999999997, 1, 0], [999999996, 1, 0], [999999995, 1, 1], [999999994, 1, 1], [999999993, 1, 1], [999999992, 1, 1], [999999991, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1, 0], [2, 2, 0], [3, 3, 0], [4, 4, 0], [5, 5, 0], [6, 6, 0], [7, 7, 0], [8, 8, 0], [9, 9, 0], [10, 10, 0], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1], [10, 10, 1]]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1, 0], [2, 2, 0], [3, 3, 0], [4, 4, 0], [5, 5, 0], [6, 6, 0], [7, 7, 0], [8, 8, 0], [9, 9, 0], [10, 10, 0], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1], [10, 10, 1]]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[5, 10, 0], [10, 20, 0], [15, 30, 0], [20, 10, 1], [25, 20, 1], [30, 30, 1]]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[5, 10, 0], [10, 20, 0], [15, 30, 0], [20, 10, 1], [25, 20, 1], [30, 30, 1]]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 10, 0], [90, 5, 1], [80, 3, 0], [70, 2, 1], [60, 4, 0], [50, 1, 1]]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 10, 0], [90, 5, 1], [80, 3, 0], [70, 2, 1], [60, 4, 0], [50, 1, 1]]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[10, 1, 0], [20, 1, 0], [30, 1, 0], [40, 1, 0], [50, 1, 0], [10, 1, 1], [20, 1, 1], [30, 1, 1], [40, 1, 1], [50, 1, 1]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[10, 1, 0], [20, 1, 0], [30, 1, 0], [40, 1, 0], [50, 1, 0], [10, 1, 1], [20, 1, 1], [30, 1, 1], [40, 1, 1], [50, 1, 1]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1000000000, 1], [1000000000, 1, 0], [2, 1000000000, 1], [999999999, 1, 0], [3, 1000000000, 1]]) == 999999984
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1000000000, 1], [1000000000, 1, 0], [2, 1000000000, 1], [999999999, 1, 0], [3, 1000000000, 1]]) == 999999984: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 10, 0], [2, 10, 0], [3, 10, 0], [4, 10, 1], [5, 10, 1], [6, 10, 1], [7, 10, 1], [8, 10, 1], [9, 10, 1]]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 10, 0], [2, 10, 0], [3, 10, 0], [4, 10, 1], [5, 10, 1], [6, 10, 1], [7, 10, 1], [8, 10, 1], [9, 10, 1]]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 1, 0], [100, 1, 0], [100, 1, 0], [100, 1, 1], [100, 1, 1], [100, 1, 1], [100, 1, 0], [100, 1, 0], [100, 1, 0], [100, 1, 1], [100, 1, 1], [100, 1, 1], [100, 1, 0], [100, 1, 0], [100, 1, 0], [100, 1, 1], [100, 1, 1], [100, 1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 1, 0], [100, 1, 0], [100, 1, 0], [100, 1, 1], [100, 1, 1], [100, 1, 1], [100, 1, 0], [100, 1, 0], [100, 1, 0], [100, 1, 1], [100, 1, 1], [100, 1, 1], [100, 1, 0], [100, 1, 0], [100, 1, 0], [100, 1, 1], [100, 1, 1], [100, 1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[100, 10, 0], [90, 20, 0], [80, 30, 0], [70, 40, 0], [60, 50, 0], [50, 60, 1], [40, 70, 1], [30, 80, 1], [20, 90, 1], [10, 100, 1]]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[100, 10, 0], [90, 20, 0], [80, 30, 0], [70, 40, 0], [60, 50, 0], [50, 60, 1], [40, 70, 1], [30, 80, 1], [20, 90, 1], [10, 100, 1]]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1000000000, 0], [2, 1000000000, 0], [3, 1000000000, 1], [4, 1000000000, 1], [5, 1000000000, 0]]) == 999999986
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1000000000, 0], [2, 1000000000, 0], [3, 1000000000, 1], [4, 1000000000, 1], [5, 1000000000, 0]]) == 999999986: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[1, 1, 0], [2, 2, 1], [3, 3, 0], [4, 4, 1], [5, 5, 0], [6, 6, 1], [7, 7, 0], [8, 8, 1], [9, 9, 0], [10, 10, 1]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[1, 1, 0], [2, 2, 1], [3, 3, 0], [4, 4, 1], [5, 5, 0], [6, 6, 1], [7, 7, 0], [8, 8, 1], [9, 9, 0], [10, 10, 1]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(orders = [[50, 10, 0], [40, 15, 0], [30, 20, 0], [20, 25, 1], [10, 30, 1], [15, 35, 0], [25, 40, 1]]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(orders = [[50, 10, 0], [40, 15, 0], [30, 20, 0], [20, 25, 1], [10, 30, 1], [15, 35, 0], [25, 40, 1]]) == 65: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(orders = [[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]) == 999999984
    assert candidate(orders = [[1, 10, 0], [1, 10, 1], [1, 10, 0], [1, 10, 1]]) == 0
    assert candidate(orders = [[100, 1, 0], [200, 2, 0], [300, 3, 1], [400, 4, 1]]) == 10
    assert candidate(orders = [[1, 1, 0], [1, 1, 1], [1, 1, 0], [1, 1, 1]]) == 0
    assert candidate(orders = [[5, 5, 0], [5, 5, 1], [5, 5, 0], [5, 5, 1]]) == 0
    assert candidate(orders = [[100, 100, 0], [100, 100, 1], [101, 100, 0], [99, 100, 1]]) == 0
    assert candidate(orders = [[1, 10, 0], [2, 10, 0], [3, 10, 1], [4, 10, 1]]) == 40
    assert candidate(orders = [[5, 5, 0], [4, 4, 1], [3, 3, 0], [2, 2, 1], [1, 1, 0]]) == 3
    assert candidate(orders = [[100, 10, 0], [200, 15, 0], [100, 5, 1], [200, 20, 1]]) == 20
    assert candidate(orders = [[5, 5, 0], [5, 5, 1]]) == 0
    assert candidate(orders = [[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]) == 6
    assert candidate(orders = [[100, 1, 0], [99, 2, 0], [98, 3, 0], [97, 4, 1], [96, 5, 1]]) == 3
    assert candidate(orders = [[5, 10, 0], [5, 5, 1], [5, 5, 0], [5, 3, 1]]) == 7
    assert candidate(orders = [[1, 10, 0], [2, 20, 1], [3, 30, 0], [4, 40, 1]]) == 60
    assert candidate(orders = [[100, 10, 0], [99, 9, 1], [98, 8, 0], [97, 7, 1], [96, 6, 0]]) == 8
    assert candidate(orders = [[10, 10, 0], [10, 10, 0], [10, 10, 1], [10, 10, 1]]) == 0
    assert candidate(orders = [[50, 10, 0], [40, 15, 0], [30, 20, 0], [20, 25, 1], [10, 30, 1], [5, 35, 1], [3, 40, 1], [2, 45, 1], [1, 50, 1]]) == 180
    assert candidate(orders = [[10, 5, 0], [20, 5, 0], [30, 5, 0], [40, 5, 0], [10, 5, 1], [20, 5, 1], [30, 5, 1], [40, 5, 1], [5, 5, 0], [35, 5, 1]]) == 30
    assert candidate(orders = [[1, 1000000000, 0], [1, 1000000000, 0], [1, 1000000000, 1], [1, 1000000000, 1], [1, 1000000000, 0], [1, 1000000000, 1]]) == 0
    assert candidate(orders = [[1000000000, 1, 0], [1000000000, 1, 0], [1000000000, 1, 0], [1000000000, 1, 1], [1000000000, 1, 1], [1000000000, 1, 1]]) == 0
    assert candidate(orders = [[10, 5, 0], [9, 5, 0], [8, 5, 0], [7, 5, 0], [6, 5, 0], [6, 5, 1], [7, 5, 1], [8, 5, 1], [9, 5, 1], [10, 5, 1]]) == 20
    assert candidate(orders = [[1000000000, 1, 0], [999999999, 2, 0], [999999998, 3, 0], [999999997, 4, 1], [999999996, 5, 1], [999999995, 6, 1]]) == 9
    assert candidate(orders = [[1, 1000000000, 0], [1000000000, 1, 1], [2, 999999999, 0], [999999999, 2, 1], [3, 999999998, 0], [999999998, 3, 1], [4, 999999997, 0], [999999997, 4, 1]]) == 999999983
    assert candidate(orders = [[1000000000, 1, 0], [999999999, 2, 0], [999999998, 3, 0], [999999997, 4, 1], [999999996, 5, 1]]) == 3
    assert candidate(orders = [[1, 1000, 0], [2, 2000, 1], [3, 3000, 0], [4, 4000, 1], [5, 5000, 0], [6, 6000, 1], [7, 7000, 0], [8, 8000, 1], [9, 9000, 0], [10, 10000, 1]]) == 15000
    assert candidate(orders = [[1000, 1, 0], [1000, 2, 0], [1000, 3, 0], [1000, 1, 1], [1000, 2, 1], [1000, 3, 1]]) == 0
    assert candidate(orders = [[10, 100, 0], [20, 50, 1], [15, 30, 0], [25, 20, 1], [5, 10, 0], [30, 5, 1]]) == 215
    assert candidate(orders = [[100, 10, 0], [90, 5, 1], [80, 15, 0], [70, 20, 1], [60, 25, 0], [50, 30, 1]]) == 5
    assert candidate(orders = [[999999999, 50000, 0], [1, 50000, 1], [999999998, 50000, 0], [2, 50000, 1], [999999997, 50000, 0], [3, 50000, 1]]) == 0
    assert candidate(orders = [[1, 1000000000, 0], [2, 999999999, 0], [3, 999999998, 0], [4, 999999997, 0], [5, 999999996, 0], [5, 999999996, 1], [4, 999999997, 1], [3, 999999998, 1], [2, 999999999, 1], [1, 1000000000, 1]]) == 0
    assert candidate(orders = [[10, 10, 0], [20, 20, 1], [15, 15, 0], [16, 16, 1], [14, 14, 0], [17, 17, 1]]) == 92
    assert candidate(orders = [[10, 1, 0], [9, 2, 0], [8, 3, 0], [7, 4, 0], [6, 5, 1], [5, 6, 1], [4, 7, 1], [3, 8, 1], [2, 9, 1], [1, 10, 1]]) == 35
    assert candidate(orders = [[1000, 1000000, 0], [1001, 1000000, 0], [1002, 1000000, 0], [999, 1000000, 1], [998, 1000000, 1], [997, 1000000, 1]]) == 0
    assert candidate(orders = [[10, 10, 0], [20, 10, 1], [15, 10, 0], [25, 10, 1], [10, 10, 0], [20, 10, 1], [15, 10, 0], [25, 10, 1], [10, 10, 0], [20, 10, 1], [15, 10, 0], [25, 10, 1], [10, 10, 0], [20, 10, 1], [15, 10, 0], [25, 10, 1]]) == 160
    assert candidate(orders = [[1, 1000000000, 0], [2, 1000000000, 1], [3, 1000000000, 0], [4, 1000000000, 1], [5, 1000000000, 0], [6, 1000000000, 1]]) == 999999993
    assert candidate(orders = [[10, 1000, 0], [20, 1000, 0], [30, 1000, 0], [40, 1000, 1], [50, 1000, 1], [60, 1000, 1], [70, 1000, 0], [80, 1000, 1], [90, 1000, 0]]) == 5000
    assert candidate(orders = [[10, 5, 0], [20, 10, 0], [30, 15, 0], [40, 20, 0], [50, 25, 0], [10, 5, 1], [20, 10, 1], [30, 15, 1], [40, 20, 1], [50, 25, 1]]) == 60
    assert candidate(orders = [[10, 5, 0], [20, 5, 0], [30, 5, 0], [40, 5, 0], [15, 5, 1], [25, 5, 1], [35, 5, 1], [45, 5, 1]]) == 20
    assert candidate(orders = [[1, 1000000000, 0], [2, 1000000000, 0], [3, 1000000000, 0], [1, 1000000000, 1], [2, 1000000000, 1], [3, 1000000000, 1]]) == 999999993
    assert candidate(orders = [[10, 1, 0], [11, 2, 0], [12, 3, 0], [13, 4, 1], [14, 5, 1], [15, 6, 1], [16, 7, 1], [17, 8, 0], [18, 9, 0], [19, 10, 0]]) == 11
    assert candidate(orders = [[10, 1, 0], [10, 2, 0], [10, 3, 0], [10, 4, 1], [10, 5, 1], [10, 6, 1], [10, 7, 1], [10, 8, 0], [10, 9, 0], [10, 10, 0]]) == 11
    assert candidate(orders = [[5, 1, 0], [5, 2, 0], [5, 3, 0], [5, 4, 0], [5, 5, 1], [5, 4, 1], [5, 3, 1], [5, 2, 1], [5, 1, 1]]) == 5
    assert candidate(orders = [[100, 5, 0], [90, 10, 0], [80, 15, 0], [70, 20, 0], [60, 25, 0], [50, 30, 1], [40, 35, 1], [30, 40, 1], [20, 45, 1], [10, 50, 1]]) == 125
    assert candidate(orders = [[10, 1000, 0], [10, 900, 0], [10, 800, 0], [10, 700, 1], [10, 600, 1], [10, 500, 1], [10, 400, 1]]) == 500
    assert candidate(orders = [[10, 5, 0], [10, 5, 1], [10, 5, 0], [10, 5, 1], [10, 5, 0], [10, 5, 1], [10, 5, 0], [10, 5, 1]]) == 0
    assert candidate(orders = [[1, 999999999, 0], [1, 999999999, 0], [1, 999999999, 0], [1, 999999999, 0], [2, 999999999, 1], [2, 999999999, 1], [2, 999999999, 1], [2, 999999999, 1]]) == 999999943
    assert candidate(orders = [[10, 1, 0], [9, 2, 0], [8, 3, 0], [7, 4, 1], [6, 5, 1], [5, 6, 0], [4, 7, 0], [3, 8, 1], [2, 9, 1], [1, 10, 0]]) == 17
    assert candidate(orders = [[5, 100, 0], [10, 100, 1], [15, 100, 0], [20, 100, 1], [25, 100, 0], [30, 100, 1]]) == 200
    assert candidate(orders = [[10, 5, 0], [10, 5, 0], [10, 5, 0], [10, 5, 1], [10, 5, 1], [10, 5, 1], [10, 5, 0], [10, 5, 1], [10, 5, 0], [10, 5, 1]]) == 0
    assert candidate(orders = [[100, 100, 1], [90, 200, 1], [80, 300, 1], [70, 400, 0], [60, 500, 0], [50, 600, 0]]) == 2100
    assert candidate(orders = [[1000000000, 1, 0], [999999999, 1, 0], [999999998, 1, 0], [999999997, 1, 1], [999999996, 1, 1], [999999995, 1, 1]]) == 0
    assert candidate(orders = [[10, 1, 0], [20, 2, 0], [30, 3, 0], [40, 4, 0], [50, 5, 0], [10, 1, 1], [20, 2, 1], [30, 3, 1], [40, 4, 1], [50, 5, 1]]) == 12
    assert candidate(orders = [[1, 1000000000, 0], [1000000000, 1, 1], [500000000, 2, 0], [1000000000, 999999999, 1], [1, 1, 0]]) == 999999996
    assert candidate(orders = [[1, 1000000000, 0], [2, 1000000000, 1], [3, 1000000000, 0], [4, 1000000000, 1], [5, 1000000000, 0], [6, 1000000000, 1]]) == 999999993
    assert candidate(orders = [[100, 1000, 0], [999, 500, 1], [998, 750, 1], [1000, 1000, 0], [999, 250, 0]]) == 1000
    assert candidate(orders = [[100, 1, 0], [99, 2, 0], [98, 3, 0], [97, 4, 1], [96, 5, 1], [95, 6, 0], [94, 7, 1], [93, 8, 0], [92, 9, 1]]) == 5
    assert candidate(orders = [[1, 1000000000, 0], [1, 1000000000, 0], [1, 1000000000, 0], [1, 1000000000, 1], [1, 1000000000, 1], [1, 1000000000, 1]]) == 0
    assert candidate(orders = [[100, 1, 0], [99, 2, 0], [98, 3, 0], [97, 4, 1], [96, 5, 1], [95, 6, 0], [94, 7, 0], [93, 8, 1], [92, 9, 1]]) == 7
    assert candidate(orders = [[100, 100, 0], [200, 200, 0], [300, 300, 0], [400, 400, 0], [500, 500, 1], [600, 600, 1], [700, 700, 1], [800, 800, 1], [900, 900, 1], [1000, 1000, 1]]) == 5500
    assert candidate(orders = [[10, 5, 0], [20, 10, 0], [30, 15, 0], [5, 1, 1], [15, 2, 1], [25, 3, 1]]) == 24
    assert candidate(orders = [[100, 100, 0], [99, 150, 0], [98, 200, 0], [97, 250, 1], [96, 300, 1], [95, 350, 1]]) == 450
    assert candidate(orders = [[1, 1, 0], [2, 1, 0], [3, 1, 0], [4, 1, 0], [5, 1, 0], [6, 1, 0], [7, 1, 0], [8, 1, 0], [9, 1, 0], [10, 1, 0], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 1, 1], [5, 1, 1], [6, 1, 1], [7, 1, 1], [8, 1, 1], [9, 1, 1], [10, 1, 1]]) == 10
    assert candidate(orders = [[1000000000, 1, 0], [1, 1, 1], [500000000, 1, 0], [500000000, 1, 1], [1000000000, 1, 0], [1, 1, 1]]) == 0
    assert candidate(orders = [[100, 100, 0], [90, 200, 0], [80, 300, 0], [70, 400, 1], [60, 500, 1], [50, 600, 1]]) == 900
    assert candidate(orders = [[10, 1, 0], [20, 2, 0], [10, 1, 1], [20, 2, 1], [30, 3, 0], [25, 2, 1], [15, 1, 0], [5, 1, 1]]) == 1
    assert candidate(orders = [[100, 5, 0], [200, 10, 0], [150, 5, 1], [160, 5, 1], [200, 20, 0], [150, 10, 1]]) == 15
    assert candidate(orders = [[10, 10, 0], [20, 10, 0], [30, 10, 0], [40, 10, 0], [50, 10, 0], [10, 10, 1], [20, 10, 1], [30, 10, 1], [40, 10, 1], [50, 10, 1], [10, 10, 0], [20, 10, 0], [30, 10, 0], [40, 10, 0], [50, 10, 0], [10, 10, 1], [20, 10, 1], [30, 10, 1], [40, 10, 1], [50, 10, 1]]) == 60
    assert candidate(orders = [[100, 1, 0], [90, 2, 0], [80, 3, 0], [70, 4, 1], [60, 5, 1], [50, 6, 1], [40, 7, 1], [30, 8, 1], [20, 9, 1], [10, 10, 1]]) == 43
    assert candidate(orders = [[1, 1, 0], [2, 1, 0], [3, 1, 0], [4, 1, 0], [5, 1, 0], [5, 1, 1], [4, 1, 1], [3, 1, 1], [2, 1, 1], [1, 1, 1]]) == 0
    assert candidate(orders = [[1000000000, 1, 0], [999999999, 2, 0], [999999998, 3, 0], [999999997, 4, 1], [999999996, 5, 1], [999999995, 6, 0], [999999994, 7, 0], [999999993, 8, 1], [999999992, 9, 1]]) == 7
    assert candidate(orders = [[10, 100, 0], [20, 50, 0], [30, 200, 1], [15, 150, 1], [25, 100, 0], [35, 100, 1]]) == 400
    assert candidate(orders = [[1, 1, 0], [1, 1, 1], [1, 1, 0], [1, 1, 1], [1, 1, 0], [1, 1, 1]]) == 0
    assert candidate(orders = [[1, 1, 0], [2, 2, 0], [3, 3, 0], [4, 4, 0], [5, 5, 0], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1]]) == 12
    assert candidate(orders = [[100, 5, 0], [100, 5, 0], [100, 5, 1], [100, 5, 1], [100, 5, 0], [100, 5, 1]]) == 0
    assert candidate(orders = [[5, 1, 0], [6, 1, 0], [7, 1, 0], [8, 1, 0], [9, 1, 0], [10, 1, 1], [11, 1, 1], [12, 1, 1], [13, 1, 1], [14, 1, 1]]) == 10
    assert candidate(orders = [[10, 10, 0], [20, 20, 0], [30, 30, 0], [40, 40, 0], [50, 50, 0], [10, 1, 1], [20, 2, 1], [30, 3, 1], [40, 4, 1], [50, 5, 1]]) == 135
    assert candidate(orders = [[50, 10, 0], [50, 15, 0], [50, 20, 0], [50, 25, 1], [50, 30, 1], [50, 35, 1], [50, 40, 1], [50, 45, 1], [50, 50, 1]]) == 180
    assert candidate(orders = [[100, 50, 0], [100, 50, 0], [100, 50, 0], [100, 50, 1], [100, 50, 1], [100, 50, 1]]) == 0
    assert candidate(orders = [[10, 5, 0], [20, 5, 0], [30, 5, 0], [10, 5, 1], [20, 5, 1], [30, 5, 1], [15, 5, 0], [25, 5, 0], [35, 5, 0]]) == 15
    assert candidate(orders = [[10, 1, 0], [10, 1, 1], [11, 1, 0], [9, 1, 1], [12, 1, 0], [8, 1, 1], [13, 1, 0], [7, 1, 1]]) == 0
    assert candidate(orders = [[1, 1000000000, 0], [2, 1000000000, 0], [3, 1000000000, 0], [4, 1000000000, 1], [5, 1000000000, 1], [6, 1000000000, 1]]) == 999999965
    assert candidate(orders = [[10, 10, 0], [10, 10, 1], [10, 10, 0], [10, 10, 1], [10, 10, 0], [10, 10, 1], [10, 10, 0], [10, 10, 1], [10, 10, 0], [10, 10, 1]]) == 0
    assert candidate(orders = [[1, 1000000000, 0], [2, 999999999, 0], [3, 999999998, 0], [4, 999999997, 1], [5, 999999996, 1], [6, 999999995, 1], [7, 999999994, 1], [8, 999999993, 0], [9, 999999992, 0], [10, 999999991, 0]]) == 999999982
    assert candidate(orders = [[50, 10, 0], [40, 20, 0], [30, 30, 0], [20, 40, 0], [10, 50, 0], [10, 60, 1], [20, 70, 1], [30, 80, 1], [40, 90, 1], [50, 100, 1], [15, 5, 0], [25, 5, 0], [35, 5, 0], [45, 5, 0], [55, 5, 0]]) == 335
    assert candidate(orders = [[100, 10, 0], [90, 10, 0], [80, 10, 0], [70, 10, 0], [60, 10, 0], [50, 10, 1], [40, 10, 1], [30, 10, 1], [20, 10, 1], [10, 10, 1]]) == 0
    assert candidate(orders = [[10, 5, 0], [20, 5, 0], [30, 5, 0], [15, 10, 1], [25, 10, 1], [35, 10, 1], [10, 5, 0], [20, 5, 0], [30, 5, 0], [15, 10, 1], [25, 10, 1], [35, 10, 1]]) == 50
    assert candidate(orders = [[100, 100000000, 0], [90, 200000000, 0], [80, 300000000, 1], [70, 400000000, 1], [60, 500000000, 0]]) == 900000000
    assert candidate(orders = [[100, 500, 0], [90, 500, 0], [80, 500, 0], [70, 500, 1], [60, 500, 1], [50, 500, 1]]) == 0
    assert candidate(orders = [[10, 1, 0], [10, 2, 1], [10, 3, 0], [10, 4, 1], [10, 5, 0]]) == 3
    assert candidate(orders = [[1, 1000000000, 0], [2, 500000000, 1], [3, 300000000, 0], [4, 200000000, 1], [5, 400000000, 0]]) == 1000000000
    assert candidate(orders = [[100, 5, 0], [101, 3, 0], [102, 2, 0], [99, 5, 1], [98, 6, 1], [97, 7, 1]]) == 8
    assert candidate(orders = [[500, 10, 0], [500, 10, 1], [500, 5, 0], [500, 5, 1], [500, 3, 0], [500, 3, 1]]) == 0
    assert candidate(orders = [[50, 10, 0], [60, 15, 0], [70, 20, 0], [40, 5, 1], [55, 10, 1], [65, 15, 1], [50, 10, 1], [60, 15, 1], [70, 20, 1]]) == 50
    assert candidate(orders = [[10, 1, 0], [20, 1, 1], [30, 1, 0], [40, 1, 1], [50, 1, 0], [60, 1, 1], [70, 1, 0], [80, 1, 1], [90, 1, 0]]) == 1
    assert candidate(orders = [[10, 10, 0], [9, 20, 0], [8, 30, 0], [7, 40, 1], [6, 50, 1], [5, 60, 1]]) == 90
    assert candidate(orders = [[20, 5, 0], [15, 3, 0], [10, 2, 1], [5, 1, 1], [15, 4, 0], [10, 6, 1]]) == 3
    assert candidate(orders = [[100, 1, 0], [200, 1, 0], [300, 1, 0], [400, 1, 0], [500, 1, 0], [150, 1, 1], [250, 1, 1], [350, 1, 1], [450, 1, 1], [550, 1, 1]]) == 6
    assert candidate(orders = [[999999999, 1, 0], [999999998, 2, 0], [999999997, 3, 0], [999999996, 4, 1], [999999995, 5, 1]]) == 3
    assert candidate(orders = [[10, 1, 0], [10, 1, 1], [10, 1, 0], [10, 1, 1], [10, 1, 0], [10, 1, 1], [10, 1, 0], [10, 1, 1], [10, 1, 0], [10, 1, 1]]) == 0
    assert candidate(orders = [[100, 500, 0], [90, 400, 0], [80, 300, 0], [70, 200, 1], [60, 100, 1], [50, 50, 1], [40, 50, 1], [30, 100, 1], [20, 200, 1]]) == 500
    assert candidate(orders = [[100, 100000, 0], [200, 200000, 0], [150, 50000, 1], [175, 75000, 1]]) == 175000
    assert candidate(orders = [[1000000000, 1, 0], [999999999, 1, 0], [999999998, 1, 0], [999999997, 1, 0], [999999996, 1, 0], [999999995, 1, 1], [999999994, 1, 1], [999999993, 1, 1], [999999992, 1, 1], [999999991, 1, 1]]) == 0
    assert candidate(orders = [[1, 1, 0], [2, 2, 0], [3, 3, 0], [4, 4, 0], [5, 5, 0], [6, 6, 0], [7, 7, 0], [8, 8, 0], [9, 9, 0], [10, 10, 0], [1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1], [5, 5, 1], [6, 6, 1], [7, 7, 1], [8, 8, 1], [9, 9, 1], [10, 10, 1]]) == 54
    assert candidate(orders = [[5, 10, 0], [10, 20, 0], [15, 30, 0], [20, 10, 1], [25, 20, 1], [30, 30, 1]]) == 120
    assert candidate(orders = [[100, 10, 0], [90, 5, 1], [80, 3, 0], [70, 2, 1], [60, 4, 0], [50, 1, 1]]) == 9
    assert candidate(orders = [[10, 1, 0], [20, 1, 0], [30, 1, 0], [40, 1, 0], [50, 1, 0], [10, 1, 1], [20, 1, 1], [30, 1, 1], [40, 1, 1], [50, 1, 1]]) == 4
    assert candidate(orders = [[1, 1000000000, 1], [1000000000, 1, 0], [2, 1000000000, 1], [999999999, 1, 0], [3, 1000000000, 1]]) == 999999984
    assert candidate(orders = [[1, 10, 0], [2, 10, 0], [3, 10, 0], [4, 10, 1], [5, 10, 1], [6, 10, 1], [7, 10, 1], [8, 10, 1], [9, 10, 1]]) == 90
    assert candidate(orders = [[100, 1, 0], [100, 1, 0], [100, 1, 0], [100, 1, 1], [100, 1, 1], [100, 1, 1], [100, 1, 0], [100, 1, 0], [100, 1, 0], [100, 1, 1], [100, 1, 1], [100, 1, 1], [100, 1, 0], [100, 1, 0], [100, 1, 0], [100, 1, 1], [100, 1, 1], [100, 1, 1]]) == 0
    assert candidate(orders = [[100, 10, 0], [90, 20, 0], [80, 30, 0], [70, 40, 0], [60, 50, 0], [50, 60, 1], [40, 70, 1], [30, 80, 1], [20, 90, 1], [10, 100, 1]]) == 250
    assert candidate(orders = [[1, 1000000000, 0], [2, 1000000000, 0], [3, 1000000000, 1], [4, 1000000000, 1], [5, 1000000000, 0]]) == 999999986
    assert candidate(orders = [[1, 1, 0], [2, 2, 1], [3, 3, 0], [4, 4, 1], [5, 5, 0], [6, 6, 1], [7, 7, 0], [8, 8, 1], [9, 9, 0], [10, 10, 1]]) == 15
    assert candidate(orders = [[50, 10, 0], [40, 15, 0], [30, 20, 0], [20, 25, 1], [10, 30, 1], [15, 35, 0], [25, 40, 1]]) == 65


