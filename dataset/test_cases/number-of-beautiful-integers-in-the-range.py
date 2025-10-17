def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(low = 100,high = 200,k = 4) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100,high = 200,k = 4) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 100,high = 200,k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100,high = 200,k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 10,high = 20,k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10,high = 20,k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 10,k = 1) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 10,k = 1) == 1: {e}')
    
    total += 1
    try:
        result = candidate(low = 100,high = 200,k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100,high = 200,k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 123,high = 456,k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 123,high = 456,k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000,high = 10000,k = 7) == 483
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000,high = 10000,k = 7) == 483: {e}')
    
    total += 1
    try:
        result = candidate(low = 123,high = 456,k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 123,high = 456,k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 5,high = 5,k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5,high = 5,k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000,high = 10000,k = 11) == 460
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000,high = 10000,k = 11) == 460: {e}')
    
    total += 1
    try:
        result = candidate(low = 999999,high = 999999,k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 999999,high = 999999,k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 123456,high = 654321,k = 15) == 11026
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 123456,high = 654321,k = 15) == 11026: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000,high = 9999,k = 11) == 460
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000,high = 9999,k = 11) == 460: {e}')
    
    total += 1
    try:
        result = candidate(low = 100000,high = 999999,k = 19) == 14801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100000,high = 999999,k = 19) == 14801: {e}')
    
    total += 1
    try:
        result = candidate(low = 9876543,high = 12345678,k = 16) == 44999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 9876543,high = 12345678,k = 16) == 44999: {e}')
    
    total += 1
    try:
        result = candidate(low = 111111,high = 222222,k = 12) == 3183
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 111111,high = 222222,k = 12) == 3183: {e}')
    
    total += 1
    try:
        result = candidate(low = 99999,high = 100001,k = 1) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 99999,high = 100001,k = 1) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000000,high = 8000000,k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000000,high = 8000000,k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 100000,high = 500000,k = 19) == 6575
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100000,high = 500000,k = 19) == 6575: {e}')
    
    total += 1
    try:
        result = candidate(low = 1234567,high = 7654321,k = 18) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1234567,high = 7654321,k = 18) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 345678,high = 876543,k = 20) == 6510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 345678,high = 876543,k = 20) == 6510: {e}')
    
    total += 1
    try:
        result = candidate(low = 5000,high = 15000,k = 13) == 147
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5000,high = 15000,k = 13) == 147: {e}')
    
    total += 1
    try:
        result = candidate(low = 100000,high = 1000000,k = 17) == 16544
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100000,high = 1000000,k = 17) == 16544: {e}')
    
    total += 1
    try:
        result = candidate(low = 1234,high = 5678,k = 9) == 251
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1234,high = 5678,k = 9) == 251: {e}')
    
    total += 1
    try:
        result = candidate(low = 10000000,high = 20000000,k = 9) == 306040
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10000000,high = 20000000,k = 9) == 306040: {e}')
    
    total += 1
    try:
        result = candidate(low = 5000,high = 50000,k = 3) == 627
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 5000,high = 50000,k = 3) == 627: {e}')
    
    total += 1
    try:
        result = candidate(low = 250000,high = 350000,k = 5) == 6500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 250000,high = 350000,k = 5) == 6500: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000000,high = 10000000,k = 19) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000000,high = 10000000,k = 19) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 50000000,high = 60000000,k = 20) == 156250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 50000000,high = 60000000,k = 20) == 156250: {e}')
    
    total += 1
    try:
        result = candidate(low = 99999,high = 100000,k = 13) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 99999,high = 100000,k = 13) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 111111111,high = 222222222,k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 111111111,high = 222222222,k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000000,high = 2000000,k = 19) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000000,high = 2000000,k = 19) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 777777,high = 888888,k = 18) == 1644
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 777777,high = 888888,k = 18) == 1644: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000,high = 10000,k = 12) == 276
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000,high = 10000,k = 12) == 276: {e}')
    
    total += 1
    try:
        result = candidate(low = 987654321,high = 987654321,k = 11) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 987654321,high = 987654321,k = 11) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 1234,high = 5678,k = 17) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1234,high = 5678,k = 17) == 101: {e}')
    
    total += 1
    try:
        result = candidate(low = 100000000,high = 999999999,k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100000000,high = 999999999,k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 123456,high = 789012,k = 17) == 12253
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 123456,high = 789012,k = 17) == 12253: {e}')
    
    total += 1
    try:
        result = candidate(low = 1111111,high = 2222222,k = 14) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1111111,high = 2222222,k = 14) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 10000,high = 99999,k = 17) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10000,high = 99999,k = 17) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 123456789,high = 987654321,k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 123456789,high = 987654321,k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000,high = 10000,k = 13) == 263
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000,high = 10000,k = 13) == 263: {e}')
    
    total += 1
    try:
        result = candidate(low = 12345,high = 67890,k = 17) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 12345,high = 67890,k = 17) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 500000000,high = 600000000,k = 13) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 500000000,high = 600000000,k = 13) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 50000,high = 60000,k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 50000,high = 60000,k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 100000000,high = 999999999,k = 17) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100000000,high = 999999999,k = 17) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 500,high = 2000,k = 17) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 500,high = 2000,k = 17) == 21: {e}')
    
    total += 1
    try:
        result = candidate(low = 11111,high = 22222,k = 14) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 11111,high = 22222,k = 14) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 123456,high = 789012,k = 15) == 13887
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 123456,high = 789012,k = 15) == 13887: {e}')
    
    total += 1
    try:
        result = candidate(low = 2000,high = 3000,k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 2000,high = 3000,k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 3333333,high = 4444444,k = 16) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 3333333,high = 4444444,k = 16) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 987654321,high = 987654321,k = 19) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 987654321,high = 987654321,k = 19) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 10000,high = 100000,k = 13) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10000,high = 100000,k = 13) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 123456,high = 654321,k = 3) == 55100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 123456,high = 654321,k = 3) == 55100: {e}')
    
    total += 1
    try:
        result = candidate(low = 555555,high = 666666,k = 16) == 1899
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 555555,high = 666666,k = 16) == 1899: {e}')
    
    total += 1
    try:
        result = candidate(low = 500000,high = 600000,k = 20) == 1875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 500000,high = 600000,k = 20) == 1875: {e}')
    
    total += 1
    try:
        result = candidate(low = 111111,high = 222222,k = 13) == 2615
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 111111,high = 222222,k = 13) == 2615: {e}')
    
    total += 1
    try:
        result = candidate(low = 123456,high = 654321,k = 17) == 9719
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 123456,high = 654321,k = 17) == 9719: {e}')
    
    total += 1
    try:
        result = candidate(low = 234567,high = 765432,k = 25) == 6663
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 234567,high = 765432,k = 25) == 6663: {e}')
    
    total += 1
    try:
        result = candidate(low = 99990,high = 100000,k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 99990,high = 100000,k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 12345678,high = 87654321,k = 16) == 1236425
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 12345678,high = 87654321,k = 16) == 1236425: {e}')
    
    total += 1
    try:
        result = candidate(low = 987654,high = 9876543,k = 3) == 1120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 987654,high = 9876543,k = 3) == 1120: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000,high = 9999,k = 12) == 276
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000,high = 9999,k = 12) == 276: {e}')
    
    total += 1
    try:
        result = candidate(low = 123456789,high = 987654321,k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 123456789,high = 987654321,k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 100000,high = 1000000,k = 19) == 14801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100000,high = 1000000,k = 19) == 14801: {e}')
    
    total += 1
    try:
        result = candidate(low = 123456,high = 654321,k = 19) == 8693
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 123456,high = 654321,k = 19) == 8693: {e}')
    
    total += 1
    try:
        result = candidate(low = 500000,high = 550000,k = 20) == 875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 500000,high = 550000,k = 20) == 875: {e}')
    
    total += 1
    try:
        result = candidate(low = 1234567,high = 8765432,k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1234567,high = 8765432,k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 10000000,high = 20000000,k = 5) == 546875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10000000,high = 20000000,k = 5) == 546875: {e}')
    
    total += 1
    try:
        result = candidate(low = 11111111,high = 22222222,k = 7) == 426428
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 11111111,high = 22222222,k = 7) == 426428: {e}')
    
    total += 1
    try:
        result = candidate(low = 55555555,high = 88888888,k = 9) == 1034831
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 55555555,high = 88888888,k = 9) == 1034831: {e}')
    
    total += 1
    try:
        result = candidate(low = 100,high = 1000,k = 3) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100,high = 1000,k = 3) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 999,high = 1000000,k = 13) == 21897
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 999,high = 1000000,k = 13) == 21897: {e}')
    
    total += 1
    try:
        result = candidate(low = 100000,high = 999999,k = 3) == 93760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100000,high = 999999,k = 3) == 93760: {e}')
    
    total += 1
    try:
        result = candidate(low = 100,high = 1000,k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100,high = 1000,k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 100,high = 999,k = 9) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100,high = 999,k = 9) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 123456789,high = 987654321,k = 18) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 123456789,high = 987654321,k = 18) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 200000,high = 300000,k = 5) == 6250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 200000,high = 300000,k = 5) == 6250: {e}')
    
    total += 1
    try:
        result = candidate(low = 100,high = 1000,k = 5) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100,high = 1000,k = 5) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 111111,high = 222222,k = 19) == 1785
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 111111,high = 222222,k = 19) == 1785: {e}')
    
    total += 1
    try:
        result = candidate(low = 500000,high = 600000,k = 19) == 1643
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 500000,high = 600000,k = 19) == 1643: {e}')
    
    total += 1
    try:
        result = candidate(low = 10000000,high = 20000000,k = 18) == 174880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10000000,high = 20000000,k = 18) == 174880: {e}')
    
    total += 1
    try:
        result = candidate(low = 100000,high = 999999,k = 17) == 16544
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100000,high = 999999,k = 17) == 16544: {e}')
    
    total += 1
    try:
        result = candidate(low = 111111,high = 222222,k = 21) == 1614
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 111111,high = 222222,k = 21) == 1614: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000000,high = 10000000,k = 2) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000000,high = 10000000,k = 2) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 333333,high = 444444,k = 14) == 2525
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 333333,high = 444444,k = 14) == 2525: {e}')
    
    total += 1
    try:
        result = candidate(low = 1111111,high = 8888888,k = 20) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1111111,high = 8888888,k = 20) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 10000,high = 100000,k = 11) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10000,high = 100000,k = 11) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 100,high = 1000,k = 11) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 100,high = 1000,k = 11) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 1234,high = 8765,k = 11) == 386
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1234,high = 8765,k = 11) == 386: {e}')
    
    total += 1
    try:
        result = candidate(low = 750000,high = 850000,k = 7) == 4287
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 750000,high = 850000,k = 7) == 4287: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000000,high = 10000000,k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000000,high = 10000000,k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 111111,high = 222222,k = 18) == 2196
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 111111,high = 222222,k = 18) == 2196: {e}')
    
    total += 1
    try:
        result = candidate(low = 234567,high = 765432,k = 18) == 10488
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 234567,high = 765432,k = 18) == 10488: {e}')
    
    total += 1
    try:
        result = candidate(low = 11111,high = 99999,k = 13) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 11111,high = 99999,k = 13) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 333333333,high = 666666666,k = 7) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 333333333,high = 666666666,k = 7) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 1,high = 1000000000,k = 20) == 1105750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1,high = 1000000000,k = 20) == 1105750: {e}')
    
    total += 1
    try:
        result = candidate(low = 1000000,high = 2000000,k = 15) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 1000000,high = 2000000,k = 15) == 0: {e}')
    
    total += 1
    try:
        result = candidate(low = 10000,high = 99999,k = 13) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(low = 10000,high = 99999,k = 13) == 0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(low = 100,high = 200,k = 4) == 0
    assert candidate(low = 100,high = 200,k = 5) == 0
    assert candidate(low = 10,high = 20,k = 3) == 2
    assert candidate(low = 1,high = 10,k = 1) == 1
    assert candidate(low = 100,high = 200,k = 7) == 0
    assert candidate(low = 123,high = 456,k = 7) == 0
    assert candidate(low = 1000,high = 10000,k = 7) == 483
    assert candidate(low = 123,high = 456,k = 5) == 0
    assert candidate(low = 5,high = 5,k = 2) == 0
    assert candidate(low = 1000,high = 10000,k = 11) == 460
    assert candidate(low = 999999,high = 999999,k = 1) == 0
    assert candidate(low = 123456,high = 654321,k = 15) == 11026
    assert candidate(low = 1000,high = 9999,k = 11) == 460
    assert candidate(low = 100000,high = 999999,k = 19) == 14801
    assert candidate(low = 9876543,high = 12345678,k = 16) == 44999
    assert candidate(low = 111111,high = 222222,k = 12) == 3183
    assert candidate(low = 99999,high = 100001,k = 1) == 0
    assert candidate(low = 1000000,high = 8000000,k = 7) == 0
    assert candidate(low = 100000,high = 500000,k = 19) == 6575
    assert candidate(low = 1234567,high = 7654321,k = 18) == 0
    assert candidate(low = 345678,high = 876543,k = 20) == 6510
    assert candidate(low = 5000,high = 15000,k = 13) == 147
    assert candidate(low = 100000,high = 1000000,k = 17) == 16544
    assert candidate(low = 1234,high = 5678,k = 9) == 251
    assert candidate(low = 10000000,high = 20000000,k = 9) == 306040
    assert candidate(low = 5000,high = 50000,k = 3) == 627
    assert candidate(low = 250000,high = 350000,k = 5) == 6500
    assert candidate(low = 1000000,high = 10000000,k = 19) == 0
    assert candidate(low = 50000000,high = 60000000,k = 20) == 156250
    assert candidate(low = 99999,high = 100000,k = 13) == 0
    assert candidate(low = 111111111,high = 222222222,k = 7) == 0
    assert candidate(low = 1000000,high = 2000000,k = 19) == 0
    assert candidate(low = 777777,high = 888888,k = 18) == 1644
    assert candidate(low = 1000,high = 10000,k = 12) == 276
    assert candidate(low = 987654321,high = 987654321,k = 11) == 0
    assert candidate(low = 1234,high = 5678,k = 17) == 101
    assert candidate(low = 100000000,high = 999999999,k = 3) == 0
    assert candidate(low = 123456,high = 789012,k = 17) == 12253
    assert candidate(low = 1111111,high = 2222222,k = 14) == 0
    assert candidate(low = 10000,high = 99999,k = 17) == 0
    assert candidate(low = 123456789,high = 987654321,k = 9) == 0
    assert candidate(low = 1000,high = 10000,k = 13) == 263
    assert candidate(low = 12345,high = 67890,k = 17) == 0
    assert candidate(low = 500000000,high = 600000000,k = 13) == 0
    assert candidate(low = 50000,high = 60000,k = 15) == 0
    assert candidate(low = 100000000,high = 999999999,k = 17) == 0
    assert candidate(low = 500,high = 2000,k = 17) == 21
    assert candidate(low = 11111,high = 22222,k = 14) == 0
    assert candidate(low = 123456,high = 789012,k = 15) == 13887
    assert candidate(low = 2000,high = 3000,k = 20) == 0
    assert candidate(low = 3333333,high = 4444444,k = 16) == 0
    assert candidate(low = 987654321,high = 987654321,k = 19) == 0
    assert candidate(low = 10000,high = 100000,k = 13) == 0
    assert candidate(low = 123456,high = 654321,k = 3) == 55100
    assert candidate(low = 555555,high = 666666,k = 16) == 1899
    assert candidate(low = 500000,high = 600000,k = 20) == 1875
    assert candidate(low = 111111,high = 222222,k = 13) == 2615
    assert candidate(low = 123456,high = 654321,k = 17) == 9719
    assert candidate(low = 234567,high = 765432,k = 25) == 6663
    assert candidate(low = 99990,high = 100000,k = 2) == 0
    assert candidate(low = 12345678,high = 87654321,k = 16) == 1236425
    assert candidate(low = 987654,high = 9876543,k = 3) == 1120
    assert candidate(low = 1000,high = 9999,k = 12) == 276
    assert candidate(low = 123456789,high = 987654321,k = 5) == 0
    assert candidate(low = 100000,high = 1000000,k = 19) == 14801
    assert candidate(low = 123456,high = 654321,k = 19) == 8693
    assert candidate(low = 500000,high = 550000,k = 20) == 875
    assert candidate(low = 1234567,high = 8765432,k = 5) == 0
    assert candidate(low = 10000000,high = 20000000,k = 5) == 546875
    assert candidate(low = 11111111,high = 22222222,k = 7) == 426428
    assert candidate(low = 55555555,high = 88888888,k = 9) == 1034831
    assert candidate(low = 100,high = 1000,k = 3) == 0
    assert candidate(low = 999,high = 1000000,k = 13) == 21897
    assert candidate(low = 100000,high = 999999,k = 3) == 93760
    assert candidate(low = 100,high = 1000,k = 9) == 0
    assert candidate(low = 100,high = 999,k = 9) == 0
    assert candidate(low = 123456789,high = 987654321,k = 18) == 0
    assert candidate(low = 200000,high = 300000,k = 5) == 6250
    assert candidate(low = 100,high = 1000,k = 5) == 0
    assert candidate(low = 111111,high = 222222,k = 19) == 1785
    assert candidate(low = 500000,high = 600000,k = 19) == 1643
    assert candidate(low = 10000000,high = 20000000,k = 18) == 174880
    assert candidate(low = 100000,high = 999999,k = 17) == 16544
    assert candidate(low = 111111,high = 222222,k = 21) == 1614
    assert candidate(low = 1000000,high = 10000000,k = 2) == 0
    assert candidate(low = 333333,high = 444444,k = 14) == 2525
    assert candidate(low = 1111111,high = 8888888,k = 20) == 0
    assert candidate(low = 10000,high = 100000,k = 11) == 0
    assert candidate(low = 100,high = 1000,k = 11) == 0
    assert candidate(low = 1234,high = 8765,k = 11) == 386
    assert candidate(low = 750000,high = 850000,k = 7) == 4287
    assert candidate(low = 1000000,high = 10000000,k = 15) == 0
    assert candidate(low = 111111,high = 222222,k = 18) == 2196
    assert candidate(low = 234567,high = 765432,k = 18) == 10488
    assert candidate(low = 11111,high = 99999,k = 13) == 0
    assert candidate(low = 333333333,high = 666666666,k = 7) == 0
    assert candidate(low = 1,high = 1000000000,k = 20) == 1105750
    assert candidate(low = 1000000,high = 2000000,k = 15) == 0
    assert candidate(low = 10000,high = 99999,k = 13) == 0


