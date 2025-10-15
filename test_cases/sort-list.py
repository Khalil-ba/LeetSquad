def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])), list_node([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])), list_node([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0])), list_node([0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0])), list_node([0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, 5, 3, 4, 0])), list_node([-1, 0, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, 5, 3, 4, 0])), list_node([-1, 0, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([])) == None
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([])) == None: {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1])), list_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1])), list_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100000, -100000, 0, 50000, -50000])), list_node([-100000, -50000, 0, 50000, 100000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100000, -100000, 0, 50000, -50000])), list_node([-100000, -50000, 0, 50000, 100000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, -10, 20, -20, 30, -30])), list_node([-30, -20, -10, 10, 20, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, -10, 20, -20, 30, -30])), list_node([-30, -20, -10, 10, 20, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100000, 100000, -100000, 100000])), list_node([-100000, -100000, 100000, 100000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100000, 100000, -100000, 100000])), list_node([-100000, -100000, 100000, 100000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100000, -100000, 0])), list_node([-100000, 0, 100000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100000, -100000, 0])), list_node([-100000, 0, 100000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([4, 2, 1, 3])), list_node([1, 2, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([4, 2, 1, 3])), list_node([1, 2, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5])), list_node([5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5])), list_node([5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10])), list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10])), list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([25000, 25001, 25002, 25003, 25004, 25005, 25006, 25007, 25008, 25009, 25010, 25011, 25012, 25013, 25014])), list_node([25000, 25001, 25002, 25003, 25004, 25005, 25006, 25007, 25008, 25009, 25010, 25011, 25012, 25013, 25014]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([25000, 25001, 25002, 25003, 25004, 25005, 25006, 25007, 25008, 25009, 25010, 25011, 25012, 25013, 25014])), list_node([25000, 25001, 25002, 25003, 25004, 25005, 25006, 25007, 25008, 25009, 25010, 25011, 25012, 25013, 25014])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31, 15, 7, 3, 1])), list_node([1, 3, 7, 15, 31, 62, 125, 250, 500, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31, 15, 7, 3, 1])), list_node([1, 3, 7, 15, 31, 62, 125, 250, 500, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 1, 9, 3, 7, 2, 8, 6, 4, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 1, 9, 3, 7, 2, 8, 6, 4, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 3, 1, 4, 2, 7, 6, 9, 8, 10, 0, -1, -2, -3, -4, -5])), list_node([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 3, 1, 4, 2, 7, 6, 9, 8, 10, 0, -1, -2, -3, -4, -5])), list_node([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 950, 850, 750, 650, 550, 450, 350, 250, 150, 50])), list_node([50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 950, 850, 750, 650, 550, 450, 350, 250, 150, 50])), list_node([50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([50000, -50000, 100000, -100000, 150000, -150000, 200000, -200000, 250000, -250000, 300000, -300000])), list_node([-300000, -250000, -200000, -150000, -100000, -50000, 50000, 100000, 150000, 200000, 250000, 300000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([50000, -50000, 100000, -100000, 150000, -150000, 200000, -200000, 250000, -250000, 300000, -300000])), list_node([-300000, -250000, -200000, -150000, -100000, -50000, 50000, 100000, 150000, 200000, 250000, 300000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 0, -10000, -20000, -30000, -40000, -50000, -60000, -70000, -80000, -90000])), list_node([-90000, -80000, -70000, -60000, -50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 0, -10000, -20000, -30000, -40000, -50000, -60000, -70000, -80000, -90000])), list_node([-90000, -80000, -70000, -60000, -50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 1, 9, 2, 8, 3, 7, 4, 6, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 1, 9, 2, 8, 3, 7, 4, 6, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 1, 4, 2, 8, 3, 7, 6, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 1, 4, 2, 8, 3, 7, 6, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000000, 100000, 10000, 1000, 100, 10, 1, 0, -1, -10, -100, -1000, -10000, -100000, -1000000])), list_node([-1000000, -100000, -10000, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 10000, 100000, 1000000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000000, 100000, 10000, 1000, 100, 10, 1, 0, -1, -10, -100, -1000, -10000, -100000, -1000000])), list_node([-1000000, -100000, -10000, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 10000, 100000, 1000000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 1, 4, 2, 8, 5, 1, 4, 2, 8])), list_node([1, 1, 2, 2, 4, 4, 5, 5, 8, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 1, 4, 2, 8, 5, 1, 4, 2, 8])), list_node([1, 1, 2, 2, 4, 4, 5, 5, 8, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991, -99990])), list_node([-99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991, -99990]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991, -99990])), list_node([-99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991, -99990])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 10, 100, 1000, 10000, 100000, -1, -10, -100, -1000, -10000, -100000])), list_node([-100000, -10000, -1000, -100, -10, -1, 1, 10, 100, 1000, 10000, 100000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 10, 100, 1000, 10000, 100000, -1, -10, -100, -1000, -10000, -100000])), list_node([-100000, -10000, -1000, -100, -10, -1, 1, 10, 100, 1000, 10000, 100000])): {e}')
    
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
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991, -99990])), list_node([-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991, -99990]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991, -99990])), list_node([-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991, -99990])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3, 1, -1, -3, -6, -12, -24, -48, -97, -195, -390, -781, -1562, -3125, -6250, -12500, -25000, -50000, -100000])), list_node([-100000, -50000, -25000, -12500, -6250, -3125, -1562, -781, -390, -195, -97, -48, -24, -12, -6, -3, -1, 1, 3, 6, 12, 24, 48, 97, 195, 390, 781, 1562, 3125, 6250, 12500, 25000, 50000, 100000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3, 1, -1, -3, -6, -12, -24, -48, -97, -195, -390, -781, -1562, -3125, -6250, -12500, -25000, -50000, -100000])), list_node([-100000, -50000, -25000, -12500, -6250, -3125, -1562, -781, -390, -195, -97, -48, -24, -12, -6, -3, -1, 1, 3, 6, 12, 24, 48, 97, 195, 390, 781, 1562, 3125, 6250, 12500, 25000, 50000, 100000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100000, 100000, -99999, 99999, -99998, 99998, -99997, 99997, -99996, 99996, -99995, 99995])), list_node([-100000, -99999, -99998, -99997, -99996, -99995, 99995, 99996, 99997, 99998, 99999, 100000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100000, 100000, -99999, 99999, -99998, 99998, -99997, 99997, -99996, 99996, -99995, 99995])), list_node([-100000, -99999, -99998, -99997, -99996, -99995, 99995, 99996, 99997, 99998, 99999, 100000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000])), list_node([100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000])), list_node([100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 1, 2, 3, 4, 5])), list_node([1, 2, 3, 4, 5, 10, 20, 30, 40, 50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 1, 2, 3, 4, 5])), list_node([1, 2, 3, 4, 5, 10, 20, 30, 40, 50])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 0, -1, 2, -2, 3, -3, 4, -4, 5])), list_node([-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 0, -1, 2, -2, 3, -3, 4, -4, 5])), list_node([-4, -3, -2, -1, 0, 1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0, -100, -200, -300, -400, -500, -600, -700, -800, -900, -1000])), list_node([-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0, -100, -200, -300, -400, -500, -600, -700, -800, -900, -1000])), list_node([-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 9, 2, 8, 3, 7, 4, 6, 5, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 9, 2, 8, 3, 7, 4, 6, 5, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990])), list_node([99990, 99991, 99992, 99993, 99994, 99995, 99996, 99997, 99998, 99999, 100000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990])), list_node([99990, 99991, 99992, 99993, 99994, 99995, 99996, 99997, 99998, 99999, 100000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 1, 9, 3, 7, 2, 8, 6, 4, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 1, 9, 3, 7, 2, 8, 6, 4, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([50000, 50001, 50002, 50003, 50004, 49999, 49998, 49997, 49996, 49995])), list_node([49995, 49996, 49997, 49998, 49999, 50000, 50001, 50002, 50003, 50004]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([50000, 50001, 50002, 50003, 50004, 49999, 49998, 49997, 49996, 49995])), list_node([49995, 49996, 49997, 49998, 49999, 50000, 50001, 50002, 50003, 50004])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9])), list_node([-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9])), list_node([-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000, 50000])), list_node([-50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000, 50000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000, 50000])), list_node([-50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000, 50000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([23, 8, 45, 78, 1, 3, 89, 4, 2, 67, 43, 90, 12, 34, 56, 78, 9, 10, 21, 11, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 34, 43, 45, 56, 67, 78, 78, 89, 90]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([23, 8, 45, 78, 1, 3, 89, 4, 2, 67, 43, 90, 12, 34, 56, 78, 9, 10, 21, 11, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 34, 43, 45, 56, 67, 78, 78, 89, 90])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9])), list_node([-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9])), list_node([-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991])), list_node([-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991])), list_node([-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 2, 9, 1, 5, 6, 3, 8, 4, 7, 1, 5, 6, 3, 8, 4, 7])), list_node([1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 2, 9, 1, 5, 6, 3, 8, 4, 7, 1, 5, 6, 3, 8, 4, 7])), list_node([1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -15])), list_node([-15, -14, -12, -10, -8, -6, -4, -2, 1, 3, 5, 7, 9, 11, 13, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -15])), list_node([-15, -14, -12, -10, -8, -6, -4, -2, 1, 3, 5, 7, 9, 11, 13, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 10, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 10, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 1, 20, 2, 30, 3, 40, 4, 50, 5, 60, 6, 70, 7, 80, 8, 90, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 1, 20, 2, 30, 3, 40, 4, 50, 5, 60, 6, 70, 7, 80, 8, 90, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8])), list_node([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8])), list_node([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991])), list_node([99991, 99992, 99993, 99994, 99995, 99996, 99997, 99998, 99999, 100000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991])), list_node([99991, 99992, 99993, 99994, 99995, 99996, 99997, 99998, 99999, 100000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10000, 1000, 100, 10, 1, 0, -1, -10, -100, -1000, -10000])), list_node([-10000, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 10000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10000, 1000, 100, 10, 1, 0, -1, -10, -100, -1000, -10000])), list_node([-10000, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 10000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990, 9989, 9988, 9987, 9986, 9985, 9984, 9983, 9982, 9981])), list_node([9981, 9982, 9983, 9984, 9985, 9986, 9987, 9988, 9989, 9990, 9991, 9992, 9993, 9994, 9995, 9996, 9997, 9998, 9999, 10000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990, 9989, 9988, 9987, 9986, 9985, 9984, 9983, 9982, 9981])), list_node([9981, 9982, 9983, 9984, 9985, 9986, 9987, 9988, 9989, 9990, 9991, 9992, 9993, 9994, 9995, 9996, 9997, 9998, 9999, 10000])): {e}')
    
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
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991])), list_node([99991, 99992, 99993, 99994, 99995, 99996, 99997, 99998, 99999, 100000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991])), list_node([99991, 99992, 99993, 99994, 99995, 99996, 99997, 99998, 99999, 100000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])), list_node([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])), list_node([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991])), list_node([-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991])), list_node([-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 25])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 25])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5])), list_node([-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5])), list_node([-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, -5, 10, -10, 15, -15, 20, -20, 25, -25, 30, -30])), list_node([-30, -25, -20, -15, -10, -5, 5, 10, 15, 20, 25, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, -5, 10, -10, 15, -15, 20, -20, 25, -25, 30, -30])), list_node([-30, -25, -20, -15, -10, -5, 5, 10, 15, 20, 25, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95])), list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95])), list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 5, 9, 13, 17, 2, 6, 10, 14, 18, 3, 7, 11, 15, 19, 4, 8, 12, 16, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 5, 9, 13, 17, 2, 6, 10, 14, 18, 3, 7, 11, 15, 19, 4, 8, 12, 16, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([9, 3, 7, 1, 5, 13, 11, 2, 6, 12, 8, 4, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([9, 3, 7, 1, 5, 13, 11, 2, 6, 12, 8, 4, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])): {e}')
    
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
    assert is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])), list_node([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0])), list_node([0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([-1, 5, 3, 4, 0])), list_node([-1, 0, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0]))
    assert candidate(head = list_node([])) == None
    assert is_same_list(candidate(head = list_node([1])), list_node([1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5])), list_node([1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([100000, -100000, 0, 50000, -50000])), list_node([-100000, -50000, 0, 50000, 100000]))
    assert is_same_list(candidate(head = list_node([10, -10, 20, -20, 30, -30])), list_node([-30, -20, -10, 10, 20, 30]))
    assert is_same_list(candidate(head = list_node([-100000, 100000, -100000, 100000])), list_node([-100000, -100000, 100000, 100000]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([100000, -100000, 0])), list_node([-100000, 0, 100000]))
    assert is_same_list(candidate(head = list_node([4, 2, 1, 3])), list_node([1, 2, 3, 4]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([5])), list_node([5]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10])), list_node([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
    assert is_same_list(candidate(head = list_node([25000, 25001, 25002, 25003, 25004, 25005, 25006, 25007, 25008, 25009, 25010, 25011, 25012, 25013, 25014])), list_node([25000, 25001, 25002, 25003, 25004, 25005, 25006, 25007, 25008, 25009, 25010, 25011, 25012, 25013, 25014]))
    assert is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31, 15, 7, 3, 1])), list_node([1, 3, 7, 15, 31, 62, 125, 250, 500, 1000]))
    assert is_same_list(candidate(head = list_node([5, 1, 9, 3, 7, 2, 8, 6, 4, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([5, 3, 1, 4, 2, 7, 6, 9, 8, 10, 0, -1, -2, -3, -4, -5])), list_node([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 950, 850, 750, 650, 550, 450, 350, 250, 150, 50])), list_node([50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]))
    assert is_same_list(candidate(head = list_node([50000, -50000, 100000, -100000, 150000, -150000, 200000, -200000, 250000, -250000, 300000, -300000])), list_node([-300000, -250000, -200000, -150000, -100000, -50000, 50000, 100000, 150000, 200000, 250000, 300000]))
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 15, 14, 13, 12, 11])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 0, -10000, -20000, -30000, -40000, -50000, -60000, -70000, -80000, -90000])), list_node([-90000, -80000, -70000, -60000, -50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]))
    assert is_same_list(candidate(head = list_node([5, 1, 9, 2, 8, 3, 7, 4, 6, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([5, 1, 4, 2, 8, 3, 7, 6, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([1000000, 100000, 10000, 1000, 100, 10, 1, 0, -1, -10, -100, -1000, -10000, -100000, -1000000])), list_node([-1000000, -100000, -10000, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 10000, 100000, 1000000]))
    assert is_same_list(candidate(head = list_node([5, 1, 4, 2, 8, 5, 1, 4, 2, 8])), list_node([1, 1, 2, 2, 4, 4, 5, 5, 8, 8]))
    assert is_same_list(candidate(head = list_node([-99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991, -99990])), list_node([-99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991, -99990]))
    assert is_same_list(candidate(head = list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
    assert is_same_list(candidate(head = list_node([1, 10, 100, 1000, 10000, 100000, -1, -10, -100, -1000, -10000, -100000])), list_node([-100000, -10000, -1000, -100, -10, -1, 1, 10, 100, 1000, 10000, 100000]))
    assert is_same_list(candidate(head = list_node([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991, -99990])), list_node([-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991, -99990]))
    assert is_same_list(candidate(head = list_node([100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3, 1, -1, -3, -6, -12, -24, -48, -97, -195, -390, -781, -1562, -3125, -6250, -12500, -25000, -50000, -100000])), list_node([-100000, -50000, -25000, -12500, -6250, -3125, -1562, -781, -390, -195, -97, -48, -24, -12, -6, -3, -1, 1, 3, 6, 12, 24, 48, 97, 195, 390, 781, 1562, 3125, 6250, 12500, 25000, 50000, 100000]))
    assert is_same_list(candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([-100000, 100000, -99999, 99999, -99998, 99998, -99997, 99997, -99996, 99996, -99995, 99995])), list_node([-100000, -99999, -99998, -99997, -99996, -99995, 99995, 99996, 99997, 99998, 99999, 100000]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49])), list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000])), list_node([100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 1, 2, 3, 4, 5])), list_node([1, 2, 3, 4, 5, 10, 20, 30, 40, 50]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
    assert is_same_list(candidate(head = list_node([1, 0, -1, 2, -2, 3, -3, 4, -4, 5])), list_node([-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0, -100, -200, -300, -400, -500, -600, -700, -800, -900, -1000])), list_node([-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]))
    assert is_same_list(candidate(head = list_node([1, 9, 2, 8, 3, 7, 4, 6, 5, 0])), list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990])), list_node([99990, 99991, 99992, 99993, 99994, 99995, 99996, 99997, 99998, 99999, 100000]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
    assert is_same_list(candidate(head = list_node([5, 1, 9, 3, 7, 2, 8, 6, 4, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([50000, 50001, 50002, 50003, 50004, 49999, 49998, 49997, 49996, 49995])), list_node([49995, 49996, 49997, 49998, 49999, 50000, 50001, 50002, 50003, 50004]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
    assert is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9])), list_node([-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([-50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000, 50000])), list_node([-50000, -40000, -30000, -20000, -10000, 0, 10000, 20000, 30000, 40000, 50000]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
    assert is_same_list(candidate(head = list_node([23, 8, 45, 78, 1, 3, 89, 4, 2, 67, 43, 90, 12, 34, 56, 78, 9, 10, 21, 11, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 34, 43, 45, 56, 67, 78, 78, 89, 90]))
    assert is_same_list(candidate(head = list_node([100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9])), list_node([-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991])), list_node([-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991]))
    assert is_same_list(candidate(head = list_node([5, 2, 9, 1, 5, 6, 3, 8, 4, 7, 1, 5, 6, 3, 8, 4, 7])), list_node([1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9]))
    assert is_same_list(candidate(head = list_node([1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -15])), list_node([-15, -14, -12, -10, -8, -6, -4, -2, 1, 3, 5, 7, 9, 11, 13, 15]))
    assert is_same_list(candidate(head = list_node([1, 3, 2, 5, 4, 7, 6, 9, 8, 10, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 26, 25, 28, 27, 30, 29])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([10, 1, 20, 2, 30, 3, 40, 4, 50, 5, 60, 6, 70, 7, 80, 8, 90, 9])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8])), list_node([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
    assert is_same_list(candidate(head = list_node([40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]))
    assert is_same_list(candidate(head = list_node([30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]))
    assert is_same_list(candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 11, 20, 12, 19, 13, 18, 14, 17, 15, 16])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991])), list_node([99991, 99992, 99993, 99994, 99995, 99996, 99997, 99998, 99999, 100000]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([10000, 1000, 100, 10, 1, 0, -1, -10, -100, -1000, -10000])), list_node([-10000, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 10000]))
    assert is_same_list(candidate(head = list_node([10000, 9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990, 9989, 9988, 9987, 9986, 9985, 9984, 9983, 9982, 9981])), list_node([9981, 9982, 9983, 9984, 9985, 9986, 9987, 9988, 9989, 9990, 9991, 9992, 9993, 9994, 9995, 9996, 9997, 9998, 9999, 10000]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991])), list_node([99991, 99992, 99993, 99994, 99995, 99996, 99997, 99998, 99999, 100000]))
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])), list_node([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991])), list_node([-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991]))
    assert is_same_list(candidate(head = list_node([2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15, 18, 17, 20, 19, 22, 21, 24, 23, 25])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))
    assert is_same_list(candidate(head = list_node([5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5, 5, -5])), list_node([-5, -5, -5, -5, -5, -5, -5, -5, -5, -5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
    assert is_same_list(candidate(head = list_node([9, 8, 7, 6, 5, 4, 3, 2, 1])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([5, -5, 10, -10, 15, -15, 20, -20, 25, -25, 30, -30])), list_node([-30, -25, -20, -15, -10, -5, 5, 10, 15, 20, 25, 30]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95])), list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]))
    assert is_same_list(candidate(head = list_node([1, 3, 5, 7, 9, 2, 4, 6, 8, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
    assert is_same_list(candidate(head = list_node([1, 5, 9, 13, 17, 2, 6, 10, 14, 18, 3, 7, 11, 15, 19, 4, 8, 12, 16, 20])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([9, 3, 7, 1, 5, 13, 11, 2, 6, 12, 8, 4, 10])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]))


