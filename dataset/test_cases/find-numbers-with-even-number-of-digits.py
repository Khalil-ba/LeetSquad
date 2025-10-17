def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [10, 100, 1000, 10000, 100000]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 100, 1000, 10000, 100000]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 100, 1000, 10000]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 100, 1000, 10000]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 22, 333, 4444, 55555]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 22, 333, 4444, 55555]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 10000, 1000, 100, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 10000, 1000, 100, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [555, 901, 482, 1771]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [555, 901, 482, 1771]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 22, 333, 4444, 55555, 666666]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 22, 333, 4444, 55555, 666666]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 345, 2, 6, 7896]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 345, 2, 6, 7896]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 22, 333, 4444, 55555]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 22, 333, 4444, 55555]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234, 56789, 101112, 13141516, 1718192021]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234, 56789, 101112, 13141516, 1718192021]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 99, 999, 9999, 99999]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 99, 999, 9999, 99999]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 2222, 33333, 444444, 5555555, 66666666]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 2222, 33333, 444444, 5555555, 66666666]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 111213141, 222324252, 333435363]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 111213141, 222324252, 333435363]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 11, 111, 1111, 11111, 111111]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 11, 111, 1111, 11111, 111111]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654, 321, 654321, 987, 65432]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654, 321, 654321, 987, 65432]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [222222, 444444, 666666, 888888, 1111111]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [222222, 444444, 666666, 888888, 1111111]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999, 1000]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999, 1000]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 789012, 34567, 11, 222222]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 789012, 34567, 11, 222222]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111111, 222222, 333333, 444444, 555555, 666666, 777777, 888888, 999999]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111111, 222222, 333333, 444444, 555555, 666666, 777777, 888888, 999999]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 345, 6789, 101112, 13141516]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 345, 6789, 101112, 13141516]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234, 56789, 101112, 13141516, 1718192021]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234, 56789, 101112, 13141516, 1718192021]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 55, 555, 5555, 55555, 555555, 5555555]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 55, 555, 5555, 55555, 555555, 5555555]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9999, 88888, 777777, 6666666, 55555555]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9999, 88888, 777777, 6666666, 55555555]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5555555555, 333333333, 11111111, 9999999, 777777, 55555, 3333, 111, 99, 7, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5555555555, 333333333, 11111111, 9999999, 777777, 55555, 3333, 111, 99, 7, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12345678, 87654321, 11223344, 55667788]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12345678, 87654321, 11223344, 55667788]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1111111111, 222222222, 33333333, 4444444, 555555, 66666, 7777, 888, 99, 9]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1111111111, 222222222, 33333333, 4444444, 555555, 66666, 7777, 888, 99, 9]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 8888, 77777, 666666, 5555555]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 8888, 77777, 666666, 5555555]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654, 876543, 765432, 654321, 543210]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654, 876543, 765432, 654321, 543210]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 1122334455, 6677889900, 1010101010]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 1122334455, 6677889900, 1010101010]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [102030, 204060, 306090, 408120, 510150]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [102030, 204060, 306090, 408120, 510150]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234567, 876543, 234567, 765432, 345678]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234567, 876543, 234567, 765432, 345678]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 11, 111, 1111, 11111, 111111, 1111111, 11111111]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 11, 111, 1111, 11111, 111111, 1111111, 11111111]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654, 123456789, 98765, 43210, 111111, 2222222]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654, 123456789, 98765, 43210, 111111, 2222222]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [54321, 12345, 67890, 98765, 43210, 11111, 22222, 33333]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [54321, 12345, 67890, 98765, 43210, 11111, 22222, 33333]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12345, 67890, 13579, 24680, 111213, 415161, 718191]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12345, 67890, 13579, 24680, 111213, 415161, 718191]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000, 200000000, 30000000, 4000000, 500000, 60000, 7000, 800, 90, 10]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000, 200000000, 30000000, 4000000, 500000, 60000, 7000, 800, 90, 10]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [102030, 405060, 708090, 11121314, 1516171819]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [102030, 405060, 708090, 11121314, 1516171819]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 111222, 222333, 333444, 444555]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 111222, 222333, 333444, 444555]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [102030, 405060, 708090, 112131, 141516]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [102030, 405060, 708090, 112131, 141516]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12345678, 98765432, 13579246, 86420864, 24681357]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12345678, 98765432, 13579246, 86420864, 24681357]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234, 5678, 9101, 1122, 3344, 5566, 7788, 8899]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234, 5678, 9101, 1122, 3344, 5566, 7788, 8899]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 345, 6789, 101112, 13141516, 1718192021]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 345, 6789, 101112, 13141516, 1718192021]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 4567, 89012, 345678, 9012345]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 4567, 89012, 345678, 9012345]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 20000, 300000, 4000000, 50000000]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 20000, 300000, 4000000, 50000000]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9876543210, 123456789, 1000000000, 11111111, 2222]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9876543210, 123456789, 1000000000, 11111111, 2222]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234, 56789, 123456, 7890123, 45678901]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234, 56789, 123456, 7890123, 45678901]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10101010, 2020202, 303030, 40404, 5050, 606, 70, 8]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10101010, 2020202, 303030, 40404, 5050, 606, 70, 8]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50000, 40000, 30000, 20000, 10000, 9999, 8888, 7777, 6666, 5555]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50000, 40000, 30000, 20000, 10000, 9999, 8888, 7777, 6666, 5555]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 200000, 30000, 4000, 500]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 200000, 30000, 4000, 500]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100001, 100010, 100100, 101000, 110000, 200000, 300000, 400000, 500000, 600000]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100001, 100010, 100100, 101000, 110000, 200000, 300000, 400000, 500000, 600000]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [12, 345, 6789, 101112, 13141516, 17181920]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [12, 345, 6789, 101112, 13141516, 17181920]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 100000, 123456, 789012, 34567890]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 100000, 123456, 789012, 34567890]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9876543210, 123456789, 98765432, 1234567, 87654]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9876543210, 123456789, 98765432, 1234567, 87654]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 200000, 300000, 400000, 500000]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 200000, 300000, 400000, 500000]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10001, 20002, 30003, 40004, 50005, 60006, 70007, 80008, 90009]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10001, 20002, 30003, 40004, 50005, 60006, 70007, 80008, 90009]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 20000, 300, 40, 5]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 20000, 300, 40, 5]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 789012, 3333, 444444, 5555555]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 789012, 3333, 444444, 5555555]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 2000, 30000, 400000, 5000000]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 2000, 30000, 400000, 5000000]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 789012, 333333, 111, 2222]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 789012, 333333, 111, 2222]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 789012, 345678, 901234, 567890]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 789012, 345678, 901234, 567890]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 99, 999, 9999, 99999, 999999]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 99, 999, 9999, 99999, 999999]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11111111, 22222222, 33333333, 44444444, 55555555, 66666666, 77777777, 88888888, 99999999]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11111111, 22222222, 33333333, 44444444, 55555555, 66666666, 77777777, 88888888, 99999999]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 4567, 89012, 345678, 9012345, 67890123]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 4567, 89012, 345678, 9012345, 67890123]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [112233, 445566, 778899, 1122334455, 6677889900]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [112233, 445566, 778899, 1122334455, 6677889900]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234567, 2345678, 3456789, 4567890, 5678901]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234567, 2345678, 3456789, 4567890, 5678901]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 987654321, 246813579, 864208642, 135791357, 975319753, 246824682, 86428642, 13571357, 9759759]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 987654321, 246813579, 864208642, 135791357, 975319753, 246824682, 86428642, 13571357, 9759759]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 4567, 89012, 345678, 9012345, 67890123, 456789012, 34567890123, 2345678901234, 123456789012345]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 4567, 89012, 345678, 9012345, 67890123, 456789012, 34567890123, 2345678901234, 123456789012345]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, 400000, 300000, 200000, 100000, 99999]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, 400000, 300000, 200000, 100000, 99999]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [102030, 405060, 708090, 123456789, 987654321]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [102030, 405060, 708090, 123456789, 987654321]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006, 7007, 8008, 9009]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006, 7007, 8008, 9009]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 9876543210, 1122334455, 6677889900, 1234]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 9876543210, 1122334455, 6677889900, 1234]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1010, 2020, 3030, 4040, 5050, 6060, 7070, 8080, 9090]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1010, 2020, 3030, 4040, 5050, 6060, 7070, 8080, 9090]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 10000, 1000, 100, 10, 1, 11, 1111, 111111, 11111111]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 10000, 1000, 100, 10, 1, 11, 1111, 111111, 11111111]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 55, 555, 5555, 55555, 555555, 5555555, 55555555, 555555555, 5555555555]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 55, 555, 5555, 55555, 555555, 5555555, 55555555, 555555555, 5555555555]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 88888, 7777, 666, 55]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 88888, 7777, 666, 55]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999, 9999999999]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999, 9999999999]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654, 321, 456789, 123, 9009, 101010]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654, 321, 456789, 123, 9009, 101010]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1001, 22222, 333333, 4444444, 55555555, 666666666, 7777777777]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1001, 22222, 333333, 4444444, 55555555, 666666666, 7777777777]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 12345, 1234, 123, 12, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 12345, 1234, 123, 12, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [98765, 4321, 8642, 13579, 24680]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [98765, 4321, 8642, 13579, 24680]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11111111, 22222222, 33333333, 44444444, 55555555]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11111111, 22222222, 33333333, 44444444, 55555555]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 789012, 333333, 1111, 222222, 9999]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 789012, 333333, 1111, 222222, 9999]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101010, 202020, 303030, 404040, 505050]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101010, 202020, 303030, 404040, 505050]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234, 5678, 1122, 3344, 5566, 7788, 9900, 1100, 2200, 3300, 4400, 5500, 6600, 7700, 8800, 9900]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234, 5678, 1122, 3344, 5566, 7788, 9900, 1100, 2200, 3300, 4400, 5500, 6600, 7700, 8800, 9900]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 456789, 1000000, 999999, 1001001, 2002002, 3003003, 4004004, 5005005, 6006006]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 456789, 1000000, 999999, 1001001, 2002002, 3003003, 4004004, 5005005, 6006006]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 1000, 10000, 100000, 1000000]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 1000, 10000, 100000, 1000000]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [222222, 33333, 444444, 5555555, 666666]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [222222, 33333, 444444, 5555555, 666666]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456789, 98765432, 87654321, 7654321, 654321, 54321, 4321, 321, 21, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456789, 98765432, 87654321, 7654321, 654321, 54321, 4321, 321, 21, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123, 4567, 89012, 345678, 901234, 5678901, 23456789]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123, 4567, 89012, 345678, 901234, 5678901, 23456789]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11223344, 55667788, 99001122, 33445566, 77889900]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11223344, 55667788, 99001122, 33445566, 77889900]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [11, 222, 3333, 44444, 555555, 6666666, 77777777]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [11, 222, 3333, 44444, 555555, 6666666, 77777777]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [24680, 13579, 2468013579, 9876543210, 1122334455]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [24680, 13579, 2468013579, 9876543210, 1122334455]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1234, 123456, 12345678, 1234567890]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1234, 123456, 12345678, 1234567890]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 20002, 300030, 4000400, 50005000]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 20002, 300030, 4000400, 50005000]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 888888, 77777, 6666, 555, 44, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 888888, 77777, 6666, 555, 44, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [111111, 222222, 333333, 444444, 555555]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [111111, 222222, 333333, 444444, 555555]) == 5: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [10, 100, 1000, 10000, 100000]) == 3
    assert candidate(nums = [10, 100, 1000, 10000]) == 2
    assert candidate(nums = [10, 22, 333, 4444, 55555]) == 3
    assert candidate(nums = [100000, 10000, 1000, 100, 10]) == 3
    assert candidate(nums = [555, 901, 482, 1771]) == 1
    assert candidate(nums = [1, 22, 333, 4444, 55555, 666666]) == 3
    assert candidate(nums = [12, 345, 2, 6, 7896]) == 2
    assert candidate(nums = [1, 3, 5, 7, 9]) == 0
    assert candidate(nums = [1, 22, 333, 4444, 55555]) == 2
    assert candidate(nums = [1234, 56789, 101112, 13141516, 1718192021]) == 4
    assert candidate(nums = [9, 99, 999, 9999, 99999]) == 2
    assert candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000]) == 9
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 1
    assert candidate(nums = [111, 2222, 33333, 444444, 5555555, 66666666]) == 3
    assert candidate(nums = [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]) == 6
    assert candidate(nums = [123456789, 987654321, 111213141, 222324252, 333435363]) == 0
    assert candidate(nums = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]) == 0
    assert candidate(nums = [1, 11, 111, 1111, 11111, 111111]) == 3
    assert candidate(nums = [987654, 321, 654321, 987, 65432]) == 2
    assert candidate(nums = [222222, 444444, 666666, 888888, 1111111]) == 4
    assert candidate(nums = [111, 222, 333, 444, 555, 666, 777, 888, 999, 1000]) == 1
    assert candidate(nums = [123456, 789012, 34567, 11, 222222]) == 4
    assert candidate(nums = [111111, 222222, 333333, 444444, 555555, 666666, 777777, 888888, 999999]) == 9
    assert candidate(nums = [12, 345, 6789, 101112, 13141516]) == 4
    assert candidate(nums = [1234, 56789, 101112, 13141516, 1718192021]) == 4
    assert candidate(nums = [5, 55, 555, 5555, 55555, 555555, 5555555]) == 3
    assert candidate(nums = [9999, 88888, 777777, 6666666, 55555555]) == 3
    assert candidate(nums = [5555555555, 333333333, 11111111, 9999999, 777777, 55555, 3333, 111, 99, 7, 5]) == 5
    assert candidate(nums = [12345678, 87654321, 11223344, 55667788]) == 4
    assert candidate(nums = [1111111111, 222222222, 33333333, 4444444, 555555, 66666, 7777, 888, 99, 9]) == 5
    assert candidate(nums = [999, 8888, 77777, 666666, 5555555]) == 2
    assert candidate(nums = [987654, 876543, 765432, 654321, 543210]) == 5
    assert candidate(nums = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999]) == 4
    assert candidate(nums = [99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111]) == 0
    assert candidate(nums = [123456789, 987654321, 1122334455, 6677889900, 1010101010]) == 3
    assert candidate(nums = [102030, 204060, 306090, 408120, 510150]) == 5
    assert candidate(nums = [1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111]) == 5
    assert candidate(nums = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]) == 9
    assert candidate(nums = [1234567, 876543, 234567, 765432, 345678]) == 4
    assert candidate(nums = [1, 11, 111, 1111, 11111, 111111, 1111111, 11111111]) == 4
    assert candidate(nums = [987654, 123456789, 98765, 43210, 111111, 2222222]) == 2
    assert candidate(nums = [54321, 12345, 67890, 98765, 43210, 11111, 22222, 33333]) == 0
    assert candidate(nums = [12345, 67890, 13579, 24680, 111213, 415161, 718191]) == 3
    assert candidate(nums = [1000000000, 200000000, 30000000, 4000000, 500000, 60000, 7000, 800, 90, 10]) == 6
    assert candidate(nums = [102030, 405060, 708090, 11121314, 1516171819]) == 5
    assert candidate(nums = [123456, 111222, 222333, 333444, 444555]) == 5
    assert candidate(nums = [102030, 405060, 708090, 112131, 141516]) == 5
    assert candidate(nums = [12345678, 98765432, 13579246, 86420864, 24681357]) == 5
    assert candidate(nums = [1234, 5678, 9101, 1122, 3344, 5566, 7788, 8899]) == 8
    assert candidate(nums = [12, 345, 6789, 101112, 13141516, 1718192021]) == 5
    assert candidate(nums = [123, 4567, 89012, 345678, 9012345]) == 2
    assert candidate(nums = [1000, 20000, 300000, 4000000, 50000000]) == 3
    assert candidate(nums = [9876543210, 123456789, 1000000000, 11111111, 2222]) == 4
    assert candidate(nums = [1234, 56789, 123456, 7890123, 45678901]) == 3
    assert candidate(nums = [10101010, 2020202, 303030, 40404, 5050, 606, 70, 8]) == 4
    assert candidate(nums = [50000, 40000, 30000, 20000, 10000, 9999, 8888, 7777, 6666, 5555]) == 5
    assert candidate(nums = [1000000, 200000, 30000, 4000, 500]) == 2
    assert candidate(nums = [100001, 100010, 100100, 101000, 110000, 200000, 300000, 400000, 500000, 600000]) == 10
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]) == 5
    assert candidate(nums = [12, 345, 6789, 101112, 13141516, 17181920]) == 5
    assert candidate(nums = [5, 100000, 123456, 789012, 34567890]) == 4
    assert candidate(nums = [9876543210, 123456789, 98765432, 1234567, 87654]) == 2
    assert candidate(nums = [100000, 200000, 300000, 400000, 500000]) == 5
    assert candidate(nums = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]) == 1
    assert candidate(nums = [10001, 20002, 30003, 40004, 50005, 60006, 70007, 80008, 90009]) == 0
    assert candidate(nums = [100000, 20000, 300, 40, 5]) == 2
    assert candidate(nums = [123456, 789012, 3333, 444444, 5555555]) == 4
    assert candidate(nums = [100, 2000, 30000, 400000, 5000000]) == 2
    assert candidate(nums = [123456, 789012, 333333, 111, 2222]) == 4
    assert candidate(nums = [123456, 789012, 345678, 901234, 567890]) == 5
    assert candidate(nums = [9, 99, 999, 9999, 99999, 999999]) == 3
    assert candidate(nums = [11111111, 22222222, 33333333, 44444444, 55555555, 66666666, 77777777, 88888888, 99999999]) == 9
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == 9
    assert candidate(nums = [123, 4567, 89012, 345678, 9012345, 67890123]) == 3
    assert candidate(nums = [112233, 445566, 778899, 1122334455, 6677889900]) == 5
    assert candidate(nums = [1234567, 2345678, 3456789, 4567890, 5678901]) == 0
    assert candidate(nums = [100000, 99999, 88888, 77777, 66666, 55555, 44444, 33333, 22222, 11111]) == 1
    assert candidate(nums = [123456789, 987654321, 246813579, 864208642, 135791357, 975319753, 246824682, 86428642, 13571357, 9759759]) == 2
    assert candidate(nums = [123, 4567, 89012, 345678, 9012345, 67890123, 456789012, 34567890123, 2345678901234, 123456789012345]) == 3
    assert candidate(nums = [500000, 400000, 300000, 200000, 100000, 99999]) == 5
    assert candidate(nums = [102030, 405060, 708090, 123456789, 987654321]) == 3
    assert candidate(nums = [1001, 2002, 3003, 4004, 5005, 6006, 7007, 8008, 9009]) == 9
    assert candidate(nums = [123456789, 9876543210, 1122334455, 6677889900, 1234]) == 4
    assert candidate(nums = [1010, 2020, 3030, 4040, 5050, 6060, 7070, 8080, 9090]) == 9
    assert candidate(nums = [100000, 10000, 1000, 100, 10, 1, 11, 1111, 111111, 11111111]) == 7
    assert candidate(nums = [5, 55, 555, 5555, 55555, 555555, 5555555, 55555555, 555555555, 5555555555]) == 5
    assert candidate(nums = [999999, 88888, 7777, 666, 55]) == 3
    assert candidate(nums = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999, 9999999999]) == 5
    assert candidate(nums = [987654, 321, 456789, 123, 9009, 101010]) == 4
    assert candidate(nums = [1001, 22222, 333333, 4444444, 55555555, 666666666, 7777777777]) == 4
    assert candidate(nums = [123456, 12345, 1234, 123, 12, 1]) == 3
    assert candidate(nums = [98765, 4321, 8642, 13579, 24680]) == 2
    assert candidate(nums = [11111111, 22222222, 33333333, 44444444, 55555555]) == 5
    assert candidate(nums = [123456, 789012, 333333, 1111, 222222, 9999]) == 6
    assert candidate(nums = [101010, 202020, 303030, 404040, 505050]) == 5
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000]) == 3
    assert candidate(nums = [1234, 5678, 1122, 3344, 5566, 7788, 9900, 1100, 2200, 3300, 4400, 5500, 6600, 7700, 8800, 9900]) == 16
    assert candidate(nums = [123, 456789, 1000000, 999999, 1001001, 2002002, 3003003, 4004004, 5005005, 6006006]) == 2
    assert candidate(nums = [100, 1000, 10000, 100000, 1000000]) == 2
    assert candidate(nums = [222222, 33333, 444444, 5555555, 666666]) == 3
    assert candidate(nums = [123456789, 98765432, 87654321, 7654321, 654321, 54321, 4321, 321, 21, 1]) == 5
    assert candidate(nums = [123, 4567, 89012, 345678, 901234, 5678901, 23456789]) == 4
    assert candidate(nums = [11223344, 55667788, 99001122, 33445566, 77889900]) == 5
    assert candidate(nums = [11, 222, 3333, 44444, 555555, 6666666, 77777777]) == 4
    assert candidate(nums = [24680, 13579, 2468013579, 9876543210, 1122334455]) == 3
    assert candidate(nums = [1234, 123456, 12345678, 1234567890]) == 4
    assert candidate(nums = [1000, 20002, 300030, 4000400, 50005000]) == 3
    assert candidate(nums = [999999, 888888, 77777, 6666, 555, 44, 3]) == 4
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 9
    assert candidate(nums = [111111, 222222, 333333, 444444, 555555]) == 5


