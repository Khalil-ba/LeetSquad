def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 90, 80, 70, 60]),n = 3), list_node([100, 90, 70, 60]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 90, 80, 70, 60]),n = 3), list_node([100, 90, 70, 60])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2]),n = 1), list_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2]),n = 1), list_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 4, 3, 2, 1]),n = 5), list_node([4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 4, 3, 2, 1]),n = 5), list_node([4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5]),n = 2), list_node([1, 2, 3, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5]),n = 2), list_node([1, 2, 3, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),n = 5), list_node([1, 2, 3, 4, 5, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),n = 5), list_node([1, 2, 3, 4, 5, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1]),n = 1) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1]),n = 1) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3]),n = 3), list_node([2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3]),n = 3), list_node([2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]),n = 15), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]),n = 15), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 15), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 15), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),n = 1), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),n = 1), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),n = 5), list_node([10, 20, 30, 40, 50, 70, 80, 90, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),n = 5), list_node([10, 20, 30, 40, 50, 70, 80, 90, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]),n = 1), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]),n = 1), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),n = 3), list_node([1, 2, 3, 4, 5, 6, 7, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),n = 3), list_node([1, 2, 3, 4, 5, 6, 7, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([30, 20, 10]),n = 2), list_node([30, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([30, 20, 10]),n = 2), list_node([30, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 29), list_node([1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 29), list_node([1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 30), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 30), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]),n = 13), list_node([7, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]),n = 13), list_node([7, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60]),n = 1), list_node([10, 20, 30, 40, 50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60]),n = 1), list_node([10, 20, 30, 40, 50])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 3, 4, 5]),n = 1), list_node([2, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 3, 4, 5]),n = 1), list_node([2, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0]),n = 2), list_node([1, 0, 1, 0, 1, 0, 1, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0]),n = 2), list_node([1, 0, 1, 0, 1, 0, 1, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 10]),n = 2), list_node([10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 10]),n = 2), list_node([10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 2, 1]),n = 1), list_node([3, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 2, 1]),n = 1), list_node([3, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89]),n = 1), list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89]),n = 1), list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90]),n = 5), list_node([10, 20, 30, 40, 60, 70, 80, 90]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90]),n = 5), list_node([10, 20, 30, 40, 60, 70, 80, 90])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 10), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 10), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),n = 10), list_node([20, 30, 40, 50, 60, 70, 80, 90, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),n = 10), list_node([20, 30, 40, 50, 60, 70, 80, 90, 100])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5]),n = 1) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5]),n = 1) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 29), list_node([30, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 29), list_node([30, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]),n = 7), list_node([3, 6, 9, 12, 15, 18, 21, 24, 30, 33, 36, 39, 42, 45]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]),n = 7), list_node([3, 6, 9, 12, 15, 18, 21, 24, 30, 33, 36, 39, 42, 45])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 29), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 29), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 10), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 10), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]),n = 30), list_node([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]),n = 30), list_node([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),n = 10), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),n = 10), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]),n = 10), list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 65, 70, 75, 80, 85, 90, 95, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]),n = 10), list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 65, 70, 75, 80, 85, 90, 95, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30]),n = 16), list_node([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30]),n = 16), list_node([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 1), list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 1), list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 5), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 5), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]),n = 3), list_node([100, 99, 98, 97, 96, 95, 94, 93, 91, 90]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]),n = 3), list_node([100, 99, 98, 97, 96, 95, 94, 93, 91, 90])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),n = 1), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),n = 1), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9]),n = 10), list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 6, 4, 3, 3, 8, 3, 2, 7, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9]),n = 10), list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 6, 4, 3, 3, 8, 3, 2, 7, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 25), list_node([1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 25), list_node([1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),n = 28), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),n = 28), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),n = 10), list_node([1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),n = 10), list_node([1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1]),n = 29), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1]),n = 29), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 20), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 20), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 5, 1, 2, 4, 7, 6, 8, 9]),n = 3), list_node([3, 5, 1, 2, 4, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 5, 1, 2, 4, 7, 6, 8, 9]),n = 3), list_node([3, 5, 1, 2, 4, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]),n = 1), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]),n = 1), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2]),n = 2), list_node([2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2]),n = 2), list_node([2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]),n = 28), list_node([1, 3, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]),n = 28), list_node([1, 3, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),n = 4), list_node([1, 2, 3, 4, 5, 6, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),n = 4), list_node([1, 2, 3, 4, 5, 6, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 4), list_node([9, 8, 7, 6, 5, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 4), list_node([9, 8, 7, 6, 5, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 15), list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 15), list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 1), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 1), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),n = 2), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),n = 2), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 3, 4, 5]),n = 4), list_node([3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 3, 4, 5]),n = 4), list_node([3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]),n = 14), list_node([10, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]),n = 14), list_node([10, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),n = 1), list_node([10, 20, 30, 40, 50, 60, 70, 80, 90]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),n = 1), list_node([10, 20, 30, 40, 50, 60, 70, 80, 90])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 29), list_node([28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 29), list_node([28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]),n = 15), list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]),n = 15), list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 30), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 30), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),n = 25), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),n = 25), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70]),n = 15), list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70]),n = 15), list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([6, 2, 8, 2, 8, 4, 1, 8, 5, 2, 8, 6, 4, 3, 2, 8, 6, 2, 4, 3, 8, 2, 6, 4, 3, 2, 8, 6, 2, 4]),n = 20), list_node([6, 2, 8, 2, 8, 4, 1, 8, 5, 2, 6, 4, 3, 2, 8, 6, 2, 4, 3, 8, 2, 6, 4, 3, 2, 8, 6, 2, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([6, 2, 8, 2, 8, 4, 1, 8, 5, 2, 8, 6, 4, 3, 2, 8, 6, 2, 4, 3, 8, 2, 6, 4, 3, 2, 8, 6, 2, 4]),n = 20), list_node([6, 2, 8, 2, 8, 4, 1, 8, 5, 2, 6, 4, 3, 2, 8, 6, 2, 4, 3, 8, 2, 6, 4, 3, 2, 8, 6, 2, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 20), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 20), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71]),n = 10), list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 79, 78, 77, 76, 75, 74, 73, 72, 71]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71]),n = 10), list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 79, 78, 77, 76, 75, 74, 73, 72, 71])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 10), list_node([9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 10), list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([99, 88, 77, 66, 55, 44, 33, 22, 11]),n = 9), list_node([88, 77, 66, 55, 44, 33, 22, 11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([99, 88, 77, 66, 55, 44, 33, 22, 11]),n = 9), list_node([88, 77, 66, 55, 44, 33, 22, 11])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 1), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 1), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]),n = 14), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]),n = 14), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]),n = 15), list_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]),n = 15), list_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71]),n = 1), list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71]),n = 1), list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71]),n = 1), list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71]),n = 1), list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 30), list_node([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 30), list_node([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),n = 7), list_node([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),n = 7), list_node([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 2, 1]),n = 2), list_node([3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 2, 1]),n = 2), list_node([3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 2), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 2), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),n = 8), list_node([1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),n = 8), list_node([1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),n = 15), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),n = 15), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 9), list_node([8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 9), list_node([8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_list(candidate(head = list_node([100, 90, 80, 70, 60]),n = 3), list_node([100, 90, 70, 60]))
    assert is_same_list(candidate(head = list_node([1, 2]),n = 1), list_node([1]))
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1]),n = 5), list_node([4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5]),n = 2), list_node([1, 2, 3, 5]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),n = 5), list_node([1, 2, 3, 4, 5, 7, 8, 9, 10]))
    assert candidate(head = list_node([1]),n = 1) == None
    assert is_same_list(candidate(head = list_node([1, 2, 3]),n = 3), list_node([2, 3]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]),n = 15), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 15), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),n = 1), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),n = 5), list_node([10, 20, 30, 40, 50, 70, 80, 90, 100]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]),n = 1), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),n = 3), list_node([1, 2, 3, 4, 5, 6, 7, 9, 10]))
    assert is_same_list(candidate(head = list_node([30, 20, 10]),n = 2), list_node([30, 10]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 29), list_node([1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 30), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]),n = 13), list_node([7, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60]),n = 1), list_node([10, 20, 30, 40, 50]))
    assert is_same_list(candidate(head = list_node([2, 3, 4, 5]),n = 1), list_node([2, 3, 4]))
    assert is_same_list(candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0]),n = 2), list_node([1, 0, 1, 0, 1, 0, 1, 0, 0]))
    assert is_same_list(candidate(head = list_node([5, 10]),n = 2), list_node([10]))
    assert is_same_list(candidate(head = list_node([3, 2, 1]),n = 1), list_node([3, 2]))
    assert is_same_list(candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89]),n = 1), list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90]),n = 5), list_node([10, 20, 30, 40, 60, 70, 80, 90]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 10), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),n = 10), list_node([20, 30, 40, 50, 60, 70, 80, 90, 100]))
    assert candidate(head = list_node([5]),n = 1) == None
    assert is_same_list(candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 29), list_node([30, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45]),n = 7), list_node([3, 6, 9, 12, 15, 18, 21, 24, 30, 33, 36, 39, 42, 45]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 29), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 10), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]),n = 30), list_node([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),n = 10), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]),n = 10), list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 65, 70, 75, 80, 85, 90, 95, 100]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30]),n = 16), list_node([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30]))
    assert is_same_list(candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 1), list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 5), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90]),n = 3), list_node([100, 99, 98, 97, 96, 95, 94, 93, 91, 90]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),n = 1), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    assert is_same_list(candidate(head = list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9]),n = 10), list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 6, 4, 3, 3, 8, 3, 2, 7, 9]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 25), list_node([1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),n = 28), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),n = 10), list_node([1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1]),n = 29), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 20), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([3, 5, 1, 2, 4, 7, 6, 8, 9]),n = 3), list_node([3, 5, 1, 2, 4, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]),n = 1), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]))
    assert is_same_list(candidate(head = list_node([1, 2]),n = 2), list_node([2]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]),n = 28), list_node([1, 3, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),n = 4), list_node([1, 2, 3, 4, 5, 6, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 4), list_node([9, 8, 7, 6, 5, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 15), list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 1), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]))
    assert is_same_list(candidate(head = list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]),n = 2), list_node([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
    assert is_same_list(candidate(head = list_node([2, 3, 4, 5]),n = 4), list_node([3, 4, 5]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]),n = 14), list_node([10, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]),n = 1), list_node([10, 20, 30, 40, 50, 60, 70, 80, 90]))
    assert is_same_list(candidate(head = list_node([29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 29), list_node([28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]),n = 15), list_node([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 30), list_node([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),n = 25), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
    assert is_same_list(candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70]),n = 15), list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70]))
    assert is_same_list(candidate(head = list_node([6, 2, 8, 2, 8, 4, 1, 8, 5, 2, 8, 6, 4, 3, 2, 8, 6, 2, 4, 3, 8, 2, 6, 4, 3, 2, 8, 6, 2, 4]),n = 20), list_node([6, 2, 8, 2, 8, 4, 1, 8, 5, 2, 6, 4, 3, 2, 8, 6, 2, 4, 3, 8, 2, 6, 4, 3, 2, 8, 6, 2, 4]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),n = 20), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71]),n = 10), list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 79, 78, 77, 76, 75, 74, 73, 72, 71]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 10), list_node([9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([99, 88, 77, 66, 55, 44, 33, 22, 11]),n = 9), list_node([88, 77, 66, 55, 44, 33, 22, 11]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 1), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2]))
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]),n = 14), list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]))
    assert is_same_list(candidate(head = list_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]),n = 15), list_node([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]))
    assert is_same_list(candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71]),n = 1), list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72]))
    assert is_same_list(candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71]),n = 1), list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 30), list_node([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),n = 7), list_node([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([3, 2, 1]),n = 2), list_node([3, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]),n = 2), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),n = 8), list_node([1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),n = 15), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1]),n = 9), list_node([8, 7, 6, 5, 4, 3, 2, 1]))


