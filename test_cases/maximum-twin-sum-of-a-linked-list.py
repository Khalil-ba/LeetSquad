def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(head = list_node([9, 4, 2, 10, 7, 8])) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([9, 4, 2, 10, 7, 8])) == 17: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([4, 2, 2, 3])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([4, 2, 2, 3])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([8, 7, 6, 5, 4, 3, 2, 1])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([8, 7, 6, 5, 4, 3, 2, 1])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([99999, 99999, 99999, 99999])) == 199998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([99999, 99999, 99999, 99999])) == 199998: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100000, 1, 100000, 1])) == 100001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100000, 1, 100000, 1])) == 100001: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 4, 2, 1])) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 4, 2, 1])) == 6: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 100000])) == 100001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 100000])) == 100001: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6])) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6])) == 7: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([9, 4, 2, 10])) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([9, 4, 2, 10])) == 19: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([3, 3, 5, 5, 7, 7, 9, 9])) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([3, 3, 5, 5, 7, 7, 9, 9])) == 12: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([8, 9, 10, 11, 12, 13, 14, 15])) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([8, 9, 10, 11, 12, 13, 14, 15])) == 23: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2])) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2])) == 3: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1])) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1])) == 20: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])) == 55: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) == 17: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])) == 19: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([50000, 50000, 50000, 50000, 50000, 50000])) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([50000, 50000, 50000, 50000, 50000, 50000])) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])) == 34: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])) == 32: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([99999, 1, 99998, 2, 99997, 3, 99996, 4])) == 100003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([99999, 1, 99998, 2, 99997, 3, 99996, 4])) == 100003: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1])) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1])) == 190: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984])) == 199983
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984])) == 199983: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])) == 130: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == 11: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])) == 130: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([8, 5, 3, 7, 1, 2, 9, 6])) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([8, 5, 3, 7, 1, 2, 9, 6])) == 14: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([99999, 1, 99998, 2, 99997, 3, 99996, 4, 99995, 5])) == 100004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([99999, 1, 99998, 2, 99997, 3, 99996, 4, 99995, 5])) == 100004: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])) == 15: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 10: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 9, 2, 8, 3, 7, 4, 6, 5, 5])) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 9, 2, 8, 3, 7, 4, 6, 5, 5])) == 14: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([99999, 1, 99998, 2, 99997, 3, 99996, 4])) == 100003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([99999, 1, 99998, 2, 99997, 3, 99996, 4])) == 100003: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000, 190000, 200000])) == 210000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000, 190000, 200000])) == 210000: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980, 99979, 99978, 99977, 99976, 99975, 99974, 99973, 99972, 99971, 99970, 99969, 99968, 99967, 99966, 99965, 99964, 99963, 99962, 99961, 99960, 99959, 99958, 99957, 99956, 99955, 99954, 99953, 99952, 99951, 99950, 99949, 99948, 99947, 99946, 99945, 99944, 99943, 99942, 99941, 99940, 99939, 99938, 99937, 99936, 99935, 99934, 99933, 99932, 99931, 99930, 99929, 99928, 99927, 99926, 99925, 99924, 99923, 99922, 99921, 99920, 99919, 99918, 99917, 99916, 99915, 99914, 99913, 99912, 99911, 99910, 99909, 99908, 99907, 99906, 99905, 99904, 99903, 99902, 99901, 99900])) == 199900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980, 99979, 99978, 99977, 99976, 99975, 99974, 99973, 99972, 99971, 99970, 99969, 99968, 99967, 99966, 99965, 99964, 99963, 99962, 99961, 99960, 99959, 99958, 99957, 99956, 99955, 99954, 99953, 99952, 99951, 99950, 99949, 99948, 99947, 99946, 99945, 99944, 99943, 99942, 99941, 99940, 99939, 99938, 99937, 99936, 99935, 99934, 99933, 99932, 99931, 99930, 99929, 99928, 99927, 99926, 99925, 99924, 99923, 99922, 99921, 99920, 99919, 99918, 99917, 99916, 99915, 99914, 99913, 99912, 99911, 99910, 99909, 99908, 99907, 99906, 99905, 99904, 99903, 99902, 99901, 99900])) == 199900: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) == 21: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([25000, 30000, 35000, 40000, 45000, 40000, 35000, 30000, 25000, 20000, 20000, 25000, 30000, 35000, 40000, 45000])) == 70000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([25000, 30000, 35000, 40000, 45000, 40000, 35000, 30000, 25000, 20000, 20000, 25000, 30000, 35000, 40000, 45000])) == 70000: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])) == 32: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])) == 210: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])) == 1100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])) == 1100: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100000, 200000, 300000, 400000, 500000, 400000, 300000, 200000, 100000, 1])) == 900000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100000, 200000, 300000, 400000, 500000, 400000, 300000, 200000, 100000, 1])) == 900000: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000])) == 130000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000])) == 130000: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100000, 1, 200000, 2, 300000, 3, 400000, 4, 500000, 5, 600000, 6])) == 600001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100000, 1, 200000, 2, 300000, 3, 400000, 4, 500000, 5, 600000, 6])) == 600001: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000])) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000])) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) == 21: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 3, 6, 7, 1, 9])) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 3, 6, 7, 1, 9])) == 14: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([99999, 99998, 99997, 99996, 1, 2, 3, 4])) == 100003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([99999, 99998, 99997, 99996, 1, 2, 3, 4])) == 100003: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 99999, 2, 99998, 3, 99997, 4, 99996])) == 100003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 99999, 2, 99998, 3, 99997, 4, 99996])) == 100003: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23])) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23])) == 31: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0])) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0])) == 190: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91])) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91])) == 110: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991])) == 99991
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991])) == 99991: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53])) == 55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53])) == 55: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 6, 7, 8, 9, 10, 1, 2, 3, 4])) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 6, 7, 8, 9, 10, 1, 2, 3, 4])) == 19: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 31
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 31: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])) == 5: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 21: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == 19: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 99999, 2, 99998, 3, 99997, 4, 99996, 5, 99995])) == 100004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 99999, 2, 99998, 3, 99997, 4, 99996, 5, 99995])) == 100004: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([50000, 50000, 50000, 50000, 50000, 50000])) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([50000, 50000, 50000, 50000, 50000, 50000])) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) == 13: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995])) == 199995
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995])) == 199995: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([150000, 1, 150000, 1, 150000, 1, 150000, 1, 150000, 1, 150000, 1, 150000, 1, 150000, 1])) == 150001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([150000, 1, 150000, 1, 150000, 1, 150000, 1, 150000, 1, 150000, 1, 150000, 1, 150000, 1])) == 150001: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])) == 1100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])) == 1100: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100000, 100000, 100000, 100000, 100000, 100000])) == 200000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100000, 100000, 100000, 100000, 100000, 100000])) == 200000: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600])) == 1700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600])) == 1700: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000])) == 100001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000])) == 100001: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 100000])) == 200000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 100000])) == 200000: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([50000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 50000])) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([50000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 50000])) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23])) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23])) == 24: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([6, 2, 6, 2, 6, 2, 6, 2, 6, 2, 6, 2, 6, 2, 6, 2])) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([6, 2, 6, 2, 6, 2, 6, 2, 6, 2, 6, 2, 6, 2, 6, 2])) == 8: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])) == 65: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])) == 32: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 21: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == 20: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([8, 7, 6, 5, 4, 3, 2, 1])) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([8, 7, 6, 5, 4, 3, 2, 1])) == 9: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])) == 110: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 2: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3])) == 100003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3])) == 100003: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])) == 42: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000])) == 110000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000])) == 110000: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 21: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009])) == 1011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009])) == 1011: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([99999, 1, 99999, 1, 99999, 1, 99999, 1])) == 100000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([99999, 1, 99999, 1, 99999, 1, 99999, 1])) == 100000: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([10000, 5000, 1000, 500, 100, 50, 10, 5])) == 10005
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([10000, 5000, 1000, 500, 100, 50, 10, 5])) == 10005: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([12345, 67890, 54321, 98765, 23456, 87654])) == 153086
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([12345, 67890, 54321, 98765, 23456, 87654])) == 153086: {e}')
    
    total += 1
    try:
        result = candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) == 17: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(head = list_node([9, 4, 2, 10, 7, 8])) == 17
    assert candidate(head = list_node([4, 2, 2, 3])) == 7
    assert candidate(head = list_node([8, 7, 6, 5, 4, 3, 2, 1])) == 9
    assert candidate(head = list_node([99999, 99999, 99999, 99999])) == 199998
    assert candidate(head = list_node([100000, 1, 100000, 1])) == 100001
    assert candidate(head = list_node([5, 4, 2, 1])) == 6
    assert candidate(head = list_node([1, 100000])) == 100001
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6])) == 7
    assert candidate(head = list_node([9, 4, 2, 10])) == 19
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8])) == 9
    assert candidate(head = list_node([3, 3, 5, 5, 7, 7, 9, 9])) == 12
    assert candidate(head = list_node([8, 9, 10, 11, 12, 13, 14, 15])) == 23
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2])) == 3
    assert candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6, 6, 5, 7, 4, 8, 3, 9, 2, 10, 1])) == 20
    assert candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])) == 55
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) == 17
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])) == 19
    assert candidate(head = list_node([50000, 50000, 50000, 50000, 50000, 50000])) == 100000
    assert candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])) == 34
    assert candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])) == 32
    assert candidate(head = list_node([99999, 1, 99998, 2, 99997, 3, 99996, 4])) == 100003
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 1])) == 190
    assert candidate(head = list_node([99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984])) == 199983
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])) == 130
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == 11
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])) == 130
    assert candidate(head = list_node([8, 5, 3, 7, 1, 2, 9, 6])) == 14
    assert candidate(head = list_node([99999, 1, 99998, 2, 99997, 3, 99996, 4, 99995, 5])) == 100004
    assert candidate(head = list_node([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])) == 15
    assert candidate(head = list_node([5, 5, 5, 5, 5, 5, 5, 5, 5, 5])) == 10
    assert candidate(head = list_node([1, 9, 2, 8, 3, 7, 4, 6, 5, 5])) == 14
    assert candidate(head = list_node([99999, 1, 99998, 2, 99997, 3, 99996, 4])) == 100003
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 2
    assert candidate(head = list_node([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000, 190000, 200000])) == 210000
    assert candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995, 99994, 99993, 99992, 99991, 99990, 99989, 99988, 99987, 99986, 99985, 99984, 99983, 99982, 99981, 99980, 99979, 99978, 99977, 99976, 99975, 99974, 99973, 99972, 99971, 99970, 99969, 99968, 99967, 99966, 99965, 99964, 99963, 99962, 99961, 99960, 99959, 99958, 99957, 99956, 99955, 99954, 99953, 99952, 99951, 99950, 99949, 99948, 99947, 99946, 99945, 99944, 99943, 99942, 99941, 99940, 99939, 99938, 99937, 99936, 99935, 99934, 99933, 99932, 99931, 99930, 99929, 99928, 99927, 99926, 99925, 99924, 99923, 99922, 99921, 99920, 99919, 99918, 99917, 99916, 99915, 99914, 99913, 99912, 99911, 99910, 99909, 99908, 99907, 99906, 99905, 99904, 99903, 99902, 99901, 99900])) == 199900
    assert candidate(head = list_node([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) == 21
    assert candidate(head = list_node([25000, 30000, 35000, 40000, 45000, 40000, 35000, 30000, 25000, 20000, 20000, 25000, 30000, 35000, 40000, 45000])) == 70000
    assert candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31])) == 32
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200])) == 210
    assert candidate(head = list_node([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100])) == 1100
    assert candidate(head = list_node([100000, 200000, 300000, 400000, 500000, 400000, 300000, 200000, 100000, 1])) == 900000
    assert candidate(head = list_node([10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000])) == 130000
    assert candidate(head = list_node([100000, 1, 200000, 2, 300000, 3, 400000, 4, 500000, 5, 600000, 6])) == 600001
    assert candidate(head = list_node([25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000, 25000])) == 50000
    assert candidate(head = list_node([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) == 21
    assert candidate(head = list_node([5, 3, 6, 7, 1, 9])) == 14
    assert candidate(head = list_node([99999, 99998, 99997, 99996, 1, 2, 3, 4])) == 100003
    assert candidate(head = list_node([1, 99999, 2, 99998, 3, 99997, 4, 99996])) == 100003
    assert candidate(head = list_node([8, 6, 4, 2, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23])) == 31
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0])) == 190
    assert candidate(head = list_node([1, 100, 2, 99, 3, 98, 4, 97, 5, 96, 6, 95, 7, 94, 8, 93, 9, 92, 10, 91])) == 110
    assert candidate(head = list_node([50000, 49999, 49998, 49997, 49996, 49995, 49994, 49993, 49992, 49991])) == 99991
    assert candidate(head = list_node([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53])) == 55
    assert candidate(head = list_node([5, 6, 7, 8, 9, 10, 1, 2, 3, 4])) == 19
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])) == 31
    assert candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5])) == 5
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 21
    assert candidate(head = list_node([5, 6, 7, 8, 9, 10, 11, 12, 13, 14])) == 19
    assert candidate(head = list_node([1, 99999, 2, 99998, 3, 99997, 4, 99996, 5, 99995])) == 100004
    assert candidate(head = list_node([50000, 50000, 50000, 50000, 50000, 50000])) == 100000
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])) == 13
    assert candidate(head = list_node([100000, 99999, 99998, 99997, 99996, 99995])) == 199995
    assert candidate(head = list_node([150000, 1, 150000, 1, 150000, 1, 150000, 1, 150000, 1, 150000, 1, 150000, 1, 150000, 1])) == 150001
    assert candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])) == 1100
    assert candidate(head = list_node([100000, 100000, 100000, 100000, 100000, 100000])) == 200000
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 2
    assert candidate(head = list_node([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600])) == 1700
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 2
    assert candidate(head = list_node([1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000])) == 100001
    assert candidate(head = list_node([100000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 100000])) == 200000
    assert candidate(head = list_node([50000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 50000])) == 100000
    assert candidate(head = list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23])) == 24
    assert candidate(head = list_node([6, 2, 6, 2, 6, 2, 6, 2, 6, 2, 6, 2, 6, 2, 6, 2])) == 8
    assert candidate(head = list_node([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])) == 65
    assert candidate(head = list_node([31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1])) == 32
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])) == 21
    assert candidate(head = list_node([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) == 20
    assert candidate(head = list_node([8, 7, 6, 5, 4, 3, 2, 1])) == 9
    assert candidate(head = list_node([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])) == 110
    assert candidate(head = list_node([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])) == 2
    assert candidate(head = list_node([100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3])) == 100003
    assert candidate(head = list_node([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40])) == 42
    assert candidate(head = list_node([100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000])) == 110000
    assert candidate(head = list_node([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])) == 21
    assert candidate(head = list_node([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009])) == 1011
    assert candidate(head = list_node([99999, 1, 99999, 1, 99999, 1, 99999, 1])) == 100000
    assert candidate(head = list_node([10000, 5000, 1000, 500, 100, 50, 10, 5])) == 10005
    assert candidate(head = list_node([12345, 67890, 54321, 98765, 23456, 87654])) == 153086
    assert candidate(head = list_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])) == 17


