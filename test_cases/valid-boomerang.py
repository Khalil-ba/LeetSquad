def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [1, 3]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [1, 3]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 5], [3, 9]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 5], [3, 9]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 3], [3, 2]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 3], [3, 2]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [6, 6], [7, 7]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [6, 6], [7, 7]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [3, 1]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [3, 1]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [2, 2]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [2, 2]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 1], [1, 1], [2, 1]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 1], [1, 1], [2, 1]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [1, 0]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [1, 0]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 1], [1, 2]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 1], [1, 2]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 3]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 3]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 1], [0, 2]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 1], [0, 2]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 0], [0, 0], [0, 5]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 0], [0, 0], [0, 5]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 2], [2, 1]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 2], [2, 1]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [2, 1]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [2, 1]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [20, 20], [30, 30]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [20, 20], [30, 30]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 0], [0, 0], [0, 1]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 0], [0, 0], [0, 1]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 0], [2, 1], [1, 2]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 0], [2, 1], [1, 2]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 3], [3, 4]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 3], [3, 4]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 1], [1, 1]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 1], [1, 1]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 0], [2, 0], [3, 0]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 0], [2, 0], [3, 0]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 1], [2, 2]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 1], [2, 2]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[2, 1], [1, 2], [3, 4]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[2, 1], [1, 2], [3, 4]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100, 100], [50, 50], [0, 0]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100, 100], [50, 50], [0, 0]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 4]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 4]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, -1], [0, 0], [1, 1]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, -1], [0, 0], [1, 1]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [3, 3], [2, 2]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [3, 3], [2, 2]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [1, 3]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [1, 3]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-10, 10], [0, 0], [10, -10]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-10, 10], [0, 0], [10, -10]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 4], [3, 6]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 4], [3, 6]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [3, 4], [5, 6]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [3, 4], [5, 6]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [2, 3]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [2, 3]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 1], [1, 0], [0, 0]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 1], [1, 0], [0, 0]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100, 100], [99, 99], [98, 98]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100, 100], [99, 99], [98, 98]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100, 0], [50, 50], [0, 100]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100, 0], [50, 50], [0, 100]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[50, 50], [50, 60], [60, 50]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[50, 50], [50, 60], [60, 50]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[33, 33], [66, 66], [99, 99]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[33, 33], [66, 66], [99, 99]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [15, 10], [10, 15]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [15, 10], [10, 15]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 1], [3, 4]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 1], [3, 4]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [4, 4]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [4, 4]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 3], [1, 5]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 3], [1, 5]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[50, 0], [0, 50], [25, 25]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[50, 0], [0, 50], [25, 25]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 2], [3, 6]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 2], [3, 6]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [2, 2]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [2, 2]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 100], [100, 0], [50, 50]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 100], [100, 0], [50, 50]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [4, 6], [5, 3]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [4, 6], [5, 3]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 2], [2, 1]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 2], [2, 1]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [1, 2]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [1, 2]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 1]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 1]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-1, 0], [0, 1], [1, 0]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-1, 0], [0, 1], [1, 0]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [100, 100], [50, 50]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [100, 100], [50, 50]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[50, 50], [60, 60], [70, 70]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[50, 50], [60, 60], [70, 70]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 20], [20, 30], [30, 40]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 20], [20, 30], [30, 40]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100, 100], [99, 98], [98, 97]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100, 100], [99, 98], [98, 97]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[50, 50], [50, 60], [50, 70]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[50, 50], [50, 60], [50, 70]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 100], [50, 50], [100, 0]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 100], [50, 50], [100, 0]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[2, 3], [5, 6], [8, 9]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[2, 3], [5, 6], [8, 9]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [0, 1], [1, 0]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [0, 1], [1, 0]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 0], [20, 0], [30, 0]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 0], [20, 0], [30, 0]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 1], [1, 2], [2, 3]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 1], [1, 2], [2, 3]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [0, 0]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [0, 0]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [10, 5], [15, 5]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [10, 5], [15, 5]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 100], [100, 1], [50, 50]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 100], [100, 1], [50, 50]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[99, 99], [98, 98], [97, 97]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[99, 99], [98, 98], [97, 97]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [3, 1], [2, 2]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [3, 1], [2, 2]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[2, 4], [4, 6], [6, 8]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[2, 4], [4, 6], [6, 8]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[99, 98], [98, 97], [97, 96]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[99, 98], [98, 97], [97, 96]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 100], [50, 50], [100, 0]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 100], [50, 50], [100, 0]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 20], [20, 30], [30, 30]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 20], [20, 30], [30, 30]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 3], [4, 5]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 3], [4, 5]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 1], [1, 0], [2, 1]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 1], [1, 0], [2, 1]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 0], [0, 5], [5, 5]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 0], [0, 5], [5, 5]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 20], [30, 40], [50, 60]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 20], [30, 40], [50, 60]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 3], [3, 1]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 3], [3, 1]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 0], [2, 0]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 0], [2, 0]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [10, 10], [15, 15]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [10, 10], [15, 15]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [10, 15], [20, 25]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [10, 15], [20, 25]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[2, 3], [3, 6], [5, 10]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[2, 3], [3, 6], [5, 10]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[3, 6], [6, 12], [9, 18]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[3, 6], [6, 12], [9, 18]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 20], [20, 10], [30, 0]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 20], [20, 10], [30, 0]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 3], [3, 6]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 3], [3, 6]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 2], [3, 5]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 2], [3, 5]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[33, 55], [66, 77], [99, 88]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[33, 55], [66, 77], [99, 88]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 0], [0, 1], [0, 2]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 0], [0, 1], [0, 2]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[50, 50], [51, 51], [52, 52]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[50, 50], [51, 51], [52, 52]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[2, 2], [1, 1], [3, 3]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[2, 2], [1, 1], [3, 3]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [5, 6], [6, 5]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [5, 6], [6, 5]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [15, 10], [25, 15]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [15, 10], [25, 15]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 3], [4, 6]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 3], [4, 6]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 50], [50, 0], [25, 25]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 50], [50, 0], [25, 25]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 2], [2, 4]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 2], [2, 4]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [1, 2], [3, 4]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [1, 2], [3, 4]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [4, 5], [7, 8]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [4, 5], [7, 8]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 20], [30, 40], [50, 60]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 20], [30, 40], [50, 60]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 10], [20, 30], [30, 50]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 10], [20, 30], [30, 50]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 5], [3, 4], [4, 5]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 5], [3, 4], [4, 5]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[50, 50], [50, 51], [51, 50]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[50, 50], [50, 51], [51, 50]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 100], [100, 1], [50, 50]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 100], [100, 1], [50, 50]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[10, 20], [20, 10], [30, 20]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[10, 20], [20, 10], [30, 20]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 5], [2, 3], [3, 1]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 5], [2, 3], [3, 1]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[-5, -5], [-4, -4], [-3, -3]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[-5, -5], [-4, -4], [-3, -3]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[99, 99], [50, 50], [1, 1]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[99, 99], [50, 50], [1, 1]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 3], [6, 4], [7, 5]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 3], [6, 4], [7, 5]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[5, 5], [5, 6], [6, 6]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[5, 5], [5, 6], [6, 6]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [2, 3], [4, 5]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [2, 3], [4, 5]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[2, 4], [4, 2], [0, 0]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[2, 4], [4, 2], [0, 0]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 2], [2, 3], [3, 5]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 2], [2, 3], [3, 5]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 1], [1, 100], [100, 1]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 1], [1, 100], [100, 1]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[1, 0], [0, 1], [-1, 0]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[1, 0], [0, 1], [-1, 0]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 1], [1, 0], [1, 1]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 1], [1, 0], [1, 1]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[99, 1], [100, 1], [99, 2]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[99, 1], [100, 1], [99, 2]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[3, 6], [6, 12], [9, 17]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[3, 6], [6, 12], [9, 17]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[100, 100], [0, 0], [50, 50]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[100, 100], [0, 0], [50, 50]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [50, 50], [100, 100]]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [50, 50], [100, 100]]) == False: {e}')
    
    total += 1
    try:
        result = candidate(points = [[0, 0], [2, 0], [1, 1]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[0, 0], [2, 0], [1, 1]]) == True: {e}')
    
    total += 1
    try:
        result = candidate(points = [[7, 7], [8, 9], [9, 7]]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(points = [[7, 7], [8, 9], [9, 7]]) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(points = [[1, 1], [2, 2], [1, 3]]) == True
    assert candidate(points = [[1, 1], [2, 5], [3, 9]]) == False
    assert candidate(points = [[1, 1], [2, 3], [3, 2]]) == True
    assert candidate(points = [[5, 5], [6, 6], [7, 7]]) == False
    assert candidate(points = [[1, 1], [2, 1], [3, 1]]) == False
    assert candidate(points = [[0, 0], [1, 1], [2, 2]]) == False
    assert candidate(points = [[0, 1], [1, 1], [2, 1]]) == False
    assert candidate(points = [[0, 0], [1, 1], [1, 0]]) == True
    assert candidate(points = [[0, 0], [1, 1], [1, 2]]) == True
    assert candidate(points = [[1, 1], [2, 2], [3, 3]]) == False
    assert candidate(points = [[0, 0], [0, 1], [0, 2]]) == False
    assert candidate(points = [[5, 0], [0, 0], [0, 5]]) == True
    assert candidate(points = [[0, 0], [1, 2], [2, 1]]) == True
    assert candidate(points = [[1, 1], [2, 2], [2, 1]]) == True
    assert candidate(points = [[10, 10], [20, 20], [30, 30]]) == False
    assert candidate(points = [[1, 0], [0, 0], [0, 1]]) == True
    assert candidate(points = [[1, 1], [1, 2], [1, 3]]) == False
    assert candidate(points = [[1, 0], [2, 1], [1, 2]]) == True
    assert candidate(points = [[1, 2], [2, 3], [3, 4]]) == False
    assert candidate(points = [[0, 0], [0, 1], [1, 1]]) == True
    assert candidate(points = [[1, 0], [2, 0], [3, 0]]) == False
    assert candidate(points = [[1, 1], [2, 1], [2, 2]]) == True
    assert candidate(points = [[2, 1], [1, 2], [3, 4]]) == True
    assert candidate(points = [[100, 100], [50, 50], [0, 0]]) == False
    assert candidate(points = [[1, 1], [2, 2], [3, 4]]) == True
    assert candidate(points = [[-1, -1], [0, 0], [1, 1]]) == False
    assert candidate(points = [[1, 1], [3, 3], [2, 2]]) == False
    assert candidate(points = [[1, 1], [1, 2], [1, 3]]) == False
    assert candidate(points = [[-10, 10], [0, 0], [10, -10]]) == False
    assert candidate(points = [[1, 2], [2, 4], [3, 6]]) == False
    assert candidate(points = [[1, 2], [3, 4], [5, 6]]) == False
    assert candidate(points = [[1, 1], [2, 2], [2, 3]]) == True
    assert candidate(points = [[0, 1], [1, 0], [0, 0]]) == True
    assert candidate(points = [[100, 100], [99, 99], [98, 98]]) == False
    assert candidate(points = [[100, 0], [50, 50], [0, 100]]) == False
    assert candidate(points = [[50, 50], [50, 60], [60, 50]]) == True
    assert candidate(points = [[33, 33], [66, 66], [99, 99]]) == False
    assert candidate(points = [[10, 10], [15, 10], [10, 15]]) == True
    assert candidate(points = [[1, 2], [2, 1], [3, 4]]) == True
    assert candidate(points = [[1, 1], [2, 2], [4, 4]]) == False
    assert candidate(points = [[1, 1], [2, 3], [1, 5]]) == True
    assert candidate(points = [[50, 0], [0, 50], [25, 25]]) == False
    assert candidate(points = [[0, 0], [1, 2], [3, 6]]) == False
    assert candidate(points = [[1, 1], [1, 2], [2, 2]]) == True
    assert candidate(points = [[0, 100], [100, 0], [50, 50]]) == False
    assert candidate(points = [[1, 2], [4, 6], [5, 3]]) == True
    assert candidate(points = [[1, 1], [1, 2], [2, 1]]) == True
    assert candidate(points = [[1, 1], [2, 2], [1, 2]]) == True
    assert candidate(points = [[0, 0], [1, 0], [2, 1]]) == True
    assert candidate(points = [[-1, 0], [0, 1], [1, 0]]) == True
    assert candidate(points = [[0, 0], [100, 100], [50, 50]]) == False
    assert candidate(points = [[50, 50], [60, 60], [70, 70]]) == False
    assert candidate(points = [[10, 20], [20, 30], [30, 40]]) == False
    assert candidate(points = [[100, 100], [99, 98], [98, 97]]) == True
    assert candidate(points = [[50, 50], [50, 60], [50, 70]]) == False
    assert candidate(points = [[0, 100], [50, 50], [100, 0]]) == False
    assert candidate(points = [[2, 3], [5, 6], [8, 9]]) == False
    assert candidate(points = [[0, 0], [0, 1], [1, 0]]) == True
    assert candidate(points = [[10, 0], [20, 0], [30, 0]]) == False
    assert candidate(points = [[0, 1], [1, 2], [2, 3]]) == False
    assert candidate(points = [[1, 1], [2, 2], [0, 0]]) == False
    assert candidate(points = [[5, 5], [10, 5], [15, 5]]) == False
    assert candidate(points = [[1, 100], [100, 1], [50, 50]]) == True
    assert candidate(points = [[99, 99], [98, 98], [97, 97]]) == False
    assert candidate(points = [[1, 1], [3, 1], [2, 2]]) == True
    assert candidate(points = [[2, 4], [4, 6], [6, 8]]) == False
    assert candidate(points = [[99, 98], [98, 97], [97, 96]]) == False
    assert candidate(points = [[0, 100], [50, 50], [100, 0]]) == False
    assert candidate(points = [[10, 20], [20, 30], [30, 30]]) == True
    assert candidate(points = [[1, 2], [2, 3], [4, 5]]) == False
    assert candidate(points = [[0, 1], [1, 0], [2, 1]]) == True
    assert candidate(points = [[5, 0], [0, 5], [5, 5]]) == True
    assert candidate(points = [[10, 20], [30, 40], [50, 60]]) == False
    assert candidate(points = [[1, 1], [2, 3], [3, 1]]) == True
    assert candidate(points = [[0, 0], [1, 0], [2, 0]]) == False
    assert candidate(points = [[5, 5], [10, 10], [15, 15]]) == False
    assert candidate(points = [[5, 5], [10, 15], [20, 25]]) == True
    assert candidate(points = [[2, 3], [3, 6], [5, 10]]) == True
    assert candidate(points = [[3, 6], [6, 12], [9, 18]]) == False
    assert candidate(points = [[10, 20], [20, 10], [30, 0]]) == False
    assert candidate(points = [[1, 1], [2, 3], [3, 6]]) == True
    assert candidate(points = [[1, 1], [2, 2], [3, 5]]) == True
    assert candidate(points = [[33, 55], [66, 77], [99, 88]]) == True
    assert candidate(points = [[1, 0], [0, 1], [0, 2]]) == True
    assert candidate(points = [[50, 50], [51, 51], [52, 52]]) == False
    assert candidate(points = [[2, 2], [1, 1], [3, 3]]) == False
    assert candidate(points = [[5, 5], [5, 6], [6, 5]]) == True
    assert candidate(points = [[5, 5], [15, 10], [25, 15]]) == False
    assert candidate(points = [[1, 1], [2, 3], [4, 6]]) == True
    assert candidate(points = [[0, 50], [50, 0], [25, 25]]) == False
    assert candidate(points = [[0, 0], [1, 2], [2, 4]]) == False
    assert candidate(points = [[0, 0], [1, 2], [3, 4]]) == True
    assert candidate(points = [[1, 2], [4, 5], [7, 8]]) == False
    assert candidate(points = [[10, 20], [30, 40], [50, 60]]) == False
    assert candidate(points = [[10, 10], [20, 30], [30, 50]]) == False
    assert candidate(points = [[1, 5], [3, 4], [4, 5]]) == True
    assert candidate(points = [[50, 50], [50, 51], [51, 50]]) == True
    assert candidate(points = [[1, 100], [100, 1], [50, 50]]) == True
    assert candidate(points = [[10, 20], [20, 10], [30, 20]]) == True
    assert candidate(points = [[1, 5], [2, 3], [3, 1]]) == False
    assert candidate(points = [[-5, -5], [-4, -4], [-3, -3]]) == False
    assert candidate(points = [[99, 99], [50, 50], [1, 1]]) == False
    assert candidate(points = [[5, 3], [6, 4], [7, 5]]) == False
    assert candidate(points = [[5, 5], [5, 6], [6, 6]]) == True
    assert candidate(points = [[1, 1], [2, 3], [4, 5]]) == True
    assert candidate(points = [[2, 4], [4, 2], [0, 0]]) == True
    assert candidate(points = [[1, 2], [2, 3], [3, 5]]) == True
    assert candidate(points = [[1, 1], [1, 100], [100, 1]]) == True
    assert candidate(points = [[1, 0], [0, 1], [-1, 0]]) == True
    assert candidate(points = [[0, 1], [1, 0], [1, 1]]) == True
    assert candidate(points = [[99, 1], [100, 1], [99, 2]]) == True
    assert candidate(points = [[3, 6], [6, 12], [9, 17]]) == True
    assert candidate(points = [[100, 100], [0, 0], [50, 50]]) == False
    assert candidate(points = [[0, 0], [50, 50], [100, 100]]) == False
    assert candidate(points = [[0, 0], [2, 0], [1, 1]]) == True
    assert candidate(points = [[7, 7], [8, 9], [9, 7]]) == True


