def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000000000, 1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000000000, 1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 7, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 7, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000000000, 1000000000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000000000, 1000000000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000000000, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000000000, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 1, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 1, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 10, 15]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 10, 15]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1000000000, 1000000000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1000000000, 1000000000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [9, 3, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [9, 3, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 900000000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 900000000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [8, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [8, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1000000000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1000000000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [21, 17, 13, 9, 5, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [21, 17, 13, 9, 5, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [100, 100, 100, 100, 100, 99, 98, 97, 96, 95]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [100, 100, 100, 100, 100, 99, 98, 97, 96, 95]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 10, 15, 20, 25, 30]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 10, 15, 20, 25, 30]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [37, 11, 25, 7, 19]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [37, 11, 25, 7, 19]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1000000000, 1, 1000000000, 1, 1000000000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1000000000, 1, 1000000000, 1, 1000000000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 6, 10, 14, 18, 22]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 6, 10, 14, 18, 22]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [100, 100, 100, 100, 99]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [100, 100, 100, 100, 99]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [13, 11, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [13, 11, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [81, 27, 9, 3, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [81, 27, 9, 3, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 7, 9, 13, 21, 34, 55]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 7, 9, 13, 21, 34, 55]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 5, 15, 20]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 5, 15, 20]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [987, 654, 321]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [987, 654, 321]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [18, 5, 7]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [18, 5, 7]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 5, 11, 13, 17]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 5, 11, 13, 17]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [50, 25, 50, 25, 50, 25, 50, 25, 50, 25, 50, 25, 50, 25, 50, 25, 50, 25, 50, 25]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [50, 25, 50, 25, 50, 25, 50, 25, 50, 25, 50, 25, 50, 25, 50, 25, 50, 25, 50, 25]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [21, 15, 12]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [21, 15, 12]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000000000, 999999999, 999999998, 999999997, 999999996]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000000000, 999999999, 999999998, 999999997, 999999996]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [7, 14, 21, 28, 35, 42, 49]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [7, 14, 21, 28, 35, 42, 49]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000001]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000001]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [123456789, 987654321, 456789123, 321987654]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [123456789, 987654321, 456789123, 321987654]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [999999999, 999999999, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [999999999, 999999999, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [8, 13, 21, 34, 55, 89]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [8, 13, 21, 34, 55, 89]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [100, 99, 98, 97]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [100, 99, 98, 97]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000000000, 1, 1, 1, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000000000, 1, 1, 1, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [123456789, 987654321, 111111111]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [123456789, 987654321, 111111111]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [17, 7, 17, 7, 17]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [17, 7, 17, 7, 17]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [4, 12, 33, 55]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [4, 12, 33, 55]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000000000, 1000000000, 1000000000, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000000000, 1000000000, 1000000000, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [45, 12, 18, 30, 36, 24]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [45, 12, 18, 30, 36, 24]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [314159265, 271828182, 161803398, 141421356]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [314159265, 271828182, 161803398, 141421356]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [7, 11, 15, 22]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [7, 11, 15, 22]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [999999999, 1, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [999999999, 1, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [33, 17, 13]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [33, 17, 13]) == True: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 2, 3, 6, 11, 20, 37, 68]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 2, 3, 6, 11, 20, 37, 68]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [101, 103, 107, 109]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [101, 103, 107, 109]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 15, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 15, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [7, 18, 5, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [7, 18, 5, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 900000000, 900000000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 900000000, 900000000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [123456789, 987654321]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [123456789, 987654321]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [100, 200, 300, 400, 500]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [100, 200, 300, 400, 500]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1000000000, 1000000000, 1000000000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1000000000, 1000000000, 1000000000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [5, 11, 19, 29, 41]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [5, 11, 19, 29, 41]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000000]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000000]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 15, 20, 30]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 15, 20, 30]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000000000, 1000000000, 999999999, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000000000, 1000000000, 999999999, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [123456789, 987654321, 456789123, 321987654, 654321987, 789456123, 123789456, 456123789, 789654321, 987456123]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [123456789, 987654321, 456789123, 321987654, 654321987, 789456123, 123789456, 456123789, 789654321, 987456123]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 9, 20, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 9, 20, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]) == False: {e}')
    
    total += 1
    try:
        result = candidate(target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == False: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(target = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
    assert candidate(target = [1, 2, 3, 4, 5]) == False
    assert candidate(target = [1000000000, 1, 1]) == False
    assert candidate(target = [5, 7, 1]) == True
    assert candidate(target = [10, 1]) == True
    assert candidate(target = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == False
    assert candidate(target = [5, 5, 5]) == False
    assert candidate(target = [1000000000, 1000000000]) == False
    assert candidate(target = [1000000000, 1]) == True
    assert candidate(target = [1, 1, 1, 2]) == False
    assert candidate(target = [5, 10, 15]) == False
    assert candidate(target = [1, 1000000000, 1000000000]) == False
    assert candidate(target = [9, 3, 5]) == True
    assert candidate(target = [1, 1, 1]) == True
    assert candidate(target = [2, 900000000]) == False
    assert candidate(target = [8, 5]) == True
    assert candidate(target = [1, 1000000000]) == True
    assert candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(target = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7]) == False
    assert candidate(target = [1000000000, 500000000, 250000000, 125000000, 62500000, 31250000, 15625000, 7812500, 3906250, 1953125]) == False
    assert candidate(target = [21, 17, 13, 9, 5, 1]) == False
    assert candidate(target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == False
    assert candidate(target = [100, 100, 100, 100, 100, 99, 98, 97, 96, 95]) == False
    assert candidate(target = [5, 10, 15, 20, 25, 30]) == False
    assert candidate(target = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == False
    assert candidate(target = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]) == False
    assert candidate(target = [37, 11, 25, 7, 19]) == False
    assert candidate(target = [41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131]) == False
    assert candidate(target = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == False
    assert candidate(target = [1, 1000000000, 1, 1000000000, 1, 1000000000]) == False
    assert candidate(target = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]) == False
    assert candidate(target = [2, 6, 10, 14, 18, 22]) == False
    assert candidate(target = [100, 100, 100, 100, 99]) == False
    assert candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 20]) == False
    assert candidate(target = [13, 11, 10]) == False
    assert candidate(target = [81, 27, 9, 3, 1]) == False
    assert candidate(target = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == False
    assert candidate(target = [5, 7, 9, 13, 21, 34, 55]) == False
    assert candidate(target = [10, 5, 15, 20]) == False
    assert candidate(target = [987, 654, 321]) == False
    assert candidate(target = [18, 5, 7]) == False
    assert candidate(target = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == False
    assert candidate(target = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == False
    assert candidate(target = [3, 5, 11, 13, 17]) == False
    assert candidate(target = [50, 25, 50, 25, 50, 25, 50, 25, 50, 25, 50, 25, 50, 25, 50, 25, 50, 25, 50, 25]) == False
    assert candidate(target = [1000000000, 999999999, 999999998, 999999997, 999999996, 999999995, 999999994]) == False
    assert candidate(target = [21, 15, 12]) == False
    assert candidate(target = [1000000000, 999999999, 999999998, 999999997, 999999996]) == False
    assert candidate(target = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
    assert candidate(target = [7, 14, 21, 28, 35, 42, 49]) == False
    assert candidate(target = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000001]) == False
    assert candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == True
    assert candidate(target = [123456789, 987654321, 456789123, 321987654]) == False
    assert candidate(target = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]) == False
    assert candidate(target = [999999999, 999999999, 1]) == False
    assert candidate(target = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == False
    assert candidate(target = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
    assert candidate(target = [8, 13, 21, 34, 55, 89]) == False
    assert candidate(target = [100, 99, 98, 97]) == False
    assert candidate(target = [1000000000, 1, 1, 1, 1]) == False
    assert candidate(target = [123456789, 987654321, 111111111]) == False
    assert candidate(target = [17, 7, 17, 7, 17]) == False
    assert candidate(target = [4, 12, 33, 55]) == False
    assert candidate(target = [1000000000, 1000000000, 1000000000, 1]) == False
    assert candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == False
    assert candidate(target = [45, 12, 18, 30, 36, 24]) == False
    assert candidate(target = [314159265, 271828182, 161803398, 141421356]) == False
    assert candidate(target = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]) == False
    assert candidate(target = [7, 11, 15, 22]) == False
    assert candidate(target = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == False
    assert candidate(target = [17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17]) == False
    assert candidate(target = [999999999, 1, 999999998, 999999997, 999999996, 999999995, 999999994, 999999993, 999999992, 999999991]) == False
    assert candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000000]) == False
    assert candidate(target = [33, 17, 13]) == True
    assert candidate(target = [1, 1, 2, 3, 6, 11, 20, 37, 68]) == False
    assert candidate(target = [101, 103, 107, 109]) == False
    assert candidate(target = [10, 15, 3]) == False
    assert candidate(target = [7, 18, 5, 4]) == False
    assert candidate(target = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == False
    assert candidate(target = [2, 900000000, 900000000]) == False
    assert candidate(target = [123456789, 987654321]) == False
    assert candidate(target = [100, 200, 300, 400, 500]) == False
    assert candidate(target = [1, 1000000000, 1000000000, 1000000000]) == False
    assert candidate(target = [2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]) == False
    assert candidate(target = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]) == False
    assert candidate(target = [5, 11, 19, 29, 41]) == False
    assert candidate(target = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1000000000]) == False
    assert candidate(target = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]) == False
    assert candidate(target = [10, 15, 20, 30]) == False
    assert candidate(target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 1]) == False
    assert candidate(target = [1000000000, 1000000000, 999999999, 1]) == False
    assert candidate(target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == False
    assert candidate(target = [123456789, 987654321, 456789123, 321987654, 654321987, 789456123, 123789456, 456123789, 789654321, 987456123]) == False
    assert candidate(target = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1]) == False
    assert candidate(target = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == False
    assert candidate(target = [3, 9, 20, 5]) == False
    assert candidate(target = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1]) == False
    assert candidate(target = [3, 6, 12, 24, 48, 96, 192, 384, 768, 1536]) == False
    assert candidate(target = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == False


