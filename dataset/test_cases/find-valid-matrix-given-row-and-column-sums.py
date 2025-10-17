def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(rowSum = [10, 15],colSum = [12, 13]) == [[10, 0], [2, 13]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [10, 15],colSum = [12, 13]) == [[10, 0], [2, 13]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [5, 5, 5],colSum = [5, 5, 5]) == [[5, 0, 0], [0, 5, 0], [0, 0, 5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [5, 5, 5],colSum = [5, 5, 5]) == [[5, 0, 0], [0, 5, 0], [0, 0, 5]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [10, 20],colSum = [15, 15]) == [[10, 0], [5, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [10, 20],colSum = [15, 15]) == [[10, 0], [5, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [10, 15, 20],colSum = [15, 15, 15]) == [[10, 0, 0], [5, 10, 0], [0, 5, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [10, 15, 20],colSum = [15, 15, 15]) == [[10, 0, 0], [5, 10, 0], [0, 5, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [1, 2, 3, 4],colSum = [1, 2, 3, 4]) == [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [1, 2, 3, 4],colSum = [1, 2, 3, 4]) == [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [1, 1, 1],colSum = [1, 1, 1]) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [1, 1, 1],colSum = [1, 1, 1]) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [5, 7, 10],colSum = [8, 6, 8]) == [[5, 0, 0], [3, 4, 0], [0, 2, 8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [5, 7, 10],colSum = [8, 6, 8]) == [[5, 0, 0], [3, 4, 0], [0, 2, 8]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [10, 15, 20],colSum = [5, 10, 20]) == [[5, 5, 0], [0, 5, 10], [0, 0, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [10, 15, 20],colSum = [5, 10, 20]) == [[5, 5, 0], [0, 5, 10], [0, 0, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [0, 0],colSum = [0, 0]) == [[0, 0], [0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [0, 0],colSum = [0, 0]) == [[0, 0], [0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [1, 2],colSum = [3, 0]) == [[1, 0], [2, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [1, 2],colSum = [3, 0]) == [[1, 0], [2, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [1, 2, 3],colSum = [3, 2, 1]) == [[1, 0, 0], [2, 0, 0], [0, 2, 1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [1, 2, 3],colSum = [3, 2, 1]) == [[1, 0, 0], [2, 0, 0], [0, 2, 1]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [0, 0, 0],colSum = [0, 0, 0]) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [0, 0, 0],colSum = [0, 0, 0]) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [3, 8],colSum = [4, 7]) == [[3, 0], [1, 7]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [3, 8],colSum = [4, 7]) == [[3, 0], [1, 7]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [25, 25, 25, 25, 25],colSum = [25, 25, 25, 25, 25]) == [[25, 0, 0, 0, 0], [0, 25, 0, 0, 0], [0, 0, 25, 0, 0], [0, 0, 0, 25, 0], [0, 0, 0, 0, 25]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [25, 25, 25, 25, 25],colSum = [25, 25, 25, 25, 25]) == [[25, 0, 0, 0, 0], [0, 25, 0, 0, 0], [0, 0, 25, 0, 0], [0, 0, 0, 25, 0], [0, 0, 0, 0, 25]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [9, 18, 27, 36, 45],colSum = [5, 10, 15, 20, 25]) == [[5, 4, 0, 0, 0], [0, 6, 12, 0, 0], [0, 0, 3, 20, 4], [0, 0, 0, 0, 21], [0, 0, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [9, 18, 27, 36, 45],colSum = [5, 10, 15, 20, 25]) == [[5, 4, 0, 0, 0], [0, 6, 12, 0, 0], [0, 0, 3, 20, 4], [0, 0, 0, 0, 21], [0, 0, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [10, 20, 30],colSum = [6, 9, 12, 15]) == [[6, 4, 0, 0], [0, 5, 12, 3], [0, 0, 0, 12]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [10, 20, 30],colSum = [6, 9, 12, 15]) == [[6, 4, 0, 0], [0, 5, 12, 3], [0, 0, 0, 12]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [5, 5, 5, 5],colSum = [4, 4, 4, 4]) == [[4, 1, 0, 0], [0, 3, 2, 0], [0, 0, 2, 3], [0, 0, 0, 1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [5, 5, 5, 5],colSum = [4, 4, 4, 4]) == [[4, 1, 0, 0], [0, 3, 2, 0], [0, 0, 2, 3], [0, 0, 0, 1]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [10, 20, 30],colSum = [6, 15, 29]) == [[6, 4, 0], [0, 11, 9], [0, 0, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [10, 20, 30],colSum = [6, 15, 29]) == [[6, 4, 0], [0, 11, 9], [0, 0, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [300, 400, 500, 600],colSum = [200, 300, 400, 700]) == [[200, 100, 0, 0], [0, 200, 200, 0], [0, 0, 200, 300], [0, 0, 0, 400]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [300, 400, 500, 600],colSum = [200, 300, 400, 700]) == [[200, 100, 0, 0], [0, 200, 200, 0], [0, 0, 200, 300], [0, 0, 0, 400]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [12, 25, 30],colSum = [20, 15, 20]) == [[12, 0, 0], [8, 15, 2], [0, 0, 18]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [12, 25, 30],colSum = [20, 15, 20]) == [[12, 0, 0], [8, 15, 2], [0, 0, 18]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [12, 15, 20],colSum = [10, 10, 17]) == [[10, 2, 0], [0, 8, 7], [0, 0, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [12, 15, 20],colSum = [10, 10, 17]) == [[10, 2, 0], [0, 8, 7], [0, 0, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [1000, 2000, 3000],colSum = [1500, 2000, 2500]) == [[1000, 0, 0], [500, 1500, 0], [0, 500, 2500]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [1000, 2000, 3000],colSum = [1500, 2000, 2500]) == [[1000, 0, 0], [500, 1500, 0], [0, 500, 2500]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [9, 18, 27],colSum = [12, 15, 18]) == [[9, 0, 0], [3, 15, 0], [0, 0, 18]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [9, 18, 27],colSum = [12, 15, 18]) == [[9, 0, 0], [3, 15, 0], [0, 0, 18]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [100, 100, 100, 100],colSum = [25, 25, 25, 25]) == [[25, 25, 25, 25], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [100, 100, 100, 100],colSum = [25, 25, 25, 25]) == [[25, 25, 25, 25], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [45, 55, 65, 75, 85],colSum = [50, 60, 70, 80, 90]) == [[45, 0, 0, 0, 0], [5, 50, 0, 0, 0], [0, 10, 55, 0, 0], [0, 0, 15, 60, 0], [0, 0, 0, 20, 65]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [45, 55, 65, 75, 85],colSum = [50, 60, 70, 80, 90]) == [[45, 0, 0, 0, 0], [5, 50, 0, 0, 0], [0, 10, 55, 0, 0], [0, 0, 15, 60, 0], [0, 0, 0, 20, 65]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [99, 100, 101, 102],colSum = [101, 102, 99, 100]) == [[99, 0, 0, 0], [2, 98, 0, 0], [0, 4, 97, 0], [0, 0, 2, 100]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [99, 100, 101, 102],colSum = [101, 102, 99, 100]) == [[99, 0, 0, 0], [2, 98, 0, 0], [0, 4, 97, 0], [0, 0, 2, 100]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [50, 100, 150],colSum = [25, 75, 100, 150]) == [[25, 25, 0, 0], [0, 50, 50, 0], [0, 0, 50, 100]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [50, 100, 150],colSum = [25, 75, 100, 150]) == [[25, 25, 0, 0], [0, 50, 50, 0], [0, 0, 50, 100]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [25, 50, 75, 100],colSum = [10, 20, 30, 40, 95]) == [[10, 15, 0, 0, 0], [0, 5, 30, 15, 0], [0, 0, 0, 25, 50], [0, 0, 0, 0, 45]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [25, 50, 75, 100],colSum = [10, 20, 30, 40, 95]) == [[10, 15, 0, 0, 0], [0, 5, 30, 15, 0], [0, 0, 0, 25, 50], [0, 0, 0, 0, 45]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [100, 150, 200, 250],colSum = [100, 100, 150, 200]) == [[100, 0, 0, 0], [0, 100, 50, 0], [0, 0, 100, 100], [0, 0, 0, 100]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [100, 150, 200, 250],colSum = [100, 100, 150, 200]) == [[100, 0, 0, 0], [0, 100, 50, 0], [0, 0, 100, 100], [0, 0, 0, 100]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [45, 55, 65, 75, 85],colSum = [30, 40, 50, 60, 70]) == [[30, 15, 0, 0, 0], [0, 25, 30, 0, 0], [0, 0, 20, 45, 0], [0, 0, 0, 15, 60], [0, 0, 0, 0, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [45, 55, 65, 75, 85],colSum = [30, 40, 50, 60, 70]) == [[30, 15, 0, 0, 0], [0, 25, 30, 0, 0], [0, 0, 20, 45, 0], [0, 0, 0, 15, 60], [0, 0, 0, 0, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [100, 200, 300, 400],colSum = [150, 250, 350, 450]) == [[100, 0, 0, 0], [50, 150, 0, 0], [0, 100, 200, 0], [0, 0, 150, 250]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [100, 200, 300, 400],colSum = [150, 250, 350, 450]) == [[100, 0, 0, 0], [50, 150, 0, 0], [0, 100, 200, 0], [0, 0, 150, 250]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [300, 200, 100, 50],colSum = [150, 150, 150, 100, 50]) == [[150, 150, 0, 0, 0], [0, 0, 150, 50, 0], [0, 0, 0, 50, 50], [0, 0, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [300, 200, 100, 50],colSum = [150, 150, 150, 100, 50]) == [[150, 150, 0, 0, 0], [0, 0, 150, 50, 0], [0, 0, 0, 50, 50], [0, 0, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [20, 30, 40, 50],colSum = [10, 20, 30, 40]) == [[10, 10, 0, 0], [0, 10, 20, 0], [0, 0, 10, 30], [0, 0, 0, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [20, 30, 40, 50],colSum = [10, 20, 30, 40]) == [[10, 10, 0, 0], [0, 10, 20, 0], [0, 0, 10, 30], [0, 0, 0, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],colSum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],colSum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [100, 200, 300],colSum = [150, 100, 250]) == [[100, 0, 0], [50, 100, 50], [0, 0, 200]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [100, 200, 300],colSum = [150, 100, 250]) == [[100, 0, 0], [50, 100, 50], [0, 0, 200]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [50, 50, 50],colSum = [40, 40, 40, 40]) == [[40, 10, 0, 0], [0, 30, 20, 0], [0, 0, 20, 30]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [50, 50, 50],colSum = [40, 40, 40, 40]) == [[40, 10, 0, 0], [0, 30, 20, 0], [0, 0, 20, 30]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [10, 20, 30, 40, 50],colSum = [15, 15, 15, 15, 15]) == [[10, 0, 0, 0, 0], [5, 15, 0, 0, 0], [0, 0, 15, 15, 0], [0, 0, 0, 0, 15], [0, 0, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [10, 20, 30, 40, 50],colSum = [15, 15, 15, 15, 15]) == [[10, 0, 0, 0, 0], [5, 15, 0, 0, 0], [0, 0, 15, 15, 0], [0, 0, 0, 0, 15], [0, 0, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [500, 500, 500, 500, 500],colSum = [250, 250, 250, 250, 250]) == [[250, 250, 0, 0, 0], [0, 0, 250, 250, 0], [0, 0, 0, 0, 250], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [500, 500, 500, 500, 500],colSum = [250, 250, 250, 250, 250]) == [[250, 250, 0, 0, 0], [0, 0, 250, 250, 0], [0, 0, 0, 0, 250], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [5, 6, 7, 8],colSum = [10, 8, 6, 4]) == [[5, 0, 0, 0], [5, 1, 0, 0], [0, 7, 0, 0], [0, 0, 6, 2]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [5, 6, 7, 8],colSum = [10, 8, 6, 4]) == [[5, 0, 0, 0], [5, 1, 0, 0], [0, 7, 0, 0], [0, 0, 6, 2]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [100, 200, 300],colSum = [150, 250, 100]) == [[100, 0, 0], [50, 150, 0], [0, 100, 100]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [100, 200, 300],colSum = [150, 250, 100]) == [[100, 0, 0], [50, 150, 0], [0, 100, 100]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [25, 50, 75, 100],colSum = [40, 50, 60, 50]) == [[25, 0, 0, 0], [15, 35, 0, 0], [0, 15, 60, 0], [0, 0, 0, 50]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [25, 50, 75, 100],colSum = [40, 50, 60, 50]) == [[25, 0, 0, 0], [15, 35, 0, 0], [0, 15, 60, 0], [0, 0, 0, 50]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [10, 20, 30, 40, 50],colSum = [50, 40, 30, 20, 10]) == [[10, 0, 0, 0, 0], [20, 0, 0, 0, 0], [20, 10, 0, 0, 0], [0, 30, 10, 0, 0], [0, 0, 20, 20, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [10, 20, 30, 40, 50],colSum = [50, 40, 30, 20, 10]) == [[10, 0, 0, 0, 0], [20, 0, 0, 0, 0], [20, 10, 0, 0, 0], [0, 30, 10, 0, 0], [0, 0, 20, 20, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [500, 300, 200],colSum = [400, 350, 250]) == [[400, 100, 0], [0, 250, 50], [0, 0, 200]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [500, 300, 200],colSum = [400, 350, 250]) == [[400, 100, 0], [0, 250, 50], [0, 0, 200]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [50, 75, 100],colSum = [120, 100, 30]) == [[50, 0, 0], [70, 5, 0], [0, 95, 5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [50, 75, 100],colSum = [120, 100, 30]) == [[50, 0, 0], [70, 5, 0], [0, 95, 5]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [8, 16, 24, 32],colSum = [16, 24, 16, 24]) == [[8, 0, 0, 0], [8, 8, 0, 0], [0, 16, 8, 0], [0, 0, 8, 24]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [8, 16, 24, 32],colSum = [16, 24, 16, 24]) == [[8, 0, 0, 0], [8, 8, 0, 0], [0, 16, 8, 0], [0, 0, 8, 24]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [8, 6, 4, 2, 0],colSum = [1, 2, 3, 4, 5]) == [[1, 2, 3, 2, 0], [0, 0, 0, 2, 4], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [8, 6, 4, 2, 0],colSum = [1, 2, 3, 4, 5]) == [[1, 2, 3, 2, 0], [0, 0, 0, 2, 4], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [88, 77, 66, 55, 44],colSum = [99, 88, 77, 66, 55]) == [[88, 0, 0, 0, 0], [11, 66, 0, 0, 0], [0, 22, 44, 0, 0], [0, 0, 33, 22, 0], [0, 0, 0, 44, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [88, 77, 66, 55, 44],colSum = [99, 88, 77, 66, 55]) == [[88, 0, 0, 0, 0], [11, 66, 0, 0, 0], [0, 22, 44, 0, 0], [0, 0, 33, 22, 0], [0, 0, 0, 44, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [150, 200, 250],colSum = [200, 150, 300]) == [[150, 0, 0], [50, 150, 0], [0, 0, 250]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [150, 200, 250],colSum = [200, 150, 300]) == [[150, 0, 0], [50, 150, 0], [0, 0, 250]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [88, 88, 88, 88, 88, 88],colSum = [77, 77, 77, 77, 77, 77]) == [[77, 11, 0, 0, 0, 0], [0, 66, 22, 0, 0, 0], [0, 0, 55, 33, 0, 0], [0, 0, 0, 44, 44, 0], [0, 0, 0, 0, 33, 55], [0, 0, 0, 0, 0, 22]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [88, 88, 88, 88, 88, 88],colSum = [77, 77, 77, 77, 77, 77]) == [[77, 11, 0, 0, 0, 0], [0, 66, 22, 0, 0, 0], [0, 0, 55, 33, 0, 0], [0, 0, 0, 44, 44, 0], [0, 0, 0, 0, 33, 55], [0, 0, 0, 0, 0, 22]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [120, 110, 100, 90],colSum = [105, 95, 85, 75]) == [[105, 15, 0, 0], [0, 80, 30, 0], [0, 0, 55, 45], [0, 0, 0, 30]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [120, 110, 100, 90],colSum = [105, 95, 85, 75]) == [[105, 15, 0, 0], [0, 80, 30, 0], [0, 0, 55, 45], [0, 0, 0, 30]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [50, 60, 70, 80, 90],colSum = [90, 80, 70, 60, 50]) == [[50, 0, 0, 0, 0], [40, 20, 0, 0, 0], [0, 60, 10, 0, 0], [0, 0, 60, 20, 0], [0, 0, 0, 40, 50]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [50, 60, 70, 80, 90],colSum = [90, 80, 70, 60, 50]) == [[50, 0, 0, 0, 0], [40, 20, 0, 0, 0], [0, 60, 10, 0, 0], [0, 0, 60, 20, 0], [0, 0, 0, 40, 50]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [123, 456, 789],colSum = [456, 789, 123]) == [[123, 0, 0], [333, 123, 0], [0, 666, 123]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [123, 456, 789],colSum = [456, 789, 123]) == [[123, 0, 0], [333, 123, 0], [0, 666, 123]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [10, 20, 30, 40, 50],colSum = [5, 10, 15, 20, 60]) == [[5, 5, 0, 0, 0], [0, 5, 15, 0, 0], [0, 0, 0, 20, 10], [0, 0, 0, 0, 40], [0, 0, 0, 0, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [10, 20, 30, 40, 50],colSum = [5, 10, 15, 20, 60]) == [[5, 5, 0, 0, 0], [0, 5, 15, 0, 0], [0, 0, 0, 20, 10], [0, 0, 0, 0, 40], [0, 0, 0, 0, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [8, 16, 24, 32],colSum = [16, 24, 32, 8]) == [[8, 0, 0, 0], [8, 8, 0, 0], [0, 16, 8, 0], [0, 0, 24, 8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [8, 16, 24, 32],colSum = [16, 24, 32, 8]) == [[8, 0, 0, 0], [8, 8, 0, 0], [0, 16, 8, 0], [0, 0, 24, 8]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [100, 200, 300, 400],colSum = [200, 300, 200, 400]) == [[100, 0, 0, 0], [100, 100, 0, 0], [0, 200, 100, 0], [0, 0, 100, 300]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [100, 200, 300, 400],colSum = [200, 300, 200, 400]) == [[100, 0, 0, 0], [100, 100, 0, 0], [0, 200, 100, 0], [0, 0, 100, 300]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [120, 80, 40],colSum = [90, 70, 30, 10]) == [[90, 30, 0, 0], [0, 40, 30, 10], [0, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [120, 80, 40],colSum = [90, 70, 30, 10]) == [[90, 30, 0, 0], [0, 40, 30, 10], [0, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [10, 20, 30, 40],colSum = [15, 25, 25, 25]) == [[10, 0, 0, 0], [5, 15, 0, 0], [0, 10, 20, 0], [0, 0, 5, 25]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [10, 20, 30, 40],colSum = [15, 25, 25, 25]) == [[10, 0, 0, 0], [5, 15, 0, 0], [0, 10, 20, 0], [0, 0, 5, 25]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [99, 98, 97, 96, 95],colSum = [95, 96, 97, 98, 99]) == [[95, 4, 0, 0, 0], [0, 92, 6, 0, 0], [0, 0, 91, 6, 0], [0, 0, 0, 92, 4], [0, 0, 0, 0, 95]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [99, 98, 97, 96, 95],colSum = [95, 96, 97, 98, 99]) == [[95, 4, 0, 0, 0], [0, 92, 6, 0, 0], [0, 0, 91, 6, 0], [0, 0, 0, 92, 4], [0, 0, 0, 0, 95]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [15, 25, 35, 45],colSum = [10, 20, 30, 40]) == [[10, 5, 0, 0], [0, 15, 10, 0], [0, 0, 20, 15], [0, 0, 0, 25]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [15, 25, 35, 45],colSum = [10, 20, 30, 40]) == [[10, 5, 0, 0], [0, 15, 10, 0], [0, 0, 20, 15], [0, 0, 0, 25]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [75, 80, 85, 90, 95, 100],colSum = [60, 65, 70, 75, 80, 85]) == [[60, 15, 0, 0, 0, 0], [0, 50, 30, 0, 0, 0], [0, 0, 40, 45, 0, 0], [0, 0, 0, 30, 60, 0], [0, 0, 0, 0, 20, 75], [0, 0, 0, 0, 0, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [75, 80, 85, 90, 95, 100],colSum = [60, 65, 70, 75, 80, 85]) == [[60, 15, 0, 0, 0, 0], [0, 50, 30, 0, 0, 0], [0, 0, 40, 45, 0, 0], [0, 0, 0, 30, 60, 0], [0, 0, 0, 0, 20, 75], [0, 0, 0, 0, 0, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [100, 150, 200],colSum = [200, 120, 130]) == [[100, 0, 0], [100, 50, 0], [0, 70, 130]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [100, 150, 200],colSum = [200, 120, 130]) == [[100, 0, 0], [100, 50, 0], [0, 70, 130]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [120, 140, 160, 180, 200],colSum = [200, 180, 160, 140, 120]) == [[120, 0, 0, 0, 0], [80, 60, 0, 0, 0], [0, 120, 40, 0, 0], [0, 0, 120, 60, 0], [0, 0, 0, 80, 120]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [120, 140, 160, 180, 200],colSum = [200, 180, 160, 140, 120]) == [[120, 0, 0, 0, 0], [80, 60, 0, 0, 0], [0, 120, 40, 0, 0], [0, 0, 120, 60, 0], [0, 0, 0, 80, 120]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [50, 60, 70, 80],colSum = [30, 40, 50, 60]) == [[30, 20, 0, 0], [0, 20, 40, 0], [0, 0, 10, 60], [0, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [50, 60, 70, 80],colSum = [30, 40, 50, 60]) == [[30, 20, 0, 0], [0, 20, 40, 0], [0, 0, 10, 60], [0, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [30, 20, 10, 0],colSum = [10, 10, 10, 30]) == [[10, 10, 10, 0], [0, 0, 0, 20], [0, 0, 0, 10], [0, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [30, 20, 10, 0],colSum = [10, 10, 10, 30]) == [[10, 10, 10, 0], [0, 0, 0, 20], [0, 0, 0, 10], [0, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [5, 10, 15, 20, 25],colSum = [25, 20, 15, 10, 5]) == [[5, 0, 0, 0, 0], [10, 0, 0, 0, 0], [10, 5, 0, 0, 0], [0, 15, 5, 0, 0], [0, 0, 10, 10, 5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [5, 10, 15, 20, 25],colSum = [25, 20, 15, 10, 5]) == [[5, 0, 0, 0, 0], [10, 0, 0, 0, 0], [10, 5, 0, 0, 0], [0, 15, 5, 0, 0], [0, 0, 10, 10, 5]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [20, 40, 60, 80],colSum = [30, 30, 30, 30]) == [[20, 0, 0, 0], [10, 30, 0, 0], [0, 0, 30, 30], [0, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [20, 40, 60, 80],colSum = [30, 30, 30, 30]) == [[20, 0, 0, 0], [10, 30, 0, 0], [0, 0, 30, 30], [0, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [1, 1, 1, 1, 1, 1],colSum = [1, 1, 1, 1, 1, 1]) == [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [1, 1, 1, 1, 1, 1],colSum = [1, 1, 1, 1, 1, 1]) == [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [50, 45, 60],colSum = [40, 30, 35]) == [[40, 10, 0], [0, 20, 25], [0, 0, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [50, 45, 60],colSum = [40, 30, 35]) == [[40, 10, 0], [0, 20, 25], [0, 0, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [123, 456, 789],colSum = [321, 654, 987]) == [[123, 0, 0], [198, 258, 0], [0, 396, 393]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [123, 456, 789],colSum = [321, 654, 987]) == [[123, 0, 0], [198, 258, 0], [0, 396, 393]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [100, 200, 300],colSum = [150, 150, 150]) == [[100, 0, 0], [50, 150, 0], [0, 0, 150]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [100, 200, 300],colSum = [150, 150, 150]) == [[100, 0, 0], [50, 150, 0], [0, 0, 150]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [30, 40, 50, 60],colSum = [50, 40, 40, 30]) == [[30, 0, 0, 0], [20, 20, 0, 0], [0, 20, 30, 0], [0, 0, 10, 30]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [30, 40, 50, 60],colSum = [50, 40, 40, 30]) == [[30, 0, 0, 0], [20, 20, 0, 0], [0, 20, 30, 0], [0, 0, 10, 30]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [1, 2, 3, 4, 5],colSum = [5, 4, 3, 2, 1]) == [[1, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 1, 0, 0, 0], [0, 3, 1, 0, 0], [0, 0, 2, 2, 1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [1, 2, 3, 4, 5],colSum = [5, 4, 3, 2, 1]) == [[1, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 1, 0, 0, 0], [0, 3, 1, 0, 0], [0, 0, 2, 2, 1]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [30, 20, 10],colSum = [15, 20, 15]) == [[15, 15, 0], [0, 5, 15], [0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [30, 20, 10],colSum = [15, 20, 15]) == [[15, 15, 0], [0, 5, 15], [0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [20, 30, 40, 50],colSum = [15, 15, 15, 15, 20, 10]) == [[15, 5, 0, 0, 0, 0], [0, 10, 15, 5, 0, 0], [0, 0, 0, 10, 20, 10], [0, 0, 0, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [20, 30, 40, 50],colSum = [15, 15, 15, 15, 20, 10]) == [[15, 5, 0, 0, 0, 0], [0, 10, 15, 5, 0, 0], [0, 0, 0, 10, 20, 10], [0, 0, 0, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [150, 200, 250, 300, 350, 400],colSum = [200, 250, 300, 350, 400, 450]) == [[150, 0, 0, 0, 0, 0], [50, 150, 0, 0, 0, 0], [0, 100, 150, 0, 0, 0], [0, 0, 150, 150, 0, 0], [0, 0, 0, 200, 150, 0], [0, 0, 0, 0, 250, 150]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [150, 200, 250, 300, 350, 400],colSum = [200, 250, 300, 350, 400, 450]) == [[150, 0, 0, 0, 0, 0], [50, 150, 0, 0, 0, 0], [0, 100, 150, 0, 0, 0], [0, 0, 150, 150, 0, 0], [0, 0, 0, 200, 150, 0], [0, 0, 0, 0, 250, 150]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [7, 14, 21, 28],colSum = [7, 14, 21, 28]) == [[7, 0, 0, 0], [0, 14, 0, 0], [0, 0, 21, 0], [0, 0, 0, 28]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [7, 14, 21, 28],colSum = [7, 14, 21, 28]) == [[7, 0, 0, 0], [0, 14, 0, 0], [0, 0, 21, 0], [0, 0, 0, 28]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [30, 60, 90, 120],colSum = [20, 40, 60, 80, 100]) == [[20, 10, 0, 0, 0], [0, 30, 30, 0, 0], [0, 0, 30, 60, 0], [0, 0, 0, 20, 100]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [30, 60, 90, 120],colSum = [20, 40, 60, 80, 100]) == [[20, 10, 0, 0, 0], [0, 30, 30, 0, 0], [0, 0, 30, 60, 0], [0, 0, 0, 20, 100]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],colSum = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 0, 0, 0], [4, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 5, 0, 0, 0, 0, 0, 0, 0, 0], [0, 4, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 6, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 6, 2, 0, 0, 0, 0, 0], [0, 0, 0, 0, 4, 5, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 3, 2, 1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],colSum = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 0, 0, 0], [4, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 5, 0, 0, 0, 0, 0, 0, 0, 0], [0, 4, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 6, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 6, 2, 0, 0, 0, 0, 0], [0, 0, 0, 0, 4, 5, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 3, 2, 1]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [10, 20, 30, 40, 50],colSum = [15, 25, 35, 25, 15]) == [[10, 0, 0, 0, 0], [5, 15, 0, 0, 0], [0, 10, 20, 0, 0], [0, 0, 15, 25, 0], [0, 0, 0, 0, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [10, 20, 30, 40, 50],colSum = [15, 25, 35, 25, 15]) == [[10, 0, 0, 0, 0], [5, 15, 0, 0, 0], [0, 10, 20, 0, 0], [0, 0, 15, 25, 0], [0, 0, 0, 0, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [33, 33, 33, 33, 33, 33],colSum = [22, 22, 22, 22, 22, 22]) == [[22, 11, 0, 0, 0, 0], [0, 11, 22, 0, 0, 0], [0, 0, 0, 22, 11, 0], [0, 0, 0, 0, 11, 22], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [33, 33, 33, 33, 33, 33],colSum = [22, 22, 22, 22, 22, 22]) == [[22, 11, 0, 0, 0, 0], [0, 11, 22, 0, 0, 0], [0, 0, 0, 22, 11, 0], [0, 0, 0, 0, 11, 22], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [100, 200, 300, 400, 500],colSum = [500, 400, 300, 200, 100]) == [[100, 0, 0, 0, 0], [200, 0, 0, 0, 0], [200, 100, 0, 0, 0], [0, 300, 100, 0, 0], [0, 0, 200, 200, 100]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [100, 200, 300, 400, 500],colSum = [500, 400, 300, 200, 100]) == [[100, 0, 0, 0, 0], [200, 0, 0, 0, 0], [200, 100, 0, 0, 0], [0, 300, 100, 0, 0], [0, 0, 200, 200, 100]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [10000, 20000, 30000],colSum = [15000, 20000, 25000]) == [[10000, 0, 0], [5000, 15000, 0], [0, 5000, 25000]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [10000, 20000, 30000],colSum = [15000, 20000, 25000]) == [[10000, 0, 0], [5000, 15000, 0], [0, 5000, 25000]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [5, 15, 25, 35],colSum = [10, 10, 10, 30]) == [[5, 0, 0, 0], [5, 10, 0, 0], [0, 0, 10, 15], [0, 0, 0, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [5, 15, 25, 35],colSum = [10, 10, 10, 30]) == [[5, 0, 0, 0], [5, 10, 0, 0], [0, 0, 10, 15], [0, 0, 0, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [1, 1, 1, 1, 1],colSum = [1, 1, 1, 1, 1]) == [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [1, 1, 1, 1, 1],colSum = [1, 1, 1, 1, 1]) == [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [7, 14, 21, 28, 35],colSum = [5, 10, 15, 20, 25]) == [[5, 2, 0, 0, 0], [0, 8, 6, 0, 0], [0, 0, 9, 12, 0], [0, 0, 0, 8, 20], [0, 0, 0, 0, 5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [7, 14, 21, 28, 35],colSum = [5, 10, 15, 20, 25]) == [[5, 2, 0, 0, 0], [0, 8, 6, 0, 0], [0, 0, 9, 12, 0], [0, 0, 0, 8, 20], [0, 0, 0, 0, 5]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [12, 34, 56, 78, 90, 123],colSum = [23, 45, 67, 89, 101, 112]) == [[12, 0, 0, 0, 0, 0], [11, 23, 0, 0, 0, 0], [0, 22, 34, 0, 0, 0], [0, 0, 33, 45, 0, 0], [0, 0, 0, 44, 46, 0], [0, 0, 0, 0, 55, 68]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [12, 34, 56, 78, 90, 123],colSum = [23, 45, 67, 89, 101, 112]) == [[12, 0, 0, 0, 0, 0], [11, 23, 0, 0, 0, 0], [0, 22, 34, 0, 0, 0], [0, 0, 33, 45, 0, 0], [0, 0, 0, 44, 46, 0], [0, 0, 0, 0, 55, 68]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [100, 200, 300, 400],colSum = [100, 150, 200, 350]) == [[100, 0, 0, 0], [0, 150, 50, 0], [0, 0, 150, 150], [0, 0, 0, 200]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [100, 200, 300, 400],colSum = [100, 150, 200, 350]) == [[100, 0, 0, 0], [0, 150, 50, 0], [0, 0, 150, 150], [0, 0, 0, 200]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [100, 200, 300, 400, 500],colSum = [250, 250, 250, 250, 250]) == [[100, 0, 0, 0, 0], [150, 50, 0, 0, 0], [0, 200, 100, 0, 0], [0, 0, 150, 250, 0], [0, 0, 0, 0, 250]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [100, 200, 300, 400, 500],colSum = [250, 250, 250, 250, 250]) == [[100, 0, 0, 0, 0], [150, 50, 0, 0, 0], [0, 200, 100, 0, 0], [0, 0, 150, 250, 0], [0, 0, 0, 0, 250]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [25, 75],colSum = [100, 50]) == [[25, 0], [75, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [25, 75],colSum = [100, 50]) == [[25, 0], [75, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [10, 20, 30, 40, 50],colSum = [5, 15, 25, 35, 45]) == [[5, 5, 0, 0, 0], [0, 10, 10, 0, 0], [0, 0, 15, 15, 0], [0, 0, 0, 20, 20], [0, 0, 0, 0, 25]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [10, 20, 30, 40, 50],colSum = [5, 15, 25, 35, 45]) == [[5, 5, 0, 0, 0], [0, 10, 10, 0, 0], [0, 0, 15, 15, 0], [0, 0, 0, 20, 20], [0, 0, 0, 0, 25]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [1000, 2000, 3000],colSum = [1500, 1500, 1500]) == [[1000, 0, 0], [500, 1500, 0], [0, 0, 1500]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [1000, 2000, 3000],colSum = [1500, 1500, 1500]) == [[1000, 0, 0], [500, 1500, 0], [0, 0, 1500]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [5, 10, 15, 20],colSum = [20, 15, 10, 5]) == [[5, 0, 0, 0], [10, 0, 0, 0], [5, 10, 0, 0], [0, 5, 10, 5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [5, 10, 15, 20],colSum = [20, 15, 10, 5]) == [[5, 0, 0, 0], [10, 0, 0, 0], [5, 10, 0, 0], [0, 5, 10, 5]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [50, 50, 50, 50, 50],colSum = [25, 25, 25, 25, 25, 25, 25]) == [[25, 25, 0, 0, 0, 0, 0], [0, 0, 25, 25, 0, 0, 0], [0, 0, 0, 0, 25, 25, 0], [0, 0, 0, 0, 0, 0, 25], [0, 0, 0, 0, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [50, 50, 50, 50, 50],colSum = [25, 25, 25, 25, 25, 25, 25]) == [[25, 25, 0, 0, 0, 0, 0], [0, 0, 25, 25, 0, 0, 0], [0, 0, 0, 0, 25, 25, 0], [0, 0, 0, 0, 0, 0, 25], [0, 0, 0, 0, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [500, 1000, 1500, 2000],colSum = [600, 700, 800, 900]) == [[500, 0, 0, 0], [100, 700, 200, 0], [0, 0, 600, 900], [0, 0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [500, 1000, 1500, 2000],colSum = [600, 700, 800, 900]) == [[500, 0, 0, 0], [100, 700, 200, 0], [0, 0, 600, 900], [0, 0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [50, 50, 50, 50],colSum = [60, 60, 60, 60]) == [[50, 0, 0, 0], [10, 40, 0, 0], [0, 20, 30, 0], [0, 0, 30, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [50, 50, 50, 50],colSum = [60, 60, 60, 60]) == [[50, 0, 0, 0], [10, 40, 0, 0], [0, 20, 30, 0], [0, 0, 30, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [40, 50, 60],colSum = [70, 60, 50]) == [[40, 0, 0], [30, 20, 0], [0, 40, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [40, 50, 60],colSum = [70, 60, 50]) == [[40, 0, 0], [30, 20, 0], [0, 40, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [12, 15, 7],colSum = [10, 10, 12]) == [[10, 2, 0], [0, 8, 7], [0, 0, 5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [12, 15, 7],colSum = [10, 10, 12]) == [[10, 2, 0], [0, 8, 7], [0, 0, 5]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [100, 200, 300],colSum = [250, 250, 200]) == [[100, 0, 0], [150, 50, 0], [0, 200, 100]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [100, 200, 300],colSum = [250, 250, 200]) == [[100, 0, 0], [150, 50, 0], [0, 200, 100]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [9, 18, 27, 36],colSum = [12, 24, 36, 48]) == [[9, 0, 0, 0], [3, 15, 0, 0], [0, 9, 18, 0], [0, 0, 18, 18]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [9, 18, 27, 36],colSum = [12, 24, 36, 48]) == [[9, 0, 0, 0], [3, 15, 0, 0], [0, 9, 18, 0], [0, 0, 18, 18]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [9, 9, 9, 9],colSum = [6, 6, 6, 6, 9]) == [[6, 3, 0, 0, 0], [0, 3, 6, 0, 0], [0, 0, 0, 6, 3], [0, 0, 0, 0, 6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [9, 9, 9, 9],colSum = [6, 6, 6, 6, 9]) == [[6, 3, 0, 0, 0], [0, 3, 6, 0, 0], [0, 0, 0, 6, 3], [0, 0, 0, 0, 6]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [50, 50, 50, 50, 50, 50],colSum = [50, 50, 50, 50, 50, 50]) == [[50, 0, 0, 0, 0, 0], [0, 50, 0, 0, 0, 0], [0, 0, 50, 0, 0, 0], [0, 0, 0, 50, 0, 0], [0, 0, 0, 0, 50, 0], [0, 0, 0, 0, 0, 50]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [50, 50, 50, 50, 50, 50],colSum = [50, 50, 50, 50, 50, 50]) == [[50, 0, 0, 0, 0, 0], [0, 50, 0, 0, 0, 0], [0, 0, 50, 0, 0, 0], [0, 0, 0, 50, 0, 0], [0, 0, 0, 0, 50, 0], [0, 0, 0, 0, 0, 50]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [33, 28, 44, 55],colSum = [30, 33, 25, 50]) == [[30, 3, 0, 0], [0, 28, 0, 0], [0, 2, 25, 17], [0, 0, 0, 33]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [33, 28, 44, 55],colSum = [30, 33, 25, 50]) == [[30, 3, 0, 0], [0, 28, 0, 0], [0, 2, 25, 17], [0, 0, 0, 33]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [300, 200, 100],colSum = [150, 200, 150]) == [[150, 150, 0], [0, 50, 150], [0, 0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [300, 200, 100],colSum = [150, 200, 150]) == [[150, 150, 0], [0, 50, 150], [0, 0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [30, 40, 50],colSum = [20, 50, 20]) == [[20, 10, 0], [0, 40, 0], [0, 0, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [30, 40, 50],colSum = [20, 50, 20]) == [[20, 10, 0], [0, 40, 0], [0, 0, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [120, 90, 75, 60],colSum = [80, 100, 75, 60]) == [[80, 40, 0, 0], [0, 60, 30, 0], [0, 0, 45, 30], [0, 0, 0, 30]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [120, 90, 75, 60],colSum = [80, 100, 75, 60]) == [[80, 40, 0, 0], [0, 60, 30, 0], [0, 0, 45, 30], [0, 0, 0, 30]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [5, 15, 25, 35],colSum = [10, 20, 30, 40]) == [[5, 0, 0, 0], [5, 10, 0, 0], [0, 10, 15, 0], [0, 0, 15, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [5, 15, 25, 35],colSum = [10, 20, 30, 40]) == [[5, 0, 0, 0], [5, 10, 0, 0], [0, 10, 15, 0], [0, 0, 15, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [34, 78, 90, 123],colSum = [50, 60, 70, 80]) == [[34, 0, 0, 0], [16, 60, 2, 0], [0, 0, 68, 22], [0, 0, 0, 58]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [34, 78, 90, 123],colSum = [50, 60, 70, 80]) == [[34, 0, 0, 0], [16, 60, 2, 0], [0, 0, 68, 22], [0, 0, 0, 58]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [120, 150, 180],colSum = [100, 130, 200]) == [[100, 20, 0], [0, 110, 40], [0, 0, 160]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [120, 150, 180],colSum = [100, 130, 200]) == [[100, 20, 0], [0, 110, 40], [0, 0, 160]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [10, 20, 30],colSum = [30, 20, 10]) == [[10, 0, 0], [20, 0, 0], [0, 20, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [10, 20, 30],colSum = [30, 20, 10]) == [[10, 0, 0], [20, 0, 0], [0, 20, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [10, 10, 10, 10, 10],colSum = [5, 5, 5, 5, 50]) == [[5, 5, 0, 0, 0], [0, 0, 5, 5, 0], [0, 0, 0, 0, 10], [0, 0, 0, 0, 10], [0, 0, 0, 0, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [10, 10, 10, 10, 10],colSum = [5, 5, 5, 5, 50]) == [[5, 5, 0, 0, 0], [0, 0, 5, 5, 0], [0, 0, 0, 0, 10], [0, 0, 0, 0, 10], [0, 0, 0, 0, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [12, 9, 6],colSum = [10, 10, 7]) == [[10, 2, 0], [0, 8, 1], [0, 0, 6]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [12, 9, 6],colSum = [10, 10, 7]) == [[10, 2, 0], [0, 8, 1], [0, 0, 6]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [15, 25, 35, 45],colSum = [20, 30, 25, 25]) == [[15, 0, 0, 0], [5, 20, 0, 0], [0, 10, 25, 0], [0, 0, 0, 25]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [15, 25, 35, 45],colSum = [20, 30, 25, 25]) == [[15, 0, 0, 0], [5, 20, 0, 0], [0, 10, 25, 0], [0, 0, 0, 25]]: {e}')
    
    total += 1
    try:
        result = candidate(rowSum = [100, 150, 200, 250],colSum = [150, 200, 250, 100]) == [[100, 0, 0, 0], [50, 100, 0, 0], [0, 100, 100, 0], [0, 0, 150, 100]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(rowSum = [100, 150, 200, 250],colSum = [150, 200, 250, 100]) == [[100, 0, 0, 0], [50, 100, 0, 0], [0, 100, 100, 0], [0, 0, 150, 100]]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(rowSum = [10, 15],colSum = [12, 13]) == [[10, 0], [2, 13]]
    assert candidate(rowSum = [5, 5, 5],colSum = [5, 5, 5]) == [[5, 0, 0], [0, 5, 0], [0, 0, 5]]
    assert candidate(rowSum = [10, 20],colSum = [15, 15]) == [[10, 0], [5, 15]]
    assert candidate(rowSum = [10, 15, 20],colSum = [15, 15, 15]) == [[10, 0, 0], [5, 10, 0], [0, 5, 15]]
    assert candidate(rowSum = [1, 2, 3, 4],colSum = [1, 2, 3, 4]) == [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]]
    assert candidate(rowSum = [1, 1, 1],colSum = [1, 1, 1]) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert candidate(rowSum = [5, 7, 10],colSum = [8, 6, 8]) == [[5, 0, 0], [3, 4, 0], [0, 2, 8]]
    assert candidate(rowSum = [10, 15, 20],colSum = [5, 10, 20]) == [[5, 5, 0], [0, 5, 10], [0, 0, 10]]
    assert candidate(rowSum = [0, 0],colSum = [0, 0]) == [[0, 0], [0, 0]]
    assert candidate(rowSum = [1, 2],colSum = [3, 0]) == [[1, 0], [2, 0]]
    assert candidate(rowSum = [1, 2, 3],colSum = [3, 2, 1]) == [[1, 0, 0], [2, 0, 0], [0, 2, 1]]
    assert candidate(rowSum = [0, 0, 0],colSum = [0, 0, 0]) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert candidate(rowSum = [3, 8],colSum = [4, 7]) == [[3, 0], [1, 7]]
    assert candidate(rowSum = [25, 25, 25, 25, 25],colSum = [25, 25, 25, 25, 25]) == [[25, 0, 0, 0, 0], [0, 25, 0, 0, 0], [0, 0, 25, 0, 0], [0, 0, 0, 25, 0], [0, 0, 0, 0, 25]]
    assert candidate(rowSum = [9, 18, 27, 36, 45],colSum = [5, 10, 15, 20, 25]) == [[5, 4, 0, 0, 0], [0, 6, 12, 0, 0], [0, 0, 3, 20, 4], [0, 0, 0, 0, 21], [0, 0, 0, 0, 0]]
    assert candidate(rowSum = [10, 20, 30],colSum = [6, 9, 12, 15]) == [[6, 4, 0, 0], [0, 5, 12, 3], [0, 0, 0, 12]]
    assert candidate(rowSum = [5, 5, 5, 5],colSum = [4, 4, 4, 4]) == [[4, 1, 0, 0], [0, 3, 2, 0], [0, 0, 2, 3], [0, 0, 0, 1]]
    assert candidate(rowSum = [10, 20, 30],colSum = [6, 15, 29]) == [[6, 4, 0], [0, 11, 9], [0, 0, 20]]
    assert candidate(rowSum = [300, 400, 500, 600],colSum = [200, 300, 400, 700]) == [[200, 100, 0, 0], [0, 200, 200, 0], [0, 0, 200, 300], [0, 0, 0, 400]]
    assert candidate(rowSum = [12, 25, 30],colSum = [20, 15, 20]) == [[12, 0, 0], [8, 15, 2], [0, 0, 18]]
    assert candidate(rowSum = [12, 15, 20],colSum = [10, 10, 17]) == [[10, 2, 0], [0, 8, 7], [0, 0, 10]]
    assert candidate(rowSum = [1000, 2000, 3000],colSum = [1500, 2000, 2500]) == [[1000, 0, 0], [500, 1500, 0], [0, 500, 2500]]
    assert candidate(rowSum = [9, 18, 27],colSum = [12, 15, 18]) == [[9, 0, 0], [3, 15, 0], [0, 0, 18]]
    assert candidate(rowSum = [100, 100, 100, 100],colSum = [25, 25, 25, 25]) == [[25, 25, 25, 25], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert candidate(rowSum = [45, 55, 65, 75, 85],colSum = [50, 60, 70, 80, 90]) == [[45, 0, 0, 0, 0], [5, 50, 0, 0, 0], [0, 10, 55, 0, 0], [0, 0, 15, 60, 0], [0, 0, 0, 20, 65]]
    assert candidate(rowSum = [99, 100, 101, 102],colSum = [101, 102, 99, 100]) == [[99, 0, 0, 0], [2, 98, 0, 0], [0, 4, 97, 0], [0, 0, 2, 100]]
    assert candidate(rowSum = [50, 100, 150],colSum = [25, 75, 100, 150]) == [[25, 25, 0, 0], [0, 50, 50, 0], [0, 0, 50, 100]]
    assert candidate(rowSum = [25, 50, 75, 100],colSum = [10, 20, 30, 40, 95]) == [[10, 15, 0, 0, 0], [0, 5, 30, 15, 0], [0, 0, 0, 25, 50], [0, 0, 0, 0, 45]]
    assert candidate(rowSum = [100, 150, 200, 250],colSum = [100, 100, 150, 200]) == [[100, 0, 0, 0], [0, 100, 50, 0], [0, 0, 100, 100], [0, 0, 0, 100]]
    assert candidate(rowSum = [45, 55, 65, 75, 85],colSum = [30, 40, 50, 60, 70]) == [[30, 15, 0, 0, 0], [0, 25, 30, 0, 0], [0, 0, 20, 45, 0], [0, 0, 0, 15, 60], [0, 0, 0, 0, 10]]
    assert candidate(rowSum = [100, 200, 300, 400],colSum = [150, 250, 350, 450]) == [[100, 0, 0, 0], [50, 150, 0, 0], [0, 100, 200, 0], [0, 0, 150, 250]]
    assert candidate(rowSum = [300, 200, 100, 50],colSum = [150, 150, 150, 100, 50]) == [[150, 150, 0, 0, 0], [0, 0, 150, 50, 0], [0, 0, 0, 50, 50], [0, 0, 0, 0, 0]]
    assert candidate(rowSum = [20, 30, 40, 50],colSum = [10, 20, 30, 40]) == [[10, 10, 0, 0], [0, 10, 20, 0], [0, 0, 10, 30], [0, 0, 0, 10]]
    assert candidate(rowSum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],colSum = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
    assert candidate(rowSum = [100, 200, 300],colSum = [150, 100, 250]) == [[100, 0, 0], [50, 100, 50], [0, 0, 200]]
    assert candidate(rowSum = [50, 50, 50],colSum = [40, 40, 40, 40]) == [[40, 10, 0, 0], [0, 30, 20, 0], [0, 0, 20, 30]]
    assert candidate(rowSum = [10, 20, 30, 40, 50],colSum = [15, 15, 15, 15, 15]) == [[10, 0, 0, 0, 0], [5, 15, 0, 0, 0], [0, 0, 15, 15, 0], [0, 0, 0, 0, 15], [0, 0, 0, 0, 0]]
    assert candidate(rowSum = [500, 500, 500, 500, 500],colSum = [250, 250, 250, 250, 250]) == [[250, 250, 0, 0, 0], [0, 0, 250, 250, 0], [0, 0, 0, 0, 250], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert candidate(rowSum = [5, 6, 7, 8],colSum = [10, 8, 6, 4]) == [[5, 0, 0, 0], [5, 1, 0, 0], [0, 7, 0, 0], [0, 0, 6, 2]]
    assert candidate(rowSum = [100, 200, 300],colSum = [150, 250, 100]) == [[100, 0, 0], [50, 150, 0], [0, 100, 100]]
    assert candidate(rowSum = [25, 50, 75, 100],colSum = [40, 50, 60, 50]) == [[25, 0, 0, 0], [15, 35, 0, 0], [0, 15, 60, 0], [0, 0, 0, 50]]
    assert candidate(rowSum = [10, 20, 30, 40, 50],colSum = [50, 40, 30, 20, 10]) == [[10, 0, 0, 0, 0], [20, 0, 0, 0, 0], [20, 10, 0, 0, 0], [0, 30, 10, 0, 0], [0, 0, 20, 20, 10]]
    assert candidate(rowSum = [500, 300, 200],colSum = [400, 350, 250]) == [[400, 100, 0], [0, 250, 50], [0, 0, 200]]
    assert candidate(rowSum = [50, 75, 100],colSum = [120, 100, 30]) == [[50, 0, 0], [70, 5, 0], [0, 95, 5]]
    assert candidate(rowSum = [8, 16, 24, 32],colSum = [16, 24, 16, 24]) == [[8, 0, 0, 0], [8, 8, 0, 0], [0, 16, 8, 0], [0, 0, 8, 24]]
    assert candidate(rowSum = [8, 6, 4, 2, 0],colSum = [1, 2, 3, 4, 5]) == [[1, 2, 3, 2, 0], [0, 0, 0, 2, 4], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    assert candidate(rowSum = [88, 77, 66, 55, 44],colSum = [99, 88, 77, 66, 55]) == [[88, 0, 0, 0, 0], [11, 66, 0, 0, 0], [0, 22, 44, 0, 0], [0, 0, 33, 22, 0], [0, 0, 0, 44, 0]]
    assert candidate(rowSum = [150, 200, 250],colSum = [200, 150, 300]) == [[150, 0, 0], [50, 150, 0], [0, 0, 250]]
    assert candidate(rowSum = [88, 88, 88, 88, 88, 88],colSum = [77, 77, 77, 77, 77, 77]) == [[77, 11, 0, 0, 0, 0], [0, 66, 22, 0, 0, 0], [0, 0, 55, 33, 0, 0], [0, 0, 0, 44, 44, 0], [0, 0, 0, 0, 33, 55], [0, 0, 0, 0, 0, 22]]
    assert candidate(rowSum = [120, 110, 100, 90],colSum = [105, 95, 85, 75]) == [[105, 15, 0, 0], [0, 80, 30, 0], [0, 0, 55, 45], [0, 0, 0, 30]]
    assert candidate(rowSum = [50, 60, 70, 80, 90],colSum = [90, 80, 70, 60, 50]) == [[50, 0, 0, 0, 0], [40, 20, 0, 0, 0], [0, 60, 10, 0, 0], [0, 0, 60, 20, 0], [0, 0, 0, 40, 50]]
    assert candidate(rowSum = [123, 456, 789],colSum = [456, 789, 123]) == [[123, 0, 0], [333, 123, 0], [0, 666, 123]]
    assert candidate(rowSum = [10, 20, 30, 40, 50],colSum = [5, 10, 15, 20, 60]) == [[5, 5, 0, 0, 0], [0, 5, 15, 0, 0], [0, 0, 0, 20, 10], [0, 0, 0, 0, 40], [0, 0, 0, 0, 10]]
    assert candidate(rowSum = [8, 16, 24, 32],colSum = [16, 24, 32, 8]) == [[8, 0, 0, 0], [8, 8, 0, 0], [0, 16, 8, 0], [0, 0, 24, 8]]
    assert candidate(rowSum = [100, 200, 300, 400],colSum = [200, 300, 200, 400]) == [[100, 0, 0, 0], [100, 100, 0, 0], [0, 200, 100, 0], [0, 0, 100, 300]]
    assert candidate(rowSum = [120, 80, 40],colSum = [90, 70, 30, 10]) == [[90, 30, 0, 0], [0, 40, 30, 10], [0, 0, 0, 0]]
    assert candidate(rowSum = [10, 20, 30, 40],colSum = [15, 25, 25, 25]) == [[10, 0, 0, 0], [5, 15, 0, 0], [0, 10, 20, 0], [0, 0, 5, 25]]
    assert candidate(rowSum = [99, 98, 97, 96, 95],colSum = [95, 96, 97, 98, 99]) == [[95, 4, 0, 0, 0], [0, 92, 6, 0, 0], [0, 0, 91, 6, 0], [0, 0, 0, 92, 4], [0, 0, 0, 0, 95]]
    assert candidate(rowSum = [15, 25, 35, 45],colSum = [10, 20, 30, 40]) == [[10, 5, 0, 0], [0, 15, 10, 0], [0, 0, 20, 15], [0, 0, 0, 25]]
    assert candidate(rowSum = [75, 80, 85, 90, 95, 100],colSum = [60, 65, 70, 75, 80, 85]) == [[60, 15, 0, 0, 0, 0], [0, 50, 30, 0, 0, 0], [0, 0, 40, 45, 0, 0], [0, 0, 0, 30, 60, 0], [0, 0, 0, 0, 20, 75], [0, 0, 0, 0, 0, 10]]
    assert candidate(rowSum = [100, 150, 200],colSum = [200, 120, 130]) == [[100, 0, 0], [100, 50, 0], [0, 70, 130]]
    assert candidate(rowSum = [120, 140, 160, 180, 200],colSum = [200, 180, 160, 140, 120]) == [[120, 0, 0, 0, 0], [80, 60, 0, 0, 0], [0, 120, 40, 0, 0], [0, 0, 120, 60, 0], [0, 0, 0, 80, 120]]
    assert candidate(rowSum = [50, 60, 70, 80],colSum = [30, 40, 50, 60]) == [[30, 20, 0, 0], [0, 20, 40, 0], [0, 0, 10, 60], [0, 0, 0, 0]]
    assert candidate(rowSum = [30, 20, 10, 0],colSum = [10, 10, 10, 30]) == [[10, 10, 10, 0], [0, 0, 0, 20], [0, 0, 0, 10], [0, 0, 0, 0]]
    assert candidate(rowSum = [5, 10, 15, 20, 25],colSum = [25, 20, 15, 10, 5]) == [[5, 0, 0, 0, 0], [10, 0, 0, 0, 0], [10, 5, 0, 0, 0], [0, 15, 5, 0, 0], [0, 0, 10, 10, 5]]
    assert candidate(rowSum = [20, 40, 60, 80],colSum = [30, 30, 30, 30]) == [[20, 0, 0, 0], [10, 30, 0, 0], [0, 0, 30, 30], [0, 0, 0, 0]]
    assert candidate(rowSum = [1, 1, 1, 1, 1, 1],colSum = [1, 1, 1, 1, 1, 1]) == [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
    assert candidate(rowSum = [50, 45, 60],colSum = [40, 30, 35]) == [[40, 10, 0], [0, 20, 25], [0, 0, 10]]
    assert candidate(rowSum = [123, 456, 789],colSum = [321, 654, 987]) == [[123, 0, 0], [198, 258, 0], [0, 396, 393]]
    assert candidate(rowSum = [100, 200, 300],colSum = [150, 150, 150]) == [[100, 0, 0], [50, 150, 0], [0, 0, 150]]
    assert candidate(rowSum = [30, 40, 50, 60],colSum = [50, 40, 40, 30]) == [[30, 0, 0, 0], [20, 20, 0, 0], [0, 20, 30, 0], [0, 0, 10, 30]]
    assert candidate(rowSum = [1, 2, 3, 4, 5],colSum = [5, 4, 3, 2, 1]) == [[1, 0, 0, 0, 0], [2, 0, 0, 0, 0], [2, 1, 0, 0, 0], [0, 3, 1, 0, 0], [0, 0, 2, 2, 1]]
    assert candidate(rowSum = [30, 20, 10],colSum = [15, 20, 15]) == [[15, 15, 0], [0, 5, 15], [0, 0, 0]]
    assert candidate(rowSum = [20, 30, 40, 50],colSum = [15, 15, 15, 15, 20, 10]) == [[15, 5, 0, 0, 0, 0], [0, 10, 15, 5, 0, 0], [0, 0, 0, 10, 20, 10], [0, 0, 0, 0, 0, 0]]
    assert candidate(rowSum = [150, 200, 250, 300, 350, 400],colSum = [200, 250, 300, 350, 400, 450]) == [[150, 0, 0, 0, 0, 0], [50, 150, 0, 0, 0, 0], [0, 100, 150, 0, 0, 0], [0, 0, 150, 150, 0, 0], [0, 0, 0, 200, 150, 0], [0, 0, 0, 0, 250, 150]]
    assert candidate(rowSum = [7, 14, 21, 28],colSum = [7, 14, 21, 28]) == [[7, 0, 0, 0], [0, 14, 0, 0], [0, 0, 21, 0], [0, 0, 0, 28]]
    assert candidate(rowSum = [30, 60, 90, 120],colSum = [20, 40, 60, 80, 100]) == [[20, 10, 0, 0, 0], [0, 30, 30, 0, 0], [0, 0, 30, 60, 0], [0, 0, 0, 20, 100]]
    assert candidate(rowSum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],colSum = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0, 0, 0, 0, 0], [4, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 5, 0, 0, 0, 0, 0, 0, 0, 0], [0, 4, 2, 0, 0, 0, 0, 0, 0, 0], [0, 0, 6, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 6, 2, 0, 0, 0, 0, 0], [0, 0, 0, 0, 4, 5, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 3, 2, 1]]
    assert candidate(rowSum = [10, 20, 30, 40, 50],colSum = [15, 25, 35, 25, 15]) == [[10, 0, 0, 0, 0], [5, 15, 0, 0, 0], [0, 10, 20, 0, 0], [0, 0, 15, 25, 0], [0, 0, 0, 0, 15]]
    assert candidate(rowSum = [33, 33, 33, 33, 33, 33],colSum = [22, 22, 22, 22, 22, 22]) == [[22, 11, 0, 0, 0, 0], [0, 11, 22, 0, 0, 0], [0, 0, 0, 22, 11, 0], [0, 0, 0, 0, 11, 22], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    assert candidate(rowSum = [100, 200, 300, 400, 500],colSum = [500, 400, 300, 200, 100]) == [[100, 0, 0, 0, 0], [200, 0, 0, 0, 0], [200, 100, 0, 0, 0], [0, 300, 100, 0, 0], [0, 0, 200, 200, 100]]
    assert candidate(rowSum = [10000, 20000, 30000],colSum = [15000, 20000, 25000]) == [[10000, 0, 0], [5000, 15000, 0], [0, 5000, 25000]]
    assert candidate(rowSum = [5, 15, 25, 35],colSum = [10, 10, 10, 30]) == [[5, 0, 0, 0], [5, 10, 0, 0], [0, 0, 10, 15], [0, 0, 0, 15]]
    assert candidate(rowSum = [1, 1, 1, 1, 1],colSum = [1, 1, 1, 1, 1]) == [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
    assert candidate(rowSum = [7, 14, 21, 28, 35],colSum = [5, 10, 15, 20, 25]) == [[5, 2, 0, 0, 0], [0, 8, 6, 0, 0], [0, 0, 9, 12, 0], [0, 0, 0, 8, 20], [0, 0, 0, 0, 5]]
    assert candidate(rowSum = [12, 34, 56, 78, 90, 123],colSum = [23, 45, 67, 89, 101, 112]) == [[12, 0, 0, 0, 0, 0], [11, 23, 0, 0, 0, 0], [0, 22, 34, 0, 0, 0], [0, 0, 33, 45, 0, 0], [0, 0, 0, 44, 46, 0], [0, 0, 0, 0, 55, 68]]
    assert candidate(rowSum = [100, 200, 300, 400],colSum = [100, 150, 200, 350]) == [[100, 0, 0, 0], [0, 150, 50, 0], [0, 0, 150, 150], [0, 0, 0, 200]]
    assert candidate(rowSum = [100, 200, 300, 400, 500],colSum = [250, 250, 250, 250, 250]) == [[100, 0, 0, 0, 0], [150, 50, 0, 0, 0], [0, 200, 100, 0, 0], [0, 0, 150, 250, 0], [0, 0, 0, 0, 250]]
    assert candidate(rowSum = [25, 75],colSum = [100, 50]) == [[25, 0], [75, 0]]
    assert candidate(rowSum = [10, 20, 30, 40, 50],colSum = [5, 15, 25, 35, 45]) == [[5, 5, 0, 0, 0], [0, 10, 10, 0, 0], [0, 0, 15, 15, 0], [0, 0, 0, 20, 20], [0, 0, 0, 0, 25]]
    assert candidate(rowSum = [1000, 2000, 3000],colSum = [1500, 1500, 1500]) == [[1000, 0, 0], [500, 1500, 0], [0, 0, 1500]]
    assert candidate(rowSum = [5, 10, 15, 20],colSum = [20, 15, 10, 5]) == [[5, 0, 0, 0], [10, 0, 0, 0], [5, 10, 0, 0], [0, 5, 10, 5]]
    assert candidate(rowSum = [50, 50, 50, 50, 50],colSum = [25, 25, 25, 25, 25, 25, 25]) == [[25, 25, 0, 0, 0, 0, 0], [0, 0, 25, 25, 0, 0, 0], [0, 0, 0, 0, 25, 25, 0], [0, 0, 0, 0, 0, 0, 25], [0, 0, 0, 0, 0, 0, 0]]
    assert candidate(rowSum = [500, 1000, 1500, 2000],colSum = [600, 700, 800, 900]) == [[500, 0, 0, 0], [100, 700, 200, 0], [0, 0, 600, 900], [0, 0, 0, 0]]
    assert candidate(rowSum = [50, 50, 50, 50],colSum = [60, 60, 60, 60]) == [[50, 0, 0, 0], [10, 40, 0, 0], [0, 20, 30, 0], [0, 0, 30, 20]]
    assert candidate(rowSum = [40, 50, 60],colSum = [70, 60, 50]) == [[40, 0, 0], [30, 20, 0], [0, 40, 20]]
    assert candidate(rowSum = [12, 15, 7],colSum = [10, 10, 12]) == [[10, 2, 0], [0, 8, 7], [0, 0, 5]]
    assert candidate(rowSum = [100, 200, 300],colSum = [250, 250, 200]) == [[100, 0, 0], [150, 50, 0], [0, 200, 100]]
    assert candidate(rowSum = [9, 18, 27, 36],colSum = [12, 24, 36, 48]) == [[9, 0, 0, 0], [3, 15, 0, 0], [0, 9, 18, 0], [0, 0, 18, 18]]
    assert candidate(rowSum = [9, 9, 9, 9],colSum = [6, 6, 6, 6, 9]) == [[6, 3, 0, 0, 0], [0, 3, 6, 0, 0], [0, 0, 0, 6, 3], [0, 0, 0, 0, 6]]
    assert candidate(rowSum = [50, 50, 50, 50, 50, 50],colSum = [50, 50, 50, 50, 50, 50]) == [[50, 0, 0, 0, 0, 0], [0, 50, 0, 0, 0, 0], [0, 0, 50, 0, 0, 0], [0, 0, 0, 50, 0, 0], [0, 0, 0, 0, 50, 0], [0, 0, 0, 0, 0, 50]]
    assert candidate(rowSum = [33, 28, 44, 55],colSum = [30, 33, 25, 50]) == [[30, 3, 0, 0], [0, 28, 0, 0], [0, 2, 25, 17], [0, 0, 0, 33]]
    assert candidate(rowSum = [300, 200, 100],colSum = [150, 200, 150]) == [[150, 150, 0], [0, 50, 150], [0, 0, 0]]
    assert candidate(rowSum = [30, 40, 50],colSum = [20, 50, 20]) == [[20, 10, 0], [0, 40, 0], [0, 0, 20]]
    assert candidate(rowSum = [120, 90, 75, 60],colSum = [80, 100, 75, 60]) == [[80, 40, 0, 0], [0, 60, 30, 0], [0, 0, 45, 30], [0, 0, 0, 30]]
    assert candidate(rowSum = [5, 15, 25, 35],colSum = [10, 20, 30, 40]) == [[5, 0, 0, 0], [5, 10, 0, 0], [0, 10, 15, 0], [0, 0, 15, 20]]
    assert candidate(rowSum = [34, 78, 90, 123],colSum = [50, 60, 70, 80]) == [[34, 0, 0, 0], [16, 60, 2, 0], [0, 0, 68, 22], [0, 0, 0, 58]]
    assert candidate(rowSum = [120, 150, 180],colSum = [100, 130, 200]) == [[100, 20, 0], [0, 110, 40], [0, 0, 160]]
    assert candidate(rowSum = [10, 20, 30],colSum = [30, 20, 10]) == [[10, 0, 0], [20, 0, 0], [0, 20, 10]]
    assert candidate(rowSum = [10, 10, 10, 10, 10],colSum = [5, 5, 5, 5, 50]) == [[5, 5, 0, 0, 0], [0, 0, 5, 5, 0], [0, 0, 0, 0, 10], [0, 0, 0, 0, 10], [0, 0, 0, 0, 10]]
    assert candidate(rowSum = [12, 9, 6],colSum = [10, 10, 7]) == [[10, 2, 0], [0, 8, 1], [0, 0, 6]]
    assert candidate(rowSum = [15, 25, 35, 45],colSum = [20, 30, 25, 25]) == [[15, 0, 0, 0], [5, 20, 0, 0], [0, 10, 25, 0], [0, 0, 0, 25]]
    assert candidate(rowSum = [100, 150, 200, 250],colSum = [150, 200, 250, 100]) == [[100, 0, 0, 0], [50, 100, 0, 0], [0, 100, 100, 0], [0, 0, 150, 100]]


