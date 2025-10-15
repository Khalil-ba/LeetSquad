def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(prices = [1, 10, 1, 1]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 10, 1, 1]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 1, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 1, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 40, 50]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 40, 50]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 1, 100, 1, 100]) == 102
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 1, 100, 1, 100]) == 102: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [26, 18, 6, 12, 49, 7, 45, 45]) == 39
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [26, 18, 6, 12, 49, 7, 45, 45]) == 39: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 300000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 300000: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 104
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 104: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1266
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1266: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317]) == 221
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317]) == 221: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50, 40, 30, 20, 10, 5, 4, 3, 2, 1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 85
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50, 40, 30, 20, 10, 5, 4, 3, 2, 1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 85: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 531
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 531: {e}')
    
    total += 1
    try:
        result = candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75]) == 374
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75]) == 374: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 10, 1, 0, 1, 10, 100, 1000, 10000, 100000, 100000, 10000, 1000, 100, 10]) == 211
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 10, 1, 0, 1, 10, 100, 1000, 10000, 100000, 100000, 10000, 1000, 100, 10]) == 211: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1, 0, 1, 3, 6]) == 2203
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1, 0, 1, 3, 6]) == 2203: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 42
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 42: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 900]) == 225000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 900]) == 225000: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 1, 5, 2, 8, 3, 6, 4, 7, 9]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 1, 5, 2, 8, 3, 6, 4, 7, 9]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(prices = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 20737
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 20737: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 1004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 1004: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 130: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1000, 1, 500, 2, 250, 3, 125, 4, 62, 5, 31, 6, 15, 7, 7]) == 1007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1000, 1, 500, 2, 250, 3, 125, 4, 62, 5, 31, 6, 15, 7, 7]) == 1007: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 801: {e}')
    
    total += 1
    try:
        result = candidate(prices = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 72
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 72: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(prices = [26, 18, 6, 12, 49, 7, 45, 45, 100, 50, 25, 12, 6, 3, 1]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [26, 18, 6, 12, 49, 7, 45, 45, 100, 50, 25, 12, 6, 3, 1]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 180
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 180: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 6, 2, 8, 4, 10, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 6, 2, 8, 4, 10, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 1, 2, 2, 1, 3, 1, 2, 2, 1, 3, 1, 2, 2, 1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 1, 2, 2, 1, 3, 1, 2, 2, 1, 3, 1, 2, 2, 1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 58: {e}')
    
    total += 1
    try:
        result = candidate(prices = [26, 18, 6, 12, 49, 7, 45, 45, 10, 20, 30, 40, 50]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [26, 18, 6, 12, 49, 7, 45, 45, 10, 20, 30, 40, 50]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16]) == 98
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16]) == 98: {e}')
    
    total += 1
    try:
        result = candidate(prices = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 1, 2, 4, 6, 8]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 1, 2, 4, 6, 8]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 1]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 1]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(prices = [26, 18, 6, 12, 49, 7, 45, 45, 30, 20, 10, 5, 2, 1, 10, 20, 30, 40, 50, 60]) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [26, 18, 6, 12, 49, 7, 45, 45, 30, 20, 10, 5, 2, 1, 10, 20, 30, 40, 50, 60]) == 41: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 25, 5, 7, 12, 20, 3, 8, 15, 6, 2, 9, 11, 4, 14]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 25, 5, 7, 12, 20, 3, 8, 15, 6, 2, 9, 11, 4, 14]) == 20: {e}')
    
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
        result = candidate(prices = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]) == 17: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 220: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 2, 1, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 2, 1, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 1, 1, 1, 1, 1, 1]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 1, 1, 1, 1, 1, 1]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 139
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 139: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 139
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 139: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 50, 20, 10, 5, 2, 1, 2, 5, 10, 20, 50, 100]) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 50, 20, 10, 5, 2, 1, 2, 5, 10, 20, 50, 100]) == 121: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3, 1, 0, 0, 0]) == 126568
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3, 1, 0, 0, 0]) == 126568: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 32: {e}')
    
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
        result = candidate(prices = [3, 1, 2, 5, 4, 6, 3]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 1, 2, 5, 4, 6, 3]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 1, 1, 1, 1, 1]) == 1266
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 1, 1, 1, 1, 1]) == 1266: {e}')
    
    total += 1
    try:
        result = candidate(prices = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 40, 50, 40, 30, 20, 10, 20, 30, 40, 50, 40, 30, 20, 10, 20, 30, 40]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 40, 50, 40, 30, 20, 10, 20, 30, 40, 50, 40, 30, 20, 10, 20, 30, 40]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0, 0]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0, 0]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1000, 1, 100, 1, 10, 1, 1000, 1, 100, 1, 10, 1, 1000, 1, 100]) == 1003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1000, 1, 100, 1, 10, 1, 1000, 1, 100, 1, 10, 1, 1000, 1, 100]) == 1003: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 5, 2, 1, 3, 1, 2, 1]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 5, 2, 1, 3, 1, 2, 1]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 2200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 2200: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 100, 2, 200, 3, 300, 4, 400, 5, 500]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 100, 2, 200, 3, 300, 4, 400, 5, 500]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000]) == 100003
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000]) == 100003: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 5, 10, 5, 10, 5, 10, 5, 10, 5]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 5, 10, 5, 10, 5, 10, 5, 10, 5]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 200, 50, 75, 300, 100, 50, 150]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 200, 50, 75, 300, 100, 50, 150]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1]) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1]) == 18: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(prices = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 10, 20, 30, 40, 50]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 10, 20, 30, 40, 50]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85]) == 374
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85]) == 374: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]) == 23
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]) == 23: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == 74
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == 74: {e}')
    
    total += 1
    try:
        result = candidate(prices = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(prices = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(prices = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110]) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110]) == 130: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(prices = [210, 190, 171, 153, 136, 120, 105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1]) == 507
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [210, 190, 171, 153, 136, 120, 105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1]) == 507: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]) == 89
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]) == 89: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 1, 3, 6, 12, 25, 50, 100]) == 126
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 1, 3, 6, 12, 25, 50, 100]) == 126: {e}')
    
    total += 1
    try:
        result = candidate(prices = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 200, 1, 500, 10, 300, 20, 400, 3, 600]) == 111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 200, 1, 500, 10, 300, 20, 400, 3, 600]) == 111: {e}')
    
    total += 1
    try:
        result = candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(prices = [100, 50, 20, 10, 5, 1]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(prices = [100, 50, 20, 10, 5, 1]) == 120: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(prices = [1, 10, 1, 1]) == 2
    assert candidate(prices = [5, 5, 5, 5]) == 10
    assert candidate(prices = [1]) == 1
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 22
    assert candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 15
    assert candidate(prices = [3, 1, 2]) == 4
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 3
    assert candidate(prices = [1, 2, 3, 4, 5]) == 4
    assert candidate(prices = [5, 5, 5, 5, 5, 5]) == 10
    assert candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == 40
    assert candidate(prices = [10, 20, 30, 40, 50]) == 40
    assert candidate(prices = [100, 1, 100, 1, 100]) == 102
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 18
    assert candidate(prices = [5, 4, 3, 2, 1]) == 8
    assert candidate(prices = [26, 18, 6, 12, 49, 7, 45, 45]) == 39
    assert candidate(prices = [5]) == 5
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8
    assert candidate(prices = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]) == 300000
    assert candidate(prices = [100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 104
    assert candidate(prices = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1266
    assert candidate(prices = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317]) == 221
    assert candidate(prices = [50, 40, 30, 20, 10, 5, 4, 3, 2, 1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 85
    assert candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 5
    assert candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]) == 531
    assert candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75]) == 374
    assert candidate(prices = [1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000]) == 3
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0]) == 22
    assert candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 20
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 10
    assert candidate(prices = [100, 10, 1, 0, 1, 10, 100, 1000, 10000, 100000, 100000, 10000, 1000, 100, 10]) == 211
    assert candidate(prices = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 50, 25, 12, 6, 3, 1, 0, 1, 3, 6]) == 2203
    assert candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 42
    assert candidate(prices = [100000, 90000, 80000, 70000, 60000, 50000, 40000, 30000, 20000, 10000, 9000, 8000, 7000, 6000, 5000, 4000, 3000, 2000, 1000, 900]) == 225000
    assert candidate(prices = [10, 1, 5, 2, 8, 3, 6, 4, 7, 9]) == 16
    assert candidate(prices = [16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == 20737
    assert candidate(prices = [1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1]) == 1004
    assert candidate(prices = [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 6
    assert candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1]) == 14
    assert candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 130
    assert candidate(prices = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
    assert candidate(prices = [1000, 1, 500, 2, 250, 3, 125, 4, 62, 5, 31, 6, 15, 7, 7]) == 1007
    assert candidate(prices = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 801
    assert candidate(prices = [29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 72
    assert candidate(prices = [5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 14
    assert candidate(prices = [9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 20
    assert candidate(prices = [26, 18, 6, 12, 49, 7, 45, 45, 100, 50, 25, 12, 6, 3, 1]) == 45
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 180
    assert candidate(prices = [3, 6, 2, 8, 4, 10, 1]) == 6
    assert candidate(prices = [3, 1, 2, 2, 1, 3, 1, 2, 2, 1, 3, 1, 2, 2, 1]) == 6
    assert candidate(prices = [9, 7, 5, 3, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 21
    assert candidate(prices = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 58
    assert candidate(prices = [26, 18, 6, 12, 49, 7, 45, 45, 10, 20, 30, 40, 50]) == 49
    assert candidate(prices = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 10
    assert candidate(prices = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16]) == 98
    assert candidate(prices = [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 1, 2, 4, 6, 8]) == 45
    assert candidate(prices = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 41
    assert candidate(prices = [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 8
    assert candidate(prices = [1, 3, 2, 4, 3, 5, 4, 6, 5, 7, 6, 8, 7, 9, 8, 10, 9, 11, 10, 12]) == 12
    assert candidate(prices = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 1]) == 46
    assert candidate(prices = [26, 18, 6, 12, 49, 7, 45, 45, 30, 20, 10, 5, 2, 1, 10, 20, 30, 40, 50, 60]) == 41
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 16
    assert candidate(prices = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(prices = [1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000]) == 4
    assert candidate(prices = [10, 25, 5, 7, 12, 20, 3, 8, 15, 6, 2, 9, 11, 4, 14]) == 20
    assert candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 26
    assert candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 40
    assert candidate(prices = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]) == 17
    assert candidate(prices = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 40
    assert candidate(prices = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]) == 220
    assert candidate(prices = [5, 2, 1, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == 8
    assert candidate(prices = [5, 5, 5, 5, 1, 1, 1, 1, 1, 1]) == 11
    assert candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 139
    assert candidate(prices = [10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10, 20, 10]) == 40
    assert candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]) == 139
    assert candidate(prices = [100, 50, 20, 10, 5, 2, 1, 2, 5, 10, 20, 50, 100]) == 121
    assert candidate(prices = [100000, 50000, 25000, 12500, 6250, 3125, 1562, 781, 390, 195, 97, 48, 24, 12, 6, 3, 1, 0, 0, 0]) == 126568
    assert candidate(prices = [10, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]) == 13
    assert candidate(prices = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]) == 19
    assert candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 32
    assert candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1]) == 4
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 18
    assert candidate(prices = [3, 1, 2, 5, 4, 6, 3]) == 8
    assert candidate(prices = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 1, 1, 1, 1, 1]) == 1266
    assert candidate(prices = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 30
    assert candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0]) == 126
    assert candidate(prices = [10, 20, 30, 40, 50, 40, 30, 20, 10, 20, 30, 40, 50, 40, 30, 20, 10, 20, 30, 40]) == 90
    assert candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 0, 0, 0]) == 126
    assert candidate(prices = [1000, 1, 100, 1, 10, 1, 1000, 1, 100, 1, 10, 1, 1000, 1, 100]) == 1003
    assert candidate(prices = [10, 5, 2, 1, 3, 1, 2, 1]) == 13
    assert candidate(prices = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]) == 2200
    assert candidate(prices = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2]) == 4
    assert candidate(prices = [1, 100, 2, 200, 3, 300, 4, 400, 5, 500]) == 6
    assert candidate(prices = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 30
    assert candidate(prices = [100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000, 1, 100000]) == 100003
    assert candidate(prices = [10, 5, 10, 5, 10, 5, 10, 5, 10, 5]) == 25
    assert candidate(prices = [100, 200, 50, 75, 300, 100, 50, 150]) == 200
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1]) == 18
    assert candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 6
    assert candidate(prices = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == 7
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 16
    assert candidate(prices = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 1, 2, 3, 4, 5, 10, 20, 30, 40, 50]) == 9
    assert candidate(prices = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 150
    assert candidate(prices = [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85]) == 374
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8
    assert candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 3
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]) == 23
    assert candidate(prices = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210]) == 74
    assert candidate(prices = [5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1]) == 9
    assert candidate(prices = [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]) == 300
    assert candidate(prices = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]) == 10
    assert candidate(prices = [1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100, 1, 100]) == 4
    assert candidate(prices = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110]) == 130
    assert candidate(prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 22
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert candidate(prices = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10]) == 13
    assert candidate(prices = [210, 190, 171, 153, 136, 120, 105, 91, 78, 66, 55, 45, 36, 28, 21, 15, 10, 6, 3, 1]) == 507
    assert candidate(prices = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]) == 89
    assert candidate(prices = [100, 50, 25, 12, 6, 3, 1, 0, 1, 3, 6, 12, 25, 50, 100]) == 126
    assert candidate(prices = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 24
    assert candidate(prices = [100, 200, 1, 500, 10, 300, 20, 400, 3, 600]) == 111
    assert candidate(prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 15
    assert candidate(prices = [100, 50, 20, 10, 5, 1]) == 120


