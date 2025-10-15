def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [500, 500, 500, 500],k = 1000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 500, 500, 500],k = 1000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35],k = 50) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35],k = 50) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 8) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 8) == 7: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996],k = 1995) == 1994
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996],k = 1995) == 1994: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45],k = 50) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45],k = 50) == 40: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5],k = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5],k = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996],k = 2000) == 1997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996],k = 2000) == 1997: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1],k = 2) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1],k = 2) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995],k = 1995) == 1994
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995],k = 1995) == 1994: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],k = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],k = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30],k = 15) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30],k = 15) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400],k = 1000) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400],k = 1000) == 700: {e}')
    
    total += 1
    try:
        result = candidate(nums = [34, 23, 1, 24, 75, 33, 54, 8],k = 60) == 58
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [34, 23, 1, 24, 75, 33, 54, 8],k = 60) == 58: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1],k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1],k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],k = 1000) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],k = 1000) == 900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 150) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 150) == 140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],k = 850) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],k = 850) == 800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999],k = 1998) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999],k = 1998) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 400, 300, 200, 100],k = 800) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 400, 300, 200, 100],k = 800) == 700: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 18) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 18) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 180) == 170
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 180) == 170: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81],k = 190) == 189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81],k = 190) == 189: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 5) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 5) == 4: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 50) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 50) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],k = 1990) == 1989
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],k = 1990) == 1989: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 30) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 30) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 1023) == 768
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 1023) == 768: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 6, 7, 9, 11, 13, 14, 18, 21],k = 30) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 6, 7, 9, 11, 13, 14, 18, 21],k = 30) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 400, 300, 200, 100, 50, 25, 10, 5, 1],k = 600) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 400, 300, 200, 100, 50, 25, 10, 5, 1],k = 600) == 550: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],k = 230) == 220
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],k = 230) == 220: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1800) == 1700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1800) == 1700: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 20) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 20) == 19: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 400, 300, 200, 100, 50, 25, 10, 5, 1],k = 1000) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 400, 300, 200, 100, 50, 25, 10, 5, 1],k = 1000) == 900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 250) == 240
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 250) == 240: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],k = 1000) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],k = 1000) == 900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [80, 70, 60, 50, 40, 30, 20, 10],k = 140) == 130
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [80, 70, 60, 50, 40, 30, 20, 10],k = 140) == 130: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 50, 25, 12, 6, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 200) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 50, 25, 12, 6, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 200) == 150: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],k = 2000) == 1999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],k = 2000) == 1999: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1500) == 1400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1500) == 1400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],k = 1999) == 1997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],k = 1999) == 1997: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1900) == 1800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1900) == 1800: {e}')
    
    total += 1
    try:
        result = candidate(nums = [800, 700, 600, 500, 400, 300, 200, 100],k = 1200) == 1100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [800, 700, 600, 500, 400, 300, 200, 100],k = 1200) == 1100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 9: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1999) == 1900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1999) == 1900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900],k = 1500) == 1400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900],k = 1500) == 1400: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 200) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 200) == 190: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81],k = 190) == 189
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81],k = 190) == 189: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 1, 998, 2, 997, 3, 996, 4],k = 2000) == 1997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 1, 998, 2, 997, 3, 996, 4],k = 2000) == 1997: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 19) == 18
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 19) == 18: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 11) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 11) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 11) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 11) == 10: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],k = 1800) == 1700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],k = 1800) == 1700: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 999, 2, 998, 3, 997, 4, 996, 5, 995],k = 2000) == 1997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 999, 2, 998, 3, 997, 4, 996, 5, 995],k = 2000) == 1997: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 25) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 25) == 24: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 499, 498, 497, 496, 495, 494, 493, 492, 491, 490, 489, 488, 487, 486, 485, 484, 483, 482, 481, 480, 479, 478, 477, 476, 475, 474, 473, 472, 471, 470, 469, 468, 467, 466, 465, 464, 463, 462, 461, 460, 459, 458, 457, 456, 455, 454, 453, 452, 451, 450],k = 999) == 998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 499, 498, 497, 496, 495, 494, 493, 492, 491, 490, 489, 488, 487, 486, 485, 484, 483, 482, 481, 480, 479, 478, 477, 476, 475, 474, 473, 472, 471, 470, 469, 468, 467, 466, 465, 464, 463, 462, 461, 460, 459, 458, 457, 456, 455, 454, 453, 452, 451, 450],k = 999) == 998: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 50) == 48
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 50) == 48: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 40) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 40) == 38: {e}')
    
    total += 1
    try:
        result = candidate(nums = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],k = 210) == 209
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],k = 210) == 209: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 50) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 50) == 49: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 150) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 150) == 140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 150) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 150) == 145: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 150) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 150) == 140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980],k = 1999) == 1997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980],k = 1999) == 1997: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 300) == 290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 300) == 290: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 14
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 14: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 70) == 65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 70) == 65: {e}')
    
    total += 1
    try:
        result = candidate(nums = [800, 700, 600, 500, 400, 300, 200, 100, 50, 10],k = 1200) == 1100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [800, 700, 600, 500, 400, 300, 200, 100, 50, 10],k = 1200) == 1100: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],k = 1998) == 1997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],k = 1998) == 1997: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 100) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 100) == 99: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 999, 2, 998, 3, 997, 4, 996, 5, 995],k = 1998) == 1997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 999, 2, 998, 3, 997, 4, 996, 5, 995],k = 1998) == 1997: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 499, 498, 497, 496, 495],k = 1000) == 999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 499, 498, 497, 496, 495],k = 1000) == 999: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31],k = 100) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31],k = 100) == 99: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 30) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 30) == 29: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1500) == 1250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1500) == 1250: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],k = 1985) == 1984
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],k = 1985) == 1984: {e}')
    
    total += 1
    try:
        result = candidate(nums = [990, 890, 790, 690, 590, 490, 390, 290, 190, 90, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1900) == 1880
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [990, 890, 790, 690, 590, 490, 390, 290, 190, 90, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1900) == 1880: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 150) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 150) == 140: {e}')
    
    total += 1
    try:
        result = candidate(nums = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5],k = 2000) == 1997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5],k = 2000) == 1997: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500],k = 1000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500],k = 1000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 39) == 38
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 39) == 38: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 18) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 18) == 17: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],k = 1700) == 1600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],k = 1700) == 1600: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 40, 30, 20, 10],k = 70) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 40, 30, 20, 10],k = 70) == 60: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 200) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 200) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1999) == 1900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1999) == 1900: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 300) == 290
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 300) == 290: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 2: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 101) == 99
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 101) == 99: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 50) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 50) == 49: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900],k = 1800) == 1700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900],k = 1800) == 1700: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 20) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 20) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1600) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1600) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500, 500, 500, 500, 500],k = 1000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500, 500, 500, 500, 500],k = 1000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550],k = 1000) == 950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550],k = 1000) == 950: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [500, 500, 500, 500],k = 1000) == -1
    assert candidate(nums = [5, 15, 25, 35],k = 50) == 40
    assert candidate(nums = [1, 2, 3, 4, 5],k = 8) == 7
    assert candidate(nums = [999, 998, 997, 996],k = 1995) == 1994
    assert candidate(nums = [5, 15, 25, 35, 45],k = 50) == 40
    assert candidate(nums = [5, 5, 5, 5],k = 10) == -1
    assert candidate(nums = [999, 998, 997, 996],k = 2000) == 1997
    assert candidate(nums = [1],k = 2) == -1
    assert candidate(nums = [999, 998, 997, 996, 995],k = 1995) == 1994
    assert candidate(nums = [1, 2, 3, 4, 5],k = 10) == 9
    assert candidate(nums = [10, 20, 30],k = 15) == -1
    assert candidate(nums = [100, 200, 300, 400],k = 1000) == 700
    assert candidate(nums = [34, 23, 1, 24, 75, 33, 54, 8],k = 60) == 58
    assert candidate(nums = [1, 1, 1, 1],k = 3) == 2
    assert candidate(nums = [100, 200, 300, 400, 500],k = 1000) == 900
    assert candidate(nums = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10],k = 150) == 140
    assert candidate(nums = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],k = 850) == 800
    assert candidate(nums = [999, 999, 999, 999, 999, 999, 999, 999, 999, 999],k = 1998) == -1
    assert candidate(nums = [500, 400, 300, 200, 100],k = 800) == 700
    assert candidate(nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10],k = 18) == 17
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 180) == 170
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81],k = 190) == 189
    assert candidate(nums = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],k = 5) == 4
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 50) == 48
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],k = 1990) == 1989
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 30) == 29
    assert candidate(nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 1023) == 768
    assert candidate(nums = [2, 3, 6, 7, 9, 11, 13, 14, 18, 21],k = 30) == 29
    assert candidate(nums = [500, 400, 300, 200, 100, 50, 25, 10, 5, 1],k = 600) == 550
    assert candidate(nums = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],k = 230) == 220
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1800) == 1700
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],k = 20) == 19
    assert candidate(nums = [500, 400, 300, 200, 100, 50, 25, 10, 5, 1],k = 1000) == 900
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 250) == 240
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == -1
    assert candidate(nums = [100, 200, 300, 400, 500],k = 1000) == 900
    assert candidate(nums = [80, 70, 60, 50, 40, 30, 20, 10],k = 140) == 130
    assert candidate(nums = [100, 50, 25, 12, 6, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 200) == 150
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],k = 2000) == 1999
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1500) == 1400
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],k = 1999) == 1997
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1900) == 1800
    assert candidate(nums = [800, 700, 600, 500, 400, 300, 200, 100],k = 1200) == 1100
    assert candidate(nums = [9, 8, 7, 6, 5, 4, 3, 2, 1],k = 10) == 9
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1999) == 1900
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900],k = 1500) == 1400
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 200) == 190
    assert candidate(nums = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81],k = 190) == 189
    assert candidate(nums = [999, 1, 998, 2, 997, 3, 996, 4],k = 2000) == 1997
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 19) == 18
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 2
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 11) == 10
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 11) == 10
    assert candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],k = 1800) == 1700
    assert candidate(nums = [1, 999, 2, 998, 3, 997, 4, 996, 5, 995],k = 2000) == 1997
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 2
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 25) == 24
    assert candidate(nums = [500, 499, 498, 497, 496, 495, 494, 493, 492, 491, 490, 489, 488, 487, 486, 485, 484, 483, 482, 481, 480, 479, 478, 477, 476, 475, 474, 473, 472, 471, 470, 469, 468, 467, 466, 465, 464, 463, 462, 461, 460, 459, 458, 457, 456, 455, 454, 453, 452, 451, 450],k = 999) == 998
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 50) == 48
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 40) == 38
    assert candidate(nums = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],k = 210) == 209
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 50) == 49
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 150) == 140
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 150) == 145
    assert candidate(nums = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],k = 10) == -1
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 150) == 140
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990, 989, 988, 987, 986, 985, 984, 983, 982, 981, 980],k = 1999) == 1997
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 300) == 290
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 15) == 14
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],k = 70) == 65
    assert candidate(nums = [800, 700, 600, 500, 400, 300, 200, 100, 50, 10],k = 1200) == 1100
    assert candidate(nums = [1000, 999, 998, 997, 996, 995, 994, 993, 992, 991],k = 1998) == 1997
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],k = 100) == 99
    assert candidate(nums = [1, 999, 2, 998, 3, 997, 4, 996, 5, 995],k = 1998) == 1997
    assert candidate(nums = [500, 499, 498, 497, 496, 495],k = 1000) == 999
    assert candidate(nums = [50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31],k = 100) == 99
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 30) == 29
    assert candidate(nums = [1000, 500, 250, 125, 62, 31, 15, 7, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 1500) == 1250
    assert candidate(nums = [999, 998, 997, 996, 995, 994, 993, 992, 991, 990],k = 1985) == 1984
    assert candidate(nums = [990, 890, 790, 690, 590, 490, 390, 290, 190, 90, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 1900) == 1880
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 150) == 140
    assert candidate(nums = [999, 1, 998, 2, 997, 3, 996, 4, 995, 5],k = 2000) == 1997
    assert candidate(nums = [500, 500, 500, 500, 500, 500, 500, 500, 500, 500],k = 1000) == -1
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 39) == 38
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 18) == 17
    assert candidate(nums = [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100],k = 1700) == 1600
    assert candidate(nums = [50, 40, 30, 20, 10],k = 70) == 60
    assert candidate(nums = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100],k = 200) == -1
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1999) == 1900
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 300) == 290
    assert candidate(nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],k = 3) == 2
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 101) == 99
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 50) == 49
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900],k = 1800) == 1700
    assert candidate(nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],k = 20) == -1
    assert candidate(nums = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1600) == 1500
    assert candidate(nums = [500, 500, 500, 500, 500],k = 1000) == -1
    assert candidate(nums = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550],k = 1000) == 950


