def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 1000000000000,target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000000,target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999,target = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999,target = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 8888,target = 32) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8888,target = 32) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 888888888,target = 24) == 1111112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888888,target = 24) == 1111112: {e}')
    
    total += 1
    try:
        result = candidate(n = 467,target = 6) == 33
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 467,target = 6) == 33: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789,target = 30) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789,target = 30) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789,target = 10) == 543211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789,target = 10) == 543211: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,target = 27) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,target = 27) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 56789,target = 25) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 56789,target = 25) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 123,target = 6) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123,target = 6) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000,target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000,target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,target = 15) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,target = 15) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789,target = 20) == 3211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789,target = 20) == 3211: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,target = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,target = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1001,target = 1) == 8999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1001,target = 1) == 8999: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999999,target = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999999,target = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 16,target = 6) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 16,target = 6) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111,target = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111,target = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 35791113151719,target = 30) == 6848281
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 35791113151719,target = 30) == 6848281: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345678910111213,target = 50) == 787
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345678910111213,target = 50) == 787: {e}')
    
    total += 1
    try:
        result = candidate(n = 100000000000,target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100000000000,target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 88888888888,target = 10) == 1111111112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 88888888888,target = 10) == 1111111112: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321098,target = 50) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321098,target = 50) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 345678901234567890,target = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 345678901234567890,target = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 888888888888,target = 24) == 1111111112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888888888,target = 24) == 1111111112: {e}')
    
    total += 1
    try:
        result = candidate(n = 101010101010,target = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 101010101010,target = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 234567890123,target = 30) == 109877
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 234567890123,target = 30) == 109877: {e}')
    
    total += 1
    try:
        result = candidate(n = 666666666666,target = 42) == 333334
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 666666666666,target = 42) == 333334: {e}')
    
    total += 1
    try:
        result = candidate(n = 9876543210987654321,target = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9876543210987654321,target = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567890,target = 15) == 432110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567890,target = 15) == 432110: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567890123456789,target = 50) == 6543211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567890123456789,target = 50) == 6543211: {e}')
    
    total += 1
    try:
        result = candidate(n = 54321,target = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 54321,target = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321098765432,target = 50) == 1234568
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321098765432,target = 50) == 1234568: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567890,target = 18) == 32110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567890,target = 18) == 32110: {e}')
    
    total += 1
    try:
        result = candidate(n = 2222222222222222222,target = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2222222222222222222,target = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111111111111,target = 9) == 8888888889
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111111111111,target = 9) == 8888888889: {e}')
    
    total += 1
    try:
        result = candidate(n = 888888888888888,target = 35) == 11111111112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888888888888,target = 35) == 11111111112: {e}')
    
    total += 1
    try:
        result = candidate(n = 555555555,target = 15) == 4444445
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 555555555,target = 15) == 4444445: {e}')
    
    total += 1
    try:
        result = candidate(n = 4567891234567890,target = 75) == 110
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4567891234567890,target = 75) == 110: {e}')
    
    total += 1
    try:
        result = candidate(n = 888888888888,target = 60) == 11112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888888888,target = 60) == 11112: {e}')
    
    total += 1
    try:
        result = candidate(n = 1999999999,target = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1999999999,target = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 567890123456,target = 75) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 567890123456,target = 75) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 9876543210,target = 30) == 3456790
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9876543210,target = 30) == 3456790: {e}')
    
    total += 1
    try:
        result = candidate(n = 9876543210,target = 50) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9876543210,target = 50) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 555555555555555555,target = 75) == 4445
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 555555555555555555,target = 75) == 4445: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,target = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,target = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321098,target = 27) == 345678902
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321098,target = 27) == 345678902: {e}')
    
    total += 1
    try:
        result = candidate(n = 500000000000,target = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500000000000,target = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789123456789,target = 75) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789123456789,target = 75) == 11: {e}')
    
    total += 1
    try:
        result = candidate(n = 222222222222222,target = 25) == 778
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 222222222222222,target = 25) == 778: {e}')
    
    total += 1
    try:
        result = candidate(n = 3333333333333333333,target = 30) == 6666666667
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3333333333333333333,target = 30) == 6666666667: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321,target = 10) == 12345679
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321,target = 10) == 12345679: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999999,target = 10) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999999,target = 10) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1999999999999,target = 150) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1999999999999,target = 150) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000001,target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000001,target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1111111111111111111,target = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111111111111111111,target = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 888888888888,target = 35) == 11111112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888888888,target = 35) == 11111112: {e}')
    
    total += 1
    try:
        result = candidate(n = 876543210,target = 10) == 23456790
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 876543210,target = 10) == 23456790: {e}')
    
    total += 1
    try:
        result = candidate(n = 999,target = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999,target = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999999999999,target = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999999999999,target = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 99999999999,target = 9) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99999999999,target = 9) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999,target = 45) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999,target = 45) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 505050505050505050,target = 45) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 505050505050505050,target = 45) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 598765432109,target = 30) == 34567891
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 598765432109,target = 30) == 34567891: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567890123456789,target = 45) == 9876543211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567890123456789,target = 45) == 9876543211: {e}')
    
    total += 1
    try:
        result = candidate(n = 1234567890123456789,target = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1234567890123456789,target = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 9000000000009,target = 18) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9000000000009,target = 18) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 599999999999999999,target = 5) == 400000000000000001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 599999999999999999,target = 5) == 400000000000000001: {e}')
    
    total += 1
    try:
        result = candidate(n = 9876543210987654321,target = 50) == 12345679
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9876543210987654321,target = 50) == 12345679: {e}')
    
    total += 1
    try:
        result = candidate(n = 123456789012,target = 45) == 988
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 123456789012,target = 45) == 988: {e}')
    
    total += 1
    try:
        result = candidate(n = 12345678901234567890,target = 100) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12345678901234567890,target = 100) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321,target = 20) == 2345679
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321,target = 20) == 2345679: {e}')
    
    total += 1
    try:
        result = candidate(n = 54321,target = 8) == 5679
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 54321,target = 8) == 5679: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111111111,target = 14) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111111111,target = 14) == 89: {e}')
    
    total += 1
    try:
        result = candidate(n = 112233445566778899,target = 60) == 1101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 112233445566778899,target = 60) == 1101: {e}')
    
    total += 1
    try:
        result = candidate(n = 100100100100,target = 3) == 899900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100100100100,target = 3) == 899900: {e}')
    
    total += 1
    try:
        result = candidate(n = 1999999999999999999,target = 90) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1999999999999999999,target = 90) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 888888888,target = 7) == 111111112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888888,target = 7) == 111111112: {e}')
    
    total += 1
    try:
        result = candidate(n = 4321,target = 4) == 5679
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4321,target = 4) == 5679: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999999,target = 2) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999999,target = 2) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999999999999,target = 100) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999999999999,target = 100) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 599599599,target = 25) == 400401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 599599599,target = 25) == 400401: {e}')
    
    total += 1
    try:
        result = candidate(n = 567890123456,target = 30) == 9876544
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 567890123456,target = 30) == 9876544: {e}')
    
    total += 1
    try:
        result = candidate(n = 54321,target = 5) == 45679
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 54321,target = 5) == 45679: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000000000,target = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000000000,target = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 99998,target = 4) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 99998,target = 4) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 246813579111357,target = 50) == 643
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 246813579111357,target = 50) == 643: {e}')
    
    total += 1
    try:
        result = candidate(n = 888888888,target = 15) == 11111112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888888,target = 15) == 11111112: {e}')
    
    total += 1
    try:
        result = candidate(n = 567890123456789,target = 50) == 43211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 567890123456789,target = 50) == 43211: {e}')
    
    total += 1
    try:
        result = candidate(n = 888888888,target = 10) == 11111112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 888888888,target = 10) == 11111112: {e}')
    
    total += 1
    try:
        result = candidate(n = 1111111111111111111,target = 150) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1111111111111111111,target = 150) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000001,target = 1) == 8999999999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000001,target = 1) == 8999999999999: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,target = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,target = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 111111111111,target = 12) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 111111111111,target = 12) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 999999999999999999,target = 81) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 999999999999999999,target = 81) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 222222222222,target = 24) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 222222222222,target = 24) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 987654321,target = 25) == 345679
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 987654321,target = 25) == 345679: {e}')
    
    total += 1
    try:
        result = candidate(n = 1999999999999999,target = 18) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1999999999999999,target = 18) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000000000000000000,target = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000000000000000000,target = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 2222222222222222222,target = 40) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2222222222222222222,target = 40) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 333333333333,target = 30) == 667
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 333333333333,target = 30) == 667: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 1000000000000,target = 1) == 0
    assert candidate(n = 1,target = 1) == 0
    assert candidate(n = 99999,target = 5) == 1
    assert candidate(n = 8888,target = 32) == 0
    assert candidate(n = 888888888,target = 24) == 1111112
    assert candidate(n = 467,target = 6) == 33
    assert candidate(n = 123456789,target = 30) == 11
    assert candidate(n = 123456789,target = 10) == 543211
    assert candidate(n = 999,target = 27) == 0
    assert candidate(n = 56789,target = 25) == 11
    assert candidate(n = 123,target = 6) == 0
    assert candidate(n = 1000000000,target = 1) == 0
    assert candidate(n = 999,target = 15) == 1
    assert candidate(n = 123456789,target = 20) == 3211
    assert candidate(n = 999999999,target = 10) == 1
    assert candidate(n = 1001,target = 1) == 8999
    assert candidate(n = 999999999999,target = 1) == 1
    assert candidate(n = 16,target = 6) == 4
    assert candidate(n = 111111111,target = 9) == 0
    assert candidate(n = 35791113151719,target = 30) == 6848281
    assert candidate(n = 12345678910111213,target = 50) == 787
    assert candidate(n = 100000000000,target = 1) == 0
    assert candidate(n = 88888888888,target = 10) == 1111111112
    assert candidate(n = 987654321098,target = 50) == 2
    assert candidate(n = 100,target = 1) == 0
    assert candidate(n = 345678901234567890,target = 100) == 0
    assert candidate(n = 888888888888,target = 24) == 1111111112
    assert candidate(n = 101010101010,target = 15) == 0
    assert candidate(n = 234567890123,target = 30) == 109877
    assert candidate(n = 666666666666,target = 42) == 333334
    assert candidate(n = 9876543210987654321,target = 100) == 0
    assert candidate(n = 1234567890,target = 15) == 432110
    assert candidate(n = 1234567890123456789,target = 50) == 6543211
    assert candidate(n = 54321,target = 15) == 0
    assert candidate(n = 987654321098765432,target = 50) == 1234568
    assert candidate(n = 1234567890,target = 18) == 32110
    assert candidate(n = 2222222222222222222,target = 50) == 0
    assert candidate(n = 111111111111111111,target = 9) == 8888888889
    assert candidate(n = 888888888888888,target = 35) == 11111111112
    assert candidate(n = 555555555,target = 15) == 4444445
    assert candidate(n = 4567891234567890,target = 75) == 110
    assert candidate(n = 888888888888,target = 60) == 11112
    assert candidate(n = 1999999999,target = 10) == 1
    assert candidate(n = 567890123456,target = 75) == 0
    assert candidate(n = 9876543210,target = 30) == 3456790
    assert candidate(n = 9876543210,target = 50) == 0
    assert candidate(n = 555555555555555555,target = 75) == 4445
    assert candidate(n = 999999999,target = 1) == 1
    assert candidate(n = 987654321098,target = 27) == 345678902
    assert candidate(n = 500000000000,target = 5) == 0
    assert candidate(n = 123456789123456789,target = 75) == 11
    assert candidate(n = 222222222222222,target = 25) == 778
    assert candidate(n = 3333333333333333333,target = 30) == 6666666667
    assert candidate(n = 987654321,target = 10) == 12345679
    assert candidate(n = 999999999999,target = 10) == 1
    assert candidate(n = 1999999999999,target = 150) == 0
    assert candidate(n = 1000000000001,target = 2) == 0
    assert candidate(n = 1111111111111111111,target = 20) == 0
    assert candidate(n = 888888888888,target = 35) == 11111112
    assert candidate(n = 876543210,target = 10) == 23456790
    assert candidate(n = 999,target = 2) == 1
    assert candidate(n = 999999999999999999,target = 5) == 1
    assert candidate(n = 99999999999,target = 9) == 1
    assert candidate(n = 999999999,target = 45) == 1
    assert candidate(n = 505050505050505050,target = 45) == 0
    assert candidate(n = 598765432109,target = 30) == 34567891
    assert candidate(n = 1234567890123456789,target = 45) == 9876543211
    assert candidate(n = 1234567890123456789,target = 100) == 0
    assert candidate(n = 9000000000009,target = 18) == 0
    assert candidate(n = 599999999999999999,target = 5) == 400000000000000001
    assert candidate(n = 9876543210987654321,target = 50) == 12345679
    assert candidate(n = 123456789012,target = 45) == 988
    assert candidate(n = 12345678901234567890,target = 100) == 0
    assert candidate(n = 987654321,target = 20) == 2345679
    assert candidate(n = 54321,target = 8) == 5679
    assert candidate(n = 111111111111111,target = 14) == 89
    assert candidate(n = 112233445566778899,target = 60) == 1101
    assert candidate(n = 100100100100,target = 3) == 899900
    assert candidate(n = 1999999999999999999,target = 90) == 1
    assert candidate(n = 888888888,target = 7) == 111111112
    assert candidate(n = 4321,target = 4) == 5679
    assert candidate(n = 999999999999,target = 2) == 1
    assert candidate(n = 999999999999999999,target = 100) == 1
    assert candidate(n = 599599599,target = 25) == 400401
    assert candidate(n = 567890123456,target = 30) == 9876544
    assert candidate(n = 54321,target = 5) == 45679
    assert candidate(n = 5000000000,target = 5) == 0
    assert candidate(n = 99998,target = 4) == 2
    assert candidate(n = 246813579111357,target = 50) == 643
    assert candidate(n = 888888888,target = 15) == 11111112
    assert candidate(n = 567890123456789,target = 50) == 43211
    assert candidate(n = 888888888,target = 10) == 11111112
    assert candidate(n = 1111111111111111111,target = 150) == 0
    assert candidate(n = 1000000000001,target = 1) == 8999999999999
    assert candidate(n = 1,target = 2) == 0
    assert candidate(n = 111111111111,target = 12) == 0
    assert candidate(n = 999999999999999999,target = 81) == 1
    assert candidate(n = 222222222222,target = 24) == 0
    assert candidate(n = 987654321,target = 25) == 345679
    assert candidate(n = 1999999999999999,target = 18) == 1
    assert candidate(n = 1000000000000000000,target = 1) == 0
    assert candidate(n = 2222222222222222222,target = 40) == 0
    assert candidate(n = 333333333333,target = 30) == 667


