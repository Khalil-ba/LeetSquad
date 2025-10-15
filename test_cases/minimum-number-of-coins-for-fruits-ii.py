def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100000, 99999, 99998, 99997, 99996]) == 199998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100000, 99999, 99998, 99997, 99996]) == 199998: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 10, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 10, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100000, 100000, 100000, 100000, 100000]) == 200000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100000, 100000, 100000, 100000, 100000]) == 200000: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100002
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100002: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 1, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 1, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 3, 4, 5, 6]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 3, 4, 5, 6]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 648
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 648: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 2, 3, 4, 5]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 2, 3, 4, 5]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100000, 100000, 100000, 100000, 100000]) == 200000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100000, 100000, 100000, 100000, 100000]) == 200000: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 200, 300, 400, 500]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 200, 300, 400, 500]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 2, 2, 2, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 2, 2, 2, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1500, 1400, 1300, 1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 3800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1500, 1400, 1300, 1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 3800: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 531
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 531: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 10, 7, 11, 8, 12, 9, 13, 10, 14]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 10, 7, 11, 8, 12, 9, 13, 10, 14]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 50, 10, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 112
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 50, 10, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 112: {e}')
    
    total += 1
    try:
        result = candidate(prices = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 98: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 1, 6, 5, 4, 7, 8, 9, 10]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 1, 6, 5, 4, 7, 8, 9, 10]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 20737
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 20737: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1]) == 100003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1]) == 100003: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 50, 25, 12, 6, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 127
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 50, 25, 12, 6, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 127: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 100]) == 103
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 100]) == 103: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1]) == 100003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1]) == 100003: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 38: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 5, 2, 1, 3, 4, 1, 2, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 5, 2, 1, 3, 4, 1, 2, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [7, 4, 1, 6, 5, 8, 2, 3, 4, 1]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [7, 4, 1, 6, 5, 8, 2, 3, 4, 1]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 58: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 800: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 10, 30, 20, 10, 40, 30, 20, 10, 50, 40, 30, 20, 10]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 10, 30, 20, 10, 40, 30, 20, 10, 50, 40, 30, 20, 10]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 10, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60, 7, 70, 8, 80, 9, 90, 10, 100]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 10, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60, 7, 70, 8, 80, 9, 90, 10, 100]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 200, 100, 300, 200, 100, 400, 300, 200, 100]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 200, 100, 300, 200, 100, 400, 300, 200, 100]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 139
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 139: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 4, 1, 5, 2, 3, 1, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 4, 1, 5, 2, 3, 1, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 26
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 26: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == 220000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == 220000: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 200, 300, 400, 500, 1, 2, 3, 4, 5]) == 401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 200, 300, 400, 500, 1, 2, 3, 4, 5]) == 401: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == 102: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 100000, 1, 1, 1, 100000, 1, 1, 1, 100000, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 100000, 1, 1, 1, 100000, 1, 1, 1, 100000, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 59
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 59: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 50, 20, 10, 5, 3, 2, 1, 1, 1]) == 122
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 50, 20, 10, 5, 3, 2, 1, 1, 1]) == 122: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 4000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 4000: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 2, 1, 2, 3, 4, 5, 6, 7, 8]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 2, 1, 2, 3, 4, 5, 6, 7, 8]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 3, 8, 6, 2, 7, 9, 4, 1, 10, 15, 12, 14, 11, 13]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 3, 8, 6, 2, 7, 9, 4, 1, 10, 15, 12, 14, 11, 13]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 10, 100, 1000, 10000, 100000, 99999, 9999, 999, 99]) == 2010
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 10, 100, 1000, 10000, 100000, 99999, 9999, 999, 99]) == 2010: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 2, 1, 10, 3, 1, 10, 4, 1, 10, 5, 1, 10, 6, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 2, 1, 10, 3, 1, 10, 4, 1, 10, 5, 1, 10, 6, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 13: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(prices = [1, 2, 3]) == 3
    assert candidate(prices = [5, 5, 5, 5, 5]) == 10
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 22
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3
    assert candidate(prices = [100000, 99999, 99998, 99997, 99996]) == 199998
    assert candidate(prices = [1, 2]) == 1
    assert candidate(prices = [1, 10, 1, 1]) == 2
    assert candidate(prices = [1]) == 1
    assert candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 19
    assert candidate(prices = [100000, 100000, 100000, 100000, 100000]) == 200000
    assert candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]) == 26
    assert candidate(prices = [100000, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 100002
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8
    assert candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 80
    assert candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 13
    assert candidate(prices = [3, 1, 2]) == 4
    assert candidate(prices = [2, 3, 4, 5, 6]) == 6
    assert candidate(prices = [512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 648
    assert candidate(prices = [5, 2, 3, 4, 5]) == 8
    assert candidate(prices = [100000, 100000, 100000, 100000, 100000]) == 200000
    assert candidate(prices = [100, 200, 300, 400, 500]) == 400
    assert candidate(prices = [5, 4, 3, 2, 1]) == 8
    assert candidate(prices = [1, 2, 3, 4, 5]) == 4
    assert candidate(prices = [2, 2, 2, 2, 2]) == 4
    assert candidate(prices = [5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3, 5, 3]) == 16
    assert candidate(prices = [1500, 1400, 1300, 1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 3800
    assert candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 3
    assert candidate(prices = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 8
    assert candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 531
    assert candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]) == 75
    assert candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20
    assert candidate(prices = [1, 3, 2, 5, 4, 7, 6, 9, 8, 11, 10, 13, 12, 15, 14]) == 15
    assert candidate(prices = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]) == 8
    assert candidate(prices = [1, 5, 2, 6, 3, 7, 4, 8, 5, 9, 6, 10, 7, 11, 8, 12, 9, 13, 10, 14]) == 12
    assert candidate(prices = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5]) == 8
    assert candidate(prices = [100, 50, 10, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 112
    assert candidate(prices = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 98
    assert candidate(prices = [3, 2, 1, 6, 5, 4, 7, 8, 9, 10]) == 8
    assert candidate(prices = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 20737
    assert candidate(prices = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1]) == 100003
    assert candidate(prices = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10, 20, 30, 40, 50]) == 90
    assert candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 14
    assert candidate(prices = [1, 100000, 2, 99999, 3, 99998, 4, 99997, 5, 99996]) == 6
    assert candidate(prices = [100, 50, 25, 12, 6, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 127
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(prices = [100, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 100]) == 103
    assert candidate(prices = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1]) == 100003
    assert candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
    assert candidate(prices = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 8
    assert candidate(prices = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]) == 4
    assert candidate(prices = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 72
    assert candidate(prices = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 5
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) == 6
    assert candidate(prices = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 38
    assert candidate(prices = [3, 2, 5, 2, 1, 3, 4, 1, 2, 3]) == 6
    assert candidate(prices = [7, 4, 1, 6, 5, 8, 2, 3, 4, 1]) == 10
    assert candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 58
    assert candidate(prices = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 800
    assert candidate(prices = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 12
    assert candidate(prices = [10, 20, 10, 30, 20, 10, 40, 30, 20, 10, 50, 40, 30, 20, 10]) == 40
    assert candidate(prices = [1, 10, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60, 7, 70, 8, 80, 9, 90, 10, 100]) == 12
    assert candidate(prices = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 8
    assert candidate(prices = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20]) == 40
    assert candidate(prices = [100, 200, 100, 300, 200, 100, 400, 300, 200, 100]) == 300
    assert candidate(prices = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 8
    assert candidate(prices = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2]) == 6
    assert candidate(prices = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]) == 8
    assert candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 26
    assert candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 40
    assert candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 4
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 139
    assert candidate(prices = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 6
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 7
    assert candidate(prices = [1, 3, 2, 4, 1, 5, 2, 3, 1, 6]) == 4
    assert candidate(prices = [8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 17
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 23
    assert candidate(prices = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 15
    assert candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 4
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 18
    assert candidate(prices = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6]) == 9
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 26
    assert candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 30
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 23
    assert candidate(prices = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]) == 1500
    assert candidate(prices = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000]) == 220000
    assert candidate(prices = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]) == 6
    assert candidate(prices = [100, 200, 300, 400, 500, 1, 2, 3, 4, 5]) == 401
    assert candidate(prices = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]) == 5
    assert candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == 19
    assert candidate(prices = [100, 1, 1, 1, 1, 1, 1, 1, 1, 100]) == 102
    assert candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 3
    assert candidate(prices = [3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3, 1, 1, 1, 1, 3, 3, 3, 3, 1]) == 8
    assert candidate(prices = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 7
    assert candidate(prices = [1, 1, 1, 100000, 1, 1, 1, 100000, 1, 1, 1, 100000, 1, 1, 1]) == 4
    assert candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 59
    assert candidate(prices = [100, 50, 20, 10, 5, 3, 2, 1, 1, 1]) == 122
    assert candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 126
    assert candidate(prices = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]) == 4
    assert candidate(prices = [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]) == 6
    assert candidate(prices = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]) == 4000
    assert candidate(prices = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 9
    assert candidate(prices = [3, 2, 1, 2, 3, 4, 5, 6, 7, 8]) == 7
    assert candidate(prices = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 10
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 6
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]) == 8
    assert candidate(prices = [1, 2, 3, 2, 1, 4, 5, 4, 3, 2]) == 4
    assert candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 13
    assert candidate(prices = [5, 3, 8, 6, 2, 7, 9, 4, 1, 10, 15, 12, 14, 11, 13]) == 11
    assert candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 14
    assert candidate(prices = [1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 4
    assert candidate(prices = [1, 10, 100, 1000, 10000, 100000, 99999, 9999, 999, 99]) == 2010
    assert candidate(prices = [10, 2, 1, 10, 3, 1, 10, 4, 1, 10, 5, 1, 10, 6, 1]) == 13
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 13


