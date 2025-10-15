def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, -5000, 0, 1000, -1000])), list_node([-1000, 1000, 0, -5000, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, -5000, 0, 1000, -1000])), list_node([-1000, 1000, 0, -5000, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2])), list_node([2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2])), list_node([2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1])), list_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1])), list_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5])), list_node([-5, -4, -3, -2, -1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5])), list_node([-5, -4, -3, -2, -1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3])), list_node([3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3])), list_node([3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1000, 0, 1000])), list_node([1000, 0, -1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1000, 0, 1000])), list_node([1000, 0, -1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, -5000, 5000, -5000])), list_node([-5000, 5000, -5000, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, -5000, 5000, -5000])), list_node([-5000, 5000, -5000, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5])), list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5])), list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])), list_node([21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])), list_node([21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5000, -4000, -3000, -2000, -1000, 0, 1000, 2000, 3000, 4000, 5000])), list_node([5000, 4000, 3000, 2000, 1000, 0, -1000, -2000, -3000, -4000, -5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5000, -4000, -3000, -2000, -1000, 0, 1000, 2000, 3000, 4000, 5000])), list_node([5000, 4000, 3000, 2000, 1000, 0, -1000, -2000, -3000, -4000, -5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5000, -2500, 0, 2500, 5000])), list_node([5000, 2500, 0, -2500, -5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5000, -2500, 0, 2500, 5000])), list_node([5000, 2500, 0, -2500, -5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25])), list_node([25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25])), list_node([25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20])), list_node([-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20])), list_node([-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5000])), list_node([-5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5000])), list_node([-5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, 2500, 0, -2500, -5000, 5000, 2500, 0, -2500, -5000])), list_node([-5000, -2500, 0, 2500, 5000, -5000, -2500, 0, 2500, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, 2500, 0, -2500, -5000, 5000, 2500, 0, -2500, -5000])), list_node([-5000, -2500, 0, 2500, 5000, -5000, -2500, 0, 2500, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10])), list_node([10, 10, 10, 9, 9, 9, 8, 8, 8, 7, 7, 7, 6, 6, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10])), list_node([10, 10, 10, 9, 9, 9, 8, 8, 8, 7, 7, 7, 6, 6, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0])), list_node([0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0])), list_node([0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39])), list_node([39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39])), list_node([39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])), list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])), list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5000, 5000, -5000, 5000, -5000, 5000])), list_node([5000, -5000, 5000, -5000, 5000, -5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5000, 5000, -5000, 5000, -5000, 5000])), list_node([5000, -5000, 5000, -5000, 5000, -5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])), list_node([10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])), list_node([10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, -2, 3, -4, 5, -6, 7, -8, 9, -10])), list_node([-10, 9, -8, 7, -6, 5, -4, 3, -2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, -2, 3, -4, 5, -6, 7, -8, 9, -10])), list_node([-10, 9, -8, 7, -6, 5, -4, 3, -2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10])), list_node([10, -10, 9, -9, 8, -8, 7, -7, 6, -6, 5, -5, 4, -4, 3, -3, 2, -2, 1, -1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10])), list_node([10, -10, 9, -9, 8, -8, 7, -7, 6, -6, 5, -5, 4, -4, 3, -3, 2, -2, 1, -1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, 4999, 4998, 4997, 4996, 4995, 4994, 4993, 4992, 4991])), list_node([4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, 4999, 4998, 4997, 4996, 4995, 4994, 4993, 4992, 4991])), list_node([4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])), list_node([-5, 5, -4, 4, -3, 3, -2, 2, -1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])), list_node([-5, 5, -4, 4, -3, 3, -2, 2, -1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])), list_node([10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])), list_node([10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, -5000, 5000, -5000, 5000, -5000, 5000, -5000, 5000, -5000])), list_node([-5000, 5000, -5000, 5000, -5000, 5000, -5000, 5000, -5000, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, -5000, 5000, -5000, 5000, -5000, 5000, -5000, 5000, -5000])), list_node([-5000, 5000, -5000, 5000, -5000, 5000, -5000, 5000, -5000, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])), list_node([21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])), list_node([21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000])), list_node([5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000])), list_node([5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])), list_node([49, 47, 45, 43, 41, 39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])), list_node([49, 47, 45, 43, 41, 39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])), list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])), list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])), list_node([100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])), list_node([100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 2000, 3000, 4000, 5000, 4000, 3000, 2000, 1000])), list_node([1000, 2000, 3000, 4000, 5000, 4000, 3000, 2000, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 2000, 3000, 4000, 5000, 4000, 3000, 2000, 1000])), list_node([1000, 2000, 3000, 4000, 5000, 4000, 3000, 2000, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-10, 9, -8, 7, -6, 5, -4, 3, -2, 1])), list_node([1, -2, 3, -4, 5, -6, 7, -8, 9, -10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-10, 9, -8, 7, -6, 5, -4, 3, -2, 1])), list_node([1, -2, 3, -4, 5, -6, 7, -8, 9, -10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 2, 2, 1, 1, 1, 3, 3, 3, 4, 4, 4])), list_node([4, 4, 4, 3, 3, 3, 1, 1, 1, 2, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 2, 2, 1, 1, 1, 3, 3, 3, 4, 4, 4])), list_node([4, 4, 4, 3, 3, 3, 1, 1, 1, 2, 2, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1])), list_node([-1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1])), list_node([-1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])), list_node([40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])), list_node([40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15])), list_node([15, 13, 11, 9, 7, 5, 3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15])), list_node([15, 13, 11, 9, 7, 5, 3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, 4999, 4998, 4997, 4996, 4995, 4994, 4993, 4992, 4991, 4990, 4989, 4988, 4987, 4986, 4985, 4984, 4983, 4982, 4981, 4980, 4979, 4978, 4977, 4976, 4975, 4974, 4973, 4972, 4971, 4970])), list_node([4970, 4971, 4972, 4973, 4974, 4975, 4976, 4977, 4978, 4979, 4980, 4981, 4982, 4983, 4984, 4985, 4986, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, 4999, 4998, 4997, 4996, 4995, 4994, 4993, 4992, 4991, 4990, 4989, 4988, 4987, 4986, 4985, 4984, 4983, 4982, 4981, 4980, 4979, 4978, 4977, 4976, 4975, 4974, 4973, 4972, 4971, 4970])), list_node([4970, 4971, 4972, 4973, 4974, 4975, 4976, 4977, 4978, 4979, 4980, 4981, 4982, 4983, 4984, 4985, 4986, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])), list_node([150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])), list_node([150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 2000, 3000, 4000, 5000, -1000, -2000, -3000, -4000, -5000])), list_node([-5000, -4000, -3000, -2000, -1000, 5000, 4000, 3000, 2000, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 2000, 3000, 4000, 5000, -1000, -2000, -3000, -4000, -5000])), list_node([-5000, -4000, -3000, -2000, -1000, 5000, 4000, 3000, 2000, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0])), list_node([0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 2, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0])), list_node([0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 2, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500])), list_node([1500, 1400, 1300, 1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500])), list_node([1500, 1400, 1300, 1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5000, 5000, -4000, 4000, -3000, 3000, -2000, 2000, -1000, 1000])), list_node([1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5000, 5000, -4000, 4000, -3000, 3000, -2000, 2000, -1000, 1000])), list_node([1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 10, 0, 20, 0, 30, 0, 40, 0, 50, 0, 60, 0, 70, 0, 80, 0, 90, 0, 100, 0])), list_node([0, 100, 0, 90, 0, 80, 0, 70, 0, 60, 0, 50, 0, 40, 0, 30, 0, 20, 0, 10, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 10, 0, 20, 0, 30, 0, 40, 0, 50, 0, 60, 0, 70, 0, 80, 0, 90, 0, 100, 0])), list_node([0, 100, 0, 90, 0, 80, 0, 70, 0, 60, 0, 50, 0, 40, 0, 30, 0, 20, 0, 10, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39])), list_node([39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39])), list_node([39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])), list_node([5, 5, 4, 4, 3, 3, 2, 2, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])), list_node([5, 5, 4, 4, 3, 3, 2, 2, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])), list_node([10, 8, 6, 4, 2, 9, 7, 5, 3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])), list_node([10, 8, 6, 4, 2, 9, 7, 5, 3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5000, 5000, -4999, 4999, -4998, 4998, -4997, 4997, -4996, 4996])), list_node([4996, -4996, 4997, -4997, 4998, -4998, 4999, -4999, 5000, -5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5000, 5000, -4999, 4999, -4998, 4998, -4997, 4997, -4996, 4996])), list_node([4996, -4996, 4997, -4997, 4998, -4998, 4999, -4999, 5000, -5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 2, 4, 6, 5, 7, 9, 8, 10])), list_node([10, 8, 9, 7, 5, 6, 4, 2, 3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 2, 4, 6, 5, 7, 9, 8, 10])), list_node([10, 8, 9, 7, 5, 6, 4, 2, 3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10])), list_node([-10, 10, -9, 9, -8, 8, -7, 7, -6, 6, -5, 5, -4, 4, -3, 3, -2, 2, -1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10])), list_node([-10, 10, -9, 9, -8, 8, -7, 7, -6, 6, -5, 5, -4, 4, -3, 3, -2, 2, -1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 2, 2, 1, 1])), list_node([1, 1, 2, 2, 3, 3, 2, 2, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 2, 2, 1, 1])), list_node([1, 1, 2, 2, 3, 3, 2, 2, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, 4000, 3000, 2000, 1000, 0, -1000, -2000, -3000, -4000, -5000])), list_node([-5000, -4000, -3000, -2000, -1000, 0, 1000, 2000, 3000, 4000, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, 4000, 3000, 2000, 1000, 0, -1000, -2000, -3000, -4000, -5000])), list_node([-5000, -4000, -3000, -2000, -1000, 0, 1000, 2000, 3000, 4000, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 2, 1])), list_node([1, 2, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 2, 1])), list_node([1, 2, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])), list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])), list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, -5, 10, -10, 15, -15, 20, -20, 25, -25, 30, -30, 35, -35, 40, -40])), list_node([-40, 40, -35, 35, -30, 30, -25, 25, -20, 20, -15, 15, -10, 10, -5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, -5, 10, -10, 15, -15, 20, -20, 25, -25, 30, -30, 35, -35, 40, -40])), list_node([-40, 40, -35, 35, -30, 30, -25, 25, -20, 20, -15, 15, -10, 10, -5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000])), list_node([2000, 1900, 1800, 1700, 1600, 1500, 1400, 1300, 1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000])), list_node([2000, 1900, 1800, 1700, 1600, 1500, 1400, 1300, 1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000])), list_node([-5000, 5000, -4000, 4000, -3000, 3000, -2000, 2000, -1000, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000])), list_node([-5000, 5000, -4000, 4000, -3000, 3000, -2000, 2000, -1000, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, 2500, 0, -2500, -5000])), list_node([-5000, -2500, 0, 2500, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, 2500, 0, -2500, -5000])), list_node([-5000, -2500, 0, 2500, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])), list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])), list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])), list_node([5, 5, 4, 4, 3, 3, 2, 2, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])), list_node([5, 5, 4, 4, 3, 3, 2, 2, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1, 0, -1, -3, -6, -12, -25, -50, -100, -200, -300, -400, -500])), list_node([-500, -400, -300, -200, -100, -50, -25, -12, -6, -3, -1, 0, 1, 3, 6, 12, 25, 50, 100, 200, 300, 400, 500]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1, 0, -1, -3, -6, -12, -25, -50, -100, -200, -300, -400, -500])), list_node([-500, -400, -300, -200, -100, -50, -25, -12, -6, -3, -1, 0, 1, 3, 6, 12, 25, 50, 100, 200, 300, 400, 500])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1])), list_node([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1])), list_node([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([49, 47, 45, 43, 41, 39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([49, 47, 45, 43, 41, 39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5000, 5000, -5000, 5000, -5000, 5000, -5000, 5000, -5000, 5000])), list_node([5000, -5000, 5000, -5000, 5000, -5000, 5000, -5000, 5000, -5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5000, 5000, -5000, 5000, -5000, 5000, -5000, 5000, -5000, 5000])), list_node([5000, -5000, 5000, -5000, 5000, -5000, 5000, -5000, 5000, -5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])), list_node([-5, 5, -4, 4, -3, 3, -2, 2, -1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])), list_node([-5, 5, -4, 4, -3, 3, -2, 2, -1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, -5000, 4000, -4000, 3000, -3000, 2000, -2000, 1000, -1000, 0])), list_node([0, -1000, 1000, -2000, 2000, -3000, 3000, -4000, 4000, -5000, 5000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, -5000, 4000, -4000, 3000, -3000, 2000, -2000, 1000, -1000, 0])), list_node([0, -1000, 1000, -2000, 2000, -3000, 3000, -4000, 4000, -5000, 5000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5])), list_node([-5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5])), list_node([-5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_list(candidate(head = list_node([5000, -5000, 0, 1000, -1000])), list_node([-1000, 1000, 0, -5000, 5000]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([5, 4, 3, 2, 1]))
    assert candidate(head = list_node([])) == None
    assert is_same_list(candidate(head = list_node([1, 2])), list_node([2, 1]))
    assert is_same_list(candidate(head = list_node([1])), list_node([1]))
    assert is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5])), list_node([-5, -4, -3, -2, -1]))
    assert is_same_list(candidate(head = list_node([3])), list_node([3]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([-1000, 0, 1000])), list_node([1000, 0, -1000]))
    assert is_same_list(candidate(head = list_node([5000, -5000, 5000, -5000])), list_node([-5000, 5000, -5000, 5000]))
    assert is_same_list(candidate(head = list_node([100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5])), list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])), list_node([21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([-5000, -4000, -3000, -2000, -1000, 0, 1000, 2000, 3000, 4000, 5000])), list_node([5000, 4000, 3000, 2000, 1000, 0, -1000, -2000, -3000, -4000, -5000]))
    assert is_same_list(candidate(head = list_node([-5000, -2500, 0, 2500, 5000])), list_node([5000, 2500, 0, -2500, -5000]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25])), list_node([25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]))
    assert is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20])), list_node([-20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]))
    assert is_same_list(candidate(head = list_node([-5000])), list_node([-5000]))
    assert is_same_list(candidate(head = list_node([5000, 2500, 0, -2500, -5000, 5000, 2500, 0, -2500, -5000])), list_node([-5000, -2500, 0, 2500, 5000, -5000, -2500, 0, 2500, 5000]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10])), list_node([10, 10, 10, 9, 9, 9, 8, 8, 8, 7, 7, 7, 6, 6, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 2, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([0])), list_node([0]))
    assert is_same_list(candidate(head = list_node([25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39])), list_node([39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]))
    assert is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])), list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([-5000, 5000, -5000, 5000, -5000, 5000])), list_node([5000, -5000, 5000, -5000, 5000, -5000]))
    assert is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])), list_node([10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]))
    assert is_same_list(candidate(head = list_node([1, -2, 3, -4, 5, -6, 7, -8, 9, -10])), list_node([-10, 9, -8, 7, -6, 5, -4, 3, -2, 1]))
    assert is_same_list(candidate(head = list_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10])), list_node([10, -10, 9, -9, 8, -8, 7, -7, 6, -6, 5, -5, 4, -4, 3, -3, 2, -2, 1, -1]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([5000, 4999, 4998, 4997, 4996, 4995, 4994, 4993, 4992, 4991])), list_node([4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, 5000]))
    assert is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])), list_node([-5, 5, -4, 4, -3, 3, -2, 2, -1, 1]))
    assert is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])), list_node([10, 10, 9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]))
    assert is_same_list(candidate(head = list_node([5000, -5000, 5000, -5000, 5000, -5000, 5000, -5000, 5000, -5000])), list_node([-5000, 5000, -5000, 5000, -5000, 5000, -5000, 5000, -5000, 5000]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])), list_node([21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([5000])), list_node([5000]))
    assert is_same_list(candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])), list_node([49, 47, 45, 43, 41, 39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]))
    assert is_same_list(candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])), list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]))
    assert is_same_list(candidate(head = list_node([21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]))
    assert is_same_list(candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])), list_node([100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5]))
    assert is_same_list(candidate(head = list_node([1000, 2000, 3000, 4000, 5000, 4000, 3000, 2000, 1000])), list_node([1000, 2000, 3000, 4000, 5000, 4000, 3000, 2000, 1000]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([-10, 9, -8, 7, -6, 5, -4, 3, -2, 1])), list_node([1, -2, 3, -4, 5, -6, 7, -8, 9, -10]))
    assert is_same_list(candidate(head = list_node([2, 2, 2, 1, 1, 1, 3, 3, 3, 4, 4, 4])), list_node([4, 4, 4, 3, 3, 3, 1, 1, 1, 2, 2, 2]))
    assert is_same_list(candidate(head = list_node([-1])), list_node([-1]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]))
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])), list_node([40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]))
    assert is_same_list(candidate(head = list_node([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15])), list_node([15, 13, 11, 9, 7, 5, 3, 1]))
    assert is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]))
    assert is_same_list(candidate(head = list_node([5000, 4999, 4998, 4997, 4996, 4995, 4994, 4993, 4992, 4991, 4990, 4989, 4988, 4987, 4986, 4985, 4984, 4983, 4982, 4981, 4980, 4979, 4978, 4977, 4976, 4975, 4974, 4973, 4972, 4971, 4970])), list_node([4970, 4971, 4972, 4973, 4974, 4975, 4976, 4977, 4978, 4979, 4980, 4981, 4982, 4983, 4984, 4985, 4986, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, 5000]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])), list_node([150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10]))
    assert is_same_list(candidate(head = list_node([1000, 2000, 3000, 4000, 5000, -1000, -2000, -3000, -4000, -5000])), list_node([-5000, -4000, -3000, -2000, -1000, 5000, 4000, 3000, 2000, 1000]))
    assert is_same_list(candidate(head = list_node([1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0])), list_node([0, 10, 0, 9, 0, 8, 0, 7, 0, 6, 0, 5, 0, 4, 0, 3, 0, 2, 0, 1]))
    assert is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500])), list_node([1500, 1400, 1300, 1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([-5000, 5000, -4000, 4000, -3000, 3000, -2000, 2000, -1000, 1000])), list_node([1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000]))
    assert is_same_list(candidate(head = list_node([0, 10, 0, 20, 0, 30, 0, 40, 0, 50, 0, 60, 0, 70, 0, 80, 0, 90, 0, 100, 0])), list_node([0, 100, 0, 90, 0, 80, 0, 70, 0, 60, 0, 50, 0, 40, 0, 30, 0, 20, 0, 10, 0]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39])), list_node([39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]))
    assert is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])), list_node([5, 5, 4, 4, 3, 3, 2, 2, 1, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])), list_node([10, 8, 6, 4, 2, 9, 7, 5, 3, 1]))
    assert is_same_list(candidate(head = list_node([-5000, 5000, -4999, 4999, -4998, 4998, -4997, 4997, -4996, 4996])), list_node([4996, -4996, 4997, -4997, 4998, -4998, 4999, -4999, 5000, -5000]))
    assert is_same_list(candidate(head = list_node([1, 3, 2, 4, 6, 5, 7, 9, 8, 10])), list_node([10, 8, 9, 7, 5, 6, 4, 2, 3, 1]))
    assert is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10])), list_node([-10, 10, -9, 9, -8, 8, -7, 7, -6, 6, -5, 5, -4, 4, -3, 3, -2, 2, -1, 1]))
    assert is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 2, 2, 1, 1])), list_node([1, 1, 2, 2, 3, 3, 2, 2, 1, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([5000, 4000, 3000, 2000, 1000, 0, -1000, -2000, -3000, -4000, -5000])), list_node([-5000, -4000, -3000, -2000, -1000, 0, 1000, 2000, 3000, 4000, 5000]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 2, 1])), list_node([1, 2, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])), list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]))
    assert is_same_list(candidate(head = list_node([5, -5, 10, -10, 15, -15, 20, -20, 25, -25, 30, -30, 35, -35, 40, -40])), list_node([-40, 40, -35, 35, -30, 30, -25, 25, -20, 20, -15, 15, -10, 10, -5, 5]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000])), list_node([2000, 1900, 1800, 1700, 1600, 1500, 1400, 1300, 1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]))
    assert is_same_list(candidate(head = list_node([1000, -1000, 2000, -2000, 3000, -3000, 4000, -4000, 5000, -5000])), list_node([-5000, 5000, -4000, 4000, -3000, 3000, -2000, 2000, -1000, 1000]))
    assert is_same_list(candidate(head = list_node([5000, 2500, 0, -2500, -5000])), list_node([-5000, -2500, 0, 2500, 5000]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])), list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]))
    assert is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])), list_node([5, 5, 4, 4, 3, 3, 2, 2, 1, 1]))
    assert is_same_list(candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1, 0, -1, -3, -6, -12, -25, -50, -100, -200, -300, -400, -500])), list_node([-500, -400, -300, -200, -100, -50, -25, -12, -6, -3, -1, 0, 1, 3, 6, 12, 25, 50, 100, 200, 300, 400, 500]))
    assert is_same_list(candidate(head = list_node([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1])), list_node([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]))
    assert is_same_list(candidate(head = list_node([49, 47, 45, 43, 41, 39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]))
    assert is_same_list(candidate(head = list_node([-5000, 5000, -5000, 5000, -5000, 5000, -5000, 5000, -5000, 5000])), list_node([5000, -5000, 5000, -5000, 5000, -5000, 5000, -5000, 5000, -5000]))
    assert is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]))
    assert is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])), list_node([-5, 5, -4, 4, -3, 3, -2, 2, -1, 1]))
    assert is_same_list(candidate(head = list_node([21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([5000, -5000, 4000, -4000, 3000, -3000, 2000, -2000, 1000, -1000, 0])), list_node([0, -1000, 1000, -2000, 2000, -3000, 3000, -4000, 4000, -5000, 5000]))
    assert is_same_list(candidate(head = list_node([5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5])), list_node([-5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5]))


