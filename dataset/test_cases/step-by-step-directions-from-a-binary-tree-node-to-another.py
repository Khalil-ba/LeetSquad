def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),startValue = 3,destValue = 18) == "UURR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),startValue = 3,destValue = 18) == "UURR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1]),startValue = 2,destValue = 1) == "L"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1]),startValue = 2,destValue = 1) == "L": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 2, 3, None, 6, 4]),startValue = 3,destValue = 6) == "UURL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 2, 3, None, 6, 4]),startValue = 3,destValue = 6) == "UURL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),startValue = 4,destValue = 7) == "UURR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),startValue = 4,destValue = 7) == "UURR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),startValue = 8,destValue = 10) == "UURL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),startValue = 8,destValue = 10) == "UURL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 8,destValue = 15) == "UUURRR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 8,destValue = 15) == "UUURRR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2]),startValue = 2,destValue = 1) == "U"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2]),startValue = 2,destValue = 1) == "U": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 1,destValue = 15) == "RRR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 1,destValue = 15) == "RRR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 8,destValue = 14) == "UUURRL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 8,destValue = 14) == "UUURRL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 4, None, 2]),startValue = 2,destValue = 4) == "UUR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 4, None, 2]),startValue = 2,destValue = 4) == "UUR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 2]),startValue = 2,destValue = 1) == "UL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 2]),startValue = 2,destValue = 1) == "UL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 17, 22, 27, 32, 38, 1, 4, 6, 8, 11, 13, 16, 18, 19, 21, 23, 24, 26, 28, 30, 31, 33, 34, 36, 37, 39, 40]),startValue = 37,destValue = 4) == "U"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 17, 22, 27, 32, 38, 1, 4, 6, 8, 11, 13, 16, 18, 19, 21, 23, 24, 26, 28, 30, 31, 33, 34, 36, 37, 39, 40]),startValue = 37,destValue = 4) == "U": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),startValue = 45,destValue = 50) == "UUUUURLLRL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),startValue = 45,destValue = 50) == "UUUUURLLRL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 2, 3, 8, 6, 4, 9, None, None, 10]),startValue = 9,destValue = 10) == "UURR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 2, 3, 8, 6, 4, 9, None, None, 10]),startValue = 9,destValue = 10) == "UURR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 12,destValue = 14) == "UURL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 12,destValue = 14) == "UURL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),startValue = 16,destValue = 19) == "UURR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),startValue = 16,destValue = 19) == "UURR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 6, 7, 8, 9, None, None, 12, 13, None, None, 16, 17]),startValue = 16,destValue = 17) == "UR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 6, 7, 8, 9, None, None, 12, 13, None, None, 16, 17]),startValue = 16,destValue = 17) == "UR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 2, 3, None, 6, 4, 8, None, None, None, 9]),startValue = 8,destValue = 9) == "UUURRL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 2, 3, None, 6, 4, 8, None, None, None, 9]),startValue = 8,destValue = 9) == "UUURRL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 2, 3, 6, None, 4, 7, 8, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15, 16]),startValue = 7,destValue = 16) == "URRR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 2, 3, 6, None, 4, 7, 8, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15, 16]),startValue = 7,destValue = 16) == "URRR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),startValue = 4,destValue = 17) == "LR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),startValue = 4,destValue = 17) == "LR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 12, 37, 62, 87, 6, 20, None, 40, None, 59, 80, 90]),startValue = 6,destValue = 80) == "UUURRL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 12, 37, 62, 87, 6, 20, None, 40, None, 59, 80, 90]),startValue = 6,destValue = 80) == "UUURRL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, None, 6, None, 11, 13, None, None, None, None, None, None, None]),startValue = 3,destValue = 13) == "UURLR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, None, 6, None, 11, 13, None, None, None, None, None, None, None]),startValue = 3,destValue = 13) == "UURLR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12]),startValue = 7,destValue = 12) == "LLLLL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12]),startValue = 7,destValue = 12) == "LLLLL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),startValue = 21,destValue = 28) == "UUUURRLL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),startValue = 21,destValue = 28) == "UUUURRLL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, None, 3, 4, None, 5, 6, None, None, 7, 8, 9]),startValue = 6,destValue = 9) == "R"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, None, 3, 4, None, 5, 6, None, None, 7, 8, 9]),startValue = 6,destValue = 9) == "R": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 17, 22, 27, 32, 38, 1, 4, 6, 8, 11, 13, 16, 18, 19, 21, 23, 24, 26, 28, 30, 31, 33, 34, 36, 37, 39, 40]),startValue = 4,destValue = 37) == "R"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 17, 22, 27, 32, 38, 1, 4, 6, 8, 11, 13, 16, 18, 19, 21, 23, 24, 26, 28, 30, 31, 33, 34, 36, 37, 39, 40]),startValue = 4,destValue = 37) == "R": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, None, 14, 20, None, None, None, None, None, 13, 16, 19]),startValue = 3,destValue = 20) == "UURRR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, None, 14, 20, None, None, None, None, None, 13, 16, 19]),startValue = 3,destValue = 20) == "UURRR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 1, 2, None, None, None, 4, None, 5, None, None, None, 6, None, None, None, None, None, None, 7]),startValue = 1,destValue = 7) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 1, 2, None, None, None, 4, None, 5, None, None, None, 6, None, None, None, None, None, None, 7]),startValue = 1,destValue = 7) == "": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),startValue = 10,destValue = 19) == "UULRR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),startValue = 10,destValue = 19) == "UULRR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 55, 59, 81, 93, 3, 9, 15, 21, 27, 35, 39, 47, 51, 57, 61, 67, 71, 77, 83, 89, 95, 1, 5, 7, 11, 13, 17, 19, 23, 29, 33, 37, 41, 45, 49, 53, 58, 63, 65, 69, 73, 75, 79, 85, 88, 91, 94, 97, 99]),startValue = 55,destValue = 88) == "UURLLL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 55, 59, 81, 93, 3, 9, 15, 21, 27, 35, 39, 47, 51, 57, 61, 67, 71, 77, 83, 89, 95, 1, 5, 7, 11, 13, 17, 19, 23, 29, 33, 37, 41, 45, 49, 53, 58, 63, 65, 69, 73, 75, 79, 85, 88, 91, 94, 97, 99]),startValue = 55,destValue = 88) == "UURLLL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([200, 100, 300, 50, 150, 250, 350, 25, 75, 125, 175, 225, 275, 325, 375, 10, 40, 60, 90, 130, 160, 180, 210, 240, 260, 290, 310, 340, 360, 390]),startValue = 10,destValue = 390) == "UUUURRRL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([200, 100, 300, 50, 150, 250, 350, 25, 75, 125, 175, 225, 275, 325, 375, 10, 40, 60, 90, 130, 160, 180, 210, 240, 260, 290, 310, 340, 360, 390]),startValue = 10,destValue = 390) == "UUUURRRL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, None, None, None, None, 8, 9, None, None, None, None, 10]),startValue = 10,destValue = 8) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, None, None, None, None, 8, 9, None, None, None, None, 10]),startValue = 10,destValue = 8) == "": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9]),startValue = 6,destValue = 9) == "URR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9]),startValue = 6,destValue = 9) == "URR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, None, None, 7, 8, None, None, 9, 10, 11, 12, 13, 14, None, None, None, None, None, None, None, 15, 16, None, 17, None, None, 18]),startValue = 6,destValue = 18) == "LLLLRL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, None, None, 7, 8, None, None, 9, 10, 11, 12, 13, 14, None, None, None, None, None, None, None, 15, 16, None, 17, None, None, 18]),startValue = 6,destValue = 18) == "LLLLRL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),startValue = 12,destValue = 24) == "L"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),startValue = 12,destValue = 24) == "L": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6]),startValue = 3,destValue = 7) == "UR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6]),startValue = 3,destValue = 7) == "UR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 8,destValue = 15) == "UUURRR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 8,destValue = 15) == "UUURRR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),startValue = 5,destValue = 1) == "UR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),startValue = 5,destValue = 1) == "UR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, None, 25, 35, 48, None, None, None, 18, None, None, None, None, None, None, None, None, 22, None, None, None, None, None, None, None, None, None, None]),startValue = 5,destValue = 22) == "RL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, None, 25, 35, 48, None, None, None, 18, None, None, None, None, None, None, None, None, 22, None, None, None, None, None, None, None, None, None, None]),startValue = 5,destValue = 22) == "RL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, None, 14, 15, None, None, None, None, None, 16, 17, 18, 19, 20]),startValue = 8,destValue = 19) == "UUURLRL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, None, 14, 15, None, None, None, None, None, 16, 17, 18, 19, 20]),startValue = 8,destValue = 19) == "UUURLRL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 14,destValue = 11) == "UUULRR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 14,destValue = 11) == "UUULRR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6]),startValue = 1,destValue = 6) == "UURL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6]),startValue = 1,destValue = 6) == "UURL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),startValue = 16,destValue = 20) == "UUURLL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),startValue = 16,destValue = 20) == "UUURLL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 5,destValue = 11) == "R"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 5,destValue = 11) == "R": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 85, 110, 140, 160, 180]),startValue = 85,destValue = 140) == "UUURLR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 85, 110, 140, 160, 180]),startValue = 85,destValue = 140) == "UUURLR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, 6, None, None, None, None, 7, 8, None, None, None, None, 9, 10]),startValue = 9,destValue = 10) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, 6, None, None, None, None, 7, 8, None, None, None, None, 9, 10]),startValue = 9,destValue = 10) == "": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),startValue = 10,destValue = 45) == "URLR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),startValue = 10,destValue = 45) == "URLR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([15, 10, 20, 8, 12, 18, 25, 6, 9, 11, 13, 16, 19, 22, 28, 5, 7, None, None, None, None, None, None, 14, None, None, None, None, None, 17, None, None, None, None, None, None, 21, None, None, None, None, None, None, None, None, None, None, None, None, 24, None, None, None, None, None, None, 26, None, 27]),startValue = 5,destValue = 27) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([15, 10, 20, 8, 12, 18, 25, 6, 9, 11, 13, 16, 19, 22, 28, 5, 7, None, None, None, None, None, None, 14, None, None, None, None, None, 17, None, None, None, None, None, None, 21, None, None, None, None, None, None, None, None, None, None, None, None, 24, None, None, None, None, None, None, 26, None, 27]),startValue = 5,destValue = 27) == "": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),startValue = 12,destValue = 49) == "LR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),startValue = 12,destValue = 49) == "LR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 65, 85, 115, 135, 165, 185]),startValue = 10,destValue = 185) == "UUURRR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 65, 85, 115, 135, 165, 185]),startValue = 10,destValue = 185) == "UUURRR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 2, 3, 9, None, 6, 4, None, None, None, None, 8]),startValue = 4,destValue = 9) == "UUR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 2, 3, 9, None, 6, 4, None, None, None, None, 8]),startValue = 4,destValue = 9) == "UUR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, 20, 21, 22, None, 24, 25, 26, 27, 28]),startValue = 20,destValue = 27) == "UUURRR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, 20, 21, 22, None, 24, 25, 26, 27, 28]),startValue = 20,destValue = 27) == "UUURRR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),startValue = 19,destValue = 7) == "UUUURR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),startValue = 19,destValue = 7) == "UUUURR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 2, 3, None, 6, 4, 8, 9, None, None, 12, 13, None, None, 16, 17, None, None, None, 18, 19, 20, None, None, None, None, 22, 23, 24, 25, 26, 27, 28, None, None, None, None, None, None, None, None, None, None, None, 30]),startValue = 16,destValue = 28) == "LRL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 2, 3, None, 6, 4, 8, 9, None, None, 12, 13, None, None, 16, 17, None, None, None, 18, 19, 20, None, None, None, None, 22, 23, 24, 25, 26, 27, 28, None, None, None, None, None, None, None, None, None, None, None, 30]),startValue = 16,destValue = 28) == "LRL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 7,destValue = 1) == "UU"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 7,destValue = 1) == "UU": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10]),startValue = 1,destValue = 10) == "RRRRRRRRR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10]),startValue = 1,destValue = 10) == "RRRRRRRRR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 48, 2, 8, 13, 16, 19, 23, 32, 38, 43, 47, 49, 1, 6, 9, 11, 14, 17, 21, 22, 24, 26, 29, 31, 33, 37, 41, 42, 44, 46, 51]),startValue = 42,destValue = 46) == "UURL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 48, 2, 8, 13, 16, 19, 23, 32, 38, 43, 47, 49, 1, 6, 9, 11, 14, 17, 21, 22, 24, 26, 29, 31, 33, 37, 41, 42, 44, 46, 51]),startValue = 42,destValue = 46) == "UURL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, None, 8, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15]),startValue = 11,destValue = 15) == "R"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, None, 8, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15]),startValue = 11,destValue = 15) == "R": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, 6, 4, None, None, None, 5]),startValue = 5,destValue = 1) == "UUU"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, 6, 4, None, None, None, 5]),startValue = 5,destValue = 1) == "UUU": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]),startValue = 10,destValue = 60) == "UUURRRLL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]),startValue = 10,destValue = 60) == "UUURRRLL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6]),startValue = 3,destValue = 6) == "URL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6]),startValue = 3,destValue = 6) == "URL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, None, 17, 16, 25, 0, 2, None, None, None, None, None, None, 9]),startValue = 3,destValue = 25) == "UURRR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, None, 17, 16, 25, 0, 2, None, None, None, None, None, None, 9]),startValue = 3,destValue = 25) == "UURRR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),startValue = 16,destValue = 30) == "UUUURLLLL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),startValue = 16,destValue = 30) == "UUUURLLLL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 12, 37, 62, 87, 112, 137, 162, 187, 6, 18, 31, 43, 55, 59, 81, 93, 107, 118, 127, 133, 147, 153, 167, 173, 183, 193, 3, 9, 15, 21, 27, 33, 39, 45, 49, 53, 58, 63, 65, 69, 73, 75, 79, 85, 88, 91, 94, 97, 99, 103, 109, 115, 121, 123, 129, 131, 139, 141, 149, 151, 157, 159, 165, 169, 171, 179, 181, 189, 191, 199]),startValue = 69,destValue = 171) == "UUUULRLLL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 12, 37, 62, 87, 112, 137, 162, 187, 6, 18, 31, 43, 55, 59, 81, 93, 107, 118, 127, 133, 147, 153, 167, 173, 183, 193, 3, 9, 15, 21, 27, 33, 39, 45, 49, 53, 58, 63, 65, 69, 73, 75, 79, 85, 88, 91, 94, 97, 99, 103, 109, 115, 121, 123, 129, 131, 139, 141, 149, 151, 157, 159, 165, 169, 171, 179, 181, 189, 191, 199]),startValue = 69,destValue = 171) == "UUUULRLLL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 2, 3, 8, None, 6, 4, None, None, 9, 10, 11]),startValue = 4,destValue = 11) == "UUURRR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 2, 3, 8, None, 6, 4, None, None, 9, 10, 11]),startValue = 4,destValue = 11) == "UUURRR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 2, 3, 6, 7, 4, None, None, None, None, None, None, 8, 9, 10, 11, None, None, 12, 13]),startValue = 8,destValue = 13) == "LR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 2, 3, 6, 7, 4, None, None, None, None, None, None, 8, 9, 10, 11, None, None, 12, 13]),startValue = 8,destValue = 13) == "LR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]),startValue = 19,destValue = 38) == "L"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]),startValue = 19,destValue = 38) == "L": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15]),startValue = 2,destValue = 14) == "URLRR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15]),startValue = 2,destValue = 14) == "URLRR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),startValue = 5,destValue = 0) == "URL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),startValue = 5,destValue = 0) == "URL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),startValue = 10,destValue = 40) == "LL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),startValue = 10,destValue = 40) == "LL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 2, 3, None, 6, 4, 8, 9, None, None, 12, 13, None, None, 16, 17, None, None, None, 18, 19, 20, None, None, None, None, 22, 23, 24, 25, 26, 27, 28, None, None, None, None, None, None, None, None, None, None, None, 30, None, None, None, 34, 35, 36, 37, 38, 39, 40, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 45]),startValue = 34,destValue = 40) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 2, 3, None, 6, 4, 8, 9, None, None, 12, 13, None, None, 16, 17, None, None, None, 18, 19, 20, None, None, None, None, 22, 23, 24, 25, 26, 27, 28, None, None, None, None, None, None, None, None, None, None, None, 30, None, None, None, 34, 35, 36, 37, 38, 39, 40, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 45]),startValue = 34,destValue = 40) == "": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([50, 25, 75, 10, 30, 60, 80, 5, 15, 27, 33, 55, 65, 77, 85]),startValue = 5,destValue = 65) == "UUURLR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([50, 25, 75, 10, 30, 60, 80, 5, 15, 27, 33, 55, 65, 77, 85]),startValue = 5,destValue = 65) == "UUURLR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 2, 8, 1, 3, 6, 9, None, None, 4, 7, None, None, None, None, 10, 11]),startValue = 10,destValue = 11) == "UR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 2, 8, 1, 3, 6, 9, None, None, 4, 7, None, None, None, None, 10, 11]),startValue = 10,destValue = 11) == "UR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, 4, None, None, None, None, None, 8]),startValue = 3,destValue = 7) == "UR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, 4, None, None, None, None, None, 8]),startValue = 3,destValue = 7) == "UR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([5, 1, 2, 3, None, 6, 4, 8, 9, None, None, 12, 13, None, None, 16, 17, None, None, None, 18, 19, 20, None, None, None, None, 22, 23, 24, 25, 26, 27, 28, None, None, None, None, None, None, None, None, None, None, None, 30, None, None, None, 34, 35, 36, 37, 38, 39, 40, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 45, None, None, None, 49, 50, 51, 52, 53, 54, 55]),startValue = 49,destValue = 55) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([5, 1, 2, 3, None, 6, 4, 8, 9, None, None, 12, 13, None, None, 16, 17, None, None, None, 18, 19, 20, None, None, None, None, 22, 23, 24, 25, 26, 27, 28, None, None, None, None, None, None, None, None, None, None, None, 30, None, None, None, 34, 35, 36, 37, 38, 39, 40, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 45, None, None, None, 49, 50, 51, 52, 53, 54, 55]),startValue = 49,destValue = 55) == "": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, None, None, 4, None, 5, 6, None, None, None, None, None, 7, 8]),startValue = 1,destValue = 8) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, None, None, 4, None, 5, 6, None, None, None, None, None, 7, 8]),startValue = 1,destValue = 8) == "": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([2, 1, 3, None, None, 4, 5]),startValue = 3,destValue = 5) == "R"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([2, 1, 3, None, None, 4, 5]),startValue = 3,destValue = 5) == "R": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37, 2, 4, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28, 32, 34, 36, 38]),startValue = 8,destValue = 32) == "UUUURRLL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37, 2, 4, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28, 32, 34, 36, 38]),startValue = 8,destValue = 32) == "UUUURRLL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),startValue = 8,destValue = 19) == "URR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),startValue = 8,destValue = 19) == "URR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None]),startValue = 6,destValue = 7) == "URL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None]),startValue = 6,destValue = 7) == "URL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 3,destValue = 14) == "RL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 3,destValue = 14) == "RL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]),startValue = 1,destValue = 9) == "RRRR"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]),startValue = 1,destValue = 9) == "RRRR": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 14,destValue = 12) == "UULL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 14,destValue = 12) == "UULL": {e}')
    
    total += 1
    try:
        result = candidate(root = tree_node([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]),startValue = 7,destValue = 13) == "UUURRL"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(root = tree_node([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]),startValue = 7,destValue = 13) == "UUURRL": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18]),startValue = 3,destValue = 18) == "UURR"
    assert candidate(root = tree_node([2, 1]),startValue = 2,destValue = 1) == "L"
    assert candidate(root = tree_node([5, 1, 2, 3, None, 6, 4]),startValue = 3,destValue = 6) == "UURL"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7]),startValue = 4,destValue = 7) == "UURR"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),startValue = 8,destValue = 10) == "UURL"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 8,destValue = 15) == "UUURRR"
    assert candidate(root = tree_node([1, 2]),startValue = 2,destValue = 1) == "U"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 1,destValue = 15) == "RRR"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 8,destValue = 14) == "UUURRL"
    assert candidate(root = tree_node([3, 1, 4, None, 2]),startValue = 2,destValue = 4) == "UUR"
    assert candidate(root = tree_node([3, 1, 2]),startValue = 2,destValue = 1) == "UL"
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 17, 22, 27, 32, 38, 1, 4, 6, 8, 11, 13, 16, 18, 19, 21, 23, 24, 26, 28, 30, 31, 33, 34, 36, 37, 39, 40]),startValue = 37,destValue = 4) == "U"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),startValue = 45,destValue = 50) == "UUUUURLLRL"
    assert candidate(root = tree_node([5, 1, 2, 3, 8, 6, 4, 9, None, None, 10]),startValue = 9,destValue = 10) == "UURR"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 12,destValue = 14) == "UURL"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),startValue = 16,destValue = 19) == "UURR"
    assert candidate(root = tree_node([1, 2, 3, None, None, 6, 7, 8, 9, None, None, 12, 13, None, None, 16, 17]),startValue = 16,destValue = 17) == "UR"
    assert candidate(root = tree_node([5, 1, 2, 3, None, 6, 4, 8, None, None, None, 9]),startValue = 8,destValue = 9) == "UUURRL"
    assert candidate(root = tree_node([5, 1, 2, 3, 6, None, 4, 7, 8, None, None, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15, 16]),startValue = 7,destValue = 16) == "URRR"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),startValue = 4,destValue = 17) == "LR"
    assert candidate(root = tree_node([50, 25, 75, 12, 37, 62, 87, 6, 20, None, 40, None, 59, 80, 90]),startValue = 6,destValue = 80) == "UUURRL"
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 18, 1, None, 6, None, 11, 13, None, None, None, None, None, None, None]),startValue = 3,destValue = 13) == "UURLR"
    assert candidate(root = tree_node([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10, None, 11, None, 12]),startValue = 7,destValue = 12) == "LLLLL"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),startValue = 21,destValue = 28) == "UUUURRLL"
    assert candidate(root = tree_node([1, 2, None, 3, 4, None, 5, 6, None, None, 7, 8, 9]),startValue = 6,destValue = 9) == "R"
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 12, 17, 22, 27, 32, 38, 1, 4, 6, 8, 11, 13, 16, 18, 19, 21, 23, 24, 26, 28, 30, 31, 33, 34, 36, 37, 39, 40]),startValue = 4,destValue = 37) == "R"
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6, None, 14, 20, None, None, None, None, None, 13, 16, 19]),startValue = 3,destValue = 20) == "UURRR"
    assert candidate(root = tree_node([3, 1, 2, None, None, None, 4, None, 5, None, None, None, 6, None, None, None, None, None, None, 7]),startValue = 1,destValue = 7) == ""
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),startValue = 10,destValue = 19) == "UULRR"
    assert candidate(root = tree_node([50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 55, 59, 81, 93, 3, 9, 15, 21, 27, 35, 39, 47, 51, 57, 61, 67, 71, 77, 83, 89, 95, 1, 5, 7, 11, 13, 17, 19, 23, 29, 33, 37, 41, 45, 49, 53, 58, 63, 65, 69, 73, 75, 79, 85, 88, 91, 94, 97, 99]),startValue = 55,destValue = 88) == "UURLLL"
    assert candidate(root = tree_node([200, 100, 300, 50, 150, 250, 350, 25, 75, 125, 175, 225, 275, 325, 375, 10, 40, 60, 90, 130, 160, 180, 210, 240, 260, 290, 310, 340, 360, 390]),startValue = 10,destValue = 390) == "UUUURRRL"
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, 7, None, None, None, None, 8, 9, None, None, None, None, 10]),startValue = 10,destValue = 8) == ""
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, None, None, 6, 7, None, None, 8, 9]),startValue = 6,destValue = 9) == "URR"
    assert candidate(root = tree_node([1, 2, 3, None, None, 4, 5, 6, None, None, 7, 8, None, None, 9, 10, 11, 12, 13, 14, None, None, None, None, None, None, None, 15, 16, None, 17, None, None, 18]),startValue = 6,destValue = 18) == "LLLLRL"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]),startValue = 12,destValue = 24) == "L"
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6]),startValue = 3,destValue = 7) == "UR"
    assert candidate(root = tree_node([5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 8,destValue = 15) == "UUURRR"
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),startValue = 5,destValue = 1) == "UR"
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, None, 25, 35, 48, None, None, None, 18, None, None, None, None, None, None, None, None, 22, None, None, None, None, None, None, None, None, None, None]),startValue = 5,destValue = 22) == "RL"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, None, None, 14, 15, None, None, None, None, None, 16, 17, 18, 19, 20]),startValue = 8,destValue = 19) == "UUURLRL"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 14,destValue = 11) == "UUULRR"
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, 1, None, 6]),startValue = 1,destValue = 6) == "UURL"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),startValue = 16,destValue = 20) == "UUURLL"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 5,destValue = 11) == "R"
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 85, 110, 140, 160, 180]),startValue = 85,destValue = 140) == "UUURLR"
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, None, 5, 6, None, None, None, None, 7, 8, None, None, None, None, 9, 10]),startValue = 9,destValue = 10) == ""
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),startValue = 10,destValue = 45) == "URLR"
    assert candidate(root = tree_node([15, 10, 20, 8, 12, 18, 25, 6, 9, 11, 13, 16, 19, 22, 28, 5, 7, None, None, None, None, None, None, 14, None, None, None, None, None, 17, None, None, None, None, None, None, 21, None, None, None, None, None, None, None, None, None, None, None, None, 24, None, None, None, None, None, None, 26, None, 27]),startValue = 5,destValue = 27) == ""
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),startValue = 12,destValue = 49) == "LR"
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 10, 35, 65, 85, 115, 135, 165, 185]),startValue = 10,destValue = 185) == "UUURRR"
    assert candidate(root = tree_node([5, 1, 2, 3, 9, None, 6, 4, None, None, None, None, 8]),startValue = 4,destValue = 9) == "UUR"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, None, None, 20, 21, 22, None, 24, 25, 26, 27, 28]),startValue = 20,destValue = 27) == "UUURRR"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),startValue = 19,destValue = 7) == "UUUURR"
    assert candidate(root = tree_node([5, 1, 2, 3, None, 6, 4, 8, 9, None, None, 12, 13, None, None, 16, 17, None, None, None, 18, 19, 20, None, None, None, None, 22, 23, 24, 25, 26, 27, 28, None, None, None, None, None, None, None, None, None, None, None, 30]),startValue = 16,destValue = 28) == "LRL"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 7,destValue = 1) == "UU"
    assert candidate(root = tree_node([1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9, None, 10]),startValue = 1,destValue = 10) == "RRRRRRRRR"
    assert candidate(root = tree_node([30, 15, 45, 10, 20, 40, 50, 5, 12, 18, 25, 35, 48, 2, 8, 13, 16, 19, 23, 32, 38, 43, 47, 49, 1, 6, 9, 11, 14, 17, 21, 22, 24, 26, 29, 31, 33, 37, 41, 42, 44, 46, 51]),startValue = 42,destValue = 46) == "UURL"
    assert candidate(root = tree_node([1, 2, 3, 4, None, 5, 6, 7, None, 8, 9, 10, None, None, 11, 12, None, None, 13, 14, None, None, 15]),startValue = 11,destValue = 15) == "R"
    assert candidate(root = tree_node([1, 2, 3, None, None, 6, 4, None, None, None, 5]),startValue = 5,destValue = 1) == "UUU"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]),startValue = 10,destValue = 60) == "UUURRRLL"
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 13, 18, 1, None, 6]),startValue = 3,destValue = 6) == "URL"
    assert candidate(root = tree_node([10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, None, 17, 16, 25, 0, 2, None, None, None, None, None, None, 9]),startValue = 3,destValue = 25) == "UURRR"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, None, None, None, None, None, None, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),startValue = 16,destValue = 30) == "UUUURLLLL"
    assert candidate(root = tree_node([100, 50, 150, 25, 75, 125, 175, 12, 37, 62, 87, 112, 137, 162, 187, 6, 18, 31, 43, 55, 59, 81, 93, 107, 118, 127, 133, 147, 153, 167, 173, 183, 193, 3, 9, 15, 21, 27, 33, 39, 45, 49, 53, 58, 63, 65, 69, 73, 75, 79, 85, 88, 91, 94, 97, 99, 103, 109, 115, 121, 123, 129, 131, 139, 141, 149, 151, 157, 159, 165, 169, 171, 179, 181, 189, 191, 199]),startValue = 69,destValue = 171) == "UUUULRLLL"
    assert candidate(root = tree_node([5, 1, 2, 3, 8, None, 6, 4, None, None, 9, 10, 11]),startValue = 4,destValue = 11) == "UUURRR"
    assert candidate(root = tree_node([5, 1, 2, 3, 6, 7, 4, None, None, None, None, None, None, 8, 9, 10, 11, None, None, 12, 13]),startValue = 8,destValue = 13) == "LR"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]),startValue = 19,destValue = 38) == "L"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, None, 8, None, 9, None, 10, None, 11, None, 12, None, 13, None, 14, None, 15]),startValue = 2,destValue = 14) == "URLRR"
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),startValue = 5,destValue = 0) == "URL"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]),startValue = 10,destValue = 40) == "LL"
    assert candidate(root = tree_node([5, 1, 2, 3, None, 6, 4, 8, 9, None, None, 12, 13, None, None, 16, 17, None, None, None, 18, 19, 20, None, None, None, None, 22, 23, 24, 25, 26, 27, 28, None, None, None, None, None, None, None, None, None, None, None, 30, None, None, None, 34, 35, 36, 37, 38, 39, 40, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 45]),startValue = 34,destValue = 40) == ""
    assert candidate(root = tree_node([50, 25, 75, 10, 30, 60, 80, 5, 15, 27, 33, 55, 65, 77, 85]),startValue = 5,destValue = 65) == "UUURLR"
    assert candidate(root = tree_node([5, 2, 8, 1, 3, 6, 9, None, None, 4, 7, None, None, None, None, 10, 11]),startValue = 10,destValue = 11) == "UR"
    assert candidate(root = tree_node([10, 5, 15, 3, 7, None, 18, None, 4, None, None, None, None, None, 8]),startValue = 3,destValue = 7) == "UR"
    assert candidate(root = tree_node([5, 1, 2, 3, None, 6, 4, 8, 9, None, None, 12, 13, None, None, 16, 17, None, None, None, 18, 19, 20, None, None, None, None, 22, 23, 24, 25, 26, 27, 28, None, None, None, None, None, None, None, None, None, None, None, 30, None, None, None, 34, 35, 36, 37, 38, 39, 40, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 45, None, None, None, 49, 50, 51, 52, 53, 54, 55]),startValue = 49,destValue = 55) == ""
    assert candidate(root = tree_node([1, 2, 3, None, None, None, 4, None, 5, 6, None, None, None, None, None, 7, 8]),startValue = 1,destValue = 8) == ""
    assert candidate(root = tree_node([2, 1, 3, None, None, 4, 5]),startValue = 3,destValue = 5) == "R"
    assert candidate(root = tree_node([20, 10, 30, 5, 15, 25, 35, 3, 7, 13, 17, 23, 27, 33, 37, 2, 4, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28, 32, 34, 36, 38]),startValue = 8,destValue = 32) == "UUUURRLL"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]),startValue = 8,destValue = 19) == "URR"
    assert candidate(root = tree_node([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None, None, None]),startValue = 6,destValue = 7) == "URL"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 3,destValue = 14) == "RL"
    assert candidate(root = tree_node([1, 2, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]),startValue = 1,destValue = 9) == "RRRR"
    assert candidate(root = tree_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),startValue = 14,destValue = 12) == "UULL"
    assert candidate(root = tree_node([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]),startValue = 7,destValue = 13) == "UUURRL"


