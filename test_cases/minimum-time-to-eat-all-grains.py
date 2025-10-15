def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(hens = [0, 1, 2, 3],grains = [0, 1, 2, 3]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [0, 1, 2, 3],grains = [0, 1, 2, 3]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hens = [4, 6, 109, 111, 213, 215],grains = [5, 110, 214]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [4, 6, 109, 111, 213, 215],grains = [5, 110, 214]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 1, 1],grains = [1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 1, 1],grains = [1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hens = [100, 200],grains = [50, 150, 250, 350]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [100, 200],grains = [50, 150, 250, 350]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 20, 30],grains = [5, 15, 25, 35]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 20, 30],grains = [5, 15, 25, 35]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hens = [0, 1, 2, 3, 4],grains = [0, 1, 2, 3, 4]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [0, 1, 2, 3, 4],grains = [0, 1, 2, 3, 4]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 20, 30, 40, 50],grains = [5, 15, 25, 35, 45, 55]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 20, 30, 40, 50],grains = [5, 15, 25, 35, 45, 55]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 10, 100],grains = [5, 50, 500, 5000]) == 4900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 10, 100],grains = [5, 50, 500, 5000]) == 4900: {e}')
    
    total += 1
    try:
        result = candidate(hens = [0, 0, 0],grains = [1, 2, 3, 4, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [0, 0, 0],grains = [1, 2, 3, 4, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 3, 5, 7, 9],grains = [2, 4, 6, 8, 10, 12, 14, 16]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 3, 5, 7, 9],grains = [2, 4, 6, 8, 10, 12, 14, 16]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 2, 3],grains = [0, 5, 6]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 2, 3],grains = [0, 5, 6]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hens = [3, 6, 7],grains = [2, 4, 7, 9]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [3, 6, 7],grains = [2, 4, 7, 9]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 1, 1, 1],grains = [2, 3, 4, 5, 6]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 1, 1, 1],grains = [2, 3, 4, 5, 6]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1000000000],grains = [1000000000]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1000000000],grains = [1000000000]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hens = [100, 200, 300],grains = [50, 150, 250, 350, 450]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [100, 200, 300],grains = [50, 150, 250, 350, 450]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(hens = [0, 0, 0, 0],grains = [0, 0, 0, 0]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [0, 0, 0, 0],grains = [0, 0, 0, 0]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 3, 5, 7, 9],grains = [2, 4, 6, 8, 10]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 3, 5, 7, 9],grains = [2, 4, 6, 8, 10]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hens = [50, 50, 50],grains = [45, 50, 55]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [50, 50, 50],grains = [45, 50, 55]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 1, 1, 1],grains = [1, 1, 1, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 1, 1, 1],grains = [1, 1, 1, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 2, 3, 4, 5],grains = [5, 4, 3, 2, 1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 2, 3, 4, 5],grains = [5, 4, 3, 2, 1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(hens = [0, 100],grains = [50, 51, 52]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [0, 100],grains = [50, 51, 52]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 2, 3],grains = [0, 1, 2, 3, 4]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 2, 3],grains = [0, 1, 2, 3, 4]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 20, 30, 40],grains = [5, 15, 25, 35, 45, 55, 65]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 20, 30, 40],grains = [5, 15, 25, 35, 45, 55, 65]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 1, 1],grains = [1, 2, 3, 4, 5]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 1, 1],grains = [1, 2, 3, 4, 5]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 2, 3, 4, 5],grains = [10, 20, 30, 40, 50]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 2, 3, 4, 5],grains = [10, 20, 30, 40, 50]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 10, 100, 1000, 10000, 100000, 1000000],grains = [2, 9, 99, 999, 9999, 99999, 999999, 9999999]) == 8999999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 10, 100, 1000, 10000, 100000, 1000000],grains = [2, 9, 99, 999, 9999, 99999, 999999, 9999999]) == 8999999: {e}')
    
    total += 1
    try:
        result = candidate(hens = [100, 200, 300, 400, 500],grains = [50, 150, 250, 350, 450, 550, 650, 750]) == 250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [100, 200, 300, 400, 500],grains = [50, 150, 250, 350, 450, 550, 650, 750]) == 250: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 10, 20, 30, 40],grains = [0, 5, 15, 25, 35, 45, 50]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 10, 20, 30, 40],grains = [0, 5, 15, 25, 35, 45, 50]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45],grains = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45],grains = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],grains = [500000000, 750000000, 1000000000, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 1000000006, 1000000007]) == 400000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],grains = [500000000, 750000000, 1000000000, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 1000000006, 1000000007]) == 400000000: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10000, 20000, 30000, 40000, 50000],grains = [9000, 19000, 29000, 39000, 49000, 59000, 69000, 79000, 89000]) == 39000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10000, 20000, 30000, 40000, 50000],grains = [9000, 19000, 29000, 39000, 49000, 59000, 69000, 79000, 89000]) == 39000: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1000000000],grains = [0, 500000000, 1000000000, 1500000000, 2000000000]) == 3000000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1000000000],grains = [0, 500000000, 1000000000, 1500000000, 2000000000]) == 3000000000: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 2, 3, 4, 5],grains = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 2, 3, 4, 5],grains = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 14: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195]) == 95
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195]) == 95: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 10, 10, 10, 10],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 10, 10, 10, 10],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 1, 1, 1, 1],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 1, 1, 1, 1],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1000000000, 500000000, 1500000000],grains = [100000000, 50000000, 150000000, 200000000, 250000000]) == 450000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1000000000, 500000000, 1500000000],grains = [100000000, 50000000, 150000000, 200000000, 250000000]) == 450000000: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]) == 61
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]) == 61: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(hens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],grains = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],grains = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],grains = [2, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],grains = [2, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]) == 101: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 10, 100, 1000, 10000],grains = [9999, 9990, 990, 90, 9]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 10, 100, 1000, 10000],grains = [9999, 9990, 990, 90, 9]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]) == 40: {e}')
    
    total += 1
    try:
        result = candidate(hens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],grains = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950, 2050, 2150, 2250, 2350, 2450, 2550, 2650, 2750, 2850, 2950]) == 950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],grains = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950, 2050, 2150, 2250, 2350, 2450, 2550, 2650, 2750, 2850, 2950]) == 950: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 20, 30, 40, 50],grains = [15, 25, 35, 45, 55, 65, 75, 85, 95]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 20, 30, 40, 50],grains = [15, 25, 35, 45, 55, 65, 75, 85, 95]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 1980
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 1980: {e}')
    
    total += 1
    try:
        result = candidate(hens = [0, 1000000000],grains = [500000000, 1500000000, 2500000000, 3500000000]) == 2500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [0, 1000000000],grains = [500000000, 1500000000, 2500000000, 3500000000]) == 2500000000: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 20, 30, 40, 50],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 20, 30, 40, 50],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 21
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 21: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500],grains = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]) == 4500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500],grains = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]) == 4500: {e}')
    
    total += 1
    try:
        result = candidate(hens = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],grains = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],grains = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [0, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [0, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1000000000, 500000000, 250000000],grains = [1000000000, 750000000, 500000000, 250000000, 0]) == 250000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1000000000, 500000000, 250000000],grains = [1000000000, 750000000, 500000000, 250000000, 0]) == 250000000: {e}')
    
    total += 1
    try:
        result = candidate(hens = [100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900],grains = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950, 2050, 2150, 2250, 2350, 2450, 2550, 2650, 2750, 2850, 2950]) == 1050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900],grains = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950, 2050, 2150, 2250, 2350, 2450, 2550, 2650, 2750, 2850, 2950]) == 1050: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 20, 30, 40, 50],grains = [5, 15, 25, 35, 45, 55, 65]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 20, 30, 40, 50],grains = [5, 15, 25, 35, 45, 55, 65]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hens = [100, 200, 300, 400, 500],grains = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [100, 200, 300, 400, 500],grains = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(hens = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],grains = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],grains = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 1, 1, 1, 1],grains = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 1, 1, 1, 1],grains = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 99: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295, 305]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295, 305]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(hens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],grains = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],grains = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 5, 10, 15, 20],grains = [2, 3, 6, 9, 11, 14, 17, 19, 22, 25]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 5, 10, 15, 20],grains = [2, 3, 6, 9, 11, 14, 17, 19, 22, 25]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hens = [500, 1000, 1500, 2000, 2500, 3000],grains = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [500, 1000, 1500, 2000, 2500, 3000],grains = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77],grains = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77],grains = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(hens = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],grains = [100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2300, 2500, 2700, 2900, 3100, 3300, 3500, 3700, 3900, 4100, 4300, 4500, 4700, 4900, 5100, 5300, 5500]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],grains = [100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2300, 2500, 2700, 2900, 3100, 3300, 3500, 3700, 3900, 4100, 4300, 4500, 4700, 4900, 5100, 5300, 5500]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 20, 30, 40, 50],grains = [9, 19, 29, 39, 49, 59, 69, 79]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 20, 30, 40, 50],grains = [9, 19, 29, 39, 49, 59, 69, 79]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(hens = [50, 150, 250, 350, 450],grains = [1, 99, 101, 199, 201, 299, 301, 399, 401, 499, 501, 599, 601]) == 151
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [50, 150, 250, 350, 450],grains = [1, 99, 101, 199, 201, 299, 301, 399, 401, 499, 501, 599, 601]) == 151: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 20, 30, 40, 50],grains = [5, 15, 25, 35, 45, 55, 65, 75]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 20, 30, 40, 50],grains = [5, 15, 25, 35, 45, 55, 65, 75]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 20, 30, 40, 50],grains = [5, 15, 25, 35, 45, 55]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 20, 30, 40, 50],grains = [5, 15, 25, 35, 45, 55]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]) == 380
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]) == 380: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 100, 200, 300, 400, 500],grains = [2, 50, 150, 250, 350, 450, 550, 650]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 100, 200, 300, 400, 500],grains = [2, 50, 150, 250, 350, 450, 550, 650]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(hens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],grains = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],grains = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(hens = [5, 25, 45, 65, 85],grains = [10, 30, 50, 70, 90, 100]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [5, 25, 45, 65, 85],grains = [10, 30, 50, 70, 90, 100]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],grains = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],grains = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],grains = [2, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96, 101, 106, 111]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],grains = [2, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96, 101, 106, 111]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(hens = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],grains = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975, 1025]) == 125
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],grains = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975, 1025]) == 125: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 3, 5, 7, 9],grains = [0, 2, 4, 6, 8, 10, 12]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 3, 5, 7, 9],grains = [0, 2, 4, 6, 8, 10, 12]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(hens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],grains = [90, 190, 290, 390, 490, 590, 690, 790, 890, 990, 1090, 1190, 1290, 1390]) == 390
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],grains = [90, 190, 290, 390, 490, 590, 690, 790, 890, 990, 1090, 1190, 1290, 1390]) == 390: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(hens = [50, 100, 150, 200],grains = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575]) == 375
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [50, 100, 150, 200],grains = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575]) == 375: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1000, 2000, 3000, 4000],grains = [500, 1500, 2500, 3500, 4500, 5500, 6500, 7500]) == 3500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1000, 2000, 3000, 4000],grains = [500, 1500, 2500, 3500, 4500, 5500, 6500, 7500]) == 3500: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1000, 2000, 3000, 4000, 5000],grains = [500, 1500, 2500, 3500, 4500, 5500, 6500]) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1000, 2000, 3000, 4000, 5000],grains = [500, 1500, 2500, 3500, 4500, 5500, 6500]) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],grains = [999, 1999, 2999, 3999, 4999, 5999, 6999, 7999, 8999, 9999, 10001, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000]) == 9000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],grains = [999, 1999, 2999, 3999, 4999, 5999, 6999, 7999, 8999, 9999, 10001, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000]) == 9000: {e}')
    
    total += 1
    try:
        result = candidate(hens = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 10, 100, 1000, 10000, 100000],grains = [0, 5, 50, 500, 5000, 50000, 500000, 1000000]) == 900000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 10, 100, 1000, 10000, 100000],grains = [0, 5, 50, 500, 5000, 50000, 500000, 1000000]) == 900000: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 20, 30, 40, 50],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 20, 30, 40, 50],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 20, 30, 40, 50, 60, 70],grains = [5, 15, 25, 35, 45, 55, 65, 75]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 20, 30, 40, 50, 60, 70],grains = [5, 15, 25, 35, 45, 55, 65, 75]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(hens = [0, 1000000000],grains = [500000000, 1500000000]) == 500000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [0, 1000000000],grains = [500000000, 1500000000]) == 500000000: {e}')
    
    total += 1
    try:
        result = candidate(hens = [500, 1000, 1500, 2000, 2500],grains = [400, 600, 800, 1200, 1400, 1600, 1800, 2100, 2400, 2600]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [500, 1000, 1500, 2000, 2500],grains = [400, 600, 800, 1200, 1400, 1600, 1800, 2100, 2400, 2600]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(hens = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],grains = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],grains = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 5, 10, 15, 20],grains = [3, 6, 9, 12, 14, 18, 22, 25]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 5, 10, 15, 20],grains = [3, 6, 9, 12, 14, 18, 22, 25]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1000, 2000, 3000, 4000, 5000],grains = [900, 1900, 2900, 3900, 4900, 5900]) == 1100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1000, 2000, 3000, 4000, 5000],grains = [900, 1900, 2900, 3900, 4900, 5900]) == 1100: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295]) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295]) == 145: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(hens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],grains = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450]) == 450
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],grains = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450]) == 450: {e}')
    
    total += 1
    try:
        result = candidate(hens = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(hens = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],grains = [1, 3, 5, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39, 41, 43, 47, 49, 51, 53, 57, 59, 61, 63, 67, 69, 71, 73, 77, 79, 81, 83, 87, 89, 91, 93, 97, 99]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],grains = [1, 3, 5, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39, 41, 43, 47, 49, 51, 53, 57, 59, 61, 63, 67, 69, 71, 73, 77, 79, 81, 83, 87, 89, 91, 93, 97, 99]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125]) == 25: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(hens = [0, 1, 2, 3],grains = [0, 1, 2, 3]) == 0
    assert candidate(hens = [4, 6, 109, 111, 213, 215],grains = [5, 110, 214]) == 1
    assert candidate(hens = [1, 1, 1],grains = [1, 1, 1, 1]) == 0
    assert candidate(hens = [100, 200],grains = [50, 150, 250, 350]) == 150
    assert candidate(hens = [10, 20, 30],grains = [5, 15, 25, 35]) == 15
    assert candidate(hens = [0, 1, 2, 3, 4],grains = [0, 1, 2, 3, 4]) == 0
    assert candidate(hens = [10, 20, 30, 40, 50],grains = [5, 15, 25, 35, 45, 55]) == 15
    assert candidate(hens = [1, 10, 100],grains = [5, 50, 500, 5000]) == 4900
    assert candidate(hens = [0, 0, 0],grains = [1, 2, 3, 4, 5]) == 5
    assert candidate(hens = [1, 3, 5, 7, 9],grains = [2, 4, 6, 8, 10, 12, 14, 16]) == 7
    assert candidate(hens = [1, 2, 3],grains = [0, 5, 6]) == 3
    assert candidate(hens = [3, 6, 7],grains = [2, 4, 7, 9]) == 2
    assert candidate(hens = [1, 1, 1, 1],grains = [2, 3, 4, 5, 6]) == 5
    assert candidate(hens = [1000000000],grains = [1000000000]) == 0
    assert candidate(hens = [100, 200, 300],grains = [50, 150, 250, 350, 450]) == 150
    assert candidate(hens = [0, 0, 0, 0],grains = [0, 0, 0, 0]) == 0
    assert candidate(hens = [1, 3, 5, 7, 9],grains = [2, 4, 6, 8, 10]) == 1
    assert candidate(hens = [50, 50, 50],grains = [45, 50, 55]) == 5
    assert candidate(hens = [1, 1, 1, 1],grains = [1, 1, 1, 1]) == 0
    assert candidate(hens = [1, 2, 3, 4, 5],grains = [5, 4, 3, 2, 1]) == 0
    assert candidate(hens = [0, 100],grains = [50, 51, 52]) == 50
    assert candidate(hens = [1, 2, 3],grains = [0, 1, 2, 3, 4]) == 1
    assert candidate(hens = [10, 20, 30, 40],grains = [5, 15, 25, 35, 45, 55, 65]) == 25
    assert candidate(hens = [1, 1, 1],grains = [1, 2, 3, 4, 5]) == 4
    assert candidate(hens = [1, 2, 3, 4, 5],grains = [10, 20, 30, 40, 50]) == 45
    assert candidate(hens = [1, 10, 100, 1000, 10000, 100000, 1000000],grains = [2, 9, 99, 999, 9999, 99999, 999999, 9999999]) == 8999999
    assert candidate(hens = [100, 200, 300, 400, 500],grains = [50, 150, 250, 350, 450, 550, 650, 750]) == 250
    assert candidate(hens = [1, 10, 20, 30, 40],grains = [0, 5, 15, 25, 35, 45, 50]) == 10
    assert candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 20
    assert candidate(hens = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45],grains = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 4
    assert candidate(hens = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],grains = [500000000, 750000000, 1000000000, 1000000001, 1000000002, 1000000003, 1000000004, 1000000005, 1000000006, 1000000007]) == 400000000
    assert candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 10
    assert candidate(hens = [10000, 20000, 30000, 40000, 50000],grains = [9000, 19000, 29000, 39000, 49000, 59000, 69000, 79000, 89000]) == 39000
    assert candidate(hens = [1000000000],grains = [0, 500000000, 1000000000, 1500000000, 2000000000]) == 3000000000
    assert candidate(hens = [1, 2, 3, 4, 5],grains = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 14
    assert candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195]) == 95
    assert candidate(hens = [10, 10, 10, 10, 10],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(hens = [1, 1, 1, 1, 1],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert candidate(hens = [1000000000, 500000000, 1500000000],grains = [100000000, 50000000, 150000000, 200000000, 250000000]) == 450000000
    assert candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]) == 61
    assert candidate(hens = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 9
    assert candidate(hens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],grains = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 19
    assert candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1
    assert candidate(hens = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],grains = [2, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]) == 101
    assert candidate(hens = [1, 10, 100, 1000, 10000],grains = [9999, 9990, 990, 90, 9]) == 10
    assert candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140]) == 40
    assert candidate(hens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],grains = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950, 2050, 2150, 2250, 2350, 2450, 2550, 2650, 2750, 2850, 2950]) == 950
    assert candidate(hens = [10, 20, 30, 40, 50],grains = [15, 25, 35, 45, 55, 65, 75, 85, 95]) == 45
    assert candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 140
    assert candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 90
    assert candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]) == 1980
    assert candidate(hens = [0, 1000000000],grains = [500000000, 1500000000, 2500000000, 3500000000]) == 2500000000
    assert candidate(hens = [10, 20, 30, 40, 50],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 45
    assert candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 3
    assert candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 21
    assert candidate(hens = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500],grains = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]) == 4500
    assert candidate(hens = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105],grains = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]) == 5
    assert candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]) == 11
    assert candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [0, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]) == 19
    assert candidate(hens = [1000000000, 500000000, 250000000],grains = [1000000000, 750000000, 500000000, 250000000, 0]) == 250000000
    assert candidate(hens = [100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900],grains = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450, 1550, 1650, 1750, 1850, 1950, 2050, 2150, 2250, 2350, 2450, 2550, 2650, 2750, 2850, 2950]) == 1050
    assert candidate(hens = [10, 20, 30, 40, 50],grains = [5, 15, 25, 35, 45, 55, 65]) == 15
    assert candidate(hens = [100, 200, 300, 400, 500],grains = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050]) == 550
    assert candidate(hens = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],grains = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975]) == 75
    assert candidate(hens = [1, 1, 1, 1, 1],grains = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 99
    assert candidate(hens = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295, 305]) == 105
    assert candidate(hens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],grains = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]) == 9
    assert candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]) == 29
    assert candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]) == 15
    assert candidate(hens = [1, 5, 10, 15, 20],grains = [2, 3, 6, 9, 11, 14, 17, 19, 22, 25]) == 5
    assert candidate(hens = [500, 1000, 1500, 2000, 2500, 3000],grains = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500]) == 500
    assert candidate(hens = [1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77],grains = [2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54, 58, 62, 66, 70, 74, 78, 82]) == 5
    assert candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]) == 19
    assert candidate(hens = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],grains = [100, 300, 500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2300, 2500, 2700, 2900, 3100, 3300, 3500, 3700, 3900, 4100, 4300, 4500, 4700, 4900, 5100, 5300, 5500]) == 600
    assert candidate(hens = [10, 20, 30, 40, 50],grains = [9, 19, 29, 39, 49, 59, 69, 79]) == 29
    assert candidate(hens = [50, 150, 250, 350, 450],grains = [1, 99, 101, 199, 201, 299, 301, 399, 401, 499, 501, 599, 601]) == 151
    assert candidate(hens = [10, 20, 30, 40, 50],grains = [5, 15, 25, 35, 45, 55, 65, 75]) == 25
    assert candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115]) == 15
    assert candidate(hens = [10, 20, 30, 40, 50],grains = [5, 15, 25, 35, 45, 55]) == 15
    assert candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],grains = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400]) == 380
    assert candidate(hens = [1, 100, 200, 300, 400, 500],grains = [2, 50, 150, 250, 350, 450, 550, 650]) == 150
    assert candidate(hens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],grains = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050]) == 150
    assert candidate(hens = [5, 25, 45, 65, 85],grains = [10, 30, 50, 70, 90, 100]) == 15
    assert candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 1
    assert candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],grains = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 3
    assert candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145]) == 45
    assert candidate(hens = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],grains = [2, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96, 101, 106, 111]) == 11
    assert candidate(hens = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],grains = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975, 1025]) == 125
    assert candidate(hens = [1, 3, 5, 7, 9],grains = [0, 2, 4, 6, 8, 10, 12]) == 3
    assert candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]) == 9
    assert candidate(hens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],grains = [90, 190, 290, 390, 490, 590, 690, 790, 890, 990, 1090, 1190, 1290, 1390]) == 390
    assert candidate(hens = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],grains = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == 1
    assert candidate(hens = [50, 100, 150, 200],grains = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575]) == 375
    assert candidate(hens = [1000, 2000, 3000, 4000],grains = [500, 1500, 2500, 3500, 4500, 5500, 6500, 7500]) == 3500
    assert candidate(hens = [1000, 2000, 3000, 4000, 5000],grains = [500, 1500, 2500, 3500, 4500, 5500, 6500]) == 1500
    assert candidate(hens = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],grains = [999, 1999, 2999, 3999, 4999, 5999, 6999, 7999, 8999, 9999, 10001, 11000, 12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000]) == 9000
    assert candidate(hens = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 4
    assert candidate(hens = [1, 10, 100, 1000, 10000, 100000],grains = [0, 5, 50, 500, 5000, 50000, 500000, 1000000]) == 900000
    assert candidate(hens = [10, 20, 30, 40, 50],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 45
    assert candidate(hens = [10, 20, 30, 40, 50, 60, 70],grains = [5, 15, 25, 35, 45, 55, 65, 75]) == 15
    assert candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195]) == 45
    assert candidate(hens = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 19
    assert candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 90
    assert candidate(hens = [0, 1000000000],grains = [500000000, 1500000000]) == 500000000
    assert candidate(hens = [500, 1000, 1500, 2000, 2500],grains = [400, 600, 800, 1200, 1400, 1600, 1800, 2100, 2400, 2600]) == 500
    assert candidate(hens = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71],grains = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]) == 29
    assert candidate(hens = [1, 5, 10, 15, 20],grains = [3, 6, 9, 12, 14, 18, 22, 25]) == 5
    assert candidate(hens = [1000, 2000, 3000, 4000, 5000],grains = [900, 1900, 2900, 3900, 4900, 5900]) == 1100
    assert candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 10
    assert candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295]) == 145
    assert candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]) == 49
    assert candidate(hens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],grains = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 10
    assert candidate(hens = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],grains = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950, 1050, 1150, 1250, 1350, 1450]) == 450
    assert candidate(hens = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195]) == 105
    assert candidate(hens = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],grains = [1, 3, 5, 7, 9, 11, 13, 17, 19, 21, 23, 27, 29, 31, 33, 37, 39, 41, 43, 47, 49, 51, 53, 57, 59, 61, 63, 67, 69, 71, 73, 77, 79, 81, 83, 87, 89, 91, 93, 97, 99]) == 12
    assert candidate(hens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],grains = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125]) == 25


