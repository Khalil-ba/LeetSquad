def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0])) == 1648386068
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0])) == 1648386068: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])) == 18880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])) == 18880: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 0, 1, 1, 0, 1])) == 77
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 0, 1, 1, 0, 1])) == 77: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([0])) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([0])) == 0: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 0, 1, 0, 1])) == 37
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 0, 1, 0, 1])) == 37: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 0, 0])) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 0, 0])) == 12: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 0, 0, 1, 1, 1, 0, 1, 0])) == 826
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 0, 0, 1, 1, 1, 0, 1, 0])) == 826: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 1])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 1])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 2147483647
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 2147483647: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 0, 1, 0])) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 0, 1, 0])) == 18: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) == 1073741825
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) == 1073741825: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0])) == 954437176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0])) == 954437176: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == 648719018
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == 648719018: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 134217728
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 134217728: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 1, 1, 0, 1, 1, 0, 1])) == 365
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 1, 1, 0, 1, 1, 0, 1])) == 365: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0])) == 1304806852
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0])) == 1304806852: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == 984263338
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == 984263338: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == 894784853
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == 894784853: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1])) == 715827883
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1])) == 715827883: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0])) == 1431655766
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0])) == 1431655766: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) == 939524097
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) == 939524097: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0])) == 920350134
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0])) == 920350134: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0])) == 969831324
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0])) == 969831324: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])) == 536870910
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])) == 536870910: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0])) == 900557658
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0])) == 900557658: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 536870912
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 536870912: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == 715827882
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == 715827882: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0])) == 214748364
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0])) == 214748364: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0])) == 899337574
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0])) == 899337574: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0])) == 843654290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0])) == 843654290: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1])) == 966367641
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1])) == 966367641: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == 760567125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == 760567125: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1073741823
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1073741823: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == 357913941
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == 357913941: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 939524096
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 939524096: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1])) == 178956971
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1])) == 178956971: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0])) == 644245094
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0])) == 644245094: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1])) == 715827883
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1])) == 715827883: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1])) == 429496729
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1])) == 429496729: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 1, 1, 0, 1, 1, 1, 0, 1])) == 733
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 1, 1, 0, 1, 1, 1, 0, 1])) == 733: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1])) == 858993459
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1])) == 858993459: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0])) == 1010580540
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0])) == 1010580540: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) == 536870913
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) == 536870913: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1])) == 697932185
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1])) == 697932185: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == 1431655765
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == 1431655765: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0])) == 900310682
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0])) == 900310682: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0])) == 4294967292
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0])) == 4294967292: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])) == 613566756
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])) == 613566756: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0])) == 692736660
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0])) == 692736660: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0])) == 107374182
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0])) == 107374182: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) == 1: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0])) == 143165576
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0])) == 143165576: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1])) == 769045933
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1])) == 769045933: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1])) == 1002159035
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1])) == 1002159035: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(head = list_node([1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0])) == 1648386068
    assert candidate(head = list_node([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0])) == 18880
    assert candidate(head = list_node([1, 0, 0, 1, 1, 0, 1])) == 77
    assert candidate(head = list_node([0])) == 0
    assert candidate(head = list_node([1, 0, 0, 1, 0, 1])) == 37
    assert candidate(head = list_node([1, 1, 0, 0])) == 12
    assert candidate(head = list_node([1])) == 1
    assert candidate(head = list_node([1, 1, 0, 0, 1, 1, 1, 0, 1, 0])) == 826
    assert candidate(head = list_node([1, 0, 1])) == 5
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 2147483647
    assert candidate(head = list_node([1, 0, 0, 1, 0])) == 18
    assert candidate(head = list_node([1, 1, 1])) == 7
    assert candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) == 1073741825
    assert candidate(head = list_node([1, 1, 1, 1])) == 15
    assert candidate(head = list_node([1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0])) == 954437176
    assert candidate(head = list_node([1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == 648719018
    assert candidate(head = list_node([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 134217728
    assert candidate(head = list_node([1, 0, 1, 1, 0, 1, 1, 0, 1])) == 365
    assert candidate(head = list_node([1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0])) == 1304806852
    assert candidate(head = list_node([1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == 984263338
    assert candidate(head = list_node([1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == 894784853
    assert candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1])) == 715827883
    assert candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) == 1
    assert candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0])) == 1431655766
    assert candidate(head = list_node([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) == 939524097
    assert candidate(head = list_node([1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0])) == 920350134
    assert candidate(head = list_node([1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0])) == 969831324
    assert candidate(head = list_node([0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0])) == 536870910
    assert candidate(head = list_node([1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0])) == 900557658
    assert candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1])) == 3
    assert candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 536870912
    assert candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])) == 715827882
    assert candidate(head = list_node([0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0])) == 214748364
    assert candidate(head = list_node([1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0])) == 899337574
    assert candidate(head = list_node([1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0])) == 843654290
    assert candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1])) == 3
    assert candidate(head = list_node([1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1])) == 966367641
    assert candidate(head = list_node([1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == 760567125
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 1073741823
    assert candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == 357913941
    assert candidate(head = list_node([1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) == 939524096
    assert candidate(head = list_node([0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1])) == 178956971
    assert candidate(head = list_node([1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0])) == 644245094
    assert candidate(head = list_node([0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1])) == 715827883
    assert candidate(head = list_node([0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1])) == 429496729
    assert candidate(head = list_node([1, 0, 1, 1, 0, 1, 1, 1, 0, 1])) == 733
    assert candidate(head = list_node([1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1])) == 858993459
    assert candidate(head = list_node([1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0])) == 1010580540
    assert candidate(head = list_node([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) == 536870913
    assert candidate(head = list_node([1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1])) == 697932185
    assert candidate(head = list_node([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])) == 1431655765
    assert candidate(head = list_node([1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0])) == 900310682
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0])) == 4294967292
    assert candidate(head = list_node([1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])) == 613566756
    assert candidate(head = list_node([1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0])) == 692736660
    assert candidate(head = list_node([0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0])) == 107374182
    assert candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])) == 1
    assert candidate(head = list_node([0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0])) == 143165576
    assert candidate(head = list_node([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1])) == 769045933
    assert candidate(head = list_node([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1])) == 3
    assert candidate(head = list_node([1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1])) == 1002159035


