def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1]],signalSpeed = 1) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1]],signalSpeed = 1) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [1, 2, 5], [2, 3, 13], [3, 4, 9], [4, 5, 2]],signalSpeed = 1) == [0, 4, 6, 6, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [1, 2, 5], [2, 3, 13], [3, 4, 9], [4, 5, 2]],signalSpeed = 1) == [0, 4, 6, 6, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [1, 2, 10], [2, 3, 15], [3, 4, 20]],signalSpeed = 5) == [0, 3, 4, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [1, 2, 10], [2, 3, 15], [3, 4, 20]],signalSpeed = 5) == [0, 3, 4, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [0, 2, 3], [1, 3, 4], [1, 4, 5], [2, 5, 6], [2, 6, 7]],signalSpeed = 1) == [9, 9, 9, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [0, 2, 3], [1, 3, 4], [1, 4, 5], [2, 5, 6], [2, 6, 7]],signalSpeed = 1) == [9, 9, 9, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [0, 2, 10], [1, 3, 10], [1, 4, 10], [2, 5, 10], [2, 6, 10]],signalSpeed = 5) == [9, 9, 9, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [0, 2, 10], [1, 3, 10], [1, 4, 10], [2, 5, 10], [2, 6, 10]],signalSpeed = 5) == [9, 9, 9, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 4], [1, 2, 8], [2, 3, 12], [3, 4, 16]],signalSpeed = 4) == [0, 3, 4, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 4], [1, 2, 8], [2, 3, 12], [3, 4, 16]],signalSpeed = 4) == [0, 3, 4, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]],signalSpeed = 2) == [0, 2, 0, 0, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]],signalSpeed = 2) == [0, 2, 0, 0, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 4, 4], [1, 5, 5], [2, 6, 6], [3, 7, 7]],signalSpeed = 1) == [16, 11, 6, 6, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 4, 4], [1, 5, 5], [2, 6, 6], [3, 7, 7]],signalSpeed = 1) == [16, 11, 6, 6, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 6], [3, 4, 8]],signalSpeed = 2) == [0, 3, 4, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 6], [3, 4, 8]],signalSpeed = 2) == [0, 3, 4, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [1, 2, 6], [2, 3, 9], [3, 4, 12], [4, 5, 15]],signalSpeed = 3) == [0, 4, 6, 6, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [1, 2, 6], [2, 3, 9], [3, 4, 12], [4, 5, 15]],signalSpeed = 3) == [0, 4, 6, 6, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 6, 3], [6, 5, 3], [0, 3, 1], [3, 2, 7], [3, 1, 6], [3, 4, 2]],signalSpeed = 3) == [2, 0, 0, 0, 0, 0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 6, 3], [6, 5, 3], [0, 3, 1], [3, 2, 7], [3, 1, 6], [3, 4, 2]],signalSpeed = 3) == [2, 0, 0, 0, 0, 0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40]],signalSpeed = 10) == [0, 3, 4, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40]],signalSpeed = 10) == [0, 3, 4, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 4], [1, 2, 8], [2, 3, 12]],signalSpeed = 4) == [0, 2, 2, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 4], [1, 2, 8], [2, 3, 12]],signalSpeed = 4) == [0, 2, 2, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 4], [1, 2, 5], [2, 3, 6]],signalSpeed = 2) == [0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 4], [1, 2, 5], [2, 3, 6]],signalSpeed = 2) == [0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 8], [3, 4, 16]],signalSpeed = 2) == [0, 3, 4, 3, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 8], [3, 4, 16]],signalSpeed = 2) == [0, 3, 4, 3, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 13], [0, 2, 26], [1, 3, 39], [1, 4, 52], [2, 5, 65], [2, 6, 78], [3, 7, 91], [4, 8, 104], [5, 9, 117], [6, 10, 130], [7, 11, 143], [8, 12, 156], [9, 13, 169]],signalSpeed = 13) == [42, 51, 46, 22, 22, 22, 12, 12, 12, 12, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 13], [0, 2, 26], [1, 3, 39], [1, 4, 52], [2, 5, 65], [2, 6, 78], [3, 7, 91], [4, 8, 104], [5, 9, 117], [6, 10, 130], [7, 11, 143], [8, 12, 156], [9, 13, 169]],signalSpeed = 13) == [42, 51, 46, 22, 22, 22, 12, 12, 12, 12, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 19], [1, 2, 38], [1, 3, 57], [2, 4, 76], [2, 5, 95], [3, 6, 114], [3, 7, 133], [4, 8, 152], [5, 9, 171], [6, 10, 190], [7, 11, 209], [8, 12, 228], [9, 13, 247], [10, 14, 266], [11, 15, 285], [12, 16, 304], [13, 17, 323], [14, 18, 342]],signalSpeed = 19) == [0, 89, 96, 89, 45, 45, 45, 32, 32, 32, 32, 17, 17, 17, 17, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 19], [1, 2, 38], [1, 3, 57], [2, 4, 76], [2, 5, 95], [3, 6, 114], [3, 7, 133], [4, 8, 152], [5, 9, 171], [6, 10, 190], [7, 11, 209], [8, 12, 228], [9, 13, 247], [10, 14, 266], [11, 15, 285], [12, 16, 304], [13, 17, 323], [14, 18, 342]],signalSpeed = 19) == [0, 89, 96, 89, 45, 45, 45, 32, 32, 32, 32, 17, 17, 17, 17, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 6], [0, 2, 12], [1, 3, 18], [1, 4, 24], [2, 5, 30], [2, 6, 36], [3, 7, 42], [3, 8, 48], [4, 9, 54], [5, 10, 60], [6, 11, 66]],signalSpeed = 6) == [30, 36, 32, 19, 10, 10, 10, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 6], [0, 2, 12], [1, 3, 18], [1, 4, 24], [2, 5, 30], [2, 6, 36], [3, 7, 42], [3, 8, 48], [4, 9, 54], [5, 10, 60], [6, 11, 66]],signalSpeed = 6) == [30, 36, 32, 19, 10, 10, 10, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 7], [0, 2, 14], [1, 3, 21], [1, 4, 28], [2, 5, 35], [2, 6, 42], [3, 7, 49], [3, 8, 56], [4, 9, 63], [4, 10, 70]],signalSpeed = 7) == [21, 33, 17, 17, 17, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 7], [0, 2, 14], [1, 3, 21], [1, 4, 28], [2, 5, 35], [2, 6, 42], [3, 7, 49], [3, 8, 56], [4, 9, 63], [4, 10, 70]],signalSpeed = 7) == [21, 33, 17, 17, 17, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 11], [1, 2, 22], [2, 3, 33], [3, 4, 44], [4, 5, 55], [5, 6, 66], [6, 7, 77], [7, 8, 88], [8, 9, 99], [9, 10, 110]],signalSpeed = 11) == [0, 9, 16, 21, 24, 25, 24, 21, 16, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 11], [1, 2, 22], [2, 3, 33], [3, 4, 44], [4, 5, 55], [5, 6, 66], [6, 7, 77], [7, 8, 88], [8, 9, 99], [9, 10, 110]],signalSpeed = 11) == [0, 9, 16, 21, 24, 25, 24, 21, 16, 9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 5, 5], [1, 6, 6], [2, 7, 7], [2, 8, 8], [3, 9, 9], [3, 10, 10], [4, 11, 11], [4, 12, 12]],signalSpeed = 1) == [54, 21, 21, 21, 21, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 5, 5], [1, 6, 6], [2, 7, 7], [2, 8, 8], [3, 9, 9], [3, 10, 10], [4, 11, 11], [4, 12, 12]],signalSpeed = 1) == [54, 21, 21, 21, 21, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 9], [1, 2, 18], [2, 3, 27], [3, 4, 36], [4, 5, 45], [5, 6, 54], [6, 7, 63], [7, 8, 72], [8, 9, 81], [9, 10, 90], [10, 11, 99], [11, 12, 108]],signalSpeed = 9) == [0, 11, 20, 27, 32, 35, 36, 35, 32, 27, 20, 11, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 9], [1, 2, 18], [2, 3, 27], [3, 4, 36], [4, 5, 45], [5, 6, 54], [6, 7, 63], [7, 8, 72], [8, 9, 81], [9, 10, 90], [10, 11, 99], [11, 12, 108]],signalSpeed = 9) == [0, 11, 20, 27, 32, 35, 36, 35, 32, 27, 20, 11, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 7], [0, 2, 14], [1, 3, 21], [1, 4, 28], [2, 5, 35], [2, 6, 42], [3, 7, 49], [3, 8, 56], [4, 9, 63], [5, 10, 70], [6, 11, 77]],signalSpeed = 7) == [30, 36, 32, 19, 10, 10, 10, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 7], [0, 2, 14], [1, 3, 21], [1, 4, 28], [2, 5, 35], [2, 6, 42], [3, 7, 49], [3, 8, 56], [4, 9, 63], [5, 10, 70], [6, 11, 77]],signalSpeed = 7) == [30, 36, 32, 19, 10, 10, 10, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 7], [0, 2, 14], [1, 3, 21], [1, 4, 28], [2, 5, 35], [2, 6, 42], [3, 7, 49], [3, 8, 56], [4, 9, 63], [4, 10, 70], [5, 11, 77], [5, 12, 84], [6, 13, 91], [6, 14, 98]],signalSpeed = 7) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 7], [0, 2, 14], [1, 3, 21], [1, 4, 28], [2, 5, 35], [2, 6, 42], [3, 7, 49], [3, 8, 56], [4, 9, 63], [4, 10, 70], [5, 11, 77], [5, 12, 84], [6, 13, 91], [6, 14, 98]],signalSpeed = 7) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 17], [0, 2, 34], [1, 3, 51], [1, 4, 68], [2, 5, 85], [2, 6, 102], [3, 7, 119], [3, 8, 136], [4, 9, 153], [4, 10, 170], [5, 11, 187], [5, 12, 204], [6, 13, 221], [6, 14, 238]],signalSpeed = 17) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 17], [0, 2, 34], [1, 3, 51], [1, 4, 68], [2, 5, 85], [2, 6, 102], [3, 7, 119], [3, 8, 136], [4, 9, 153], [4, 10, 170], [5, 11, 187], [5, 12, 204], [6, 13, 221], [6, 14, 238]],signalSpeed = 17) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 8], [3, 4, 16], [4, 5, 32], [5, 6, 64], [6, 7, 128], [7, 8, 256], [8, 9, 512]],signalSpeed = 2) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 8], [3, 4, 16], [4, 5, 32], [5, 6, 64], [6, 7, 128], [7, 8, 256], [8, 9, 512]],signalSpeed = 2) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 100000], [1, 2, 200000], [2, 3, 300000], [3, 4, 400000], [4, 5, 500000], [5, 6, 600000], [6, 7, 700000]],signalSpeed = 100000) == [0, 6, 10, 12, 12, 10, 6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 100000], [1, 2, 200000], [2, 3, 300000], [3, 4, 400000], [4, 5, 500000], [5, 6, 600000], [6, 7, 700000]],signalSpeed = 100000) == [0, 6, 10, 12, 12, 10, 6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 8], [3, 4, 16], [4, 5, 32], [5, 6, 64]],signalSpeed = 2) == [0, 5, 8, 9, 8, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 8], [3, 4, 16], [4, 5, 32], [5, 6, 64]],signalSpeed = 2) == [0, 5, 8, 9, 8, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [1, 4, 40], [1, 5, 50], [2, 6, 60], [2, 7, 70], [3, 8, 80], [3, 9, 90], [4, 10, 100], [5, 11, 110], [6, 12, 120]],signalSpeed = 10) == [47, 36, 29, 21, 11, 11, 11, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [1, 4, 40], [1, 5, 50], [2, 6, 60], [2, 7, 70], [3, 8, 80], [3, 9, 90], [4, 10, 100], [5, 11, 110], [6, 12, 120]],signalSpeed = 10) == [47, 36, 29, 21, 11, 11, 11, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10]],signalSpeed = 2) == [0, 4, 0, 2, 6, 6, 2, 0, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10]],signalSpeed = 2) == [0, 4, 0, 2, 6, 6, 2, 0, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [1, 2, 10], [1, 3, 15], [2, 4, 20], [3, 5, 25], [4, 6, 30], [5, 7, 35]],signalSpeed = 5) == [0, 15, 10, 10, 6, 6, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [1, 2, 10], [1, 3, 15], [2, 4, 20], [3, 5, 25], [4, 6, 30], [5, 7, 35]],signalSpeed = 5) == [0, 15, 10, 10, 6, 6, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 8], [3, 4, 16], [4, 5, 32], [5, 6, 64], [6, 7, 128], [7, 8, 256], [8, 9, 512], [9, 10, 1024]],signalSpeed = 2) == [0, 9, 16, 21, 24, 25, 24, 21, 16, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 8], [3, 4, 16], [4, 5, 32], [5, 6, 64], [6, 7, 128], [7, 8, 256], [8, 9, 512], [9, 10, 1024]],signalSpeed = 2) == [0, 9, 16, 21, 24, 25, 24, 21, 16, 9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [0, 2, 6], [1, 3, 9], [1, 4, 12], [2, 5, 15], [2, 6, 18]],signalSpeed = 3) == [9, 9, 9, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [0, 2, 6], [1, 3, 9], [1, 4, 12], [2, 5, 15], [2, 6, 18]],signalSpeed = 3) == [9, 9, 9, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 7], [1, 2, 14], [2, 3, 21], [3, 4, 28], [4, 5, 35], [5, 6, 42], [6, 7, 49], [7, 8, 56]],signalSpeed = 7) == [0, 7, 12, 15, 16, 15, 12, 7, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 7], [1, 2, 14], [2, 3, 21], [3, 4, 28], [4, 5, 35], [5, 6, 42], [6, 7, 49], [7, 8, 56]],signalSpeed = 7) == [0, 7, 12, 15, 16, 15, 12, 7, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 6], [1, 2, 12], [1, 3, 18], [3, 4, 24], [3, 5, 30], [5, 6, 36], [5, 7, 42], [7, 8, 48], [7, 9, 54], [9, 10, 60], [10, 11, 66]],signalSpeed = 6) == [0, 19, 0, 31, 0, 35, 0, 31, 0, 18, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 6], [1, 2, 12], [1, 3, 18], [3, 4, 24], [3, 5, 30], [5, 6, 36], [5, 7, 42], [7, 8, 48], [7, 9, 54], [9, 10, 60], [10, 11, 66]],signalSpeed = 6) == [0, 19, 0, 31, 0, 35, 0, 31, 0, 18, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [0, 2, 20], [1, 3, 15], [1, 4, 25], [2, 5, 30], [2, 6, 35]],signalSpeed = 5) == [9, 9, 9, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [0, 2, 20], [1, 3, 15], [1, 4, 25], [2, 5, 30], [2, 6, 35]],signalSpeed = 5) == [9, 9, 9, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 7], [0, 2, 14], [1, 3, 21], [1, 4, 28], [2, 5, 35], [2, 6, 42], [3, 7, 49], [4, 8, 56], [5, 9, 63], [6, 10, 70], [7, 11, 77], [8, 12, 84], [9, 13, 91], [10, 14, 98], [11, 15, 105], [12, 16, 112], [13, 17, 119], [14, 18, 126]],signalSpeed = 7) == [81, 96, 96, 45, 45, 45, 45, 32, 32, 32, 32, 17, 17, 17, 17, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 7], [0, 2, 14], [1, 3, 21], [1, 4, 28], [2, 5, 35], [2, 6, 42], [3, 7, 49], [4, 8, 56], [5, 9, 63], [6, 10, 70], [7, 11, 77], [8, 12, 84], [9, 13, 91], [10, 14, 98], [11, 15, 105], [12, 16, 112], [13, 17, 119], [14, 18, 126]],signalSpeed = 7) == [81, 96, 96, 45, 45, 45, 45, 32, 32, 32, 32, 17, 17, 17, 17, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [0, 2, 9], [1, 3, 12], [1, 4, 6], [2, 5, 15], [2, 6, 3]],signalSpeed = 3) == [9, 9, 9, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [0, 2, 9], [1, 3, 12], [1, 4, 6], [2, 5, 15], [2, 6, 3]],signalSpeed = 3) == [9, 9, 9, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [1, 5, 1], [1, 6, 1], [2, 7, 1], [2, 8, 1], [3, 9, 1], [3, 10, 1], [4, 11, 1], [4, 12, 1]],signalSpeed = 1) == [54, 21, 21, 21, 21, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [1, 5, 1], [1, 6, 1], [2, 7, 1], [2, 8, 1], [3, 9, 1], [3, 10, 1], [4, 11, 1], [4, 12, 1]],signalSpeed = 1) == [54, 21, 21, 21, 21, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [0, 2, 10], [0, 3, 15], [1, 4, 20], [2, 5, 25], [3, 6, 30]],signalSpeed = 5) == [12, 5, 5, 5, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [0, 2, 10], [0, 3, 15], [1, 4, 20], [2, 5, 25], [3, 6, 30]],signalSpeed = 5) == [12, 5, 5, 5, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70]],signalSpeed = 5) == [0, 6, 10, 12, 12, 10, 6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70]],signalSpeed = 5) == [0, 6, 10, 12, 12, 10, 6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [0, 2, 10], [1, 3, 15], [1, 4, 20], [2, 5, 25], [2, 6, 30], [3, 7, 35], [4, 8, 40], [5, 9, 45], [6, 10, 50], [7, 11, 55], [8, 12, 60], [9, 13, 65], [10, 14, 70]],signalSpeed = 5) == [49, 57, 57, 24, 24, 24, 24, 13, 13, 13, 13, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [0, 2, 10], [1, 3, 15], [1, 4, 20], [2, 5, 25], [2, 6, 30], [3, 7, 35], [4, 8, 40], [5, 9, 45], [6, 10, 50], [7, 11, 55], [8, 12, 60], [9, 13, 65], [10, 14, 70]],signalSpeed = 5) == [49, 57, 57, 24, 24, 24, 24, 13, 13, 13, 13, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70], [7, 8, 80], [8, 9, 90], [9, 10, 100], [10, 11, 110]],signalSpeed = 10) == [0, 10, 18, 24, 28, 30, 30, 28, 24, 18, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70], [7, 8, 80], [8, 9, 90], [9, 10, 100], [10, 11, 110]],signalSpeed = 10) == [0, 10, 18, 24, 28, 30, 30, 28, 24, 18, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [0, 2, 2], [1, 3, 3], [1, 4, 4], [2, 5, 5], [2, 6, 6], [3, 7, 7], [3, 8, 8], [4, 9, 9], [5, 10, 10], [6, 11, 11]],signalSpeed = 1) == [30, 36, 32, 19, 10, 10, 10, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [0, 2, 2], [1, 3, 3], [1, 4, 4], [2, 5, 5], [2, 6, 6], [3, 7, 7], [3, 8, 8], [4, 9, 9], [5, 10, 10], [6, 11, 11]],signalSpeed = 1) == [30, 36, 32, 19, 10, 10, 10, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 11], [1, 2, 22], [2, 3, 33], [3, 4, 44], [4, 5, 55], [5, 6, 66], [6, 7, 77], [7, 8, 88], [8, 9, 99]],signalSpeed = 33) == [0, 0, 5, 8, 1, 9, 8, 0, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 11], [1, 2, 22], [2, 3, 33], [3, 4, 44], [4, 5, 55], [5, 6, 66], [6, 7, 77], [7, 8, 88], [8, 9, 99]],signalSpeed = 33) == [0, 0, 5, 8, 1, 9, 8, 0, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 100], [1, 2, 200], [2, 3, 300], [3, 4, 400], [4, 5, 500], [5, 6, 600], [6, 7, 700], [7, 8, 800]],signalSpeed = 100) == [0, 7, 12, 15, 16, 15, 12, 7, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 100], [1, 2, 200], [2, 3, 300], [3, 4, 400], [4, 5, 500], [5, 6, 600], [6, 7, 700], [7, 8, 800]],signalSpeed = 100) == [0, 7, 12, 15, 16, 15, 12, 7, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [1, 2, 4], [2, 3, 5], [3, 4, 6], [4, 5, 7], [5, 6, 8], [6, 7, 9]],signalSpeed = 3) == [0, 4, 0, 6, 6, 0, 4, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [1, 2, 4], [2, 3, 5], [3, 4, 6], [4, 5, 7], [5, 6, 8], [6, 7, 9]],signalSpeed = 3) == [0, 4, 0, 6, 6, 0, 4, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [1, 2, 10], [2, 3, 15], [3, 4, 20], [4, 5, 25], [5, 6, 30], [6, 7, 35], [7, 8, 40]],signalSpeed = 7) == [0, 0, 0, 0, 0, 1, 1, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [1, 2, 10], [2, 3, 15], [3, 4, 20], [4, 5, 25], [5, 6, 30], [6, 7, 35], [7, 8, 40]],signalSpeed = 7) == [0, 0, 0, 0, 0, 1, 1, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 11], [0, 2, 22], [2, 3, 33], [2, 4, 44], [4, 5, 55], [4, 6, 66], [6, 7, 77], [6, 8, 88], [8, 9, 99], [8, 10, 110], [9, 11, 121], [11, 12, 132]],signalSpeed = 11) == [11, 0, 29, 0, 39, 0, 41, 0, 35, 20, 0, 11, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 11], [0, 2, 22], [2, 3, 33], [2, 4, 44], [4, 5, 55], [4, 6, 66], [6, 7, 77], [6, 8, 88], [8, 9, 99], [8, 10, 110], [9, 11, 121], [11, 12, 132]],signalSpeed = 11) == [11, 0, 29, 0, 39, 0, 41, 0, 35, 20, 0, 11, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [1, 2, 15], [1, 3, 25], [3, 4, 35], [3, 5, 45], [5, 6, 55], [5, 7, 65], [7, 8, 75], [7, 9, 85], [9, 10, 95]],signalSpeed = 5) == [0, 17, 0, 27, 0, 29, 0, 23, 0, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [1, 2, 15], [1, 3, 25], [3, 4, 35], [3, 5, 45], [5, 6, 55], [5, 7, 65], [7, 8, 75], [7, 9, 85], [9, 10, 95]],signalSpeed = 5) == [0, 17, 0, 27, 0, 29, 0, 23, 0, 9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 8], [0, 2, 16], [1, 3, 24], [1, 4, 32], [2, 5, 40], [2, 6, 48], [3, 7, 56], [3, 8, 64], [4, 9, 72], [4, 10, 80], [5, 11, 88], [5, 12, 96], [6, 13, 104], [6, 14, 112]],signalSpeed = 8) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 8], [0, 2, 16], [1, 3, 24], [1, 4, 32], [2, 5, 40], [2, 6, 48], [3, 7, 56], [3, 8, 64], [4, 9, 72], [4, 10, 80], [5, 11, 88], [5, 12, 96], [6, 13, 104], [6, 14, 112]],signalSpeed = 8) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 11], [0, 2, 22], [1, 3, 33], [1, 4, 44], [2, 5, 55], [2, 6, 66], [3, 7, 77], [4, 8, 88], [5, 9, 99], [6, 10, 110], [7, 11, 121], [8, 12, 132], [9, 13, 143], [10, 14, 154], [11, 15, 165], [12, 16, 176], [13, 17, 187], [14, 18, 198], [15, 19, 209], [16, 20, 220]],signalSpeed = 11) == [99, 125, 112, 64, 64, 51, 51, 51, 51, 36, 36, 36, 36, 19, 19, 19, 19, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 11], [0, 2, 22], [1, 3, 33], [1, 4, 44], [2, 5, 55], [2, 6, 66], [3, 7, 77], [4, 8, 88], [5, 9, 99], [6, 10, 110], [7, 11, 121], [8, 12, 132], [9, 13, 143], [10, 14, 154], [11, 15, 165], [12, 16, 176], [13, 17, 187], [14, 18, 198], [15, 19, 209], [16, 20, 220]],signalSpeed = 11) == [99, 125, 112, 64, 64, 51, 51, 51, 51, 36, 36, 36, 36, 19, 19, 19, 19, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 19], [0, 2, 38], [1, 3, 57], [1, 4, 76], [2, 5, 95], [2, 6, 114], [3, 7, 133], [3, 8, 152], [4, 9, 171], [4, 10, 190], [5, 11, 209], [5, 12, 228], [6, 13, 247], [6, 14, 266]],signalSpeed = 19) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 19], [0, 2, 38], [1, 3, 57], [1, 4, 76], [2, 5, 95], [2, 6, 114], [3, 7, 133], [3, 8, 152], [4, 9, 171], [4, 10, 190], [5, 11, 209], [5, 12, 228], [6, 13, 247], [6, 14, 266]],signalSpeed = 19) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [1, 2, 10], [2, 3, 15], [3, 4, 20], [4, 5, 25], [5, 6, 30], [6, 7, 35], [7, 8, 40], [8, 9, 45]],signalSpeed = 5) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [1, 2, 10], [2, 3, 15], [3, 4, 20], [4, 5, 25], [5, 6, 30], [6, 7, 35], [7, 8, 40], [8, 9, 45]],signalSpeed = 5) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 13], [1, 2, 26], [2, 3, 39], [3, 4, 52], [4, 5, 65], [5, 6, 78], [6, 7, 91], [7, 8, 104], [8, 9, 117], [9, 10, 130]],signalSpeed = 13) == [0, 9, 16, 21, 24, 25, 24, 21, 16, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 13], [1, 2, 26], [2, 3, 39], [3, 4, 52], [4, 5, 65], [5, 6, 78], [6, 7, 91], [7, 8, 104], [8, 9, 117], [9, 10, 130]],signalSpeed = 13) == [0, 9, 16, 21, 24, 25, 24, 21, 16, 9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 15], [1, 2, 30], [2, 3, 45], [3, 4, 60], [4, 5, 75], [5, 6, 90], [6, 7, 105], [7, 8, 120]],signalSpeed = 15) == [0, 7, 12, 15, 16, 15, 12, 7, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 15], [1, 2, 30], [2, 3, 45], [3, 4, 60], [4, 5, 75], [5, 6, 90], [6, 7, 105], [7, 8, 120]],signalSpeed = 15) == [0, 7, 12, 15, 16, 15, 12, 7, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [0, 2, 9], [2, 3, 27], [2, 4, 81], [4, 5, 243], [4, 6, 729], [6, 7, 2187], [6, 8, 6561], [8, 9, 19683], [8, 10, 59049]],signalSpeed = 3) == [9, 0, 23, 0, 29, 0, 27, 0, 17, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [0, 2, 9], [2, 3, 27], [2, 4, 81], [4, 5, 243], [4, 6, 729], [6, 7, 2187], [6, 8, 6561], [8, 9, 19683], [8, 10, 59049]],signalSpeed = 3) == [9, 0, 23, 0, 29, 0, 27, 0, 17, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 7], [1, 2, 14], [2, 3, 21], [3, 4, 28], [4, 5, 35], [5, 6, 42], [6, 7, 49], [7, 8, 56], [8, 9, 63], [9, 10, 70]],signalSpeed = 7) == [0, 9, 16, 21, 24, 25, 24, 21, 16, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 7], [1, 2, 14], [2, 3, 21], [3, 4, 28], [4, 5, 35], [5, 6, 42], [6, 7, 49], [7, 8, 56], [8, 9, 63], [9, 10, 70]],signalSpeed = 7) == [0, 9, 16, 21, 24, 25, 24, 21, 16, 9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [1, 2, 9], [2, 3, 12], [1, 4, 7], [4, 5, 14], [5, 6, 8]],signalSpeed = 3) == [0, 5, 3, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [1, 2, 9], [2, 3, 12], [1, 4, 7], [4, 5, 14], [5, 6, 8]],signalSpeed = 3) == [0, 5, 3, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 13], [0, 2, 26], [1, 3, 39], [1, 4, 52], [2, 5, 65], [2, 6, 78], [3, 7, 91], [3, 8, 104], [4, 9, 117], [4, 10, 130], [5, 11, 143], [5, 12, 156], [6, 13, 169], [6, 14, 182]],signalSpeed = 13) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 13], [0, 2, 26], [1, 3, 39], [1, 4, 52], [2, 5, 65], [2, 6, 78], [3, 7, 91], [3, 8, 104], [4, 9, 117], [4, 10, 130], [5, 11, 143], [5, 12, 156], [6, 13, 169], [6, 14, 182]],signalSpeed = 13) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [0, 2, 3], [0, 3, 5], [1, 4, 7], [1, 5, 9], [2, 6, 11], [2, 7, 13], [3, 8, 15], [3, 9, 17]],signalSpeed = 1) == [27, 15, 15, 15, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [0, 2, 3], [0, 3, 5], [1, 4, 7], [1, 5, 9], [2, 6, 11], [2, 7, 13], [3, 8, 15], [3, 9, 17]],signalSpeed = 1) == [27, 15, 15, 15, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9]],signalSpeed = 3) == [0, 0, 5, 8, 1, 9, 8, 0, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9]],signalSpeed = 3) == [0, 0, 5, 8, 1, 9, 8, 0, 5, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [1, 4, 40], [1, 5, 50], [2, 6, 60], [2, 7, 70], [3, 8, 80], [3, 9, 90]],signalSpeed = 10) == [27, 15, 15, 15, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [1, 4, 40], [1, 5, 50], [2, 6, 60], [2, 7, 70], [3, 8, 80], [3, 9, 90]],signalSpeed = 10) == [27, 15, 15, 15, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 11], [0, 2, 22], [1, 3, 33], [1, 4, 44], [2, 5, 55], [2, 6, 66], [3, 7, 77], [3, 8, 88], [4, 9, 99], [4, 10, 110], [5, 11, 121], [5, 12, 132], [6, 13, 143], [6, 14, 154]],signalSpeed = 11) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 11], [0, 2, 22], [1, 3, 33], [1, 4, 44], [2, 5, 55], [2, 6, 66], [3, 7, 77], [3, 8, 88], [4, 9, 99], [4, 10, 110], [5, 11, 121], [5, 12, 132], [6, 13, 143], [6, 14, 154]],signalSpeed = 11) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [0, 2, 10], [1, 3, 15], [1, 4, 20], [2, 5, 25], [2, 6, 30], [3, 7, 35], [3, 8, 40], [4, 9, 45], [4, 10, 50], [5, 11, 55], [5, 12, 60], [6, 13, 65], [6, 14, 70]],signalSpeed = 5) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [0, 2, 10], [1, 3, 15], [1, 4, 20], [2, 5, 25], [2, 6, 30], [3, 7, 35], [3, 8, 40], [4, 9, 45], [4, 10, 50], [5, 11, 55], [5, 12, 60], [6, 13, 65], [6, 14, 70]],signalSpeed = 5) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [0, 2, 20], [1, 3, 30], [1, 4, 40], [2, 5, 50], [2, 6, 60], [5, 7, 70], [5, 8, 80]],signalSpeed = 10) == [15, 13, 19, 0, 0, 13, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [0, 2, 20], [1, 3, 30], [1, 4, 40], [2, 5, 50], [2, 6, 60], [5, 7, 70], [5, 8, 80]],signalSpeed = 10) == [15, 13, 19, 0, 0, 13, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 13], [1, 2, 26], [2, 3, 39], [3, 4, 52], [4, 5, 65], [5, 6, 78], [6, 7, 91], [7, 8, 104], [8, 9, 117], [9, 10, 130], [10, 11, 143]],signalSpeed = 13) == [0, 10, 18, 24, 28, 30, 30, 28, 24, 18, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 13], [1, 2, 26], [2, 3, 39], [3, 4, 52], [4, 5, 65], [5, 6, 78], [6, 7, 91], [7, 8, 104], [8, 9, 117], [9, 10, 130], [10, 11, 143]],signalSpeed = 13) == [0, 10, 18, 24, 28, 30, 30, 28, 24, 18, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 6], [1, 2, 12], [2, 3, 18], [3, 4, 24], [4, 5, 30], [5, 6, 36], [6, 7, 42], [7, 8, 48], [8, 9, 54]],signalSpeed = 6) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 6], [1, 2, 12], [2, 3, 18], [3, 4, 24], [4, 5, 30], [5, 6, 36], [6, 7, 42], [7, 8, 48], [8, 9, 54]],signalSpeed = 6) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 6], [3, 4, 8], [4, 5, 10], [5, 6, 12], [6, 7, 14], [7, 8, 16], [8, 9, 18], [9, 10, 20]],signalSpeed = 2) == [0, 9, 16, 21, 24, 25, 24, 21, 16, 9, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 6], [3, 4, 8], [4, 5, 10], [5, 6, 12], [6, 7, 14], [7, 8, 16], [8, 9, 18], [9, 10, 20]],signalSpeed = 2) == [0, 9, 16, 21, 24, 25, 24, 21, 16, 9, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [1, 2, 9], [2, 3, 27], [3, 4, 81], [4, 5, 243], [5, 6, 729], [6, 7, 2187], [7, 8, 6561], [8, 9, 19683]],signalSpeed = 3) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [1, 2, 9], [2, 3, 27], [3, 4, 81], [4, 5, 243], [5, 6, 729], [6, 7, 2187], [7, 8, 6561], [8, 9, 19683]],signalSpeed = 3) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 7], [0, 2, 14], [1, 3, 21], [1, 4, 28], [2, 5, 35], [2, 6, 42], [3, 7, 49], [4, 8, 56], [5, 9, 63]],signalSpeed = 7) == [20, 24, 20, 8, 8, 8, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 7], [0, 2, 14], [1, 3, 21], [1, 4, 28], [2, 5, 35], [2, 6, 42], [3, 7, 49], [4, 8, 56], [5, 9, 63]],signalSpeed = 7) == [20, 24, 20, 8, 8, 8, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 9], [1, 2, 18], [2, 3, 27], [3, 4, 36], [4, 5, 45], [5, 6, 54], [6, 7, 63], [7, 8, 72], [8, 9, 81], [9, 10, 90], [10, 11, 99]],signalSpeed = 9) == [0, 10, 18, 24, 28, 30, 30, 28, 24, 18, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 9], [1, 2, 18], [2, 3, 27], [3, 4, 36], [4, 5, 45], [5, 6, 54], [6, 7, 63], [7, 8, 72], [8, 9, 81], [9, 10, 90], [10, 11, 99]],signalSpeed = 9) == [0, 10, 18, 24, 28, 30, 30, 28, 24, 18, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 17], [1, 2, 34], [2, 3, 51], [3, 4, 68], [4, 5, 85], [5, 6, 102], [6, 7, 119], [7, 8, 136], [8, 9, 153], [9, 10, 170], [10, 11, 187], [11, 12, 204]],signalSpeed = 17) == [0, 11, 20, 27, 32, 35, 36, 35, 32, 27, 20, 11, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 17], [1, 2, 34], [2, 3, 51], [3, 4, 68], [4, 5, 85], [5, 6, 102], [6, 7, 119], [7, 8, 136], [8, 9, 153], [9, 10, 170], [10, 11, 187], [11, 12, 204]],signalSpeed = 17) == [0, 11, 20, 27, 32, 35, 36, 35, 32, 27, 20, 11, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 6], [3, 4, 8], [4, 5, 10], [5, 6, 12], [6, 7, 14], [7, 8, 16], [8, 9, 18]],signalSpeed = 2) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 6], [3, 4, 8], [4, 5, 10], [5, 6, 12], [6, 7, 14], [7, 8, 16], [8, 9, 18]],signalSpeed = 2) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [1, 2, 10], [2, 3, 15], [3, 4, 20], [4, 5, 25], [5, 6, 30], [6, 7, 35], [7, 8, 40]],signalSpeed = 5) == [0, 7, 12, 15, 16, 15, 12, 7, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [1, 2, 10], [2, 3, 15], [3, 4, 20], [4, 5, 25], [5, 6, 30], [6, 7, 35], [7, 8, 40]],signalSpeed = 5) == [0, 7, 12, 15, 16, 15, 12, 7, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 23], [1, 2, 46], [2, 3, 69], [3, 4, 92], [4, 5, 115], [5, 6, 138], [6, 7, 161], [7, 8, 184], [8, 9, 207], [9, 10, 230], [10, 11, 253], [11, 12, 276], [12, 13, 299], [13, 14, 322]],signalSpeed = 23) == [0, 13, 24, 33, 40, 45, 48, 49, 48, 45, 40, 33, 24, 13, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 23], [1, 2, 46], [2, 3, 69], [3, 4, 92], [4, 5, 115], [5, 6, 138], [6, 7, 161], [7, 8, 184], [8, 9, 207], [9, 10, 230], [10, 11, 253], [11, 12, 276], [12, 13, 299], [13, 14, 322]],signalSpeed = 23) == [0, 13, 24, 33, 40, 45, 48, 49, 48, 45, 40, 33, 24, 13, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 12], [0, 2, 24], [1, 3, 36], [1, 4, 48], [2, 5, 60], [2, 6, 72], [3, 7, 84], [3, 8, 96], [4, 9, 108], [4, 10, 120], [5, 11, 132], [5, 12, 144], [6, 13, 156], [6, 14, 168]],signalSpeed = 12) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 12], [0, 2, 24], [1, 3, 36], [1, 4, 48], [2, 5, 60], [2, 6, 72], [3, 7, 84], [3, 8, 96], [4, 9, 108], [4, 10, 120], [5, 11, 132], [5, 12, 144], [6, 13, 156], [6, 14, 168]],signalSpeed = 12) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 100], [1, 2, 200], [2, 3, 300], [3, 4, 400], [4, 5, 500], [5, 6, 600], [6, 7, 700], [7, 8, 800], [8, 9, 900]],signalSpeed = 50) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 100], [1, 2, 200], [2, 3, 300], [3, 4, 400], [4, 5, 500], [5, 6, 600], [6, 7, 700], [7, 8, 800], [8, 9, 900]],signalSpeed = 50) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 19], [1, 2, 38], [2, 3, 57], [3, 4, 76], [4, 5, 95], [5, 6, 114], [6, 7, 133], [7, 8, 152], [8, 9, 171], [9, 10, 190], [10, 11, 209], [11, 12, 228], [12, 13, 247]],signalSpeed = 19) == [0, 12, 22, 30, 36, 40, 42, 42, 40, 36, 30, 22, 12, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 19], [1, 2, 38], [2, 3, 57], [3, 4, 76], [4, 5, 95], [5, 6, 114], [6, 7, 133], [7, 8, 152], [8, 9, 171], [9, 10, 190], [10, 11, 209], [11, 12, 228], [12, 13, 247]],signalSpeed = 19) == [0, 12, 22, 30, 36, 40, 42, 42, 40, 36, 30, 22, 12, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 11], [1, 2, 22], [2, 3, 33], [3, 4, 44], [4, 5, 55], [5, 6, 66], [6, 7, 77], [7, 8, 88], [8, 9, 99]],signalSpeed = 11) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 11], [1, 2, 22], [2, 3, 33], [3, 4, 44], [4, 5, 55], [5, 6, 66], [6, 7, 77], [7, 8, 88], [8, 9, 99]],signalSpeed = 11) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 11], [0, 2, 22], [0, 3, 33], [1, 4, 44], [1, 5, 55], [2, 6, 66], [2, 7, 77], [3, 8, 88], [3, 9, 99], [4, 10, 110], [4, 11, 121], [5, 12, 132], [5, 13, 143], [6, 14, 154], [6, 15, 165], [7, 16, 176], [7, 17, 187], [8, 18, 198], [8, 19, 209], [9, 20, 220], [9, 21, 231]],signalSpeed = 11) == [147, 99, 99, 99, 39, 39, 39, 39, 39, 39, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 11], [0, 2, 22], [0, 3, 33], [1, 4, 44], [1, 5, 55], [2, 6, 66], [2, 7, 77], [3, 8, 88], [3, 9, 99], [4, 10, 110], [4, 11, 121], [5, 12, 132], [5, 13, 143], [6, 14, 154], [6, 15, 165], [7, 16, 176], [7, 17, 187], [8, 18, 198], [8, 19, 209], [9, 20, 220], [9, 21, 231]],signalSpeed = 11) == [147, 99, 99, 99, 39, 39, 39, 39, 39, 39, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 11], [1, 2, 22], [1, 3, 33], [2, 4, 44], [2, 5, 55], [3, 6, 66], [3, 7, 77], [4, 8, 88], [5, 9, 99], [6, 10, 110], [7, 11, 121]],signalSpeed = 11) == [0, 35, 32, 32, 10, 10, 10, 10, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 11], [1, 2, 22], [1, 3, 33], [2, 4, 44], [2, 5, 55], [3, 6, 66], [3, 7, 77], [4, 8, 88], [5, 9, 99], [6, 10, 110], [7, 11, 121]],signalSpeed = 11) == [0, 35, 32, 32, 10, 10, 10, 10, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [1, 2, 6], [1, 3, 9], [2, 4, 12], [2, 5, 15], [3, 6, 18], [3, 7, 21]],signalSpeed = 3) == [0, 15, 11, 11, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [1, 2, 6], [1, 3, 9], [2, 4, 12], [2, 5, 15], [3, 6, 18], [3, 7, 21]],signalSpeed = 3) == [0, 15, 11, 11, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [0, 2, 4], [0, 3, 6], [1, 4, 8], [1, 5, 10], [2, 6, 12], [2, 7, 14], [3, 8, 16], [3, 9, 18]],signalSpeed = 2) == [27, 15, 15, 15, 0, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [0, 2, 4], [0, 3, 6], [1, 4, 8], [1, 5, 10], [2, 6, 12], [2, 7, 14], [3, 8, 16], [3, 9, 18]],signalSpeed = 2) == [27, 15, 15, 15, 0, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 6], [1, 2, 12], [2, 3, 18], [3, 4, 24], [4, 5, 30], [5, 6, 36], [6, 7, 42], [7, 8, 48], [8, 9, 54], [9, 10, 60], [10, 11, 66]],signalSpeed = 6) == [0, 10, 18, 24, 28, 30, 30, 28, 24, 18, 10, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 6], [1, 2, 12], [2, 3, 18], [3, 4, 24], [4, 5, 30], [5, 6, 36], [6, 7, 42], [7, 8, 48], [8, 9, 54], [9, 10, 60], [10, 11, 66]],signalSpeed = 6) == [0, 10, 18, 24, 28, 30, 30, 28, 24, 18, 10, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70]],signalSpeed = 10) == [0, 6, 10, 12, 12, 10, 6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70]],signalSpeed = 10) == [0, 6, 10, 12, 12, 10, 6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [0, 2, 6], [1, 3, 9], [1, 4, 12], [2, 5, 15], [2, 6, 18], [3, 7, 21], [4, 8, 24], [5, 9, 27], [6, 10, 30]],signalSpeed = 3) == [25, 28, 28, 9, 9, 9, 9, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [0, 2, 6], [1, 3, 9], [1, 4, 12], [2, 5, 15], [2, 6, 18], [3, 7, 21], [4, 8, 24], [5, 9, 27], [6, 10, 30]],signalSpeed = 3) == [25, 28, 28, 9, 9, 9, 9, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [0, 2, 4], [1, 3, 6], [1, 4, 8], [2, 5, 10], [2, 6, 12]],signalSpeed = 2) == [9, 9, 9, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [0, 2, 4], [1, 3, 6], [1, 4, 8], [2, 5, 10], [2, 6, 12]],signalSpeed = 2) == [9, 9, 9, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 7], [1, 2, 14], [2, 3, 21], [3, 4, 28], [4, 5, 35], [5, 6, 42], [6, 7, 49], [7, 8, 56], [8, 9, 63]],signalSpeed = 7) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 7], [1, 2, 14], [2, 3, 21], [3, 4, 28], [4, 5, 35], [5, 6, 42], [6, 7, 49], [7, 8, 56], [8, 9, 63]],signalSpeed = 7) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 17], [1, 2, 34], [1, 3, 51], [2, 4, 68], [2, 5, 85], [3, 6, 102], [3, 7, 119], [4, 8, 136], [5, 9, 153], [6, 10, 170], [7, 11, 187], [8, 12, 204], [9, 13, 221], [10, 14, 238]],signalSpeed = 17) == [0, 55, 57, 51, 24, 24, 24, 13, 13, 13, 13, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 17], [1, 2, 34], [1, 3, 51], [2, 4, 68], [2, 5, 85], [3, 6, 102], [3, 7, 119], [4, 8, 136], [5, 9, 153], [6, 10, 170], [7, 11, 187], [8, 12, 204], [9, 13, 221], [10, 14, 238]],signalSpeed = 17) == [0, 55, 57, 51, 24, 24, 24, 13, 13, 13, 13, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 14], [0, 2, 28], [1, 3, 42], [1, 4, 56], [2, 5, 70], [2, 6, 84], [4, 7, 98], [4, 8, 112], [5, 9, 126], [5, 10, 140], [7, 11, 154], [7, 12, 168]],signalSpeed = 14) == [35, 41, 35, 0, 35, 21, 0, 21, 0, 0, 0, 0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 14], [0, 2, 28], [1, 3, 42], [1, 4, 56], [2, 5, 70], [2, 6, 84], [4, 7, 98], [4, 8, 112], [5, 9, 126], [5, 10, 140], [7, 11, 154], [7, 12, 168]],signalSpeed = 14) == [35, 41, 35, 0, 35, 21, 0, 21, 0, 0, 0, 0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [1, 2, 6], [2, 3, 9], [3, 4, 12], [4, 5, 15], [5, 6, 18]],signalSpeed = 3) == [0, 5, 8, 9, 8, 5, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [1, 2, 6], [2, 3, 9], [3, 4, 12], [4, 5, 15], [5, 6, 18]],signalSpeed = 3) == [0, 5, 8, 9, 8, 5, 0]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1]],signalSpeed = 1) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]
    assert candidate(edges = [[0, 1, 1], [1, 2, 5], [2, 3, 13], [3, 4, 9], [4, 5, 2]],signalSpeed = 1) == [0, 4, 6, 6, 4, 0]
    assert candidate(edges = [[0, 1, 5], [1, 2, 10], [2, 3, 15], [3, 4, 20]],signalSpeed = 5) == [0, 3, 4, 3, 0]
    assert candidate(edges = [[0, 1, 2], [0, 2, 3], [1, 3, 4], [1, 4, 5], [2, 5, 6], [2, 6, 7]],signalSpeed = 1) == [9, 9, 9, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 10], [0, 2, 10], [1, 3, 10], [1, 4, 10], [2, 5, 10], [2, 6, 10]],signalSpeed = 5) == [9, 9, 9, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 4], [1, 2, 8], [2, 3, 12], [3, 4, 16]],signalSpeed = 4) == [0, 3, 4, 3, 0]
    assert candidate(edges = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]],signalSpeed = 2) == [0, 2, 0, 0, 2, 0]
    assert candidate(edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 4, 4], [1, 5, 5], [2, 6, 6], [3, 7, 7]],signalSpeed = 1) == [16, 11, 6, 6, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 6], [3, 4, 8]],signalSpeed = 2) == [0, 3, 4, 3, 0]
    assert candidate(edges = [[0, 1, 3], [1, 2, 6], [2, 3, 9], [3, 4, 12], [4, 5, 15]],signalSpeed = 3) == [0, 4, 6, 6, 4, 0]
    assert candidate(edges = [[0, 6, 3], [6, 5, 3], [0, 3, 1], [3, 2, 7], [3, 1, 6], [3, 4, 2]],signalSpeed = 3) == [2, 0, 0, 0, 0, 0, 2]
    assert candidate(edges = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40]],signalSpeed = 10) == [0, 3, 4, 3, 0]
    assert candidate(edges = [[0, 1, 4], [1, 2, 8], [2, 3, 12]],signalSpeed = 4) == [0, 2, 2, 0]
    assert candidate(edges = [[0, 1, 4], [1, 2, 5], [2, 3, 6]],signalSpeed = 2) == [0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 8], [3, 4, 16]],signalSpeed = 2) == [0, 3, 4, 3, 0]
    assert candidate(edges = [[0, 1, 13], [0, 2, 26], [1, 3, 39], [1, 4, 52], [2, 5, 65], [2, 6, 78], [3, 7, 91], [4, 8, 104], [5, 9, 117], [6, 10, 130], [7, 11, 143], [8, 12, 156], [9, 13, 169]],signalSpeed = 13) == [42, 51, 46, 22, 22, 22, 12, 12, 12, 12, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 19], [1, 2, 38], [1, 3, 57], [2, 4, 76], [2, 5, 95], [3, 6, 114], [3, 7, 133], [4, 8, 152], [5, 9, 171], [6, 10, 190], [7, 11, 209], [8, 12, 228], [9, 13, 247], [10, 14, 266], [11, 15, 285], [12, 16, 304], [13, 17, 323], [14, 18, 342]],signalSpeed = 19) == [0, 89, 96, 89, 45, 45, 45, 32, 32, 32, 32, 17, 17, 17, 17, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 6], [0, 2, 12], [1, 3, 18], [1, 4, 24], [2, 5, 30], [2, 6, 36], [3, 7, 42], [3, 8, 48], [4, 9, 54], [5, 10, 60], [6, 11, 66]],signalSpeed = 6) == [30, 36, 32, 19, 10, 10, 10, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 7], [0, 2, 14], [1, 3, 21], [1, 4, 28], [2, 5, 35], [2, 6, 42], [3, 7, 49], [3, 8, 56], [4, 9, 63], [4, 10, 70]],signalSpeed = 7) == [21, 33, 17, 17, 17, 0, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 11], [1, 2, 22], [2, 3, 33], [3, 4, 44], [4, 5, 55], [5, 6, 66], [6, 7, 77], [7, 8, 88], [8, 9, 99], [9, 10, 110]],signalSpeed = 11) == [0, 9, 16, 21, 24, 25, 24, 21, 16, 9, 0]
    assert candidate(edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [1, 5, 5], [1, 6, 6], [2, 7, 7], [2, 8, 8], [3, 9, 9], [3, 10, 10], [4, 11, 11], [4, 12, 12]],signalSpeed = 1) == [54, 21, 21, 21, 21, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 9], [1, 2, 18], [2, 3, 27], [3, 4, 36], [4, 5, 45], [5, 6, 54], [6, 7, 63], [7, 8, 72], [8, 9, 81], [9, 10, 90], [10, 11, 99], [11, 12, 108]],signalSpeed = 9) == [0, 11, 20, 27, 32, 35, 36, 35, 32, 27, 20, 11, 0]
    assert candidate(edges = [[0, 1, 7], [0, 2, 14], [1, 3, 21], [1, 4, 28], [2, 5, 35], [2, 6, 42], [3, 7, 49], [3, 8, 56], [4, 9, 63], [5, 10, 70], [6, 11, 77]],signalSpeed = 7) == [30, 36, 32, 19, 10, 10, 10, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 7], [0, 2, 14], [1, 3, 21], [1, 4, 28], [2, 5, 35], [2, 6, 42], [3, 7, 49], [3, 8, 56], [4, 9, 63], [4, 10, 70], [5, 11, 77], [5, 12, 84], [6, 13, 91], [6, 14, 98]],signalSpeed = 7) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 17], [0, 2, 34], [1, 3, 51], [1, 4, 68], [2, 5, 85], [2, 6, 102], [3, 7, 119], [3, 8, 136], [4, 9, 153], [4, 10, 170], [5, 11, 187], [5, 12, 204], [6, 13, 221], [6, 14, 238]],signalSpeed = 17) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 8], [3, 4, 16], [4, 5, 32], [5, 6, 64], [6, 7, 128], [7, 8, 256], [8, 9, 512]],signalSpeed = 2) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]
    assert candidate(edges = [[0, 1, 100000], [1, 2, 200000], [2, 3, 300000], [3, 4, 400000], [4, 5, 500000], [5, 6, 600000], [6, 7, 700000]],signalSpeed = 100000) == [0, 6, 10, 12, 12, 10, 6, 0]
    assert candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 8], [3, 4, 16], [4, 5, 32], [5, 6, 64]],signalSpeed = 2) == [0, 5, 8, 9, 8, 5, 0]
    assert candidate(edges = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [1, 4, 40], [1, 5, 50], [2, 6, 60], [2, 7, 70], [3, 8, 80], [3, 9, 90], [4, 10, 100], [5, 11, 110], [6, 12, 120]],signalSpeed = 10) == [47, 36, 29, 21, 11, 11, 11, 0, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8], [7, 8, 9], [8, 9, 10]],signalSpeed = 2) == [0, 4, 0, 2, 6, 6, 2, 0, 4, 0]
    assert candidate(edges = [[0, 1, 5], [1, 2, 10], [1, 3, 15], [2, 4, 20], [3, 5, 25], [4, 6, 30], [5, 7, 35]],signalSpeed = 5) == [0, 15, 10, 10, 6, 6, 0, 0]
    assert candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 8], [3, 4, 16], [4, 5, 32], [5, 6, 64], [6, 7, 128], [7, 8, 256], [8, 9, 512], [9, 10, 1024]],signalSpeed = 2) == [0, 9, 16, 21, 24, 25, 24, 21, 16, 9, 0]
    assert candidate(edges = [[0, 1, 3], [0, 2, 6], [1, 3, 9], [1, 4, 12], [2, 5, 15], [2, 6, 18]],signalSpeed = 3) == [9, 9, 9, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 7], [1, 2, 14], [2, 3, 21], [3, 4, 28], [4, 5, 35], [5, 6, 42], [6, 7, 49], [7, 8, 56]],signalSpeed = 7) == [0, 7, 12, 15, 16, 15, 12, 7, 0]
    assert candidate(edges = [[0, 1, 6], [1, 2, 12], [1, 3, 18], [3, 4, 24], [3, 5, 30], [5, 6, 36], [5, 7, 42], [7, 8, 48], [7, 9, 54], [9, 10, 60], [10, 11, 66]],signalSpeed = 6) == [0, 19, 0, 31, 0, 35, 0, 31, 0, 18, 10, 0]
    assert candidate(edges = [[0, 1, 10], [0, 2, 20], [1, 3, 15], [1, 4, 25], [2, 5, 30], [2, 6, 35]],signalSpeed = 5) == [9, 9, 9, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 7], [0, 2, 14], [1, 3, 21], [1, 4, 28], [2, 5, 35], [2, 6, 42], [3, 7, 49], [4, 8, 56], [5, 9, 63], [6, 10, 70], [7, 11, 77], [8, 12, 84], [9, 13, 91], [10, 14, 98], [11, 15, 105], [12, 16, 112], [13, 17, 119], [14, 18, 126]],signalSpeed = 7) == [81, 96, 96, 45, 45, 45, 45, 32, 32, 32, 32, 17, 17, 17, 17, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 3], [0, 2, 9], [1, 3, 12], [1, 4, 6], [2, 5, 15], [2, 6, 3]],signalSpeed = 3) == [9, 9, 9, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [1, 5, 1], [1, 6, 1], [2, 7, 1], [2, 8, 1], [3, 9, 1], [3, 10, 1], [4, 11, 1], [4, 12, 1]],signalSpeed = 1) == [54, 21, 21, 21, 21, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 5], [0, 2, 10], [0, 3, 15], [1, 4, 20], [2, 5, 25], [3, 6, 30]],signalSpeed = 5) == [12, 5, 5, 5, 0, 0, 0]
    assert candidate(edges = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70]],signalSpeed = 5) == [0, 6, 10, 12, 12, 10, 6, 0]
    assert candidate(edges = [[0, 1, 5], [0, 2, 10], [1, 3, 15], [1, 4, 20], [2, 5, 25], [2, 6, 30], [3, 7, 35], [4, 8, 40], [5, 9, 45], [6, 10, 50], [7, 11, 55], [8, 12, 60], [9, 13, 65], [10, 14, 70]],signalSpeed = 5) == [49, 57, 57, 24, 24, 24, 24, 13, 13, 13, 13, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70], [7, 8, 80], [8, 9, 90], [9, 10, 100], [10, 11, 110]],signalSpeed = 10) == [0, 10, 18, 24, 28, 30, 30, 28, 24, 18, 10, 0]
    assert candidate(edges = [[0, 1, 1], [0, 2, 2], [1, 3, 3], [1, 4, 4], [2, 5, 5], [2, 6, 6], [3, 7, 7], [3, 8, 8], [4, 9, 9], [5, 10, 10], [6, 11, 11]],signalSpeed = 1) == [30, 36, 32, 19, 10, 10, 10, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 11], [1, 2, 22], [2, 3, 33], [3, 4, 44], [4, 5, 55], [5, 6, 66], [6, 7, 77], [7, 8, 88], [8, 9, 99]],signalSpeed = 33) == [0, 0, 5, 8, 1, 9, 8, 0, 5, 0]
    assert candidate(edges = [[0, 1, 100], [1, 2, 200], [2, 3, 300], [3, 4, 400], [4, 5, 500], [5, 6, 600], [6, 7, 700], [7, 8, 800]],signalSpeed = 100) == [0, 7, 12, 15, 16, 15, 12, 7, 0]
    assert candidate(edges = [[0, 1, 3], [1, 2, 4], [2, 3, 5], [3, 4, 6], [4, 5, 7], [5, 6, 8], [6, 7, 9]],signalSpeed = 3) == [0, 4, 0, 6, 6, 0, 4, 0]
    assert candidate(edges = [[0, 1, 5], [1, 2, 10], [2, 3, 15], [3, 4, 20], [4, 5, 25], [5, 6, 30], [6, 7, 35], [7, 8, 40]],signalSpeed = 7) == [0, 0, 0, 0, 0, 1, 1, 0, 0]
    assert candidate(edges = [[0, 1, 11], [0, 2, 22], [2, 3, 33], [2, 4, 44], [4, 5, 55], [4, 6, 66], [6, 7, 77], [6, 8, 88], [8, 9, 99], [8, 10, 110], [9, 11, 121], [11, 12, 132]],signalSpeed = 11) == [11, 0, 29, 0, 39, 0, 41, 0, 35, 20, 0, 11, 0]
    assert candidate(edges = [[0, 1, 5], [1, 2, 15], [1, 3, 25], [3, 4, 35], [3, 5, 45], [5, 6, 55], [5, 7, 65], [7, 8, 75], [7, 9, 85], [9, 10, 95]],signalSpeed = 5) == [0, 17, 0, 27, 0, 29, 0, 23, 0, 9, 0]
    assert candidate(edges = [[0, 1, 8], [0, 2, 16], [1, 3, 24], [1, 4, 32], [2, 5, 40], [2, 6, 48], [3, 7, 56], [3, 8, 64], [4, 9, 72], [4, 10, 80], [5, 11, 88], [5, 12, 96], [6, 13, 104], [6, 14, 112]],signalSpeed = 8) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 11], [0, 2, 22], [1, 3, 33], [1, 4, 44], [2, 5, 55], [2, 6, 66], [3, 7, 77], [4, 8, 88], [5, 9, 99], [6, 10, 110], [7, 11, 121], [8, 12, 132], [9, 13, 143], [10, 14, 154], [11, 15, 165], [12, 16, 176], [13, 17, 187], [14, 18, 198], [15, 19, 209], [16, 20, 220]],signalSpeed = 11) == [99, 125, 112, 64, 64, 51, 51, 51, 51, 36, 36, 36, 36, 19, 19, 19, 19, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 19], [0, 2, 38], [1, 3, 57], [1, 4, 76], [2, 5, 95], [2, 6, 114], [3, 7, 133], [3, 8, 152], [4, 9, 171], [4, 10, 190], [5, 11, 209], [5, 12, 228], [6, 13, 247], [6, 14, 266]],signalSpeed = 19) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 5], [1, 2, 10], [2, 3, 15], [3, 4, 20], [4, 5, 25], [5, 6, 30], [6, 7, 35], [7, 8, 40], [8, 9, 45]],signalSpeed = 5) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]
    assert candidate(edges = [[0, 1, 13], [1, 2, 26], [2, 3, 39], [3, 4, 52], [4, 5, 65], [5, 6, 78], [6, 7, 91], [7, 8, 104], [8, 9, 117], [9, 10, 130]],signalSpeed = 13) == [0, 9, 16, 21, 24, 25, 24, 21, 16, 9, 0]
    assert candidate(edges = [[0, 1, 15], [1, 2, 30], [2, 3, 45], [3, 4, 60], [4, 5, 75], [5, 6, 90], [6, 7, 105], [7, 8, 120]],signalSpeed = 15) == [0, 7, 12, 15, 16, 15, 12, 7, 0]
    assert candidate(edges = [[0, 1, 3], [0, 2, 9], [2, 3, 27], [2, 4, 81], [4, 5, 243], [4, 6, 729], [6, 7, 2187], [6, 8, 6561], [8, 9, 19683], [8, 10, 59049]],signalSpeed = 3) == [9, 0, 23, 0, 29, 0, 27, 0, 17, 0, 0]
    assert candidate(edges = [[0, 1, 7], [1, 2, 14], [2, 3, 21], [3, 4, 28], [4, 5, 35], [5, 6, 42], [6, 7, 49], [7, 8, 56], [8, 9, 63], [9, 10, 70]],signalSpeed = 7) == [0, 9, 16, 21, 24, 25, 24, 21, 16, 9, 0]
    assert candidate(edges = [[0, 1, 3], [1, 2, 9], [2, 3, 12], [1, 4, 7], [4, 5, 14], [5, 6, 8]],signalSpeed = 3) == [0, 5, 3, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 13], [0, 2, 26], [1, 3, 39], [1, 4, 52], [2, 5, 65], [2, 6, 78], [3, 7, 91], [3, 8, 104], [4, 9, 117], [4, 10, 130], [5, 11, 143], [5, 12, 156], [6, 13, 169], [6, 14, 182]],signalSpeed = 13) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 1], [0, 2, 3], [0, 3, 5], [1, 4, 7], [1, 5, 9], [2, 6, 11], [2, 7, 13], [3, 8, 15], [3, 9, 17]],signalSpeed = 1) == [27, 15, 15, 15, 0, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9]],signalSpeed = 3) == [0, 0, 5, 8, 1, 9, 8, 0, 5, 0]
    assert candidate(edges = [[0, 1, 10], [0, 2, 20], [0, 3, 30], [1, 4, 40], [1, 5, 50], [2, 6, 60], [2, 7, 70], [3, 8, 80], [3, 9, 90]],signalSpeed = 10) == [27, 15, 15, 15, 0, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 11], [0, 2, 22], [1, 3, 33], [1, 4, 44], [2, 5, 55], [2, 6, 66], [3, 7, 77], [3, 8, 88], [4, 9, 99], [4, 10, 110], [5, 11, 121], [5, 12, 132], [6, 13, 143], [6, 14, 154]],signalSpeed = 11) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 5], [0, 2, 10], [1, 3, 15], [1, 4, 20], [2, 5, 25], [2, 6, 30], [3, 7, 35], [3, 8, 40], [4, 9, 45], [4, 10, 50], [5, 11, 55], [5, 12, 60], [6, 13, 65], [6, 14, 70]],signalSpeed = 5) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 10], [0, 2, 20], [1, 3, 30], [1, 4, 40], [2, 5, 50], [2, 6, 60], [5, 7, 70], [5, 8, 80]],signalSpeed = 10) == [15, 13, 19, 0, 0, 13, 0, 0, 0]
    assert candidate(edges = [[0, 1, 13], [1, 2, 26], [2, 3, 39], [3, 4, 52], [4, 5, 65], [5, 6, 78], [6, 7, 91], [7, 8, 104], [8, 9, 117], [9, 10, 130], [10, 11, 143]],signalSpeed = 13) == [0, 10, 18, 24, 28, 30, 30, 28, 24, 18, 10, 0]
    assert candidate(edges = [[0, 1, 6], [1, 2, 12], [2, 3, 18], [3, 4, 24], [4, 5, 30], [5, 6, 36], [6, 7, 42], [7, 8, 48], [8, 9, 54]],signalSpeed = 6) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]
    assert candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 6], [3, 4, 8], [4, 5, 10], [5, 6, 12], [6, 7, 14], [7, 8, 16], [8, 9, 18], [9, 10, 20]],signalSpeed = 2) == [0, 9, 16, 21, 24, 25, 24, 21, 16, 9, 0]
    assert candidate(edges = [[0, 1, 3], [1, 2, 9], [2, 3, 27], [3, 4, 81], [4, 5, 243], [5, 6, 729], [6, 7, 2187], [7, 8, 6561], [8, 9, 19683]],signalSpeed = 3) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]
    assert candidate(edges = [[0, 1, 7], [0, 2, 14], [1, 3, 21], [1, 4, 28], [2, 5, 35], [2, 6, 42], [3, 7, 49], [4, 8, 56], [5, 9, 63]],signalSpeed = 7) == [20, 24, 20, 8, 8, 8, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 9], [1, 2, 18], [2, 3, 27], [3, 4, 36], [4, 5, 45], [5, 6, 54], [6, 7, 63], [7, 8, 72], [8, 9, 81], [9, 10, 90], [10, 11, 99]],signalSpeed = 9) == [0, 10, 18, 24, 28, 30, 30, 28, 24, 18, 10, 0]
    assert candidate(edges = [[0, 1, 17], [1, 2, 34], [2, 3, 51], [3, 4, 68], [4, 5, 85], [5, 6, 102], [6, 7, 119], [7, 8, 136], [8, 9, 153], [9, 10, 170], [10, 11, 187], [11, 12, 204]],signalSpeed = 17) == [0, 11, 20, 27, 32, 35, 36, 35, 32, 27, 20, 11, 0]
    assert candidate(edges = [[0, 1, 2], [1, 2, 4], [2, 3, 6], [3, 4, 8], [4, 5, 10], [5, 6, 12], [6, 7, 14], [7, 8, 16], [8, 9, 18]],signalSpeed = 2) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]
    assert candidate(edges = [[0, 1, 5], [1, 2, 10], [2, 3, 15], [3, 4, 20], [4, 5, 25], [5, 6, 30], [6, 7, 35], [7, 8, 40]],signalSpeed = 5) == [0, 7, 12, 15, 16, 15, 12, 7, 0]
    assert candidate(edges = [[0, 1, 23], [1, 2, 46], [2, 3, 69], [3, 4, 92], [4, 5, 115], [5, 6, 138], [6, 7, 161], [7, 8, 184], [8, 9, 207], [9, 10, 230], [10, 11, 253], [11, 12, 276], [12, 13, 299], [13, 14, 322]],signalSpeed = 23) == [0, 13, 24, 33, 40, 45, 48, 49, 48, 45, 40, 33, 24, 13, 0]
    assert candidate(edges = [[0, 1, 12], [0, 2, 24], [1, 3, 36], [1, 4, 48], [2, 5, 60], [2, 6, 72], [3, 7, 84], [3, 8, 96], [4, 9, 108], [4, 10, 120], [5, 11, 132], [5, 12, 144], [6, 13, 156], [6, 14, 168]],signalSpeed = 12) == [49, 57, 57, 25, 25, 25, 25, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 100], [1, 2, 200], [2, 3, 300], [3, 4, 400], [4, 5, 500], [5, 6, 600], [6, 7, 700], [7, 8, 800], [8, 9, 900]],signalSpeed = 50) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]
    assert candidate(edges = [[0, 1, 19], [1, 2, 38], [2, 3, 57], [3, 4, 76], [4, 5, 95], [5, 6, 114], [6, 7, 133], [7, 8, 152], [8, 9, 171], [9, 10, 190], [10, 11, 209], [11, 12, 228], [12, 13, 247]],signalSpeed = 19) == [0, 12, 22, 30, 36, 40, 42, 42, 40, 36, 30, 22, 12, 0]
    assert candidate(edges = [[0, 1, 11], [1, 2, 22], [2, 3, 33], [3, 4, 44], [4, 5, 55], [5, 6, 66], [6, 7, 77], [7, 8, 88], [8, 9, 99]],signalSpeed = 11) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]
    assert candidate(edges = [[0, 1, 11], [0, 2, 22], [0, 3, 33], [1, 4, 44], [1, 5, 55], [2, 6, 66], [2, 7, 77], [3, 8, 88], [3, 9, 99], [4, 10, 110], [4, 11, 121], [5, 12, 132], [5, 13, 143], [6, 14, 154], [6, 15, 165], [7, 16, 176], [7, 17, 187], [8, 18, 198], [8, 19, 209], [9, 20, 220], [9, 21, 231]],signalSpeed = 11) == [147, 99, 99, 99, 39, 39, 39, 39, 39, 39, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 11], [1, 2, 22], [1, 3, 33], [2, 4, 44], [2, 5, 55], [3, 6, 66], [3, 7, 77], [4, 8, 88], [5, 9, 99], [6, 10, 110], [7, 11, 121]],signalSpeed = 11) == [0, 35, 32, 32, 10, 10, 10, 10, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 3], [1, 2, 6], [1, 3, 9], [2, 4, 12], [2, 5, 15], [3, 6, 18], [3, 7, 21]],signalSpeed = 3) == [0, 15, 11, 11, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 2], [0, 2, 4], [0, 3, 6], [1, 4, 8], [1, 5, 10], [2, 6, 12], [2, 7, 14], [3, 8, 16], [3, 9, 18]],signalSpeed = 2) == [27, 15, 15, 15, 0, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 6], [1, 2, 12], [2, 3, 18], [3, 4, 24], [4, 5, 30], [5, 6, 36], [6, 7, 42], [7, 8, 48], [8, 9, 54], [9, 10, 60], [10, 11, 66]],signalSpeed = 6) == [0, 10, 18, 24, 28, 30, 30, 28, 24, 18, 10, 0]
    assert candidate(edges = [[0, 1, 10], [1, 2, 20], [2, 3, 30], [3, 4, 40], [4, 5, 50], [5, 6, 60], [6, 7, 70]],signalSpeed = 10) == [0, 6, 10, 12, 12, 10, 6, 0]
    assert candidate(edges = [[0, 1, 3], [0, 2, 6], [1, 3, 9], [1, 4, 12], [2, 5, 15], [2, 6, 18], [3, 7, 21], [4, 8, 24], [5, 9, 27], [6, 10, 30]],signalSpeed = 3) == [25, 28, 28, 9, 9, 9, 9, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 2], [0, 2, 4], [1, 3, 6], [1, 4, 8], [2, 5, 10], [2, 6, 12]],signalSpeed = 2) == [9, 9, 9, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 7], [1, 2, 14], [2, 3, 21], [3, 4, 28], [4, 5, 35], [5, 6, 42], [6, 7, 49], [7, 8, 56], [8, 9, 63]],signalSpeed = 7) == [0, 8, 14, 18, 20, 20, 18, 14, 8, 0]
    assert candidate(edges = [[0, 1, 17], [1, 2, 34], [1, 3, 51], [2, 4, 68], [2, 5, 85], [3, 6, 102], [3, 7, 119], [4, 8, 136], [5, 9, 153], [6, 10, 170], [7, 11, 187], [8, 12, 204], [9, 13, 221], [10, 14, 238]],signalSpeed = 17) == [0, 55, 57, 51, 24, 24, 24, 13, 13, 13, 13, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 14], [0, 2, 28], [1, 3, 42], [1, 4, 56], [2, 5, 70], [2, 6, 84], [4, 7, 98], [4, 8, 112], [5, 9, 126], [5, 10, 140], [7, 11, 154], [7, 12, 168]],signalSpeed = 14) == [35, 41, 35, 0, 35, 21, 0, 21, 0, 0, 0, 0, 0]
    assert candidate(edges = [[0, 1, 3], [1, 2, 6], [2, 3, 9], [3, 4, 12], [4, 5, 15], [5, 6, 18]],signalSpeed = 3) == [0, 5, 8, 9, 8, 5, 0]


