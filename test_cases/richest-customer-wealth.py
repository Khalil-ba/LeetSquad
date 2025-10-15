def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(accounts = [[10, 20, 30], [1, 2, 3], [100, 200, 300]]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[10, 20, 30], [1, 2, 3], [100, 200, 300]]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[10, 10], [20, 20], [30, 30], [40, 40]]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[10, 10], [20, 20], [30, 30], [40, 40]]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[100, 100], [50, 50, 50, 50]]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[100, 100], [50, 50, 50, 50]]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[100], [100], [100]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[100], [100], [100]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[5, 5, 5], [15], [10, 10]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[5, 5, 5], [15], [10, 10]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[10, 20, 30], [5, 15, 25], [1, 2, 3]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[10, 20, 30], [5, 15, 25], [1, 2, 3]]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[50, 50], [25, 75], [75, 25], [100]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[50, 50], [25, 75], [75, 25], [100]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[50, 50], [50, 50], [50, 50]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[50, 50], [50, 50], [50, 50]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[10, 20, 30], [5, 15, 25], [1, 2, 3, 4, 5]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[10, 20, 30], [5, 15, 25], [1, 2, 3, 4, 5]]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1, 2], [3, 4], [5, 6], [7, 8]]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1, 2], [3, 4], [5, 6], [7, 8]]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1, 5], [7, 3], [3, 5]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1, 5], [7, 3], [3, 5]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[10, 10, 10], [5, 5, 5], [1, 1, 1]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[10, 10, 10], [5, 5, 5], [1, 1, 1]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1], [2], [3]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1], [2], [3]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[100, 100], [50, 50, 50], [25, 25, 25, 25]]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[100, 100], [50, 50, 50], [25, 25, 25, 25]]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1, 2, 3], [3, 2, 1]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1, 2, 3], [3, 2, 1]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1], [2], [3], [4], [5]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1], [2], [3], [4], [5]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[45, 45, 10], [30, 30, 30], [20, 20, 20, 20], [10, 10, 10, 10, 10]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[45, 45, 10], [30, 30, 30], [20, 20, 20, 20], [10, 10, 10, 10, 10]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[10, 20], [30, 40], [50, 60], [70, 80], [90, 100]]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[10, 20], [30, 40], [50, 60], [70, 80], [90, 100]]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1, 100, 1], [10, 50, 10], [100, 1, 100], [50, 10, 50]]) == 201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1, 100, 1], [10, 50, 10], [100, 1, 100], [50, 10, 50]]) == 201: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[100, 100, 100, 100, 100], [50, 50, 50, 50], [25, 25, 25, 25, 25], [125, 125]]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[100, 100, 100, 100, 100], [50, 50, 50, 50], [25, 25, 25, 25, 25], [125, 125]]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[99, 1, 2, 3], [4, 5, 6, 99], [7, 8, 9, 10]]) == 114
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[99, 1, 2, 3], [4, 5, 6, 99], [7, 8, 9, 10]]) == 114: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[5, 5, 5, 5, 5], [1, 1, 1, 1, 100], [10, 10, 10, 10, 10], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[5, 5, 5, 5, 5], [1, 1, 1, 1, 100], [10, 10, 10, 10, 10], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]) == 104: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[10, 20, 30, 40, 50], [90, 80, 70, 60, 50], [1, 2, 3, 4, 5]]) == 350
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[10, 20, 30, 40, 50], [90, 80, 70, 60, 50], [1, 2, 3, 4, 5]]) == 350: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[50, 1, 50], [1, 50, 50], [50, 50, 1], [50, 1, 50], [1, 50, 50], [50, 50, 1]]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[50, 1, 50], [1, 50, 50], [50, 50, 1], [50, 1, 50], [1, 50, 50], [50, 50, 1]]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[10, 10, 10, 10, 10], [9, 9, 9, 9, 9, 9], [8, 8, 8, 8, 8, 8, 8], [7, 7, 7, 7, 7, 7, 7, 7]]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[10, 10, 10, 10, 10], [9, 9, 9, 9, 9, 9], [8, 8, 8, 8, 8, 8, 8], [7, 7, 7, 7, 7, 7, 7, 7]]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 2, 3, 4, 5]]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 2, 3, 4, 5]]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[99, 1, 1, 1, 1], [1, 99, 1, 1, 1], [1, 1, 99, 1, 1], [1, 1, 1, 99, 1], [1, 1, 1, 1, 99]]) == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[99, 1, 1, 1, 1], [1, 99, 1, 1, 1], [1, 1, 99, 1, 1], [1, 1, 1, 99, 1], [1, 1, 1, 1, 99]]) == 103: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[90, 5], [5, 90], [45, 55], [55, 45], [75, 25], [25, 75], [60, 40], [40, 60]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[90, 5], [5, 90], [45, 55], [55, 45], [75, 25], [25, 75], [60, 40], [40, 60]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[50, 50, 50], [25, 25, 25, 25], [100], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[50, 50, 50], [25, 25, 25, 25], [100], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[100], [100, 100], [100, 100, 100], [100, 100, 100, 100], [100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100, 100]]) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[100], [100, 100], [100, 100, 100], [100, 100, 100, 100], [100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100, 100]]) == 700: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[10, 20, 30], [50, 10, 20], [30, 30, 30], [25, 25, 25, 25]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[10, 20, 30], [50, 10, 20], [30, 30, 30], [25, 25, 25, 25]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1, 100], [100, 1], [50, 50], [25, 25, 25, 25]]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1, 100], [100, 1], [50, 50], [25, 25, 25, 25]]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[50, 100, 150, 200, 250], [1, 2, 3, 4, 5], [99, 98, 97, 96, 95], [500, 400, 300, 200, 100]]) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[50, 100, 150, 200, 250], [1, 2, 3, 4, 5], [99, 98, 97, 96, 95], [500, 400, 300, 200, 100]]) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[100, 100, 100, 100, 100], [99, 99, 99, 99, 99], [98, 98, 98, 98, 98], [97, 97, 97, 97, 97], [96, 96, 96, 96, 96]]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[100, 100, 100, 100, 100], [99, 99, 99, 99, 99], [98, 98, 98, 98, 98], [97, 97, 97, 97, 97], [96, 96, 96, 96, 96]]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[90, 10, 10], [10, 90, 10], [10, 10, 90], [30, 30, 30], [20, 20, 20, 20, 10]]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[90, 10, 10], [10, 90, 10], [10, 10, 90], [30, 30, 30], [20, 20, 20, 20, 10]]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[99, 1], [1, 99], [50, 50], [25, 25, 25, 25]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[99, 1], [1, 99], [50, 50], [25, 25, 25, 25]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[10, 20, 30], [50, 60, 70], [80, 90, 100], [10, 10, 10]]) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[10, 20, 30], [50, 60, 70], [80, 90, 100], [10, 10, 10]]) == 270: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[50, 50, 50, 50], [100, 200, 300, 400], [5, 10, 15, 20, 25]]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[50, 50, 50, 50], [100, 200, 300, 400], [5, 10, 15, 20, 25]]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[45, 45, 45, 45, 45, 45], [90, 90, 90], [22, 22, 22, 22, 22, 22, 22, 22, 22, 22]]) == 270
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[45, 45, 45, 45, 45, 45], [90, 90, 90], [22, 22, 22, 22, 22, 22, 22, 22, 22, 22]]) == 270: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40], [50, 50, 50], [60, 60, 60], [70, 70, 70], [80, 80, 80], [90, 90, 90], [100, 100, 100]]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40], [50, 50, 50], [60, 60, 60], [70, 70, 70], [80, 80, 80], [90, 90, 90], [100, 100, 100]]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[10, 20], [30, 40], [50, 60], [70, 80], [90, 100]]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[10, 20], [30, 40], [50, 60], [70, 80], [90, 100]]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[42], [42, 42], [42, 42, 42], [42, 42, 42, 42], [42, 42, 42, 42, 42]]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[42], [42, 42], [42, 42, 42], [42, 42, 42, 42], [42, 42, 42, 42, 42]]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[90, 10, 1], [1, 99, 1], [50, 50, 50], [75, 25, 0], [25, 25, 25, 25]]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[90, 10, 1], [1, 99, 1], [50, 50, 50], [75, 25, 0], [25, 25, 25, 25]]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[99, 1], [1, 99], [49, 51], [51, 49], [50, 50]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[99, 1], [1, 99], [49, 51], [51, 49], [50, 50]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[30, 20, 10], [10, 20, 30], [20, 30, 10], [30, 10, 20], [10, 30, 20]]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[30, 20, 10], [10, 20, 30], [20, 30, 10], [30, 10, 20], [10, 30, 20]]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[50, 50, 50], [50, 50, 50], [50, 50, 50], [50, 50, 50], [50, 50, 50]]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[50, 50, 50], [50, 50, 50], [50, 50, 50], [50, 50, 50], [50, 50, 50]]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[50, 50], [25, 25, 25, 25], [100, 0], [0, 100], [20, 20, 20, 20, 20]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[50, 50], [25, 25, 25, 25], [100, 0], [0, 100], [20, 20, 20, 20, 20]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[100], [200], [300], [400], [500], [600], [700], [800], [900], [1000]]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[100], [200], [300], [400], [500], [600], [700], [800], [900], [1000]]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[99, 1], [98, 2], [97, 3], [96, 4], [95, 5], [94, 6], [93, 7], [92, 8], [91, 9], [90, 10]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[99, 1], [98, 2], [97, 3], [96, 4], [95, 5], [94, 6], [93, 7], [92, 8], [91, 9], [90, 10]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[99, 1], [100, 100], [50, 50, 1], [25, 25, 25, 25]]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[99, 1], [100, 100], [50, 50, 1], [25, 25, 25, 25]]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[50], [50, 50], [50, 50, 50], [50, 50, 50, 50], [50, 50, 50, 50, 50]]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[50], [50, 50], [50, 50, 50], [50, 50, 50, 50], [50, 50, 50, 50, 50]]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1, 99], [2, 98], [3, 97], [4, 96], [5, 95]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1, 99], [2, 98], [3, 97], [4, 96], [5, 95]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[50, 50, 50], [25, 25, 25, 25], [10, 10, 10, 10, 10, 10]]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[50, 50, 50], [25, 25, 25, 25], [10, 10, 10, 10, 10, 10]]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[45, 55], [46, 54], [47, 53], [48, 52], [49, 51]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[45, 55], [46, 54], [47, 53], [48, 52], [49, 51]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [10, 9, 8, 7, 6], [6, 7, 8, 9, 10]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [10, 9, 8, 7, 6], [6, 7, 8, 9, 10]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[99, 1, 100], [100, 1, 99], [50, 50, 50]]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[99, 1, 100], [100, 1, 99], [50, 50, 50]]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[100, 100, 100, 100, 100], [90, 90, 90, 90, 90, 90], [80, 80, 80, 80, 80, 80, 80], [70, 70, 70, 70, 70, 70, 70, 70]]) == 560
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[100, 100, 100, 100, 100], [90, 90, 90, 90, 90, 90], [80, 80, 80, 80, 80, 80, 80], [70, 70, 70, 70, 70, 70, 70, 70]]) == 560: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[100, 0, 0, 0, 0], [0, 100, 0, 0, 0], [0, 0, 100, 0, 0], [0, 0, 0, 100, 0], [0, 0, 0, 0, 100]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[100, 0, 0, 0, 0], [0, 100, 0, 0, 0], [0, 0, 100, 0, 0], [0, 0, 0, 100, 0], [0, 0, 0, 0, 100]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[100, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 100, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 100, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 100, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 100, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 100, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 100, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 100, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 100, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 100]]) == 109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[100, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 100, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 100, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 100, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 100, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 100, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 100, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 100, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 100, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 100]]) == 109: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]) == 65: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[100, 200, 300, 400], [99, 88, 77, 66], [1, 2, 3, 4]]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[100, 200, 300, 400], [99, 88, 77, 66], [1, 2, 3, 4]]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[100, 100, 100, 100, 100], [99, 99, 99, 99, 99, 99], [50, 50, 50, 50, 50, 50, 50], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 594
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[100, 100, 100, 100, 100], [99, 99, 99, 99, 99, 99], [50, 50, 50, 50, 50, 50, 50], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 594: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[90, 90, 90, 90, 90], [80, 80, 80, 80, 80], [70, 70, 70, 70, 70], [60, 60, 60, 60, 60], [50, 50, 50, 50, 50]]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[90, 90, 90, 90, 90], [80, 80, 80, 80, 80], [70, 70, 70, 70, 70], [60, 60, 60, 60, 60], [50, 50, 50, 50, 50]]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 2, 3, 4, 5], [50, 40, 30, 20, 10]]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 2, 3, 4, 5], [50, 40, 30, 20, 10]]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[10, 10, 10, 10], [20, 20, 20, 20], [30, 30, 30, 30], [40, 40, 40, 40]]) == 160
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[10, 10, 10, 10], [20, 20, 20, 20], [30, 30, 30, 30], [40, 40, 40, 40]]) == 160: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[50, 50, 50], [25, 25, 25, 25, 25], [100, 0], [0, 100, 0], [33, 33, 33, 1]]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[50, 50, 50], [25, 25, 25, 25, 25], [100, 0], [0, 100, 0], [33, 33, 33, 1]]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(accounts = [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [20, 20, 20, 20, 20], [30, 30, 30, 30, 30, 30]]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(accounts = [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [20, 20, 20, 20, 20], [30, 30, 30, 30, 30, 30]]) == 180: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(accounts = [[10, 20, 30], [1, 2, 3], [100, 200, 300]]) == 600
    assert candidate(accounts = [[10, 10], [20, 20], [30, 30], [40, 40]]) == 80
    assert candidate(accounts = [[100, 100], [50, 50, 50, 50]]) == 200
    assert candidate(accounts = [[100], [100], [100]]) == 100
    assert candidate(accounts = [[5, 5, 5], [15], [10, 10]]) == 20
    assert candidate(accounts = [[10, 20, 30], [5, 15, 25], [1, 2, 3]]) == 60
    assert candidate(accounts = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) == 3
    assert candidate(accounts = [[50, 50], [25, 75], [75, 25], [100]]) == 100
    assert candidate(accounts = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]) == 25
    assert candidate(accounts = [[50, 50], [50, 50], [50, 50]]) == 100
    assert candidate(accounts = [[10, 20, 30], [5, 15, 25], [1, 2, 3, 4, 5]]) == 60
    assert candidate(accounts = [[1, 2], [3, 4], [5, 6], [7, 8]]) == 15
    assert candidate(accounts = [[1, 5], [7, 3], [3, 5]]) == 10
    assert candidate(accounts = [[10, 10, 10], [5, 5, 5], [1, 1, 1]]) == 30
    assert candidate(accounts = [[1], [2], [3]]) == 3
    assert candidate(accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
    assert candidate(accounts = [[100, 100], [50, 50, 50], [25, 25, 25, 25]]) == 200
    assert candidate(accounts = [[1, 2, 3], [3, 2, 1]]) == 6
    assert candidate(accounts = [[1], [2], [3], [4], [5]]) == 5
    assert candidate(accounts = [[45, 45, 10], [30, 30, 30], [20, 20, 20, 20], [10, 10, 10, 10, 10]]) == 100
    assert candidate(accounts = [[10, 20], [30, 40], [50, 60], [70, 80], [90, 100]]) == 190
    assert candidate(accounts = [[1, 100, 1], [10, 50, 10], [100, 1, 100], [50, 10, 50]]) == 201
    assert candidate(accounts = [[100, 100, 100, 100, 100], [50, 50, 50, 50], [25, 25, 25, 25, 25], [125, 125]]) == 500
    assert candidate(accounts = [[1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]) == 7
    assert candidate(accounts = [[99, 1, 2, 3], [4, 5, 6, 99], [7, 8, 9, 10]]) == 114
    assert candidate(accounts = [[5, 5, 5, 5, 5], [1, 1, 1, 1, 100], [10, 10, 10, 10, 10], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]) == 104
    assert candidate(accounts = [[10, 20, 30, 40, 50], [90, 80, 70, 60, 50], [1, 2, 3, 4, 5]]) == 350
    assert candidate(accounts = [[50, 1, 50], [1, 50, 50], [50, 50, 1], [50, 1, 50], [1, 50, 50], [50, 50, 1]]) == 101
    assert candidate(accounts = [[10, 10, 10, 10, 10], [9, 9, 9, 9, 9, 9], [8, 8, 8, 8, 8, 8, 8], [7, 7, 7, 7, 7, 7, 7, 7]]) == 56
    assert candidate(accounts = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]) == 150
    assert candidate(accounts = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 2, 3, 4, 5]]) == 150
    assert candidate(accounts = [[99, 1, 1, 1, 1], [1, 99, 1, 1, 1], [1, 1, 99, 1, 1], [1, 1, 1, 99, 1], [1, 1, 1, 1, 99]]) == 103
    assert candidate(accounts = [[90, 5], [5, 90], [45, 55], [55, 45], [75, 25], [25, 75], [60, 40], [40, 60]]) == 100
    assert candidate(accounts = [[50, 50, 50], [25, 25, 25, 25], [100], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 150
    assert candidate(accounts = [[100], [100, 100], [100, 100, 100], [100, 100, 100, 100], [100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100], [100, 100, 100, 100, 100, 100, 100]]) == 700
    assert candidate(accounts = [[10, 20, 30], [50, 10, 20], [30, 30, 30], [25, 25, 25, 25]]) == 100
    assert candidate(accounts = [[1, 100], [100, 1], [50, 50], [25, 25, 25, 25]]) == 101
    assert candidate(accounts = [[50, 100, 150, 200, 250], [1, 2, 3, 4, 5], [99, 98, 97, 96, 95], [500, 400, 300, 200, 100]]) == 1500
    assert candidate(accounts = [[100, 100, 100, 100, 100], [99, 99, 99, 99, 99], [98, 98, 98, 98, 98], [97, 97, 97, 97, 97], [96, 96, 96, 96, 96]]) == 500
    assert candidate(accounts = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]) == 30
    assert candidate(accounts = [[90, 10, 10], [10, 90, 10], [10, 10, 90], [30, 30, 30], [20, 20, 20, 20, 10]]) == 110
    assert candidate(accounts = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]) == 25
    assert candidate(accounts = [[99, 1], [1, 99], [50, 50], [25, 25, 25, 25]]) == 100
    assert candidate(accounts = [[10, 20, 30], [50, 60, 70], [80, 90, 100], [10, 10, 10]]) == 270
    assert candidate(accounts = [[50, 50, 50, 50], [100, 200, 300, 400], [5, 10, 15, 20, 25]]) == 1000
    assert candidate(accounts = [[45, 45, 45, 45, 45, 45], [90, 90, 90], [22, 22, 22, 22, 22, 22, 22, 22, 22, 22]]) == 270
    assert candidate(accounts = [[10, 10, 10], [20, 20, 20], [30, 30, 30], [40, 40, 40], [50, 50, 50], [60, 60, 60], [70, 70, 70], [80, 80, 80], [90, 90, 90], [100, 100, 100]]) == 300
    assert candidate(accounts = [[10, 20], [30, 40], [50, 60], [70, 80], [90, 100]]) == 190
    assert candidate(accounts = [[42], [42, 42], [42, 42, 42], [42, 42, 42, 42], [42, 42, 42, 42, 42]]) == 210
    assert candidate(accounts = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]) == 30
    assert candidate(accounts = [[90, 10, 1], [1, 99, 1], [50, 50, 50], [75, 25, 0], [25, 25, 25, 25]]) == 150
    assert candidate(accounts = [[99, 1], [1, 99], [49, 51], [51, 49], [50, 50]]) == 100
    assert candidate(accounts = [[30, 20, 10], [10, 20, 30], [20, 30, 10], [30, 10, 20], [10, 30, 20]]) == 60
    assert candidate(accounts = [[50, 50, 50], [50, 50, 50], [50, 50, 50], [50, 50, 50], [50, 50, 50]]) == 150
    assert candidate(accounts = [[50, 50], [25, 25, 25, 25], [100, 0], [0, 100], [20, 20, 20, 20, 20]]) == 100
    assert candidate(accounts = [[100], [200], [300], [400], [500], [600], [700], [800], [900], [1000]]) == 1000
    assert candidate(accounts = [[99, 1], [98, 2], [97, 3], [96, 4], [95, 5], [94, 6], [93, 7], [92, 8], [91, 9], [90, 10]]) == 100
    assert candidate(accounts = [[99, 1], [100, 100], [50, 50, 1], [25, 25, 25, 25]]) == 200
    assert candidate(accounts = [[50], [50, 50], [50, 50, 50], [50, 50, 50, 50], [50, 50, 50, 50, 50]]) == 250
    assert candidate(accounts = [[5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]) == 90
    assert candidate(accounts = [[1, 99], [2, 98], [3, 97], [4, 96], [5, 95]]) == 100
    assert candidate(accounts = [[50, 50, 50], [25, 25, 25, 25], [10, 10, 10, 10, 10, 10]]) == 150
    assert candidate(accounts = [[45, 55], [46, 54], [47, 53], [48, 52], [49, 51]]) == 100
    assert candidate(accounts = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [10, 9, 8, 7, 6], [6, 7, 8, 9, 10]]) == 40
    assert candidate(accounts = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]) == 55
    assert candidate(accounts = [[99, 1, 100], [100, 1, 99], [50, 50, 50]]) == 200
    assert candidate(accounts = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]]) == 55
    assert candidate(accounts = [[100, 100, 100, 100, 100], [90, 90, 90, 90, 90, 90], [80, 80, 80, 80, 80, 80, 80], [70, 70, 70, 70, 70, 70, 70, 70]]) == 560
    assert candidate(accounts = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]]) == 120
    assert candidate(accounts = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]]) == 500
    assert candidate(accounts = [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 10
    assert candidate(accounts = [[100, 0, 0, 0, 0], [0, 100, 0, 0, 0], [0, 0, 100, 0, 0], [0, 0, 0, 100, 0], [0, 0, 0, 0, 100]]) == 100
    assert candidate(accounts = [[100, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 100, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 100, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 100, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 100, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 100, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 100, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 100, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 100, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 100]]) == 109
    assert candidate(accounts = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14, 15]]) == 65
    assert candidate(accounts = [[100, 200, 300, 400], [99, 88, 77, 66], [1, 2, 3, 4]]) == 1000
    assert candidate(accounts = [[100, 100, 100, 100, 100], [99, 99, 99, 99, 99, 99], [50, 50, 50, 50, 50, 50, 50], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 594
    assert candidate(accounts = [[90, 90, 90, 90, 90], [80, 80, 80, 80, 80], [70, 70, 70, 70, 70], [60, 60, 60, 60, 60], [50, 50, 50, 50, 50]]) == 450
    assert candidate(accounts = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]]) == 20
    assert candidate(accounts = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]) == 40
    assert candidate(accounts = [[10, 20, 30, 40, 50], [5, 15, 25, 35, 45], [1, 2, 3, 4, 5], [50, 40, 30, 20, 10]]) == 150
    assert candidate(accounts = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]]) == 100
    assert candidate(accounts = [[10, 10, 10, 10], [20, 20, 20, 20], [30, 30, 30, 30], [40, 40, 40, 40]]) == 160
    assert candidate(accounts = [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [5, 5, 5, 5, 5, 5, 5, 5, 5, 5], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == 100
    assert candidate(accounts = [[50, 50, 50], [25, 25, 25, 25, 25], [100, 0], [0, 100, 0], [33, 33, 33, 1]]) == 150
    assert candidate(accounts = [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10], [20, 20, 20, 20, 20], [30, 30, 30, 30, 30, 30]]) == 180


