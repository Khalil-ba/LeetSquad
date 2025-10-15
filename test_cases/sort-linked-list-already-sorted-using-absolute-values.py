def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, -1, -1, 0, 0, 0, 1, 1, 1])), list_node([-1, -1, -1, 0, 0, 0, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, -1, -1, 0, 0, 0, 1, 1, 1])), list_node([-1, -1, -1, 0, 0, 0, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, -1000, 500, -500, 250, -250, 125, -125])), list_node([-125, -250, -500, -1000, 1000, 500, 250, 125]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, -1000, 500, -500, 250, -250, 125, -125])), list_node([-125, -250, -500, -1000, 1000, 500, 250, 125])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, -2, -3])), list_node([-3, -2, -1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, -2, -3])), list_node([-3, -2, -1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, -3, 3, -2, 2, -1, 1, 0])), list_node([-1, -2, -3, 5, 3, 2, 1, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, -3, 3, -2, 2, -1, 1, 0])), list_node([-1, -2, -3, 5, 3, 2, 1, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 5, 5, 5])), list_node([5, 5, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 5, 5, 5])), list_node([5, 5, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5, -5, -5, -5])), list_node([-5, -5, -5, -5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5, -5, -5, -5])), list_node([-5, -5, -5, -5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, -1000, 500, -500, 0])), list_node([-500, -1000, 1000, 500, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, -1000, 500, -500, 0])), list_node([-500, -1000, 1000, 500, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, 0, 1])), list_node([-1, 0, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, 0, 1])), list_node([-1, 0, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 2, -5, 5, 10, -10])), list_node([-10, -5, 0, 2, 5, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 2, -5, 5, 10, -10])), list_node([-10, -5, 0, 2, 5, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, -2, -3, 4, 5])), list_node([-3, -2, -1, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, -2, -3, 4, 5])), list_node([-3, -2, -1, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5000, 5000, -4999, 4999, -1, 1])), list_node([-1, -4999, -5000, 5000, 4999, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5000, 5000, -4999, 4999, -1, 1])), list_node([-1, -4999, -5000, 5000, 4999, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1])), list_node([1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1])), list_node([1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, -1, 3, -2, 4])), list_node([-2, -1, 5, 3, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, -1, 3, -2, 4])), list_node([-2, -1, 5, 3, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, -1000, 500, -500, 250, -250])), list_node([-250, -500, -1000, 1000, 500, 250]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, -1000, 500, -500, 250, -250])), list_node([-250, -500, -1000, 1000, 500, 250])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-3, 1, -2, 2])), list_node([-2, -3, 1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-3, 1, -2, 2])), list_node([-2, -3, 1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-3, -2, -1, 0, 1, 2, 3])), list_node([-1, -2, -3, 0, 1, 2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-3, -2, -1, 0, 1, 2, 3])), list_node([-1, -2, -3, 0, 1, 2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, 2, 1])), list_node([3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, 2, 1])), list_node([3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, -1, -2, -3, 1, 2, 3])), list_node([-3, -2, -1, 0, 0, 0, 1, 2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, -1, -2, -3, 1, 2, 3])), list_node([-3, -2, -1, 0, 0, 0, 1, 2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, 2])), list_node([0, 1, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, 2])), list_node([0, 1, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5])), list_node([-5, -4, -3, -2, -1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5])), list_node([-5, -4, -3, -2, -1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-3, 1, -2, 2, -1, 3])), list_node([-1, -2, -3, 1, 2, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-3, 1, -2, 2, -1, 3])), list_node([-1, -2, -3, 1, 2, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, 3, -1, 2, -4, 0])), list_node([-4, -1, 5, 3, 2, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, 3, -1, 2, -4, 0])), list_node([-4, -1, 5, 3, 2, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100, -50, 0, 50, 100])), list_node([-50, -100, 0, 50, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100, -50, 0, 50, 100])), list_node([-50, -100, 0, 50, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5, -4, 3, -2, 1])), list_node([-2, -4, 5, 3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5, -4, 3, -2, 1])), list_node([-2, -4, 5, 3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1000, 0, 1000, -500, 500])), list_node([-500, -1000, 0, 1000, 500]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1000, 0, 1000, -500, 500])), list_node([-500, -1000, 0, 1000, 500])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1000, 1000, -500, 500, 0])), list_node([-500, -1000, 1000, 500, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1000, 1000, -500, 500, 0])), list_node([-500, -1000, 1000, 500, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5000, 5000, -4999, 4999])), list_node([-4999, -5000, 5000, 4999]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5000, 5000, -4999, 4999])), list_node([-4999, -5000, 5000, 4999])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5, -3, -1, 0, 2, 4])), list_node([-1, -3, -5, 0, 2, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5, -3, -1, 0, 2, 4])), list_node([-1, -3, -5, 0, 2, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, -1, 1, 1])), list_node([-1, -1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, -1, 1, 1])), list_node([-1, -1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5000, 5000, -4500, 4500, -4000, 4000, -3500, 3500, -3000, 3000, -2500, 2500, -2000, 2000, -1500, 1500, -1000, 1000, -500, 500, -250, 250, -100, 100, -50, 50, -25, 25, -10, 10, -5, 5, -1, 1])), list_node([-1, -5, -10, -25, -50, -100, -250, -500, -1000, -1500, -2000, -2500, -3000, -3500, -4000, -4500, -5000, 5000, 4500, 4000, 3500, 3000, 2500, 2000, 1500, 1000, 500, 250, 100, 50, 25, 10, 5, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5000, 5000, -4500, 4500, -4000, 4000, -3500, 3500, -3000, 3000, -2500, 2500, -2000, 2000, -1500, 1500, -1000, 1000, -500, 500, -250, 250, -100, 100, -50, 50, -25, 25, -10, 10, -5, 5, -1, 1])), list_node([-1, -5, -10, -25, -50, -100, -250, -500, -1000, -1500, -2000, -2500, -3000, -3500, -4000, -4500, -5000, 5000, 4500, 4000, 3500, 3000, 2500, 2000, 1500, 1000, 500, 250, 100, 50, 25, 10, 5, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2000, -1500, 1000, -500, 0, 500, -1000, 1500, -2000])), list_node([-2000, -1000, -500, -1500, 2000, 1000, 0, 500, 1500]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2000, -1500, 1000, -500, 0, 500, -1000, 1500, -2000])), list_node([-2000, -1000, -500, -1500, 2000, 1000, 0, 500, 1500])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1000, -999, -998, -997, -996, -995, -994, -993, -992, -991])), list_node([-991, -992, -993, -994, -995, -996, -997, -998, -999, -1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1000, -999, -998, -997, -996, -995, -994, -993, -992, -991])), list_node([-991, -992, -993, -994, -995, -996, -997, -998, -999, -1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([500, -400, 300, -200, 100, -50, 0, 50, -100, 200, -300, 400])), list_node([-300, -100, -50, -200, -400, 500, 300, 100, 0, 50, 200, 400]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([500, -400, 300, -200, 100, -50, 0, 50, -100, 200, -300, 400])), list_node([-300, -100, -50, -200, -400, 500, 300, 100, 0, 50, 200, 400])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1])), list_node([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1])), list_node([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])), list_node([-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])), list_node([-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5])), list_node([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5])), list_node([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-3000, -2000, -1000, 0, 1000, 2000, 3000])), list_node([-1000, -2000, -3000, 0, 1000, 2000, 3000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-3000, -2000, -1000, 0, 1000, 2000, 3000])), list_node([-1000, -2000, -3000, 0, 1000, 2000, 3000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-2000, -1500, -1000, -500, 0, 500, 1000, 1500, 2000, -100, -200, -300, -400, -50, -25, -10, -5, -1, 1, 5, 10, 25, 50, 100, 200, 300, 400, 500])), list_node([-1, -5, -10, -25, -50, -400, -300, -200, -100, -500, -1000, -1500, -2000, 0, 500, 1000, 1500, 2000, 1, 5, 10, 25, 50, 100, 200, 300, 400, 500]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-2000, -1500, -1000, -500, 0, 500, 1000, 1500, 2000, -100, -200, -300, -400, -50, -25, -10, -5, -1, 1, 5, 10, 25, 50, 100, 200, 300, 400, 500])), list_node([-1, -5, -10, -25, -50, -400, -300, -200, -100, -500, -1000, -1500, -2000, 0, 500, 1000, 1500, 2000, 1, 5, 10, 25, 50, 100, 200, 300, 400, 500])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, -1, -1, 1, 1, 1, 2, 2, 2, -2, -2, -2, 3, 3, 3, -3, -3, -3])), list_node([-3, -3, -3, -2, -2, -2, -1, -1, -1, 1, 1, 1, 2, 2, 2, 3, 3, 3]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, -1, -1, 1, 1, 1, 2, 2, 2, -2, -2, -2, 3, 3, 3, -3, -3, -3])), list_node([-3, -3, -3, -2, -2, -2, -1, -1, -1, 1, 1, 1, 2, 2, 2, 3, 3, 3])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, 0, 1, -2, 0, 2, -3, 0, 3, -4, 0, 4])), list_node([-4, -3, -2, -1, 0, 1, 0, 2, 0, 3, 0, 4]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, 0, 1, -2, 0, 2, -3, 0, 3, -4, 0, 4])), list_node([-4, -3, -2, -1, 0, 1, 0, 2, 0, 3, 0, 4])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])), list_node([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])), list_node([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-3000, 3000, -2500, 2500, -2000, 2000, -1500, 1500, -1000, 1000, -500, 500, -250, 250, -100, 100, -50, 50, -25, 25, -10, 10, -5, 5, -1, 1])), list_node([-1, -5, -10, -25, -50, -100, -250, -500, -1000, -1500, -2000, -2500, -3000, 3000, 2500, 2000, 1500, 1000, 500, 250, 100, 50, 25, 10, 5, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-3000, 3000, -2500, 2500, -2000, 2000, -1500, 1500, -1000, 1000, -500, 500, -250, 250, -100, 100, -50, 50, -25, 25, -10, 10, -5, 5, -1, 1])), list_node([-1, -5, -10, -25, -50, -100, -250, -500, -1000, -1500, -2000, -2500, -3000, 3000, 2500, 2000, 1500, 1000, 500, 250, 100, 50, 25, 10, 5, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13, -13, 14, -14, 15, -15])), list_node([-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13, -13, 14, -14, 15, -15])), list_node([-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990, -4989, -4988, -4987, -4986, -4985, -4984, -4983, -4982, -4981, -4980, 4980, 4981, 4982, 4983, 4984, 4985, 4986, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999])), list_node([-4980, -4981, -4982, -4983, -4984, -4985, -4986, -4987, -4988, -4989, -4990, -4991, -4992, -4993, -4994, -4995, -4996, -4997, -4998, -4999, 4980, 4981, 4982, 4983, 4984, 4985, 4986, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990, -4989, -4988, -4987, -4986, -4985, -4984, -4983, -4982, -4981, -4980, 4980, 4981, 4982, 4983, 4984, 4985, 4986, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999])), list_node([-4980, -4981, -4982, -4983, -4984, -4985, -4986, -4987, -4988, -4989, -4990, -4991, -4992, -4993, -4994, -4995, -4996, -4997, -4998, -4999, 4980, 4981, 4982, 4983, 4984, 4985, 4986, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([500, -250, 250, -125, 125, -62, 62, -31, 31, 0])), list_node([-31, -62, -125, -250, 500, 250, 125, 62, 31, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([500, -250, 250, -125, 125, -62, 62, -31, 31, 0])), list_node([-31, -62, -125, -250, 500, 250, 125, 62, 31, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-4500, -4000, -3500, -3000, 2500, 3000, 3500, 4000, 4500])), list_node([-3000, -3500, -4000, -4500, 2500, 3000, 3500, 4000, 4500]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-4500, -4000, -3500, -3000, 2500, 3000, 3500, 4000, 4500])), list_node([-3000, -3500, -4000, -4500, 2500, 3000, 3500, 4000, 4500])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])), list_node([-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])), list_node([-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-3000, 3000, -1500, 1500, -750, 750, -375, 375])), list_node([-375, -750, -1500, -3000, 3000, 1500, 750, 375]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-3000, 3000, -1500, 1500, -750, 750, -375, 375])), list_node([-375, -750, -1500, -3000, 3000, 1500, 750, 375])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9])), list_node([-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9])), list_node([-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 999, 998, 997, 996, 995, -994, -993, -992, -991, -990, -989, -988, -987, -986, -985])), list_node([-985, -986, -987, -988, -989, -990, -991, -992, -993, -994, 1000, 999, 998, 997, 996, 995]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 999, 998, 997, 996, 995, -994, -993, -992, -991, -990, -989, -988, -987, -986, -985])), list_node([-985, -986, -987, -988, -989, -990, -991, -992, -993, -994, 1000, 999, 998, 997, 996, 995])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2])), list_node([-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2])), list_node([-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([500, 400, 300, 200, 100, 50, 25, 10, 5, 1, -1, -5, -10, -25, -50, -100, -200, -300, -400, -500, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([-500, -400, -300, -200, -100, -50, -25, -10, -5, -1, 500, 400, 300, 200, 100, 50, 25, 10, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([500, 400, 300, 200, 100, 50, 25, 10, 5, 1, -1, -5, -10, -25, -50, -100, -200, -300, -400, -500, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([-500, -400, -300, -200, -100, -50, -25, -10, -5, -1, 500, 400, 300, 200, 100, 50, 25, 10, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([500, -500, 400, -400, 300, -300, 200, -200, 100, -100, 0])), list_node([-100, -200, -300, -400, -500, 500, 400, 300, 200, 100, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([500, -500, 400, -400, 300, -300, 200, -200, 100, -100, 0])), list_node([-100, -200, -300, -400, -500, 500, 400, 300, 200, 100, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-3000, -2000, 2000, 3000, -1000, 1000, -500, 500])), list_node([-500, -1000, -2000, -3000, 2000, 3000, 1000, 500]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-3000, -2000, 2000, 3000, -1000, 1000, -500, 500])), list_node([-500, -1000, -2000, -3000, 2000, 3000, 1000, 500])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-2, -3, -4, -5, -6, -7, -8, -9, 1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([-9, -8, -7, -6, -5, -4, -3, -2, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-2, -3, -4, -5, -6, -7, -8, -9, 1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([-9, -8, -7, -6, -5, -4, -3, -2, 1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, -5000, 4999, -4999, 4998, -4998, 4997, -4997, 4996, -4996])), list_node([-4996, -4997, -4998, -4999, -5000, 5000, 4999, 4998, 4997, 4996]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, -5000, 4999, -4999, 4998, -4998, 4997, -4997, 4996, -4996])), list_node([-4996, -4997, -4998, -4999, -5000, 5000, 4999, 4998, 4997, 4996])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990])), list_node([-4990, -4991, -4992, -4993, -4994, -4995, -4996, -4997, -4998, -4999]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990])), list_node([-4990, -4991, -4992, -4993, -4994, -4995, -4996, -4997, -4998, -4999])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-2500, 2500, -2499, 2499, -2498, 2498, -2497, 2497, -2496, 2496, -2495, 2495, -2494, 2494])), list_node([-2494, -2495, -2496, -2497, -2498, -2499, -2500, 2500, 2499, 2498, 2497, 2496, 2495, 2494]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-2500, 2500, -2499, 2499, -2498, 2498, -2497, 2497, -2496, 2496, -2495, 2495, -2494, 2494])), list_node([-2494, -2495, -2496, -2497, -2498, -2499, -2500, 2500, 2499, 2498, 2497, 2496, 2495, 2494])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-10, -10, -5, -5, 0, 0, 5, 5, 10, 10])), list_node([-5, -5, -10, -10, 0, 0, 5, 5, 10, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-10, -10, -5, -5, 0, 0, 5, 5, 10, 10])), list_node([-5, -5, -10, -10, 0, 0, 5, 5, 10, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-2, 2, -1, 1, 0, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -1, -2, 2, 1, 0, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-2, 2, -1, 1, 0, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -1, -2, 2, 1, 0, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10, -11, 11, -12, 12, -13, 13, -14, 14])), list_node([-14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10, -11, 11, -12, 12, -13, 13, -14, 14])), list_node([-14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-25, -25, -25, 0, 25, 25, 25])), list_node([-25, -25, -25, 0, 25, 25, 25]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-25, -25, -25, 0, 25, 25, 25])), list_node([-25, -25, -25, 0, 25, 25, 25])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5000, 5000, -4999, 4999, -4998, 4998, -4997, 4997, -4996, 4996, -4995, 4995])), list_node([-4995, -4996, -4997, -4998, -4999, -5000, 5000, 4999, 4998, 4997, 4996, 4995]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5000, 5000, -4999, 4999, -4998, 4998, -4997, 4997, -4996, 4996, -4995, 4995])), list_node([-4995, -4996, -4997, -4998, -4999, -5000, 5000, 4999, 4998, 4997, 4996, 4995])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-4000, -3500, -3000, -2500, -2000, -1500, -1000, -500, 0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5])), list_node([-5, -4, -3, -2, -1, -500, -1000, -1500, -2000, -2500, -3000, -3500, -4000, 0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-4000, -3500, -3000, -2500, -2000, -1500, -1000, -500, 0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5])), list_node([-5, -4, -3, -2, -1, -500, -1000, -1500, -2000, -2500, -3000, -3500, -4000, 0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-500, 500, -400, 400, -300, 300, -200, 200, -100, 100, -50, 50, -25, 25, -10, 10, -5, 5, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([-1, -5, -10, -25, -50, -100, -200, -300, -400, -500, 500, 400, 300, 200, 100, 50, 25, 10, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-500, 500, -400, 400, -300, 300, -200, 200, -100, 100, -50, 50, -25, 25, -10, 10, -5, 5, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([-1, -5, -10, -25, -50, -100, -200, -300, -400, -500, 500, 400, 300, 200, 100, 50, 25, 10, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2500, -2500, 2000, -2000, 1500, -1500, 1000, -1000, 500, -500, 0, 500, -500, 1000, -1000])), list_node([-1000, -500, -500, -1000, -1500, -2000, -2500, 2500, 2000, 1500, 1000, 500, 0, 500, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2500, -2500, 2000, -2000, 1500, -1500, 1000, -1000, 500, -500, 0, 500, -500, 1000, -1000])), list_node([-1000, -500, -500, -1000, -1500, -2000, -2500, 2500, 2000, 1500, 1000, 500, 0, 500, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312, 156, -156, 78, -78, 39, -39, 19, -19, 9, -9, 4, -4, 2, -2, 1, -1])), list_node([-1, -2, -4, -9, -19, -39, -78, -156, -312, -625, -1250, -2500, -5000, 5000, 2500, 1250, 625, 312, 156, 78, 39, 19, 9, 4, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312, 156, -156, 78, -78, 39, -39, 19, -19, 9, -9, 4, -4, 2, -2, 1, -1])), list_node([-1, -2, -4, -9, -19, -39, -78, -156, -312, -625, -1250, -2500, -5000, 5000, 2500, 1250, 625, 312, 156, 78, 39, 19, 9, 4, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5])), list_node([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5])), list_node([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, -10, -20, -30, -40, -50, 0, 0, 0, 0, 0, 0])), list_node([-50, -40, -30, -20, -10, 10, 20, 30, 40, 50, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, -10, -20, -30, -40, -50, 0, 0, 0, 0, 0, 0])), list_node([-50, -40, -30, -20, -10, 10, 20, 30, 40, 50, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, -1000, 900, -900, 800, -800, 700, -700, 600, -600, 500, -500, 400, -400, 300, -300, 200, -200, 100, -100])), list_node([-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, -1000, 900, -900, 800, -800, 700, -700, 600, -600, 500, -500, 400, -400, 300, -300, 200, -200, 100, -100])), list_node([-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-250, -125, 0, 125, 250, -62, 62, -31, 31, -15, 15, -7, 7, -3, 3, -1, 1])), list_node([-1, -3, -7, -15, -31, -62, -125, -250, 0, 125, 250, 62, 31, 15, 7, 3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-250, -125, 0, 125, 250, -62, 62, -31, 31, -15, 15, -7, 7, -3, 3, -1, 1])), list_node([-1, -3, -7, -15, -31, -62, -125, -250, 0, 125, 250, 62, 31, 15, 7, 3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([3, -2, 1, -1, 0, -3, 2])), list_node([-3, -1, -2, 3, 1, 0, 2]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([3, -2, 1, -1, 0, -3, 2])), list_node([-3, -1, -2, 3, 1, 0, 2])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-3000, 3000, -2500, 2500, -2000, 2000, -1500, 1500, -1000, 1000, -500, 500, -100, 100, -50, 50, 0])), list_node([-50, -100, -500, -1000, -1500, -2000, -2500, -3000, 3000, 2500, 2000, 1500, 1000, 500, 100, 50, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-3000, 3000, -2500, 2500, -2000, 2000, -1500, 1500, -1000, 1000, -500, 500, -100, 100, -50, 50, 0])), list_node([-50, -100, -500, -1000, -1500, -2000, -2500, -3000, 3000, 2500, 2000, 1500, 1000, 500, 100, 50, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-5000, 5000, -4000, 4000, -3000, 3000, -2000, 2000, -1000, 1000, 0, 1000, -1000, 2000, -2000])), list_node([-2000, -1000, -1000, -2000, -3000, -4000, -5000, 5000, 4000, 3000, 2000, 1000, 0, 1000, 2000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-5000, 5000, -4000, 4000, -3000, 3000, -2000, 2000, -1000, 1000, 0, 1000, -1000, 2000, -2000])), list_node([-2000, -1000, -1000, -2000, -3000, -4000, -5000, 5000, 4000, 3000, 2000, 1000, 0, 1000, 2000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, -5000, 4999, -4999, 4998, -4998])), list_node([-4998, -4999, -5000, 5000, 4999, 4998]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, -5000, 4999, -4999, 4998, -4998])), list_node([-4998, -4999, -5000, 5000, 4999, 4998])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([4000, -3500, 3500, -3000, 3000, -2500, 2500, -2000, 2000, -1500, 1500, -1000, 1000, -500, 500, -250, 250, -125, 125])), list_node([-125, -250, -500, -1000, -1500, -2000, -2500, -3000, -3500, 4000, 3500, 3000, 2500, 2000, 1500, 1000, 500, 250, 125]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([4000, -3500, 3500, -3000, 3000, -2500, 2500, -2000, 2000, -1500, 1500, -1000, 1000, -500, 500, -250, 250, -125, 125])), list_node([-125, -250, -500, -1000, -1500, -2000, -2500, -3000, -3500, 4000, 3500, 3000, 2500, 2000, 1500, 1000, 500, 250, 125])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-4999, 4999, -4998, 4998, -4997, 4997, -4996, 4996, -4995, 4995])), list_node([-4995, -4996, -4997, -4998, -4999, 4999, 4998, 4997, 4996, 4995]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-4999, 4999, -4998, 4998, -4997, 4997, -4996, 4996, -4995, 4995])), list_node([-4995, -4996, -4997, -4998, -4999, 4999, 4998, 4997, 4996, 4995])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0, -100, -200, -300, -400, -500, -600, -700, -800, -900, -1000])), list_node([-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0, -100, -200, -300, -400, -500, -600, -700, -800, -900, -1000])), list_node([-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([4999, -4998, 4997, -4996, 4995, -4994, 4993, -4992, 4991, -4990])), list_node([-4990, -4992, -4994, -4996, -4998, 4999, 4997, 4995, 4993, 4991]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([4999, -4998, 4997, -4996, 4995, -4994, 4993, -4992, 4991, -4990])), list_node([-4990, -4992, -4994, -4996, -4998, 4999, 4997, 4995, 4993, 4991])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, 5, 4, 3, 2, 1])), list_node([-5, -4, -3, -2, -1, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, 5, 4, 3, 2, 1])), list_node([-5, -4, -3, -2, -1, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-4000, 4000, -3000, 3000, -2000, 2000, -1000, 1000, -500, 500, 0])), list_node([-500, -1000, -2000, -3000, -4000, 4000, 3000, 2000, 1000, 500, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-4000, 4000, -3000, 3000, -2000, 2000, -1000, 1000, -500, 500, 0])), list_node([-500, -1000, -2000, -3000, -4000, 4000, 3000, 2000, 1000, 500, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5])), list_node([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5])), list_node([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-4500, 4500, -4000, 4000, -3500, 3500, -3000, 3000, -2500, 2500, -2000, 2000, -1500, 1500, -1000, 1000, -500, 500, -100, 100, -50, 50, 0])), list_node([-50, -100, -500, -1000, -1500, -2000, -2500, -3000, -3500, -4000, -4500, 4500, 4000, 3500, 3000, 2500, 2000, 1500, 1000, 500, 100, 50, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-4500, 4500, -4000, 4000, -3500, 3500, -3000, 3000, -2500, 2500, -2000, 2000, -1500, 1500, -1000, 1000, -500, 500, -100, 100, -50, 50, 0])), list_node([-50, -100, -500, -1000, -1500, -2000, -2500, -3000, -3500, -4000, -4500, 4500, 4000, 3500, 3000, 2500, 2000, 1500, 1000, 500, 100, 50, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, -1000, 500, -500, 250, -250, 125, -125, 62, -62, 31, -31])), list_node([-31, -62, -125, -250, -500, -1000, 1000, 500, 250, 125, 62, 31]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, -1000, 500, -500, 250, -250, 125, -125, 62, -62, 31, -31])), list_node([-31, -62, -125, -250, -500, -1000, 1000, 500, 250, 125, 62, 31])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([500, -250, 250, -125, 125, -62, 62, -31, 31, -15, 15, -7, 7, -3, 3, -1, 1, 0])), list_node([-1, -3, -7, -15, -31, -62, -125, -250, 500, 250, 125, 62, 31, 15, 7, 3, 1, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([500, -250, 250, -125, 125, -62, 62, -31, 31, -15, 15, -7, 7, -3, 3, -1, 1, 0])), list_node([-1, -3, -7, -15, -31, -62, -125, -250, 500, 250, 125, 62, 31, 15, 7, 3, 1, 0])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-4999, -2499, 0, 2499, 4999, -1249, 1249, -624, 624, -312, 312, -156, 156])), list_node([-156, -312, -624, -1249, -2499, -4999, 0, 2499, 4999, 1249, 624, 312, 156]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-4999, -2499, 0, 2499, 4999, -1249, 1249, -624, 624, -312, 312, -156, 156])), list_node([-156, -312, -624, -1249, -2499, -4999, 0, 2499, 4999, 1249, 624, 312, 156])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9])), list_node([-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9])), list_node([-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-1, 0, 1, -2, 0, 2, -3, 0, 3, -4, 0, 4, -5, 0, 5, -6, 0, 6, -7, 0, 7, -8, 0, 8, -9, 0, 9, -10, 0, 10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-1, 0, 1, -2, 0, 2, -3, 0, 3, -4, 0, 4, -5, 0, 5, -6, 0, 6, -7, 0, 7, -8, 0, 8, -9, 0, 9, -10, 0, 10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600, 700, -700, 800, -800, 900, -900, 1000, -1000])), list_node([-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600, 700, -700, 800, -800, 900, -900, 1000, -1000])), list_node([-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10])), list_node([-9, -7, -5, -3, -1, 0, 2, 4, 6, 8, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10])), list_node([-9, -7, -5, -3, -1, 0, 2, 4, 6, 8, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1])), list_node([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1])), list_node([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-10, -5, 5, 10, 15, 20, -20, -15])), list_node([-15, -20, -5, -10, 5, 10, 15, 20]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-10, -5, 5, 10, 15, 20, -20, -15])), list_node([-15, -20, -5, -10, 5, 10, 15, 20])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([100, -100, 99, -99, 98, -98, 97, -97, 96, -96, 95, -95, 94, -94, 93, -93, 92, -92, 91, -91, 90, -90, 89, -89, 88, -88, 87, -87, 86, -86, 85, -85, 84, -84, 83, -83, 82, -82, 81, -81, 80, -80, 79, -79, 78, -78, 77, -77, 76, -76, 75, -75, 74, -74, 73, -73, 72, -72, 71, -71, 70, -70, 69, -69, 68, -68, 67, -67, 66, -66, 65, -65, 64, -64, 63, -63, 62, -62, 61, -61, 60, -60, 59, -59, 58, -58, 57, -57, 56, -56, 55, -55, 54, -54, 53, -53, 52, -52, 51, -51, 50, -50, 49, -49, 48, -48, 47, -47, 46, -46, 45, -45, 44, -44, 43, -43, 42, -42, 41, -41, 40, -40, 39, -39, 38, -38, 37, -37, 36, -36, 35, -35, 34, -34, 33, -33, 32, -32, 31, -31, 30, -30, 29, -29, 28, -28, 27, -27, 26, -26, 25, -25, 24, -24, 23, -23, 22, -22, 21, -21, 20, -20, 19, -19, 18, -18, 17, -17, 16, -16, 15, -15, 14, -14, 13, -13, 12, -12, 11, -11, 10, -10, 9, -9, 8, -8, 7, -7, 6, -6, 5, -5, 4, -4, 3, -3, 2, -2, 1, -1])), list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -32, -33, -34, -35, -36, -37, -38, -39, -40, -41, -42, -43, -44, -45, -46, -47, -48, -49, -50, -51, -52, -53, -54, -55, -56, -57, -58, -59, -60, -61, -62, -63, -64, -65, -66, -67, -68, -69, -70, -71, -72, -73, -74, -75, -76, -77, -78, -79, -80, -81, -82, -83, -84, -85, -86, -87, -88, -89, -90, -91, -92, -93, -94, -95, -96, -97, -98, -99, -100, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([100, -100, 99, -99, 98, -98, 97, -97, 96, -96, 95, -95, 94, -94, 93, -93, 92, -92, 91, -91, 90, -90, 89, -89, 88, -88, 87, -87, 86, -86, 85, -85, 84, -84, 83, -83, 82, -82, 81, -81, 80, -80, 79, -79, 78, -78, 77, -77, 76, -76, 75, -75, 74, -74, 73, -73, 72, -72, 71, -71, 70, -70, 69, -69, 68, -68, 67, -67, 66, -66, 65, -65, 64, -64, 63, -63, 62, -62, 61, -61, 60, -60, 59, -59, 58, -58, 57, -57, 56, -56, 55, -55, 54, -54, 53, -53, 52, -52, 51, -51, 50, -50, 49, -49, 48, -48, 47, -47, 46, -46, 45, -45, 44, -44, 43, -43, 42, -42, 41, -41, 40, -40, 39, -39, 38, -38, 37, -37, 36, -36, 35, -35, 34, -34, 33, -33, 32, -32, 31, -31, 30, -30, 29, -29, 28, -28, 27, -27, 26, -26, 25, -25, 24, -24, 23, -23, 22, -22, 21, -21, 20, -20, 19, -19, 18, -18, 17, -17, 16, -16, 15, -15, 14, -14, 13, -13, 12, -12, 11, -11, 10, -10, 9, -9, 8, -8, 7, -7, 6, -6, 5, -5, 4, -4, 3, -3, 2, -2, 1, -1])), list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -32, -33, -34, -35, -36, -37, -38, -39, -40, -41, -42, -43, -44, -45, -46, -47, -48, -49, -50, -51, -52, -53, -54, -55, -56, -57, -58, -59, -60, -61, -62, -63, -64, -65, -66, -67, -68, -69, -70, -71, -72, -73, -74, -75, -76, -77, -78, -79, -80, -81, -82, -83, -84, -85, -86, -87, -88, -89, -90, -91, -92, -93, -94, -95, -96, -97, -98, -99, -100, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1])), list_node([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1])), list_node([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-2000, 1999, -1998, 1997, -1996, 1995, -1994, 1993, -1992, 1991])), list_node([-1992, -1994, -1996, -1998, -2000, 1999, 1997, 1995, 1993, 1991]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-2000, 1999, -1998, 1997, -1996, 1995, -1994, 1993, -1992, 1991])), list_node([-1992, -1994, -1996, -1998, -2000, 1999, 1997, 1995, 1993, 1991])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-3000, 3000, -2999, 2999, -2998, 2998, -2997, 2997, -2996, 2996])), list_node([-2996, -2997, -2998, -2999, -3000, 3000, 2999, 2998, 2997, 2996]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-3000, 3000, -2999, 2999, -2998, 2998, -2997, 2997, -2996, 2996])), list_node([-2996, -2997, -2998, -2999, -3000, 3000, 2999, 2998, 2997, 2996])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100, 0, 100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600, 700, -700])), list_node([-700, -600, -500, -400, -300, -200, -100, 0, 100, 200, 300, 400, 500, 600, 700]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100, 0, 100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600, 700, -700])), list_node([-700, -600, -500, -400, -300, -200, -100, 0, 100, 200, 300, 400, 500, 600, 700])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([2500, -2499, 2498, -2497, 2496, -2495, 2494, -2493, 2492, -2491])), list_node([-2491, -2493, -2495, -2497, -2499, 2500, 2498, 2496, 2494, 2492]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([2500, -2499, 2498, -2497, 2496, -2495, 2494, -2493, 2492, -2491])), list_node([-2491, -2493, -2495, -2497, -2499, 2500, 2498, 2496, 2494, 2492])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312])), list_node([-312, -625, -1250, -2500, -5000, 5000, 2500, 1250, 625, 312]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312])), list_node([-312, -625, -1250, -2500, -5000, 5000, 2500, 1250, 625, 312])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-3000, -2000, -1000, 0, 1000, 2000, 3000, -2500, -1500, -500, 500, 1500, 2500])), list_node([-500, -1500, -2500, -1000, -2000, -3000, 0, 1000, 2000, 3000, 500, 1500, 2500]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-3000, -2000, -1000, 0, 1000, 2000, 3000, -2500, -1500, -500, 500, 1500, 2500])), list_node([-500, -1500, -2500, -1000, -2000, -3000, 0, 1000, 2000, 3000, 500, 1500, 2500])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8])), list_node([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8])), list_node([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, 10, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, 10, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, -1, -3, -7, -15, -31, -62, -125, -250, -500, -1000])), list_node([-1000, -500, -250, -125, -62, -31, -15, -7, -3, -1, 1000, 500, 250, 125, 62, 31, 15, 7, 3, 1]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, -1, -3, -7, -15, -31, -62, -125, -250, -500, -1000])), list_node([-1000, -500, -250, -125, -62, -31, -15, -7, -3, -1, 1000, 500, 250, 125, 62, 31, 15, 7, 3, 1])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([50, 25, -25, 0, 75, -75, 100, -100, 125, -125, 150, -150, 175, -175, 200, -200])), list_node([-200, -175, -150, -125, -100, -75, -25, 50, 25, 0, 75, 100, 125, 150, 175, 200]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([50, 25, -25, 0, 75, -75, 100, -100, 125, -125, 150, -150, 175, -175, 200, -200])), list_node([-200, -175, -150, -125, -100, -75, -25, 50, 25, 0, 75, 100, 125, 150, 175, 200])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-100, 0, 100, -50, 50, -25, 25, -12, 12, -6, 6, -3, 3, -1, 1, 0, -2, 2, -4, 4, -7, 7, -8, 8, -9, 9, -11, 11])), list_node([-11, -9, -8, -7, -4, -2, -1, -3, -6, -12, -25, -50, -100, 0, 100, 50, 25, 12, 6, 3, 1, 0, 2, 4, 7, 8, 9, 11]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-100, 0, 100, -50, 50, -25, 25, -12, 12, -6, 6, -3, 3, -1, 1, 0, -2, 2, -4, 4, -7, 7, -8, 8, -9, 9, -11, 11])), list_node([-11, -9, -8, -7, -4, -2, -1, -3, -6, -12, -25, -50, -100, 0, 100, 50, 25, 12, 6, 3, 1, 0, 2, 4, 7, 8, 9, 11])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([-10000, -9000, -8000, -7000, -6000, 6000, 7000, 8000, 9000, 10000])), list_node([-6000, -7000, -8000, -9000, -10000, 6000, 7000, 8000, 9000, 10000]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([-10000, -9000, -8000, -7000, -6000, 6000, 7000, 8000, 9000, 10000])), list_node([-6000, -7000, -8000, -9000, -10000, 6000, 7000, 8000, 9000, 10000])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([1, 1, -1, -1, 2, 2, -2, -2, 3, 3, -3, -3, 4, 4, -4, -4, 5, 5, -5, -5])), list_node([-5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([1, 1, -1, -1, 2, 2, -2, -2, 3, 3, -3, -3, 4, 4, -4, -4, 5, 5, -5, -5])), list_node([-5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([500, 300, 200, -100, -200, -300, -400, 0, 100])), list_node([-400, -300, -200, -100, 500, 300, 200, 0, 100]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([500, 300, 200, -100, -200, -300, -400, 0, 100])), list_node([-400, -300, -200, -100, 500, 300, 200, 0, 100])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, -4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990])), list_node([-4990, -4991, -4992, -4993, -4994, -4995, -4996, -4997, -4998, -4999, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, -4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990])), list_node([-4990, -4991, -4992, -4993, -4994, -4995, -4996, -4997, -4998, -4999, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([4999, -4999, 4998, -4998, 4997, -4997, 4996, -4996, 4995, -4995])), list_node([-4995, -4996, -4997, -4998, -4999, 4999, 4998, 4997, 4996, 4995]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([4999, -4999, 4998, -4998, 4997, -4997, 4996, -4996, 4995, -4995])), list_node([-4995, -4996, -4997, -4998, -4999, 4999, 4998, 4997, 4996, 4995])): {e}')
    
    total += 1
    try:
        result = is_same_list(candidate(head = list_node([50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50])), list_node([-50, -40, -30, -20, -10, 50, 40, 30, 20, 10, 0]))
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in is_same_list(candidate(head = list_node([50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50])), list_node([-50, -40, -30, -20, -10, 50, 40, 30, 20, 10, 0])): {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert is_same_list(candidate(head = list_node([-1, -1, -1, 0, 0, 0, 1, 1, 1])), list_node([-1, -1, -1, 0, 0, 0, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([5, 4, 3, 2, 1])), list_node([5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([1000, -1000, 500, -500, 250, -250, 125, -125])), list_node([-125, -250, -500, -1000, 1000, 500, 250, 125]))
    assert is_same_list(candidate(head = list_node([-1, -2, -3])), list_node([-3, -2, -1]))
    assert is_same_list(candidate(head = list_node([5, -3, 3, -2, 2, -1, 1, 0])), list_node([-1, -2, -3, 5, 3, 2, 1, 0]))
    assert is_same_list(candidate(head = list_node([5, 5, 5, 5])), list_node([5, 5, 5, 5]))
    assert is_same_list(candidate(head = list_node([-5, -5, -5, -5])), list_node([-5, -5, -5, -5]))
    assert is_same_list(candidate(head = list_node([1000, -1000, 500, -500, 0])), list_node([-500, -1000, 1000, 500, 0]))
    assert is_same_list(candidate(head = list_node([-1, 0, 1])), list_node([-1, 0, 1]))
    assert is_same_list(candidate(head = list_node([0, 2, -5, 5, 10, -10])), list_node([-10, -5, 0, 2, 5, 10]))
    assert is_same_list(candidate(head = list_node([-1, -2, -3, 4, 5])), list_node([-3, -2, -1, 4, 5]))
    assert is_same_list(candidate(head = list_node([-5000, 5000, -4999, 4999, -1, 1])), list_node([-1, -4999, -5000, 5000, 4999, 1]))
    assert is_same_list(candidate(head = list_node([1])), list_node([1]))
    assert is_same_list(candidate(head = list_node([5, -1, 3, -2, 4])), list_node([-2, -1, 5, 3, 4]))
    assert is_same_list(candidate(head = list_node([1000, -1000, 500, -500, 250, -250])), list_node([-250, -500, -1000, 1000, 500, 250]))
    assert is_same_list(candidate(head = list_node([-3, 1, -2, 2])), list_node([-2, -3, 1, 2]))
    assert is_same_list(candidate(head = list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])), list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([-3, -2, -1, 0, 1, 2, 3])), list_node([-1, -2, -3, 0, 1, 2, 3]))
    assert is_same_list(candidate(head = list_node([3, 2, 1])), list_node([3, 2, 1]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, -1, -2, -3, 1, 2, 3])), list_node([-3, -2, -1, 0, 0, 0, 1, 2, 3]))
    assert is_same_list(candidate(head = list_node([0, 1, 2])), list_node([0, 1, 2]))
    assert is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5])), list_node([-5, -4, -3, -2, -1]))
    assert is_same_list(candidate(head = list_node([-3, 1, -2, 2, -1, 3])), list_node([-1, -2, -3, 1, 2, 3]))
    assert is_same_list(candidate(head = list_node([5, 3, -1, 2, -4, 0])), list_node([-4, -1, 5, 3, 2, 0]))
    assert is_same_list(candidate(head = list_node([-100, -50, 0, 50, 100])), list_node([-50, -100, 0, 50, 100]))
    assert is_same_list(candidate(head = list_node([5, -4, 3, -2, 1])), list_node([-2, -4, 5, 3, 1]))
    assert is_same_list(candidate(head = list_node([-1000, 0, 1000, -500, 500])), list_node([-500, -1000, 0, 1000, 500]))
    assert is_same_list(candidate(head = list_node([-1000, 1000, -500, 500, 0])), list_node([-500, -1000, 1000, 500, 0]))
    assert is_same_list(candidate(head = list_node([-5000, 5000, -4999, 4999])), list_node([-4999, -5000, 5000, 4999]))
    assert is_same_list(candidate(head = list_node([-5, -3, -1, 0, 2, 4])), list_node([-1, -3, -5, 0, 2, 4]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([-1, -1, 1, 1])), list_node([-1, -1, 1, 1]))
    assert is_same_list(candidate(head = list_node([-5000, 5000, -4500, 4500, -4000, 4000, -3500, 3500, -3000, 3000, -2500, 2500, -2000, 2000, -1500, 1500, -1000, 1000, -500, 500, -250, 250, -100, 100, -50, 50, -25, 25, -10, 10, -5, 5, -1, 1])), list_node([-1, -5, -10, -25, -50, -100, -250, -500, -1000, -1500, -2000, -2500, -3000, -3500, -4000, -4500, -5000, 5000, 4500, 4000, 3500, 3000, 2500, 2000, 1500, 1000, 500, 250, 100, 50, 25, 10, 5, 1]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([2000, -1500, 1000, -500, 0, 500, -1000, 1500, -2000])), list_node([-2000, -1000, -500, -1500, 2000, 1000, 0, 500, 1500]))
    assert is_same_list(candidate(head = list_node([-1000, -999, -998, -997, -996, -995, -994, -993, -992, -991])), list_node([-991, -992, -993, -994, -995, -996, -997, -998, -999, -1000]))
    assert is_same_list(candidate(head = list_node([500, -400, 300, -200, 100, -50, 0, 50, -100, 200, -300, 400])), list_node([-300, -100, -50, -200, -400, 500, 300, 100, 0, 50, 200, 400]))
    assert is_same_list(candidate(head = list_node([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1])), list_node([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([1, 2, 3, 4, 5, -1, -2, -3, -4, -5, 6, 7, 8, 9, 10, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])), list_node([-10, -20, -30, -40, -50, -60, -70, -80, -90, -100, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))
    assert is_same_list(candidate(head = list_node([-1, 0, 1, -2, 2, -3, 3, -4, 4, -5, 5])), list_node([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([-3000, -2000, -1000, 0, 1000, 2000, 3000])), list_node([-1000, -2000, -3000, 0, 1000, 2000, 3000]))
    assert is_same_list(candidate(head = list_node([-2000, -1500, -1000, -500, 0, 500, 1000, 1500, 2000, -100, -200, -300, -400, -50, -25, -10, -5, -1, 1, 5, 10, 25, 50, 100, 200, 300, 400, 500])), list_node([-1, -5, -10, -25, -50, -400, -300, -200, -100, -500, -1000, -1500, -2000, 0, 500, 1000, 1500, 2000, 1, 5, 10, 25, 50, 100, 200, 300, 400, 500]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([-1, -1, -1, 1, 1, 1, 2, 2, 2, -2, -2, -2, 3, 3, 3, -3, -3, -3])), list_node([-3, -3, -3, -2, -2, -2, -1, -1, -1, 1, 1, 1, 2, 2, 2, 3, 3, 3]))
    assert is_same_list(candidate(head = list_node([0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([-1, 0, 1, -2, 0, 2, -3, 0, 3, -4, 0, 4])), list_node([-4, -3, -2, -1, 0, 1, 0, 2, 0, 3, 0, 4]))
    assert is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5])), list_node([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([-3000, 3000, -2500, 2500, -2000, 2000, -1500, 1500, -1000, 1000, -500, 500, -250, 250, -100, 100, -50, 50, -25, 25, -10, 10, -5, 5, -1, 1])), list_node([-1, -5, -10, -25, -50, -100, -250, -500, -1000, -1500, -2000, -2500, -3000, 3000, 2500, 2000, 1500, 1000, 500, 250, 100, 50, 25, 10, 5, 1]))
    assert is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13, -13, 14, -14, 15, -15])), list_node([-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
    assert is_same_list(candidate(head = list_node([-4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990, -4989, -4988, -4987, -4986, -4985, -4984, -4983, -4982, -4981, -4980, 4980, 4981, 4982, 4983, 4984, 4985, 4986, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999])), list_node([-4980, -4981, -4982, -4983, -4984, -4985, -4986, -4987, -4988, -4989, -4990, -4991, -4992, -4993, -4994, -4995, -4996, -4997, -4998, -4999, 4980, 4981, 4982, 4983, 4984, 4985, 4986, 4987, 4988, 4989, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999]))
    assert is_same_list(candidate(head = list_node([500, -250, 250, -125, 125, -62, 62, -31, 31, 0])), list_node([-31, -62, -125, -250, 500, 250, 125, 62, 31, 0]))
    assert is_same_list(candidate(head = list_node([-4500, -4000, -3500, -3000, 2500, 3000, 3500, 4000, 4500])), list_node([-3000, -3500, -4000, -4500, 2500, 3000, 3500, 4000, 4500]))
    assert is_same_list(candidate(head = list_node([-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])), list_node([-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]))
    assert is_same_list(candidate(head = list_node([-3000, 3000, -1500, 1500, -750, 750, -375, 375])), list_node([-375, -750, -1500, -3000, 3000, 1500, 750, 375]))
    assert is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9])), list_node([-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([1000, 999, 998, 997, 996, 995, -994, -993, -992, -991, -990, -989, -988, -987, -986, -985])), list_node([-985, -986, -987, -988, -989, -990, -991, -992, -993, -994, 1000, 999, 998, 997, 996, 995]))
    assert is_same_list(candidate(head = list_node([2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2, 2, -2])), list_node([-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]))
    assert is_same_list(candidate(head = list_node([500, 400, 300, 200, 100, 50, 25, 10, 5, 1, -1, -5, -10, -25, -50, -100, -200, -300, -400, -500, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([-500, -400, -300, -200, -100, -50, -25, -10, -5, -1, 500, 400, 300, 200, 100, 50, 25, 10, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([500, -500, 400, -400, 300, -300, 200, -200, 100, -100, 0])), list_node([-100, -200, -300, -400, -500, 500, 400, 300, 200, 100, 0]))
    assert is_same_list(candidate(head = list_node([-3000, -2000, 2000, 3000, -1000, 1000, -500, 500])), list_node([-500, -1000, -2000, -3000, 2000, 3000, 1000, 500]))
    assert is_same_list(candidate(head = list_node([-2, -3, -4, -5, -6, -7, -8, -9, 1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([-9, -8, -7, -6, -5, -4, -3, -2, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([5000, -5000, 4999, -4999, 4998, -4998, 4997, -4997, 4996, -4996])), list_node([-4996, -4997, -4998, -4999, -5000, 5000, 4999, 4998, 4997, 4996]))
    assert is_same_list(candidate(head = list_node([-4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990])), list_node([-4990, -4991, -4992, -4993, -4994, -4995, -4996, -4997, -4998, -4999]))
    assert is_same_list(candidate(head = list_node([-2500, 2500, -2499, 2499, -2498, 2498, -2497, 2497, -2496, 2496, -2495, 2495, -2494, 2494])), list_node([-2494, -2495, -2496, -2497, -2498, -2499, -2500, 2500, 2499, 2498, 2497, 2496, 2495, 2494]))
    assert is_same_list(candidate(head = list_node([-10, -10, -5, -5, 0, 0, 5, 5, 10, 10])), list_node([-5, -5, -10, -10, 0, 0, 5, 5, 10, 10]))
    assert is_same_list(candidate(head = list_node([-2, 2, -1, 1, 0, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -1, -2, 2, 1, 0, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10, -11, 11, -12, 12, -13, 13, -14, 14])), list_node([-14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))
    assert is_same_list(candidate(head = list_node([-25, -25, -25, 0, 25, 25, 25])), list_node([-25, -25, -25, 0, 25, 25, 25]))
    assert is_same_list(candidate(head = list_node([-5000, 5000, -4999, 4999, -4998, 4998, -4997, 4997, -4996, 4996, -4995, 4995])), list_node([-4995, -4996, -4997, -4998, -4999, -5000, 5000, 4999, 4998, 4997, 4996, 4995]))
    assert is_same_list(candidate(head = list_node([-4000, -3500, -3000, -2500, -2000, -1500, -1000, -500, 0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5])), list_node([-5, -4, -3, -2, -1, -500, -1000, -1500, -2000, -2500, -3000, -3500, -4000, 0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([-500, 500, -400, 400, -300, 300, -200, 200, -100, 100, -50, 50, -25, 25, -10, 10, -5, 5, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])), list_node([-1, -5, -10, -25, -50, -100, -200, -300, -400, -500, 500, 400, 300, 200, 100, 50, 25, 10, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([2500, -2500, 2000, -2000, 1500, -1500, 1000, -1000, 500, -500, 0, 500, -500, 1000, -1000])), list_node([-1000, -500, -500, -1000, -1500, -2000, -2500, 2500, 2000, 1500, 1000, 500, 0, 500, 1000]))
    assert is_same_list(candidate(head = list_node([5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312, 156, -156, 78, -78, 39, -39, 19, -19, 9, -9, 4, -4, 2, -2, 1, -1])), list_node([-1, -2, -4, -9, -19, -39, -78, -156, -312, -625, -1250, -2500, -5000, 5000, 2500, 1250, 625, 312, 156, 78, 39, 19, 9, 4, 2, 1]))
    assert is_same_list(candidate(head = list_node([0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5])), list_node([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9])), list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([10, 20, 30, 40, 50, -10, -20, -30, -40, -50, 0, 0, 0, 0, 0, 0])), list_node([-50, -40, -30, -20, -10, 10, 20, 30, 40, 50, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1000, -1000, 900, -900, 800, -800, 700, -700, 600, -600, 500, -500, 400, -400, 300, -300, 200, -200, 100, -100])), list_node([-100, -200, -300, -400, -500, -600, -700, -800, -900, -1000, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]))
    assert is_same_list(candidate(head = list_node([-250, -125, 0, 125, 250, -62, 62, -31, 31, -15, 15, -7, 7, -3, 3, -1, 1])), list_node([-1, -3, -7, -15, -31, -62, -125, -250, 0, 125, 250, 62, 31, 15, 7, 3, 1]))
    assert is_same_list(candidate(head = list_node([3, -2, 1, -1, 0, -3, 2])), list_node([-3, -1, -2, 3, 1, 0, 2]))
    assert is_same_list(candidate(head = list_node([-3000, 3000, -2500, 2500, -2000, 2000, -1500, 1500, -1000, 1000, -500, 500, -100, 100, -50, 50, 0])), list_node([-50, -100, -500, -1000, -1500, -2000, -2500, -3000, 3000, 2500, 2000, 1500, 1000, 500, 100, 50, 0]))
    assert is_same_list(candidate(head = list_node([-5000, 5000, -4000, 4000, -3000, 3000, -2000, 2000, -1000, 1000, 0, 1000, -1000, 2000, -2000])), list_node([-2000, -1000, -1000, -2000, -3000, -4000, -5000, 5000, 4000, 3000, 2000, 1000, 0, 1000, 2000]))
    assert is_same_list(candidate(head = list_node([5000, -5000, 4999, -4999, 4998, -4998])), list_node([-4998, -4999, -5000, 5000, 4999, 4998]))
    assert is_same_list(candidate(head = list_node([4000, -3500, 3500, -3000, 3000, -2500, 2500, -2000, 2000, -1500, 1500, -1000, 1000, -500, 500, -250, 250, -125, 125])), list_node([-125, -250, -500, -1000, -1500, -2000, -2500, -3000, -3500, 4000, 3500, 3000, 2500, 2000, 1500, 1000, 500, 250, 125]))
    assert is_same_list(candidate(head = list_node([-4999, 4999, -4998, 4998, -4997, 4997, -4996, 4996, -4995, 4995])), list_node([-4995, -4996, -4997, -4998, -4999, 4999, 4998, 4997, 4996, 4995]))
    assert is_same_list(candidate(head = list_node([0, 0, 0, 0, 0, 0, 0])), list_node([0, 0, 0, 0, 0, 0, 0]))
    assert is_same_list(candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0, -100, -200, -300, -400, -500, -600, -700, -800, -900, -1000])), list_node([-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0]))
    assert is_same_list(candidate(head = list_node([4999, -4998, 4997, -4996, 4995, -4994, 4993, -4992, 4991, -4990])), list_node([-4990, -4992, -4994, -4996, -4998, 4999, 4997, 4995, 4993, 4991]))
    assert is_same_list(candidate(head = list_node([-1, -2, -3, -4, -5, 5, 4, 3, 2, 1])), list_node([-5, -4, -3, -2, -1, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([-4000, 4000, -3000, 3000, -2000, 2000, -1000, 1000, -500, 500, 0])), list_node([-500, -1000, -2000, -3000, -4000, 4000, 3000, 2000, 1000, 500, 0]))
    assert is_same_list(candidate(head = list_node([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5])), list_node([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]))
    assert is_same_list(candidate(head = list_node([-4500, 4500, -4000, 4000, -3500, 3500, -3000, 3000, -2500, 2500, -2000, 2000, -1500, 1500, -1000, 1000, -500, 500, -100, 100, -50, 50, 0])), list_node([-50, -100, -500, -1000, -1500, -2000, -2500, -3000, -3500, -4000, -4500, 4500, 4000, 3500, 3000, 2500, 2000, 1500, 1000, 500, 100, 50, 0]))
    assert is_same_list(candidate(head = list_node([1000, -1000, 500, -500, 250, -250, 125, -125, 62, -62, 31, -31])), list_node([-31, -62, -125, -250, -500, -1000, 1000, 500, 250, 125, 62, 31]))
    assert is_same_list(candidate(head = list_node([500, -250, 250, -125, 125, -62, 62, -31, 31, -15, 15, -7, 7, -3, 3, -1, 1, 0])), list_node([-1, -3, -7, -15, -31, -62, -125, -250, 500, 250, 125, 62, 31, 15, 7, 3, 1, 0]))
    assert is_same_list(candidate(head = list_node([-4999, -2499, 0, 2499, 4999, -1249, 1249, -624, 624, -312, 312, -156, 156])), list_node([-156, -312, -624, -1249, -2499, -4999, 0, 2499, 4999, 1249, 624, 312, 156]))
    assert is_same_list(candidate(head = list_node([-2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, -10, 10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9])), list_node([-9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    assert is_same_list(candidate(head = list_node([-1, 0, 1, -2, 0, 2, -3, 0, 3, -4, 0, 4, -5, 0, 5, -6, 0, 6, -7, 0, 7, -8, 0, 8, -9, 0, 9, -10, 0, 10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0, 7, 0, 8, 0, 9, 0, 10]))
    assert is_same_list(candidate(head = list_node([100, -100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600, 700, -700, 800, -800, 900, -900, 1000, -1000])), list_node([-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]))
    assert is_same_list(candidate(head = list_node([0, -1, 2, -3, 4, -5, 6, -7, 8, -9, 10])), list_node([-9, -7, -5, -3, -1, 0, 2, 4, 6, 8, 10]))
    assert is_same_list(candidate(head = list_node([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1])), list_node([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([-10, -5, 5, 10, 15, 20, -20, -15])), list_node([-15, -20, -5, -10, 5, 10, 15, 20]))
    assert is_same_list(candidate(head = list_node([100, -100, 99, -99, 98, -98, 97, -97, 96, -96, 95, -95, 94, -94, 93, -93, 92, -92, 91, -91, 90, -90, 89, -89, 88, -88, 87, -87, 86, -86, 85, -85, 84, -84, 83, -83, 82, -82, 81, -81, 80, -80, 79, -79, 78, -78, 77, -77, 76, -76, 75, -75, 74, -74, 73, -73, 72, -72, 71, -71, 70, -70, 69, -69, 68, -68, 67, -67, 66, -66, 65, -65, 64, -64, 63, -63, 62, -62, 61, -61, 60, -60, 59, -59, 58, -58, 57, -57, 56, -56, 55, -55, 54, -54, 53, -53, 52, -52, 51, -51, 50, -50, 49, -49, 48, -48, 47, -47, 46, -46, 45, -45, 44, -44, 43, -43, 42, -42, 41, -41, 40, -40, 39, -39, 38, -38, 37, -37, 36, -36, 35, -35, 34, -34, 33, -33, 32, -32, 31, -31, 30, -30, 29, -29, 28, -28, 27, -27, 26, -26, 25, -25, 24, -24, 23, -23, 22, -22, 21, -21, 20, -20, 19, -19, 18, -18, 17, -17, 16, -16, 15, -15, 14, -14, 13, -13, 12, -12, 11, -11, 10, -10, 9, -9, 8, -8, 7, -7, 6, -6, 5, -5, 4, -4, 3, -3, 2, -2, 1, -1])), list_node([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -32, -33, -34, -35, -36, -37, -38, -39, -40, -41, -42, -43, -44, -45, -46, -47, -48, -49, -50, -51, -52, -53, -54, -55, -56, -57, -58, -59, -60, -61, -62, -63, -64, -65, -66, -67, -68, -69, -70, -71, -72, -73, -74, -75, -76, -77, -78, -79, -80, -81, -82, -83, -84, -85, -86, -87, -88, -89, -90, -91, -92, -93, -94, -95, -96, -97, -98, -99, -100, 100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1])), list_node([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
    assert is_same_list(candidate(head = list_node([-2000, 1999, -1998, 1997, -1996, 1995, -1994, 1993, -1992, 1991])), list_node([-1992, -1994, -1996, -1998, -2000, 1999, 1997, 1995, 1993, 1991]))
    assert is_same_list(candidate(head = list_node([-3000, 3000, -2999, 2999, -2998, 2998, -2997, 2997, -2996, 2996])), list_node([-2996, -2997, -2998, -2999, -3000, 3000, 2999, 2998, 2997, 2996]))
    assert is_same_list(candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    assert is_same_list(candidate(head = list_node([-100, 0, 100, 200, -200, 300, -300, 400, -400, 500, -500, 600, -600, 700, -700])), list_node([-700, -600, -500, -400, -300, -200, -100, 0, 100, 200, 300, 400, 500, 600, 700]))
    assert is_same_list(candidate(head = list_node([2500, -2499, 2498, -2497, 2496, -2495, 2494, -2493, 2492, -2491])), list_node([-2491, -2493, -2495, -2497, -2499, 2500, 2498, 2496, 2494, 2492]))
    assert is_same_list(candidate(head = list_node([5000, -5000, 2500, -2500, 1250, -1250, 625, -625, 312, -312])), list_node([-312, -625, -1250, -2500, -5000, 5000, 2500, 1250, 625, 312]))
    assert is_same_list(candidate(head = list_node([-3000, -2000, -1000, 0, 1000, 2000, 3000, -2500, -1500, -500, 500, 1500, 2500])), list_node([-500, -1500, -2500, -1000, -2000, -3000, 0, 1000, 2000, 3000, 500, 1500, 2500]))
    assert is_same_list(candidate(head = list_node([1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8])), list_node([-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]))
    assert is_same_list(candidate(head = list_node([0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6, -7, 7, -8, 8, -9, 9, 10, -10])), list_node([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    assert is_same_list(candidate(head = list_node([1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, -1, -3, -7, -15, -31, -62, -125, -250, -500, -1000])), list_node([-1000, -500, -250, -125, -62, -31, -15, -7, -3, -1, 1000, 500, 250, 125, 62, 31, 15, 7, 3, 1]))
    assert is_same_list(candidate(head = list_node([50, 25, -25, 0, 75, -75, 100, -100, 125, -125, 150, -150, 175, -175, 200, -200])), list_node([-200, -175, -150, -125, -100, -75, -25, 50, 25, 0, 75, 100, 125, 150, 175, 200]))
    assert is_same_list(candidate(head = list_node([-100, 0, 100, -50, 50, -25, 25, -12, 12, -6, 6, -3, 3, -1, 1, 0, -2, 2, -4, 4, -7, 7, -8, 8, -9, 9, -11, 11])), list_node([-11, -9, -8, -7, -4, -2, -1, -3, -6, -12, -25, -50, -100, 0, 100, 50, 25, 12, 6, 3, 1, 0, 2, 4, 7, 8, 9, 11]))
    assert is_same_list(candidate(head = list_node([-10000, -9000, -8000, -7000, -6000, 6000, 7000, 8000, 9000, 10000])), list_node([-6000, -7000, -8000, -9000, -10000, 6000, 7000, 8000, 9000, 10000]))
    assert is_same_list(candidate(head = list_node([1, 1, -1, -1, 2, 2, -2, -2, 3, 3, -3, -3, 4, 4, -4, -4, 5, 5, -5, -5])), list_node([-5, -5, -4, -4, -3, -3, -2, -2, -1, -1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))
    assert is_same_list(candidate(head = list_node([500, 300, 200, -100, -200, -300, -400, 0, 100])), list_node([-400, -300, -200, -100, 500, 300, 200, 0, 100]))
    assert is_same_list(candidate(head = list_node([4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999, -4999, -4998, -4997, -4996, -4995, -4994, -4993, -4992, -4991, -4990])), list_node([-4990, -4991, -4992, -4993, -4994, -4995, -4996, -4997, -4998, -4999, 4990, 4991, 4992, 4993, 4994, 4995, 4996, 4997, 4998, 4999]))
    assert is_same_list(candidate(head = list_node([4999, -4999, 4998, -4998, 4997, -4997, 4996, -4996, 4995, -4995])), list_node([-4995, -4996, -4997, -4998, -4999, 4999, 4998, 4997, 4996, 4995]))
    assert is_same_list(candidate(head = list_node([50, 40, 30, 20, 10, 0, -10, -20, -30, -40, -50])), list_node([-50, -40, -30, -20, -10, 50, 40, 30, 20, 10, 0]))


