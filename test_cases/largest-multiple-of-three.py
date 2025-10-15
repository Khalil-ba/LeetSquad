def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(digits = [5, 5, 5]) == "555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [5, 5, 5]) == "555": {e}')
    
    total += 1
    try:
        result = candidate(digits = [3, 3, 3]) == "333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [3, 3, 3]) == "333": {e}')
    
    total += 1
    try:
        result = candidate(digits = [3, 3, 3, 3, 3]) == "33333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [3, 3, 3, 3, 3]) == "33333": {e}')
    
    total += 1
    try:
        result = candidate(digits = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == "9999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == "9999999999": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "9876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "9876543210": {e}')
    
    total += 1
    try:
        result = candidate(digits = [0, 0, 0]) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [0, 0, 0]) == "0": {e}')
    
    total += 1
    try:
        result = candidate(digits = [3, 3, 3, 3]) == "3333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [3, 3, 3, 3]) == "3333": {e}')
    
    total += 1
    try:
        result = candidate(digits = [2, 2, 2, 2, 2, 2, 2]) == "222222"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [2, 2, 2, 2, 2, 2, 2]) == "222222": {e}')
    
    total += 1
    try:
        result = candidate(digits = [3, 6, 9, 1, 8]) == "98631"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [3, 6, 9, 1, 8]) == "98631": {e}')
    
    total += 1
    try:
        result = candidate(digits = [8, 6, 7, 1, 0]) == "8760"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [8, 6, 7, 1, 0]) == "8760": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == "987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == "987654321": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1]) == ""
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1]) == "": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 4, 7, 8, 5, 2]) == "875421"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 4, 7, 8, 5, 2]) == "875421": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == "333222111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == "333222111": {e}')
    
    total += 1
    try:
        result = candidate(digits = [3, 6, 9, 3, 6, 9]) == "996633"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [3, 6, 9, 3, 6, 9]) == "996633": {e}')
    
    total += 1
    try:
        result = candidate(digits = [5, 5, 5, 5, 5, 5]) == "555555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [5, 5, 5, 5, 5, 5]) == "555555": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 1, 1, 2, 2, 2]) == "222111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 1, 1, 2, 2, 2]) == "222111": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 4, 7, 2, 5, 8, 3, 6, 9, 0]) == "9876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 4, 7, 2, 5, 8, 3, 6, 9, 0]) == "9876543210": {e}')
    
    total += 1
    try:
        result = candidate(digits = [2, 2, 2, 2, 2, 2]) == "222222"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [2, 2, 2, 2, 2, 2]) == "222222": {e}')
    
    total += 1
    try:
        result = candidate(digits = [8, 1, 9]) == "981"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [8, 1, 9]) == "981": {e}')
    
    total += 1
    try:
        result = candidate(digits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "9876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "9876543210": {e}')
    
    total += 1
    try:
        result = candidate(digits = [5, 5, 5, 5, 5, 5, 5]) == "555555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [5, 5, 5, 5, 5, 5, 5]) == "555555": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "111111111": {e}')
    
    total += 1
    try:
        result = candidate(digits = [2, 5, 8, 1, 4, 7, 0, 3, 6, 9]) == "9876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [2, 5, 8, 1, 4, 7, 0, 3, 6, 9]) == "9876543210": {e}')
    
    total += 1
    try:
        result = candidate(digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "0": {e}')
    
    total += 1
    try:
        result = candidate(digits = [0, 0, 0, 0, 0, 0, 0, 0, 0]) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [0, 0, 0, 0, 0, 0, 0, 0, 0]) == "0": {e}')
    
    total += 1
    try:
        result = candidate(digits = [2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == "33333222222"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == "33333222222": {e}')
    
    total += 1
    try:
        result = candidate(digits = [2, 3, 6, 9, 9, 3, 2, 6, 2, 3]) == "9966333222"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [2, 3, 6, 9, 9, 3, 2, 6, 2, 3]) == "9966333222": {e}')
    
    total += 1
    try:
        result = candidate(digits = [3, 0, 3, 0, 3, 0, 3, 0, 3, 0]) == "3333300000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [3, 0, 3, 0, 3, 0, 3, 0, 3, 0]) == "3333300000": {e}')
    
    total += 1
    try:
        result = candidate(digits = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == "33333333333333333333"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == "33333333333333333333": {e}')
    
    total += 1
    try:
        result = candidate(digits = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == "99999999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == "99999999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(digits = [9, 6, 3, 0, 9, 6, 3, 0, 9, 6, 3, 0, 9, 6, 3, 0, 9, 6, 3, 0]) == "99999666663333300000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [9, 6, 3, 0, 9, 6, 3, 0, 9, 6, 3, 0, 9, 6, 3, 0, 9, 6, 3, 0]) == "99999666663333300000": {e}')
    
    total += 1
    try:
        result = candidate(digits = [5, 5, 5, 5, 5, 5, 0, 0, 0]) == "555555000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [5, 5, 5, 5, 5, 5, 0, 0, 0]) == "555555000": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == "444333222111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == "444333222111": {e}')
    
    total += 1
    try:
        result = candidate(digits = [2, 5, 8, 2, 6, 3, 6, 9, 0, 5]) == "98665530"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [2, 5, 8, 2, 6, 3, 6, 9, 0, 5]) == "98665530": {e}')
    
    total += 1
    try:
        result = candidate(digits = [8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4]) == "988776655443210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4]) == "988776655443210": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == "333333333222222222111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == "333333333222222222111111111": {e}')
    
    total += 1
    try:
        result = candidate(digits = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == "555555555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == "555555555": {e}')
    
    total += 1
    try:
        result = candidate(digits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0]) == "9876543210000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0]) == "9876543210000": {e}')
    
    total += 1
    try:
        result = candidate(digits = [7, 8, 5, 2, 3, 6, 1, 4, 9, 0]) == "9876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [7, 8, 5, 2, 3, 6, 1, 4, 9, 0]) == "9876543210": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0]) == "987654321000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0]) == "987654321000000": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 4, 7, 1, 4, 7, 1, 4, 7]) == "777444111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 4, 7, 1, 4, 7, 1, 4, 7]) == "777444111": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == "22222222222222222221"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == "22222222222222222221": {e}')
    
    total += 1
    try:
        result = candidate(digits = [2, 5, 8, 5, 2, 8, 5, 2, 8]) == "888555222"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [2, 5, 8, 5, 2, 8, 5, 2, 8]) == "888555222": {e}')
    
    total += 1
    try:
        result = candidate(digits = [5, 8, 4, 2, 7, 9, 3, 6, 0, 1]) == "9876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [5, 8, 4, 2, 7, 9, 3, 6, 0, 1]) == "9876543210": {e}')
    
    total += 1
    try:
        result = candidate(digits = [2, 3, 4, 5, 6, 7, 8, 9]) == "9876543"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [2, 3, 4, 5, 6, 7, 8, 9]) == "9876543": {e}')
    
    total += 1
    try:
        result = candidate(digits = [7, 8, 9, 4, 5, 6, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4]) == "9988776655443210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [7, 8, 9, 4, 5, 6, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4]) == "9988776655443210": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "99887766554433221100"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "99887766554433221100": {e}')
    
    total += 1
    try:
        result = candidate(digits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "999888777666555444333222111000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "999888777666555444333222111000": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == "999888777666555444333222111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == "999888777666555444333222111": {e}')
    
    total += 1
    try:
        result = candidate(digits = [6, 3, 2, 1, 0, 9, 8, 7, 4, 5]) == "9876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [6, 3, 2, 1, 0, 9, 8, 7, 4, 5]) == "9876543210": {e}')
    
    total += 1
    try:
        result = candidate(digits = [4, 7, 4, 7, 4, 7]) == "777444"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [4, 7, 4, 7, 4, 7]) == "777444": {e}')
    
    total += 1
    try:
        result = candidate(digits = [3, 3, 3, 6, 6, 6, 9, 9, 9, 0, 0, 0]) == "999666333000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [3, 3, 3, 6, 6, 6, 9, 9, 9, 0, 0, 0]) == "999666333000": {e}')
    
    total += 1
    try:
        result = candidate(digits = [3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0]) == "33333333333330000000000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0]) == "33333333333330000000000000": {e}')
    
    total += 1
    try:
        result = candidate(digits = [5, 2, 5, 2, 5, 2, 5, 2, 5]) == "555552222"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [5, 2, 5, 2, 5, 2, 5, 2, 5]) == "555552222": {e}')
    
    total += 1
    try:
        result = candidate(digits = [5, 8, 3, 9, 2, 6, 1, 0]) == "9865320"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [5, 8, 3, 9, 2, 6, 1, 0]) == "9865320": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == "999888777666555444333222111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == "999888777666555444333222111": {e}')
    
    total += 1
    try:
        result = candidate(digits = [2, 4, 6, 8, 0, 0, 0, 0, 0, 0]) == "864000000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [2, 4, 6, 8, 0, 0, 0, 0, 0, 0]) == "864000000": {e}')
    
    total += 1
    try:
        result = candidate(digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "0": {e}')
    
    total += 1
    try:
        result = candidate(digits = [5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8]) == "888888888855555555"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8]) == "888888888855555555": {e}')
    
    total += 1
    try:
        result = candidate(digits = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == "777777777777777"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == "777777777777777": {e}')
    
    total += 1
    try:
        result = candidate(digits = [2, 4, 6, 8, 0, 1, 3, 5, 7, 9]) == "9876543210"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [2, 4, 6, 8, 0, 1, 3, 5, 7, 9]) == "9876543210": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "111111111": {e}')
    
    total += 1
    try:
        result = candidate(digits = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == "777777777777777777777777777"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == "777777777777777777777777777": {e}')
    
    total += 1
    try:
        result = candidate(digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "0"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "0": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7]) == "777777777744444444441111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7]) == "777777777744444444441111111111": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "111111111111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "111111111111111111": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "111111111111"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "111111111111": {e}')
    
    total += 1
    try:
        result = candidate(digits = [1, 4, 7, 2, 5, 8, 3, 6, 9]) == "987654321"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [1, 4, 7, 2, 5, 8, 3, 6, 9]) == "987654321": {e}')
    
    total += 1
    try:
        result = candidate(digits = [9, 9, 9, 6, 6, 6, 3, 3, 3, 0, 0, 0]) == "999666333000"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [9, 9, 9, 6, 6, 6, 3, 3, 3, 0, 0, 0]) == "999666333000": {e}')
    
    total += 1
    try:
        result = candidate(digits = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == "999999999999999"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == "999999999999999": {e}')
    
    total += 1
    try:
        result = candidate(digits = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == "777777777"
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(digits = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == "777777777": {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(digits = [5, 5, 5]) == "555"
    assert candidate(digits = [3, 3, 3]) == "333"
    assert candidate(digits = [3, 3, 3, 3, 3]) == "33333"
    assert candidate(digits = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == "9999999999"
    assert candidate(digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "9876543210"
    assert candidate(digits = [0, 0, 0]) == "0"
    assert candidate(digits = [3, 3, 3, 3]) == "3333"
    assert candidate(digits = [2, 2, 2, 2, 2, 2, 2]) == "222222"
    assert candidate(digits = [3, 6, 9, 1, 8]) == "98631"
    assert candidate(digits = [8, 6, 7, 1, 0]) == "8760"
    assert candidate(digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == "987654321"
    assert candidate(digits = [1]) == ""
    assert candidate(digits = [1, 4, 7, 8, 5, 2]) == "875421"
    assert candidate(digits = [1, 1, 1, 2, 2, 2, 3, 3, 3]) == "333222111"
    assert candidate(digits = [3, 6, 9, 3, 6, 9]) == "996633"
    assert candidate(digits = [5, 5, 5, 5, 5, 5]) == "555555"
    assert candidate(digits = [1, 1, 1, 2, 2, 2]) == "222111"
    assert candidate(digits = [1, 4, 7, 2, 5, 8, 3, 6, 9, 0]) == "9876543210"
    assert candidate(digits = [2, 2, 2, 2, 2, 2]) == "222222"
    assert candidate(digits = [8, 1, 9]) == "981"
    assert candidate(digits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "9876543210"
    assert candidate(digits = [5, 5, 5, 5, 5, 5, 5]) == "555555"
    assert candidate(digits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "111111111"
    assert candidate(digits = [2, 5, 8, 1, 4, 7, 0, 3, 6, 9]) == "9876543210"
    assert candidate(digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "0"
    assert candidate(digits = [0, 0, 0, 0, 0, 0, 0, 0, 0]) == "0"
    assert candidate(digits = [2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == "33333222222"
    assert candidate(digits = [2, 3, 6, 9, 9, 3, 2, 6, 2, 3]) == "9966333222"
    assert candidate(digits = [3, 0, 3, 0, 3, 0, 3, 0, 3, 0]) == "3333300000"
    assert candidate(digits = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == "33333333333333333333"
    assert candidate(digits = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == "99999999999999999999"
    assert candidate(digits = [9, 6, 3, 0, 9, 6, 3, 0, 9, 6, 3, 0, 9, 6, 3, 0, 9, 6, 3, 0]) == "99999666663333300000"
    assert candidate(digits = [5, 5, 5, 5, 5, 5, 0, 0, 0]) == "555555000"
    assert candidate(digits = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == "444333222111"
    assert candidate(digits = [2, 5, 8, 2, 6, 3, 6, 9, 0, 5]) == "98665530"
    assert candidate(digits = [8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4]) == "988776655443210"
    assert candidate(digits = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == "333333333222222222111111111"
    assert candidate(digits = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == "555555555"
    assert candidate(digits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0]) == "9876543210000"
    assert candidate(digits = [7, 8, 5, 2, 3, 6, 1, 4, 9, 0]) == "9876543210"
    assert candidate(digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0]) == "987654321000000"
    assert candidate(digits = [1, 4, 7, 1, 4, 7, 1, 4, 7]) == "777444111"
    assert candidate(digits = [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == "22222222222222222221"
    assert candidate(digits = [2, 5, 8, 5, 2, 8, 5, 2, 8]) == "888555222"
    assert candidate(digits = [5, 8, 4, 2, 7, 9, 3, 6, 0, 1]) == "9876543210"
    assert candidate(digits = [2, 3, 4, 5, 6, 7, 8, 9]) == "9876543"
    assert candidate(digits = [7, 8, 9, 4, 5, 6, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4]) == "9988776655443210"
    assert candidate(digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "99887766554433221100"
    assert candidate(digits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == "999888777666555444333222111000"
    assert candidate(digits = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == "999888777666555444333222111"
    assert candidate(digits = [6, 3, 2, 1, 0, 9, 8, 7, 4, 5]) == "9876543210"
    assert candidate(digits = [4, 7, 4, 7, 4, 7]) == "777444"
    assert candidate(digits = [3, 3, 3, 6, 6, 6, 9, 9, 9, 0, 0, 0]) == "999666333000"
    assert candidate(digits = [3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0, 3, 0]) == "33333333333330000000000000"
    assert candidate(digits = [5, 2, 5, 2, 5, 2, 5, 2, 5]) == "555552222"
    assert candidate(digits = [5, 8, 3, 9, 2, 6, 1, 0]) == "9865320"
    assert candidate(digits = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]) == "999888777666555444333222111"
    assert candidate(digits = [2, 4, 6, 8, 0, 0, 0, 0, 0, 0]) == "864000000"
    assert candidate(digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "0"
    assert candidate(digits = [5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8, 5, 8]) == "888888888855555555"
    assert candidate(digits = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == "777777777777777"
    assert candidate(digits = [2, 4, 6, 8, 0, 1, 3, 5, 7, 9]) == "9876543210"
    assert candidate(digits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "111111111"
    assert candidate(digits = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == "777777777777777777777777777"
    assert candidate(digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == "0"
    assert candidate(digits = [1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7, 1, 4, 7]) == "777777777744444444441111111111"
    assert candidate(digits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "111111111111111111"
    assert candidate(digits = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == "111111111111"
    assert candidate(digits = [1, 4, 7, 2, 5, 8, 3, 6, 9]) == "987654321"
    assert candidate(digits = [9, 9, 9, 6, 6, 6, 3, 3, 3, 0, 0, 0]) == "999666333000"
    assert candidate(digits = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == "999999999999999"
    assert candidate(digits = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == "777777777"


