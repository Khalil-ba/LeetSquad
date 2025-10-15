def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]],maxMoves = 10,n = 4) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]],maxMoves = 10,n = 4) == 23: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 0], [1, 2, 0]],maxMoves = 3,n = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 0], [1, 2, 0]],maxMoves = 3,n = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5]],maxMoves = 5,n = 2) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5]],maxMoves = 5,n = 2) == 6: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]],maxMoves = 17,n = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]],maxMoves = 17,n = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5]],maxMoves = 10,n = 2) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5]],maxMoves = 10,n = 2) == 7: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 0], [1, 2, 0]],maxMoves = 1,n = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 0], [1, 2, 0]],maxMoves = 1,n = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [0, 2, 2], [1, 2, 2]],maxMoves = 10,n = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [0, 2, 2], [1, 2, 2]],maxMoves = 10,n = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0]],maxMoves = 3,n = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0]],maxMoves = 3,n = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 0], [0, 2, 0], [1, 2, 0]],maxMoves = 1,n = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 0], [0, 2, 0], [1, 2, 0]],maxMoves = 1,n = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [],maxMoves = 0,n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [],maxMoves = 0,n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [0, 2, 1], [1, 2, 2]],maxMoves = 6,n = 3) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [0, 2, 1], [1, 2, 2]],maxMoves = 6,n = 3) == 13: {e}')
    
    total += 1
    try:
        result = candidate(edges = [],maxMoves = 5,n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [],maxMoves = 5,n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [],maxMoves = 10,n = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [],maxMoves = 10,n = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [0, 2, 5], [0, 3, 5], [1, 2, 5], [1, 3, 5], [2, 3, 5], [3, 4, 5], [4, 5, 5], [5, 0, 5]],maxMoves = 15,n = 6) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [0, 2, 5], [0, 3, 5], [1, 2, 5], [1, 3, 5], [2, 3, 5], [3, 4, 5], [4, 5, 5], [5, 0, 5]],maxMoves = 15,n = 6) == 51: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 0, 1], [0, 5, 1], [5, 6, 1], [6, 7, 1], [7, 0, 1], [0, 8, 1], [8, 9, 1], [9, 0, 1]],maxMoves = 20,n = 10) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 0, 1], [0, 5, 1], [5, 6, 1], [6, 7, 1], [7, 0, 1], [0, 8, 1], [8, 9, 1], [9, 0, 1]],maxMoves = 20,n = 10) == 22: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [0, 2, 10], [0, 3, 10], [0, 4, 10]],maxMoves = 15,n = 5) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [0, 2, 10], [0, 3, 10], [0, 4, 10]],maxMoves = 15,n = 5) == 45: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 100], [0, 2, 200], [1, 3, 300], [2, 4, 400], [3, 5, 500], [4, 6, 600], [5, 7, 700], [6, 8, 800], [7, 9, 900]],maxMoves = 1500,n = 10) == 3001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 100], [0, 2, 200], [1, 3, 300], [2, 4, 400], [3, 5, 500], [4, 6, 600], [5, 7, 700], [6, 8, 800], [7, 9, 900]],maxMoves = 1500,n = 10) == 3001: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [3, 4, 100], [4, 5, 100], [5, 0, 100]],maxMoves = 50,n = 6) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [3, 4, 100], [4, 5, 100], [5, 0, 100]],maxMoves = 50,n = 6) == 101: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [1, 4, 1], [1, 5, 1], [2, 6, 1], [2, 7, 1], [3, 8, 1], [3, 9, 1]],maxMoves = 5,n = 10) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [1, 4, 1], [1, 5, 1], [2, 6, 1], [2, 7, 1], [3, 8, 1], [3, 9, 1]],maxMoves = 5,n = 10) == 19: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [0, 2, 10], [0, 3, 10], [1, 2, 10], [1, 3, 10], [2, 3, 10]],maxMoves = 20,n = 4) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [0, 2, 10], [0, 3, 10], [1, 2, 10], [1, 3, 10], [2, 3, 10]],maxMoves = 20,n = 4) == 64: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [0, 2, 2], [1, 2, 1]],maxMoves = 5,n = 3) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [0, 2, 2], [1, 2, 1]],maxMoves = 5,n = 3) == 9: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [0, 3, 4], [1, 2, 1], [2, 3, 2], [3, 4, 3]],maxMoves = 10,n = 5) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [0, 3, 4], [1, 2, 1], [2, 3, 2], [3, 4, 3]],maxMoves = 10,n = 5) == 17: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1]],maxMoves = 9,n = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1]],maxMoves = 9,n = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [1, 2, 2], [2, 3, 1], [0, 3, 4]],maxMoves = 7,n = 4) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [1, 2, 2], [2, 3, 1], [0, 3, 4]],maxMoves = 7,n = 4) == 14: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 100], [0, 2, 100], [1, 2, 100], [1, 3, 100], [2, 3, 100], [3, 4, 100], [4, 5, 100], [5, 6, 100], [6, 7, 100], [7, 8, 100], [8, 9, 100]],maxMoves = 300,n = 10) == 602
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 100], [0, 2, 100], [1, 2, 100], [1, 3, 100], [2, 3, 100], [3, 4, 100], [4, 5, 100], [5, 6, 100], [6, 7, 100], [7, 8, 100], [8, 9, 100]],maxMoves = 300,n = 10) == 602: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 6, 0], [6, 0, 0]],maxMoves = 6,n = 7) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 6, 0], [6, 0, 0]],maxMoves = 6,n = 7) == 7: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [1, 2, 1], [1, 3, 1], [2, 3, 1]],maxMoves = 1,n = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [1, 2, 1], [1, 3, 1], [2, 3, 1]],maxMoves = 1,n = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 6, 0], [6, 7, 0], [7, 8, 0], [8, 9, 0]],maxMoves = 5,n = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 6, 0], [6, 7, 0], [7, 8, 0], [8, 9, 0]],maxMoves = 5,n = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [0, 2, 2], [1, 2, 3], [1, 3, 4], [2, 3, 5], [2, 4, 6], [3, 4, 7], [3, 5, 8], [4, 5, 9]],maxMoves = 20,n = 6) == 51
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [0, 2, 2], [1, 2, 3], [1, 3, 4], [2, 3, 5], [2, 4, 6], [3, 4, 7], [3, 5, 8], [4, 5, 9]],maxMoves = 20,n = 6) == 51: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [1, 2, 2], [0, 2, 4]],maxMoves = 5,n = 3) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [1, 2, 2], [0, 2, 4]],maxMoves = 5,n = 3) == 11: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [1, 2, 3], [2, 3, 3], [3, 0, 3], [0, 4, 3], [4, 5, 3], [5, 6, 3], [6, 0, 3], [1, 7, 3], [7, 8, 3], [8, 1, 3], [2, 9, 3], [9, 10, 3], [10, 2, 3]],maxMoves = 10,n = 11) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [1, 2, 3], [2, 3, 3], [3, 0, 3], [0, 4, 3], [4, 5, 3], [5, 6, 3], [6, 0, 3], [1, 7, 3], [7, 8, 3], [8, 1, 3], [2, 9, 3], [9, 10, 3], [10, 2, 3]],maxMoves = 10,n = 11) == 46: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 0, 6]],maxMoves = 12,n = 6) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 0, 6]],maxMoves = 12,n = 6) == 25: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0]],maxMoves = 5,n = 6) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0]],maxMoves = 5,n = 6) == 6: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [0, 2, 5], [1, 2, 5], [1, 3, 5], [2, 3, 5]],maxMoves = 15,n = 4) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [0, 2, 5], [1, 2, 5], [1, 3, 5], [2, 3, 5]],maxMoves = 15,n = 4) == 29: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [0, 2, 2], [1, 2, 3], [0, 3, 4], [1, 3, 5], [2, 3, 6], [0, 4, 7], [1, 4, 8], [2, 4, 9], [3, 4, 10]],maxMoves = 15,n = 5) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [0, 2, 2], [1, 2, 3], [0, 3, 4], [1, 3, 5], [2, 3, 6], [0, 4, 7], [1, 4, 8], [2, 4, 9], [3, 4, 10]],maxMoves = 15,n = 5) == 60: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1], [3, 4, 5], [2, 5, 3]],maxMoves = 15,n = 6) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1], [3, 4, 5], [2, 5, 3]],maxMoves = 15,n = 6) == 33: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [0, 2, 4], [1, 2, 5]],maxMoves = 7,n = 3) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [0, 2, 4], [1, 2, 5]],maxMoves = 7,n = 3) == 15: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [1, 2, 3], [2, 3, 2], [3, 0, 4], [0, 4, 1]],maxMoves = 9,n = 5) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [1, 2, 3], [2, 3, 2], [3, 0, 4], [0, 4, 1]],maxMoves = 9,n = 5) == 20: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [0, 2, 5], [0, 3, 5], [0, 4, 5], [1, 2, 5], [1, 3, 5], [1, 4, 5], [2, 3, 5], [2, 4, 5], [3, 4, 5]],maxMoves = 15,n = 5) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [0, 2, 5], [0, 3, 5], [0, 4, 5], [1, 2, 5], [1, 3, 5], [1, 4, 5], [2, 3, 5], [2, 4, 5], [3, 4, 5]],maxMoves = 15,n = 5) == 55: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 0, 4], [0, 2, 5], [1, 3, 6]],maxMoves = 10,n = 4) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 0, 4], [0, 2, 5], [1, 3, 6]],maxMoves = 10,n = 4) == 25: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 0, 0]],maxMoves = 1,n = 5) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 0, 0]],maxMoves = 1,n = 5) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [0, 2, 5], [2, 3, 3], [1, 4, 4]],maxMoves = 15,n = 5) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [0, 2, 5], [2, 3, 3], [1, 4, 4]],maxMoves = 15,n = 5) == 26: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 6, 0], [6, 7, 0], [7, 8, 0], [8, 9, 0], [9, 0, 0]],maxMoves = 5,n = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 6, 0], [6, 7, 0], [7, 8, 0], [8, 9, 0], [9, 0, 0]],maxMoves = 5,n = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [0, 2, 3], [1, 2, 1], [1, 3, 4], [2, 4, 2]],maxMoves = 8,n = 5) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [0, 2, 3], [1, 2, 1], [1, 3, 4], [2, 4, 2]],maxMoves = 8,n = 5) == 17: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 4, 10], [4, 0, 10], [0, 5, 10], [5, 6, 10], [6, 7, 10], [7, 0, 10], [0, 8, 10], [8, 9, 10], [9, 0, 10]],maxMoves = 30,n = 10) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 4, 10], [4, 0, 10], [0, 5, 10], [5, 6, 10], [6, 7, 10], [7, 0, 10], [0, 8, 10], [8, 9, 10], [9, 0, 10]],maxMoves = 30,n = 10) == 130: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [0, 2, 5], [1, 2, 10], [1, 3, 7], [2, 4, 3], [3, 4, 8]],maxMoves = 20,n = 5) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [0, 2, 5], [1, 2, 10], [1, 3, 7], [2, 4, 3], [3, 4, 8]],maxMoves = 20,n = 5) == 48: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 0, 6], [0, 5, 7], [5, 6, 8], [6, 7, 9], [7, 8, 10], [8, 5, 11]],maxMoves = 30,n = 9) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 0, 6], [0, 5, 7], [5, 6, 8], [6, 7, 9], [7, 8, 10], [8, 5, 11]],maxMoves = 30,n = 9) == 74: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [0, 5, 1], [0, 6, 1], [0, 7, 1], [0, 8, 1], [0, 9, 1], [0, 10, 1]],maxMoves = 1,n = 11) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [0, 5, 1], [0, 6, 1], [0, 7, 1], [0, 8, 1], [0, 9, 1], [0, 10, 1]],maxMoves = 1,n = 11) == 11: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [1, 2, 5], [2, 3, 5], [3, 4, 5], [4, 5, 5], [5, 0, 5]],maxMoves = 15,n = 6) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [1, 2, 5], [2, 3, 5], [3, 4, 5], [4, 5, 5], [5, 0, 5]],maxMoves = 15,n = 6) == 31: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1000], [1, 2, 2000], [2, 3, 3000], [3, 4, 4000]],maxMoves = 10000,n = 5) == 10001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1000], [1, 2, 2000], [2, 3, 3000], [3, 4, 4000]],maxMoves = 10000,n = 5) == 10001: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [0, 2, 3], [1, 3, 4], [2, 4, 5], [3, 5, 6], [4, 6, 7]],maxMoves = 15,n = 7) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [0, 2, 3], [1, 3, 4], [2, 4, 5], [3, 5, 6], [4, 6, 7]],maxMoves = 15,n = 7) == 31: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 4, 2], [4, 0, 2], [0, 5, 2], [5, 6, 2], [6, 7, 2], [7, 0, 2]],maxMoves = 10,n = 8) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 4, 2], [4, 0, 2], [0, 5, 2], [5, 6, 2], [6, 7, 2], [7, 0, 2]],maxMoves = 10,n = 8) == 26: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [0, 2, 3], [1, 2, 3], [1, 3, 3], [2, 3, 3], [0, 4, 3], [1, 4, 3], [2, 4, 3], [3, 4, 3]],maxMoves = 5,n = 5) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [0, 2, 3], [1, 2, 3], [1, 3, 3], [2, 3, 3], [0, 4, 3], [1, 4, 3], [2, 4, 3], [3, 4, 3]],maxMoves = 5,n = 5) == 22: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [0, 2, 20], [1, 3, 30], [2, 4, 40], [3, 4, 50]],maxMoves = 35,n = 5) == 71
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [0, 2, 20], [1, 3, 30], [2, 4, 40], [3, 4, 50]],maxMoves = 35,n = 5) == 71: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6]],maxMoves = 15,n = 7) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6]],maxMoves = 15,n = 7) == 16: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [0, 2, 3], [1, 3, 4], [1, 4, 5], [2, 5, 6], [2, 6, 7], [3, 7, 8], [3, 8, 9], [4, 8, 10], [5, 9, 11], [6, 9, 12]],maxMoves = 30,n = 10) == 87
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [0, 2, 3], [1, 3, 4], [1, 4, 5], [2, 5, 6], [2, 6, 7], [3, 7, 8], [3, 8, 9], [4, 8, 10], [5, 9, 11], [6, 9, 12]],maxMoves = 30,n = 10) == 87: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [3, 4, 100], [4, 0, 100]],maxMoves = 250,n = 5) == 501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [3, 4, 100], [4, 0, 100]],maxMoves = 250,n = 5) == 501: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 0, 1], [1, 3, 1], [2, 4, 1]],maxMoves = 5,n = 5) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 0, 1], [1, 3, 1], [2, 4, 1]],maxMoves = 5,n = 5) == 12: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 100], [0, 2, 50], [1, 3, 25], [1, 4, 75], [2, 5, 20], [2, 6, 40], [3, 7, 30], [4, 8, 60], [5, 9, 10], [6, 10, 15], [7, 11, 20], [8, 12, 25], [9, 13, 30], [10, 14, 35], [11, 15, 40], [12, 16, 45], [13, 17, 50], [14, 18, 55], [15, 19, 60]],maxMoves = 300,n = 20) == 795
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 100], [0, 2, 50], [1, 3, 25], [1, 4, 75], [2, 5, 20], [2, 6, 40], [3, 7, 30], [4, 8, 60], [5, 9, 10], [6, 10, 15], [7, 11, 20], [8, 12, 25], [9, 13, 30], [10, 14, 35], [11, 15, 40], [12, 16, 45], [13, 17, 50], [14, 18, 55], [15, 19, 60]],maxMoves = 300,n = 20) == 795: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [1, 2, 3], [2, 3, 4], [3, 4, 2], [4, 0, 6]],maxMoves = 15,n = 5) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [1, 2, 3], [2, 3, 4], [3, 4, 2], [4, 0, 6]],maxMoves = 15,n = 5) == 25: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9]],maxMoves = 25,n = 10) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9]],maxMoves = 25,n = 10) == 26: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [0, 2, 5], [1, 2, 3], [1, 3, 4], [2, 3, 2]],maxMoves = 15,n = 4) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [0, 2, 5], [1, 2, 3], [1, 3, 4], [2, 3, 2]],maxMoves = 15,n = 4) == 28: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 2, 4], [2, 3, 5]],maxMoves = 10,n = 4) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 2, 4], [2, 3, 5]],maxMoves = 10,n = 4) == 19: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [1, 2, 5], [2, 3, 5], [3, 4, 5], [4, 0, 5], [0, 5, 5], [5, 6, 5], [6, 7, 5], [7, 0, 5]],maxMoves = 15,n = 8) == 53
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [1, 2, 5], [2, 3, 5], [3, 4, 5], [4, 0, 5], [0, 5, 5], [5, 6, 5], [6, 7, 5], [7, 0, 5]],maxMoves = 15,n = 8) == 53: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 0], [0, 2, 0], [1, 2, 0], [1, 3, 0], [2, 3, 0]],maxMoves = 5,n = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 0], [0, 2, 0], [1, 2, 0], [1, 3, 0], [2, 3, 0]],maxMoves = 5,n = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [0, 2, 2], [1, 2, 1], [1, 3, 2], [2, 3, 1], [2, 4, 2], [3, 4, 1], [3, 5, 2], [4, 5, 1]],maxMoves = 5,n = 6) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [0, 2, 2], [1, 2, 1], [1, 3, 2], [2, 3, 1], [2, 4, 2], [3, 4, 1], [3, 5, 2], [4, 5, 1]],maxMoves = 5,n = 6) == 13: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 100], [0, 2, 50], [1, 2, 50], [1, 3, 30], [2, 3, 20], [2, 4, 40], [3, 4, 50]],maxMoves = 200,n = 5) == 345
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 100], [0, 2, 50], [1, 2, 50], [1, 3, 30], [2, 3, 20], [2, 4, 40], [3, 4, 50]],maxMoves = 200,n = 5) == 345: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [1, 2, 2], [2, 3, 1], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8]],maxMoves = 30,n = 9) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [1, 2, 2], [2, 3, 1], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8]],maxMoves = 30,n = 9) == 31: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [1, 2, 5], [2, 3, 5], [3, 0, 5], [0, 4, 5], [1, 4, 5], [2, 4, 5], [3, 4, 5]],maxMoves = 10,n = 5) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [1, 2, 5], [2, 3, 5], [3, 0, 5], [0, 4, 5], [1, 4, 5], [2, 4, 5], [3, 4, 5]],maxMoves = 10,n = 5) == 41: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [0, 2, 5], [0, 3, 5], [0, 4, 5], [0, 5, 5], [0, 6, 5], [0, 7, 5], [0, 8, 5], [0, 9, 5], [0, 10, 5]],maxMoves = 20,n = 11) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [0, 2, 5], [0, 3, 5], [0, 4, 5], [0, 5, 5], [0, 6, 5], [0, 7, 5], [0, 8, 5], [0, 9, 5], [0, 10, 5]],maxMoves = 20,n = 11) == 61: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [0, 2, 1], [1, 2, 2], [2, 3, 5], [3, 4, 3]],maxMoves = 12,n = 5) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [0, 2, 1], [1, 2, 2], [2, 3, 5], [3, 4, 3]],maxMoves = 12,n = 5) == 26: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 0, 0]],maxMoves = 3,n = 5) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 0, 0]],maxMoves = 3,n = 5) == 5: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 0, 0]],maxMoves = 0,n = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 0, 0]],maxMoves = 0,n = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [0, 2, 2], [0, 3, 2], [0, 4, 2], [1, 5, 2], [2, 6, 2], [3, 7, 2], [4, 8, 2], [5, 6, 2], [6, 7, 2], [7, 8, 2]],maxMoves = 5,n = 9) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [0, 2, 2], [0, 3, 2], [0, 4, 2], [1, 5, 2], [2, 6, 2], [3, 7, 2], [4, 8, 2], [5, 6, 2], [6, 7, 2], [7, 8, 2]],maxMoves = 5,n = 9) == 21: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 20], [0, 2, 15], [1, 2, 10], [1, 3, 25], [2, 4, 30], [3, 4, 5]],maxMoves = 50,n = 5) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 20], [0, 2, 15], [1, 2, 10], [1, 3, 25], [2, 4, 30], [3, 4, 5]],maxMoves = 50,n = 5) == 110: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 4], [0, 2, 4], [1, 2, 5], [1, 3, 2], [2, 3, 3]],maxMoves = 10,n = 4) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 4], [0, 2, 4], [1, 2, 5], [1, 3, 2], [2, 3, 3]],maxMoves = 10,n = 4) == 22: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 0, 7]],maxMoves = 25,n = 6) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 0, 7]],maxMoves = 25,n = 6) == 33: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [2, 3, 1], [4, 5, 1]],maxMoves = 3,n = 6) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [2, 3, 1], [4, 5, 1]],maxMoves = 3,n = 6) == 3: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [0, 5, 5], [0, 6, 6], [0, 7, 7], [0, 8, 8], [0, 9, 9]],maxMoves = 15,n = 10) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [0, 5, 5], [0, 6, 6], [0, 7, 7], [0, 8, 8], [0, 9, 9]],maxMoves = 15,n = 10) == 55: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 100], [1, 2, 200], [2, 3, 300], [3, 0, 400]],maxMoves = 800,n = 4) == 1004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 100], [1, 2, 200], [2, 3, 300], [3, 0, 400]],maxMoves = 800,n = 4) == 1004: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [1, 2, 3], [2, 3, 3], [3, 0, 3]],maxMoves = 6,n = 4) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [1, 2, 3], [2, 3, 3], [3, 0, 3]],maxMoves = 6,n = 4) == 13: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [0, 5, 1], [1, 2, 1], [1, 3, 1], [1, 4, 1], [1, 5, 1]],maxMoves = 5,n = 6) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [0, 5, 1], [1, 2, 1], [1, 3, 1], [1, 4, 1], [1, 5, 1]],maxMoves = 5,n = 6) == 15: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 0], [1, 2, 3], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 0, 0]],maxMoves = 10,n = 6) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 0], [1, 2, 3], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 0, 0]],maxMoves = 10,n = 6) == 9: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [0, 2, 4], [0, 3, 3], [1, 2, 1], [1, 3, 2], [2, 3, 5], [3, 4, 2], [4, 5, 3], [5, 6, 4], [6, 7, 1]],maxMoves = 25,n = 8) == 35
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [0, 2, 4], [0, 3, 3], [1, 2, 1], [1, 3, 2], [2, 3, 5], [3, 4, 2], [4, 5, 3], [5, 6, 4], [6, 7, 1]],maxMoves = 25,n = 8) == 35: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 0, 1], [0, 4, 1], [4, 5, 1], [5, 6, 1], [6, 0, 1]],maxMoves = 3,n = 7) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 0, 1], [0, 4, 1], [4, 5, 1], [5, 6, 1], [6, 0, 1]],maxMoves = 3,n = 7) == 13: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [0, 2, 5], [0, 3, 5], [1, 2, 5], [1, 3, 5], [2, 3, 5]],maxMoves = 10,n = 4) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [0, 2, 5], [0, 3, 5], [1, 2, 5], [1, 3, 5], [2, 3, 5]],maxMoves = 10,n = 4) == 34: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9], [9, 10, 10]],maxMoves = 55,n = 11) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9], [9, 10, 10]],maxMoves = 55,n = 11) == 56: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [0, 2, 5], [1, 3, 3], [2, 3, 7], [3, 4, 2]],maxMoves = 20,n = 5) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [0, 2, 5], [1, 3, 3], [2, 3, 7], [3, 4, 2]],maxMoves = 20,n = 5) == 32: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 5], [0, 2, 5], [1, 2, 5], [1, 3, 5], [2, 3, 5], [2, 4, 5], [3, 4, 5], [3, 5, 5], [4, 5, 5]],maxMoves = 10,n = 6) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 5], [0, 2, 5], [1, 2, 5], [1, 3, 5], [2, 3, 5], [2, 4, 5], [3, 4, 5], [3, 5, 5], [4, 5, 5]],maxMoves = 10,n = 6) == 30: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 4, 10], [4, 5, 10], [5, 6, 10], [6, 7, 10], [7, 8, 10], [8, 9, 10], [9, 0, 10]],maxMoves = 50,n = 10) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 4, 10], [4, 5, 10], [5, 6, 10], [6, 7, 10], [7, 8, 10], [8, 9, 10], [9, 0, 10]],maxMoves = 50,n = 10) == 101: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1000], [1, 2, 1000], [2, 3, 1000], [3, 4, 1000], [4, 0, 1000]],maxMoves = 2000,n = 5) == 4001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1000], [1, 2, 1000], [2, 3, 1000], [3, 4, 1000], [4, 0, 1000]],maxMoves = 2000,n = 5) == 4001: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1000], [0, 2, 1000], [1, 2, 1000], [1, 3, 1000], [2, 3, 1000], [2, 4, 1000], [3, 4, 1000], [3, 5, 1000], [4, 5, 1000]],maxMoves = 3000,n = 6) == 9001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1000], [0, 2, 1000], [1, 2, 1000], [1, 3, 1000], [2, 3, 1000], [2, 4, 1000], [3, 4, 1000], [3, 5, 1000], [4, 5, 1000]],maxMoves = 3000,n = 6) == 9001: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 3], [0, 2, 2], [0, 3, 1], [1, 4, 2], [2, 5, 3], [3, 6, 4], [4, 7, 1], [5, 8, 2], [6, 9, 3]],maxMoves = 20,n = 10) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 3], [0, 2, 2], [0, 3, 1], [1, 4, 2], [2, 5, 3], [3, 6, 4], [4, 7, 1], [5, 8, 2], [6, 9, 3]],maxMoves = 20,n = 10) == 31: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 6, 0], [6, 7, 0], [7, 8, 0], [8, 9, 0], [9, 10, 0], [10, 0, 0]],maxMoves = 5,n = 11) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 6, 0], [6, 7, 0], [7, 8, 0], [8, 9, 0], [9, 10, 0], [10, 0, 0]],maxMoves = 5,n = 11) == 11: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 2], [0, 2, 2], [0, 3, 2], [1, 2, 2], [1, 3, 2], [2, 3, 2], [0, 4, 2], [1, 4, 2], [2, 4, 2], [3, 4, 2]],maxMoves = 3,n = 5) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 2], [0, 2, 2], [0, 3, 2], [1, 2, 2], [1, 3, 2], [2, 3, 2], [0, 4, 2], [1, 4, 2], [2, 4, 2], [3, 4, 2]],maxMoves = 3,n = 5) == 13: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [0, 2, 1], [1, 2, 2], [1, 3, 5], [2, 3, 3], [3, 4, 7]],maxMoves = 20,n = 5) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [0, 2, 1], [1, 2, 2], [1, 3, 5], [2, 3, 3], [3, 4, 7]],maxMoves = 20,n = 5) == 33: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 6, 0], [6, 7, 0], [7, 8, 0], [8, 9, 0], [9, 10, 0]],maxMoves = 5,n = 11) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 6, 0], [6, 7, 0], [7, 8, 0], [8, 9, 0], [9, 10, 0]],maxMoves = 5,n = 11) == 6: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1]],maxMoves = 5,n = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1]],maxMoves = 5,n = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1000], [0, 2, 1000], [1, 3, 1000], [1, 4, 1000], [2, 5, 1000], [2, 6, 1000], [3, 7, 1000], [4, 8, 1000], [5, 9, 1000], [6, 10, 1000], [7, 11, 1000], [8, 12, 1000], [9, 13, 1000], [10, 14, 1000], [11, 15, 1000], [12, 16, 1000], [13, 17, 1000], [14, 18, 1000], [15, 19, 1000]],maxMoves = 10000,n = 20) == 19020
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1000], [0, 2, 1000], [1, 3, 1000], [1, 4, 1000], [2, 5, 1000], [2, 6, 1000], [3, 7, 1000], [4, 8, 1000], [5, 9, 1000], [6, 10, 1000], [7, 11, 1000], [8, 12, 1000], [9, 13, 1000], [10, 14, 1000], [11, 15, 1000], [12, 16, 1000], [13, 17, 1000], [14, 18, 1000], [15, 19, 1000]],maxMoves = 10000,n = 20) == 19020: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 0, 6]],maxMoves = 20,n = 6) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 0, 6]],maxMoves = 20,n = 6) == 27: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1], [3, 4, 2], [4, 5, 7]],maxMoves = 20,n = 6) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1], [3, 4, 2], [4, 5, 7]],maxMoves = 20,n = 6) == 34: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 10], [0, 2, 5], [1, 2, 5], [1, 3, 3], [2, 3, 2], [2, 4, 4], [3, 4, 5]],maxMoves = 15,n = 5) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 10], [0, 2, 5], [1, 2, 5], [1, 3, 3], [2, 3, 2], [2, 4, 4], [3, 4, 5]],maxMoves = 15,n = 5) == 39: {e}')
    
    total += 1
    try:
        result = candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 0, 1]],maxMoves = 8,n = 9) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 0, 1]],maxMoves = 8,n = 9) == 17: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(edges = [[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]],maxMoves = 10,n = 4) == 23
    assert candidate(edges = [[0, 1, 0], [1, 2, 0]],maxMoves = 3,n = 3) == 3
    assert candidate(edges = [[0, 1, 5]],maxMoves = 5,n = 2) == 6
    assert candidate(edges = [[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]],maxMoves = 17,n = 5) == 1
    assert candidate(edges = [[0, 1, 5]],maxMoves = 10,n = 2) == 7
    assert candidate(edges = [[0, 1, 0], [1, 2, 0]],maxMoves = 1,n = 3) == 2
    assert candidate(edges = [[0, 1, 3], [0, 2, 2], [1, 2, 2]],maxMoves = 10,n = 3) == 10
    assert candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0]],maxMoves = 3,n = 4) == 4
    assert candidate(edges = [[0, 1, 0], [0, 2, 0], [1, 2, 0]],maxMoves = 1,n = 3) == 3
    assert candidate(edges = [],maxMoves = 0,n = 1) == 1
    assert candidate(edges = [[0, 1, 10], [0, 2, 1], [1, 2, 2]],maxMoves = 6,n = 3) == 13
    assert candidate(edges = [],maxMoves = 5,n = 1) == 1
    assert candidate(edges = [],maxMoves = 10,n = 1) == 1
    assert candidate(edges = [[0, 1, 5], [0, 2, 5], [0, 3, 5], [1, 2, 5], [1, 3, 5], [2, 3, 5], [3, 4, 5], [4, 5, 5], [5, 0, 5]],maxMoves = 15,n = 6) == 51
    assert candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 0, 1], [0, 5, 1], [5, 6, 1], [6, 7, 1], [7, 0, 1], [0, 8, 1], [8, 9, 1], [9, 0, 1]],maxMoves = 20,n = 10) == 22
    assert candidate(edges = [[0, 1, 10], [0, 2, 10], [0, 3, 10], [0, 4, 10]],maxMoves = 15,n = 5) == 45
    assert candidate(edges = [[0, 1, 100], [0, 2, 200], [1, 3, 300], [2, 4, 400], [3, 5, 500], [4, 6, 600], [5, 7, 700], [6, 8, 800], [7, 9, 900]],maxMoves = 1500,n = 10) == 3001
    assert candidate(edges = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [3, 4, 100], [4, 5, 100], [5, 0, 100]],maxMoves = 50,n = 6) == 101
    assert candidate(edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [1, 4, 1], [1, 5, 1], [2, 6, 1], [2, 7, 1], [3, 8, 1], [3, 9, 1]],maxMoves = 5,n = 10) == 19
    assert candidate(edges = [[0, 1, 10], [0, 2, 10], [0, 3, 10], [1, 2, 10], [1, 3, 10], [2, 3, 10]],maxMoves = 20,n = 4) == 64
    assert candidate(edges = [[0, 1, 3], [0, 2, 2], [1, 2, 1]],maxMoves = 5,n = 3) == 9
    assert candidate(edges = [[0, 1, 2], [0, 3, 4], [1, 2, 1], [2, 3, 2], [3, 4, 3]],maxMoves = 10,n = 5) == 17
    assert candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1]],maxMoves = 9,n = 10) == 10
    assert candidate(edges = [[0, 1, 3], [1, 2, 2], [2, 3, 1], [0, 3, 4]],maxMoves = 7,n = 4) == 14
    assert candidate(edges = [[0, 1, 100], [0, 2, 100], [1, 2, 100], [1, 3, 100], [2, 3, 100], [3, 4, 100], [4, 5, 100], [5, 6, 100], [6, 7, 100], [7, 8, 100], [8, 9, 100]],maxMoves = 300,n = 10) == 602
    assert candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 6, 0], [6, 0, 0]],maxMoves = 6,n = 7) == 7
    assert candidate(edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [1, 2, 1], [1, 3, 1], [2, 3, 1]],maxMoves = 1,n = 4) == 4
    assert candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 6, 0], [6, 7, 0], [7, 8, 0], [8, 9, 0]],maxMoves = 5,n = 10) == 6
    assert candidate(edges = [[0, 1, 1], [0, 2, 2], [1, 2, 3], [1, 3, 4], [2, 3, 5], [2, 4, 6], [3, 4, 7], [3, 5, 8], [4, 5, 9]],maxMoves = 20,n = 6) == 51
    assert candidate(edges = [[0, 1, 3], [1, 2, 2], [0, 2, 4]],maxMoves = 5,n = 3) == 11
    assert candidate(edges = [[0, 1, 3], [1, 2, 3], [2, 3, 3], [3, 0, 3], [0, 4, 3], [4, 5, 3], [5, 6, 3], [6, 0, 3], [1, 7, 3], [7, 8, 3], [8, 1, 3], [2, 9, 3], [9, 10, 3], [10, 2, 3]],maxMoves = 10,n = 11) == 46
    assert candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 0, 6]],maxMoves = 12,n = 6) == 25
    assert candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0]],maxMoves = 5,n = 6) == 6
    assert candidate(edges = [[0, 1, 5], [0, 2, 5], [1, 2, 5], [1, 3, 5], [2, 3, 5]],maxMoves = 15,n = 4) == 29
    assert candidate(edges = [[0, 1, 1], [0, 2, 2], [1, 2, 3], [0, 3, 4], [1, 3, 5], [2, 3, 6], [0, 4, 7], [1, 4, 8], [2, 4, 9], [3, 4, 10]],maxMoves = 15,n = 5) == 60
    assert candidate(edges = [[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1], [3, 4, 5], [2, 5, 3]],maxMoves = 15,n = 6) == 33
    assert candidate(edges = [[0, 1, 3], [0, 2, 4], [1, 2, 5]],maxMoves = 7,n = 3) == 15
    assert candidate(edges = [[0, 1, 5], [1, 2, 3], [2, 3, 2], [3, 0, 4], [0, 4, 1]],maxMoves = 9,n = 5) == 20
    assert candidate(edges = [[0, 1, 5], [0, 2, 5], [0, 3, 5], [0, 4, 5], [1, 2, 5], [1, 3, 5], [1, 4, 5], [2, 3, 5], [2, 4, 5], [3, 4, 5]],maxMoves = 15,n = 5) == 55
    assert candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 0, 4], [0, 2, 5], [1, 3, 6]],maxMoves = 10,n = 4) == 25
    assert candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 0, 0]],maxMoves = 1,n = 5) == 3
    assert candidate(edges = [[0, 1, 10], [0, 2, 5], [2, 3, 3], [1, 4, 4]],maxMoves = 15,n = 5) == 26
    assert candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 6, 0], [6, 7, 0], [7, 8, 0], [8, 9, 0], [9, 0, 0]],maxMoves = 5,n = 10) == 10
    assert candidate(edges = [[0, 1, 2], [0, 2, 3], [1, 2, 1], [1, 3, 4], [2, 4, 2]],maxMoves = 8,n = 5) == 17
    assert candidate(edges = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 4, 10], [4, 0, 10], [0, 5, 10], [5, 6, 10], [6, 7, 10], [7, 0, 10], [0, 8, 10], [8, 9, 10], [9, 0, 10]],maxMoves = 30,n = 10) == 130
    assert candidate(edges = [[0, 1, 10], [0, 2, 5], [1, 2, 10], [1, 3, 7], [2, 4, 3], [3, 4, 8]],maxMoves = 20,n = 5) == 48
    assert candidate(edges = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 0, 6], [0, 5, 7], [5, 6, 8], [6, 7, 9], [7, 8, 10], [8, 5, 11]],maxMoves = 30,n = 9) == 74
    assert candidate(edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [0, 5, 1], [0, 6, 1], [0, 7, 1], [0, 8, 1], [0, 9, 1], [0, 10, 1]],maxMoves = 1,n = 11) == 11
    assert candidate(edges = [[0, 1, 5], [1, 2, 5], [2, 3, 5], [3, 4, 5], [4, 5, 5], [5, 0, 5]],maxMoves = 15,n = 6) == 31
    assert candidate(edges = [[0, 1, 1000], [1, 2, 2000], [2, 3, 3000], [3, 4, 4000]],maxMoves = 10000,n = 5) == 10001
    assert candidate(edges = [[0, 1, 2], [0, 2, 3], [1, 3, 4], [2, 4, 5], [3, 5, 6], [4, 6, 7]],maxMoves = 15,n = 7) == 31
    assert candidate(edges = [[0, 1, 2], [1, 2, 2], [2, 3, 2], [3, 4, 2], [4, 0, 2], [0, 5, 2], [5, 6, 2], [6, 7, 2], [7, 0, 2]],maxMoves = 10,n = 8) == 26
    assert candidate(edges = [[0, 1, 3], [0, 2, 3], [1, 2, 3], [1, 3, 3], [2, 3, 3], [0, 4, 3], [1, 4, 3], [2, 4, 3], [3, 4, 3]],maxMoves = 5,n = 5) == 22
    assert candidate(edges = [[0, 1, 10], [0, 2, 20], [1, 3, 30], [2, 4, 40], [3, 4, 50]],maxMoves = 35,n = 5) == 71
    assert candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6]],maxMoves = 15,n = 7) == 16
    assert candidate(edges = [[0, 1, 2], [0, 2, 3], [1, 3, 4], [1, 4, 5], [2, 5, 6], [2, 6, 7], [3, 7, 8], [3, 8, 9], [4, 8, 10], [5, 9, 11], [6, 9, 12]],maxMoves = 30,n = 10) == 87
    assert candidate(edges = [[0, 1, 100], [1, 2, 100], [2, 3, 100], [3, 4, 100], [4, 0, 100]],maxMoves = 250,n = 5) == 501
    assert candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 0, 1], [1, 3, 1], [2, 4, 1]],maxMoves = 5,n = 5) == 12
    assert candidate(edges = [[0, 1, 100], [0, 2, 50], [1, 3, 25], [1, 4, 75], [2, 5, 20], [2, 6, 40], [3, 7, 30], [4, 8, 60], [5, 9, 10], [6, 10, 15], [7, 11, 20], [8, 12, 25], [9, 13, 30], [10, 14, 35], [11, 15, 40], [12, 16, 45], [13, 17, 50], [14, 18, 55], [15, 19, 60]],maxMoves = 300,n = 20) == 795
    assert candidate(edges = [[0, 1, 5], [1, 2, 3], [2, 3, 4], [3, 4, 2], [4, 0, 6]],maxMoves = 15,n = 5) == 25
    assert candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9]],maxMoves = 25,n = 10) == 26
    assert candidate(edges = [[0, 1, 10], [0, 2, 5], [1, 2, 3], [1, 3, 4], [2, 3, 2]],maxMoves = 15,n = 4) == 28
    assert candidate(edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [1, 2, 4], [2, 3, 5]],maxMoves = 10,n = 4) == 19
    assert candidate(edges = [[0, 1, 5], [1, 2, 5], [2, 3, 5], [3, 4, 5], [4, 0, 5], [0, 5, 5], [5, 6, 5], [6, 7, 5], [7, 0, 5]],maxMoves = 15,n = 8) == 53
    assert candidate(edges = [[0, 1, 0], [0, 2, 0], [1, 2, 0], [1, 3, 0], [2, 3, 0]],maxMoves = 5,n = 4) == 4
    assert candidate(edges = [[0, 1, 1], [0, 2, 2], [1, 2, 1], [1, 3, 2], [2, 3, 1], [2, 4, 2], [3, 4, 1], [3, 5, 2], [4, 5, 1]],maxMoves = 5,n = 6) == 13
    assert candidate(edges = [[0, 1, 100], [0, 2, 50], [1, 2, 50], [1, 3, 30], [2, 3, 20], [2, 4, 40], [3, 4, 50]],maxMoves = 200,n = 5) == 345
    assert candidate(edges = [[0, 1, 3], [1, 2, 2], [2, 3, 1], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8]],maxMoves = 30,n = 9) == 31
    assert candidate(edges = [[0, 1, 5], [1, 2, 5], [2, 3, 5], [3, 0, 5], [0, 4, 5], [1, 4, 5], [2, 4, 5], [3, 4, 5]],maxMoves = 10,n = 5) == 41
    assert candidate(edges = [[0, 1, 5], [0, 2, 5], [0, 3, 5], [0, 4, 5], [0, 5, 5], [0, 6, 5], [0, 7, 5], [0, 8, 5], [0, 9, 5], [0, 10, 5]],maxMoves = 20,n = 11) == 61
    assert candidate(edges = [[0, 1, 10], [0, 2, 1], [1, 2, 2], [2, 3, 5], [3, 4, 3]],maxMoves = 12,n = 5) == 26
    assert candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 0, 0]],maxMoves = 3,n = 5) == 5
    assert candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 0, 0]],maxMoves = 0,n = 5) == 1
    assert candidate(edges = [[0, 1, 2], [0, 2, 2], [0, 3, 2], [0, 4, 2], [1, 5, 2], [2, 6, 2], [3, 7, 2], [4, 8, 2], [5, 6, 2], [6, 7, 2], [7, 8, 2]],maxMoves = 5,n = 9) == 21
    assert candidate(edges = [[0, 1, 20], [0, 2, 15], [1, 2, 10], [1, 3, 25], [2, 4, 30], [3, 4, 5]],maxMoves = 50,n = 5) == 110
    assert candidate(edges = [[0, 1, 4], [0, 2, 4], [1, 2, 5], [1, 3, 2], [2, 3, 3]],maxMoves = 10,n = 4) == 22
    assert candidate(edges = [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 0, 7]],maxMoves = 25,n = 6) == 33
    assert candidate(edges = [[0, 1, 1], [2, 3, 1], [4, 5, 1]],maxMoves = 3,n = 6) == 3
    assert candidate(edges = [[0, 1, 1], [0, 2, 2], [0, 3, 3], [0, 4, 4], [0, 5, 5], [0, 6, 6], [0, 7, 7], [0, 8, 8], [0, 9, 9]],maxMoves = 15,n = 10) == 55
    assert candidate(edges = [[0, 1, 100], [1, 2, 200], [2, 3, 300], [3, 0, 400]],maxMoves = 800,n = 4) == 1004
    assert candidate(edges = [[0, 1, 3], [1, 2, 3], [2, 3, 3], [3, 0, 3]],maxMoves = 6,n = 4) == 13
    assert candidate(edges = [[0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [0, 5, 1], [1, 2, 1], [1, 3, 1], [1, 4, 1], [1, 5, 1]],maxMoves = 5,n = 6) == 15
    assert candidate(edges = [[0, 1, 0], [1, 2, 3], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 0, 0]],maxMoves = 10,n = 6) == 9
    assert candidate(edges = [[0, 1, 2], [0, 2, 4], [0, 3, 3], [1, 2, 1], [1, 3, 2], [2, 3, 5], [3, 4, 2], [4, 5, 3], [5, 6, 4], [6, 7, 1]],maxMoves = 25,n = 8) == 35
    assert candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 0, 1], [0, 4, 1], [4, 5, 1], [5, 6, 1], [6, 0, 1]],maxMoves = 3,n = 7) == 13
    assert candidate(edges = [[0, 1, 5], [0, 2, 5], [0, 3, 5], [1, 2, 5], [1, 3, 5], [2, 3, 5]],maxMoves = 10,n = 4) == 34
    assert candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 6, 6], [6, 7, 7], [7, 8, 8], [8, 9, 9], [9, 10, 10]],maxMoves = 55,n = 11) == 56
    assert candidate(edges = [[0, 1, 10], [0, 2, 5], [1, 3, 3], [2, 3, 7], [3, 4, 2]],maxMoves = 20,n = 5) == 32
    assert candidate(edges = [[0, 1, 5], [0, 2, 5], [1, 2, 5], [1, 3, 5], [2, 3, 5], [2, 4, 5], [3, 4, 5], [3, 5, 5], [4, 5, 5]],maxMoves = 10,n = 6) == 30
    assert candidate(edges = [[0, 1, 10], [1, 2, 10], [2, 3, 10], [3, 4, 10], [4, 5, 10], [5, 6, 10], [6, 7, 10], [7, 8, 10], [8, 9, 10], [9, 0, 10]],maxMoves = 50,n = 10) == 101
    assert candidate(edges = [[0, 1, 1000], [1, 2, 1000], [2, 3, 1000], [3, 4, 1000], [4, 0, 1000]],maxMoves = 2000,n = 5) == 4001
    assert candidate(edges = [[0, 1, 1000], [0, 2, 1000], [1, 2, 1000], [1, 3, 1000], [2, 3, 1000], [2, 4, 1000], [3, 4, 1000], [3, 5, 1000], [4, 5, 1000]],maxMoves = 3000,n = 6) == 9001
    assert candidate(edges = [[0, 1, 3], [0, 2, 2], [0, 3, 1], [1, 4, 2], [2, 5, 3], [3, 6, 4], [4, 7, 1], [5, 8, 2], [6, 9, 3]],maxMoves = 20,n = 10) == 31
    assert candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 6, 0], [6, 7, 0], [7, 8, 0], [8, 9, 0], [9, 10, 0], [10, 0, 0]],maxMoves = 5,n = 11) == 11
    assert candidate(edges = [[0, 1, 2], [0, 2, 2], [0, 3, 2], [1, 2, 2], [1, 3, 2], [2, 3, 2], [0, 4, 2], [1, 4, 2], [2, 4, 2], [3, 4, 2]],maxMoves = 3,n = 5) == 13
    assert candidate(edges = [[0, 1, 10], [0, 2, 1], [1, 2, 2], [1, 3, 5], [2, 3, 3], [3, 4, 7]],maxMoves = 20,n = 5) == 33
    assert candidate(edges = [[0, 1, 0], [1, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0], [5, 6, 0], [6, 7, 0], [7, 8, 0], [8, 9, 0], [9, 10, 0]],maxMoves = 5,n = 11) == 6
    assert candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 9, 1]],maxMoves = 5,n = 10) == 6
    assert candidate(edges = [[0, 1, 1000], [0, 2, 1000], [1, 3, 1000], [1, 4, 1000], [2, 5, 1000], [2, 6, 1000], [3, 7, 1000], [4, 8, 1000], [5, 9, 1000], [6, 10, 1000], [7, 11, 1000], [8, 12, 1000], [9, 13, 1000], [10, 14, 1000], [11, 15, 1000], [12, 16, 1000], [13, 17, 1000], [14, 18, 1000], [15, 19, 1000]],maxMoves = 10000,n = 20) == 19020
    assert candidate(edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [4, 5, 5], [5, 0, 6]],maxMoves = 20,n = 6) == 27
    assert candidate(edges = [[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1], [3, 4, 2], [4, 5, 7]],maxMoves = 20,n = 6) == 34
    assert candidate(edges = [[0, 1, 10], [0, 2, 5], [1, 2, 5], [1, 3, 3], [2, 3, 2], [2, 4, 4], [3, 4, 5]],maxMoves = 15,n = 5) == 39
    assert candidate(edges = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 0, 1]],maxMoves = 8,n = 9) == 17


