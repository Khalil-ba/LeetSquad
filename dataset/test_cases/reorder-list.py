def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 4, 3, 2, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 4, 3, 2, 1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([500, 400, 300, 200, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([500, 400, 300, 200, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 4, 3, 2, 1, 6, 7, 8, 9, 10])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 4, 3, 2, 1, 6, 7, 8, 9, 10])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 3, 5, 7, 9, 2, 4, 6, 8])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 3, 5, 7, 9, 2, 4, 6, 8])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175, 182, 189, 196, 203, 210])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175, 182, 189, 196, 203, 210])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80])) == None: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8])) == None: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(head = list_node([1, 2, 3])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5])) == None
    assert candidate(head = list_node([1])) == None
    assert candidate(head = list_node([1, 2])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == None
    assert candidate(head = list_node([1, 2, 3, 4])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])) == None
    assert candidate(head = list_node([5, 4, 3, 2, 1])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])) == None
    assert candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])) == None
    assert candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34])) == None
    assert candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])) == None
    assert candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == None
    assert candidate(head = list_node([40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == None
    assert candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == None
    assert candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])) == None
    assert candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50])) == None
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None
    assert candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60])) == None
    assert candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])) == None
    assert candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])) == None
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == None
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160])) == None
    assert candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70])) == None
    assert candidate(head = list_node([5])) == None
    assert candidate(head = list_node([500, 400, 300, 200, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7])) == None
    assert candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35])) == None
    assert candidate(head = list_node([50, 40, 30, 20, 10, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205])) == None
    assert candidate(head = list_node([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])) == None
    assert candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])) == None
    assert candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == None
    assert candidate(head = list_node([5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) == None
    assert candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39])) == None
    assert candidate(head = list_node([5, 4, 3, 2, 1, 6, 7, 8, 9, 10])) == None
    assert candidate(head = list_node([1, 3, 5, 7, 9, 2, 4, 6, 8])) == None
    assert candidate(head = list_node([1000, 999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989])) == None
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80])) == None
    assert candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
    assert candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29])) == None
    assert candidate(head = list_node([500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1])) == None
    assert candidate(head = list_node([50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == None
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90])) == None
    assert candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26])) == None
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250])) == None
    assert candidate(head = list_node([7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175, 182, 189, 196, 203, 210])) == None
    assert candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])) == None
    assert candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41])) == None
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])) == None
    assert candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])) == None
    assert candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000])) == None
    assert candidate(head = list_node([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == None
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130])) == None
    assert candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])) == None
    assert candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) == None
    assert candidate(head = list_node([99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80])) == None
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8])) == None


