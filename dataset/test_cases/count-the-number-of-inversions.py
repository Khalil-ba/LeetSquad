def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 4,requirements = [[3, 3], [1, 1], [2, 2], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,requirements = [[3, 3], [1, 1], [2, 2], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,requirements = [[4, 6], [2, 2], [3, 3], [1, 1], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,requirements = [[4, 6], [2, 2], [3, 3], [1, 1], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 2,requirements = [[0, 0], [1, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2,requirements = [[0, 0], [1, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,requirements = [[2, 2], [0, 0]]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,requirements = [[2, 2], [0, 0]]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 3,requirements = [[2, 2], [1, 1], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3,requirements = [[2, 2], [1, 1], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,requirements = [[4, 5], [2, 2], [0, 0]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,requirements = [[4, 5], [2, 2], [0, 0]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,requirements = [[14, 50], [10, 25], [6, 15], [4, 10], [2, 5], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,requirements = [[14, 50], [10, 25], [6, 15], [4, 10], [2, 5], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requirements = [[5, 6], [3, 3], [1, 1], [0, 0]]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requirements = [[5, 6], [3, 3], [1, 1], [0, 0]]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,requirements = [[6, 15], [4, 10], [2, 5], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,requirements = [[6, 15], [4, 10], [2, 5], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 30,requirements = [[29, 150], [24, 75], [19, 40], [15, 20], [11, 10], [7, 5], [5, 3], [3, 1], [1, 0], [0, 0]]) == 363866727
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 30,requirements = [[29, 150], [24, 75], [19, 40], [15, 20], [11, 10], [7, 5], [5, 3], [3, 1], [1, 0], [0, 0]]) == 363866727: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,requirements = [[14, 60], [8, 20], [9, 30], [4, 8], [5, 12], [2, 4], [3, 6], [6, 18], [7, 24], [10, 40], [11, 50], [12, 60], [13, 70], [1, 2], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,requirements = [[14, 60], [8, 20], [9, 30], [4, 8], [5, 12], [2, 4], [3, 6], [6, 18], [7, 24], [10, 40], [11, 50], [12, 60], [13, 70], [1, 2], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requirements = [[7, 14], [5, 6], [3, 3], [1, 1], [2, 2], [4, 4], [6, 8], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requirements = [[7, 14], [5, 6], [3, 3], [1, 1], [2, 2], [4, 4], [6, 8], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,requirements = [[14, 85], [12, 45], [10, 20], [8, 10], [6, 6], [4, 3], [2, 2], [0, 0], [3, 5], [5, 8], [7, 12], [9, 18], [11, 30], [13, 50]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,requirements = [[14, 85], [12, 45], [10, 20], [8, 10], [6, 6], [4, 3], [2, 2], [0, 0], [3, 5], [5, 8], [7, 12], [9, 18], [11, 30], [13, 50]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,requirements = [[19, 90], [16, 60], [13, 40], [10, 20], [7, 10], [4, 5], [2, 2], [0, 0]]) == 358259893
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,requirements = [[19, 90], [16, 60], [13, 40], [10, 20], [7, 10], [4, 5], [2, 2], [0, 0]]) == 358259893: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,requirements = [[4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,requirements = [[4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,requirements = [[14, 91], [13, 78], [12, 65], [11, 52], [10, 39], [9, 26], [8, 13], [7, 0], [6, 0], [5, 0], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,requirements = [[14, 91], [13, 78], [12, 65], [11, 52], [10, 39], [9, 26], [8, 13], [7, 0], [6, 0], [5, 0], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,requirements = [[11, 40], [9, 25], [7, 15], [5, 10], [3, 5], [1, 2], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,requirements = [[11, 40], [9, 25], [7, 15], [5, 10], [3, 5], [1, 2], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,requirements = [[6, 21], [5, 15], [4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,requirements = [[6, 21], [5, 15], [4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requirements = [[7, 18], [5, 10], [4, 7], [3, 4], [2, 3], [1, 2], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requirements = [[7, 18], [5, 10], [4, 7], [3, 4], [2, 3], [1, 2], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,requirements = [[9, 30], [7, 15], [5, 8], [3, 4], [1, 2], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,requirements = [[9, 30], [7, 15], [5, 8], [3, 4], [1, 2], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,requirements = [[8, 20], [6, 12], [5, 8], [4, 5], [3, 3], [2, 2], [1, 1], [0, 0]]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,requirements = [[8, 20], [6, 12], [5, 8], [4, 5], [3, 3], [2, 2], [1, 1], [0, 0]]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requirements = [[5, 10], [3, 4], [2, 2], [1, 1], [0, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requirements = [[5, 10], [3, 4], [2, 2], [1, 1], [0, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,requirements = [[19, 171], [18, 153], [17, 136], [16, 119], [15, 102], [14, 85], [13, 68], [12, 51], [11, 34], [10, 17], [9, 0], [8, 0], [7, 0], [6, 0], [5, 0], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,requirements = [[19, 171], [18, 153], [17, 136], [16, 119], [15, 102], [14, 85], [13, 68], [12, 51], [11, 34], [10, 17], [9, 0], [8, 0], [7, 0], [6, 0], [5, 0], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,requirements = [[14, 105], [11, 40], [8, 15], [6, 7], [3, 3], [2, 1], [1, 0], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,requirements = [[14, 105], [11, 40], [8, 15], [6, 7], [3, 3], [2, 1], [1, 0], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requirements = [[7, 28], [6, 21], [5, 15], [4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requirements = [[7, 28], [6, 21], [5, 15], [4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requirements = [[7, 20], [6, 15], [5, 10], [4, 6], [3, 4], [2, 3], [1, 2], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requirements = [[7, 20], [6, 15], [5, 10], [4, 6], [3, 4], [2, 3], [1, 2], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,requirements = [[11, 45], [9, 25], [7, 15], [5, 8], [3, 4], [1, 2], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,requirements = [[11, 45], [9, 25], [7, 15], [5, 8], [3, 4], [1, 2], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,requirements = [[8, 18], [6, 12], [4, 8], [2, 4], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,requirements = [[8, 18], [6, 12], [4, 8], [2, 4], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,requirements = [[9, 35], [8, 25], [7, 20], [6, 15], [5, 10], [4, 6], [3, 4], [2, 3], [1, 2], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,requirements = [[9, 35], [8, 25], [7, 20], [6, 15], [5, 10], [4, 6], [3, 4], [2, 3], [1, 2], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,requirements = [[24, 100], [15, 30], [16, 40], [12, 20], [13, 25], [8, 10], [9, 15], [6, 5], [7, 10], [4, 3], [5, 6], [2, 2], [3, 3], [17, 50], [18, 60], [19, 70], [20, 80], [21, 90], [22, 100], [23, 110], [1, 1], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,requirements = [[24, 100], [15, 30], [16, 40], [12, 20], [13, 25], [8, 10], [9, 15], [6, 5], [7, 10], [4, 3], [5, 6], [2, 2], [3, 3], [17, 50], [18, 60], [19, 70], [20, 80], [21, 90], [22, 100], [23, 110], [1, 1], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,requirements = [[11, 66], [8, 30], [6, 15], [4, 7], [2, 2], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,requirements = [[11, 66], [8, 30], [6, 15], [4, 7], [2, 2], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requirements = [[7, 10], [4, 4], [5, 5], [2, 1], [3, 2], [6, 6], [1, 0], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requirements = [[7, 10], [4, 4], [5, 5], [2, 1], [3, 2], [6, 6], [1, 0], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,requirements = [[24, 150], [21, 105], [18, 70], [15, 45], [12, 30], [9, 20], [6, 15], [3, 10], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,requirements = [[24, 150], [21, 105], [18, 70], [15, 45], [12, 30], [9, 20], [6, 15], [3, 10], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,requirements = [[8, 25], [7, 20], [6, 15], [5, 10], [4, 6], [3, 4], [2, 3], [1, 2], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,requirements = [[8, 25], [7, 20], [6, 15], [5, 10], [4, 6], [3, 4], [2, 3], [1, 2], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,requirements = [[6, 15], [4, 8], [2, 4], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,requirements = [[6, 15], [4, 8], [2, 4], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requirements = [[5, 6], [4, 3], [3, 2], [2, 1], [1, 0], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requirements = [[5, 6], [4, 3], [3, 2], [2, 1], [1, 0], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,requirements = [[6, 10], [4, 5], [3, 3], [2, 1], [1, 0], [0, 0]]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,requirements = [[6, 10], [4, 5], [3, 3], [2, 1], [1, 0], [0, 0]]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,requirements = [[9, 30], [5, 10], [6, 15], [3, 4], [4, 8], [2, 2], [7, 20], [8, 25], [1, 1], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,requirements = [[9, 30], [5, 10], [6, 15], [3, 4], [4, 8], [2, 2], [7, 20], [8, 25], [1, 1], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requirements = [[5, 10], [3, 5], [1, 2], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requirements = [[5, 10], [3, 5], [1, 2], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requirements = [[5, 6], [3, 2], [2, 1], [1, 0], [0, 0]]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requirements = [[5, 6], [3, 2], [2, 1], [1, 0], [0, 0]]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,requirements = [[24, 250], [22, 170], [20, 100], [18, 60], [16, 40], [14, 20], [12, 10], [10, 6], [8, 4], [6, 3], [4, 2], [2, 1], [0, 0], [1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17], [19, 19], [21, 21], [23, 23]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,requirements = [[24, 250], [22, 170], [20, 100], [18, 60], [16, 40], [14, 20], [12, 10], [10, 6], [8, 4], [6, 3], [4, 2], [2, 1], [0, 0], [1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17], [19, 19], [21, 21], [23, 23]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,requirements = [[9, 45], [7, 21], [5, 10], [4, 6], [3, 4], [2, 2], [1, 1], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,requirements = [[9, 45], [7, 21], [5, 10], [4, 6], [3, 4], [2, 2], [1, 1], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,requirements = [[9, 25], [7, 15], [5, 10], [3, 5], [1, 2], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,requirements = [[9, 25], [7, 15], [5, 10], [3, 5], [1, 2], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requirements = [[7, 10], [5, 5], [3, 3], [1, 1], [0, 0]]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requirements = [[7, 10], [5, 5], [3, 3], [1, 1], [0, 0]]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,requirements = [[9, 28], [7, 15], [5, 6], [3, 3], [1, 1], [2, 2], [4, 4], [6, 8], [8, 20], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,requirements = [[9, 28], [7, 15], [5, 6], [3, 3], [1, 1], [2, 2], [4, 4], [6, 8], [8, 20], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requirements = [[5, 9], [4, 7], [3, 5], [2, 3], [1, 1], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requirements = [[5, 9], [4, 7], [3, 5], [2, 3], [1, 1], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,requirements = [[17, 60], [13, 30], [9, 15], [6, 10], [4, 5], [2, 2], [0, 0]]) == 217514306
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,requirements = [[17, 60], [13, 30], [9, 15], [6, 10], [4, 5], [2, 2], [0, 0]]) == 217514306: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,requirements = [[6, 15], [5, 10], [4, 6], [3, 4], [2, 2], [1, 1], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,requirements = [[6, 15], [5, 10], [4, 6], [3, 4], [2, 2], [1, 1], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requirements = [[7, 21], [5, 10], [4, 6], [3, 4], [2, 2], [1, 1], [0, 0]]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requirements = [[7, 21], [5, 10], [4, 6], [3, 4], [2, 2], [1, 1], [0, 0]]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,requirements = [[14, 50], [12, 30], [10, 20], [8, 15], [6, 10], [4, 5], [2, 3], [0, 0]]) == 57024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,requirements = [[14, 50], [12, 30], [10, 20], [8, 15], [6, 10], [4, 5], [2, 3], [0, 0]]) == 57024: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requirements = [[7, 15], [3, 5], [5, 10], [2, 2], [1, 1], [0, 0]]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requirements = [[7, 15], [3, 5], [5, 10], [2, 2], [1, 1], [0, 0]]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,requirements = [[6, 15], [4, 10], [2, 3], [0, 0], [3, 4], [5, 9], [1, 1]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,requirements = [[6, 15], [4, 10], [2, 3], [0, 0], [3, 4], [5, 9], [1, 1]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,requirements = [[19, 130], [17, 80], [15, 40], [13, 20], [11, 10], [9, 6], [7, 4], [5, 3], [3, 2], [1, 1], [0, 0], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16], [18, 18]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,requirements = [[19, 130], [17, 80], [15, 40], [13, 20], [11, 10], [9, 6], [7, 4], [5, 3], [3, 2], [1, 1], [0, 0], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16], [18, 18]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,requirements = [[11, 66], [10, 55], [9, 45], [8, 36], [7, 28], [6, 21], [5, 15], [4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,requirements = [[11, 66], [10, 55], [9, 45], [8, 36], [7, 28], [6, 21], [5, 15], [4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requirements = [[5, 12], [4, 8], [3, 5], [2, 3], [1, 1], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requirements = [[5, 12], [4, 8], [3, 5], [2, 3], [1, 1], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 18,requirements = [[17, 63], [14, 42], [11, 28], [8, 21], [5, 14], [2, 7], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 18,requirements = [[17, 63], [14, 42], [11, 28], [8, 21], [5, 14], [2, 7], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,requirements = [[14, 45], [11, 25], [8, 10], [5, 5], [2, 2], [0, 0]]) == 5518800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,requirements = [[14, 45], [11, 25], [8, 10], [5, 5], [2, 2], [0, 0]]) == 5518800: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,requirements = [[11, 28], [8, 15], [5, 8], [2, 3], [0, 0]]) == 51170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,requirements = [[11, 28], [8, 15], [5, 8], [2, 3], [0, 0]]) == 51170: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,requirements = [[9, 45], [8, 36], [7, 28], [6, 21], [5, 15], [4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,requirements = [[9, 45], [8, 36], [7, 28], [6, 21], [5, 15], [4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 25,requirements = [[24, 100], [20, 50], [15, 25], [11, 15], [7, 10], [5, 5], [3, 2], [1, 0], [0, 0]]) == 195391545
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 25,requirements = [[24, 100], [20, 50], [15, 25], [11, 15], [7, 10], [5, 5], [3, 2], [1, 0], [0, 0]]) == 195391545: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,requirements = [[9, 35], [8, 25], [7, 18], [6, 12], [5, 8], [4, 5], [3, 3], [2, 2], [1, 1], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,requirements = [[9, 35], [8, 25], [7, 18], [6, 12], [5, 8], [4, 5], [3, 3], [2, 2], [1, 1], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requirements = [[7, 21], [4, 10], [3, 5], [2, 3], [1, 1], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requirements = [[7, 21], [4, 10], [3, 5], [2, 3], [1, 1], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requirements = [[7, 10], [6, 5], [5, 2], [4, 1], [3, 0], [2, 0], [1, 0], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requirements = [[7, 10], [6, 5], [5, 2], [4, 1], [3, 0], [2, 0], [1, 0], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,requirements = [[8, 36], [7, 28], [6, 21], [5, 15], [4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,requirements = [[8, 36], [7, 28], [6, 21], [5, 15], [4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,requirements = [[14, 105], [13, 84], [12, 63], [11, 42], [10, 28], [9, 21], [8, 15], [7, 10], [6, 6], [5, 4], [4, 2], [3, 1], [2, 1], [1, 0], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,requirements = [[14, 105], [13, 84], [12, 63], [11, 42], [10, 28], [9, 21], [8, 15], [7, 10], [6, 6], [5, 4], [4, 2], [3, 1], [2, 1], [1, 0], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 12,requirements = [[11, 30], [8, 15], [5, 8], [3, 3], [1, 1], [0, 0]]) == 47250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12,requirements = [[11, 30], [8, 15], [5, 8], [3, 3], [1, 1], [0, 0]]) == 47250: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,requirements = [[19, 190], [18, 171], [17, 153], [16, 136], [15, 119], [14, 105], [13, 92], [12, 80], [11, 69], [10, 58], [9, 48], [8, 39], [7, 31], [6, 24], [5, 18], [4, 13], [3, 9], [2, 6], [1, 4], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,requirements = [[19, 190], [18, 171], [17, 153], [16, 136], [15, 119], [14, 105], [13, 92], [12, 80], [11, 69], [10, 58], [9, 48], [8, 39], [7, 31], [6, 24], [5, 18], [4, 13], [3, 9], [2, 6], [1, 4], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,requirements = [[4, 6], [3, 4], [2, 3], [1, 2], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,requirements = [[4, 6], [3, 4], [2, 3], [1, 2], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requirements = [[7, 14], [5, 7], [3, 3], [1, 1], [0, 0]]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requirements = [[7, 14], [5, 7], [3, 3], [1, 1], [0, 0]]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,requirements = [[9, 45], [5, 15], [3, 5], [2, 3], [1, 1], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,requirements = [[9, 45], [5, 15], [3, 5], [2, 3], [1, 1], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requirements = [[7, 20], [5, 10], [3, 5], [1, 2], [0, 0], [6, 12], [4, 6]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requirements = [[7, 20], [5, 10], [3, 5], [1, 2], [0, 0], [6, 12], [4, 6]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 8,requirements = [[7, 21], [5, 12], [3, 6], [1, 3], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8,requirements = [[7, 21], [5, 12], [3, 6], [1, 3], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 9,requirements = [[8, 28], [6, 18], [4, 10], [2, 5], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9,requirements = [[8, 28], [6, 18], [4, 10], [2, 5], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,requirements = [[9, 40], [7, 25], [5, 15], [4, 10], [3, 6], [2, 4], [1, 2], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,requirements = [[9, 40], [7, 25], [5, 15], [4, 10], [3, 6], [2, 4], [1, 2], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requirements = [[5, 6], [3, 3], [1, 1], [2, 2], [4, 4], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requirements = [[5, 6], [3, 3], [1, 1], [2, 2], [4, 4], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,requirements = [[9, 20], [6, 10], [4, 5], [2, 2], [0, 0]]) == 2688
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,requirements = [[9, 20], [6, 10], [4, 5], [2, 2], [0, 0]]) == 2688: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,requirements = [[6, 15], [5, 10], [4, 6], [2, 3], [0, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,requirements = [[6, 15], [5, 10], [4, 6], [2, 3], [0, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,requirements = [[4, 6], [3, 4], [2, 2], [1, 1], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,requirements = [[4, 6], [3, 4], [2, 2], [1, 1], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,requirements = [[19, 80], [15, 40], [11, 20], [7, 10], [5, 5], [3, 2], [1, 0], [0, 0]]) == 208478921
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,requirements = [[19, 80], [15, 40], [11, 20], [7, 10], [5, 5], [3, 2], [1, 0], [0, 0]]) == 208478921: {e}')
    
    total += 1
    try:
        result = candidate(n = 15,requirements = [[14, 91], [12, 50], [10, 25], [8, 15], [6, 8], [4, 4], [2, 2], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,requirements = [[14, 91], [12, 50], [10, 25], [8, 15], [6, 8], [4, 4], [2, 2], [0, 0]]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requirements = [[5, 15], [4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requirements = [[5, 15], [4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 6,requirements = [[5, 6], [3, 3], [2, 1], [1, 0], [0, 0]]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6,requirements = [[5, 6], [3, 3], [2, 1], [1, 0], [0, 0]]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,requirements = [[9, 20], [8, 15], [7, 10], [6, 5], [5, 3], [4, 2], [3, 1], [2, 0], [1, 0], [0, 0]]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,requirements = [[9, 20], [8, 15], [7, 10], [6, 5], [5, 3], [4, 2], [3, 1], [2, 0], [1, 0], [0, 0]]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 20,requirements = [[19, 150], [10, 50], [11, 60], [7, 20], [8, 30], [5, 10], [6, 15], [3, 5], [4, 10], [1, 2], [2, 3], [12, 70], [13, 80], [14, 90], [15, 100], [16, 110], [17, 120], [18, 130], [0, 0]]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 20,requirements = [[19, 150], [10, 50], [11, 60], [7, 20], [8, 30], [5, 10], [6, 15], [3, 5], [4, 10], [1, 2], [2, 3], [12, 70], [13, 80], [14, 90], [15, 100], [16, 110], [17, 120], [18, 130], [0, 0]]) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 4,requirements = [[3, 3], [1, 1], [2, 2], [0, 0]]) == 1
    assert candidate(n = 5,requirements = [[4, 6], [2, 2], [3, 3], [1, 1], [0, 0]]) == 1
    assert candidate(n = 2,requirements = [[0, 0], [1, 0]]) == 1
    assert candidate(n = 3,requirements = [[2, 2], [0, 0]]) == 2
    assert candidate(n = 3,requirements = [[2, 2], [1, 1], [0, 0]]) == 1
    assert candidate(n = 5,requirements = [[4, 5], [2, 2], [0, 0]]) == 8
    assert candidate(n = 15,requirements = [[14, 50], [10, 25], [6, 15], [4, 10], [2, 5], [0, 0]]) == 0
    assert candidate(n = 6,requirements = [[5, 6], [3, 3], [1, 1], [0, 0]]) == 12
    assert candidate(n = 7,requirements = [[6, 15], [4, 10], [2, 5], [0, 0]]) == 0
    assert candidate(n = 30,requirements = [[29, 150], [24, 75], [19, 40], [15, 20], [11, 10], [7, 5], [5, 3], [3, 1], [1, 0], [0, 0]]) == 363866727
    assert candidate(n = 15,requirements = [[14, 60], [8, 20], [9, 30], [4, 8], [5, 12], [2, 4], [3, 6], [6, 18], [7, 24], [10, 40], [11, 50], [12, 60], [13, 70], [1, 2], [0, 0]]) == 0
    assert candidate(n = 8,requirements = [[7, 14], [5, 6], [3, 3], [1, 1], [2, 2], [4, 4], [6, 8], [0, 0]]) == 1
    assert candidate(n = 15,requirements = [[14, 85], [12, 45], [10, 20], [8, 10], [6, 6], [4, 3], [2, 2], [0, 0], [3, 5], [5, 8], [7, 12], [9, 18], [11, 30], [13, 50]]) == 0
    assert candidate(n = 20,requirements = [[19, 90], [16, 60], [13, 40], [10, 20], [7, 10], [4, 5], [2, 2], [0, 0]]) == 358259893
    assert candidate(n = 5,requirements = [[4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1
    assert candidate(n = 15,requirements = [[14, 91], [13, 78], [12, 65], [11, 52], [10, 39], [9, 26], [8, 13], [7, 0], [6, 0], [5, 0], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]) == 0
    assert candidate(n = 12,requirements = [[11, 40], [9, 25], [7, 15], [5, 10], [3, 5], [1, 2], [0, 0]]) == 0
    assert candidate(n = 7,requirements = [[6, 21], [5, 15], [4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1
    assert candidate(n = 8,requirements = [[7, 18], [5, 10], [4, 7], [3, 4], [2, 3], [1, 2], [0, 0]]) == 0
    assert candidate(n = 10,requirements = [[9, 30], [7, 15], [5, 8], [3, 4], [1, 2], [0, 0]]) == 0
    assert candidate(n = 9,requirements = [[8, 20], [6, 12], [5, 8], [4, 5], [3, 3], [2, 2], [1, 1], [0, 0]]) == 8
    assert candidate(n = 6,requirements = [[5, 10], [3, 4], [2, 2], [1, 1], [0, 0]]) == 4
    assert candidate(n = 20,requirements = [[19, 171], [18, 153], [17, 136], [16, 119], [15, 102], [14, 85], [13, 68], [12, 51], [11, 34], [10, 17], [9, 0], [8, 0], [7, 0], [6, 0], [5, 0], [4, 0], [3, 0], [2, 0], [1, 0], [0, 0]]) == 0
    assert candidate(n = 15,requirements = [[14, 105], [11, 40], [8, 15], [6, 7], [3, 3], [2, 1], [1, 0], [0, 0]]) == 0
    assert candidate(n = 8,requirements = [[7, 28], [6, 21], [5, 15], [4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1
    assert candidate(n = 8,requirements = [[7, 20], [6, 15], [5, 10], [4, 6], [3, 4], [2, 3], [1, 2], [0, 0]]) == 0
    assert candidate(n = 12,requirements = [[11, 45], [9, 25], [7, 15], [5, 8], [3, 4], [1, 2], [0, 0]]) == 0
    assert candidate(n = 9,requirements = [[8, 18], [6, 12], [4, 8], [2, 4], [0, 0]]) == 0
    assert candidate(n = 10,requirements = [[9, 35], [8, 25], [7, 20], [6, 15], [5, 10], [4, 6], [3, 4], [2, 3], [1, 2], [0, 0]]) == 0
    assert candidate(n = 25,requirements = [[24, 100], [15, 30], [16, 40], [12, 20], [13, 25], [8, 10], [9, 15], [6, 5], [7, 10], [4, 3], [5, 6], [2, 2], [3, 3], [17, 50], [18, 60], [19, 70], [20, 80], [21, 90], [22, 100], [23, 110], [1, 1], [0, 0]]) == 0
    assert candidate(n = 12,requirements = [[11, 66], [8, 30], [6, 15], [4, 7], [2, 2], [0, 0]]) == 0
    assert candidate(n = 8,requirements = [[7, 10], [4, 4], [5, 5], [2, 1], [3, 2], [6, 6], [1, 0], [0, 0]]) == 1
    assert candidate(n = 25,requirements = [[24, 150], [21, 105], [18, 70], [15, 45], [12, 30], [9, 20], [6, 15], [3, 10], [0, 0]]) == 0
    assert candidate(n = 9,requirements = [[8, 25], [7, 20], [6, 15], [5, 10], [4, 6], [3, 4], [2, 3], [1, 2], [0, 0]]) == 0
    assert candidate(n = 7,requirements = [[6, 15], [4, 8], [2, 4], [0, 0]]) == 0
    assert candidate(n = 6,requirements = [[5, 6], [4, 3], [3, 2], [2, 1], [1, 0], [0, 0]]) == 1
    assert candidate(n = 7,requirements = [[6, 10], [4, 5], [3, 3], [2, 1], [1, 0], [0, 0]]) == 6
    assert candidate(n = 10,requirements = [[9, 30], [5, 10], [6, 15], [3, 4], [4, 8], [2, 2], [7, 20], [8, 25], [1, 1], [0, 0]]) == 1
    assert candidate(n = 6,requirements = [[5, 10], [3, 5], [1, 2], [0, 0]]) == 0
    assert candidate(n = 6,requirements = [[5, 6], [3, 2], [2, 1], [1, 0], [0, 0]]) == 5
    assert candidate(n = 25,requirements = [[24, 250], [22, 170], [20, 100], [18, 60], [16, 40], [14, 20], [12, 10], [10, 6], [8, 4], [6, 3], [4, 2], [2, 1], [0, 0], [1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17], [19, 19], [21, 21], [23, 23]]) == 0
    assert candidate(n = 10,requirements = [[9, 45], [7, 21], [5, 10], [4, 6], [3, 4], [2, 2], [1, 1], [0, 0]]) == 0
    assert candidate(n = 10,requirements = [[9, 25], [7, 15], [5, 10], [3, 5], [1, 2], [0, 0]]) == 0
    assert candidate(n = 8,requirements = [[7, 10], [5, 5], [3, 3], [1, 1], [0, 0]]) == 54
    assert candidate(n = 10,requirements = [[9, 28], [7, 15], [5, 6], [3, 3], [1, 1], [2, 2], [4, 4], [6, 8], [8, 20], [0, 0]]) == 1
    assert candidate(n = 6,requirements = [[5, 9], [4, 7], [3, 5], [2, 3], [1, 1], [0, 0]]) == 1
    assert candidate(n = 18,requirements = [[17, 60], [13, 30], [9, 15], [6, 10], [4, 5], [2, 2], [0, 0]]) == 217514306
    assert candidate(n = 7,requirements = [[6, 15], [5, 10], [4, 6], [3, 4], [2, 2], [1, 1], [0, 0]]) == 1
    assert candidate(n = 8,requirements = [[7, 21], [5, 10], [4, 6], [3, 4], [2, 2], [1, 1], [0, 0]]) == 3
    assert candidate(n = 15,requirements = [[14, 50], [12, 30], [10, 20], [8, 15], [6, 10], [4, 5], [2, 3], [0, 0]]) == 57024
    assert candidate(n = 8,requirements = [[7, 15], [3, 5], [5, 10], [2, 2], [1, 1], [0, 0]]) == 30
    assert candidate(n = 7,requirements = [[6, 15], [4, 10], [2, 3], [0, 0], [3, 4], [5, 9], [1, 1]]) == 0
    assert candidate(n = 20,requirements = [[19, 130], [17, 80], [15, 40], [13, 20], [11, 10], [9, 6], [7, 4], [5, 3], [3, 2], [1, 1], [0, 0], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16], [18, 18]]) == 0
    assert candidate(n = 12,requirements = [[11, 66], [10, 55], [9, 45], [8, 36], [7, 28], [6, 21], [5, 15], [4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1
    assert candidate(n = 6,requirements = [[5, 12], [4, 8], [3, 5], [2, 3], [1, 1], [0, 0]]) == 1
    assert candidate(n = 18,requirements = [[17, 63], [14, 42], [11, 28], [8, 21], [5, 14], [2, 7], [0, 0]]) == 0
    assert candidate(n = 15,requirements = [[14, 45], [11, 25], [8, 10], [5, 5], [2, 2], [0, 0]]) == 5518800
    assert candidate(n = 12,requirements = [[11, 28], [8, 15], [5, 8], [2, 3], [0, 0]]) == 51170
    assert candidate(n = 10,requirements = [[9, 45], [8, 36], [7, 28], [6, 21], [5, 15], [4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1
    assert candidate(n = 25,requirements = [[24, 100], [20, 50], [15, 25], [11, 15], [7, 10], [5, 5], [3, 2], [1, 0], [0, 0]]) == 195391545
    assert candidate(n = 10,requirements = [[9, 35], [8, 25], [7, 18], [6, 12], [5, 8], [4, 5], [3, 3], [2, 2], [1, 1], [0, 0]]) == 0
    assert candidate(n = 8,requirements = [[7, 21], [4, 10], [3, 5], [2, 3], [1, 1], [0, 0]]) == 0
    assert candidate(n = 8,requirements = [[7, 10], [6, 5], [5, 2], [4, 1], [3, 0], [2, 0], [1, 0], [0, 0]]) == 1
    assert candidate(n = 9,requirements = [[8, 36], [7, 28], [6, 21], [5, 15], [4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1
    assert candidate(n = 15,requirements = [[14, 105], [13, 84], [12, 63], [11, 42], [10, 28], [9, 21], [8, 15], [7, 10], [6, 6], [5, 4], [4, 2], [3, 1], [2, 1], [1, 0], [0, 0]]) == 0
    assert candidate(n = 12,requirements = [[11, 30], [8, 15], [5, 8], [3, 3], [1, 1], [0, 0]]) == 47250
    assert candidate(n = 20,requirements = [[19, 190], [18, 171], [17, 153], [16, 136], [15, 119], [14, 105], [13, 92], [12, 80], [11, 69], [10, 58], [9, 48], [8, 39], [7, 31], [6, 24], [5, 18], [4, 13], [3, 9], [2, 6], [1, 4], [0, 0]]) == 0
    assert candidate(n = 5,requirements = [[4, 6], [3, 4], [2, 3], [1, 2], [0, 0]]) == 0
    assert candidate(n = 8,requirements = [[7, 14], [5, 7], [3, 3], [1, 1], [0, 0]]) == 105
    assert candidate(n = 10,requirements = [[9, 45], [5, 15], [3, 5], [2, 3], [1, 1], [0, 0]]) == 0
    assert candidate(n = 8,requirements = [[7, 20], [5, 10], [3, 5], [1, 2], [0, 0], [6, 12], [4, 6]]) == 0
    assert candidate(n = 8,requirements = [[7, 21], [5, 12], [3, 6], [1, 3], [0, 0]]) == 0
    assert candidate(n = 9,requirements = [[8, 28], [6, 18], [4, 10], [2, 5], [0, 0]]) == 0
    assert candidate(n = 10,requirements = [[9, 40], [7, 25], [5, 15], [4, 10], [3, 6], [2, 4], [1, 2], [0, 0]]) == 0
    assert candidate(n = 6,requirements = [[5, 6], [3, 3], [1, 1], [2, 2], [4, 4], [0, 0]]) == 1
    assert candidate(n = 10,requirements = [[9, 20], [6, 10], [4, 5], [2, 2], [0, 0]]) == 2688
    assert candidate(n = 7,requirements = [[6, 15], [5, 10], [4, 6], [2, 3], [0, 0]]) == 4
    assert candidate(n = 5,requirements = [[4, 6], [3, 4], [2, 2], [1, 1], [0, 0]]) == 1
    assert candidate(n = 20,requirements = [[19, 80], [15, 40], [11, 20], [7, 10], [5, 5], [3, 2], [1, 0], [0, 0]]) == 208478921
    assert candidate(n = 15,requirements = [[14, 91], [12, 50], [10, 25], [8, 15], [6, 8], [4, 4], [2, 2], [0, 0]]) == 0
    assert candidate(n = 6,requirements = [[5, 15], [4, 10], [3, 6], [2, 3], [1, 1], [0, 0]]) == 1
    assert candidate(n = 6,requirements = [[5, 6], [3, 3], [2, 1], [1, 0], [0, 0]]) == 4
    assert candidate(n = 10,requirements = [[9, 20], [8, 15], [7, 10], [6, 5], [5, 3], [4, 2], [3, 1], [2, 0], [1, 0], [0, 0]]) == 1
    assert candidate(n = 20,requirements = [[19, 150], [10, 50], [11, 60], [7, 20], [8, 30], [5, 10], [6, 15], [3, 5], [4, 10], [1, 2], [2, 3], [12, 70], [13, 80], [14, 90], [15, 100], [16, 110], [17, 120], [18, 130], [0, 0]]) == 0


