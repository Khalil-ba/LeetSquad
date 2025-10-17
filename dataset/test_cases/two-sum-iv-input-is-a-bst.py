def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),k = 28) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),k = 28) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),k = 9) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),k = 9) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 180]),k = 150) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 180]),k = 150) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 0, 3, -4, 1]),k = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 0, 3, -4, 1]),k = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 190]),k = 500) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 190]),k = 500) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3]),k = 4) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3]),k = 4) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 10, 3, 7, 9, 12]),k = 14) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 10, 3, 7, 9, 12]),k = 14) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 2]),k = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 2]),k = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 9, 1, 5, None, 11, 0, 2, 4, 6, 8, 10, 12]),k = 19) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 9, 1, 5, None, 11, 0, 2, 4, 6, 8, 10, 12]),k = 19) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, -5, 0, -7, -8, 5, 7, 6, 8, None, None, 3, 1]),k = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, -5, 0, -7, -8, 5, 7, 6, 8, None, None, 3, 1]),k = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 0, 3, -4, 1]),k = -1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 0, 3, -4, 1]),k = -1) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 30, 45, 57, 70, 80, 90]),k = 500) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 30, 45, 57, 70, 80, 90]),k = 500) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, None, None, None, None, None, 8]),k = 14) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, None, None, None, None, None, 8]),k = 14) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, None, None, None, 20]),k = 17) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, None, None, None, 20]),k = 17) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6]),k = 18) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6]),k = 18) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),k = 11) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),k = 11) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 0, 3, -4, 1]),k = 0) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 0, 3, -4, 1]),k = 0) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),k = 8) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),k = 8) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 9, 20, 7, 11, 17, 22, 3, 8, 10, 12, 16, 18, 21, 23]),k = 25) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 9, 20, 7, 11, 17, 22, 3, 8, 10, 12, 16, 18, 21, 23]),k = 25) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 5, 10, 3, 6, 9, 11]),k = 21) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 5, 10, 3, 6, 9, 11]),k = 21) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1]),k = 3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1]),k = 3) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 190]),k = 200) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 190]),k = 200) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1]),k = 8) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1]),k = 8) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -1, 2, None, -2, None, 3]),k = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -1, 2, None, -2, None, 3]),k = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 8, None, 4, None, None, 3, None, 2, None, None, None, 0, None, -1]),k = 8) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 8, None, 4, None, None, 3, None, 2, None, None, None, 0, None, -1]),k = 8) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 2, -1, None, None, None, -2, None]),k = -1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 2, -1, None, None, None, -2, None]),k = -1) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10000, 5000, 15000, 2500, 7500, 12500, 17500]),k = 20000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10000, 5000, 15000, 2500, 7500, 12500, 17500]),k = 20000) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 2]),k = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 2]),k = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, -5, 0, -7, -8, 5, 7, 6, 8, None, None, 3, 1]),k = -5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, -5, 0, -7, -8, 5, 7, 6, 8, None, None, 3, 1]),k = -5) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]),k = 29) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]),k = 29) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 2, None, -1]),k = 1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 2, None, -1]),k = 1) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 2, None, None, 2, None]),k = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 2, None, None, 2, None]),k = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),k = 27) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),k = 27) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35]),k = 30) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35]),k = 30) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 30, 45, 57, 70, 80, 90]),k = 45) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 30, 45, 57, 70, 80, 90]),k = 45) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, -5, 0, 1, None, -6, None, -8]),k = -16) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, -5, 0, 1, None, -6, None, -8]),k = -16) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 0, 3, -4, 1]),k = 6) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 0, 3, -4, 1]),k = 6) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 2, -1, None, None, None]),k = -1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 2, -1, None, None, None]),k = -1) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190]),k = 125) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190]),k = 125) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 1, None, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]),k = 18) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 1, None, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]),k = 18) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 180]),k = 200) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 180]),k = 200) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, None, None, None, None, None, 8]),k = 15) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, None, None, None, None, None, 8]),k = 15) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10000, 5000, 15000, 2500, 7500, 12500, 17500]),k = 25000) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10000, 5000, 15000, 2500, 7500, 12500, 17500]),k = 25000) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3]),k = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3]),k = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, -20, -5, -15, None, -30]),k = -30) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, -20, -5, -15, None, -30]),k = -30) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 15, 30, 10, 17, 25, 40, 5, 12, None, None, None, None, 35, 45]),k = 52) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 15, 30, 10, 17, 25, 40, 5, 12, None, None, None, None, 35, 45]),k = 52) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 15, 25, 10, 18, 22, 30, 5, 13, None, None, 17, 19, None, None, 3, 8]),k = 25) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 15, 25, 10, 18, 22, 30, 5, 13, None, None, 17, 19, None, None, 3, 8]),k = 25) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 8, 12, 17, 25, 6, 9, 11, 13, 16, 18, 22, 28]),k = 33) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 8, 12, 17, 25, 6, 9, 11, 13, 16, 18, 22, 28]),k = 33) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 90, 110, 140, 160, 190]),k = 200) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 90, 110, 140, 160, 190]),k = 200) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),k = 25) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),k = 25) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 30, 45, 57, 70, 80, 90]),k = 110) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 30, 45, 57, 70, 80, 90]),k = 110) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35]),k = 60) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35]),k = 60) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-10, -5, 0, -7, -8, 5, 7, 6, 8, None, None, 3, 1]),k = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-10, -5, 0, -7, -8, 5, 7, 6, 8, None, None, 3, 1]),k = 0) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([-1, -2, -3, -4, -5]),k = -8) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([-1, -2, -3, -4, -5]),k = -8) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1, None, None, None, None, 8]),k = 15) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1, None, None, None, None, 8]),k = 15) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]),k = 27) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]),k = 27) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 30, 45, 57, 70, 80, 90]),k = 150) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 30, 45, 57, 70, 80, 90]),k = 150) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6]),k = 26) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6]),k = 26) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, None, 3, 5, 7, 9, 11, 13, 15]),k = 30) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, None, 3, 5, 7, 9, 11, 13, 15]),k = 30) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 8, 12, 7, 9, 11, 13]),k = 21) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 8, 12, 7, 9, 11, 13]),k = 21) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 23, 27, 32, 37]),k = 45) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 23, 27, 32, 37]),k = 45) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, None, None, 9, 20]),k = 22) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, None, None, 9, 20]),k = 22) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, None, 5, 7, 9, 11, 13, 15]),k = 26) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, None, 5, 7, 9, 11, 13, 15]),k = 26) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 4, None, 2]),k = 6) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 4, None, 2]),k = 6) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 0, 3, -4, 1]),k = -3) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 0, 3, -4, 1]),k = -3) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 0, 3, -4, 1]),k = 2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 0, 3, -4, 1]),k = 2) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 4, None, 2]),k = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 4, None, 2]),k = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 0, 2, None, -1]),k = -1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 0, 2, None, -1]),k = -1) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190]),k = 200) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190]),k = 200) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 17) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 17) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 4, 6, 3, None, 7]),k = 9) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 4, 6, 3, None, 7]),k = 9) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180]),k = 300) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180]),k = 300) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, None, None, None, 22]),k = 33) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, None, None, None, 22]),k = 33) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180]),k = 200) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180]),k = 200) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 30) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 30) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 25) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 25) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 0, 3, -4, 1]),k = -2) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 0, 3, -4, 1]),k = -2) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([45, 30, 60, 20, 35, 50, 70, 10, 25, 32, 37, 48, 55, 65, 75, 5, 15, 22, 28, 33, 36, 42, 47, 52, 58, 62, 68, 72, 78, 80]),k = 85) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([45, 30, 60, 20, 35, 50, 70, 10, 25, 32, 37, 48, 55, 65, 75, 5, 15, 22, 28, 33, 36, 42, 47, 52, 58, 62, 68, 72, 78, 80]),k = 85) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([7, 3, 15, 1, 5, 9, 20, None, None, None, 6]),k = 11) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([7, 3, 15, 1, 5, 9, 20, None, None, None, 6]),k = 11) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),k = 5) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),k = 5) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 18) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 18) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),k = 15) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),k = 15) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180]),k = 250) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180]),k = 250) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -1, 2, None, -3, None, 4]),k = -1) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -1, 2, None, -3, None, 4]),k = -1) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35]),k = 40) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35]),k = 40) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5]),k = 10) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5]),k = 10) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 2, 4, None, 1]),k = 6) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 2, 4, None, 1]),k = 6) == True: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1]),k = 2) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1]),k = 2) == False: {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([0, -1, 2, -2, None, None, 3, -3, None, None, None]),k = 0) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([0, -1, 2, -2, None, None, 3, -3, None, None, None]),k = 0) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),k = 28) == False
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),k = 9) == True
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 180]),k = 150) == True
    assert candidate(root = tree_node([2, 0, 3, -4, 1]),k = 5) == True
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 190]),k = 500) == False
    assert candidate(root = tree_node([2, 1, 3]),k = 4) == True
    assert candidate(root = tree_node([8, 5, 10, 3, 7, 9, 12]),k = 14) == True
    assert candidate(root = tree_node([1, 0, 2]),k = 3) == True
    assert candidate(root = tree_node([7, 3, 9, 1, 5, None, 11, 0, 2, 4, 6, 8, 10, 12]),k = 19) == True
    assert candidate(root = tree_node([-10, -5, 0, -7, -8, 5, 7, 6, 8, None, None, 3, 1]),k = 10) == True
    assert candidate(root = tree_node([2, 0, 3, -4, 1]),k = -1) == True
    assert candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 30, 45, 57, 70, 80, 90]),k = 500) == False
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, None, None, None, None, None, 8]),k = 14) == True
    assert candidate(root = tree_node([7, 3, 15, None, None, None, 20]),k = 17) == False
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6]),k = 18) == True
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),k = 11) == True
    assert candidate(root = tree_node([2, 0, 3, -4, 1]),k = 0) == False
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),k = 8) == True
    assert candidate(root = tree_node([15, 9, 20, 7, 11, 17, 22, 3, 8, 10, 12, 16, 18, 21, 23]),k = 25) == True
    assert candidate(root = tree_node([8, 5, 10, 3, 6, 9, 11]),k = 21) == True
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1]),k = 3) == True
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 190]),k = 200) == True
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1]),k = 8) == True
    assert candidate(root = tree_node([0, -1, 2, None, -2, None, 3]),k = 0) == True
    assert candidate(root = tree_node([5, 1, 8, None, 4, None, None, 3, None, 2, None, None, None, 0, None, -1]),k = 8) == True
    assert candidate(root = tree_node([1, 0, 2, -1, None, None, None, -2, None]),k = -1) == True
    assert candidate(root = tree_node([10000, 5000, 15000, 2500, 7500, 12500, 17500]),k = 20000) == True
    assert candidate(root = tree_node([1, 0, 2]),k = 1) == True
    assert candidate(root = tree_node([-10, -5, 0, -7, -8, 5, 7, 6, 8, None, None, 3, 1]),k = -5) == True
    assert candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]),k = 29) == True
    assert candidate(root = tree_node([1, 0, 2, None, -1]),k = 1) == True
    assert candidate(root = tree_node([1, 0, 2, None, None, 2, None]),k = 2) == True
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),k = 27) == True
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35]),k = 30) == True
    assert candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 30, 45, 57, 70, 80, 90]),k = 45) == False
    assert candidate(root = tree_node([-10, -5, 0, 1, None, -6, None, -8]),k = -16) == True
    assert candidate(root = tree_node([2, 0, 3, -4, 1]),k = 6) == False
    assert candidate(root = tree_node([1, 0, 2, -1, None, None, None]),k = -1) == True
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190]),k = 125) == True
    assert candidate(root = tree_node([10, 1, None, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]),k = 18) == True
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 90, 110, 140, 160, 180]),k = 200) == True
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, None, None, None, None, None, 8]),k = 15) == True
    assert candidate(root = tree_node([10000, 5000, 15000, 2500, 7500, 12500, 17500]),k = 25000) == True
    assert candidate(root = tree_node([2, 1, 3]),k = 5) == True
    assert candidate(root = tree_node([-10, -20, -5, -15, None, -30]),k = -30) == True
    assert candidate(root = tree_node([20, 15, 30, 10, 17, 25, 40, 5, 12, None, None, None, None, 35, 45]),k = 52) == True
    assert candidate(root = tree_node([20, 15, 25, 10, 18, 22, 30, 5, 13, None, None, 17, 19, None, None, 3, 8]),k = 25) == True
    assert candidate(root = tree_node([15, 10, 20, 8, 12, 17, 25, 6, 9, 11, 13, 16, 18, 22, 28]),k = 33) == True
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 60, 90, 110, 140, 160, 190]),k = 200) == True
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),k = 25) == True
    assert candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 30, 45, 57, 70, 80, 90]),k = 110) == True
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35]),k = 60) == True
    assert candidate(root = tree_node([-10, -5, 0, -7, -8, 5, 7, 6, 8, None, None, 3, 1]),k = 0) == True
    assert candidate(root = tree_node([-1, -2, -3, -4, -5]),k = -8) == True
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7, 1, None, None, None, None, 8]),k = 15) == True
    assert candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]),k = 27) == True
    assert candidate(root = tree_node([50, 25, 75, 12, 37, 63, 87, 6, 18, 30, 45, 57, 70, 80, 90]),k = 150) == True
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6]),k = 26) == False
    assert candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, None, 3, 5, 7, 9, 11, 13, 15]),k = 30) == False
    assert candidate(root = tree_node([10, 8, 12, 7, 9, 11, 13]),k = 21) == True
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 2, 7, 12, 18, 23, 27, 32, 37]),k = 45) == True
    assert candidate(root = tree_node([7, 3, 15, None, None, 9, 20]),k = 22) == True
    assert candidate(root = tree_node([8, 4, 12, 2, 6, 10, 14, 1, None, 5, 7, 9, 11, 13, 15]),k = 26) == True
    assert candidate(root = tree_node([3, 1, 4, None, 2]),k = 6) == True
    assert candidate(root = tree_node([2, 0, 3, -4, 1]),k = -3) == True
    assert candidate(root = tree_node([2, 0, 3, -4, 1]),k = 2) == True
    assert candidate(root = tree_node([3, 1, 4, None, 2]),k = 5) == True
    assert candidate(root = tree_node([1, 0, 2, None, -1]),k = -1) == True
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 190]),k = 200) == True
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 17) == True
    assert candidate(root = tree_node([5, 4, 6, 3, None, 7]),k = 9) == True
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180]),k = 300) == True
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, None, None, None, 22]),k = 33) == True
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180]),k = 200) == True
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 30) == False
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 25) == True
    assert candidate(root = tree_node([2, 0, 3, -4, 1]),k = -2) == True
    assert candidate(root = tree_node([45, 30, 60, 20, 35, 50, 70, 10, 25, 32, 37, 48, 55, 65, 75, 5, 15, 22, 28, 33, 36, 42, 47, 52, 58, 62, 68, 72, 78, 80]),k = 85) == True
    assert candidate(root = tree_node([7, 3, 15, 1, 5, 9, 20, None, None, None, 6]),k = 11) == True
    assert candidate(root = tree_node([5, 3, 6, 2, 4, None, 7]),k = 5) == True
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),k = 18) == True
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18]),k = 15) == True
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80, 110, 140, 160, 180]),k = 250) == True
    assert candidate(root = tree_node([0, -1, 2, None, -3, None, 4]),k = -1) == True
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35]),k = 40) == True
    assert candidate(root = tree_node([5, 5, 5, 5, 5, 5, 5]),k = 10) == True
    assert candidate(root = tree_node([3, 2, 4, None, 1]),k = 6) == True
    assert candidate(root = tree_node([1]),k = 2) == False
    assert candidate(root = tree_node([0, -1, 2, -2, None, None, 3, -3, None, None, None]),k = 0) == True


