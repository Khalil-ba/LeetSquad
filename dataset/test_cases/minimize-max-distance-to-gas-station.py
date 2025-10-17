def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(stations = [23, 24, 36, 39, 46, 56, 57, 65, 84, 98],k = 1) == 13.999999737279722
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [23, 24, 36, 39, 46, 56, 57, 65, 84, 98],k = 1) == 13.999999737279722: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 5, 9, 14, 20, 25, 30, 35, 40],k = 5) == 4.999999703159119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 5, 9, 14, 20, 25, 30, 35, 40],k = 5) == 4.999999703159119: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 9) == 0.4999996860988176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 9) == 0.4999996860988176: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50],k = 2) == 9.999999406318238
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50],k = 2) == 9.999999406318238: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 100000000],k = 1000000) == 99.99989885045579
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 100000000],k = 1000000) == 99.99989885045579: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 10, 15, 20, 25, 30],k = 3) == 4.999999703159119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 10, 15, 20, 25, 30],k = 3) == 4.999999703159119: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 15, 25, 35, 45, 55],k = 3) == 9.999999406318238
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 15, 25, 35, 45, 55],k = 3) == 9.999999406318238: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 20) == 4.999999703159119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 20) == 4.999999703159119: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 50000000, 100000000],k = 500000) == 199.99919942392808
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 50000000, 100000000],k = 500000) == 199.99919942392808: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 50, 90, 130, 170, 210, 250, 290, 330, 370, 410, 450, 490, 530, 570, 610, 650, 690, 730, 770, 810, 850, 890, 930, 970, 1000],k = 50) == 13.333333015452808
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 50, 90, 130, 170, 210, 250, 290, 330, 370, 410, 450, 490, 530, 570, 610, 650, 690, 730, 770, 810, 850, 890, 930, 970, 1000],k = 50) == 13.333333015452808: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10000000],k = 500000) == 19.999957601157803
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10000000],k = 500000) == 19.999957601157803: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 1.9999994549380062
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 1.9999994549380062: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 50) == 292.5714284174319
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 50) == 292.5714284174319: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],k = 100) == 2.4999998515795596
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],k = 100) == 2.4999998515795596: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 25, 50, 75, 100],k = 10) == 8.33333331229369
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 25, 50, 75, 100],k = 10) == 8.33333331229369: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 3.3333328985918342
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 3.3333328985918342: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10, 25, 40, 55, 70, 85, 100, 115, 130, 145, 160, 175, 190, 200],k = 20) == 7.499999554738679
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10, 25, 40, 55, 70, 85, 100, 115, 130, 145, 160, 175, 190, 200],k = 20) == 7.499999554738679: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99],k = 50) == 0.9999993721976352
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99],k = 50) == 0.9999993721976352: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 5, 10, 15, 25, 50, 100],k = 10) == 7.142856617292637
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 5, 10, 15, 25, 50, 100],k = 10) == 7.142856617292637: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 100000000],k = 100000) == 999.9899894808095
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 100000000],k = 100000) == 999.9899894808095: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 23, 36, 39, 46, 56, 57, 65, 84, 98],k = 5) == 9.999999406318238
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 23, 36, 39, 46, 56, 57, 65, 84, 98],k = 5) == 9.999999406318238: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 30) == 3.3333328985918342
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 30) == 3.3333328985918342: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 25) == 4.999999703159119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 25) == 4.999999703159119: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],k = 25) == 3.3333328985918342
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],k = 25) == 3.3333328985918342: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300],k = 100) == 2.6666661767649202
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300],k = 100) == 2.6666661767649202: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 20) == 4.999999703159119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 20) == 4.999999703159119: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 5, 10, 25, 50, 100, 200, 500, 1000, 5000, 10000],k = 20) == 444.4444442697204
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 5, 10, 25, 50, 100, 200, 500, 1000, 5000, 10000],k = 20) == 444.4444442697204: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 50) == 2.4999998515795596
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 50) == 2.4999998515795596: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 15) == 4.999999703159119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 15) == 4.999999703159119: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 4.999999703159119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 4.999999703159119: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000],k = 100) == 4.999999703159119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000],k = 100) == 4.999999703159119: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99],k = 100) == 0.6666660112841782
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99],k = 100) == 0.6666660112841782: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625],k = 150) == 3.8333332952333876
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625],k = 150) == 3.8333332952333876: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000],k = 1000) == 99778.27050988708
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000],k = 1000) == 99778.27050988708: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000],k = 100) == 978260.8695651619
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000],k = 100) == 978260.8695651619: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 30) == 0.4999996860988176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 30) == 0.4999996860988176: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 50) == 0.4999996860988176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 50) == 0.4999996860988176: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205],k = 50) == 3.3333328985918342
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205],k = 50) == 3.3333328985918342: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250],k = 50) == 3.3333328985918342
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250],k = 50) == 3.3333328985918342: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 100000000],k = 999999) == 99.9999983264388
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 100000000],k = 999999) == 99.9999983264388: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 4.999999703159119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 4.999999703159119: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 15) == 4.999999703159119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 15) == 4.999999703159119: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 50) == 1.6666660940245492
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 50) == 1.6666660940245492: {e}')
    
    total += 1
    try:
        result = candidate(stations = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119],k = 50) == 0.33333265037072124
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119],k = 50) == 0.33333265037072124: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400],k = 500) == 0.7692307235629414
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400],k = 500) == 0.7692307235629414: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300],k = 200) == 1.249999570518412
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300],k = 200) == 1.249999570518412: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],k = 20) == 38.833332638432694
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],k = 20) == 38.833332638432694: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 20) == 4.999999703159119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 20) == 4.999999703159119: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 25, 50, 75, 100, 125, 150, 175, 200],k = 10) == 12.499999968440534
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 25, 50, 75, 100, 125, 150, 175, 200],k = 10) == 12.499999968440534: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 30) == 0.4999996860988176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 30) == 0.4999996860988176: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 100) == 4.923076346585731
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 100) == 4.923076346585731: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575],k = 150) == 6721.641025109193
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575],k = 150) == 6721.641025109193: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 30) == 4.999999703159119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 30) == 4.999999703159119: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 350, 400, 450, 500],k = 150) == 3.1249996368387656
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 350, 400, 450, 500],k = 150) == 3.1249996368387656: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 100) == 0.9090904029562807
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 100) == 0.9090904029562807: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 15) == 4.999999703159119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 15) == 4.999999703159119: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 30) == 4.999999703159119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 30) == 4.999999703159119: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 5, 10, 20, 30, 50, 60, 70, 80, 100],k = 20) == 3.9999996204187482
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 5, 10, 20, 30, 50, 60, 70, 80, 100],k = 20) == 3.9999996204187482: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 50) == 3.3333328985918342
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 50) == 3.3333328985918342: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 20, 35, 50, 65, 80, 95],k = 15) == 4.999999703159119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 20, 35, 50, 65, 80, 95],k = 15) == 4.999999703159119: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 5, 10, 20, 30, 50, 70, 90, 100],k = 20) == 3.9999996204187482
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 5, 10, 20, 30, 50, 70, 90, 100],k = 20) == 3.9999996204187482: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400],k = 100) == 3.3333328985918342
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400],k = 100) == 3.3333328985918342: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100],k = 12) == 4.999999703159119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100],k = 12) == 4.999999703159119: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1000) == 0.990098669717554
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1000) == 0.990098669717554: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 100000000],k = 1000) == 99900.09890046282
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 100000000],k = 1000) == 99900.09890046282: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],k = 50) == 0.6666660112841782
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],k = 50) == 0.6666660112841782: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016],k = 50) == 25.499999622979885
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016],k = 50) == 25.499999622979885: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 15) == 4.999999703159119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 15) == 4.999999703159119: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],k = 100) == 2.4999998515795596
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],k = 100) == 2.4999998515795596: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500],k = 25) == 14.285713945128009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500],k = 25) == 14.285713945128009: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 20) == 2.4999998515795596
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 20) == 2.4999998515795596: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],k = 200) == 5090.1747570719635
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],k = 200) == 5090.1747570719635: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 500) == 1.9607838908086705
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 500) == 1.9607838908086705: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 500) == 19.607842460800384
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 500) == 19.607842460800384: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195],k = 100) == 1.6666660940245492
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195],k = 100) == 1.6666660940245492: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 50) == 0.4999996860988176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 50) == 0.4999996860988176: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 0.9999993721976352
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 0.9999993721976352: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610],k = 30) == 17.799999341150397
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610],k = 30) == 17.799999341150397: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],k = 50) == 16.66666662458738
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],k = 50) == 16.66666662458738: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10, 50, 100, 200, 500, 1000, 2000, 5000, 10000],k = 500) == 19.86754938343438
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10, 50, 100, 200, 500, 1000, 2000, 5000, 10000],k = 500) == 19.86754938343438: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195],k = 25) == 4.999999703159119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195],k = 25) == 4.999999703159119: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 1000) == 997782.7050995813
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 1000) == 997782.7050995813: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 15) == 1.9999994549380062
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 15) == 1.9999994549380062: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000],k = 100000) == 999.9777780933528
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000],k = 100000) == 999.9777780933528: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 99.99999974752427
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 99.99999974752427: {e}')
    
    total += 1
    try:
        result = candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],k = 250) == 1.111110492502121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],k = 250) == 1.111110492502121: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200],k = 100) == 1.7857139766874752
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200],k = 100) == 1.7857139766874752: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500],k = 50) == 9.090909003361958
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500],k = 50) == 9.090909003361958: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 10) == 4.999999703159119
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 10) == 4.999999703159119: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1000) == 0.990098669717554
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1000) == 0.990098669717554: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000, 80000000, 90000000, 100000000],k = 1000000) == 99.99899930335232
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000, 80000000, 90000000, 100000000],k = 1000000) == 99.99899930335232: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380],k = 200) == 1.8181815164552972
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380],k = 200) == 1.8181815164552972: {e}')
    
    total += 1
    try:
        result = candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 0.9999993721976352
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 0.9999993721976352: {e}')
    
    total += 1
    try:
        result = candidate(stations = [5, 10, 20, 35, 55, 80, 110, 145, 185, 230, 280, 335, 400, 470, 550, 640, 740, 850, 970, 1100],k = 50) == 18.333332718611928
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(stations = [5, 10, 20, 35, 55, 80, 110, 145, 185, 230, 280, 335, 400, 470, 550, 640, 740, 850, 970, 1100],k = 50) == 18.333332718611928: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(stations = [23, 24, 36, 39, 46, 56, 57, 65, 84, 98],k = 1) == 13.999999737279722
    assert candidate(stations = [1, 5, 9, 14, 20, 25, 30, 35, 40],k = 5) == 4.999999703159119
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],k = 9) == 0.4999996860988176
    assert candidate(stations = [10, 20, 30, 40, 50],k = 2) == 9.999999406318238
    assert candidate(stations = [1, 100000000],k = 1000000) == 99.99989885045579
    assert candidate(stations = [5, 10, 15, 20, 25, 30],k = 3) == 4.999999703159119
    assert candidate(stations = [5, 15, 25, 35, 45, 55],k = 3) == 9.999999406318238
    assert candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 20) == 4.999999703159119
    assert candidate(stations = [1, 50000000, 100000000],k = 500000) == 199.99919942392808
    assert candidate(stations = [10, 50, 90, 130, 170, 210, 250, 290, 330, 370, 410, 450, 490, 530, 570, 610, 650, 690, 730, 770, 810, 850, 890, 930, 970, 1000],k = 50) == 13.333333015452808
    assert candidate(stations = [1, 10000000],k = 500000) == 19.999957601157803
    assert candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 10) == 1.9999994549380062
    assert candidate(stations = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384],k = 50) == 292.5714284174319
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],k = 100) == 2.4999998515795596
    assert candidate(stations = [5, 25, 50, 75, 100],k = 10) == 8.33333331229369
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 20) == 3.3333328985918342
    assert candidate(stations = [1, 10, 25, 40, 55, 70, 85, 100, 115, 130, 145, 160, 175, 190, 200],k = 20) == 7.499999554738679
    assert candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99],k = 50) == 0.9999993721976352
    assert candidate(stations = [1, 2, 5, 10, 15, 25, 50, 100],k = 10) == 7.142856617292637
    assert candidate(stations = [1, 100000000],k = 100000) == 999.9899894808095
    assert candidate(stations = [1, 23, 36, 39, 46, 56, 57, 65, 84, 98],k = 5) == 9.999999406318238
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 30) == 3.3333328985918342
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 25) == 4.999999703159119
    assert candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90],k = 25) == 3.3333328985918342
    assert candidate(stations = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300],k = 100) == 2.6666661767649202
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 20) == 4.999999703159119
    assert candidate(stations = [1, 5, 10, 25, 50, 100, 200, 500, 1000, 5000, 10000],k = 20) == 444.4444442697204
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 50) == 2.4999998515795596
    assert candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 15) == 4.999999703159119
    assert candidate(stations = [1, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 4.999999703159119
    assert candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000],k = 100) == 4.999999703159119
    assert candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99],k = 100) == 0.6666660112841782
    assert candidate(stations = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625],k = 150) == 3.8333332952333876
    assert candidate(stations = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000],k = 1000) == 99778.27050988708
    assert candidate(stations = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000],k = 100) == 978260.8695651619
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 30) == 0.4999996860988176
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 50) == 0.4999996860988176
    assert candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205],k = 50) == 3.3333328985918342
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250],k = 50) == 3.3333328985918342
    assert candidate(stations = [1, 100000000],k = 999999) == 99.9999983264388
    assert candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 10) == 4.999999703159119
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 15) == 4.999999703159119
    assert candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 50) == 1.6666660940245492
    assert candidate(stations = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119],k = 50) == 0.33333265037072124
    assert candidate(stations = [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400],k = 500) == 0.7692307235629414
    assert candidate(stations = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300],k = 200) == 1.249999570518412
    assert candidate(stations = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987],k = 20) == 38.833332638432694
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],k = 20) == 4.999999703159119
    assert candidate(stations = [5, 25, 50, 75, 100, 125, 150, 175, 200],k = 10) == 12.499999968440534
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],k = 30) == 0.4999996860988176
    assert candidate(stations = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],k = 100) == 4.923076346585731
    assert candidate(stations = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287, 1048575],k = 150) == 6721.641025109193
    assert candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 30) == 4.999999703159119
    assert candidate(stations = [1, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 350, 400, 450, 500],k = 150) == 3.1249996368387656
    assert candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 100) == 0.9090904029562807
    assert candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],k = 15) == 4.999999703159119
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 30) == 4.999999703159119
    assert candidate(stations = [1, 2, 5, 10, 20, 30, 50, 60, 70, 80, 100],k = 20) == 3.9999996204187482
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200],k = 50) == 3.3333328985918342
    assert candidate(stations = [5, 20, 35, 50, 65, 80, 95],k = 15) == 4.999999703159119
    assert candidate(stations = [1, 5, 10, 20, 30, 50, 70, 90, 100],k = 20) == 3.9999996204187482
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400],k = 100) == 3.3333328985918342
    assert candidate(stations = [1, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100],k = 12) == 4.999999703159119
    assert candidate(stations = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1000) == 0.990098669717554
    assert candidate(stations = [1, 100000000],k = 1000) == 99900.09890046282
    assert candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49],k = 50) == 0.6666660112841782
    assert candidate(stations = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 1035, 1081, 1128, 1176, 1225, 1275, 1326, 1378, 1431, 1485, 1540, 1596, 1653, 1711, 1770, 1830, 1891, 1953, 2016],k = 50) == 25.499999622979885
    assert candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 15) == 4.999999703159119
    assert candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],k = 100) == 2.4999998515795596
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500],k = 25) == 14.285713945128009
    assert candidate(stations = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],k = 20) == 2.4999998515795596
    assert candidate(stations = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],k = 200) == 5090.1747570719635
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 500) == 1.9607838908086705
    assert candidate(stations = [10, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],k = 500) == 19.607842460800384
    assert candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195],k = 100) == 1.6666660940245492
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50],k = 50) == 0.4999996860988176
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],k = 10) == 0.9999993721976352
    assert candidate(stations = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610],k = 30) == 17.799999341150397
    assert candidate(stations = [1, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000],k = 50) == 16.66666662458738
    assert candidate(stations = [1, 10, 50, 100, 200, 500, 1000, 2000, 5000, 10000],k = 500) == 19.86754938343438
    assert candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195],k = 25) == 4.999999703159119
    assert candidate(stations = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000],k = 1000) == 997782.7050995813
    assert candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39],k = 15) == 1.9999994549380062
    assert candidate(stations = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000],k = 100000) == 999.9777780933528
    assert candidate(stations = [1, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 5) == 99.99999974752427
    assert candidate(stations = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300],k = 250) == 1.111110492502121
    assert candidate(stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200],k = 100) == 1.7857139766874752
    assert candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500],k = 50) == 9.090909003361958
    assert candidate(stations = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],k = 10) == 4.999999703159119
    assert candidate(stations = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],k = 1000) == 0.990098669717554
    assert candidate(stations = [1, 10000000, 20000000, 30000000, 40000000, 50000000, 60000000, 70000000, 80000000, 90000000, 100000000],k = 1000000) == 99.99899930335232
    assert candidate(stations = [1, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 340, 360, 380],k = 200) == 1.8181815164552972
    assert candidate(stations = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],k = 10) == 0.9999993721976352
    assert candidate(stations = [5, 10, 20, 35, 55, 80, 110, 145, 185, 230, 280, 335, 400, 470, 550, 640, 740, 850, 970, 1100],k = 50) == 18.333332718611928


