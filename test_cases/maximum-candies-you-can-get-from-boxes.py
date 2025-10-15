def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0],candies = [100, 200, 300],keys = [[1, 2], [0, 2], [0, 1]],containedBoxes = [[1, 2], [0, 2], [0, 1]],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0],candies = [100, 200, 300],keys = [[1, 2], [0, 2], [0, 1]],containedBoxes = [[1, 2], [0, 2], [0, 1]],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0],candies = [10, 20, 30],keys = [[1], [2], []],containedBoxes = [[], [], []],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0],candies = [10, 20, 30],keys = [[1], [2], []],containedBoxes = [[], [], []],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 1, 0, 0, 1],candies = [5, 15, 25, 35, 45],keys = [[2, 3], [], [4], [], []],containedBoxes = [[1, 2], [3], [], [], []],initialBoxes = [0]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 1, 0, 0, 1],candies = [5, 15, 25, 35, 45],keys = [[2, 3], [], [4], [], []],containedBoxes = [[1, 2], [3], [], [], []],initialBoxes = [0]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 1, 0, 0],candies = [10, 20, 30, 40],keys = [[], [], [2], [3]],containedBoxes = [[2, 3], [], [], []],initialBoxes = [0, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 1, 0, 0],candies = [10, 20, 30, 40],keys = [[], [], [2], [3]],containedBoxes = [[2, 3], [], [], []],initialBoxes = [0, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 1, 0, 0],candies = [10, 20, 30, 40],keys = [[2], [3], [], []],containedBoxes = [[], [], [1, 3], []],initialBoxes = [0, 1]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 1, 0, 0],candies = [10, 20, 30, 40],keys = [[2], [3], [], []],containedBoxes = [[], [], [1, 3], []],initialBoxes = [0, 1]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 1, 0, 1],candies = [3, 5, 2, 7, 6],keys = [[2], [1, 4], [0], [], [3]],containedBoxes = [[4], [3], [], [1], [2]],initialBoxes = [0]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 1, 0, 1],candies = [3, 5, 2, 7, 6],keys = [[2], [1, 4], [0], [], [3]],containedBoxes = [[4], [3], [], [1], [2]],initialBoxes = [0]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 1, 1],candies = [10, 20, 30, 40],keys = [[1, 3], [0], [], []],containedBoxes = [[2], [3], [], []],initialBoxes = [2]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 1, 1],candies = [10, 20, 30, 40],keys = [[1, 3], [0], [], []],containedBoxes = [[2], [3], [], []],initialBoxes = [2]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 1, 1],candies = [10, 20, 30, 40],keys = [[1, 2], [0], [3], []],containedBoxes = [[2, 3], [1], [], []],initialBoxes = [2]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 1, 1],candies = [10, 20, 30, 40],keys = [[1, 2], [0], [3], []],containedBoxes = [[2, 3], [1], [], []],initialBoxes = [2]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 1, 1],candies = [5, 10, 15],keys = [[], [2], []],containedBoxes = [[1], [], []],initialBoxes = [0]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 1, 1],candies = [5, 10, 15],keys = [[], [2], []],containedBoxes = [[1], [], []],initialBoxes = [0]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 0, 0, 0, 0],candies = [1, 1, 1, 1, 1, 1],keys = [[1, 2, 3, 4, 5], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5], [], [], [], [], []],initialBoxes = [0]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 0, 0, 0, 0],candies = [1, 1, 1, 1, 1, 1],keys = [[1, 2, 3, 4, 5], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5], [], [], [], [], []],initialBoxes = [0]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0],candies = [100, 200, 300, 400],keys = [[1, 2], [2, 3], [3], []],containedBoxes = [[1, 2, 3], [], [], []],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0],candies = [100, 200, 300, 400],keys = [[1, 2], [2, 3], [3], []],containedBoxes = [[1, 2, 3], [], [], []],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 0],candies = [100, 200, 300],keys = [[1], [], [2]],containedBoxes = [[2], [], []],initialBoxes = [0]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 0],candies = [100, 200, 300],keys = [[1], [], [2]],containedBoxes = [[2], [], []],initialBoxes = [0]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 1, 1],candies = [2, 3, 5, 7],keys = [[1, 2], [2, 3], [], []],containedBoxes = [[2, 3], [3], [], []],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 1, 1],candies = [2, 3, 5, 7],keys = [[1, 2], [2, 3], [], []],containedBoxes = [[2, 3], [3], [], []],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 1, 0],candies = [7, 5, 4, 100],keys = [[], [], [1], []],containedBoxes = [[1, 2], [3], [], []],initialBoxes = [0]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 1, 0],candies = [7, 5, 4, 100],keys = [[], [], [1], []],containedBoxes = [[1, 2], [3], [], []],initialBoxes = [0]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 1, 1],candies = [5, 5, 5],keys = [[], [2], [1]],containedBoxes = [[1, 2], [0, 2], [0, 1]],initialBoxes = [0]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 1, 1],candies = [5, 5, 5],keys = [[], [2], [1]],containedBoxes = [[1, 2], [0, 2], [0, 1]],initialBoxes = [0]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[3, 5], [0, 2], [4], [], [6], [], []],containedBoxes = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 0], [6, 1], [0, 2]],initialBoxes = [0]) == 260
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[3, 5], [0, 2], [4], [], [6], [], []],containedBoxes = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 0], [6, 1], [0, 2]],initialBoxes = [0]) == 260: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 1, 0, 1, 0, 1, 0],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[1, 3, 5], [2, 4, 6], [3, 4], [0, 5, 6], [0, 2, 4], [0, 3, 5], [2, 4, 6]],containedBoxes = [[1, 2, 3], [4, 5, 6], [0, 3, 5], [2, 4, 6], [0, 1, 5], [2, 3, 4], [0, 1, 4]],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 1, 0, 1, 0, 1, 0],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[1, 3, 5], [2, 4, 6], [3, 4], [0, 5, 6], [0, 2, 4], [0, 3, 5], [2, 4, 6]],containedBoxes = [[1, 2, 3], [4, 5, 6], [0, 3, 5], [2, 4, 6], [0, 1, 5], [2, 3, 4], [0, 1, 4]],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],keys = [[1, 2], [3, 4], [5, 6], [7, 8], [9], [], [], [], [], []],containedBoxes = [[3, 4, 5], [6, 7, 8], [9], [], [], [0, 1, 2], [3, 4, 5], [6, 7, 8], [9], [0, 1, 2]],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],keys = [[1, 2], [3, 4], [5, 6], [7, 8], [9], [], [], [], [], []],containedBoxes = [[3, 4, 5], [6, 7, 8], [9], [], [], [0, 1, 2], [3, 4, 5], [6, 7, 8], [9], [0, 1, 2]],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60],keys = [[1, 2], [0], [3], [4], [5], []],containedBoxes = [[2, 3], [0, 3], [1, 4], [2, 5], [3], []],initialBoxes = [1]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60],keys = [[1, 2], [0], [3], [4], [5], []],containedBoxes = [[2, 3], [0, 3], [1, 4], [2, 5], [3], []],initialBoxes = [1]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90],keys = [[1, 3, 5, 7, 8], [2, 4, 6], [0, 3, 6, 8], [1, 4, 7], [0, 2, 7, 8], [1, 3, 6], [0, 2, 5, 8], [1, 3, 4, 8], [0, 1, 2, 3, 4, 5, 6, 7]],containedBoxes = [[1, 3, 5, 7, 8], [2, 4, 6], [0, 3, 6, 8], [1, 4, 7], [0, 2, 7, 8], [1, 3, 6], [0, 2, 5, 8], [1, 3, 4, 8], [0, 1, 2, 3, 4, 5, 6, 7]],initialBoxes = [0]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90],keys = [[1, 3, 5, 7, 8], [2, 4, 6], [0, 3, 6, 8], [1, 4, 7], [0, 2, 7, 8], [1, 3, 6], [0, 2, 5, 8], [1, 3, 4, 8], [0, 1, 2, 3, 4, 5, 6, 7]],containedBoxes = [[1, 3, 5, 7, 8], [2, 4, 6], [0, 3, 6, 8], [1, 4, 7], [0, 2, 7, 8], [1, 3, 6], [0, 2, 5, 8], [1, 3, 4, 8], [0, 1, 2, 3, 4, 5, 6, 7]],initialBoxes = [0]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],keys = [[1, 3, 5, 7], [2, 4, 6, 8], [], [], [], [], [], [], [], []],containedBoxes = [[1, 3, 5, 7], [2, 4, 6, 8], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],keys = [[1, 3, 5, 7], [2, 4, 6, 8], [], [], [], [], [], [], [], []],containedBoxes = [[1, 3, 5, 7], [2, 4, 6, 8], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0],candies = [50, 100, 150, 200, 250, 300, 350],keys = [[2, 3], [1, 3], [0, 2, 4], [0, 1, 2, 5], [0, 3, 5, 6], [1, 4, 6], [1, 3, 4]],containedBoxes = [[1, 2, 3], [0, 2, 4], [0, 1, 5], [0, 1, 2, 5], [0, 3, 5, 6], [1, 4, 6], [1, 3, 4]],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0],candies = [50, 100, 150, 200, 250, 300, 350],keys = [[2, 3], [1, 3], [0, 2, 4], [0, 1, 2, 5], [0, 3, 5, 6], [1, 4, 6], [1, 3, 4]],containedBoxes = [[1, 2, 3], [0, 2, 4], [0, 1, 5], [0, 1, 2, 5], [0, 3, 5, 6], [1, 4, 6], [1, 3, 4]],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[1, 2, 3], [3, 4], [4, 5, 6], [5, 6], [], [], []],containedBoxes = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [], [], []],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[1, 2, 3], [3, 4], [4, 5, 6], [5, 6], [], [], []],containedBoxes = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [], [], []],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70, 80],keys = [[1, 3, 5, 7], [2, 4, 6], [0, 3, 6], [1, 4, 7], [0, 2, 7], [1, 3, 6], [0, 2, 5], [1, 3, 4]],containedBoxes = [[1, 3, 5, 7], [2, 4, 6], [0, 3, 6], [1, 4, 7], [0, 2, 7], [1, 3, 6], [0, 2, 5], [1, 3, 4]],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70, 80],keys = [[1, 3, 5, 7], [2, 4, 6], [0, 3, 6], [1, 4, 7], [0, 2, 7], [1, 3, 6], [0, 2, 5], [1, 3, 4]],containedBoxes = [[1, 3, 5, 7], [2, 4, 6], [0, 3, 6], [1, 4, 7], [0, 2, 7], [1, 3, 6], [0, 2, 5], [1, 3, 4]],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],keys = [[1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8]],containedBoxes = [[1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8]],initialBoxes = [0, 2, 4, 6, 8]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],keys = [[1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8]],containedBoxes = [[1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8]],initialBoxes = [0, 2, 4, 6, 8]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 1, 1, 1, 1, 1, 1, 1, 1],keys = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [], []],containedBoxes = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [], []],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 1, 1, 1, 1, 1, 1, 1, 1],keys = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [], []],containedBoxes = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [], []],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [500, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],keys = [[], [3, 4, 5], [6, 7, 8], [9, 10], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], [], [5, 6, 7, 8, 9, 10], [], [], [], [], [], [], []],initialBoxes = [0]) == 6000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [500, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],keys = [[], [3, 4, 5], [6, 7, 8], [9, 10], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], [], [5, 6, 7, 8, 9, 10], [], [], [], [], [], [], []],initialBoxes = [0]) == 6000: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],keys = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 660
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],keys = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 660: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8],keys = [[1, 2], [3, 4], [5, 6], [], [7], [], [], []],containedBoxes = [[1, 2], [3, 4], [5, 6], [], [7], [], [], []],initialBoxes = [0]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8],keys = [[1, 2], [3, 4], [5, 6], [], [7], [], [], []],containedBoxes = [[1, 2], [3, 4], [5, 6], [], [7], [], [], []],initialBoxes = [0]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 0, 0, 1, 0],candies = [150, 120, 300, 180, 90, 210],keys = [[1, 4], [2], [3], [4], [], [3]],containedBoxes = [[2], [3], [4], [5], [], []],initialBoxes = [0]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 0, 0, 1, 0],candies = [150, 120, 300, 180, 90, 210],keys = [[1, 4], [2], [3], [4], [], [3]],containedBoxes = [[2], [3], [4], [5], [], []],initialBoxes = [0]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 66
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 66: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 1, 0, 1, 0],candies = [10, 20, 30, 40, 50, 60],keys = [[2, 3], [1, 4], [0, 5], [0, 4], [3, 5], []],containedBoxes = [[2, 5], [4], [], [1], [5], [0]],initialBoxes = [0]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 1, 0, 1, 0],candies = [10, 20, 30, 40, 50, 60],keys = [[2, 3], [1, 4], [0, 5], [0, 4], [3, 5], []],containedBoxes = [[2, 5], [4], [], [1], [5], [0]],initialBoxes = [0]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[1, 3], [2, 4], [5], [], [6], [], []],containedBoxes = [[3, 4], [0, 1, 5], [2, 6], [], [], [], []],initialBoxes = [0]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[1, 3], [2, 4], [5], [], [6], [], []],containedBoxes = [[3, 4], [0, 1, 5], [2, 6], [], [], [], []],initialBoxes = [0]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],candies = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],keys = [[3, 5, 7, 9], [0, 2, 4, 6, 8], [], [], [], [], [], [], [], []],containedBoxes = [[1, 3, 5, 7, 9], [2, 4, 6, 8], [3, 5, 7, 9], [4, 6, 8], [5, 7, 9], [6, 8], [7, 9], [8, 9], [9], []],initialBoxes = [0]) == 3600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],candies = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],keys = [[3, 5, 7, 9], [0, 2, 4, 6, 8], [], [], [], [], [], [], [], []],containedBoxes = [[1, 3, 5, 7, 9], [2, 4, 6, 8], [3, 5, 7, 9], [4, 6, 8], [5, 7, 9], [6, 8], [7, 9], [8, 9], [9], []],initialBoxes = [0]) == 3600: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70, 80],keys = [[1, 4], [2, 5], [3, 6], [0, 7], [6, 3], [0, 7], [1, 4], [2, 5]],containedBoxes = [[2, 5], [4, 6], [7, 0], [3, 1], [6, 5], [0, 2], [5, 4], [7, 1]],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70, 80],keys = [[1, 4], [2, 5], [3, 6], [0, 7], [6, 3], [0, 7], [1, 4], [2, 5]],containedBoxes = [[2, 5], [4, 6], [7, 0], [3, 1], [6, 5], [0, 2], [5, 4], [7, 1]],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 1, 0, 1, 0, 0, 0, 1],candies = [15, 25, 35, 5, 10, 15, 20, 25, 30, 40],keys = [[1, 3], [5], [], [6], [], [], [0], [7], [8], []],containedBoxes = [[1, 2, 3, 4], [5, 6], [7, 8], [], [5, 6], [0, 1, 2], [3, 4], [5, 6], [7, 8], []],initialBoxes = [3, 9]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 1, 0, 1, 0, 0, 0, 1],candies = [15, 25, 35, 5, 10, 15, 20, 25, 30, 40],keys = [[1, 3], [5], [], [6], [], [], [0], [7], [8], []],containedBoxes = [[1, 2, 3, 4], [5, 6], [7, 8], [], [5, 6], [0, 1, 2], [3, 4], [5, 6], [7, 8], []],initialBoxes = [3, 9]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],candies = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],keys = [[1, 3, 5, 7, 9], [2, 4, 6, 8], [], [], [], [], [], [], [], []],containedBoxes = [[1, 3, 5, 7, 9], [2, 4, 6, 8], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],candies = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],keys = [[1, 3, 5, 7, 9], [2, 4, 6, 8], [], [], [], [], [], [], [], []],containedBoxes = [[1, 3, 5, 7, 9], [2, 4, 6, 8], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 275: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 1, 0, 1, 0, 0],candies = [10, 20, 30, 40, 50, 60],keys = [[1, 2], [4], [3, 5], [], [5], []],containedBoxes = [[2, 3], [3], [4], [], [5], []],initialBoxes = [0]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 1, 0, 1, 0, 0],candies = [10, 20, 30, 40, 50, 60],keys = [[1, 2], [4], [3, 5], [], [5], []],containedBoxes = [[2, 3], [3], [4], [], [5], []],initialBoxes = [0]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],keys = [[1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]],containedBoxes = [[1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],keys = [[1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]],containedBoxes = [[1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90],keys = [[1, 2], [3, 4], [5, 6], [7, 8], [], [], [], [], []],containedBoxes = [[1, 2], [3, 4], [5, 6], [7, 8], [], [], [], [], []],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90],keys = [[1, 2], [3, 4], [5, 6], [7, 8], [], [], [], [], []],containedBoxes = [[1, 2], [3, 4], [5, 6], [7, 8], [], [], [], [], []],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11], [], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11], [], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11], [], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11], [], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 0, 1, 0, 0, 0, 1],candies = [100, 200, 300, 400, 500, 600, 700, 800],keys = [[1, 3, 7], [2, 5], [4, 6], [], [], [], [], []],containedBoxes = [[2, 5, 6], [3, 4, 7], [1, 5, 7], [0, 4, 6], [], [], [], [0, 2]],initialBoxes = [0, 3]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 0, 1, 0, 0, 0, 1],candies = [100, 200, 300, 400, 500, 600, 700, 800],keys = [[1, 3, 7], [2, 5], [4, 6], [], [], [], [], []],containedBoxes = [[2, 5, 6], [3, 4, 7], [1, 5, 7], [0, 4, 6], [], [], [], [0, 2]],initialBoxes = [0, 3]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0],candies = [5, 10, 15, 20, 25, 30, 35],keys = [[1, 2, 3, 4, 5, 6], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6], [], [], [], [], [], []],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0],candies = [5, 10, 15, 20, 25, 30, 35],keys = [[1, 2, 3, 4, 5, 6], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6], [], [], [], [], [], []],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 0, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[2, 3], [4], [], [], [], [6], [1]],containedBoxes = [[1, 2, 3], [], [4, 5], [], [], [], []],initialBoxes = [0]) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 0, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[2, 3], [4], [], [], [], [6], [1]],containedBoxes = [[1, 2, 3], [], [4, 5], [], [], [], []],initialBoxes = [0]) == 130: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9], [], [5, 6, 7, 8, 9], [6, 7, 8, 9], [7, 8, 9], [8, 9], [9], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [3, 4, 5, 6, 7, 8, 9], [], [6, 7, 8, 9], [7, 8, 9], [8, 9], [9], [], [], []],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9], [], [5, 6, 7, 8, 9], [6, 7, 8, 9], [7, 8, 9], [8, 9], [9], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [3, 4, 5, 6, 7, 8, 9], [], [6, 7, 8, 9], [7, 8, 9], [8, 9], [9], [], [], []],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 1, 0, 0, 1, 0],candies = [10, 50, 20, 60, 30, 40, 70],keys = [[3], [1, 4], [5], [], [0], [], [2]],containedBoxes = [[2, 4], [5], [], [6], [], [0, 2], []],initialBoxes = [0]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 1, 0, 0, 1, 0],candies = [10, 50, 20, 60, 30, 40, 70],keys = [[3], [1, 4], [5], [], [0], [], [2]],containedBoxes = [[2, 4], [5], [], [6], [], [0, 2], []],initialBoxes = [0]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],keys = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9], [8, 9], [9], []],containedBoxes = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9], [8, 9], [9], []],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],keys = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9], [8, 9], [9], []],containedBoxes = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9], [8, 9], [9], []],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],keys = [[], [], [], [], [], [], [], [], [], [0, 1, 2, 3, 4, 5, 6, 7, 8]],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [0, 1, 2, 3, 4, 5, 6, 7, 8]],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],keys = [[], [], [], [], [], [], [], [], [], [0, 1, 2, 3, 4, 5, 6, 7, 8]],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [0, 1, 2, 3, 4, 5, 6, 7, 8]],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80],keys = [[1, 3, 5], [2, 4, 6], [3, 4], [0, 5, 6], [0, 2, 4], [0, 3, 5], [2, 4, 6], [1, 2, 3]],containedBoxes = [[1, 2, 3], [4, 5, 6], [0, 3, 5], [2, 4, 6], [0, 1, 5], [2, 3, 4], [0, 1, 4], [0, 1, 2, 3, 4, 5, 6]],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80],keys = [[1, 3, 5], [2, 4, 6], [3, 4], [0, 5, 6], [0, 2, 4], [0, 3, 5], [2, 4, 6], [1, 2, 3]],containedBoxes = [[1, 2, 3], [4, 5, 6], [0, 3, 5], [2, 4, 6], [0, 1, 5], [2, 3, 4], [0, 1, 4], [0, 1, 2, 3, 4, 5, 6]],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 1, 0, 0, 0, 1, 0],candies = [1, 2, 3, 4, 5, 6, 7],keys = [[1, 2, 3, 4, 5, 6], [], [4, 5], [5, 6], [1, 3, 5], [], [2, 4]],containedBoxes = [[1, 2, 3, 4, 5, 6], [], [3, 4], [3, 5], [1, 3, 5], [], [2, 4]],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 1, 0, 0, 0, 1, 0],candies = [1, 2, 3, 4, 5, 6, 7],keys = [[1, 2, 3, 4, 5, 6], [], [4, 5], [5, 6], [1, 3, 5], [], [2, 4]],containedBoxes = [[1, 2, 3, 4, 5, 6], [], [3, 4], [3, 5], [1, 3, 5], [], [2, 4]],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 1, 0, 0, 1],candies = [10, 20, 30, 40, 50, 60],keys = [[3, 4], [1], [2], [0], [5], []],containedBoxes = [[1, 2], [3], [4], [5], [], []],initialBoxes = [0]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 1, 0, 0, 1],candies = [10, 20, 30, 40, 50, 60],keys = [[3, 4], [1], [2], [0], [5], []],containedBoxes = [[1, 2], [3], [4], [5], [], []],initialBoxes = [0]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 1, 1, 1, 1, 1, 1, 1],candies = [100, 200, 300, 400, 500, 600, 700, 800],keys = [[], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7], [], [], [], [], [], [], []],initialBoxes = [0]) == 3600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 1, 1, 1, 1, 1, 1, 1],candies = [100, 200, 300, 400, 500, 600, 700, 800],keys = [[], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7], [], [], [], [], [], [], []],initialBoxes = [0]) == 3600: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],candies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],keys = [[1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [], [], [], [], [], [], [], []],containedBoxes = [[1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [], [], [], [], [], [], [], []],initialBoxes = [1, 3, 5, 7, 9]) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],candies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],keys = [[1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [], [], [], [], [], [], [], []],containedBoxes = [[1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [], [], [], [], [], [], [], []],initialBoxes = [1, 3, 5, 7, 9]) == 55: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 1, 0, 0, 1],candies = [50, 20, 10, 80, 60, 90],keys = [[3, 4], [2, 5], [], [], [], [1]],containedBoxes = [[1, 2], [3, 5], [], [], [2], []],initialBoxes = [0]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 1, 0, 0, 1],candies = [50, 20, 10, 80, 60, 90],keys = [[3, 4], [2, 5], [], [], [], [1]],containedBoxes = [[1, 2], [3, 5], [], [], [2], []],initialBoxes = [0]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 0, 1, 0, 1],candies = [100, 200, 300, 400, 500, 600],keys = [[2, 4], [], [1], [5], [], [0]],containedBoxes = [[3, 4, 5], [], [], [], [], [2]],initialBoxes = [0]) == 1900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 0, 1, 0, 1],candies = [100, 200, 300, 400, 500, 600],keys = [[2, 4], [], [1], [5], [], [0]],containedBoxes = [[3, 4, 5], [], [], [], [], [2]],initialBoxes = [0]) == 1900: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],keys = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [], [], [], [], [], [], []],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],keys = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [], [], [], [], [], [], []],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [9], []],initialBoxes = [9]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [9], []],initialBoxes = [9]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 1, 0, 1, 0, 1, 0, 1],candies = [5, 10, 15, 20, 25, 30, 35, 40],keys = [[1, 3, 5, 7], [], [3, 5, 7], [], [3, 5, 7], [], [3, 5, 7], []],containedBoxes = [[1, 3, 5, 7], [], [1, 3, 5, 7], [], [1, 3, 5, 7], [], [1, 3, 5, 7], []],initialBoxes = [0, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 1, 0, 1, 0, 1, 0, 1],candies = [5, 10, 15, 20, 25, 30, 35, 40],keys = [[1, 3, 5, 7], [], [3, 5, 7], [], [3, 5, 7], [], [3, 5, 7], []],containedBoxes = [[1, 3, 5, 7], [], [1, 3, 5, 7], [], [1, 3, 5, 7], [], [1, 3, 5, 7], []],initialBoxes = [0, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8],keys = [[1], [2], [3], [4], [5], [6], [7], []],containedBoxes = [[1], [2], [3], [4], [5], [6], [7], []],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8],keys = [[1], [2], [3], [4], [5], [6], [7], []],containedBoxes = [[1], [2], [3], [4], [5], [6], [7], []],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[1], [2], [3], [4], [5], [6], []],containedBoxes = [[2], [3], [4], [5], [6], [7], []],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[1], [2], [3], [4], [5], [6], []],containedBoxes = [[2], [3], [4], [5], [6], [7], []],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 1, 0, 0, 0, 1],candies = [220, 130, 50, 110, 80, 70, 60],keys = [[1, 2], [3, 4], [5, 6], [], [], [], [1]],containedBoxes = [[3, 4], [5], [6], [], [], [], [0]],initialBoxes = [2]) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 1, 0, 0, 0, 1],candies = [220, 130, 50, 110, 80, 70, 60],keys = [[1, 2], [3, 4], [5, 6], [], [], [], [1]],containedBoxes = [[3, 4], [5], [6], [], [], [], [0]],initialBoxes = [2]) == 110: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 1, 0, 1, 0, 1, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80],keys = [[1], [3], [5], [7], [], [], [], []],containedBoxes = [[1, 3, 5, 7], [], [], [], [], [], [], []],initialBoxes = [0, 2, 4, 6]) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 1, 0, 1, 0, 1, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80],keys = [[1], [3], [5], [7], [], [], [], []],containedBoxes = [[1, 3, 5, 7], [], [], [], [], [], [], []],initialBoxes = [0, 2, 4, 6]) == 360: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 1, 0, 1, 0, 1, 0],candies = [1, 3, 5, 7, 9, 11, 13, 15],keys = [[2, 4, 6], [1, 3, 5], [], [], [], [], [], []],containedBoxes = [[1, 3, 5], [2, 4, 6], [], [], [], [], [], []],initialBoxes = [0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 1, 0, 1, 0, 1, 0],candies = [1, 3, 5, 7, 9, 11, 13, 15],keys = [[2, 4, 6], [1, 3, 5], [], [], [], [], [], []],containedBoxes = [[1, 3, 5], [2, 4, 6], [], [], [], [], [], []],initialBoxes = [0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 1, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60],keys = [[1, 2, 3, 4, 5], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5], [], [], [], [], []],initialBoxes = [0]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 1, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60],keys = [[1, 2, 3, 4, 5], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5], [], [], [], [], []],initialBoxes = [0]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 1, 0, 0, 0, 0, 0, 0],candies = [50, 30, 40, 20, 10, 70, 60, 80],keys = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7], [], []],containedBoxes = [[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7], [], [], []],initialBoxes = [0, 1]) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 1, 0, 0, 0, 0, 0, 0],candies = [50, 30, 40, 20, 10, 70, 60, 80],keys = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7], [], []],containedBoxes = [[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7], [], [], []],initialBoxes = [0, 1]) == 360: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60],keys = [[2, 3], [0, 5], [3, 4], [0, 5], [1, 2], [4]],containedBoxes = [[3, 4], [1, 5], [0, 4], [0, 1], [1, 3], [0]],initialBoxes = [3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60],keys = [[2, 3], [0, 5], [3, 4], [0, 5], [1, 2], [4]],containedBoxes = [[3, 4], [1, 5], [0, 4], [0, 1], [1, 3], [0]],initialBoxes = [3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 1, 0, 0, 0, 1, 0],candies = [5, 15, 25, 35, 45, 55, 65],keys = [[3], [4], [], [6], [2], [], [0]],containedBoxes = [[2, 3, 4], [1, 5], [], [], [], [], []],initialBoxes = [0, 1]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 1, 0, 0, 0, 1, 0],candies = [5, 15, 25, 35, 45, 55, 65],keys = [[3], [4], [], [6], [2], [], [0]],containedBoxes = [[2, 3, 4], [1, 5], [], [], [], [], []],initialBoxes = [0, 1]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8, 9],keys = [[1, 3, 5], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 7], [1, 5, 8], [0, 2, 6], [2, 3, 5]],containedBoxes = [[1, 3, 5], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 7], [1, 5, 8], [0, 2, 6], [2, 3, 5]],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8, 9],keys = [[1, 3, 5], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 7], [1, 5, 8], [0, 2, 6], [2, 3, 5]],containedBoxes = [[1, 3, 5], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 7], [1, 5, 8], [0, 2, 6], [2, 3, 5]],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 1, 0, 1, 0, 1],candies = [100, 200, 300, 400, 500, 600, 700],keys = [[1], [2], [3], [4], [5], [6], []],containedBoxes = [[1, 3, 5], [2, 4, 6], [3, 5, 6], [4, 5, 6], [5, 6], [6], []],initialBoxes = [0]) == 2800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 1, 0, 1, 0, 1],candies = [100, 200, 300, 400, 500, 600, 700],keys = [[1], [2], [3], [4], [5], [6], []],containedBoxes = [[1, 3, 5], [2, 4, 6], [3, 5, 6], [4, 5, 6], [5, 6], [6], []],initialBoxes = [0]) == 2800: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 1, 1, 1, 1],candies = [10, 20, 30, 40, 50],keys = [[], [3, 4], [4], [], []],containedBoxes = [[1, 2, 3], [2, 3, 4], [3, 4], [], []],initialBoxes = [0]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 1, 1, 1, 1],candies = [10, 20, 30, 40, 50],keys = [[], [3, 4], [4], [], []],containedBoxes = [[1, 2, 3], [2, 3, 4], [3, 4], [], []],initialBoxes = [0]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],candies = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],keys = [[1, 2], [3, 4], [5, 6], [7, 8], [9], [0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],containedBoxes = [[4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9], [6, 7, 8, 9], [7, 8, 9], [8, 9], [9, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]],initialBoxes = [0]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],candies = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],keys = [[1, 2], [3, 4], [5, 6], [7, 8], [9], [0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],containedBoxes = [[4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9], [6, 7, 8, 9], [7, 8, 9], [8, 9], [9, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]],initialBoxes = [0]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],candies = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [1], [], [], []],containedBoxes = [[2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [0], [], [], []],initialBoxes = [0, 6]) == 265
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],candies = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [1], [], [], []],containedBoxes = [[2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [0], [], [], []],initialBoxes = [0, 6]) == 265: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],candies = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],candies = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 1, 0, 1, 0],candies = [5, 10, 15, 20, 25, 30],keys = [[2], [1, 3], [4], [0, 5], [], []],containedBoxes = [[2, 3], [1, 4], [0, 5], [], [], [2]],initialBoxes = [0]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 1, 0, 1, 0],candies = [5, 10, 15, 20, 25, 30],keys = [[2], [1, 3], [4], [0, 5], [], []],containedBoxes = [[2, 3], [1, 4], [0, 5], [], [], [2]],initialBoxes = [0]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6], []],containedBoxes = [[1, 2, 3, 4, 5, 6], [], [], [], [], [], []],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6], []],containedBoxes = [[1, 2, 3, 4, 5, 6], [], [], [], [], [], []],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],candies = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],keys = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [], [0, 1], [2, 3], [4, 5], [6, 7], [8, 9], []],containedBoxes = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [], [0, 1], [2, 3], [4, 5], [6, 7], [8, 9], []],initialBoxes = [0, 2, 4, 6, 8]) == 275
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],candies = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],keys = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [], [0, 1], [2, 3], [4, 5], [6, 7], [8, 9], []],containedBoxes = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [], [0, 1], [2, 3], [4, 5], [6, 7], [8, 9], []],initialBoxes = [0, 2, 4, 6, 8]) == 275: {e}')
    
    total += 1
    try:
        result = candidate(status = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],candies = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],keys = [[1, 2], [3, 4], [5, 6], [7, 8], [9], [0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],containedBoxes = [[3, 4, 5], [6, 7, 8], [9], [0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 1], [2, 3]],initialBoxes = [0]) == 2500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],candies = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],keys = [[1, 2], [3, 4], [5, 6], [7, 8], [9], [0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],containedBoxes = [[3, 4, 5], [6, 7, 8], [9], [0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 1], [2, 3]],initialBoxes = [0]) == 2500: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],candies = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],keys = [[2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7]],containedBoxes = [[4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9], [6, 7, 8, 9], [7, 8, 9], [8, 9], [9, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],candies = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],keys = [[2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7]],containedBoxes = [[4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9], [6, 7, 8, 9], [7, 8, 9], [8, 9], [9, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]],initialBoxes = [0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70, 80],keys = [[2], [3], [4], [5], [6], [7], [], [1]],containedBoxes = [[1, 3, 5, 7], [2, 4, 6], [3, 5, 7], [4, 6], [5, 7], [6, 7], [], []],initialBoxes = [0, 1]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70, 80],keys = [[2], [3], [4], [5], [6], [7], [], [1]],containedBoxes = [[1, 3, 5, 7], [2, 4, 6], [3, 5, 7], [4, 6], [5, 7], [6, 7], [], []],initialBoxes = [0, 1]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(status = [0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80],keys = [[1, 2], [3, 4], [5, 6], [7], [6], [5], [4], [3]],containedBoxes = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 0], [7, 1], [0, 2]],initialBoxes = [0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(status = [0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80],keys = [[1, 2], [3, 4], [5, 6], [7], [6], [5], [4], [3]],containedBoxes = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 0], [7, 1], [0, 2]],initialBoxes = [0]) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(status = [0, 0, 0],candies = [100, 200, 300],keys = [[1, 2], [0, 2], [0, 1]],containedBoxes = [[1, 2], [0, 2], [0, 1]],initialBoxes = [0]) == 0
    assert candidate(status = [0, 0, 0],candies = [10, 20, 30],keys = [[1], [2], []],containedBoxes = [[], [], []],initialBoxes = [0]) == 0
    assert candidate(status = [1, 1, 0, 0, 1],candies = [5, 15, 25, 35, 45],keys = [[2, 3], [], [4], [], []],containedBoxes = [[1, 2], [3], [], [], []],initialBoxes = [0]) == 80
    assert candidate(status = [1, 1, 0, 0],candies = [10, 20, 30, 40],keys = [[], [], [2], [3]],containedBoxes = [[2, 3], [], [], []],initialBoxes = [0, 1]) == 30
    assert candidate(status = [1, 1, 0, 0],candies = [10, 20, 30, 40],keys = [[2], [3], [], []],containedBoxes = [[], [], [1, 3], []],initialBoxes = [0, 1]) == 30
    assert candidate(status = [1, 0, 1, 0, 1],candies = [3, 5, 2, 7, 6],keys = [[2], [1, 4], [0], [], [3]],containedBoxes = [[4], [3], [], [1], [2]],initialBoxes = [0]) == 11
    assert candidate(status = [0, 0, 1, 1],candies = [10, 20, 30, 40],keys = [[1, 3], [0], [], []],containedBoxes = [[2], [3], [], []],initialBoxes = [2]) == 30
    assert candidate(status = [0, 0, 1, 1],candies = [10, 20, 30, 40],keys = [[1, 2], [0], [3], []],containedBoxes = [[2, 3], [1], [], []],initialBoxes = [2]) == 30
    assert candidate(status = [1, 1, 1],candies = [5, 10, 15],keys = [[], [2], []],containedBoxes = [[1], [], []],initialBoxes = [0]) == 15
    assert candidate(status = [1, 0, 0, 0, 0, 0],candies = [1, 1, 1, 1, 1, 1],keys = [[1, 2, 3, 4, 5], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5], [], [], [], [], []],initialBoxes = [0]) == 6
    assert candidate(status = [0, 0, 0, 0],candies = [100, 200, 300, 400],keys = [[1, 2], [2, 3], [3], []],containedBoxes = [[1, 2, 3], [], [], []],initialBoxes = [0]) == 0
    assert candidate(status = [1, 0, 0],candies = [100, 200, 300],keys = [[1], [], [2]],containedBoxes = [[2], [], []],initialBoxes = [0]) == 100
    assert candidate(status = [0, 0, 1, 1],candies = [2, 3, 5, 7],keys = [[1, 2], [2, 3], [], []],containedBoxes = [[2, 3], [3], [], []],initialBoxes = [0]) == 0
    assert candidate(status = [1, 0, 1, 0],candies = [7, 5, 4, 100],keys = [[], [], [1], []],containedBoxes = [[1, 2], [3], [], []],initialBoxes = [0]) == 16
    assert candidate(status = [1, 1, 1],candies = [5, 5, 5],keys = [[], [2], [1]],containedBoxes = [[1, 2], [0, 2], [0, 1]],initialBoxes = [0]) == 15
    assert candidate(status = [1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[3, 5], [0, 2], [4], [], [6], [], []],containedBoxes = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 0], [6, 1], [0, 2]],initialBoxes = [0]) == 260
    assert candidate(status = [0, 1, 0, 1, 0, 1, 0],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[1, 3, 5], [2, 4, 6], [3, 4], [0, 5, 6], [0, 2, 4], [0, 3, 5], [2, 4, 6]],containedBoxes = [[1, 2, 3], [4, 5, 6], [0, 3, 5], [2, 4, 6], [0, 1, 5], [2, 3, 4], [0, 1, 4]],initialBoxes = [0]) == 0
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],keys = [[1, 2], [3, 4], [5, 6], [7, 8], [9], [], [], [], [], []],containedBoxes = [[3, 4, 5], [6, 7, 8], [9], [], [], [0, 1, 2], [3, 4, 5], [6, 7, 8], [9], [0, 1, 2]],initialBoxes = [0]) == 0
    assert candidate(status = [0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60],keys = [[1, 2], [0], [3], [4], [5], []],containedBoxes = [[2, 3], [0, 3], [1, 4], [2, 5], [3], []],initialBoxes = [1]) == 210
    assert candidate(status = [1, 0, 1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90],keys = [[1, 3, 5, 7, 8], [2, 4, 6], [0, 3, 6, 8], [1, 4, 7], [0, 2, 7, 8], [1, 3, 6], [0, 2, 5, 8], [1, 3, 4, 8], [0, 1, 2, 3, 4, 5, 6, 7]],containedBoxes = [[1, 3, 5, 7, 8], [2, 4, 6], [0, 3, 6, 8], [1, 4, 7], [0, 2, 7, 8], [1, 3, 6], [0, 2, 5, 8], [1, 3, 4, 8], [0, 1, 2, 3, 4, 5, 6, 7]],initialBoxes = [0]) == 450
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],keys = [[1, 3, 5, 7], [2, 4, 6, 8], [], [], [], [], [], [], [], []],containedBoxes = [[1, 3, 5, 7], [2, 4, 6, 8], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 0
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0],candies = [50, 100, 150, 200, 250, 300, 350],keys = [[2, 3], [1, 3], [0, 2, 4], [0, 1, 2, 5], [0, 3, 5, 6], [1, 4, 6], [1, 3, 4]],containedBoxes = [[1, 2, 3], [0, 2, 4], [0, 1, 5], [0, 1, 2, 5], [0, 3, 5, 6], [1, 4, 6], [1, 3, 4]],initialBoxes = [0]) == 0
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[1, 2, 3], [3, 4], [4, 5, 6], [5, 6], [], [], []],containedBoxes = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [], [], []],initialBoxes = [0]) == 0
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 0
    assert candidate(status = [0, 1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70, 80],keys = [[1, 3, 5, 7], [2, 4, 6], [0, 3, 6], [1, 4, 7], [0, 2, 7], [1, 3, 6], [0, 2, 5], [1, 3, 4]],containedBoxes = [[1, 3, 5, 7], [2, 4, 6], [0, 3, 6], [1, 4, 7], [0, 2, 7], [1, 3, 6], [0, 2, 5], [1, 3, 4]],initialBoxes = [0]) == 0
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],keys = [[1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8]],containedBoxes = [[1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8], [1, 3, 5, 7], [2, 4, 6, 8]],initialBoxes = [0, 2, 4, 6, 8]) == 0
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 1, 1, 1, 1, 1, 1, 1, 1],keys = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [], []],containedBoxes = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [], []],initialBoxes = [0]) == 0
    assert candidate(status = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [500, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],keys = [[], [3, 4, 5], [6, 7, 8], [9, 10], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], [], [5, 6, 7, 8, 9, 10], [], [], [], [], [], [], []],initialBoxes = [0]) == 6000
    assert candidate(status = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],keys = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 660
    assert candidate(status = [1, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8],keys = [[1, 2], [3, 4], [5, 6], [], [7], [], [], []],containedBoxes = [[1, 2], [3, 4], [5, 6], [], [7], [], [], []],initialBoxes = [0]) == 36
    assert candidate(status = [1, 0, 0, 0, 1, 0],candies = [150, 120, 300, 180, 90, 210],keys = [[1, 4], [2], [3], [4], [], [3]],containedBoxes = [[2], [3], [4], [5], [], []],initialBoxes = [0]) == 150
    assert candidate(status = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 66
    assert candidate(status = [1, 0, 1, 0, 1, 0],candies = [10, 20, 30, 40, 50, 60],keys = [[2, 3], [1, 4], [0, 5], [0, 4], [3, 5], []],containedBoxes = [[2, 5], [4], [], [1], [5], [0]],initialBoxes = [0]) == 100
    assert candidate(status = [1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[1, 3], [2, 4], [5], [], [6], [], []],containedBoxes = [[3, 4], [0, 1, 5], [2, 6], [], [], [], []],initialBoxes = [0]) == 100
    assert candidate(status = [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],candies = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],keys = [[3, 5, 7, 9], [0, 2, 4, 6, 8], [], [], [], [], [], [], [], []],containedBoxes = [[1, 3, 5, 7, 9], [2, 4, 6, 8], [3, 5, 7, 9], [4, 6, 8], [5, 7, 9], [6, 8], [7, 9], [8, 9], [9], []],initialBoxes = [0]) == 3600
    assert candidate(status = [0, 1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70, 80],keys = [[1, 4], [2, 5], [3, 6], [0, 7], [6, 3], [0, 7], [1, 4], [2, 5]],containedBoxes = [[2, 5], [4, 6], [7, 0], [3, 1], [6, 5], [0, 2], [5, 4], [7, 1]],initialBoxes = [0]) == 0
    assert candidate(status = [0, 0, 0, 1, 0, 1, 0, 0, 0, 1],candies = [15, 25, 35, 5, 10, 15, 20, 25, 30, 40],keys = [[1, 3], [5], [], [6], [], [], [0], [7], [8], []],containedBoxes = [[1, 2, 3, 4], [5, 6], [7, 8], [], [5, 6], [0, 1, 2], [3, 4], [5, 6], [7, 8], []],initialBoxes = [3, 9]) == 45
    assert candidate(status = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],candies = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],keys = [[1, 3, 5, 7, 9], [2, 4, 6, 8], [], [], [], [], [], [], [], []],containedBoxes = [[1, 3, 5, 7, 9], [2, 4, 6, 8], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 275
    assert candidate(status = [1, 1, 0, 1, 0, 0],candies = [10, 20, 30, 40, 50, 60],keys = [[1, 2], [4], [3, 5], [], [5], []],containedBoxes = [[2, 3], [3], [4], [], [5], []],initialBoxes = [0]) == 80
    assert candidate(status = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],keys = [[1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]],containedBoxes = [[1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]],initialBoxes = [0]) == 0
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90],keys = [[1, 2], [3, 4], [5, 6], [7, 8], [], [], [], [], []],containedBoxes = [[1, 2], [3, 4], [5, 6], [7, 8], [], [], [], [], []],initialBoxes = [0]) == 0
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 0
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11], [], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11], [], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 0
    assert candidate(status = [1, 0, 0, 1, 0, 0, 0, 1],candies = [100, 200, 300, 400, 500, 600, 700, 800],keys = [[1, 3, 7], [2, 5], [4, 6], [], [], [], [], []],containedBoxes = [[2, 5, 6], [3, 4, 7], [1, 5, 7], [0, 4, 6], [], [], [], [0, 2]],initialBoxes = [0, 3]) == 500
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0],candies = [5, 10, 15, 20, 25, 30, 35],keys = [[1, 2, 3, 4, 5, 6], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6], [], [], [], [], [], []],initialBoxes = [0]) == 0
    assert candidate(status = [1, 0, 0, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[2, 3], [4], [], [], [], [6], [1]],containedBoxes = [[1, 2, 3], [], [4, 5], [], [], [], []],initialBoxes = [0]) == 130
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9], [], [5, 6, 7, 8, 9], [6, 7, 8, 9], [7, 8, 9], [8, 9], [9], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [3, 4, 5, 6, 7, 8, 9], [], [6, 7, 8, 9], [7, 8, 9], [8, 9], [9], [], [], []],initialBoxes = [0]) == 0
    assert candidate(status = [1, 0, 1, 0, 0, 1, 0],candies = [10, 50, 20, 60, 30, 40, 70],keys = [[3], [1, 4], [5], [], [0], [], [2]],containedBoxes = [[2, 4], [5], [], [6], [], [0, 2], []],initialBoxes = [0]) == 30
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],keys = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9], [8, 9], [9], []],containedBoxes = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9], [7, 8, 9], [8, 9], [9], []],initialBoxes = [0]) == 0
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],keys = [[], [], [], [], [], [], [], [], [], [0, 1, 2, 3, 4, 5, 6, 7, 8]],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [0, 1, 2, 3, 4, 5, 6, 7, 8]],initialBoxes = [0]) == 0
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80],keys = [[1, 3, 5], [2, 4, 6], [3, 4], [0, 5, 6], [0, 2, 4], [0, 3, 5], [2, 4, 6], [1, 2, 3]],containedBoxes = [[1, 2, 3], [4, 5, 6], [0, 3, 5], [2, 4, 6], [0, 1, 5], [2, 3, 4], [0, 1, 4], [0, 1, 2, 3, 4, 5, 6]],initialBoxes = [0]) == 0
    assert candidate(status = [0, 1, 0, 0, 0, 1, 0],candies = [1, 2, 3, 4, 5, 6, 7],keys = [[1, 2, 3, 4, 5, 6], [], [4, 5], [5, 6], [1, 3, 5], [], [2, 4]],containedBoxes = [[1, 2, 3, 4, 5, 6], [], [3, 4], [3, 5], [1, 3, 5], [], [2, 4]],initialBoxes = [0]) == 0
    assert candidate(status = [1, 0, 1, 0, 0, 1],candies = [10, 20, 30, 40, 50, 60],keys = [[3, 4], [1], [2], [0], [5], []],containedBoxes = [[1, 2], [3], [4], [5], [], []],initialBoxes = [0]) == 90
    assert candidate(status = [1, 1, 1, 1, 1, 1, 1, 1],candies = [100, 200, 300, 400, 500, 600, 700, 800],keys = [[], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7], [], [], [], [], [], [], []],initialBoxes = [0]) == 3600
    assert candidate(status = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],candies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],keys = [[1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [], [], [], [], [], [], [], []],containedBoxes = [[1, 3, 5, 7, 9], [0, 2, 4, 6, 8], [], [], [], [], [], [], [], []],initialBoxes = [1, 3, 5, 7, 9]) == 55
    assert candidate(status = [1, 0, 1, 0, 0, 1],candies = [50, 20, 10, 80, 60, 90],keys = [[3, 4], [2, 5], [], [], [], [1]],containedBoxes = [[1, 2], [3, 5], [], [], [2], []],initialBoxes = [0]) == 60
    assert candidate(status = [1, 0, 0, 1, 0, 1],candies = [100, 200, 300, 400, 500, 600],keys = [[2, 4], [], [1], [5], [], [0]],containedBoxes = [[3, 4, 5], [], [], [], [], [2]],initialBoxes = [0]) == 1900
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],keys = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [], [], [], [], [], [], []],initialBoxes = [0]) == 0
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [9], []],initialBoxes = [9]) == 100
    assert candidate(status = [0, 1, 0, 1, 0, 1, 0, 1],candies = [5, 10, 15, 20, 25, 30, 35, 40],keys = [[1, 3, 5, 7], [], [3, 5, 7], [], [3, 5, 7], [], [3, 5, 7], []],containedBoxes = [[1, 3, 5, 7], [], [1, 3, 5, 7], [], [1, 3, 5, 7], [], [1, 3, 5, 7], []],initialBoxes = [0, 1]) == 10
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8],keys = [[1], [2], [3], [4], [5], [6], [7], []],containedBoxes = [[1], [2], [3], [4], [5], [6], [7], []],initialBoxes = [0]) == 0
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[1], [2], [3], [4], [5], [6], []],containedBoxes = [[2], [3], [4], [5], [6], [7], []],initialBoxes = [0]) == 0
    assert candidate(status = [0, 0, 1, 0, 0, 0, 1],candies = [220, 130, 50, 110, 80, 70, 60],keys = [[1, 2], [3, 4], [5, 6], [], [], [], [1]],containedBoxes = [[3, 4], [5], [6], [], [], [], [0]],initialBoxes = [2]) == 110
    assert candidate(status = [1, 0, 1, 0, 1, 0, 1, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80],keys = [[1], [3], [5], [7], [], [], [], []],containedBoxes = [[1, 3, 5, 7], [], [], [], [], [], [], []],initialBoxes = [0, 2, 4, 6]) == 360
    assert candidate(status = [1, 0, 1, 0, 1, 0, 1, 0],candies = [1, 3, 5, 7, 9, 11, 13, 15],keys = [[2, 4, 6], [1, 3, 5], [], [], [], [], [], []],containedBoxes = [[1, 3, 5], [2, 4, 6], [], [], [], [], [], []],initialBoxes = [0]) == 1
    assert candidate(status = [1, 1, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60],keys = [[1, 2, 3, 4, 5], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5], [], [], [], [], []],initialBoxes = [0]) == 210
    assert candidate(status = [1, 1, 0, 0, 0, 0, 0, 0],candies = [50, 30, 40, 20, 10, 70, 60, 80],keys = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7], [], []],containedBoxes = [[2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7], [], [], []],initialBoxes = [0, 1]) == 360
    assert candidate(status = [0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60],keys = [[2, 3], [0, 5], [3, 4], [0, 5], [1, 2], [4]],containedBoxes = [[3, 4], [1, 5], [0, 4], [0, 1], [1, 3], [0]],initialBoxes = [3]) == 0
    assert candidate(status = [1, 1, 0, 0, 0, 1, 0],candies = [5, 15, 25, 35, 45, 55, 65],keys = [[3], [4], [], [6], [2], [], [0]],containedBoxes = [[2, 3, 4], [1, 5], [], [], [], [], []],initialBoxes = [0, 1]) == 180
    assert candidate(status = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 5500
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0, 0, 0],candies = [1, 2, 3, 4, 5, 6, 7, 8, 9],keys = [[1, 3, 5], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 7], [1, 5, 8], [0, 2, 6], [2, 3, 5]],containedBoxes = [[1, 3, 5], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 7], [1, 5, 8], [0, 2, 6], [2, 3, 5]],initialBoxes = [0]) == 0
    assert candidate(status = [1, 0, 1, 0, 1, 0, 1],candies = [100, 200, 300, 400, 500, 600, 700],keys = [[1], [2], [3], [4], [5], [6], []],containedBoxes = [[1, 3, 5], [2, 4, 6], [3, 5, 6], [4, 5, 6], [5, 6], [6], []],initialBoxes = [0]) == 2800
    assert candidate(status = [1, 1, 1, 1, 1],candies = [10, 20, 30, 40, 50],keys = [[], [3, 4], [4], [], []],containedBoxes = [[1, 2, 3], [2, 3, 4], [3, 4], [], []],initialBoxes = [0]) == 150
    assert candidate(status = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],candies = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],keys = [[1, 2], [3, 4], [5, 6], [7, 8], [9], [0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],containedBoxes = [[4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9], [6, 7, 8, 9], [7, 8, 9], [8, 9], [9, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]],initialBoxes = [0]) == 500
    assert candidate(status = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],candies = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [1], [], [], []],containedBoxes = [[2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [0], [], [], []],initialBoxes = [0, 6]) == 265
    assert candidate(status = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],candies = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],keys = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],containedBoxes = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [], [], [], [], [], [], [], [], []],initialBoxes = [0]) == 100
    assert candidate(status = [1, 0, 1, 0, 1, 0],candies = [5, 10, 15, 20, 25, 30],keys = [[2], [1, 3], [4], [0, 5], [], []],containedBoxes = [[2, 3], [1, 4], [0, 5], [], [], [2]],initialBoxes = [0]) == 20
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70],keys = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6], []],containedBoxes = [[1, 2, 3, 4, 5, 6], [], [], [], [], [], []],initialBoxes = [0]) == 0
    assert candidate(status = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],candies = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],keys = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [], [0, 1], [2, 3], [4, 5], [6, 7], [8, 9], []],containedBoxes = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [], [0, 1], [2, 3], [4, 5], [6, 7], [8, 9], []],initialBoxes = [0, 2, 4, 6, 8]) == 275
    assert candidate(status = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],candies = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],keys = [[1, 2], [3, 4], [5, 6], [7, 8], [9], [0, 1], [2, 3], [4, 5], [6, 7], [8, 9]],containedBoxes = [[3, 4, 5], [6, 7, 8], [9], [0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [0, 1], [2, 3]],initialBoxes = [0]) == 2500
    assert candidate(status = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],candies = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],keys = [[2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7]],containedBoxes = [[4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9], [6, 7, 8, 9], [7, 8, 9], [8, 9], [9, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]],initialBoxes = [0]) == 0
    assert candidate(status = [0, 1, 0, 1, 0, 1, 0, 1],candies = [10, 20, 30, 40, 50, 60, 70, 80],keys = [[2], [3], [4], [5], [6], [7], [], [1]],containedBoxes = [[1, 3, 5, 7], [2, 4, 6], [3, 5, 7], [4, 6], [5, 7], [6, 7], [], []],initialBoxes = [0, 1]) == 20
    assert candidate(status = [0, 0, 0, 0, 0, 0, 0, 0],candies = [10, 20, 30, 40, 50, 60, 70, 80],keys = [[1, 2], [3, 4], [5, 6], [7], [6], [5], [4], [3]],containedBoxes = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 0], [7, 1], [0, 2]],initialBoxes = [0]) == 0


