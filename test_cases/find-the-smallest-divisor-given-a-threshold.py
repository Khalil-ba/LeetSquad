def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],threshold = 15) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],threshold = 15) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [44, 22, 33, 11, 1],threshold = 5) == 44
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [44, 22, 33, 11, 1],threshold = 5) == 44: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],threshold = 5) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],threshold = 5) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],threshold = 100) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],threshold = 100) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 999999, 999999],threshold = 2999997) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 999999, 999999],threshold = 2999997) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1],threshold = 1) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1],threshold = 1) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 5, 9],threshold = 6) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 5, 9],threshold = 6) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000],threshold = 1000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000],threshold = 1000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 234567, 345678, 456789, 567890, 678901, 789012, 890123, 901234, 1012345],threshold = 2500000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 234567, 345678, 456789, 567890, 678901, 789012, 890123, 901234, 1012345],threshold = 2500000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],threshold = 30) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],threshold = 30) == 30: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15],threshold = 50) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15],threshold = 50) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],threshold = 20) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],threshold = 20) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, 500000, 500000, 500000, 500000],threshold = 1000000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, 500000, 500000, 500000, 500000],threshold = 1000000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],threshold = 1000) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],threshold = 1000) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],threshold = 18) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],threshold = 18) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000],threshold = 1000000) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000],threshold = 1000000) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],threshold = 100) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],threshold = 100) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000],threshold = 5000000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000],threshold = 5000000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000],threshold = 500000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000],threshold = 500000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],threshold = 1000000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],threshold = 1000000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],threshold = 100) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],threshold = 100) == 58: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],threshold = 20) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],threshold = 20) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 400, 300, 200, 100],threshold = 50) == 32
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 400, 300, 200, 100],threshold = 50) == 32: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],threshold = 50) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],threshold = 50) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],threshold = 10000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],threshold = 10000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654, 876543, 765432, 654321, 543210, 432109, 321098, 210987, 109876],threshold = 4000000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654, 876543, 765432, 654321, 543210, 432109, 321098, 210987, 109876],threshold = 4000000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000],threshold = 55000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000],threshold = 55000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],threshold = 50) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],threshold = 50) == 25: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999],threshold = 9999990) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999],threshold = 9999990) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250],threshold = 1000000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250],threshold = 1000000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],threshold = 30) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],threshold = 30) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [800, 800, 800, 800, 800, 800, 800, 800, 800, 800],threshold = 10) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [800, 800, 800, 800, 800, 800, 800, 800, 800, 800],threshold = 10) == 800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654, 321456, 789012, 456789, 234567],threshold = 2000000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654, 321456, 789012, 456789, 234567],threshold = 2000000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],threshold = 50) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],threshold = 50) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100000, 200000, 300000, 400000, 500000],threshold = 200000) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100000, 200000, 300000, 400000, 500000],threshold = 200000) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],threshold = 100) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],threshold = 100) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],threshold = 30) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],threshold = 30) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],threshold = 10) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],threshold = 10) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],threshold = 50) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],threshold = 50) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 654321, 111111, 222222, 333333, 444444, 555555, 666666, 777777, 888888],threshold = 1000000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 654321, 111111, 222222, 333333, 444444, 555555, 666666, 777777, 888888],threshold = 1000000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 654321, 111111, 222222, 333333, 444444, 555555],threshold = 1000000) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 654321, 111111, 222222, 333333, 444444, 555555],threshold = 1000000) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],threshold = 300) == 41
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],threshold = 300) == 41: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000],threshold = 1000000) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000],threshold = 1000000) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [888888, 888887, 888886, 888885, 888884, 888883, 888882, 888881, 888880, 888879],threshold = 8888800) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [888888, 888887, 888886, 888885, 888884, 888883, 888882, 888881, 888880, 888879],threshold = 8888800) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000],threshold = 20) == 834
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000],threshold = 20) == 834: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, 999997],threshold = 3999990) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, 999997],threshold = 3999990) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],threshold = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],threshold = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],threshold = 50000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],threshold = 50000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],threshold = 20) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],threshold = 20) == 5: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],threshold = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],threshold = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],threshold = 50) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],threshold = 50) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 789012, 345678, 901234, 567890],threshold = 2000000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 789012, 345678, 901234, 567890],threshold = 2000000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, 1000000, 1500000, 2000000, 2500000],threshold = 5000000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, 1000000, 1500000, 2000000, 2500000],threshold = 5000000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 234567, 345678, 456789, 567890],threshold = 500000) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 234567, 345678, 456789, 567890],threshold = 500000) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],threshold = 25) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],threshold = 25) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],threshold = 25) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],threshold = 25) == 100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, 400000, 300000, 200000, 100000],threshold = 1000000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, 400000, 300000, 200000, 100000],threshold = 1000000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],threshold = 10000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],threshold = 10000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],threshold = 75) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],threshold = 75) == 16: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 999998, 999997, 999996],threshold = 5000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 999998, 999997, 999996],threshold = 5000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],threshold = 10000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],threshold = 10000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],threshold = 210101) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],threshold = 210101) == 6: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],threshold = 111111) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],threshold = 111111) == 11: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],threshold = 25) == 267
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],threshold = 25) == 267: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],threshold = 18) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],threshold = 18) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],threshold = 75) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],threshold = 75) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [123456, 234567, 345678, 456789, 567890],threshold = 1500000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [123456, 234567, 345678, 456789, 567890],threshold = 1500000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [987654, 987654, 987654, 987654, 987654, 987654, 987654, 987654, 987654, 987654],threshold = 5000000) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [987654, 987654, 987654, 987654, 987654, 987654, 987654, 987654, 987654, 987654],threshold = 5000000) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],threshold = 1111111) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],threshold = 1111111) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 999999, 888888, 777777, 666666],threshold = 5000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 999999, 888888, 777777, 666666],threshold = 5000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],threshold = 100) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],threshold = 100) == 3: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625],threshold = 2000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625],threshold = 2000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61, 30, 15, 7, 3, 1],threshold = 20) == 1000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61, 30, 15, 7, 3, 1],threshold = 20) == 1000000: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],threshold = 50) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],threshold = 50) == 120: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],threshold = 2101011) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],threshold = 2101011) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000],threshold = 5000000) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000],threshold = 5000000) == 1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],threshold = 12) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],threshold = 12) == 8: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999],threshold = 1000) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999],threshold = 1000) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],threshold = 1000) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],threshold = 1000) == 22: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000, 499999, 499998, 499997, 499996],threshold = 2499980) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000, 499999, 499998, 499997, 499996],threshold = 2499980) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],threshold = 20) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],threshold = 20) == 10: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [10, 20, 30, 40, 50],threshold = 15) == 10
    assert candidate(nums = [44, 22, 33, 11, 1],threshold = 5) == 44
    assert candidate(nums = [1, 1, 1, 1, 1],threshold = 5) == 1
    assert candidate(nums = [10, 20, 30, 40, 50],threshold = 100) == 2
    assert candidate(nums = [999999, 999999, 999999],threshold = 2999997) == 1
    assert candidate(nums = [1, 1, 1, 1, 1],threshold = 1) == 2
    assert candidate(nums = [1, 2, 5, 9],threshold = 6) == 5
    assert candidate(nums = [1000000],threshold = 1000000) == 1
    assert candidate(nums = [123456, 234567, 345678, 456789, 567890, 678901, 789012, 890123, 901234, 1012345],threshold = 2500000) == 3
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],threshold = 30) == 30
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15],threshold = 50) == 7
    assert candidate(nums = [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7],threshold = 20) == 7
    assert candidate(nums = [500000, 500000, 500000, 500000, 500000],threshold = 1000000) == 3
    assert candidate(nums = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000],threshold = 1000) == 17
    assert candidate(nums = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9],threshold = 18) == 9
    assert candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000],threshold = 1000000) == 6
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],threshold = 100) == 4
    assert candidate(nums = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000],threshold = 5000000) == 2
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000],threshold = 500000) == 10
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288],threshold = 1000000) == 2
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],threshold = 100) == 58
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],threshold = 20) == 3
    assert candidate(nums = [500, 400, 300, 200, 100],threshold = 50) == 32
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],threshold = 50) == 9
    assert candidate(nums = [1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000],threshold = 10000000) == 1
    assert candidate(nums = [987654, 876543, 765432, 654321, 543210, 432109, 321098, 210987, 109876],threshold = 4000000) == 2
    assert candidate(nums = [1000000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000, 8000000, 9000000, 10000000],threshold = 55000000) == 1
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],threshold = 50) == 25
    assert candidate(nums = [999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999, 999999],threshold = 9999990) == 1
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250],threshold = 1000000) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],threshold = 30) == 2
    assert candidate(nums = [800, 800, 800, 800, 800, 800, 800, 800, 800, 800],threshold = 10) == 800
    assert candidate(nums = [987654, 321456, 789012, 456789, 234567],threshold = 2000000) == 2
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],threshold = 50) == 16
    assert candidate(nums = [100000, 200000, 300000, 400000, 500000],threshold = 200000) == 8
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],threshold = 100) == 24
    assert candidate(nums = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],threshold = 30) == 5
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],threshold = 10) == 6
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],threshold = 50) == 2
    assert candidate(nums = [123456, 654321, 111111, 222222, 333333, 444444, 555555, 666666, 777777, 888888],threshold = 1000000) == 5
    assert candidate(nums = [123456, 654321, 111111, 222222, 333333, 444444, 555555],threshold = 1000000) == 3
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],threshold = 300) == 41
    assert candidate(nums = [500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000],threshold = 1000000) == 5
    assert candidate(nums = [888888, 888887, 888886, 888885, 888884, 888883, 888882, 888881, 888880, 888879],threshold = 8888800) == 2
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000],threshold = 20) == 834
    assert candidate(nums = [1000000, 999999, 999998, 999997],threshold = 3999990) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],threshold = 20) == 20
    assert candidate(nums = [10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000],threshold = 50000) == 2
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],threshold = 20) == 5
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],threshold = 10) == 10
    assert candidate(nums = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],threshold = 50) == 1200
    assert candidate(nums = [123456, 789012, 345678, 901234, 567890],threshold = 2000000) == 2
    assert candidate(nums = [500000, 1000000, 1500000, 2000000, 2500000],threshold = 5000000) == 2
    assert candidate(nums = [123456, 234567, 345678, 456789, 567890],threshold = 500000) == 4
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],threshold = 25) == 3
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],threshold = 25) == 100
    assert candidate(nums = [500000, 400000, 300000, 200000, 100000],threshold = 1000000) == 2
    assert candidate(nums = [1000000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],threshold = 10000000) == 1
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],threshold = 75) == 16
    assert candidate(nums = [1000000, 999999, 999998, 999997, 999996],threshold = 5000000) == 1
    assert candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500],threshold = 10000) == 1
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],threshold = 210101) == 6
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],threshold = 111111) == 11
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],threshold = 25) == 267
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],threshold = 18) == 4
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],threshold = 75) == 18
    assert candidate(nums = [123456, 234567, 345678, 456789, 567890],threshold = 1500000) == 2
    assert candidate(nums = [987654, 987654, 987654, 987654, 987654, 987654, 987654, 987654, 987654, 987654],threshold = 5000000) == 2
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],threshold = 1111111) == 1
    assert candidate(nums = [1000000, 999999, 888888, 777777, 666666],threshold = 5000000) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],threshold = 100) == 3
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625],threshold = 2000000) == 1
    assert candidate(nums = [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61, 30, 15, 7, 3, 1],threshold = 20) == 1000000
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],threshold = 50) == 120
    assert candidate(nums = [1, 10, 100, 1000, 10000, 100000, 1000000],threshold = 2101011) == 1
    assert candidate(nums = [500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000, 500000],threshold = 5000000) == 1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],threshold = 12) == 8
    assert candidate(nums = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999],threshold = 1000) == 10
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],threshold = 1000) == 22
    assert candidate(nums = [500000, 499999, 499998, 499997, 499996],threshold = 2499980) == 2
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],threshold = 20) == 10


