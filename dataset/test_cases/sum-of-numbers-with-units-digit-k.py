def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(num = 25,k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 25,k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 2023,k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2023,k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 37,k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 37,k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num = 100,k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100,k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 58,k = 9) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 58,k = 9) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 99,k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 99,k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 15,k = 3) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 15,k = 3) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num = 27,k = 9) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 27,k = 9) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 888,k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 888,k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 0,k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 0,k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 100,k = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100,k = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(num = 88,k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 88,k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 20,k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 20,k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 45,k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 45,k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 1,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 999,k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999,k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 100,k = 3) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100,k = 3) == 10: {e}')
    
    total += 1
    try:
        result = candidate(num = 9,k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9,k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 10,k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 10,k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 100,k = 9) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 100,k = 9) == 10: {e}')
    
    total += 1
    try:
        result = candidate(num = 666,k = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 666,k = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 345,k = 4) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 345,k = 4) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000,k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000,k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 123,k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123,k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 2997,k = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2997,k = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 2999,k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2999,k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 275,k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 275,k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 3000,k = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3000,k = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(num = 222,k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 222,k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 210,k = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 210,k = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(num = 256,k = 7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 256,k = 7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(num = 1995,k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1995,k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 900,k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 900,k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 456,k = 4) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 456,k = 4) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 256,k = 8) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 256,k = 8) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 789,k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 789,k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 21,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 21,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 202,k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 202,k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 333,k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 333,k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 150,k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 150,k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 123,k = 8) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123,k = 8) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num = 2500,k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2500,k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 400,k = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 400,k = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num = 7531,k = 3) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 7531,k = 3) == 7: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234,k = 8) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234,k = 8) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 777,k = 1) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 777,k = 1) == 7: {e}')
    
    total += 1
    try:
        result = candidate(num = 234,k = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 234,k = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num = 3000,k = 9) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3000,k = 9) == 10: {e}')
    
    total += 1
    try:
        result = candidate(num = 2345,k = 4) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2345,k = 4) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num = 678,k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 678,k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 999,k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999,k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 145,k = 6) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 145,k = 6) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num = 56,k = 0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 56,k = 0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num = 777,k = 7) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 777,k = 7) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 2999,k = 3) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2999,k = 3) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 1200,k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1200,k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 567,k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 567,k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num = 444,k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 444,k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 54321,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 54321,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 50,k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 50,k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 8642,k = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 8642,k = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 999,k = 1) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999,k = 1) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 256,k = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 256,k = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 189,k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 189,k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 555,k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 555,k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 111,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 450,k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 450,k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 13579,k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 13579,k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 0,k = 0) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 0,k = 0) == 0: {e}')
    
    total += 1
    try:
        result = candidate(num = 299,k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 299,k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 250,k = 7) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 250,k = 7) == 10: {e}')
    
    total += 1
    try:
        result = candidate(num = 768,k = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 768,k = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 1985,k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1985,k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 1500,k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1500,k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 3000,k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3000,k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 2875,k = 7) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2875,k = 7) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num = 158,k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 158,k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 99,k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 99,k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234,k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234,k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 234,k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 234,k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 111,k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 111,k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num = 101,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 101,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 3000,k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 3000,k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 143,k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 143,k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 800,k = 2) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 800,k = 2) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num = 1024,k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1024,k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(num = 303,k = 3) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 303,k = 3) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 888,k = 2) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 888,k = 2) == 4: {e}')
    
    total += 1
    try:
        result = candidate(num = 500,k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 500,k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 123,k = 4) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123,k = 4) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num = 1234,k = 7) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1234,k = 7) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000,k = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000,k = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(num = 75,k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 75,k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 1999,k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1999,k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 243,k = 7) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 243,k = 7) == 9: {e}')
    
    total += 1
    try:
        result = candidate(num = 1998,k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1998,k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 246,k = 7) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 246,k = 7) == 8: {e}')
    
    total += 1
    try:
        result = candidate(num = 135,k = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 135,k = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 676,k = 6) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 676,k = 6) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 123,k = 1) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 123,k = 1) == 3: {e}')
    
    total += 1
    try:
        result = candidate(num = 9999,k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 9999,k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 150,k = 1) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 150,k = 1) == 10: {e}')
    
    total += 1
    try:
        result = candidate(num = 2500,k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2500,k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 2345,k = 9) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2345,k = 9) == 5: {e}')
    
    total += 1
    try:
        result = candidate(num = 5,k = 0) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 5,k = 0) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num = 999,k = 5) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 999,k = 5) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num = 250,k = 5) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 250,k = 5) == 2: {e}')
    
    total += 1
    try:
        result = candidate(num = 147,k = 6) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 147,k = 6) == -1: {e}')
    
    total += 1
    try:
        result = candidate(num = 199,k = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 199,k = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 1000,k = 0) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1000,k = 0) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 2468,k = 8) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2468,k = 8) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 2024,k = 4) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 2024,k = 4) == 1: {e}')
    
    total += 1
    try:
        result = candidate(num = 234,k = 3) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 234,k = 3) == 8: {e}')
    
    total += 1
    try:
        result = candidate(num = 1111,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(num = 1111,k = 1) == 1: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(num = 25,k = 5) == 1
    assert candidate(num = 2023,k = 3) == 1
    assert candidate(num = 37,k = 2) == -1
    assert candidate(num = 100,k = 0) == 1
    assert candidate(num = 58,k = 9) == 2
    assert candidate(num = 99,k = 9) == 1
    assert candidate(num = 15,k = 3) == 5
    assert candidate(num = 27,k = 9) == 3
    assert candidate(num = 888,k = 8) == 1
    assert candidate(num = 0,k = 7) == 0
    assert candidate(num = 100,k = 1) == 10
    assert candidate(num = 88,k = 8) == 1
    assert candidate(num = 20,k = 5) == 2
    assert candidate(num = 45,k = 5) == 1
    assert candidate(num = 1,k = 1) == 1
    assert candidate(num = 999,k = 9) == 1
    assert candidate(num = 100,k = 3) == 10
    assert candidate(num = 9,k = 9) == 1
    assert candidate(num = 10,k = 0) == 1
    assert candidate(num = 100,k = 9) == 10
    assert candidate(num = 666,k = 6) == 1
    assert candidate(num = 345,k = 4) == -1
    assert candidate(num = 1000,k = 5) == 2
    assert candidate(num = 123,k = 3) == 1
    assert candidate(num = 2997,k = 7) == 1
    assert candidate(num = 2999,k = 9) == 1
    assert candidate(num = 275,k = 5) == 1
    assert candidate(num = 3000,k = 1) == 10
    assert candidate(num = 222,k = 2) == 1
    assert candidate(num = 210,k = 1) == 10
    assert candidate(num = 256,k = 7) == 8
    assert candidate(num = 1995,k = 5) == 1
    assert candidate(num = 900,k = 0) == 1
    assert candidate(num = 456,k = 4) == 4
    assert candidate(num = 256,k = 8) == 2
    assert candidate(num = 789,k = 9) == 1
    assert candidate(num = 21,k = 1) == 1
    assert candidate(num = 202,k = 2) == 1
    assert candidate(num = 333,k = 3) == 1
    assert candidate(num = 150,k = 5) == 2
    assert candidate(num = 123,k = 8) == -1
    assert candidate(num = 2500,k = 5) == 2
    assert candidate(num = 400,k = 6) == 5
    assert candidate(num = 7531,k = 3) == 7
    assert candidate(num = 1234,k = 8) == 3
    assert candidate(num = 777,k = 1) == 7
    assert candidate(num = 234,k = 5) == -1
    assert candidate(num = 3000,k = 9) == 10
    assert candidate(num = 2345,k = 4) == -1
    assert candidate(num = 678,k = 8) == 1
    assert candidate(num = 999,k = 3) == 3
    assert candidate(num = 145,k = 6) == -1
    assert candidate(num = 56,k = 0) == -1
    assert candidate(num = 777,k = 7) == 1
    assert candidate(num = 2999,k = 3) == 3
    assert candidate(num = 1200,k = 0) == 1
    assert candidate(num = 567,k = 2) == -1
    assert candidate(num = 444,k = 4) == 1
    assert candidate(num = 54321,k = 1) == 1
    assert candidate(num = 50,k = 5) == 2
    assert candidate(num = 8642,k = 2) == 1
    assert candidate(num = 999,k = 1) == 9
    assert candidate(num = 256,k = 6) == 1
    assert candidate(num = 189,k = 9) == 1
    assert candidate(num = 555,k = 5) == 1
    assert candidate(num = 111,k = 1) == 1
    assert candidate(num = 450,k = 5) == 2
    assert candidate(num = 13579,k = 9) == 1
    assert candidate(num = 0,k = 0) == 0
    assert candidate(num = 299,k = 9) == 1
    assert candidate(num = 250,k = 7) == 10
    assert candidate(num = 768,k = 4) == 2
    assert candidate(num = 1985,k = 5) == 1
    assert candidate(num = 1500,k = 0) == 1
    assert candidate(num = 3000,k = 5) == 2
    assert candidate(num = 2875,k = 7) == 5
    assert candidate(num = 158,k = 8) == 1
    assert candidate(num = 99,k = 2) == -1
    assert candidate(num = 1234,k = 4) == 1
    assert candidate(num = 234,k = 4) == 1
    assert candidate(num = 111,k = 2) == -1
    assert candidate(num = 101,k = 1) == 1
    assert candidate(num = 3000,k = 0) == 1
    assert candidate(num = 143,k = 3) == 1
    assert candidate(num = 800,k = 2) == 5
    assert candidate(num = 1024,k = 3) == 8
    assert candidate(num = 303,k = 3) == 1
    assert candidate(num = 888,k = 2) == 4
    assert candidate(num = 500,k = 5) == 2
    assert candidate(num = 123,k = 4) == -1
    assert candidate(num = 1234,k = 7) == 2
    assert candidate(num = 1000,k = 1) == 10
    assert candidate(num = 75,k = 5) == 1
    assert candidate(num = 1999,k = 9) == 1
    assert candidate(num = 243,k = 7) == 9
    assert candidate(num = 1998,k = 8) == 1
    assert candidate(num = 246,k = 7) == 8
    assert candidate(num = 135,k = 5) == 1
    assert candidate(num = 676,k = 6) == 1
    assert candidate(num = 123,k = 1) == 3
    assert candidate(num = 9999,k = 9) == 1
    assert candidate(num = 150,k = 1) == 10
    assert candidate(num = 2500,k = 0) == 1
    assert candidate(num = 2345,k = 9) == 5
    assert candidate(num = 5,k = 0) == -1
    assert candidate(num = 999,k = 5) == -1
    assert candidate(num = 250,k = 5) == 2
    assert candidate(num = 147,k = 6) == -1
    assert candidate(num = 199,k = 9) == 1
    assert candidate(num = 1000,k = 0) == 1
    assert candidate(num = 2468,k = 8) == 1
    assert candidate(num = 2024,k = 4) == 1
    assert candidate(num = 234,k = 3) == 8
    assert candidate(num = 1111,k = 1) == 1


