def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(h = 10,w = 10,horizontalCuts = [2, 5, 7],verticalCuts = [2, 5, 7]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 10,w = 10,horizontalCuts = [2, 5, 7],verticalCuts = [2, 5, 7]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(h = 5,w = 4,horizontalCuts = [3, 1],verticalCuts = [1]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 5,w = 4,horizontalCuts = [3, 1],verticalCuts = [1]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(h = 5,w = 4,horizontalCuts = [1, 2, 4],verticalCuts = [1, 3]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 5,w = 4,horizontalCuts = [1, 2, 4],verticalCuts = [1, 3]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(h = 10,w = 10,horizontalCuts = [2, 5, 7],verticalCuts = [3, 6, 9]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 10,w = 10,horizontalCuts = [2, 5, 7],verticalCuts = [3, 6, 9]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(h = 10,w = 10,horizontalCuts = [2, 4, 6, 8],verticalCuts = [2, 4, 6, 8]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 10,w = 10,horizontalCuts = [2, 4, 6, 8],verticalCuts = [2, 4, 6, 8]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000000000,w = 1000000000,horizontalCuts = [1, 500000000],verticalCuts = [1, 500000000]) == 250000014
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000000000,w = 1000000000,horizontalCuts = [1, 500000000],verticalCuts = [1, 500000000]) == 250000014: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000000000,w = 1000000000,horizontalCuts = [1, 999999999],verticalCuts = [1, 999999999]) == 81
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000000000,w = 1000000000,horizontalCuts = [1, 999999999],verticalCuts = [1, 999999999]) == 81: {e}')
    
    total += 1
    try:
        result = candidate(h = 5,w = 4,horizontalCuts = [3],verticalCuts = [3]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 5,w = 4,horizontalCuts = [3],verticalCuts = [3]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(h = 7,w = 7,horizontalCuts = [1, 2, 3, 4, 5, 6],verticalCuts = [1, 2, 3, 4, 5, 6]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 7,w = 7,horizontalCuts = [1, 2, 3, 4, 5, 6],verticalCuts = [1, 2, 3, 4, 5, 6]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(h = 6,w = 4,horizontalCuts = [1, 2, 5],verticalCuts = [1, 3]) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 6,w = 4,horizontalCuts = [1, 2, 5],verticalCuts = [1, 3]) == 6: {e}')
    
    total += 1
    try:
        result = candidate(h = 10,w = 10,horizontalCuts = [2, 5, 7],verticalCuts = [3, 6, 8]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 10,w = 10,horizontalCuts = [2, 5, 7],verticalCuts = [3, 6, 8]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000000000,w = 1000000000,horizontalCuts = [500000000],verticalCuts = [500000000]) == 250000014
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000000000,w = 1000000000,horizontalCuts = [500000000],verticalCuts = [500000000]) == 250000014: {e}')
    
    total += 1
    try:
        result = candidate(h = 6,w = 6,horizontalCuts = [1, 2, 3, 4, 5],verticalCuts = [1, 2, 3, 4, 5]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 6,w = 6,horizontalCuts = [1, 2, 3, 4, 5],verticalCuts = [1, 2, 3, 4, 5]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(h = 600,w = 800,horizontalCuts = [100, 200, 300, 400, 500],verticalCuts = [120, 240, 360, 480, 600, 720]) == 12000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 600,w = 800,horizontalCuts = [100, 200, 300, 400, 500],verticalCuts = [120, 240, 360, 480, 600, 720]) == 12000: {e}')
    
    total += 1
    try:
        result = candidate(h = 100,w = 200,horizontalCuts = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],verticalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 100,w = 200,horizontalCuts = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],verticalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000000000,w = 1000000000,horizontalCuts = [1, 2, 999999998, 999999999],verticalCuts = [1, 2, 999999998, 999999999]) == 121
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000000000,w = 1000000000,horizontalCuts = [1, 2, 999999998, 999999999],verticalCuts = [1, 2, 999999998, 999999999]) == 121: {e}')
    
    total += 1
    try:
        result = candidate(h = 50000,w = 100000,horizontalCuts = [25000, 37500],verticalCuts = [50000]) == 249999993
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 50000,w = 100000,horizontalCuts = [25000, 37500],verticalCuts = [50000]) == 249999993: {e}')
    
    total += 1
    try:
        result = candidate(h = 200,w = 150,horizontalCuts = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190],verticalCuts = [15, 45, 75, 105, 135]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 200,w = 150,horizontalCuts = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190],verticalCuts = [15, 45, 75, 105, 135]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(h = 7,w = 13,horizontalCuts = [1, 3, 5],verticalCuts = [2, 4, 6, 8, 10, 12]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 7,w = 13,horizontalCuts = [1, 3, 5],verticalCuts = [2, 4, 6, 8, 10, 12]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(h = 100,w = 200,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 100,w = 200,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(h = 999999999,w = 999999999,horizontalCuts = [500000000, 250000000, 750000000, 100000000],verticalCuts = [500000000, 250000000, 750000000, 100000000]) == 562500007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 999999999,w = 999999999,horizontalCuts = [500000000, 250000000, 750000000, 100000000],verticalCuts = [500000000, 250000000, 750000000, 100000000]) == 562500007: {e}')
    
    total += 1
    try:
        result = candidate(h = 100,w = 50,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 100,w = 50,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(h = 500,w = 400,horizontalCuts = [100, 200, 300],verticalCuts = [80, 160, 240, 320]) == 16000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 500,w = 400,horizontalCuts = [100, 200, 300],verticalCuts = [80, 160, 240, 320]) == 16000: {e}')
    
    total += 1
    try:
        result = candidate(h = 100,w = 100,horizontalCuts = [10, 30, 50, 70, 90],verticalCuts = [20, 40, 60, 80]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 100,w = 100,horizontalCuts = [10, 30, 50, 70, 90],verticalCuts = [20, 40, 60, 80]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000000000,w = 1000000000,horizontalCuts = [100, 200, 300, 400, 500],verticalCuts = [150, 250, 350, 450, 550]) == 282399
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000000000,w = 1000000000,horizontalCuts = [100, 200, 300, 400, 500],verticalCuts = [150, 250, 350, 450, 550]) == 282399: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000,w = 1000,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 828100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000,w = 1000,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 828100: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000,w = 1000,horizontalCuts = [250, 500, 750],verticalCuts = [250, 500, 750]) == 62500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000,w = 1000,horizontalCuts = [250, 500, 750],verticalCuts = [250, 500, 750]) == 62500: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000,w = 1000,horizontalCuts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95],verticalCuts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]) == 819025
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000,w = 1000,horizontalCuts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95],verticalCuts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]) == 819025: {e}')
    
    total += 1
    try:
        result = candidate(h = 8,w = 12,horizontalCuts = [2, 3, 5, 7],verticalCuts = [2, 4, 6, 8, 10]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 8,w = 12,horizontalCuts = [2, 3, 5, 7],verticalCuts = [2, 4, 6, 8, 10]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(h = 8,w = 8,horizontalCuts = [2, 4, 6],verticalCuts = [2, 4, 6]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 8,w = 8,horizontalCuts = [2, 4, 6],verticalCuts = [2, 4, 6]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000,w = 1000,horizontalCuts = [1, 2, 3, 997, 998, 999],verticalCuts = [1, 2, 3, 997, 998, 999]) == 988036
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000,w = 1000,horizontalCuts = [1, 2, 3, 997, 998, 999],verticalCuts = [1, 2, 3, 997, 998, 999]) == 988036: {e}')
    
    total += 1
    try:
        result = candidate(h = 500,w = 500,horizontalCuts = [25, 125, 225, 325, 425],verticalCuts = [25, 125, 225, 325, 425]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 500,w = 500,horizontalCuts = [25, 125, 225, 325, 425],verticalCuts = [25, 125, 225, 325, 425]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(h = 50,w = 60,horizontalCuts = [10, 20, 30, 40],verticalCuts = [12, 24, 36, 48]) == 120
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 50,w = 60,horizontalCuts = [10, 20, 30, 40],verticalCuts = [12, 24, 36, 48]) == 120: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000,w = 500,horizontalCuts = [200, 400, 600, 800],verticalCuts = [100, 200, 300, 400]) == 20000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000,w = 500,horizontalCuts = [200, 400, 600, 800],verticalCuts = [100, 200, 300, 400]) == 20000: {e}')
    
    total += 1
    try:
        result = candidate(h = 50000,w = 30000,horizontalCuts = [10000, 20000, 30000, 40000],verticalCuts = [5000, 10000, 15000, 25000, 28000]) == 100000000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 50000,w = 30000,horizontalCuts = [10000, 20000, 30000, 40000],verticalCuts = [5000, 10000, 15000, 25000, 28000]) == 100000000: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000000,w = 1000000,horizontalCuts = [1, 999999],verticalCuts = [1, 999999]) == 995993011
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000000,w = 1000000,horizontalCuts = [1, 999999],verticalCuts = [1, 999999]) == 995993011: {e}')
    
    total += 1
    try:
        result = candidate(h = 200,w = 300,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],verticalCuts = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 200,w = 300,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],verticalCuts = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(h = 100,w = 100,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 100,w = 100,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(h = 500,w = 300,horizontalCuts = [50, 100, 150, 200, 250, 450],verticalCuts = [30, 60, 90, 120, 150, 180, 210, 240, 270]) == 6000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 500,w = 300,horizontalCuts = [50, 100, 150, 200, 250, 450],verticalCuts = [30, 60, 90, 120, 150, 180, 210, 240, 270]) == 6000: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000,w = 1000,horizontalCuts = [100, 200, 300, 400, 500, 600, 700, 800, 900],verticalCuts = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000,w = 1000,horizontalCuts = [100, 200, 300, 400, 500, 600, 700, 800, 900],verticalCuts = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(h = 50,w = 50,horizontalCuts = [25],verticalCuts = [25]) == 625
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 50,w = 50,horizontalCuts = [25],verticalCuts = [25]) == 625: {e}')
    
    total += 1
    try:
        result = candidate(h = 30,w = 40,horizontalCuts = [5, 15, 25],verticalCuts = [8, 16, 24, 32]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 30,w = 40,horizontalCuts = [5, 15, 25],verticalCuts = [8, 16, 24, 32]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(h = 100,w = 150,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [15, 30, 45, 60, 75, 90, 120, 135]) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 100,w = 150,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [15, 30, 45, 60, 75, 90, 120, 135]) == 300: {e}')
    
    total += 1
    try:
        result = candidate(h = 150,w = 200,horizontalCuts = [25, 50, 75, 100, 125],verticalCuts = [30, 60, 90, 120, 150, 180]) == 750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 150,w = 200,horizontalCuts = [25, 50, 75, 100, 125],verticalCuts = [30, 60, 90, 120, 150, 180]) == 750: {e}')
    
    total += 1
    try:
        result = candidate(h = 100000,w = 50000,horizontalCuts = [50000],verticalCuts = [25000, 37500]) == 249999993
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 100000,w = 50000,horizontalCuts = [50000],verticalCuts = [25000, 37500]) == 249999993: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000,w = 1000,horizontalCuts = [100, 200, 300, 400, 500, 600, 700, 800, 900],verticalCuts = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000,w = 1000,horizontalCuts = [100, 200, 300, 400, 500, 600, 700, 800, 900],verticalCuts = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000,w = 500,horizontalCuts = [10, 20, 30, 40, 50],verticalCuts = [25, 50, 75, 100, 125]) == 356250
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000,w = 500,horizontalCuts = [10, 20, 30, 40, 50],verticalCuts = [25, 50, 75, 100, 125]) == 356250: {e}')
    
    total += 1
    try:
        result = candidate(h = 2000,w = 3000,horizontalCuts = [500, 1000, 1500],verticalCuts = [750, 1500, 2250]) == 375000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 2000,w = 3000,horizontalCuts = [500, 1000, 1500],verticalCuts = [750, 1500, 2250]) == 375000: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000000,w = 1000000,horizontalCuts = [500000],verticalCuts = [500000]) == 999998257
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000000,w = 1000000,horizontalCuts = [500000],verticalCuts = [500000]) == 999998257: {e}')
    
    total += 1
    try:
        result = candidate(h = 40,w = 50,horizontalCuts = [8, 16, 24, 32, 40],verticalCuts = [10, 20, 30, 40, 50]) == 80
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 40,w = 50,horizontalCuts = [8, 16, 24, 32, 40],verticalCuts = [10, 20, 30, 40, 50]) == 80: {e}')
    
    total += 1
    try:
        result = candidate(h = 15,w = 20,horizontalCuts = [1, 3, 5, 7, 9, 11, 13],verticalCuts = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 15,w = 20,horizontalCuts = [1, 3, 5, 7, 9, 11, 13],verticalCuts = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(h = 10,w = 10,horizontalCuts = [1, 2, 3, 4, 5, 6, 7, 8, 9],verticalCuts = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 10,w = 10,horizontalCuts = [1, 2, 3, 4, 5, 6, 7, 8, 9],verticalCuts = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(h = 100,w = 100,horizontalCuts = [1, 99],verticalCuts = [1, 99]) == 9604
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 100,w = 100,horizontalCuts = [1, 99],verticalCuts = [1, 99]) == 9604: {e}')
    
    total += 1
    try:
        result = candidate(h = 500000000,w = 300000000,horizontalCuts = [100000000, 200000000, 300000000, 400000000],verticalCuts = [50000000, 150000000, 250000000]) == 930000007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 500000000,w = 300000000,horizontalCuts = [100000000, 200000000, 300000000, 400000000],verticalCuts = [50000000, 150000000, 250000000]) == 930000007: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000,w = 2000,horizontalCuts = [250, 500, 750],verticalCuts = [500, 1000, 1500]) == 125000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000,w = 2000,horizontalCuts = [250, 500, 750],verticalCuts = [500, 1000, 1500]) == 125000: {e}')
    
    total += 1
    try:
        result = candidate(h = 100,w = 200,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [20, 40, 60, 80, 100, 120, 140, 160, 180]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 100,w = 200,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [20, 40, 60, 80, 100, 120, 140, 160, 180]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(h = 800,w = 600,horizontalCuts = [50, 100, 200, 300, 400, 500, 600, 700],verticalCuts = [50, 100, 200, 300, 400, 500, 600]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 800,w = 600,horizontalCuts = [50, 100, 200, 300, 400, 500, 600, 700],verticalCuts = [50, 100, 200, 300, 400, 500, 600]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(h = 10,w = 10,horizontalCuts = [1, 2, 3, 4, 5, 6, 7, 8, 9],verticalCuts = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 10,w = 10,horizontalCuts = [1, 2, 3, 4, 5, 6, 7, 8, 9],verticalCuts = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(h = 100000,w = 100000,horizontalCuts = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],verticalCuts = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 99999944
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 100000,w = 100000,horizontalCuts = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],verticalCuts = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 99999944: {e}')
    
    total += 1
    try:
        result = candidate(h = 20,w = 30,horizontalCuts = [3, 6, 9, 12, 15, 18],verticalCuts = [4, 8, 12, 16, 24, 28]) == 24
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 20,w = 30,horizontalCuts = [3, 6, 9, 12, 15, 18],verticalCuts = [4, 8, 12, 16, 24, 28]) == 24: {e}')
    
    total += 1
    try:
        result = candidate(h = 800,w = 600,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],verticalCuts = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 315000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 800,w = 600,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],verticalCuts = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 315000: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000000000,w = 1000000000,horizontalCuts = [1, 500000000, 999999999],verticalCuts = [1, 500000000, 999999999]) == 250000022
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000000000,w = 1000000000,horizontalCuts = [1, 500000000, 999999999],verticalCuts = [1, 500000000, 999999999]) == 250000022: {e}')
    
    total += 1
    try:
        result = candidate(h = 999999999,w = 999999999,horizontalCuts = [1, 2, 3, 4, 5],verticalCuts = [1, 2, 3, 4, 5]) == 169
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 999999999,w = 999999999,horizontalCuts = [1, 2, 3, 4, 5],verticalCuts = [1, 2, 3, 4, 5]) == 169: {e}')
    
    total += 1
    try:
        result = candidate(h = 800,w = 600,horizontalCuts = [50, 150, 250, 350, 450, 550, 650, 750],verticalCuts = [30, 130, 230, 330, 430, 530, 590]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 800,w = 600,horizontalCuts = [50, 150, 250, 350, 450, 550, 650, 750],verticalCuts = [30, 130, 230, 330, 430, 530, 590]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(h = 200,w = 100,horizontalCuts = [20, 180],verticalCuts = [10, 90]) == 12800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 200,w = 100,horizontalCuts = [20, 180],verticalCuts = [10, 90]) == 12800: {e}')
    
    total += 1
    try:
        result = candidate(h = 150,w = 200,horizontalCuts = [10, 30, 50, 70, 90, 110, 130, 140],verticalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 150,w = 200,horizontalCuts = [10, 30, 50, 70, 90, 110, 130, 140],verticalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 200: {e}')
    
    total += 1
    try:
        result = candidate(h = 999,w = 999,horizontalCuts = [1, 998],verticalCuts = [1, 998]) == 994009
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 999,w = 999,horizontalCuts = [1, 998],verticalCuts = [1, 998]) == 994009: {e}')
    
    total += 1
    try:
        result = candidate(h = 200,w = 200,horizontalCuts = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190],verticalCuts = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 200,w = 200,horizontalCuts = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190],verticalCuts = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000000,w = 1000000,horizontalCuts = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000],verticalCuts = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000]) == 999999937
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000000,w = 1000000,horizontalCuts = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000],verticalCuts = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000]) == 999999937: {e}')
    
    total += 1
    try:
        result = candidate(h = 999999999,w = 999999999,horizontalCuts = [500000000],verticalCuts = [500000000]) == 250000014
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 999999999,w = 999999999,horizontalCuts = [500000000],verticalCuts = [500000000]) == 250000014: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000000000,w = 1000000000,horizontalCuts = [1, 2, 3, 4, 5],verticalCuts = [1, 2, 3, 4, 5]) == 144
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000000000,w = 1000000000,horizontalCuts = [1, 2, 3, 4, 5],verticalCuts = [1, 2, 3, 4, 5]) == 144: {e}')
    
    total += 1
    try:
        result = candidate(h = 999999,w = 999999,horizontalCuts = [1, 999998],verticalCuts = [1, 999998]) == 993993016
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 999999,w = 999999,horizontalCuts = [1, 999998],verticalCuts = [1, 999998]) == 993993016: {e}')
    
    total += 1
    try:
        result = candidate(h = 500,w = 600,horizontalCuts = [100, 200, 300, 400],verticalCuts = [150, 250, 350, 450, 550]) == 15000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 500,w = 600,horizontalCuts = [100, 200, 300, 400],verticalCuts = [150, 250, 350, 450, 550]) == 15000: {e}')
    
    total += 1
    try:
        result = candidate(h = 500000000,w = 500000000,horizontalCuts = [125000000, 250000000, 375000000, 500000000],verticalCuts = [125000000, 250000000, 375000000, 500000000]) == 890625007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 500000000,w = 500000000,horizontalCuts = [125000000, 250000000, 375000000, 500000000],verticalCuts = [125000000, 250000000, 375000000, 500000000]) == 890625007: {e}')
    
    total += 1
    try:
        result = candidate(h = 10000,w = 10000,horizontalCuts = [2500, 5000, 7500],verticalCuts = [2500, 5000, 7500]) == 6250000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 10000,w = 10000,horizontalCuts = [2500, 5000, 7500],verticalCuts = [2500, 5000, 7500]) == 6250000: {e}')
    
    total += 1
    try:
        result = candidate(h = 30,w = 20,horizontalCuts = [2, 5, 8, 12, 16, 25],verticalCuts = [2, 4, 6, 10, 14]) == 54
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 30,w = 20,horizontalCuts = [2, 5, 8, 12, 16, 25],verticalCuts = [2, 4, 6, 10, 14]) == 54: {e}')
    
    total += 1
    try:
        result = candidate(h = 800,w = 600,horizontalCuts = [100, 300, 500, 700],verticalCuts = [150, 300, 450, 600]) == 30000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 800,w = 600,horizontalCuts = [100, 300, 500, 700],verticalCuts = [150, 300, 450, 600]) == 30000: {e}')
    
    total += 1
    try:
        result = candidate(h = 100,w = 200,horizontalCuts = [10, 90],verticalCuts = [20, 180]) == 12800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 100,w = 200,horizontalCuts = [10, 90],verticalCuts = [20, 180]) == 12800: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000,w = 1500,horizontalCuts = [100, 200, 300, 400, 500, 600, 700, 800, 900],verticalCuts = [150, 300, 450, 600, 750, 900, 1200, 1350]) == 30000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000,w = 1500,horizontalCuts = [100, 200, 300, 400, 500, 600, 700, 800, 900],verticalCuts = [150, 300, 450, 600, 750, 900, 1200, 1350]) == 30000: {e}')
    
    total += 1
    try:
        result = candidate(h = 700,w = 500,horizontalCuts = [50, 100, 200, 300, 400, 500, 600, 650, 700],verticalCuts = [50, 100, 200, 300, 400, 500]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 700,w = 500,horizontalCuts = [50, 100, 200, 300, 400, 500, 600, 650, 700],verticalCuts = [50, 100, 200, 300, 400, 500]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(h = 25,w = 30,horizontalCuts = [5, 10, 15, 20],verticalCuts = [5, 10, 15, 20, 25]) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 25,w = 30,horizontalCuts = [5, 10, 15, 20],verticalCuts = [5, 10, 15, 20, 25]) == 25: {e}')
    
    total += 1
    try:
        result = candidate(h = 50,w = 50,horizontalCuts = [1, 5, 10, 25, 49],verticalCuts = [2, 10, 20, 30, 45]) == 360
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 50,w = 50,horizontalCuts = [1, 5, 10, 25, 49],verticalCuts = [2, 10, 20, 30, 45]) == 360: {e}')
    
    total += 1
    try:
        result = candidate(h = 1000,w = 1000,horizontalCuts = [10, 100, 200, 300, 400, 500, 600, 700, 800, 900],verticalCuts = [10, 100, 200, 300, 400, 500, 600, 700, 800, 900]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 1000,w = 1000,horizontalCuts = [10, 100, 200, 300, 400, 500, 600, 700, 800, 900],verticalCuts = [10, 100, 200, 300, 400, 500, 600, 700, 800, 900]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(h = 20,w = 15,horizontalCuts = [1, 5, 10, 15],verticalCuts = [2, 6, 10, 14]) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 20,w = 15,horizontalCuts = [1, 5, 10, 15],verticalCuts = [2, 6, 10, 14]) == 20: {e}')
    
    total += 1
    try:
        result = candidate(h = 60,w = 70,horizontalCuts = [10, 20, 30, 40, 50],verticalCuts = [14, 28, 42, 56, 70]) == 140
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 60,w = 70,horizontalCuts = [10, 20, 30, 40, 50],verticalCuts = [14, 28, 42, 56, 70]) == 140: {e}')
    
    total += 1
    try:
        result = candidate(h = 500,w = 500,horizontalCuts = [100, 150, 200, 250, 300, 350, 400, 450],verticalCuts = [100, 150, 200, 250, 300, 350, 400, 450]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 500,w = 500,horizontalCuts = [100, 150, 200, 250, 300, 350, 400, 450],verticalCuts = [100, 150, 200, 250, 300, 350, 400, 450]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(h = 100,w = 100,horizontalCuts = [1, 50, 99],verticalCuts = [1, 50, 99]) == 2401
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 100,w = 100,horizontalCuts = [1, 50, 99],verticalCuts = [1, 50, 99]) == 2401: {e}')
    
    total += 1
    try:
        result = candidate(h = 50,w = 200,horizontalCuts = [5, 15, 25, 35, 45],verticalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 50,w = 200,horizontalCuts = [5, 15, 25, 35, 45],verticalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(h = 100,w = 100,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 100,w = 100,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(h = 70,w = 80,horizontalCuts = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],verticalCuts = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]) == 56
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 70,w = 80,horizontalCuts = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],verticalCuts = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]) == 56: {e}')
    
    total += 1
    try:
        result = candidate(h = 300,w = 300,horizontalCuts = [50, 100, 150, 200, 250],verticalCuts = [50, 100, 150, 200, 250]) == 2500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 300,w = 300,horizontalCuts = [50, 100, 150, 200, 250],verticalCuts = [50, 100, 150, 200, 250]) == 2500: {e}')
    
    total += 1
    try:
        result = candidate(h = 100,w = 100,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(h = 100,w = 100,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 100: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(h = 10,w = 10,horizontalCuts = [2, 5, 7],verticalCuts = [2, 5, 7]) == 9
    assert candidate(h = 5,w = 4,horizontalCuts = [3, 1],verticalCuts = [1]) == 6
    assert candidate(h = 5,w = 4,horizontalCuts = [1, 2, 4],verticalCuts = [1, 3]) == 4
    assert candidate(h = 10,w = 10,horizontalCuts = [2, 5, 7],verticalCuts = [3, 6, 9]) == 9
    assert candidate(h = 10,w = 10,horizontalCuts = [2, 4, 6, 8],verticalCuts = [2, 4, 6, 8]) == 4
    assert candidate(h = 1000000000,w = 1000000000,horizontalCuts = [1, 500000000],verticalCuts = [1, 500000000]) == 250000014
    assert candidate(h = 1000000000,w = 1000000000,horizontalCuts = [1, 999999999],verticalCuts = [1, 999999999]) == 81
    assert candidate(h = 5,w = 4,horizontalCuts = [3],verticalCuts = [3]) == 9
    assert candidate(h = 7,w = 7,horizontalCuts = [1, 2, 3, 4, 5, 6],verticalCuts = [1, 2, 3, 4, 5, 6]) == 1
    assert candidate(h = 6,w = 4,horizontalCuts = [1, 2, 5],verticalCuts = [1, 3]) == 6
    assert candidate(h = 10,w = 10,horizontalCuts = [2, 5, 7],verticalCuts = [3, 6, 8]) == 9
    assert candidate(h = 1000000000,w = 1000000000,horizontalCuts = [500000000],verticalCuts = [500000000]) == 250000014
    assert candidate(h = 6,w = 6,horizontalCuts = [1, 2, 3, 4, 5],verticalCuts = [1, 2, 3, 4, 5]) == 1
    assert candidate(h = 600,w = 800,horizontalCuts = [100, 200, 300, 400, 500],verticalCuts = [120, 240, 360, 480, 600, 720]) == 12000
    assert candidate(h = 100,w = 200,horizontalCuts = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],verticalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 100
    assert candidate(h = 1000000000,w = 1000000000,horizontalCuts = [1, 2, 999999998, 999999999],verticalCuts = [1, 2, 999999998, 999999999]) == 121
    assert candidate(h = 50000,w = 100000,horizontalCuts = [25000, 37500],verticalCuts = [50000]) == 249999993
    assert candidate(h = 200,w = 150,horizontalCuts = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190],verticalCuts = [15, 45, 75, 105, 135]) == 600
    assert candidate(h = 7,w = 13,horizontalCuts = [1, 3, 5],verticalCuts = [2, 4, 6, 8, 10, 12]) == 4
    assert candidate(h = 100,w = 200,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 100
    assert candidate(h = 999999999,w = 999999999,horizontalCuts = [500000000, 250000000, 750000000, 100000000],verticalCuts = [500000000, 250000000, 750000000, 100000000]) == 562500007
    assert candidate(h = 100,w = 50,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [5, 10, 15, 20, 25, 30, 35, 40, 45]) == 50
    assert candidate(h = 500,w = 400,horizontalCuts = [100, 200, 300],verticalCuts = [80, 160, 240, 320]) == 16000
    assert candidate(h = 100,w = 100,horizontalCuts = [10, 30, 50, 70, 90],verticalCuts = [20, 40, 60, 80]) == 400
    assert candidate(h = 1000000000,w = 1000000000,horizontalCuts = [100, 200, 300, 400, 500],verticalCuts = [150, 250, 350, 450, 550]) == 282399
    assert candidate(h = 1000,w = 1000,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 828100
    assert candidate(h = 1000,w = 1000,horizontalCuts = [250, 500, 750],verticalCuts = [250, 500, 750]) == 62500
    assert candidate(h = 1000,w = 1000,horizontalCuts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95],verticalCuts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]) == 819025
    assert candidate(h = 8,w = 12,horizontalCuts = [2, 3, 5, 7],verticalCuts = [2, 4, 6, 8, 10]) == 4
    assert candidate(h = 8,w = 8,horizontalCuts = [2, 4, 6],verticalCuts = [2, 4, 6]) == 4
    assert candidate(h = 1000,w = 1000,horizontalCuts = [1, 2, 3, 997, 998, 999],verticalCuts = [1, 2, 3, 997, 998, 999]) == 988036
    assert candidate(h = 500,w = 500,horizontalCuts = [25, 125, 225, 325, 425],verticalCuts = [25, 125, 225, 325, 425]) == 10000
    assert candidate(h = 50,w = 60,horizontalCuts = [10, 20, 30, 40],verticalCuts = [12, 24, 36, 48]) == 120
    assert candidate(h = 1000,w = 500,horizontalCuts = [200, 400, 600, 800],verticalCuts = [100, 200, 300, 400]) == 20000
    assert candidate(h = 50000,w = 30000,horizontalCuts = [10000, 20000, 30000, 40000],verticalCuts = [5000, 10000, 15000, 25000, 28000]) == 100000000
    assert candidate(h = 1000000,w = 1000000,horizontalCuts = [1, 999999],verticalCuts = [1, 999999]) == 995993011
    assert candidate(h = 200,w = 300,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],verticalCuts = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285]) == 150
    assert candidate(h = 100,w = 100,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 100
    assert candidate(h = 500,w = 300,horizontalCuts = [50, 100, 150, 200, 250, 450],verticalCuts = [30, 60, 90, 120, 150, 180, 210, 240, 270]) == 6000
    assert candidate(h = 1000,w = 1000,horizontalCuts = [100, 200, 300, 400, 500, 600, 700, 800, 900],verticalCuts = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == 10000
    assert candidate(h = 50,w = 50,horizontalCuts = [25],verticalCuts = [25]) == 625
    assert candidate(h = 30,w = 40,horizontalCuts = [5, 15, 25],verticalCuts = [8, 16, 24, 32]) == 80
    assert candidate(h = 100,w = 150,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [15, 30, 45, 60, 75, 90, 120, 135]) == 300
    assert candidate(h = 150,w = 200,horizontalCuts = [25, 50, 75, 100, 125],verticalCuts = [30, 60, 90, 120, 150, 180]) == 750
    assert candidate(h = 100000,w = 50000,horizontalCuts = [50000],verticalCuts = [25000, 37500]) == 249999993
    assert candidate(h = 1000,w = 1000,horizontalCuts = [100, 200, 300, 400, 500, 600, 700, 800, 900],verticalCuts = [100, 200, 300, 400, 500, 600, 700, 800, 900]) == 10000
    assert candidate(h = 1000,w = 500,horizontalCuts = [10, 20, 30, 40, 50],verticalCuts = [25, 50, 75, 100, 125]) == 356250
    assert candidate(h = 2000,w = 3000,horizontalCuts = [500, 1000, 1500],verticalCuts = [750, 1500, 2250]) == 375000
    assert candidate(h = 1000000,w = 1000000,horizontalCuts = [500000],verticalCuts = [500000]) == 999998257
    assert candidate(h = 40,w = 50,horizontalCuts = [8, 16, 24, 32, 40],verticalCuts = [10, 20, 30, 40, 50]) == 80
    assert candidate(h = 15,w = 20,horizontalCuts = [1, 3, 5, 7, 9, 11, 13],verticalCuts = [2, 4, 6, 8, 10, 12, 14, 16, 18]) == 4
    assert candidate(h = 10,w = 10,horizontalCuts = [1, 2, 3, 4, 5, 6, 7, 8, 9],verticalCuts = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
    assert candidate(h = 100,w = 100,horizontalCuts = [1, 99],verticalCuts = [1, 99]) == 9604
    assert candidate(h = 500000000,w = 300000000,horizontalCuts = [100000000, 200000000, 300000000, 400000000],verticalCuts = [50000000, 150000000, 250000000]) == 930000007
    assert candidate(h = 1000,w = 2000,horizontalCuts = [250, 500, 750],verticalCuts = [500, 1000, 1500]) == 125000
    assert candidate(h = 100,w = 200,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [20, 40, 60, 80, 100, 120, 140, 160, 180]) == 200
    assert candidate(h = 800,w = 600,horizontalCuts = [50, 100, 200, 300, 400, 500, 600, 700],verticalCuts = [50, 100, 200, 300, 400, 500, 600]) == 10000
    assert candidate(h = 10,w = 10,horizontalCuts = [1, 2, 3, 4, 5, 6, 7, 8, 9],verticalCuts = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
    assert candidate(h = 100000,w = 100000,horizontalCuts = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],verticalCuts = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]) == 99999944
    assert candidate(h = 20,w = 30,horizontalCuts = [3, 6, 9, 12, 15, 18],verticalCuts = [4, 8, 12, 16, 24, 28]) == 24
    assert candidate(h = 800,w = 600,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],verticalCuts = [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]) == 315000
    assert candidate(h = 1000000000,w = 1000000000,horizontalCuts = [1, 500000000, 999999999],verticalCuts = [1, 500000000, 999999999]) == 250000022
    assert candidate(h = 999999999,w = 999999999,horizontalCuts = [1, 2, 3, 4, 5],verticalCuts = [1, 2, 3, 4, 5]) == 169
    assert candidate(h = 800,w = 600,horizontalCuts = [50, 150, 250, 350, 450, 550, 650, 750],verticalCuts = [30, 130, 230, 330, 430, 530, 590]) == 10000
    assert candidate(h = 200,w = 100,horizontalCuts = [20, 180],verticalCuts = [10, 90]) == 12800
    assert candidate(h = 150,w = 200,horizontalCuts = [10, 30, 50, 70, 90, 110, 130, 140],verticalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 200
    assert candidate(h = 999,w = 999,horizontalCuts = [1, 998],verticalCuts = [1, 998]) == 994009
    assert candidate(h = 200,w = 200,horizontalCuts = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190],verticalCuts = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190]) == 400
    assert candidate(h = 1000000,w = 1000000,horizontalCuts = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000],verticalCuts = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000]) == 999999937
    assert candidate(h = 999999999,w = 999999999,horizontalCuts = [500000000],verticalCuts = [500000000]) == 250000014
    assert candidate(h = 1000000000,w = 1000000000,horizontalCuts = [1, 2, 3, 4, 5],verticalCuts = [1, 2, 3, 4, 5]) == 144
    assert candidate(h = 999999,w = 999999,horizontalCuts = [1, 999998],verticalCuts = [1, 999998]) == 993993016
    assert candidate(h = 500,w = 600,horizontalCuts = [100, 200, 300, 400],verticalCuts = [150, 250, 350, 450, 550]) == 15000
    assert candidate(h = 500000000,w = 500000000,horizontalCuts = [125000000, 250000000, 375000000, 500000000],verticalCuts = [125000000, 250000000, 375000000, 500000000]) == 890625007
    assert candidate(h = 10000,w = 10000,horizontalCuts = [2500, 5000, 7500],verticalCuts = [2500, 5000, 7500]) == 6250000
    assert candidate(h = 30,w = 20,horizontalCuts = [2, 5, 8, 12, 16, 25],verticalCuts = [2, 4, 6, 10, 14]) == 54
    assert candidate(h = 800,w = 600,horizontalCuts = [100, 300, 500, 700],verticalCuts = [150, 300, 450, 600]) == 30000
    assert candidate(h = 100,w = 200,horizontalCuts = [10, 90],verticalCuts = [20, 180]) == 12800
    assert candidate(h = 1000,w = 1500,horizontalCuts = [100, 200, 300, 400, 500, 600, 700, 800, 900],verticalCuts = [150, 300, 450, 600, 750, 900, 1200, 1350]) == 30000
    assert candidate(h = 700,w = 500,horizontalCuts = [50, 100, 200, 300, 400, 500, 600, 650, 700],verticalCuts = [50, 100, 200, 300, 400, 500]) == 10000
    assert candidate(h = 25,w = 30,horizontalCuts = [5, 10, 15, 20],verticalCuts = [5, 10, 15, 20, 25]) == 25
    assert candidate(h = 50,w = 50,horizontalCuts = [1, 5, 10, 25, 49],verticalCuts = [2, 10, 20, 30, 45]) == 360
    assert candidate(h = 1000,w = 1000,horizontalCuts = [10, 100, 200, 300, 400, 500, 600, 700, 800, 900],verticalCuts = [10, 100, 200, 300, 400, 500, 600, 700, 800, 900]) == 10000
    assert candidate(h = 20,w = 15,horizontalCuts = [1, 5, 10, 15],verticalCuts = [2, 6, 10, 14]) == 20
    assert candidate(h = 60,w = 70,horizontalCuts = [10, 20, 30, 40, 50],verticalCuts = [14, 28, 42, 56, 70]) == 140
    assert candidate(h = 500,w = 500,horizontalCuts = [100, 150, 200, 250, 300, 350, 400, 450],verticalCuts = [100, 150, 200, 250, 300, 350, 400, 450]) == 10000
    assert candidate(h = 100,w = 100,horizontalCuts = [1, 50, 99],verticalCuts = [1, 50, 99]) == 2401
    assert candidate(h = 50,w = 200,horizontalCuts = [5, 15, 25, 35, 45],verticalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]) == 100
    assert candidate(h = 100,w = 100,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]) == 100
    assert candidate(h = 70,w = 80,horizontalCuts = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70],verticalCuts = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]) == 56
    assert candidate(h = 300,w = 300,horizontalCuts = [50, 100, 150, 200, 250],verticalCuts = [50, 100, 150, 200, 250]) == 2500
    assert candidate(h = 100,w = 100,horizontalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90],verticalCuts = [10, 20, 30, 40, 50, 60, 70, 80, 90]) == 100


