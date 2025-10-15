def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0])), list_node([0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0])), list_node([0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, -1, 0, 5, 3, 2, -5])), list_node([-5, -1, 0, 2, 3, 5, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, -1, 0, 5, 3, 2, -5])), list_node([-5, -1, 0, 2, 3, 5, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 2, 4, 6, 1, 3])), list_node([1, 2, 3, 4, 5, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 2, 4, 6, 1, 3])), list_node([1, 2, 3, 4, 5, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 1, 2, 1, 3, 1, 2])), list_node([1, 1, 1, 2, 2, 3, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 1, 2, 1, 3, 1, 2])), list_node([1, 1, 1, 2, 2, 3, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 2, 4, 5])), list_node([1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 2, 4, 5])), list_node([1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31, 15, 7, 3, 1])), list_node([1, 3, 7, 15, 31, 62, 125, 250, 500, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31, 15, 7, 3, 1])), list_node([1, 3, 7, 15, 31, 62, 125, 250, 500, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1])), list_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1])), list_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 999, 998, 997, 996, 995, 994, 993, 992, 991])), list_node([991, 992, 993, 994, 995, 996, 997, 998, 999, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 999, 998, 997, 996, 995, 994, 993, 992, 991])), list_node([991, 992, 993, 994, 995, 996, 997, 998, 999, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, 5, 3, 4, 0])), list_node([-1, 0, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, 5, 3, 4, 0])), list_node([-1, 0, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, -1, -2, -3, -4])), list_node([-4, -3, -2, -1, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, -1, -2, -3, -4])), list_node([-4, -3, -2, -1, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5000, 5000, -5000, 5000, 0])), list_node([-5000, -5000, 0, 5000, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5000, 5000, -5000, 5000, 0])), list_node([-5000, -5000, 0, 5000, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([4, 2, 1, 3])), list_node([1, 2, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([4, 2, 1, 3])), list_node([1, 2, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 50, 25, 12, 6, 3, 1])), list_node([1, 3, 6, 12, 25, 50, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 50, 25, 12, 6, 3, 1])), list_node([1, 3, 6, 12, 25, 50, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([4, 4, 4, 4, 4])), list_node([4, 4, 4, 4, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([4, 4, 4, 4, 4])), list_node([4, 4, 4, 4, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 1, 4, 2, 3])), list_node([1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 1, 4, 2, 3])), list_node([1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5000, 5000, -4999, 4999])), list_node([-5000, -4999, 4999, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5000, 5000, -4999, 4999])), list_node([-5000, -4999, 4999, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, -5000, 2500, 0, -2500, 1250, -1250, 625, -625, 312, -312])), list_node([-5000, -2500, -1250, -625, -312, 0, 312, 625, 1250, 2500, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, -5000, 2500, 0, -2500, 1250, -1250, 625, -625, 312, -312])), list_node([-5000, -2500, -1250, -625, -312, 0, 312, 625, 1250, 2500, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, -5000, 0, 2500, -2500, 4000, -4000, 1000, -1000])), list_node([-5000, -4000, -2500, -1000, 0, 1000, 2500, 4000, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, -5000, 0, 2500, -2500, 4000, -4000, 1000, -1000])), list_node([-5000, -4000, -2500, -1000, 0, 1000, 2500, 4000, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140])), list_node([7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140])), list_node([7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([34, 22, 10, 19, 17, 26, 31, 44, 54, 20])), list_node([10, 17, 19, 20, 22, 26, 31, 34, 44, 54]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([34, 22, 10, 19, 17, 26, 31, 44, 54, 20])), list_node([10, 17, 19, 20, 22, 26, 31, 34, 44, 54])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([23, 5, 67, 2, 34, 89, 12, 56, 3, 78])), list_node([2, 3, 5, 12, 23, 34, 56, 67, 78, 89]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([23, 5, 67, 2, 34, 89, 12, 56, 3, 78])), list_node([2, 3, 5, 12, 23, 34, 56, 67, 78, 89])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, -5000, 4999, -4999, 4998, -4998, 4997, -4997, 4996, -4996, 4995, -4995, 4994, -4994])), list_node([-5000, -4999, -4998, -4997, -4996, -4995, -4994, 4994, 4995, 4996, 4997, 4998, 4999, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, -5000, 4999, -4999, 4998, -4998, 4997, -4997, 4996, -4996, 4995, -4995, 4994, -4994])), list_node([-5000, -4999, -4998, -4997, -4996, -4995, -4994, 4994, 4995, 4996, 4997, 4998, 4999, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 2, 4, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 2, 4, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, -1, -2, -3, -4, -5, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])), list_node([-5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, -1, -2, -3, -4, -5, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])), list_node([-5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, -5000, 2500, -2500, 1250, -1250])), list_node([-5000, -2500, -1250, 1250, 2500, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, -5000, 2500, -2500, 1250, -1250])), list_node([-5000, -2500, -1250, 1250, 2500, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])), list_node([1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])), list_node([1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])), list_node([1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])), list_node([1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5])), list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5])), list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])), list_node([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])), list_node([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 1, 2, 5, 4, 6, 7, 8, 10, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 1, 2, 5, 4, 6, 7, 8, 10, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 150, 250, 350, 450, 550])), list_node([100, 150, 200, 250, 300, 350, 400, 450, 500, 550]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 150, 250, 350, 450, 550])), list_node([100, 150, 200, 250, 300, 350, 400, 450, 500, 550])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 3, 5, 4, 1, 7, 6, 9, 8, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 3, 5, 4, 1, 7, 6, 9, 8, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5000, -4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990, -4989, -4988, -4987, -4986, -4985, -4984, -4983, -4982, -4981])), list_node([-5000, -4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990, -4989, -4988, -4987, -4986, -4985, -4984, -4983, -4982, -4981]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5000, -4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990, -4989, -4988, -4987, -4986, -4985, -4984, -4983, -4982, -4981])), list_node([-5000, -4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990, -4989, -4988, -4987, -4986, -4985, -4984, -4983, -4982, -4981])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 9, 3, 3, 7, 2, 0, 7, 8, 1, 6, 4, 2, 1, 6, 1, 9, 9, 9, 4, 5, 3, 0, 7, 7, 2, 7])), list_node([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 9, 3, 3, 7, 2, 0, 7, 8, 1, 6, 4, 2, 1, 6, 1, 9, 9, 9, 4, 5, 3, 0, 7, 7, 2, 7])), list_node([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1, 6, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1, 6, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990])), list_node([9990, 9991, 9992, 9993, 9994, 9995, 9996, 9997, 9998, 9999]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990])), list_node([9990, 9991, 9992, 9993, 9994, 9995, 9996, 9997, 9998, 9999])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 2, 1, 3, 2, 1, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 2, 1, 3, 2, 1, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 10, 20, 30, 40, 50, 60, 70, 80, 90, 1])), list_node([1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 10, 20, 30, 40, 50, 60, 70, 80, 90, 1])), list_node([1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 50, 25, 12, 6, 3, 1, 0, -1, -2, -5, -10, -25, -50, -100])), list_node([-100, -50, -25, -10, -5, -2, -1, 0, 1, 3, 6, 12, 25, 50, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 50, 25, 12, 6, 3, 1, 0, -1, -2, -5, -10, -25, -50, -100])), list_node([-100, -50, -25, -10, -5, -2, -1, 0, 1, 3, 6, 12, 25, 50, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 3, 8, 6, 2, 7, 4, 1, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 3, 8, 6, 2, 7, 4, 1, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 200, 150, 175, 160, 180, 190, 140, 130, 120])), list_node([100, 120, 130, 140, 150, 160, 175, 180, 190, 200]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 200, 150, 175, 160, 180, 190, 140, 130, 120])), list_node([100, 120, 130, 140, 150, 160, 175, 180, 190, 200])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, -10, 20, -20, 30, -30, 40, -40, 50, -50])), list_node([-50, -40, -30, -20, -10, 10, 20, 30, 40, 50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, -10, 20, -20, 30, -30, 40, -40, 50, -50])), list_node([-50, -40, -30, -20, -10, 10, 20, 30, 40, 50])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312, 156, -156, 78, -78, 39, -39, 19, -19, 9, -9, 4, -4, 2, -2, 1, -1])), list_node([-5000, -2500, -1250, -625, -312, -156, -78, -39, -19, -9, -4, -2, -1, 0, 1, 2, 4, 9, 19, 39, 78, 156, 312, 625, 1250, 2500, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312, 156, -156, 78, -78, 39, -39, 19, -19, 9, -9, 4, -4, 2, -2, 1, -1])), list_node([-5000, -2500, -1250, -625, -312, -156, -78, -39, -19, -9, -4, -2, -1, 0, 1, 2, 4, 9, 19, 39, 78, 156, 312, 625, 1250, 2500, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000])), list_node([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000])), list_node([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20])), list_node([-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20])), list_node([-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])), list_node([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])), list_node([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 2, 4, 6, 7, 8, 10, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 2, 4, 6, 7, 8, 10, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, -1, 4, 1, 5, 9, -2, 6, 5, 3, 5])), list_node([-2, -1, 1, 3, 3, 4, 5, 5, 5, 6, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, -1, 4, 1, 5, 9, -2, 6, 5, 3, 5])), list_node([-2, -1, 1, 3, 3, 4, 5, 5, 5, 6, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312, 156, -156, 78, -78, 39, -39])), list_node([-5000, -2500, -1250, -625, -312, -156, -78, -39, 39, 78, 156, 312, 625, 1250, 2500, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312, 156, -156, 78, -78, 39, -39])), list_node([-5000, -2500, -1250, -625, -312, -156, -78, -39, 39, 78, 156, 312, 625, 1250, 2500, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 1, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 1, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 3, 4, 2, 6, 1, 7, 9, 8, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 3, 4, 2, 6, 1, 7, 9, 8, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13, -13, 14, -14, 15, -15])), list_node([-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13, -13, 14, -14, 15, -15])), list_node([-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 50, 150, 250, 350, 450])), list_node([50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 50, 150, 250, 350, 450])), list_node([50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1, 2, 3, 4, 5])), list_node([1, 2, 3, 4, 5, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1, 2, 3, 4, 5])), list_node([1, 2, 3, 4, 5, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([4, 1, 7, 3, 2, 6, 5, 8, 0, 9])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([4, 1, 7, 3, 2, 6, 5, 8, 0, 9])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-10, -20, 5, 3, -15, 7, 0])), list_node([-20, -15, -10, 0, 3, 5, 7]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-10, -20, 5, 3, -15, 7, 0])), list_node([-20, -15, -10, 0, 3, 5, 7])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 3, 8, 6, 2, 7, 4, 1, 10, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 3, 8, 6, 2, 7, 4, 1, 10, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([23, 45, 12, 33, 5, 67, 4, 89, 21])), list_node([4, 5, 12, 21, 23, 33, 45, 67, 89]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([23, 45, 12, 33, 5, 67, 4, 89, 21])), list_node([4, 5, 12, 21, 23, 33, 45, 67, 89])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 3, 1, 9, 2, 5, 8, 7, 6, 4])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 3, 1, 9, 2, 5, 8, 7, 6, 4])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25])), list_node([-25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25])), list_node([-25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, -5000, 0, 2500, -2500, 1250, -1250, 625, -625, 312, -312])), list_node([-5000, -2500, -1250, -625, -312, 0, 312, 625, 1250, 2500, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, -5000, 0, 2500, -2500, 1250, -1250, 625, -625, 312, -312])), list_node([-5000, -2500, -1250, -625, -312, 0, 312, 625, 1250, 2500, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])), list_node([-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])), list_node([-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5])), list_node([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5])), list_node([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75])), list_node([75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75])), list_node([75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5000, -4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990, -4989, -4988, -4987, -4986, -4985])), list_node([-5000, -4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990, -4989, -4988, -4987, -4986, -4985]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5000, -4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990, -4989, -4988, -4987, -4986, -4985])), list_node([-5000, -4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990, -4989, -4988, -4987, -4986, -4985])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, 4999, 4998, 4997, 4996, 4995, 4994, 4993, 4992, 4991, 4990, 4989, 4988, 4987, 4986, 4985, 4984, 4983, 4982, 4981])), list_node([4981, 4982, 4983, 4984, 4985, 4986, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, 4999, 4998, 4997, 4996, 4995, 4994, 4993, 4992, 4991, 4990, 4989, 4988, 4987, 4986, 4985, 4984, 4983, 4982, 4981])), list_node([4981, 4982, 4983, 4984, 4985, 4986, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 1, 2, 1, 3, 1, 2, 1, 3])), list_node([1, 1, 1, 1, 2, 2, 3, 3, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 1, 2, 1, 3, 1, 2, 1, 3])), list_node([1, 1, 1, 1, 2, 2, 3, 3, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2000, 1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, -1, -3, -7, -15, -31, -62, -125, -250, -500, -1000, -2000])), list_node([-2000, -1000, -500, -250, -125, -62, -31, -15, -7, -3, -1, 1, 3, 7, 15, 31, 62, 125, 250, 500, 1000, 2000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2000, 1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, -1, -3, -7, -15, -31, -62, -125, -250, -500, -1000, -2000])), list_node([-2000, -1000, -500, -250, -125, -62, -31, -15, -7, -3, -1, 1, 3, 7, 15, 31, 62, 125, 250, 500, 1000, 2000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1])), list_node([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1])), list_node([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 1, 2, 5, 4, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21])), list_node([1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 1, 2, 5, 4, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21])), list_node([1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 101, 99, 98, 102, 103, 97, 96, 104, 105])), list_node([96, 97, 98, 99, 100, 101, 102, 103, 104, 105]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 101, 99, 98, 102, 103, 97, 96, 104, 105])), list_node([96, 97, 98, 99, 100, 101, 102, 103, 104, 105])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, 4999, 4998, 4997, 4996, 4995, 4994, 4993, 4992, 4991, 4990, 4989, 4988, 4987, 4986, 4985])), list_node([4985, 4986, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, 4999, 4998, 4997, 4996, 4995, 4994, 4993, 4992, 4991, 4990, 4989, 4988, 4987, 4986, 4985])), list_node([4985, 4986, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 3, 1, 4, 2, 6, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 3, 1, 4, 2, 6, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 30, 40, 50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 30, 40, 50])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312])), list_node([-5000, -2500, -1250, -625, -312, 312, 625, 1250, 2500, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312])), list_node([-5000, -2500, -1250, -625, -312, 312, 625, 1250, 2500, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])), list_node([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])), list_node([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100, -200, -150, -175, -160, -180, -190, -140, -130, -120])), list_node([-200, -190, -180, -175, -160, -150, -140, -130, -120, -100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100, -200, -150, -175, -160, -180, -190, -140, -130, -120])), list_node([-200, -190, -180, -175, -160, -150, -140, -130, -120, -100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, 4999, 4998, 4997, 4996, 4995, 4994, 4993, 4992, 4991, 4990, 4989, 4988, 4987, 4986, 4985, 4984, 4983, 4982, 4981, 4980])), list_node([4980, 4981, 4982, 4983, 4984, 4985, 4986, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, 4999, 4998, 4997, 4996, 4995, 4994, 4993, 4992, 4991, 4990, 4989, 4988, 4987, 4986, 4985, 4984, 4983, 4982, 4981, 4980])), list_node([4980, 4981, 4982, 4983, 4984, 4985, 4986, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0])), list_node([0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([10, -1, 0, 5, 3, 2, -5])), list_node([-5, -1, 0, 2, 3, 5, 10]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([5, 2, 4, 6, 1, 3])), list_node([1, 2, 3, 4, 5, 6]))
    assert is_same_list(candidate(head = list_node([3, 1, 2, 1, 3, 1, 2])), list_node([1, 1, 1, 2, 2, 3, 3]))
    assert is_same_list(candidate(head = list_node([1, 3, 2, 4, 5])), list_node([1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31, 15, 7, 3, 1])), list_node([1, 3, 7, 15, 31, 62, 125, 250, 500, 1000]))
    assert is_same_list(candidate(head = list_node([1])), list_node([1]))
    assert is_same_list(candidate(head = list_node([1000, 999, 998, 997, 996, 995, 994, 993, 992, 991])), list_node([991, 992, 993, 994, 995, 996, 997, 998, 999, 1000]))
    assert is_same_list(candidate(head = list_node([-1, 5, 3, 4, 0])), list_node([-1, 0, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([0, -1, -2, -3, -4])), list_node([-4, -3, -2, -1, 0]))
    assert is_same_list(candidate(head = list_node([-5000, 5000, -5000, 5000, 0])), list_node([-5000, -5000, 0, 5000, 5000]))
    assert is_same_list(candidate(head = list_node([4, 2, 1, 3])), list_node([1, 2, 3, 4]))
    assert is_same_list(candidate(head = list_node([100, 50, 25, 12, 6, 3, 1])), list_node([1, 3, 6, 12, 25, 50, 100]))
    assert is_same_list(candidate(head = list_node([4, 4, 4, 4, 4])), list_node([4, 4, 4, 4, 4]))
    assert is_same_list(candidate(head = list_node([5, 1, 4, 2, 3])), list_node([1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([-5000, 5000, -4999, 4999])), list_node([-5000, -4999, 4999, 5000]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([5000, -5000, 2500, 0, -2500, 1250, -1250, 625, -625, 312, -312])), list_node([-5000, -2500, -1250, -625, -312, 0, 312, 625, 1250, 2500, 5000]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([5000, -5000, 0, 2500, -2500, 4000, -4000, 1000, -1000])), list_node([-5000, -4000, -2500, -1000, 0, 1000, 2500, 4000, 5000]))
    assert is_same_list(candidate(head = list_node([7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140])), list_node([7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140]))
    assert is_same_list(candidate(head = list_node([34, 22, 10, 19, 17, 26, 31, 44, 54, 20])), list_node([10, 17, 19, 20, 22, 26, 31, 34, 44, 54]))
    assert is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([23, 5, 67, 2, 34, 89, 12, 56, 3, 78])), list_node([2, 3, 5, 12, 23, 34, 56, 67, 78, 89]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([5000, -5000, 4999, -4999, 4998, -4998, 4997, -4997, 4996, -4996, 4995, -4995, 4994, -4994])), list_node([-5000, -4999, -4998, -4997, -4996, -4995, -4994, 4994, 4995, 4996, 4997, 4998, 4999, 5000]))
    assert is_same_list(candidate(head = list_node([1, 3, 2, 4, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([0, -1, -2, -3, -4, -5, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])), list_node([-5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 0, 0, 1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([5000, -5000, 2500, -2500, 1250, -1250])), list_node([-5000, -2500, -1250, 1250, 2500, 5000]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
    assert is_same_list(candidate(head = list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])), list_node([1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]))
    assert is_same_list(candidate(head = list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])), list_node([1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 4, 3, 2, 1, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5])), list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])), list_node([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([3, 1, 2, 5, 4, 6, 7, 8, 10, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([3, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 150, 250, 350, 450, 550])), list_node([100, 150, 200, 250, 300, 350, 400, 450, 500, 550]))
    assert is_same_list(candidate(head = list_node([2, 3, 5, 4, 1, 7, 6, 9, 8, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([-5000, -4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990, -4989, -4988, -4987, -4986, -4985, -4984, -4983, -4982, -4981])), list_node([-5000, -4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990, -4989, -4988, -4987, -4986, -4985, -4984, -4983, -4982, -4981]))
    assert is_same_list(candidate(head = list_node([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 9, 3, 3, 7, 2, 0, 7, 8, 1, 6, 4, 2, 1, 6, 1, 9, 9, 9, 4, 5, 3, 0, 7, 7, 2, 7])), list_node([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 2, 1, 4, 5, 4, 3, 2, 1, 6, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 6, 7]))
    assert is_same_list(candidate(head = list_node([9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990])), list_node([9990, 9991, 9992, 9993, 9994, 9995, 9996, 9997, 9998, 9999]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 2, 1, 3, 2, 1, 2, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 10, 20, 30, 40, 50, 60, 70, 80, 90, 1])), list_node([1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]))
    assert is_same_list(candidate(head = list_node([100, 50, 25, 12, 6, 3, 1, 0, -1, -2, -5, -10, -25, -50, -100])), list_node([-100, -50, -25, -10, -5, -2, -1, 0, 1, 3, 6, 12, 25, 50, 100]))
    assert is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
    assert is_same_list(candidate(head = list_node([5, 3, 8, 6, 2, 7, 4, 1, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
    assert is_same_list(candidate(head = list_node([100, 200, 150, 175, 160, 180, 190, 140, 130, 120])), list_node([100, 120, 130, 140, 150, 160, 175, 180, 190, 200]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([10, -10, 20, -20, 30, -30, 40, -40, 50, -50])), list_node([-50, -40, -30, -20, -10, 10, 20, 30, 40, 50]))
    assert is_same_list(candidate(head = list_node([0, 5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312, 156, -156, 78, -78, 39, -39, 19, -19, 9, -9, 4, -4, 2, -2, 1, -1])), list_node([-5000, -2500, -1250, -625, -312, -156, -78, -39, -19, -9, -4, -2, -1, 0, 1, 2, 4, 9, 19, 39, 78, 156, 312, 625, 1250, 2500, 5000]))
    assert is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000])), list_node([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20])), list_node([-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])), list_node([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 2, 4, 6, 7, 8, 10, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([3, -1, 4, 1, 5, 9, -2, 6, 5, 3, 5])), list_node([-2, -1, 1, 3, 3, 4, 5, 5, 5, 6, 9]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312, 156, -156, 78, -78, 39, -39])), list_node([-5000, -2500, -1250, -625, -312, -156, -78, -39, 39, 78, 156, 312, 625, 1250, 2500, 5000]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([3, 1, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([5, 3, 4, 2, 6, 1, 7, 9, 8, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13, -13, 14, -14, 15, -15])), list_node([-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 50, 150, 250, 350, 450])), list_node([50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1, 2, 3, 4, 5])), list_node([1, 2, 3, 4, 5, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]))
    assert is_same_list(candidate(head = list_node([4, 1, 7, 3, 2, 6, 5, 8, 0, 9])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([-10, -20, 5, 3, -15, 7, 0])), list_node([-20, -15, -10, 0, 3, 5, 7]))
    assert is_same_list(candidate(head = list_node([5, 3, 8, 6, 2, 7, 4, 1, 10, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([23, 45, 12, 33, 5, 67, 4, 89, 21])), list_node([4, 5, 12, 21, 23, 33, 45, 67, 89]))
    assert is_same_list(candidate(head = list_node([10, 3, 1, 9, 2, 5, 8, 7, 6, 4])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25])), list_node([-25, -24, -23, -22, -21, -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]))
    assert is_same_list(candidate(head = list_node([5000, -5000, 0, 2500, -2500, 1250, -1250, 625, -625, 312, -312])), list_node([-5000, -2500, -1250, -625, -312, 0, 312, 625, 1250, 2500, 5000]))
    assert is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])), list_node([-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5])), list_node([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
    assert is_same_list(candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75])), list_node([75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]))
    assert is_same_list(candidate(head = list_node([-5000, -4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990, -4989, -4988, -4987, -4986, -4985])), list_node([-5000, -4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990, -4989, -4988, -4987, -4986, -4985]))
    assert is_same_list(candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([5000, 4999, 4998, 4997, 4996, 4995, 4994, 4993, 4992, 4991, 4990, 4989, 4988, 4987, 4986, 4985, 4984, 4983, 4982, 4981])), list_node([4981, 4982, 4983, 4984, 4985, 4986, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, 5000]))
    assert is_same_list(candidate(head = list_node([3, 1, 2, 1, 3, 1, 2, 1, 3])), list_node([1, 1, 1, 1, 2, 2, 3, 3, 3]))
    assert is_same_list(candidate(head = list_node([2000, 1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, -1, -3, -7, -15, -31, -62, -125, -250, -500, -1000, -2000])), list_node([-2000, -1000, -500, -250, -125, -62, -31, -15, -7, -3, -1, 1, 3, 7, 15, 31, 62, 125, 250, 500, 1000, 2000]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1])), list_node([1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([3, 1, 2, 5, 4, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21])), list_node([1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]))
    assert is_same_list(candidate(head = list_node([100, 101, 99, 98, 102, 103, 97, 96, 104, 105])), list_node([96, 97, 98, 99, 100, 101, 102, 103, 104, 105]))
    assert is_same_list(candidate(head = list_node([5000, 4999, 4998, 4997, 4996, 4995, 4994, 4993, 4992, 4991, 4990, 4989, 4988, 4987, 4986, 4985])), list_node([4985, 4986, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, 5000]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([5, 3, 1, 4, 2, 6, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 30, 40, 50]))
    assert is_same_list(candidate(head = list_node([5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312])), list_node([-5000, -2500, -1250, -625, -312, 312, 625, 1250, 2500, 5000]))
    assert is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14, 17, 16, 19, 18, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])), list_node([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([-100, -200, -150, -175, -160, -180, -190, -140, -130, -120])), list_node([-200, -190, -180, -175, -160, -150, -140, -130, -120, -100]))
    assert is_same_list(candidate(head = list_node([5000, 4999, 4998, 4997, 4996, 4995, 4994, 4993, 4992, 4991, 4990, 4989, 4988, 4987, 4986, 4985, 4984, 4983, 4982, 4981, 4980])), list_node([4980, 4981, 4982, 4983, 4984, 4985, 4986, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, 5000]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))


