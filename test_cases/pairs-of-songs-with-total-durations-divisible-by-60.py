def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = [1, 3, 5, 7, 9, 11]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [1, 3, 5, 7, 9, 11]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = [40, 20, 50, 30, 10]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [40, 20, 50, 30, 10]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(time = [60, 120, 180, 240, 300]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [60, 120, 180, 240, 300]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(time = [37, 123, 45, 20, 7, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [37, 123, 45, 20, 7, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = [30, 60, 90, 120, 150]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [30, 60, 90, 120, 150]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(time = [10, 20, 30, 40, 50]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [10, 20, 30, 40, 50]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(time = [37, 49, 58, 37, 17]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [37, 49, 58, 37, 17]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = [60, 60, 60]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [60, 60, 60]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(time = [30, 20, 150, 100, 40]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [30, 20, 150, 100, 40]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(time = [15, 60, 75, 90, 105]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [15, 60, 75, 90, 105]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(time = [5, 10, 15, 20, 25, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [5, 10, 15, 20, 25, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = [59, 61, 59, 61, 59, 61]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [59, 61, 59, 61, 59, 61]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(time = [10, 50, 90, 150, 210]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [10, 50, 90, 150, 210]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(time = [120, 240, 360, 480, 600]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [120, 240, 360, 480, 600]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(time = [59, 1, 59, 2, 59, 3, 59, 4, 59, 5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [59, 1, 59, 2, 59, 3, 59, 4, 59, 5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(time = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(time = [59, 1, 59, 2, 58, 3, 57, 4, 56, 5, 55, 6, 54, 7, 53, 8, 52, 9, 51, 10, 50]) == 11
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [59, 1, 59, 2, 58, 3, 57, 4, 56, 5, 55, 6, 54, 7, 53, 8, 52, 9, 51, 10, 50]) == 11: {e}')
    
    total += 1
    try:
        result = candidate(time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(time = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240]) == 28
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240]) == 28: {e}')
    
    total += 1
    try:
        result = candidate(time = [1, 119, 2, 118, 3, 117, 4, 116, 5, 115]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [1, 119, 2, 118, 3, 117, 4, 116, 5, 115]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(time = [59, 61, 119, 121, 179, 181, 239, 241, 299, 301]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [59, 61, 119, 121, 179, 181, 239, 241, 299, 301]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(time = [29, 31, 17, 43, 13, 47, 7, 53, 19, 41]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [29, 31, 17, 43, 13, 47, 7, 53, 19, 41]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(time = [40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480]) == 22
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480]) == 22: {e}')
    
    total += 1
    try:
        result = candidate(time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = [5, 15, 25, 35, 45, 55, 105, 115, 125, 135, 145, 155]) == 12
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [5, 15, 25, 35, 45, 55, 105, 115, 125, 135, 145, 155]) == 12: {e}')
    
    total += 1
    try:
        result = candidate(time = [14, 26, 38, 50, 2, 18, 30, 42, 54, 6]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [14, 26, 38, 50, 2, 18, 30, 42, 54, 6]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(time = [59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = [35, 25, 55, 35, 25, 55, 35, 25, 55, 35, 25, 55, 35, 25, 55, 35, 25, 55, 35, 25, 55, 35, 25, 55, 35, 25, 55]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [35, 25, 55, 35, 25, 55, 35, 25, 55, 35, 25, 55, 35, 25, 55, 35, 25, 55, 35, 25, 55, 35, 25, 55, 35, 25, 55]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(time = [59, 119, 179, 239, 299, 359, 419, 479, 539, 599, 659, 719, 779, 839, 899]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [59, 119, 179, 239, 299, 359, 419, 479, 539, 599, 659, 719, 779, 839, 899]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 70
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 70: {e}')
    
    total += 1
    try:
        result = candidate(time = [35, 25, 55, 15, 45, 5, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295]) == 75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [35, 25, 55, 15, 45, 5, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295]) == 75: {e}')
    
    total += 1
    try:
        result = candidate(time = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900]) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900]) == 210: {e}')
    
    total += 1
    try:
        result = candidate(time = [40, 20, 50, 10, 80, 30, 70, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900, 930, 960, 990, 1020, 1050, 1080, 1110, 1140, 1170, 1200, 1230, 1260, 1290, 1320, 1350, 1380, 1410, 1440, 1470, 1500, 1530, 1560, 1590, 1620, 1650, 1680]) == 760
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [40, 20, 50, 10, 80, 30, 70, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900, 930, 960, 990, 1020, 1050, 1080, 1110, 1140, 1170, 1200, 1230, 1260, 1290, 1320, 1350, 1380, 1410, 1440, 1470, 1500, 1530, 1560, 1590, 1620, 1650, 1680]) == 760: {e}')
    
    total += 1
    try:
        result = candidate(time = [53, 5, 3, 17, 57, 23, 59, 41, 37, 19, 49, 11]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [53, 5, 3, 17, 57, 23, 59, 41, 37, 19, 49, 11]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(time = [1, 61, 121, 181, 241, 301, 361, 421, 481, 541, 601, 661, 721, 781, 841, 901, 961, 1021, 1081, 1141, 1201, 1261, 1321, 1381, 1441, 1501, 1561, 1621, 1681, 1741, 1801, 1861, 1921, 1981, 2041, 2101, 2161, 2221, 2281, 2341, 2401, 2461, 2521, 2581, 2641, 2701, 2761, 2821, 2881, 2941, 3001, 3061, 3121, 3181, 3241, 3301, 3361, 3421, 3481, 3541, 3601]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [1, 61, 121, 181, 241, 301, 361, 421, 481, 541, 601, 661, 721, 781, 841, 901, 961, 1021, 1081, 1141, 1201, 1261, 1321, 1381, 1441, 1501, 1561, 1621, 1681, 1741, 1801, 1861, 1921, 1981, 2041, 2101, 2161, 2221, 2281, 2341, 2401, 2461, 2521, 2581, 2641, 2701, 2761, 2821, 2881, 2941, 3001, 3061, 3121, 3181, 3241, 3301, 3361, 3421, 3481, 3541, 3601]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = [30, 45, 60, 75, 90, 105, 120, 135, 150, 165]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [30, 45, 60, 75, 90, 105, 120, 135, 150, 165]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(time = [37, 123, 45, 20, 7, 30, 23, 37, 123, 45, 20, 7, 30, 23, 37, 123, 45, 20, 7, 30]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [37, 123, 45, 20, 7, 30, 23, 37, 123, 45, 20, 7, 30, 23, 37, 123, 45, 20, 7, 30]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(time = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300]) == 145
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300]) == 145: {e}')
    
    total += 1
    try:
        result = candidate(time = [59, 59, 59, 59, 59, 1, 1, 1, 1, 1]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [59, 59, 59, 59, 59, 1, 1, 1, 1, 1]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(time = [33, 27, 42, 18, 24, 36, 6, 54, 12, 48]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [33, 27, 42, 18, 24, 36, 6, 54, 12, 48]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(time = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 60
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 60: {e}')
    
    total += 1
    try:
        result = candidate(time = [59, 61, 119, 121, 179, 181, 239, 241, 299, 301, 359, 361, 419, 421, 479, 481, 539, 541, 599, 601, 659, 661, 719, 721, 779, 781, 839, 841, 899, 901, 959, 961, 1019, 1021, 1079, 1081, 1139, 1141, 1199, 1201, 1259, 1261, 1319, 1321, 1379, 1381, 1439, 1441, 1499, 1501, 1559, 1561, 1619, 1621, 1679, 1681]) == 784
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [59, 61, 119, 121, 179, 181, 239, 241, 299, 301, 359, 361, 419, 421, 479, 481, 539, 541, 599, 601, 659, 661, 719, 721, 779, 781, 839, 841, 899, 901, 959, 961, 1019, 1021, 1079, 1081, 1139, 1141, 1199, 1201, 1259, 1261, 1319, 1321, 1379, 1381, 1439, 1441, 1499, 1501, 1559, 1561, 1619, 1621, 1679, 1681]) == 784: {e}')
    
    total += 1
    try:
        result = candidate(time = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(time = [1, 59, 2, 58, 3, 57, 4, 56, 5, 55, 6, 54, 7, 53, 8, 52, 9, 51, 10, 50]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [1, 59, 2, 58, 3, 57, 4, 56, 5, 55, 6, 54, 7, 53, 8, 52, 9, 51, 10, 50]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(time = [1, 2, 3, 4, 5, 55, 56, 57, 58, 59]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [1, 2, 3, 4, 5, 55, 56, 57, 58, 59]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(time = [1, 61, 2, 62, 3, 63, 4, 64, 5, 65, 6, 66, 7, 67, 8, 68, 9, 69, 10, 70]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [1, 61, 2, 62, 3, 63, 4, 64, 5, 65, 6, 66, 7, 67, 8, 68, 9, 69, 10, 70]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = [1, 2, 3, 4, 5, 58, 59, 60, 61, 62, 63, 118, 119, 120, 121, 122, 178, 179, 180, 181, 182]) == 27
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [1, 2, 3, 4, 5, 58, 59, 60, 61, 62, 63, 118, 119, 120, 121, 122, 178, 179, 180, 181, 182]) == 27: {e}')
    
    total += 1
    try:
        result = candidate(time = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900, 960, 1020, 1080, 1140, 1200, 1260, 1320, 1380, 1440, 1500, 1560, 1620, 1680, 1740, 1800, 1860, 1920, 1980, 2040, 2100, 2160, 2220, 2280, 2340, 2400, 2460, 2520, 2580, 2640, 2700, 2760, 2820, 2880, 2940, 3000]) == 1225
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900, 960, 1020, 1080, 1140, 1200, 1260, 1320, 1380, 1440, 1500, 1560, 1620, 1680, 1740, 1800, 1860, 1920, 1980, 2040, 2100, 2160, 2220, 2280, 2340, 2400, 2460, 2520, 2580, 2640, 2700, 2760, 2820, 2880, 2940, 3000]) == 1225: {e}')
    
    total += 1
    try:
        result = candidate(time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(time = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(time = [58, 59, 1, 2, 57, 56, 3, 4, 55, 54, 5, 6, 53, 52, 7, 8, 51, 50, 9, 10, 49, 48, 11, 12, 47, 46, 13, 14, 45, 44, 15, 16, 43, 42, 17, 18, 41, 40, 19, 20, 39, 38, 21, 22, 37, 36, 23, 24, 35, 34, 25, 26, 33, 32, 27, 28, 31, 30, 29]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [58, 59, 1, 2, 57, 56, 3, 4, 55, 54, 5, 6, 53, 52, 7, 8, 51, 50, 9, 10, 49, 48, 11, 12, 47, 46, 13, 14, 45, 44, 15, 16, 43, 42, 17, 18, 41, 40, 19, 20, 39, 38, 21, 22, 37, 36, 23, 24, 35, 34, 25, 26, 33, 32, 27, 28, 31, 30, 29]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(time = [29, 31, 59, 1, 58, 2, 57, 3, 56, 4, 55, 5, 54, 6, 53, 7, 52, 8, 51, 9, 50, 10, 49, 11, 48, 12, 47, 13, 46, 14, 45, 15, 44, 16, 43, 17, 42, 18, 41, 19, 40, 20, 39, 21, 38, 22, 37, 23, 36, 24, 35, 25, 34, 26, 33, 27, 32, 28]) == 29
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [29, 31, 59, 1, 58, 2, 57, 3, 56, 4, 55, 5, 54, 6, 53, 7, 52, 8, 51, 9, 50, 10, 49, 11, 48, 12, 47, 13, 46, 14, 45, 15, 44, 16, 43, 17, 42, 18, 41, 19, 40, 20, 39, 21, 38, 22, 37, 23, 36, 24, 35, 25, 34, 26, 33, 27, 32, 28]) == 29: {e}')
    
    total += 1
    try:
        result = candidate(time = [45, 105, 165, 225, 285, 345, 405, 465, 525, 585]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [45, 105, 165, 225, 285, 345, 405, 465, 525, 585]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = [40, 20, 60, 80, 100, 120, 140, 160, 180, 200]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [40, 20, 60, 80, 100, 120, 140, 160, 180, 200]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(time = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600]) == 90
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600]) == 90: {e}')
    
    total += 1
    try:
        result = candidate(time = [1, 2, 3, 4, 5, 58, 59, 60, 61, 62, 118, 119, 120, 121, 122]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [1, 2, 3, 4, 5, 58, 59, 60, 61, 62, 118, 119, 120, 121, 122]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(time = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900, 930, 960, 990, 1020, 1050, 1080, 1110, 1140, 1170, 1200, 1230, 1260, 1290, 1320, 1350, 1380, 1410, 1440, 1470, 1500]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900, 930, 960, 990, 1020, 1050, 1080, 1110, 1140, 1170, 1200, 1230, 1260, 1290, 1320, 1350, 1380, 1410, 1440, 1470, 1500]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(time = [31, 29, 1, 59, 2, 58, 3, 57, 4, 56, 5, 55, 6, 54, 7, 53, 8, 52, 9, 51]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [31, 29, 1, 59, 2, 58, 3, 57, 4, 56, 5, 55, 6, 54, 7, 53, 8, 52, 9, 51]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(time = [40, 40, 40, 40, 40, 40, 20, 20, 20, 20, 20, 20]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [40, 40, 40, 40, 40, 40, 20, 20, 20, 20, 20, 20]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(time = [60, 120, 180, 240, 300, 360, 420, 480, 540]) == 36
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [60, 120, 180, 240, 300, 360, 420, 480, 540]) == 36: {e}')
    
    total += 1
    try:
        result = candidate(time = [59, 1, 59, 1, 59, 1, 59, 1]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [59, 1, 59, 1, 59, 1, 59, 1]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(time = [1, 59, 2, 58, 3, 57, 4, 56, 5, 55, 6, 54, 7, 53]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [1, 59, 2, 58, 3, 57, 4, 56, 5, 55, 6, 54, 7, 53]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(time = [3, 12, 21, 30, 39, 48, 57, 66, 75, 84, 93, 102, 111, 120, 129, 138, 147, 156, 165, 174]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [3, 12, 21, 30, 39, 48, 57, 66, 75, 84, 93, 102, 111, 120, 129, 138, 147, 156, 165, 174]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(time = [54, 42, 18, 24, 30, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600]) == 46
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [54, 42, 18, 24, 30, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600]) == 46: {e}')
    
    total += 1
    try:
        result = candidate(time = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(time = [11, 22, 33, 44, 55, 11, 22, 33, 44, 55, 11, 22, 33, 44, 55, 11, 22, 33, 44, 55]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [11, 22, 33, 44, 55, 11, 22, 33, 44, 55, 11, 22, 33, 44, 55, 11, 22, 33, 44, 55]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = [42, 18, 78, 36, 12, 24, 30, 60, 120, 180]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [42, 18, 78, 36, 12, 24, 30, 60, 120, 180]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = [40, 20, 50, 30, 10, 70, 110, 90]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [40, 20, 50, 30, 10, 70, 110, 90]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(time = [51, 9, 42, 18, 27, 33, 6, 54, 12, 48]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [51, 9, 42, 18, 27, 33, 6, 54, 12, 48]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(time = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(time = [1, 2, 3, 4, 5, 58, 59, 118, 119, 178, 179, 238, 239, 298, 299]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [1, 2, 3, 4, 5, 58, 59, 118, 119, 178, 179, 238, 239, 298, 299]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(time = [45, 90, 135, 180, 225, 270, 315, 360, 405, 450]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [45, 90, 135, 180, 225, 270, 315, 360, 405, 450]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(time = [15, 25, 35, 45, 55, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195]) == 19
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [15, 25, 35, 45, 55, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195]) == 19: {e}')
    
    total += 1
    try:
        result = candidate(time = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(time = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144]) == 13
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144]) == 13: {e}')
    
    total += 1
    try:
        result = candidate(time = [14, 44, 23, 32, 56, 33, 92, 88, 31, 29]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [14, 44, 23, 32, 56, 33, 92, 88, 31, 29]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(time = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360]) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360]) == 30: {e}')
    
    total += 1
    try:
        result = candidate(time = [47, 47, 47, 47, 47, 13, 13, 13, 13, 13]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [47, 47, 47, 47, 47, 13, 13, 13, 13, 13]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(time = [37, 37, 37, 37, 37, 23, 23, 23, 23, 23, 13, 13, 13, 13, 13]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [37, 37, 37, 37, 37, 23, 23, 23, 23, 23, 13, 13, 13, 13, 13]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(time = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900]) == 105
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900]) == 105: {e}')
    
    total += 1
    try:
        result = candidate(time = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600]) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600]) == 45: {e}')
    
    total += 1
    try:
        result = candidate(time = [37, 123, 45, 20, 7, 30, 60, 120, 180, 240]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(time = [37, 123, 45, 20, 7, 30, 60, 120, 180, 240]) == 6: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
    assert candidate(time = [1, 3, 5, 7, 9, 11]) == 0
    assert candidate(time = [40, 20, 50, 30, 10]) == 2
    assert candidate(time = [60, 120, 180, 240, 300]) == 10
    assert candidate(time = [37, 123, 45, 20, 7, 30]) == 0
    assert candidate(time = [30, 60, 90, 120, 150]) == 4
    assert candidate(time = [10, 20, 30, 40, 50]) == 2
    assert candidate(time = [37, 49, 58, 37, 17]) == 0
    assert candidate(time = [60, 60, 60]) == 3
    assert candidate(time = [30, 20, 150, 100, 40]) == 3
    assert candidate(time = [15, 60, 75, 90, 105]) == 2
    assert candidate(time = [5, 10, 15, 20, 25, 30]) == 0
    assert candidate(time = [59, 61, 59, 61, 59, 61]) == 9
    assert candidate(time = [10, 50, 90, 150, 210]) == 4
    assert candidate(time = [120, 240, 360, 480, 600]) == 10
    assert candidate(time = [59, 1, 59, 2, 59, 3, 59, 4, 59, 5]) == 5
    assert candidate(time = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570]) == 81
    assert candidate(time = [59, 1, 59, 2, 58, 3, 57, 4, 56, 5, 55, 6, 54, 7, 53, 8, 52, 9, 51, 10, 50]) == 11
    assert candidate(time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]) == 30
    assert candidate(time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]) == 29
    assert candidate(time = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240]) == 28
    assert candidate(time = [1, 119, 2, 118, 3, 117, 4, 116, 5, 115]) == 5
    assert candidate(time = [59, 61, 119, 121, 179, 181, 239, 241, 299, 301]) == 25
    assert candidate(time = [29, 31, 17, 43, 13, 47, 7, 53, 19, 41]) == 5
    assert candidate(time = [40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480]) == 22
    assert candidate(time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
    assert candidate(time = [5, 15, 25, 35, 45, 55, 105, 115, 125, 135, 145, 155]) == 12
    assert candidate(time = [14, 26, 38, 50, 2, 18, 30, 42, 54, 6]) == 2
    assert candidate(time = [59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59, 59]) == 0
    assert candidate(time = [35, 25, 55, 35, 25, 55, 35, 25, 55, 35, 25, 55, 35, 25, 55, 35, 25, 55, 35, 25, 55, 35, 25, 55, 35, 25, 55]) == 81
    assert candidate(time = [59, 119, 179, 239, 299, 359, 419, 479, 539, 599, 659, 719, 779, 839, 899]) == 0
    assert candidate(time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 70
    assert candidate(time = [35, 25, 55, 15, 45, 5, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205, 215, 225, 235, 245, 255, 265, 275, 285, 295]) == 75
    assert candidate(time = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900]) == 210
    assert candidate(time = [40, 20, 50, 10, 80, 30, 70, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900, 930, 960, 990, 1020, 1050, 1080, 1110, 1140, 1170, 1200, 1230, 1260, 1290, 1320, 1350, 1380, 1410, 1440, 1470, 1500, 1530, 1560, 1590, 1620, 1650, 1680]) == 760
    assert candidate(time = [53, 5, 3, 17, 57, 23, 59, 41, 37, 19, 49, 11]) == 4
    assert candidate(time = [1, 61, 121, 181, 241, 301, 361, 421, 481, 541, 601, 661, 721, 781, 841, 901, 961, 1021, 1081, 1141, 1201, 1261, 1321, 1381, 1441, 1501, 1561, 1621, 1681, 1741, 1801, 1861, 1921, 1981, 2041, 2101, 2161, 2221, 2281, 2341, 2401, 2461, 2521, 2581, 2641, 2701, 2761, 2821, 2881, 2941, 3001, 3061, 3121, 3181, 3241, 3301, 3361, 3421, 3481, 3541, 3601]) == 0
    assert candidate(time = [30, 45, 60, 75, 90, 105, 120, 135, 150, 165]) == 10
    assert candidate(time = [37, 123, 45, 20, 7, 30, 23, 37, 123, 45, 20, 7, 30, 23, 37, 123, 45, 20, 7, 30]) == 9
    assert candidate(time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 16
    assert candidate(time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]) == 29
    assert candidate(time = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300]) == 145
    assert candidate(time = [59, 59, 59, 59, 59, 1, 1, 1, 1, 1]) == 25
    assert candidate(time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) == 16
    assert candidate(time = [33, 27, 42, 18, 24, 36, 6, 54, 12, 48]) == 5
    assert candidate(time = [30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]) == 60
    assert candidate(time = [59, 61, 119, 121, 179, 181, 239, 241, 299, 301, 359, 361, 419, 421, 479, 481, 539, 541, 599, 601, 659, 661, 719, 721, 779, 781, 839, 841, 899, 901, 959, 961, 1019, 1021, 1079, 1081, 1139, 1141, 1199, 1201, 1259, 1261, 1319, 1321, 1379, 1381, 1439, 1441, 1499, 1501, 1559, 1561, 1619, 1621, 1679, 1681]) == 784
    assert candidate(time = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]) == 9
    assert candidate(time = [1, 59, 2, 58, 3, 57, 4, 56, 5, 55, 6, 54, 7, 53, 8, 52, 9, 51, 10, 50]) == 10
    assert candidate(time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500]) == 200
    assert candidate(time = [1, 2, 3, 4, 5, 55, 56, 57, 58, 59]) == 5
    assert candidate(time = [1, 61, 2, 62, 3, 63, 4, 64, 5, 65, 6, 66, 7, 67, 8, 68, 9, 69, 10, 70]) == 0
    assert candidate(time = [1, 2, 3, 4, 5, 58, 59, 60, 61, 62, 63, 118, 119, 120, 121, 122, 178, 179, 180, 181, 182]) == 27
    assert candidate(time = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900, 960, 1020, 1080, 1140, 1200, 1260, 1320, 1380, 1440, 1500, 1560, 1620, 1680, 1740, 1800, 1860, 1920, 1980, 2040, 2100, 2160, 2220, 2280, 2340, 2400, 2460, 2520, 2580, 2640, 2700, 2760, 2820, 2880, 2940, 3000]) == 1225
    assert candidate(time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]) == 10
    assert candidate(time = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205]) == 36
    assert candidate(time = [58, 59, 1, 2, 57, 56, 3, 4, 55, 54, 5, 6, 53, 52, 7, 8, 51, 50, 9, 10, 49, 48, 11, 12, 47, 46, 13, 14, 45, 44, 15, 16, 43, 42, 17, 18, 41, 40, 19, 20, 39, 38, 21, 22, 37, 36, 23, 24, 35, 34, 25, 26, 33, 32, 27, 28, 31, 30, 29]) == 29
    assert candidate(time = [29, 31, 59, 1, 58, 2, 57, 3, 56, 4, 55, 5, 54, 6, 53, 7, 52, 8, 51, 9, 50, 10, 49, 11, 48, 12, 47, 13, 46, 14, 45, 15, 44, 16, 43, 17, 42, 18, 41, 19, 40, 20, 39, 21, 38, 22, 37, 23, 36, 24, 35, 25, 34, 26, 33, 27, 32, 28]) == 29
    assert candidate(time = [45, 105, 165, 225, 285, 345, 405, 465, 525, 585]) == 0
    assert candidate(time = [40, 20, 60, 80, 100, 120, 140, 160, 180, 200]) == 15
    assert candidate(time = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600]) == 90
    assert candidate(time = [1, 2, 3, 4, 5, 58, 59, 60, 61, 62, 118, 119, 120, 121, 122]) == 13
    assert candidate(time = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900, 930, 960, 990, 1020, 1050, 1080, 1110, 1140, 1170, 1200, 1230, 1260, 1290, 1320, 1350, 1380, 1410, 1440, 1470, 1500]) == 600
    assert candidate(time = [31, 29, 1, 59, 2, 58, 3, 57, 4, 56, 5, 55, 6, 54, 7, 53, 8, 52, 9, 51]) == 10
    assert candidate(time = [40, 40, 40, 40, 40, 40, 20, 20, 20, 20, 20, 20]) == 36
    assert candidate(time = [60, 120, 180, 240, 300, 360, 420, 480, 540]) == 36
    assert candidate(time = [59, 1, 59, 1, 59, 1, 59, 1]) == 16
    assert candidate(time = [1, 59, 2, 58, 3, 57, 4, 56, 5, 55, 6, 54, 7, 53]) == 7
    assert candidate(time = [3, 12, 21, 30, 39, 48, 57, 66, 75, 84, 93, 102, 111, 120, 129, 138, 147, 156, 165, 174]) == 9
    assert candidate(time = [54, 42, 18, 24, 30, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600]) == 46
    assert candidate(time = [30, 30, 30, 30, 30, 30, 30, 30, 30, 30]) == 45
    assert candidate(time = [11, 22, 33, 44, 55, 11, 22, 33, 44, 55, 11, 22, 33, 44, 55, 11, 22, 33, 44, 55]) == 0
    assert candidate(time = [42, 18, 78, 36, 12, 24, 30, 60, 120, 180]) == 6
    assert candidate(time = [40, 20, 50, 30, 10, 70, 110, 90]) == 6
    assert candidate(time = [51, 9, 42, 18, 27, 33, 6, 54, 12, 48]) == 5
    assert candidate(time = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 132, 143, 154, 165]) == 0
    assert candidate(time = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70]) == 0
    assert candidate(time = [1, 2, 3, 4, 5, 58, 59, 118, 119, 178, 179, 238, 239, 298, 299]) == 10
    assert candidate(time = [45, 90, 135, 180, 225, 270, 315, 360, 405, 450]) == 10
    assert candidate(time = [15, 25, 35, 45, 55, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195]) == 19
    assert candidate(time = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300]) == 20
    assert candidate(time = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144]) == 13
    assert candidate(time = [14, 44, 23, 32, 56, 33, 92, 88, 31, 29]) == 3
    assert candidate(time = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360]) == 30
    assert candidate(time = [47, 47, 47, 47, 47, 13, 13, 13, 13, 13]) == 25
    assert candidate(time = [37, 37, 37, 37, 37, 23, 23, 23, 23, 23, 13, 13, 13, 13, 13]) == 25
    assert candidate(time = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900]) == 105
    assert candidate(time = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600]) == 45
    assert candidate(time = [37, 123, 45, 20, 7, 30, 60, 120, 180, 240]) == 6


