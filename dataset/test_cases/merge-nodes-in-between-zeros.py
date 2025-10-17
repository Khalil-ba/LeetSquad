def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 3, 1, 0, 4, 5, 2, 0])), list_node([4, 11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 3, 1, 0, 4, 5, 2, 0])), list_node([4, 11])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 0])), list_node([15, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 0])), list_node([15, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 10, 0])), list_node([10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 10, 0])), list_node([10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 5, 6, 7, 8, 0, 9, 10, 11, 0])), list_node([26, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 5, 6, 7, 8, 0, 9, 10, 11, 0])), list_node([26, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 10, 20, 30, 0, 40, 50, 60, 0])), list_node([60, 150]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 10, 20, 30, 0, 40, 50, 60, 0])), list_node([60, 150])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 0, 4, 5, 6, 0])), list_node([6, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 0, 4, 5, 6, 0])), list_node([6, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 999, 0, 1, 2, 3, 0, 1000, 0])), list_node([999, 6, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 999, 0, 1, 2, 3, 0, 1000, 0])), list_node([999, 6, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 3, 0, 2, 2, 0])), list_node([1, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 3, 0, 2, 2, 0])), list_node([1, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 10, 0, 20, 30, 0, 40, 50, 0])), list_node([10, 50, 90]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 10, 0, 20, 30, 0, 40, 50, 0])), list_node([10, 50, 90])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 10, 20, 30, 0, 5, 5, 0, 4, 4, 4, 0])), list_node([60, 10, 12]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 10, 20, 30, 0, 5, 5, 0, 4, 4, 4, 0])), list_node([60, 10, 12])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 999, 999, 999, 0])), list_node([2997]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 999, 999, 999, 0])), list_node([2997])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0])), list_node([0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0])), list_node([0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1000, 0, 1000, 1000, 0])), list_node([1000, 2000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1000, 0, 1000, 1000, 0])), list_node([1000, 2000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1000, 0])), list_node([1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1000, 0])), list_node([1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 100, 0, 200, 0, 300, 0, 400, 0, 500, 0, 600, 0, 700, 0])), list_node([100, 200, 300, 400, 500, 600, 700]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 100, 0, 200, 0, 300, 0, 400, 0, 500, 0, 600, 0, 700, 0])), list_node([100, 200, 300, 400, 500, 600, 700])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 10, 20, 30, 40, 50, 0, 60, 70, 80, 90, 100, 0, 110, 120, 130, 0])), list_node([150, 400, 360]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 10, 20, 30, 40, 50, 0, 60, 70, 80, 90, 100, 0, 110, 120, 130, 0])), list_node([150, 400, 360])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 10, 0, 20, 0, 30, 0, 40, 0, 50, 0, 60, 0, 70, 0])), list_node([10, 20, 30, 40, 50, 60, 70]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 10, 0, 20, 0, 30, 0, 40, 0, 50, 0, 60, 0, 70, 0])), list_node([10, 20, 30, 40, 50, 60, 70])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0])), list_node([210]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0])), list_node([210])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 10, 20, 30, 40, 50, 0, 60, 70, 80, 90, 100, 0, 110, 120, 130, 0, 140, 150, 160, 170, 180, 190, 0])), list_node([150, 400, 360, 990]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 10, 20, 30, 40, 50, 0, 60, 70, 80, 90, 100, 0, 110, 120, 130, 0, 140, 150, 160, 170, 180, 190, 0])), list_node([150, 400, 360, 990])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 10, 20, 30, 40, 50, 0, 60, 70, 80, 90, 100, 0, 110, 120, 130, 140, 150, 0, 160, 170, 180, 190, 200, 0])), list_node([150, 400, 650, 900]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 10, 20, 30, 40, 50, 0, 60, 70, 80, 90, 100, 0, 110, 120, 130, 140, 150, 0, 160, 170, 180, 190, 200, 0])), list_node([150, 400, 650, 900])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 999, 1, 0, 998, 2, 0, 997, 3, 0])), list_node([1000, 1000, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 999, 1, 0, 998, 2, 0, 997, 3, 0])), list_node([1000, 1000, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 999, 1, 2, 3, 0, 456, 789, 0, 101, 202, 303, 404, 0])), list_node([1005, 1245, 1010]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 999, 1, 2, 3, 0, 456, 789, 0, 101, 202, 303, 404, 0])), list_node([1005, 1245, 1010])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 100, 200, 300, 400, 500, 0, 600, 700, 800, 900, 1000, 0])), list_node([1500, 4000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 100, 200, 300, 400, 500, 0, 600, 700, 800, 900, 1000, 0])), list_node([1500, 4000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 0, 10, 11, 12, 0, 13, 14, 15, 0, 16, 17, 18, 0, 19, 20, 21, 0])), list_node([6, 15, 24, 33, 42, 51, 60]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 0, 10, 11, 12, 0, 13, 14, 15, 0, 16, 17, 18, 0, 19, 20, 21, 0])), list_node([6, 15, 24, 33, 42, 51, 60])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])), list_node([120]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])), list_node([120])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10, 0, 11, 12, 13, 14, 0, 15, 16, 17, 0, 18, 19, 20, 0])), list_node([15, 40, 50, 48, 57]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10, 0, 11, 12, 13, 14, 0, 15, 16, 17, 0, 18, 19, 20, 0])), list_node([15, 40, 50, 48, 57])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 999, 999, 999, 999, 999, 0, 999, 999, 999, 999, 999, 0])), list_node([4995, 4995]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 999, 999, 999, 999, 999, 0, 999, 999, 999, 999, 999, 0])), list_node([4995, 4995])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0])), list_node([6, 39, 145]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0])), list_node([6, 39, 145])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 0, 10, 11, 12, 0, 13, 14, 15, 16, 17, 0, 18, 19, 20, 0])), list_node([15, 30, 33, 75, 57]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 0, 10, 11, 12, 0, 13, 14, 15, 16, 17, 0, 18, 19, 20, 0])), list_node([15, 30, 33, 75, 57])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 100, 200, 300, 400, 0, 500, 600, 700, 800, 900, 0, 1000, 0])), list_node([1000, 3500, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 100, 200, 300, 400, 0, 500, 600, 700, 800, 900, 0, 1000, 0])), list_node([1000, 3500, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 100, 200, 0, 300, 400, 500, 0, 600, 700, 800, 900, 1000, 0])), list_node([300, 1200, 4000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 100, 200, 0, 300, 400, 500, 0, 600, 700, 800, 900, 1000, 0])), list_node([300, 1200, 4000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 100, 200, 300, 400, 0, 500, 600, 700, 800, 0, 900, 1000, 0])), list_node([1000, 2600, 1900]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 100, 200, 300, 400, 0, 500, 600, 700, 800, 0, 900, 1000, 0])), list_node([1000, 2600, 1900])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 999, 0, 998, 0, 997, 0, 996, 0, 995, 0, 994, 0, 993, 0, 992, 0, 991, 0])), list_node([999, 998, 997, 996, 995, 994, 993, 992, 991]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 999, 0, 998, 0, 997, 0, 996, 0, 995, 0, 994, 0, 993, 0, 992, 0, 991, 0])), list_node([999, 998, 997, 996, 995, 994, 993, 992, 991])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 0, 10, 11, 12, 0])), list_node([6, 15, 24, 33]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 0, 10, 11, 12, 0])), list_node([6, 15, 24, 33])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 0, 3, 3, 0])), list_node([4, 10, 6]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 0, 3, 3, 0])), list_node([4, 10, 6])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0])), list_node([325]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0])), list_node([325])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 0])), list_node([5, 10, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 0])), list_node([5, 10, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 10, 10, 10, 10, 0, 10, 10, 10, 10, 0, 10, 10, 10, 10, 0])), list_node([40, 40, 40]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 10, 10, 10, 10, 0, 10, 10, 10, 10, 0, 10, 10, 10, 10, 0])), list_node([40, 40, 40])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 100, 200, 300, 400, 0, 500, 600, 700, 800, 900, 0, 1000, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])), list_node([1000, 3500, 1000, 45]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 100, 200, 300, 400, 0, 500, 600, 700, 800, 900, 0, 1000, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])), list_node([1000, 3500, 1000, 45])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([45, 55]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([45, 55])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 0, 3, 4, 5, 0, 6, 7, 8, 9, 10, 0])), list_node([3, 12, 40]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 0, 3, 4, 5, 0, 6, 7, 8, 9, 10, 0])), list_node([3, 12, 40])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 999, 0, 999, 999, 0, 999, 999, 999, 0, 999, 999, 999, 0])), list_node([999, 1998, 2997, 2997]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 999, 0, 999, 999, 0, 999, 999, 999, 0, 999, 999, 999, 0])), list_node([999, 1998, 2997, 2997])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 100, 200, 300, 0, 400, 500, 600, 0, 700, 800, 900, 0])), list_node([600, 1500, 2400]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 100, 200, 300, 0, 400, 500, 600, 0, 700, 800, 900, 0])), list_node([600, 1500, 2400])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0])), list_node([45, 145]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0])), list_node([45, 145])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 0])), list_node([45, 75]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 0])), list_node([45, 75])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 20, 21, 22, 23, 24, 25, 0])), list_node([15, 30, 145, 135]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 20, 21, 22, 23, 24, 25, 0])), list_node([15, 30, 145, 135])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 100, 200, 0, 300, 400, 500, 0, 600, 700, 0, 800, 900, 0])), list_node([300, 1200, 1300, 1700]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 100, 200, 0, 300, 400, 500, 0, 600, 700, 0, 800, 900, 0])), list_node([300, 1200, 1300, 1700])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 0, 4, 4, 4, 4, 4, 0])), list_node([5, 10, 15, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 0, 4, 4, 4, 4, 4, 0])), list_node([5, 10, 15, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 999, 1, 0, 998, 2, 0, 997, 3, 0, 996, 4, 0, 995, 5, 0])), list_node([1000, 1000, 1000, 1000, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 999, 1, 0, 998, 2, 0, 997, 3, 0, 996, 4, 0, 995, 5, 0])), list_node([1000, 1000, 1000, 1000, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 20, 21, 22, 23, 24, 25, 0, 26, 27, 28, 29, 30, 0])), list_node([45, 145, 135, 140]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 20, 21, 22, 23, 24, 25, 0, 26, 27, 28, 29, 30, 0])), list_node([45, 145, 135, 140])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([45, 45]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([45, 45])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 50, 50, 0, 100, 100, 100, 0, 150, 150, 150, 150, 0])), list_node([100, 300, 600]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 50, 50, 0, 100, 100, 100, 0, 150, 150, 150, 150, 0])), list_node([100, 300, 600])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 100, 200, 300, 0, 400, 500, 0, 600, 700, 0, 800, 900, 0, 1000, 0])), list_node([600, 900, 1300, 1700, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 100, 200, 300, 0, 400, 500, 0, 600, 700, 0, 800, 900, 0, 1000, 0])), list_node([600, 900, 1300, 1700, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 10, 0, 20, 0, 30, 0, 40, 0, 50, 0, 60, 0, 70, 0, 80, 0, 90, 0, 100, 0])), list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 10, 0, 20, 0, 30, 0, 40, 0, 50, 0, 60, 0, 70, 0, 80, 0, 90, 0, 100, 0])), list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 0])), list_node([1, 3, 6, 10, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 0])), list_node([1, 3, 6, 10, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 0, 15, 16, 17, 18, 19, 20, 0])), list_node([45, 60, 105]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 0, 15, 16, 17, 18, 19, 20, 0])), list_node([45, 60, 105])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 500, 0, 500, 0, 500, 0, 500, 0, 500, 0, 500, 0, 500, 0, 500, 0, 500, 0])), list_node([500, 500, 500, 500, 500, 500, 500, 500, 500]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 500, 0, 500, 0, 500, 0, 500, 0, 500, 0, 500, 0, 500, 0, 500, 0, 500, 0])), list_node([500, 500, 500, 500, 500, 500, 500, 500, 500])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0])), list_node([1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0])), list_node([1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0, 16, 0, 17, 0, 18, 0, 19, 0, 20, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0, 16, 0, 17, 0, 18, 0, 19, 0, 20, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 0, 4, 5, 0, 6, 7, 8, 0, 9, 10, 11, 0, 12, 13, 14, 0, 15, 16, 17, 0])), list_node([6, 9, 21, 30, 39, 48]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 0, 4, 5, 0, 6, 7, 8, 0, 9, 10, 11, 0, 12, 13, 14, 0, 15, 16, 17, 0])), list_node([6, 9, 21, 30, 39, 48])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 0, 7, 8, 9, 10, 11, 0, 12, 13, 14, 0])), list_node([21, 45, 39]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 0, 7, 8, 9, 10, 11, 0, 12, 13, 14, 0])), list_node([21, 45, 39])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 0])), list_node([25, 25, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 0])), list_node([25, 25, 25])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 250, 250, 250, 0, 750, 0, 125, 125, 125, 125, 0, 625, 625, 0])), list_node([750, 750, 500, 1250]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 250, 250, 250, 0, 750, 0, 125, 125, 125, 125, 0, 625, 625, 0])), list_node([750, 750, 500, 1250])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 100, 0, 200, 0, 300, 0, 400, 0, 500, 0, 600, 0, 700, 0, 800, 0, 900, 0, 1000, 0])), list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 100, 0, 200, 0, 300, 0, 400, 0, 500, 0, 600, 0, 700, 0, 800, 0, 900, 0, 1000, 0])), list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0])), list_node([10, 20, 30]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0])), list_node([10, 20, 30])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 50, 50, 50, 50, 0, 50, 50, 50, 50, 0, 50, 50, 50, 50, 0, 50, 50, 50, 50, 0, 50, 50, 50, 50, 0])), list_node([200, 200, 200, 200, 200]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 50, 50, 50, 50, 0, 50, 50, 50, 50, 0, 50, 50, 50, 50, 0, 50, 50, 50, 50, 0, 50, 50, 50, 50, 0])), list_node([200, 200, 200, 200, 200])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 999, 1, 0, 998, 2, 0, 997, 3, 0, 996, 4, 0])), list_node([1000, 1000, 1000, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 999, 1, 0, 998, 2, 0, 997, 3, 0, 996, 4, 0])), list_node([1000, 1000, 1000, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 10, 0])), list_node([6, 15, 34]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 10, 0])), list_node([6, 15, 34])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 50, 25, 0, 75, 100, 0, 200, 150, 0, 300, 400, 0, 500, 600, 0, 700, 800, 900, 0])), list_node([75, 175, 350, 700, 1100, 2400]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 50, 25, 0, 75, 100, 0, 200, 150, 0, 300, 400, 0, 500, 600, 0, 700, 800, 900, 0])), list_node([75, 175, 350, 700, 1100, 2400])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 999, 0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0])), list_node([999, 15, 30, 165]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 999, 0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0])), list_node([999, 15, 30, 165])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0])), list_node([55, 155]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0])), list_node([55, 155])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 100, 200, 300, 400, 0, 500, 600, 700, 800, 900, 0, 1000, 1000, 1000, 0])), list_node([1000, 3500, 3000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 100, 200, 300, 400, 0, 500, 600, 700, 800, 900, 0, 1000, 1000, 1000, 0])), list_node([1000, 3500, 3000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 100, 200, 0, 300, 400, 500, 0, 600, 700, 0])), list_node([300, 1200, 1300]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 100, 200, 0, 300, 400, 500, 0, 600, 700, 0])), list_node([300, 1200, 1300])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 2, 3, 4, 0, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 0, 16, 17, 18, 19, 20, 0])), list_node([1, 9, 35, 75, 90]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 2, 3, 4, 0, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 0, 16, 17, 18, 19, 20, 0])), list_node([1, 9, 35, 75, 90])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])), list_node([45, 45]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])), list_node([45, 45])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 100, 200, 0, 300, 400, 500, 0, 600, 700, 800, 900, 0])), list_node([300, 1200, 3000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 100, 200, 0, 300, 400, 500, 0, 600, 700, 800, 900, 0])), list_node([300, 1200, 3000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 500, 400, 300, 200, 100, 0, 900, 800, 700, 600, 500, 0, 400, 300, 200, 100, 0, 900, 800, 700, 600, 500, 0, 400, 300, 200, 100, 0])), list_node([1500, 3500, 1000, 3500, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 500, 400, 300, 200, 100, 0, 900, 800, 700, 600, 500, 0, 400, 300, 200, 100, 0, 900, 800, 700, 600, 500, 0, 400, 300, 200, 100, 0])), list_node([1500, 3500, 1000, 3500, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])), list_node([19]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])), list_node([19])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 10, 20, 0, 30, 40, 0, 50, 60, 70, 0, 80, 90, 0])), list_node([30, 70, 180, 170]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 10, 20, 0, 30, 40, 0, 50, 60, 70, 0, 80, 90, 0])), list_node([30, 70, 180, 170])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0])), list_node([0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0])), list_node([0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 0])), list_node([820]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 0])), list_node([820])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_list(candidate(head = list_node([0, 3, 1, 0, 4, 5, 2, 0])), list_node([4, 11]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 0])), list_node([15, 30]))
    assert is_same_list(candidate(head = list_node([0, 10, 0])), list_node([10]))
    assert is_same_list(candidate(head = list_node([0, 5, 6, 7, 8, 0, 9, 10, 11, 0])), list_node([26, 30]))
    assert is_same_list(candidate(head = list_node([0, 10, 20, 30, 0, 40, 50, 60, 0])), list_node([60, 150]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 0, 4, 5, 6, 0])), list_node([6, 15]))
    assert is_same_list(candidate(head = list_node([0, 999, 0, 1, 2, 3, 0, 1000, 0])), list_node([999, 6, 1000]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 3, 0, 2, 2, 0])), list_node([1, 3, 4]))
    assert is_same_list(candidate(head = list_node([0, 10, 0, 20, 30, 0, 40, 50, 0])), list_node([10, 50, 90]))
    assert is_same_list(candidate(head = list_node([0, 10, 20, 30, 0, 5, 5, 0, 4, 4, 4, 0])), list_node([60, 10, 12]))
    assert is_same_list(candidate(head = list_node([0, 999, 999, 999, 0])), list_node([2997]))
    assert is_same_list(candidate(head = list_node([0, 0])), list_node([0]))
    assert is_same_list(candidate(head = list_node([0, 1000, 0, 1000, 1000, 0])), list_node([1000, 2000]))
    assert is_same_list(candidate(head = list_node([0, 1000, 0])), list_node([1000]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0])), list_node([1, 0, 1, 0, 1, 0, 1, 0, 1]))
    assert is_same_list(candidate(head = list_node([0, 100, 0, 200, 0, 300, 0, 400, 0, 500, 0, 600, 0, 700, 0])), list_node([100, 200, 300, 400, 500, 600, 700]))
    assert is_same_list(candidate(head = list_node([0, 10, 20, 30, 40, 50, 0, 60, 70, 80, 90, 100, 0, 110, 120, 130, 0])), list_node([150, 400, 360]))
    assert is_same_list(candidate(head = list_node([0, 10, 0, 20, 0, 30, 0, 40, 0, 50, 0, 60, 0, 70, 0])), list_node([10, 20, 30, 40, 50, 60, 70]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0])), list_node([210]))
    assert is_same_list(candidate(head = list_node([0, 10, 20, 30, 40, 50, 0, 60, 70, 80, 90, 100, 0, 110, 120, 130, 0, 140, 150, 160, 170, 180, 190, 0])), list_node([150, 400, 360, 990]))
    assert is_same_list(candidate(head = list_node([0, 10, 20, 30, 40, 50, 0, 60, 70, 80, 90, 100, 0, 110, 120, 130, 140, 150, 0, 160, 170, 180, 190, 200, 0])), list_node([150, 400, 650, 900]))
    assert is_same_list(candidate(head = list_node([0, 999, 1, 0, 998, 2, 0, 997, 3, 0])), list_node([1000, 1000, 1000]))
    assert is_same_list(candidate(head = list_node([0, 999, 1, 2, 3, 0, 456, 789, 0, 101, 202, 303, 404, 0])), list_node([1005, 1245, 1010]))
    assert is_same_list(candidate(head = list_node([0, 100, 200, 300, 400, 500, 0, 600, 700, 800, 900, 1000, 0])), list_node([1500, 4000]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 0, 10, 11, 12, 0, 13, 14, 15, 0, 16, 17, 18, 0, 19, 20, 21, 0])), list_node([6, 15, 24, 33, 42, 51, 60]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])), list_node([120]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 10, 0, 11, 12, 13, 14, 0, 15, 16, 17, 0, 18, 19, 20, 0])), list_node([15, 40, 50, 48, 57]))
    assert is_same_list(candidate(head = list_node([0, 999, 999, 999, 999, 999, 0, 999, 999, 999, 999, 999, 0])), list_node([4995, 4995]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0])), list_node([6, 39, 145]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 0, 10, 11, 12, 0, 13, 14, 15, 16, 17, 0, 18, 19, 20, 0])), list_node([15, 30, 33, 75, 57]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([0, 100, 200, 300, 400, 0, 500, 600, 700, 800, 900, 0, 1000, 0])), list_node([1000, 3500, 1000]))
    assert is_same_list(candidate(head = list_node([0, 100, 200, 0, 300, 400, 500, 0, 600, 700, 800, 900, 1000, 0])), list_node([300, 1200, 4000]))
    assert is_same_list(candidate(head = list_node([0, 100, 200, 300, 400, 0, 500, 600, 700, 800, 0, 900, 1000, 0])), list_node([1000, 2600, 1900]))
    assert is_same_list(candidate(head = list_node([0, 999, 0, 998, 0, 997, 0, 996, 0, 995, 0, 994, 0, 993, 0, 992, 0, 991, 0])), list_node([999, 998, 997, 996, 995, 994, 993, 992, 991]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 0, 10, 11, 12, 0])), list_node([6, 15, 24, 33]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([0, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 0, 3, 3, 0])), list_node([4, 10, 6]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 0])), list_node([325]))
    assert is_same_list(candidate(head = list_node([0, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 0])), list_node([5, 10, 15]))
    assert is_same_list(candidate(head = list_node([0, 10, 10, 10, 10, 0, 10, 10, 10, 10, 0, 10, 10, 10, 10, 0])), list_node([40, 40, 40]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([0, 100, 200, 300, 400, 0, 500, 600, 700, 800, 900, 0, 1000, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])), list_node([1000, 3500, 1000, 45]))
    assert is_same_list(candidate(head = list_node([0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([45, 55]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 0, 3, 4, 5, 0, 6, 7, 8, 9, 10, 0])), list_node([3, 12, 40]))
    assert is_same_list(candidate(head = list_node([0, 999, 0, 999, 999, 0, 999, 999, 999, 0, 999, 999, 999, 0])), list_node([999, 1998, 2997, 2997]))
    assert is_same_list(candidate(head = list_node([0, 100, 200, 300, 0, 400, 500, 600, 0, 700, 800, 900, 0])), list_node([600, 1500, 2400]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0])), list_node([45, 145]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 0])), list_node([45, 75]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 20, 21, 22, 23, 24, 25, 0])), list_node([15, 30, 145, 135]))
    assert is_same_list(candidate(head = list_node([0, 100, 200, 0, 300, 400, 500, 0, 600, 700, 0, 800, 900, 0])), list_node([300, 1200, 1300, 1700]))
    assert is_same_list(candidate(head = list_node([0, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 0, 4, 4, 4, 4, 4, 0])), list_node([5, 10, 15, 20]))
    assert is_same_list(candidate(head = list_node([0, 999, 1, 0, 998, 2, 0, 997, 3, 0, 996, 4, 0, 995, 5, 0])), list_node([1000, 1000, 1000, 1000, 1000]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 20, 21, 22, 23, 24, 25, 0, 26, 27, 28, 29, 30, 0])), list_node([45, 145, 135, 140]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])), list_node([45, 45]))
    assert is_same_list(candidate(head = list_node([0, 50, 50, 0, 100, 100, 100, 0, 150, 150, 150, 150, 0])), list_node([100, 300, 600]))
    assert is_same_list(candidate(head = list_node([0, 100, 200, 300, 0, 400, 500, 0, 600, 700, 0, 800, 900, 0, 1000, 0])), list_node([600, 900, 1300, 1700, 1000]))
    assert is_same_list(candidate(head = list_node([0, 10, 0, 20, 0, 30, 0, 40, 0, 50, 0, 60, 0, 70, 0, 80, 0, 90, 0, 100, 0])), list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 0])), list_node([1, 3, 6, 10, 15]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 0, 15, 16, 17, 18, 19, 20, 0])), list_node([45, 60, 105]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([0, 500, 0, 500, 0, 500, 0, 500, 0, 500, 0, 500, 0, 500, 0, 500, 0, 500, 0])), list_node([500, 500, 500, 500, 500, 500, 500, 500, 500]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0])), list_node([1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0, 16, 0, 17, 0, 18, 0, 19, 0, 20, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 0, 4, 5, 0, 6, 7, 8, 0, 9, 10, 11, 0, 12, 13, 14, 0, 15, 16, 17, 0])), list_node([6, 9, 21, 30, 39, 48]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 0, 7, 8, 9, 10, 11, 0, 12, 13, 14, 0])), list_node([21, 45, 39]))
    assert is_same_list(candidate(head = list_node([0, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 0])), list_node([25, 25, 25]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([0, 250, 250, 250, 0, 750, 0, 125, 125, 125, 125, 0, 625, 625, 0])), list_node([750, 750, 500, 1250]))
    assert is_same_list(candidate(head = list_node([0, 100, 0, 200, 0, 300, 0, 400, 0, 500, 0, 600, 0, 700, 0, 800, 0, 900, 0, 1000, 0])), list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]))
    assert is_same_list(candidate(head = list_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0])), list_node([10, 20, 30]))
    assert is_same_list(candidate(head = list_node([0, 50, 50, 50, 50, 0, 50, 50, 50, 50, 0, 50, 50, 50, 50, 0, 50, 50, 50, 50, 0, 50, 50, 50, 50, 0])), list_node([200, 200, 200, 200, 200]))
    assert is_same_list(candidate(head = list_node([0, 999, 1, 0, 998, 2, 0, 997, 3, 0, 996, 4, 0])), list_node([1000, 1000, 1000, 1000]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 9, 10, 0])), list_node([6, 15, 34]))
    assert is_same_list(candidate(head = list_node([0, 50, 25, 0, 75, 100, 0, 200, 150, 0, 300, 400, 0, 500, 600, 0, 700, 800, 900, 0])), list_node([75, 175, 350, 700, 1100, 2400]))
    assert is_same_list(candidate(head = list_node([0, 999, 0, 1, 2, 3, 4, 5, 0, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0])), list_node([999, 15, 30, 165]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0])), list_node([55, 155]))
    assert is_same_list(candidate(head = list_node([0, 100, 200, 300, 400, 0, 500, 600, 700, 800, 900, 0, 1000, 1000, 1000, 0])), list_node([1000, 3500, 3000]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0])), list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0, 5, 0])), list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]))
    assert is_same_list(candidate(head = list_node([0, 100, 200, 0, 300, 400, 500, 0, 600, 700, 0])), list_node([300, 1200, 1300]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 2, 3, 4, 0, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13, 14, 15, 0, 16, 17, 18, 19, 20, 0])), list_node([1, 9, 35, 75, 90]))
    assert is_same_list(candidate(head = list_node([0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0])), list_node([45, 45]))
    assert is_same_list(candidate(head = list_node([0, 100, 200, 0, 300, 400, 500, 0, 600, 700, 800, 900, 0])), list_node([300, 1200, 3000]))
    assert is_same_list(candidate(head = list_node([0, 500, 400, 300, 200, 100, 0, 900, 800, 700, 600, 500, 0, 400, 300, 200, 100, 0, 900, 800, 700, 600, 500, 0, 400, 300, 200, 100, 0])), list_node([1500, 3500, 1000, 3500, 1000]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])), list_node([19]))
    assert is_same_list(candidate(head = list_node([0, 10, 20, 0, 30, 40, 0, 50, 60, 70, 0, 80, 90, 0])), list_node([30, 70, 180, 170]))
    assert is_same_list(candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])), list_node([1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0])), list_node([0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 0])), list_node([820]))


