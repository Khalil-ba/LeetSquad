def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(m = 4,n = 3,hFences = [2, 3],vFences = [2]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 4,n = 3,hFences = [2, 3],vFences = [2]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,hFences = [3, 7],vFences = [2, 8]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,hFences = [3, 7],vFences = [2, 8]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 12,hFences = [5, 10],vFences = [4, 8]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 12,hFences = [5, 10],vFences = [4, 8]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(m = 50,n = 50,hFences = [10, 20, 30],vFences = [10, 20, 30]) == 2401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 50,n = 50,hFences = [10, 20, 30],vFences = [10, 20, 30]) == 2401: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 15,hFences = [4, 12],vFences = [5, 10]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 15,hFences = [4, 12],vFences = [5, 10]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 10,hFences = [3, 7],vFences = [3, 7]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 10,hFences = [3, 7],vFences = [3, 7]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 5,hFences = [2, 6],vFences = [2]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 5,hFences = [2, 6],vFences = [2]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 15,hFences = [4, 6, 10],vFences = [4, 6, 10]) == 196
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 15,hFences = [4, 6, 10],vFences = [4, 6, 10]) == 196: {e}')
    
    total += 1
    try:
        result = candidate(m = 7,n = 8,hFences = [3],vFences = [3, 5]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 7,n = 8,hFences = [3],vFences = [3, 5]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(m = 9,n = 5,hFences = [2, 5, 8],vFences = [2, 3]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 9,n = 5,hFences = [2, 5, 8],vFences = [2, 3]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 100,hFences = [20, 40, 60, 80],vFences = [20, 40, 60, 80]) == 9801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 100,hFences = [20, 40, 60, 80],vFences = [20, 40, 60, 80]) == 9801: {e}')
    
    total += 1
    try:
        result = candidate(m = 12,n = 12,hFences = [3, 9],vFences = [3, 9]) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 12,n = 12,hFences = [3, 9],vFences = [3, 9]) == 121: {e}')
    
    total += 1
    try:
        result = candidate(m = 9,n = 9,hFences = [5],vFences = [5]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 9,n = 9,hFences = [5],vFences = [5]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(m = 15,n = 12,hFences = [5, 10],vFences = [3, 9]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 15,n = 12,hFences = [5, 10],vFences = [3, 9]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 5,hFences = [2, 5],vFences = [2, 3]) == 16
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 5,hFences = [2, 5],vFences = [2, 3]) == 16: {e}')
    
    total += 1
    try:
        result = candidate(m = 6,n = 7,hFences = [2],vFences = [4]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 6,n = 7,hFences = [2],vFences = [4]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(m = 1000000000,n = 1000000000,hFences = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000],vFences = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1000000000,n = 1000000000,hFences = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000],vFences = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 100,hFences = [20, 30, 40, 50],vFences = [15, 25, 35, 45]) == 9801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 100,hFences = [20, 30, 40, 50],vFences = [15, 25, 35, 45]) == 9801: {e}')
    
    total += 1
    try:
        result = candidate(m = 999999999,n = 999999999,hFences = [333333333, 666666666],vFences = [333333333, 666666666]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 999999999,n = 999999999,hFences = [333333333, 666666666],vFences = [333333333, 666666666]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(m = 1000,n = 1000,hFences = [250, 500, 750],vFences = [250, 500, 750]) == 998001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1000,n = 1000,hFences = [250, 500, 750],vFences = [250, 500, 750]) == 998001: {e}')
    
    total += 1
    try:
        result = candidate(m = 200,n = 200,hFences = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],vFences = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 39601
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 200,n = 200,hFences = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],vFences = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 39601: {e}')
    
    total += 1
    try:
        result = candidate(m = 500,n = 500,hFences = [50, 150, 250, 350, 450],vFences = [75, 125, 175, 225, 275, 325, 375, 425, 475]) == 249001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 500,n = 500,hFences = [50, 150, 250, 350, 450],vFences = [75, 125, 175, 225, 275, 325, 375, 425, 475]) == 249001: {e}')
    
    total += 1
    try:
        result = candidate(m = 8,n = 12,hFences = [2, 4, 6, 7],vFences = [3, 5, 9, 11]) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 8,n = 12,hFences = [2, 4, 6, 7],vFences = [3, 5, 9, 11]) == 49: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 100,hFences = [10, 20, 30, 40, 50],vFences = [15, 25, 35, 45, 55]) == 9801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 100,hFences = [10, 20, 30, 40, 50],vFences = [15, 25, 35, 45, 55]) == 9801: {e}')
    
    total += 1
    try:
        result = candidate(m = 800,n = 600,hFences = [100, 300, 500, 700],vFences = [120, 240, 360, 480]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 800,n = 600,hFences = [100, 300, 500, 700],vFences = [120, 240, 360, 480]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(m = 10000,n = 10000,hFences = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000],vFences = [500, 1500, 2500, 3500, 4500, 5500, 6500, 7500, 8500, 9500]) == 99980001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10000,n = 10000,hFences = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000],vFences = [500, 1500, 2500, 3500, 4500, 5500, 6500, 7500, 8500, 9500]) == 99980001: {e}')
    
    total += 1
    try:
        result = candidate(m = 1000000000,n = 1000000000,hFences = [100000, 200000, 300000],vFences = [150000, 250000, 350000]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1000000000,n = 1000000000,hFences = [100000, 200000, 300000],vFences = [150000, 250000, 350000]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(m = 1200,n = 800,hFences = [240, 480, 720, 960],vFences = [160, 320, 480, 640]) == 230400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1200,n = 800,hFences = [240, 480, 720, 960],vFences = [160, 320, 480, 640]) == 230400: {e}')
    
    total += 1
    try:
        result = candidate(m = 3000,n = 2000,hFences = [750, 1500, 2250],vFences = [500, 1000, 1500]) == 2250000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 3000,n = 2000,hFences = [750, 1500, 2250],vFences = [500, 1000, 1500]) == 2250000: {e}')
    
    total += 1
    try:
        result = candidate(m = 50,n = 30,hFences = [5, 10, 15, 20, 25, 30, 35, 40, 45],vFences = [3, 6, 9, 12, 15, 18, 21, 24, 27]) == 841
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 50,n = 30,hFences = [5, 10, 15, 20, 25, 30, 35, 40, 45],vFences = [3, 6, 9, 12, 15, 18, 21, 24, 27]) == 841: {e}')
    
    total += 1
    try:
        result = candidate(m = 999,n = 999,hFences = [100, 200, 300, 400, 500, 600, 700, 800, 900],vFences = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 996004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 999,n = 999,hFences = [100, 200, 300, 400, 500, 600, 700, 800, 900],vFences = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 996004: {e}')
    
    total += 1
    try:
        result = candidate(m = 1200,n = 900,hFences = [150, 300, 450, 600, 750, 900],vFences = [200, 400, 600, 800]) == 808201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1200,n = 900,hFences = [150, 300, 450, 600, 750, 900],vFences = [200, 400, 600, 800]) == 808201: {e}')
    
    total += 1
    try:
        result = candidate(m = 2000,n = 3000,hFences = [500, 1000, 1500],vFences = [750, 1500, 2250]) == 2250000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2000,n = 3000,hFences = [500, 1000, 1500],vFences = [750, 1500, 2250]) == 2250000: {e}')
    
    total += 1
    try:
        result = candidate(m = 1000,n = 1000,hFences = [150, 350, 550, 750, 950],vFences = [150, 350, 550, 750, 950]) == 998001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1000,n = 1000,hFences = [150, 350, 550, 750, 950],vFences = [150, 350, 550, 750, 950]) == 998001: {e}')
    
    total += 1
    try:
        result = candidate(m = 150,n = 150,hFences = [10, 20, 30, 40, 50],vFences = [15, 30, 45, 60, 75]) == 22201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 150,n = 150,hFences = [10, 20, 30, 40, 50],vFences = [15, 30, 45, 60, 75]) == 22201: {e}')
    
    total += 1
    try:
        result = candidate(m = 10,n = 20,hFences = [2, 3, 5, 7],vFences = [4, 8, 12, 16]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10,n = 20,hFences = [2, 3, 5, 7],vFences = [4, 8, 12, 16]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(m = 500,n = 300,hFences = [50, 150, 250, 350, 450],vFences = [100, 200, 250, 300]) == 62001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 500,n = 300,hFences = [50, 150, 250, 350, 450],vFences = [100, 200, 250, 300]) == 62001: {e}')
    
    total += 1
    try:
        result = candidate(m = 1000,n = 1000,hFences = [200, 300, 400, 500, 600, 700, 800, 900],vFences = [100, 200, 300, 400, 500, 600, 700, 800]) == 998001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1000,n = 1000,hFences = [200, 300, 400, 500, 600, 700, 800, 900],vFences = [100, 200, 300, 400, 500, 600, 700, 800]) == 998001: {e}')
    
    total += 1
    try:
        result = candidate(m = 600,n = 400,hFences = [100, 200, 300, 400, 500],vFences = [150, 250, 350]) == 159201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 600,n = 400,hFences = [100, 200, 300, 400, 500],vFences = [150, 250, 350]) == 159201: {e}')
    
    total += 1
    try:
        result = candidate(m = 1000000,n = 1000000,hFences = [100000, 200000, 300000, 400000, 500000],vFences = [100000, 200000, 300000, 400000, 500000]) == 997993008
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1000000,n = 1000000,hFences = [100000, 200000, 300000, 400000, 500000],vFences = [100000, 200000, 300000, 400000, 500000]) == 997993008: {e}')
    
    total += 1
    try:
        result = candidate(m = 30,n = 18,hFences = [3, 6, 9, 12, 15, 18, 24, 27],vFences = [4, 8, 12, 16, 20, 24, 28]) == 729
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 30,n = 18,hFences = [3, 6, 9, 12, 15, 18, 24, 27],vFences = [4, 8, 12, 16, 20, 24, 28]) == 729: {e}')
    
    total += 1
    try:
        result = candidate(m = 750,n = 1000,hFences = [10, 20, 30, 40, 50, 60, 70, 80, 90],vFences = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 7921
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 750,n = 1000,hFences = [10, 20, 30, 40, 50, 60, 70, 80, 90],vFences = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 7921: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 15,hFences = [3, 6, 12, 18],vFences = [4, 8, 14]) == 196
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 15,hFences = [3, 6, 12, 18],vFences = [4, 8, 14]) == 196: {e}')
    
    total += 1
    try:
        result = candidate(m = 600,n = 900,hFences = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600],vFences = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720]) == 358801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 600,n = 900,hFences = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600],vFences = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720]) == 358801: {e}')
    
    total += 1
    try:
        result = candidate(m = 2000000000,n = 1000000000,hFences = [500000000, 1500000000, 1000000000],vFences = [250000000, 750000000, 500000000]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2000000000,n = 1000000000,hFences = [500000000, 1500000000, 1000000000],vFences = [250000000, 750000000, 500000000]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(m = 5000,n = 5000,hFences = [1000, 2000, 3000, 4000],vFences = [1200, 2200, 3200, 4200]) == 24990001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 5000,n = 5000,hFences = [1000, 2000, 3000, 4000],vFences = [1200, 2200, 3200, 4200]) == 24990001: {e}')
    
    total += 1
    try:
        result = candidate(m = 10000,n = 10000,hFences = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000],vFences = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == 99980001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 10000,n = 10000,hFences = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000],vFences = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == 99980001: {e}')
    
    total += 1
    try:
        result = candidate(m = 999,n = 999,hFences = [100, 200, 300, 400, 500, 600, 700, 800],vFences = [100, 200, 300, 400, 500, 600, 700, 800]) == 996004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 999,n = 999,hFences = [100, 200, 300, 400, 500, 600, 700, 800],vFences = [100, 200, 300, 400, 500, 600, 700, 800]) == 996004: {e}')
    
    total += 1
    try:
        result = candidate(m = 800,n = 600,hFences = [50, 100, 150, 200, 250],vFences = [75, 125, 175, 225, 275]) == 40000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 800,n = 600,hFences = [50, 100, 150, 200, 250],vFences = [75, 125, 175, 225, 275]) == 40000: {e}')
    
    total += 1
    try:
        result = candidate(m = 200,n = 150,hFences = [50, 100, 150],vFences = [30, 60, 90, 120]) == 22201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 200,n = 150,hFences = [50, 100, 150],vFences = [30, 60, 90, 120]) == 22201: {e}')
    
    total += 1
    try:
        result = candidate(m = 1000,n = 1000,hFences = [200, 400, 600, 800],vFences = [250, 500, 750]) == 998001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1000,n = 1000,hFences = [200, 400, 600, 800],vFences = [250, 500, 750]) == 998001: {e}')
    
    total += 1
    try:
        result = candidate(m = 500,n = 300,hFences = [100, 200, 300, 400],vFences = [50, 150, 250, 290]) == 89401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 500,n = 300,hFences = [100, 200, 300, 400],vFences = [50, 150, 250, 290]) == 89401: {e}')
    
    total += 1
    try:
        result = candidate(m = 2000,n = 3000,hFences = [200, 600, 1000, 1400, 1800],vFences = [300, 900, 1500, 2100, 2700]) == 3240000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 2000,n = 3000,hFences = [200, 600, 1000, 1400, 1800],vFences = [300, 900, 1500, 2100, 2700]) == 3240000: {e}')
    
    total += 1
    try:
        result = candidate(m = 999,n = 999,hFences = [333, 666],vFences = [333, 666]) == 996004
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 999,n = 999,hFences = [333, 666],vFences = [333, 666]) == 996004: {e}')
    
    total += 1
    try:
        result = candidate(m = 123456789,n = 987654321,hFences = [12345678, 24691356, 37037034],vFences = [9876543, 19753086, 29629629]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 123456789,n = 987654321,hFences = [12345678, 24691356, 37037034],vFences = [9876543, 19753086, 29629629]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(m = 1000,n = 1000,hFences = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],vFences = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == 998001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1000,n = 1000,hFences = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],vFences = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == 998001: {e}')
    
    total += 1
    try:
        result = candidate(m = 500,n = 500,hFences = [100, 150, 200, 250, 300],vFences = [50, 100, 150, 200, 250]) == 249001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 500,n = 500,hFences = [100, 150, 200, 250, 300],vFences = [50, 100, 150, 200, 250]) == 249001: {e}')
    
    total += 1
    try:
        result = candidate(m = 800,n = 900,hFences = [50, 150, 250, 350, 450],vFences = [60, 160, 260, 360, 460]) == 160000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 800,n = 900,hFences = [50, 150, 250, 350, 450],vFences = [60, 160, 260, 360, 460]) == 160000: {e}')
    
    total += 1
    try:
        result = candidate(m = 700,n = 500,hFences = [70, 140, 210, 280, 350, 420, 490, 560, 630],vFences = [50, 100, 150, 200, 250, 300, 350, 400, 450]) == 122500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 700,n = 500,hFences = [70, 140, 210, 280, 350, 420, 490, 560, 630],vFences = [50, 100, 150, 200, 250, 300, 350, 400, 450]) == 122500: {e}')
    
    total += 1
    try:
        result = candidate(m = 1000000000,n = 1000000000,hFences = [200, 300, 400],vFences = [200, 300, 400]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1000000000,n = 1000000000,hFences = [200, 300, 400],vFences = [200, 300, 400]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(m = 500,n = 500,hFences = [100, 200, 300, 400],vFences = [100, 200, 300, 400]) == 249001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 500,n = 500,hFences = [100, 200, 300, 400],vFences = [100, 200, 300, 400]) == 249001: {e}')
    
    total += 1
    try:
        result = candidate(m = 1200,n = 900,hFences = [150, 300, 450, 600, 750, 900],vFences = [180, 360, 540, 720, 900]) == 808201
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1200,n = 900,hFences = [150, 300, 450, 600, 750, 900],vFences = [180, 360, 540, 720, 900]) == 808201: {e}')
    
    total += 1
    try:
        result = candidate(m = 500000000,n = 500000000,hFences = [250000000],vFences = [250000000]) == 250000022
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 500000000,n = 500000000,hFences = [250000000],vFences = [250000000]) == 250000022: {e}')
    
    total += 1
    try:
        result = candidate(m = 50,n = 30,hFences = [10, 20, 30, 40],vFences = [5, 15, 25, 35, 45]) == 1600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 50,n = 30,hFences = [10, 20, 30, 40],vFences = [5, 15, 25, 35, 45]) == 1600: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 100,hFences = [10, 30, 50, 70, 90],vFences = [10, 30, 50, 70, 90]) == 9801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 100,hFences = [10, 30, 50, 70, 90],vFences = [10, 30, 50, 70, 90]) == 9801: {e}')
    
    total += 1
    try:
        result = candidate(m = 123456789,n = 987654321,hFences = [12345678, 24691356, 37037034, 49382712, 61728390, 74074068, 86419746, 98765424],vFences = [9876543, 19753086, 29629629, 39506172, 49382715, 59259258, 69135801, 79012344, 88888887]) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 123456789,n = 987654321,hFences = [12345678, 24691356, 37037034, 49382712, 61728390, 74074068, 86419746, 98765424],vFences = [9876543, 19753086, 29629629, 39506172, 49382715, 59259258, 69135801, 79012344, 88888887]) == -1: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 100,hFences = [15, 25, 35, 45, 55, 65, 75, 85, 95],vFences = [15, 25, 35, 45, 55, 65, 75, 85, 95]) == 9801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 100,hFences = [15, 25, 35, 45, 55, 65, 75, 85, 95],vFences = [15, 25, 35, 45, 55, 65, 75, 85, 95]) == 9801: {e}')
    
    total += 1
    try:
        result = candidate(m = 1000000000,n = 2000000000,hFences = [250000000, 750000000, 500000000],vFences = [500000000, 1500000000, 1000000000]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1000000000,n = 2000000000,hFences = [250000000, 750000000, 500000000],vFences = [500000000, 1500000000, 1000000000]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 100,hFences = [10, 20, 30, 40, 50, 60, 70, 80, 90],vFences = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 9801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 100,hFences = [10, 20, 30, 40, 50, 60, 70, 80, 90],vFences = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 9801: {e}')
    
    total += 1
    try:
        result = candidate(m = 123456,n = 654321,hFences = [23456, 45678, 67890],vFences = [34567, 56789, 78901]) == 493817284
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 123456,n = 654321,hFences = [23456, 45678, 67890],vFences = [34567, 56789, 78901]) == 493817284: {e}')
    
    total += 1
    try:
        result = candidate(m = 800,n = 400,hFences = [100, 300, 500, 700],vFences = [100, 200, 300]) == 90000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 800,n = 400,hFences = [100, 300, 500, 700],vFences = [100, 200, 300]) == 90000: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 100,hFences = [20, 40, 60, 80],vFences = [20, 40, 60, 80]) == 9801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 100,hFences = [20, 40, 60, 80],vFences = [20, 40, 60, 80]) == 9801: {e}')
    
    total += 1
    try:
        result = candidate(m = 999999999,n = 999999999,hFences = [100000001, 200000001, 300000001, 400000001, 500000001],vFences = [100000002, 200000002, 300000002, 400000002, 500000002]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 999999999,n = 999999999,hFences = [100000001, 200000001, 300000001, 400000001, 500000001],vFences = [100000002, 200000002, 300000002, 400000002, 500000002]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(m = 1000000000,n = 1000000000,hFences = [500000000],vFences = [500000000]) == 64
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1000000000,n = 1000000000,hFences = [500000000],vFences = [500000000]) == 64: {e}')
    
    total += 1
    try:
        result = candidate(m = 1000,n = 1000,hFences = [200, 300, 400, 500, 600, 700, 800, 900],vFences = [150, 250, 350, 450, 550, 650, 750, 850]) == 998001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1000,n = 1000,hFences = [200, 300, 400, 500, 600, 700, 800, 900],vFences = [150, 250, 350, 450, 550, 650, 750, 850]) == 998001: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 200,hFences = [10, 20, 30, 40],vFences = [15, 25, 35, 45]) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 200,hFences = [10, 20, 30, 40],vFences = [15, 25, 35, 45]) == 900: {e}')
    
    total += 1
    try:
        result = candidate(m = 500,n = 500,hFences = [25, 50, 75, 100, 125, 150, 175, 200],vFences = [25, 50, 75, 100, 125, 150, 175, 200]) == 249001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 500,n = 500,hFences = [25, 50, 75, 100, 125, 150, 175, 200],vFences = [25, 50, 75, 100, 125, 150, 175, 200]) == 249001: {e}')
    
    total += 1
    try:
        result = candidate(m = 500,n = 600,hFences = [150, 250, 350],vFences = [200, 300, 400, 500]) == 249001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 500,n = 600,hFences = [150, 250, 350],vFences = [200, 300, 400, 500]) == 249001: {e}')
    
    total += 1
    try:
        result = candidate(m = 120,n = 120,hFences = [24, 48, 72, 96],vFences = [24, 48, 72, 96]) == 14161
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 120,n = 120,hFences = [24, 48, 72, 96],vFences = [24, 48, 72, 96]) == 14161: {e}')
    
    total += 1
    try:
        result = candidate(m = 80,n = 80,hFences = [20, 40, 60],vFences = [20, 40, 60]) == 6241
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 80,n = 80,hFences = [20, 40, 60],vFences = [20, 40, 60]) == 6241: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 20,hFences = [4, 8, 12, 16],vFences = [4, 8, 12, 16]) == 361
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 20,hFences = [4, 8, 12, 16],vFences = [4, 8, 12, 16]) == 361: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 20,hFences = [4, 8, 12, 16],vFences = [5, 10, 15]) == 361
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 20,hFences = [4, 8, 12, 16],vFences = [5, 10, 15]) == 361: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 100,hFences = [20, 40, 60, 80],vFences = [25, 50, 75]) == 9801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 100,hFences = [20, 40, 60, 80],vFences = [25, 50, 75]) == 9801: {e}')
    
    total += 1
    try:
        result = candidate(m = 50,n = 50,hFences = [25, 35, 45],vFences = [10, 20, 30, 40, 50]) == 2401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 50,n = 50,hFences = [25, 35, 45],vFences = [10, 20, 30, 40, 50]) == 2401: {e}')
    
    total += 1
    try:
        result = candidate(m = 897,n = 789,hFences = [123, 234, 345, 456, 567, 678, 789],vFences = [87, 174, 261, 348, 435, 522, 609]) == 620944
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 897,n = 789,hFences = [123, 234, 345, 456, 567, 678, 789],vFences = [87, 174, 261, 348, 435, 522, 609]) == 620944: {e}')
    
    total += 1
    try:
        result = candidate(m = 99,n = 99,hFences = [33, 66],vFences = [33, 66]) == 9604
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 99,n = 99,hFences = [33, 66],vFences = [33, 66]) == 9604: {e}')
    
    total += 1
    try:
        result = candidate(m = 500,n = 500,hFences = [100, 200, 300],vFences = [150, 250, 350]) == 249001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 500,n = 500,hFences = [100, 200, 300],vFences = [150, 250, 350]) == 249001: {e}')
    
    total += 1
    try:
        result = candidate(m = 100,n = 100,hFences = [20, 30, 40, 50, 60, 70, 80, 90],vFences = [15, 25, 35, 45, 55, 65, 75, 85, 95]) == 9801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 100,n = 100,hFences = [20, 30, 40, 50, 60, 70, 80, 90],vFences = [15, 25, 35, 45, 55, 65, 75, 85, 95]) == 9801: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 20,hFences = [3, 7, 13, 17],vFences = [4, 8, 12, 16]) == 361
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 20,hFences = [3, 7, 13, 17],vFences = [4, 8, 12, 16]) == 361: {e}')
    
    total += 1
    try:
        result = candidate(m = 777,n = 777,hFences = [259, 518],vFences = [259, 518]) == 602176
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 777,n = 777,hFences = [259, 518],vFences = [259, 518]) == 602176: {e}')
    
    total += 1
    try:
        result = candidate(m = 50,n = 50,hFences = [10, 20, 30, 40],vFences = [10, 20, 30, 40]) == 2401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 50,n = 50,hFences = [10, 20, 30, 40],vFences = [10, 20, 30, 40]) == 2401: {e}')
    
    total += 1
    try:
        result = candidate(m = 1024,n = 1024,hFences = [256, 512, 768],vFences = [256, 512, 768]) == 1046529
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1024,n = 1024,hFences = [256, 512, 768],vFences = [256, 512, 768]) == 1046529: {e}')
    
    total += 1
    try:
        result = candidate(m = 1000,n = 1000,hFences = [100, 200, 300, 400, 500, 600, 700, 800, 900],vFences = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == 998001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1000,n = 1000,hFences = [100, 200, 300, 400, 500, 600, 700, 800, 900],vFences = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == 998001: {e}')
    
    total += 1
    try:
        result = candidate(m = 1000000,n = 500000,hFences = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000],vFences = [50000, 150000, 250000, 350000, 450000, 550000, 650000, 750000, 850000, 950000]) == 999994337
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1000000,n = 500000,hFences = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000],vFences = [50000, 150000, 250000, 350000, 450000, 550000, 650000, 750000, 850000, 950000]) == 999994337: {e}')
    
    total += 1
    try:
        result = candidate(m = 1000,n = 1000,hFences = [100, 200, 300, 400, 500, 600, 700, 800, 900],vFences = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 998001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 1000,n = 1000,hFences = [100, 200, 300, 400, 500, 600, 700, 800, 900],vFences = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 998001: {e}')
    
    total += 1
    try:
        result = candidate(m = 500000000,n = 500000000,hFences = [50000000, 100000000, 150000000, 200000000, 250000000, 300000000, 350000000, 400000000, 450000000, 499999990],vFences = [50000000, 100000000, 150000000, 200000000, 250000000, 300000000, 350000000, 400000000, 450000000, 499999990]) == 250000022
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 500000000,n = 500000000,hFences = [50000000, 100000000, 150000000, 200000000, 250000000, 300000000, 350000000, 400000000, 450000000, 499999990],vFences = [50000000, 100000000, 150000000, 200000000, 250000000, 300000000, 350000000, 400000000, 450000000, 499999990]) == 250000022: {e}')
    
    total += 1
    try:
        result = candidate(m = 987654,n = 456789,hFences = [123456, 234567, 345678, 456789, 567890],vFences = [98765, 197530, 296295, 395060, 493825]) == 655275488
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 987654,n = 456789,hFences = [123456, 234567, 345678, 456789, 567890],vFences = [98765, 197530, 296295, 395060, 493825]) == 655275488: {e}')
    
    total += 1
    try:
        result = candidate(m = 800,n = 600,hFences = [100, 200, 300, 400, 500, 600, 700],vFences = [125, 250, 375, 500, 625]) == 358801
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 800,n = 600,hFences = [100, 200, 300, 400, 500, 600, 700],vFences = [125, 250, 375, 500, 625]) == 358801: {e}')
    
    total += 1
    try:
        result = candidate(m = 75,n = 60,hFences = [15, 30, 45],vFences = [10, 20, 30, 40]) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 75,n = 60,hFences = [15, 30, 45],vFences = [10, 20, 30, 40]) == 900: {e}')
    
    total += 1
    try:
        result = candidate(m = 20,n = 15,hFences = [3, 7, 12],vFences = [4, 8, 11]) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 20,n = 15,hFences = [3, 7, 12],vFences = [4, 8, 11]) == 121: {e}')
    
    total += 1
    try:
        result = candidate(m = 50,n = 40,hFences = [10, 20, 30, 40],vFences = [5, 15, 25, 35]) == 1521
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(m = 50,n = 40,hFences = [10, 20, 30, 40],vFences = [5, 15, 25, 35]) == 1521: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(m = 4,n = 3,hFences = [2, 3],vFences = [2]) == 4
    assert candidate(m = 10,n = 10,hFences = [3, 7],vFences = [2, 8]) == 81
    assert candidate(m = 15,n = 12,hFences = [5, 10],vFences = [4, 8]) == 16
    assert candidate(m = 50,n = 50,hFences = [10, 20, 30],vFences = [10, 20, 30]) == 2401
    assert candidate(m = 20,n = 15,hFences = [4, 12],vFences = [5, 10]) == -1
    assert candidate(m = 10,n = 10,hFences = [3, 7],vFences = [3, 7]) == 81
    assert candidate(m = 8,n = 5,hFences = [2, 6],vFences = [2]) == 16
    assert candidate(m = 15,n = 15,hFences = [4, 6, 10],vFences = [4, 6, 10]) == 196
    assert candidate(m = 7,n = 8,hFences = [3],vFences = [3, 5]) == 16
    assert candidate(m = 9,n = 5,hFences = [2, 5, 8],vFences = [2, 3]) == 16
    assert candidate(m = 100,n = 100,hFences = [20, 40, 60, 80],vFences = [20, 40, 60, 80]) == 9801
    assert candidate(m = 12,n = 12,hFences = [3, 9],vFences = [3, 9]) == 121
    assert candidate(m = 9,n = 9,hFences = [5],vFences = [5]) == 64
    assert candidate(m = 15,n = 12,hFences = [5, 10],vFences = [3, 9]) == 81
    assert candidate(m = 8,n = 5,hFences = [2, 5],vFences = [2, 3]) == 16
    assert candidate(m = 6,n = 7,hFences = [2],vFences = [4]) == -1
    assert candidate(m = 1000000000,n = 1000000000,hFences = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000],vFences = [100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000]) == 64
    assert candidate(m = 100,n = 100,hFences = [20, 30, 40, 50],vFences = [15, 25, 35, 45]) == 9801
    assert candidate(m = 999999999,n = 999999999,hFences = [333333333, 666666666],vFences = [333333333, 666666666]) == 81
    assert candidate(m = 1000,n = 1000,hFences = [250, 500, 750],vFences = [250, 500, 750]) == 998001
    assert candidate(m = 200,n = 200,hFences = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],vFences = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 39601
    assert candidate(m = 500,n = 500,hFences = [50, 150, 250, 350, 450],vFences = [75, 125, 175, 225, 275, 325, 375, 425, 475]) == 249001
    assert candidate(m = 8,n = 12,hFences = [2, 4, 6, 7],vFences = [3, 5, 9, 11]) == 49
    assert candidate(m = 100,n = 100,hFences = [10, 20, 30, 40, 50],vFences = [15, 25, 35, 45, 55]) == 9801
    assert candidate(m = 800,n = 600,hFences = [100, 300, 500, 700],vFences = [120, 240, 360, 480]) == -1
    assert candidate(m = 10000,n = 10000,hFences = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000],vFences = [500, 1500, 2500, 3500, 4500, 5500, 6500, 7500, 8500, 9500]) == 99980001
    assert candidate(m = 1000000000,n = 1000000000,hFences = [100000, 200000, 300000],vFences = [150000, 250000, 350000]) == 64
    assert candidate(m = 1200,n = 800,hFences = [240, 480, 720, 960],vFences = [160, 320, 480, 640]) == 230400
    assert candidate(m = 3000,n = 2000,hFences = [750, 1500, 2250],vFences = [500, 1000, 1500]) == 2250000
    assert candidate(m = 50,n = 30,hFences = [5, 10, 15, 20, 25, 30, 35, 40, 45],vFences = [3, 6, 9, 12, 15, 18, 21, 24, 27]) == 841
    assert candidate(m = 999,n = 999,hFences = [100, 200, 300, 400, 500, 600, 700, 800, 900],vFences = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 996004
    assert candidate(m = 1200,n = 900,hFences = [150, 300, 450, 600, 750, 900],vFences = [200, 400, 600, 800]) == 808201
    assert candidate(m = 2000,n = 3000,hFences = [500, 1000, 1500],vFences = [750, 1500, 2250]) == 2250000
    assert candidate(m = 1000,n = 1000,hFences = [150, 350, 550, 750, 950],vFences = [150, 350, 550, 750, 950]) == 998001
    assert candidate(m = 150,n = 150,hFences = [10, 20, 30, 40, 50],vFences = [15, 30, 45, 60, 75]) == 22201
    assert candidate(m = 10,n = 20,hFences = [2, 3, 5, 7],vFences = [4, 8, 12, 16]) == 64
    assert candidate(m = 500,n = 300,hFences = [50, 150, 250, 350, 450],vFences = [100, 200, 250, 300]) == 62001
    assert candidate(m = 1000,n = 1000,hFences = [200, 300, 400, 500, 600, 700, 800, 900],vFences = [100, 200, 300, 400, 500, 600, 700, 800]) == 998001
    assert candidate(m = 600,n = 400,hFences = [100, 200, 300, 400, 500],vFences = [150, 250, 350]) == 159201
    assert candidate(m = 1000000,n = 1000000,hFences = [100000, 200000, 300000, 400000, 500000],vFences = [100000, 200000, 300000, 400000, 500000]) == 997993008
    assert candidate(m = 30,n = 18,hFences = [3, 6, 9, 12, 15, 18, 24, 27],vFences = [4, 8, 12, 16, 20, 24, 28]) == 729
    assert candidate(m = 750,n = 1000,hFences = [10, 20, 30, 40, 50, 60, 70, 80, 90],vFences = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 7921
    assert candidate(m = 20,n = 15,hFences = [3, 6, 12, 18],vFences = [4, 8, 14]) == 196
    assert candidate(m = 600,n = 900,hFences = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600],vFences = [60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720]) == 358801
    assert candidate(m = 2000000000,n = 1000000000,hFences = [500000000, 1500000000, 1000000000],vFences = [250000000, 750000000, 500000000]) == 64
    assert candidate(m = 5000,n = 5000,hFences = [1000, 2000, 3000, 4000],vFences = [1200, 2200, 3200, 4200]) == 24990001
    assert candidate(m = 10000,n = 10000,hFences = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000],vFences = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == 99980001
    assert candidate(m = 999,n = 999,hFences = [100, 200, 300, 400, 500, 600, 700, 800],vFences = [100, 200, 300, 400, 500, 600, 700, 800]) == 996004
    assert candidate(m = 800,n = 600,hFences = [50, 100, 150, 200, 250],vFences = [75, 125, 175, 225, 275]) == 40000
    assert candidate(m = 200,n = 150,hFences = [50, 100, 150],vFences = [30, 60, 90, 120]) == 22201
    assert candidate(m = 1000,n = 1000,hFences = [200, 400, 600, 800],vFences = [250, 500, 750]) == 998001
    assert candidate(m = 500,n = 300,hFences = [100, 200, 300, 400],vFences = [50, 150, 250, 290]) == 89401
    assert candidate(m = 2000,n = 3000,hFences = [200, 600, 1000, 1400, 1800],vFences = [300, 900, 1500, 2100, 2700]) == 3240000
    assert candidate(m = 999,n = 999,hFences = [333, 666],vFences = [333, 666]) == 996004
    assert candidate(m = 123456789,n = 987654321,hFences = [12345678, 24691356, 37037034],vFences = [9876543, 19753086, 29629629]) == -1
    assert candidate(m = 1000,n = 1000,hFences = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950],vFences = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == 998001
    assert candidate(m = 500,n = 500,hFences = [100, 150, 200, 250, 300],vFences = [50, 100, 150, 200, 250]) == 249001
    assert candidate(m = 800,n = 900,hFences = [50, 150, 250, 350, 450],vFences = [60, 160, 260, 360, 460]) == 160000
    assert candidate(m = 700,n = 500,hFences = [70, 140, 210, 280, 350, 420, 490, 560, 630],vFences = [50, 100, 150, 200, 250, 300, 350, 400, 450]) == 122500
    assert candidate(m = 1000000000,n = 1000000000,hFences = [200, 300, 400],vFences = [200, 300, 400]) == 64
    assert candidate(m = 500,n = 500,hFences = [100, 200, 300, 400],vFences = [100, 200, 300, 400]) == 249001
    assert candidate(m = 1200,n = 900,hFences = [150, 300, 450, 600, 750, 900],vFences = [180, 360, 540, 720, 900]) == 808201
    assert candidate(m = 500000000,n = 500000000,hFences = [250000000],vFences = [250000000]) == 250000022
    assert candidate(m = 50,n = 30,hFences = [10, 20, 30, 40],vFences = [5, 15, 25, 35, 45]) == 1600
    assert candidate(m = 100,n = 100,hFences = [10, 30, 50, 70, 90],vFences = [10, 30, 50, 70, 90]) == 9801
    assert candidate(m = 123456789,n = 987654321,hFences = [12345678, 24691356, 37037034, 49382712, 61728390, 74074068, 86419746, 98765424],vFences = [9876543, 19753086, 29629629, 39506172, 49382715, 59259258, 69135801, 79012344, 88888887]) == -1
    assert candidate(m = 100,n = 100,hFences = [15, 25, 35, 45, 55, 65, 75, 85, 95],vFences = [15, 25, 35, 45, 55, 65, 75, 85, 95]) == 9801
    assert candidate(m = 1000000000,n = 2000000000,hFences = [250000000, 750000000, 500000000],vFences = [500000000, 1500000000, 1000000000]) == 64
    assert candidate(m = 100,n = 100,hFences = [10, 20, 30, 40, 50, 60, 70, 80, 90],vFences = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 9801
    assert candidate(m = 123456,n = 654321,hFences = [23456, 45678, 67890],vFences = [34567, 56789, 78901]) == 493817284
    assert candidate(m = 800,n = 400,hFences = [100, 300, 500, 700],vFences = [100, 200, 300]) == 90000
    assert candidate(m = 100,n = 100,hFences = [20, 40, 60, 80],vFences = [20, 40, 60, 80]) == 9801
    assert candidate(m = 999999999,n = 999999999,hFences = [100000001, 200000001, 300000001, 400000001, 500000001],vFences = [100000002, 200000002, 300000002, 400000002, 500000002]) == 81
    assert candidate(m = 1000000000,n = 1000000000,hFences = [500000000],vFences = [500000000]) == 64
    assert candidate(m = 1000,n = 1000,hFences = [200, 300, 400, 500, 600, 700, 800, 900],vFences = [150, 250, 350, 450, 550, 650, 750, 850]) == 998001
    assert candidate(m = 100,n = 200,hFences = [10, 20, 30, 40],vFences = [15, 25, 35, 45]) == 900
    assert candidate(m = 500,n = 500,hFences = [25, 50, 75, 100, 125, 150, 175, 200],vFences = [25, 50, 75, 100, 125, 150, 175, 200]) == 249001
    assert candidate(m = 500,n = 600,hFences = [150, 250, 350],vFences = [200, 300, 400, 500]) == 249001
    assert candidate(m = 120,n = 120,hFences = [24, 48, 72, 96],vFences = [24, 48, 72, 96]) == 14161
    assert candidate(m = 80,n = 80,hFences = [20, 40, 60],vFences = [20, 40, 60]) == 6241
    assert candidate(m = 20,n = 20,hFences = [4, 8, 12, 16],vFences = [4, 8, 12, 16]) == 361
    assert candidate(m = 20,n = 20,hFences = [4, 8, 12, 16],vFences = [5, 10, 15]) == 361
    assert candidate(m = 100,n = 100,hFences = [20, 40, 60, 80],vFences = [25, 50, 75]) == 9801
    assert candidate(m = 50,n = 50,hFences = [25, 35, 45],vFences = [10, 20, 30, 40, 50]) == 2401
    assert candidate(m = 897,n = 789,hFences = [123, 234, 345, 456, 567, 678, 789],vFences = [87, 174, 261, 348, 435, 522, 609]) == 620944
    assert candidate(m = 99,n = 99,hFences = [33, 66],vFences = [33, 66]) == 9604
    assert candidate(m = 500,n = 500,hFences = [100, 200, 300],vFences = [150, 250, 350]) == 249001
    assert candidate(m = 100,n = 100,hFences = [20, 30, 40, 50, 60, 70, 80, 90],vFences = [15, 25, 35, 45, 55, 65, 75, 85, 95]) == 9801
    assert candidate(m = 20,n = 20,hFences = [3, 7, 13, 17],vFences = [4, 8, 12, 16]) == 361
    assert candidate(m = 777,n = 777,hFences = [259, 518],vFences = [259, 518]) == 602176
    assert candidate(m = 50,n = 50,hFences = [10, 20, 30, 40],vFences = [10, 20, 30, 40]) == 2401
    assert candidate(m = 1024,n = 1024,hFences = [256, 512, 768],vFences = [256, 512, 768]) == 1046529
    assert candidate(m = 1000,n = 1000,hFences = [100, 200, 300, 400, 500, 600, 700, 800, 900],vFences = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == 998001
    assert candidate(m = 1000000,n = 500000,hFences = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000],vFences = [50000, 150000, 250000, 350000, 450000, 550000, 650000, 750000, 850000, 950000]) == 999994337
    assert candidate(m = 1000,n = 1000,hFences = [100, 200, 300, 400, 500, 600, 700, 800, 900],vFences = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 998001
    assert candidate(m = 500000000,n = 500000000,hFences = [50000000, 100000000, 150000000, 200000000, 250000000, 300000000, 350000000, 400000000, 450000000, 499999990],vFences = [50000000, 100000000, 150000000, 200000000, 250000000, 300000000, 350000000, 400000000, 450000000, 499999990]) == 250000022
    assert candidate(m = 987654,n = 456789,hFences = [123456, 234567, 345678, 456789, 567890],vFences = [98765, 197530, 296295, 395060, 493825]) == 655275488
    assert candidate(m = 800,n = 600,hFences = [100, 200, 300, 400, 500, 600, 700],vFences = [125, 250, 375, 500, 625]) == 358801
    assert candidate(m = 75,n = 60,hFences = [15, 30, 45],vFences = [10, 20, 30, 40]) == 900
    assert candidate(m = 20,n = 15,hFences = [3, 7, 12],vFences = [4, 8, 11]) == 121
    assert candidate(m = 50,n = 40,hFences = [10, 20, 30, 40],vFences = [5, 15, 25, 35]) == 1521


