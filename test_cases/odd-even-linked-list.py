def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3])), list_node([1, 3, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3])), list_node([1, 3, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90])), list_node([10, 30, 50, 70, 90, 20, 40, 60, 80]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90])), list_node([10, 30, 50, 70, 90, 20, 40, 60, 80])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 1, 3, 5, 6, 4, 7])), list_node([2, 3, 6, 7, 1, 5, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 1, 3, 5, 6, 4, 7])), list_node([2, 3, 6, 7, 1, 5, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0])), list_node([0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0])), list_node([0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, 0, 1, -2, 2, -3, 3])), list_node([-1, 1, 2, 3, 0, -2, -3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, 0, 1, -2, 2, -3, 3])), list_node([-1, 1, 2, 3, 0, -2, -3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 3, 5, 2, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 3, 5, 2, 4])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2])), list_node([1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2])), list_node([1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1])), list_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1])), list_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4])), list_node([1, 3, 2, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4])), list_node([1, 3, 2, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6])), list_node([1, 3, 5, 2, 4, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6])), list_node([1, 3, 5, 2, 4, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])), list_node([1, 5, 9, 4, 8, 3, 7, 2, 6, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])), list_node([1, 5, 9, 4, 8, 3, 7, 2, 6, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([5, 3, 1, 4, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([5, 3, 1, 4, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59])), list_node([1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59])), list_node([1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 3, 8, 6, 2, 4, 7, 1, 9])), list_node([5, 8, 2, 7, 9, 3, 6, 4, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 3, 8, 6, 2, 4, 7, 1, 9])), list_node([5, 8, 2, 7, 9, 3, 6, 4, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 3, 1, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14])), list_node([2, 1, 4, 6, 8, 10, 12, 14, 3, 5, 7, 9, 11, 13, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 3, 1, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14])), list_node([2, 1, 4, 6, 8, 10, 12, 14, 3, 5, 7, 9, 11, 13, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110, -120, -130, -140, -150])), list_node([-10, -30, -50, -70, -90, -110, -130, -150, -20, -40, -60, -80, -100, -120, -140]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110, -120, -130, -140, -150])), list_node([-10, -30, -50, -70, -90, -110, -130, -150, -20, -40, -60, -80, -100, -120, -140])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 11, 10, 11, 10, 11, 10, 11, 10, 11, 10, 11, 10, 11, 10, 11, 10, 11, 10, 11])), list_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 11, 10, 11, 10, 11, 10, 11, 10, 11, 10, 11, 10, 11, 10, 11, 10, 11, 10, 11])), list_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30])), list_node([-1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -25, -27, -29, -2, -4, -6, -8, -10, -12, -14, -16, -18, -20, -22, -24, -26, -28, -30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30])), list_node([-1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -25, -27, -29, -2, -4, -6, -8, -10, -12, -14, -16, -18, -20, -22, -24, -26, -28, -30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])), list_node([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])), list_node([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])), list_node([1, 2, 3, 4, 4, 5, 5, 5, 2, 3, 3, 4, 4, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])), list_node([1, 2, 3, 4, 4, 5, 5, 5, 2, 3, 3, 4, 4, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 3, 8, 6, 2, 4, 7, 1, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([5, 8, 2, 7, 9, 11, 13, 15, 17, 19, 3, 6, 4, 1, 10, 12, 14, 16, 18, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 3, 8, 6, 2, 4, 7, 1, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([5, 8, 2, 7, 9, 11, 13, 15, 17, 19, 3, 6, 4, 1, 10, 12, 14, 16, 18, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11])), list_node([5, 3, 1, 9, 7, 15, 13, 11, 4, 2, 10, 8, 6, 14, 12]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11])), list_node([5, 3, 1, 9, 7, 15, 13, 11, 4, 2, 10, 8, 6, 14, 12])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 21, 32, 43, 54, 65, 76, 87, 98, 109])), list_node([10, 32, 54, 76, 98, 21, 43, 65, 87, 109]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 21, 32, 43, 54, 65, 76, 87, 98, 109])), list_node([10, 32, 54, 76, 98, 21, 43, 65, 87, 109])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39])), list_node([1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 3, 7, 11, 15, 19, 23, 27, 31, 35, 39]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39])), list_node([1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 3, 7, 11, 15, 19, 23, 27, 31, 35, 39])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([999999, -999999, 999998, -999998, 999997, -999997, 999996, -999996])), list_node([999999, 999998, 999997, 999996, -999999, -999998, -999997, -999996]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([999999, -999999, 999998, -999998, 999997, -999997, 999996, -999996])), list_node([999999, 999998, 999997, 999996, -999999, -999998, -999997, -999996])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000000, -1000000, 500000, -500000, 250000, -250000, 125000, -125000])), list_node([1000000, 500000, 250000, 125000, -1000000, -500000, -250000, -125000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000000, -1000000, 500000, -500000, 250000, -250000, 125000, -125000])), list_node([1000000, 500000, 250000, 125000, -1000000, -500000, -250000, -125000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])), list_node([10, 30, 50, 70, 90, 110, 20, 40, 60, 80, 100, 120]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])), list_node([10, 30, 50, 70, 90, 110, 20, 40, 60, 80, 100, 120])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])), list_node([1, 2, 3, 4, 5, 10, 9, 8, 7, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])), list_node([1, 2, 3, 4, 5, 10, 9, 8, 7, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([999999, -999999, 999998, -999998, 999997, -999997, 999996, -999996, 999995, -999995, 999994, -999994, 999993, -999993, 999992, -999992, 999991, -999991, 999990, -999990])), list_node([999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990, -999999, -999998, -999997, -999996, -999995, -999994, -999993, -999992, -999991, -999990]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([999999, -999999, 999998, -999998, 999997, -999997, 999996, -999996, 999995, -999995, 999994, -999994, 999993, -999993, 999992, -999992, 999991, -999991, 999990, -999990])), list_node([999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990, -999999, -999998, -999997, -999996, -999995, -999994, -999993, -999992, -999991, -999990])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 8, 6, 4, 2, 9, 7, 5, 3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 8, 6, 4, 2, 9, 7, 5, 3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100000, -100000, 100000, -100000, 100000, -100000])), list_node([100000, 100000, 100000, -100000, -100000, -100000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100000, -100000, 100000, -100000, 100000, -100000])), list_node([100000, 100000, 100000, -100000, -100000, -100000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10000, -10000, 5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312, 156, -156, 78, -78, 39, -39, 19, -19])), list_node([10000, 5000, 2500, 1250, 625, 312, 156, 78, 39, 19, -10000, -5000, -2500, -1250, -625, -312, -156, -78, -39, -19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10000, -10000, 5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312, 156, -156, 78, -78, 39, -39, 19, -19])), list_node([10000, 5000, 2500, 1250, 625, 312, 156, 78, 39, 19, -10000, -5000, -2500, -1250, -625, -312, -156, -78, -39, -19])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])), list_node([-5, -3, -1, 1, 3, 5, -4, -2, 0, 2, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])), list_node([-5, -3, -1, 1, 3, 5, -4, -2, 0, 2, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])), list_node([1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])), list_node([1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])), list_node([1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])), list_node([1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 12, 14, 16, 18, 20])), list_node([1, 5, 9, 4, 8, 11, 15, 19, 14, 18, 3, 7, 2, 6, 10, 13, 17, 12, 16, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 12, 14, 16, 18, 20])), list_node([1, 5, 9, 4, 8, 11, 15, 19, 14, 18, 3, 7, 2, 6, 10, 13, 17, 12, 16, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 21, 32, 43, 54, 65, 76, 87, 98, 109, 110])), list_node([10, 32, 54, 76, 98, 110, 21, 43, 65, 87, 109]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 21, 32, 43, 54, 65, 76, 87, 98, 109, 110])), list_node([10, 32, 54, 76, 98, 110, 21, 43, 65, 87, 109])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-1, -3, -5, -7, -9, -2, -4, -6, -8, -10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-1, -3, -5, -7, -9, -2, -4, -6, -8, -10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])), list_node([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])), list_node([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4])), list_node([1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4])), list_node([1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 2, 4, 5, 7, 6, 9, 8, 11, 10])), list_node([1, 2, 5, 6, 8, 10, 3, 4, 7, 9, 11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 2, 4, 5, 7, 6, 9, 8, 11, 10])), list_node([1, 2, 5, 6, 8, 10, 3, 4, 7, 9, 11])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, -200, 300, 0, 500, 600, -700, 800, 900, 1000])), list_node([100, 300, 500, -700, 900, -200, 0, 600, 800, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, -200, 300, 0, 500, 600, -700, 800, 900, 1000])), list_node([100, 300, 500, -700, 900, -200, 0, 600, 800, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000000, -1000000, 2000000, -2000000, 3000000, -3000000])), list_node([1000000, 2000000, 3000000, -1000000, -2000000, -3000000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000000, -1000000, 2000000, -2000000, 3000000, -3000000])), list_node([1000000, 2000000, 3000000, -1000000, -2000000, -3000000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9])), list_node([9, 7, 5, 3, 1, -1, -3, -5, -7, -9, 8, 6, 4, 2, 0, -2, -4, -6, -8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9])), list_node([9, 7, 5, 3, 1, -1, -3, -5, -7, -9, 8, 6, 4, 2, 0, -2, -4, -6, -8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, -200, 300, -400, 500, -600, 700, -800, 900, -1000])), list_node([100, 300, 500, 700, 900, -200, -400, -600, -800, -1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, -200, 300, -400, 500, -600, 700, -800, 900, -1000])), list_node([100, 300, 500, 700, 900, -200, -400, -600, -800, -1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])), list_node([-1, -3, -5, -7, -9, -11, -13, -15, -2, -4, -6, -8, -10, -12, -14]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])), list_node([-1, -3, -5, -7, -9, -11, -13, -15, -2, -4, -6, -8, -10, -12, -14])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 3, 1, 4, 2, 6, 8, 7, 9, 11, 13, 10, 12, 14, 15])), list_node([5, 1, 2, 8, 9, 13, 12, 15, 3, 4, 6, 7, 11, 10, 14]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 3, 1, 4, 2, 6, 8, 7, 9, 11, 13, 10, 12, 14, 15])), list_node([5, 1, 2, 8, 9, 13, 12, 15, 3, 4, 6, 7, 11, 10, 14])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])), list_node([100, 300, 500, 700, 900, 200, 400, 600, 800, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])), list_node([100, 300, 500, 700, 900, 200, 400, 600, 800, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210])), list_node([10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210])), list_node([10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])), list_node([10, 30, 50, 70, 90, 110, 130, 150, 20, 40, 60, 80, 100, 120, 140]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])), list_node([10, 30, 50, 70, 90, 110, 130, 150, 20, 40, 60, 80, 100, 120, 140])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([999999, -999999, 999999, -999999, 999999, -999999, 999999, -999999, 999999, -999999, 999999, -999999])), list_node([999999, 999999, 999999, 999999, 999999, 999999, -999999, -999999, -999999, -999999, -999999, -999999]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([999999, -999999, 999999, -999999, 999999, -999999, 999999, -999999, 999999, -999999, 999999, -999999])), list_node([999999, 999999, 999999, 999999, 999999, 999999, -999999, -999999, -999999, -999999, -999999, -999999])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 1, 3, 5, 7, 9])), list_node([2, 6, 10, 3, 7, 4, 8, 1, 5, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 1, 3, 5, 7, 9])), list_node([2, 6, 10, 3, 7, 4, 8, 1, 5, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])), list_node([1, 5, 9, 13, 17, 2, 6, 10, 14, 18, 3, 7, 11, 15, 19, 4, 8, 12, 16, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])), list_node([1, 5, 9, 13, 17, 2, 6, 10, 14, 18, 3, 7, 11, 15, 19, 4, 8, 12, 16, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])), list_node([2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])), list_node([2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])), list_node([5, 3, 1, -1, -3, -5, 4, 2, 0, -2, -4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])), list_node([5, 3, 1, -1, -3, -5, 4, 2, 0, -2, -4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991])), list_node([100000, 99998, 99996, 99994, 99992, 99999, 99997, 99995, 99993, 99991]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991])), list_node([100000, 99998, 99996, 99994, 99992, 99999, 99997, 99995, 99993, 99991])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])), list_node([10, 30, 50, 70, 90, 110, 20, 40, 60, 80, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])), list_node([10, 30, 50, 70, 90, 110, 20, 40, 60, 80, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1])), list_node([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1])), list_node([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([9, 7, 5, 3, 1, 8, 6, 4, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([9, 7, 5, 3, 1, 8, 6, 4, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000000, -1000000, 500000, -500000, 250000, -250000, 125000, -125000, 62500, -62500])), list_node([1000000, 500000, 250000, 125000, 62500, -1000000, -500000, -250000, -125000, -62500]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000000, -1000000, 500000, -500000, 250000, -250000, 125000, -125000, 62500, -62500])), list_node([1000000, 500000, 250000, 125000, 62500, -1000000, -500000, -250000, -125000, -62500])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100000, -100000, 50000, -50000, 25000, -25000, 12500, -12500])), list_node([100000, 50000, 25000, 12500, -100000, -50000, -25000, -12500]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100000, -100000, 50000, -50000, 25000, -25000, 12500, -12500])), list_node([100000, 50000, 25000, 12500, -100000, -50000, -25000, -12500])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3])), list_node([1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 2, 2, 2, 3, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3])), list_node([1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 2, 2, 2, 3, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_list(candidate(head = list_node([1, 2, 3])), list_node([1, 3, 2]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90])), list_node([10, 30, 50, 70, 90, 20, 40, 60, 80]))
    assert is_same_list(candidate(head = list_node([2, 1, 3, 5, 6, 4, 7])), list_node([2, 3, 6, 7, 1, 5, 4]))
    assert is_same_list(candidate(head = list_node([0])), list_node([0]))
    assert is_same_list(candidate(head = list_node([-1, 0, 1, -2, 2, -3, 3])), list_node([-1, 1, 2, 3, 0, -2, -3]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 3, 5, 2, 4]))
    assert candidate(head = list_node([])) == None
    assert is_same_list(candidate(head = list_node([1, 2])), list_node([1, 2]))
    assert is_same_list(candidate(head = list_node([1])), list_node([1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4])), list_node([1, 3, 2, 4]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6])), list_node([1, 3, 5, 2, 4, 6]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])), list_node([1, 5, 9, 4, 8, 3, 7, 2, 6, 10]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([5, 3, 1, 4, 2]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59])), list_node([1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59]))
    assert is_same_list(candidate(head = list_node([5, 3, 8, 6, 2, 4, 7, 1, 9])), list_node([5, 8, 2, 7, 9, 3, 6, 4, 1]))
    assert is_same_list(candidate(head = list_node([2, 3, 1, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14])), list_node([2, 1, 4, 6, 8, 10, 12, 14, 3, 5, 7, 9, 11, 13, 15]))
    assert is_same_list(candidate(head = list_node([-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110, -120, -130, -140, -150])), list_node([-10, -30, -50, -70, -90, -110, -130, -150, -20, -40, -60, -80, -100, -120, -140]))
    assert is_same_list(candidate(head = list_node([10, 11, 10, 11, 10, 11, 10, 11, 10, 11, 10, 11, 10, 11, 10, 11, 10, 11, 10, 11])), list_node([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]))
    assert is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30])), list_node([-1, -3, -5, -7, -9, -11, -13, -15, -17, -19, -21, -23, -25, -27, -29, -2, -4, -6, -8, -10, -12, -14, -16, -18, -20, -22, -24, -26, -28, -30]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])), list_node([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])), list_node([1, 2, 3, 4, 4, 5, 5, 5, 2, 3, 3, 4, 4, 5, 5]))
    assert is_same_list(candidate(head = list_node([5, 3, 8, 6, 2, 4, 7, 1, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([5, 8, 2, 7, 9, 11, 13, 15, 17, 19, 3, 6, 4, 1, 10, 12, 14, 16, 18, 20]))
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11])), list_node([5, 3, 1, 9, 7, 15, 13, 11, 4, 2, 10, 8, 6, 14, 12]))
    assert is_same_list(candidate(head = list_node([10, 21, 32, 43, 54, 65, 76, 87, 98, 109])), list_node([10, 32, 54, 76, 98, 21, 43, 65, 87, 109]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39])), list_node([1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 3, 7, 11, 15, 19, 23, 27, 31, 35, 39]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([999999, -999999, 999998, -999998, 999997, -999997, 999996, -999996])), list_node([999999, 999998, 999997, 999996, -999999, -999998, -999997, -999996]))
    assert is_same_list(candidate(head = list_node([1000000, -1000000, 500000, -500000, 250000, -250000, 125000, -125000])), list_node([1000000, 500000, 250000, 125000, -1000000, -500000, -250000, -125000]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])), list_node([10, 30, 50, 70, 90, 110, 20, 40, 60, 80, 100, 120]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
    assert is_same_list(candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])), list_node([1, 2, 3, 4, 5, 10, 9, 8, 7, 6]))
    assert is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([999999, -999999, 999998, -999998, 999997, -999997, 999996, -999996, 999995, -999995, 999994, -999994, 999993, -999993, 999992, -999992, 999991, -999991, 999990, -999990])), list_node([999999, 999998, 999997, 999996, 999995, 999994, 999993, 999992, 999991, 999990, -999999, -999998, -999997, -999996, -999995, -999994, -999993, -999992, -999991, -999990]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([10, 8, 6, 4, 2, 9, 7, 5, 3, 1]))
    assert is_same_list(candidate(head = list_node([100000, -100000, 100000, -100000, 100000, -100000])), list_node([100000, 100000, 100000, -100000, -100000, -100000]))
    assert is_same_list(candidate(head = list_node([10000, -10000, 5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312, 156, -156, 78, -78, 39, -39, 19, -19])), list_node([10000, 5000, 2500, 1250, 625, 312, 156, 78, 39, 19, -10000, -5000, -2500, -1250, -625, -312, -156, -78, -39, -19]))
    assert is_same_list(candidate(head = list_node([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])), list_node([-5, -3, -1, 1, 3, 5, -4, -2, 0, 2, 4]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])), list_node([1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])), list_node([1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 12, 14, 16, 18, 20])), list_node([1, 5, 9, 4, 8, 11, 15, 19, 14, 18, 3, 7, 2, 6, 10, 13, 17, 12, 16, 20]))
    assert is_same_list(candidate(head = list_node([10, 21, 32, 43, 54, 65, 76, 87, 98, 109, 110])), list_node([10, 32, 54, 76, 98, 110, 21, 43, 65, 87, 109]))
    assert is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-1, -3, -5, -7, -9, -2, -4, -6, -8, -10]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])), list_node([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4])), list_node([1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 1, 1, 2, 2, 2, 3, 3, 4, 4, 4]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([1, 3, 2, 4, 5, 7, 6, 9, 8, 11, 10])), list_node([1, 2, 5, 6, 8, 10, 3, 4, 7, 9, 11]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([100, -200, 300, 0, 500, 600, -700, 800, 900, 1000])), list_node([100, 300, 500, -700, 900, -200, 0, 600, 800, 1000]))
    assert is_same_list(candidate(head = list_node([1000000, -1000000, 2000000, -2000000, 3000000, -3000000])), list_node([1000000, 2000000, 3000000, -1000000, -2000000, -3000000]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]))
    assert is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9])), list_node([9, 7, 5, 3, 1, -1, -3, -5, -7, -9, 8, 6, 4, 2, 0, -2, -4, -6, -8]))
    assert is_same_list(candidate(head = list_node([100, -200, 300, -400, 500, -600, 700, -800, 900, -1000])), list_node([100, 300, 500, 700, 900, -200, -400, -600, -800, -1000]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15])), list_node([-1, -3, -5, -7, -9, -11, -13, -15, -2, -4, -6, -8, -10, -12, -14]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14]))
    assert is_same_list(candidate(head = list_node([5, 3, 1, 4, 2, 6, 8, 7, 9, 11, 13, 10, 12, 14, 15])), list_node([5, 1, 2, 8, 9, 13, 12, 15, 3, 4, 6, 7, 11, 10, 14]))
    assert is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])), list_node([100, 300, 500, 700, 900, 200, 400, 600, 800, 1000]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([10, 8, 6, 4, 2, 0, -2, -4, -6, -8, -10, 9, 7, 5, 3, 1, -1, -3, -5, -7, -9]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210])), list_node([10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])), list_node([10, 30, 50, 70, 90, 110, 130, 150, 20, 40, 60, 80, 100, 120, 140]))
    assert is_same_list(candidate(head = list_node([1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]))
    assert is_same_list(candidate(head = list_node([999999, -999999, 999999, -999999, 999999, -999999, 999999, -999999, 999999, -999999, 999999, -999999])), list_node([999999, 999999, 999999, 999999, 999999, 999999, -999999, -999999, -999999, -999999, -999999, -999999]))
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 1, 3, 5, 7, 9])), list_node([2, 6, 10, 3, 7, 4, 8, 1, 5, 9]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])), list_node([1, 5, 9, 13, 17, 2, 6, 10, 14, 18, 3, 7, 11, 15, 19, 4, 8, 12, 16, 20]))
    assert is_same_list(candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])), list_node([2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])), list_node([5, 3, 1, -1, -3, -5, 4, 2, 0, -2, -4]))
    assert is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991])), list_node([100000, 99998, 99996, 99994, 99992, 99999, 99997, 99995, 99993, 99991]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])), list_node([10, 30, 50, 70, 90, 110, 20, 40, 60, 80, 100]))
    assert is_same_list(candidate(head = list_node([1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1])), list_node([1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]))
    assert is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([9, 7, 5, 3, 1, 8, 6, 4, 2]))
    assert is_same_list(candidate(head = list_node([1000000, -1000000, 500000, -500000, 250000, -250000, 125000, -125000, 62500, -62500])), list_node([1000000, 500000, 250000, 125000, 62500, -1000000, -500000, -250000, -125000, -62500]))
    assert is_same_list(candidate(head = list_node([100000, -100000, 50000, -50000, 25000, -25000, 12500, -12500])), list_node([100000, 50000, 25000, 12500, -100000, -50000, -25000, -12500]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3])), list_node([1, 1, 1, 2, 2, 3, 3, 3, 1, 1, 2, 2, 2, 3, 3]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]))


