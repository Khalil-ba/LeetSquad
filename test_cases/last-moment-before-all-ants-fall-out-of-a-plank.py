def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(n = 15,left = [10, 11, 12],right = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15,left = [10, 11, 12],right = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 15: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,left = [],right = [0]) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,left = [],right = [0]) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,left = [5],right = [0]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,left = [5],right = [0]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,left = [1],right = []) == 1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,left = [1],right = []) == 1: {e}')
    
    total += 1
    try:
        result = candidate(n = 5,left = [1, 2],right = [3, 4]) == 2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5,left = [1, 2],right = [3, 4]) == 2: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,left = [0],right = [1]) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,left = [0],right = [1]) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,left = [0, 1, 2, 3, 4, 5, 6, 7],right = []) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,left = [0, 1, 2, 3, 4, 5, 6, 7],right = []) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 4,left = [4, 3],right = [0, 1]) == 4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4,left = [4, 3],right = [0, 1]) == 4: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,left = [2, 6, 7],right = [1, 3, 5, 8]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,left = [2, 6, 7],right = [1, 3, 5, 8]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,left = [10, 20, 30, 40, 50],right = [60, 70, 80, 90, 100]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,left = [10, 20, 30, 40, 50],right = [60, 70, 80, 90, 100]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,left = [2, 6],right = [3, 7]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,left = [2, 6],right = [3, 7]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,left = [],right = [0, 1, 2, 3, 4, 5, 6]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,left = [],right = [0, 1, 2, 3, 4, 5, 6]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,left = [],right = [0, 100]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,left = [],right = [0, 100]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,left = [500, 501, 502],right = [497, 498, 499]) == 503
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,left = [500, 501, 502],right = [497, 498, 499]) == 503: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,left = [50],right = [50]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,left = [50],right = [50]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(n = 1,left = [0],right = []) == 0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1,left = [0],right = []) == 0: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,left = [],right = [0, 1, 2, 3, 4, 5, 6, 7]) == 7
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,left = [],right = [0, 1, 2, 3, 4, 5, 6, 7]) == 7: {e}')
    
    total += 1
    try:
        result = candidate(n = 7,left = [0, 1, 2, 3, 4, 5, 6],right = []) == 6
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7,left = [0, 1, 2, 3, 4, 5, 6],right = []) == 6: {e}')
    
    total += 1
    try:
        result = candidate(n = 100,left = [0, 100],right = []) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 100,left = [0, 100],right = []) == 100: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,left = [5],right = [5]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,left = [5],right = [5]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [1, 2, 3],right = [9997, 9998, 9999]) == 3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [1, 2, 3],right = [9997, 9998, 9999]) == 3: {e}')
    
    total += 1
    try:
        result = candidate(n = 10,left = [1, 2, 3],right = [5, 6, 7]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10,left = [1, 2, 3],right = [5, 6, 7]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 200,left = [100, 150],right = [50, 100]) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 200,left = [100, 150],right = [50, 100]) == 150: {e}')
    
    total += 1
    try:
        result = candidate(n = 7000,left = [0, 7000],right = [3500]) == 7000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7000,left = [0, 7000],right = [3500]) == 7000: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [],right = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == 9000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [],right = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == 9000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],right = [990, 991, 992, 993, 994, 995, 996, 997, 998, 999]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],right = [990, 991, 992, 993, 994, 995, 996, 997, 998, 999]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 3000,left = [100, 200, 300, 400, 500, 600],right = [2400, 2500, 2600, 2700, 2800, 2900]) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3000,left = [100, 200, 300, 400, 500, 600],right = [2400, 2500, 2600, 2700, 2800, 2900]) == 600: {e}')
    
    total += 1
    try:
        result = candidate(n = 8000,left = [100, 200, 300, 400, 500],right = [7900, 7800, 7700, 7600, 7500]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8000,left = [100, 200, 300, 400, 500],right = [7900, 7800, 7700, 7600, 7500]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(n = 3000,left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],right = [2999, 2998, 2997, 2996, 2995, 2994, 2993, 2992, 2991, 2990]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3000,left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],right = [2999, 2998, 2997, 2996, 2995, 2994, 2993, 2992, 2991, 2990]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [1000, 3000, 5000],right = [2000, 4000, 6000, 8000, 9000]) == 8000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [1000, 3000, 5000],right = [2000, 4000, 6000, 8000, 9000]) == 8000: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,left = [1234, 2345, 3456, 4567],right = [1000, 2000, 3000, 4000]) == 4567
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,left = [1234, 2345, 3456, 4567],right = [1000, 2000, 3000, 4000]) == 4567: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [1000, 2000, 3000, 4000],right = [6000, 7000, 8000, 9000]) == 4000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [1000, 2000, 3000, 4000],right = [6000, 7000, 8000, 9000]) == 4000: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [9990, 9991, 9992, 9993, 9994, 9995, 9996, 9997, 9998, 9999],right = []) == 9999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [9990, 9991, 9992, 9993, 9994, 9995, 9996, 9997, 9998, 9999],right = []) == 9999: {e}')
    
    total += 1
    try:
        result = candidate(n = 6000,left = [1500, 2000, 2500, 3000],right = [3500, 4000, 4500, 5000, 5500]) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6000,left = [1500, 2000, 2500, 3000],right = [3500, 4000, 4500, 5000, 5500]) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(n = 8000,left = [1, 100, 200, 300, 400, 500, 600, 700],right = [7999, 7899, 7799, 7699, 7599, 7499, 7399, 7299]) == 701
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8000,left = [1, 100, 200, 300, 400, 500, 600, 700],right = [7999, 7899, 7799, 7699, 7599, 7499, 7399, 7299]) == 701: {e}')
    
    total += 1
    try:
        result = candidate(n = 6000,left = [1000, 2000, 3000, 4000, 5000],right = [1500, 2500, 3500, 4500, 5500]) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6000,left = [1000, 2000, 3000, 4000, 5000],right = [1500, 2500, 3500, 4500, 5500]) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(n = 3000,left = [300, 600, 900, 1200, 1500],right = [2700, 2400, 2100, 1800, 1500]) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3000,left = [300, 600, 900, 1200, 1500],right = [2700, 2400, 2100, 1800, 1500]) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(n = 9000,left = [9000],right = [0]) == 9000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9000,left = [9000],right = [0]) == 9000: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],right = [9990, 9991, 9992, 9993, 9994, 9995, 9996, 9997, 9998, 9999]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],right = [9990, 9991, 9992, 9993, 9994, 9995, 9996, 9997, 9998, 9999]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 4000,left = [0, 800, 1600, 2400, 3200],right = [0, 800, 1600, 2400, 3200]) == 4000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4000,left = [0, 800, 1600, 2400, 3200],right = [0, 800, 1600, 2400, 3200]) == 4000: {e}')
    
    total += 1
    try:
        result = candidate(n = 8000,left = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],right = [7900, 7910, 7920, 7930, 7940, 7950, 7960, 7970, 7980, 7990]) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8000,left = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],right = [7900, 7910, 7920, 7930, 7940, 7950, 7960, 7970, 7980, 7990]) == 100: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [5000, 6000, 7000, 8000, 9000],right = [1000, 2000, 3000, 4000]) == 9000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [5000, 6000, 7000, 8000, 9000],right = [1000, 2000, 3000, 4000]) == 9000: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999,left = [9998, 9997, 9996],right = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999,left = [9998, 9997, 9996],right = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9998: {e}')
    
    total += 1
    try:
        result = candidate(n = 7000,left = [1000, 2000, 3000, 4000, 5000, 6000],right = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 6999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7000,left = [1000, 2000, 3000, 4000, 5000, 6000],right = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 6999: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000,left = [1000, 1500, 1600, 1700],right = [400, 500, 600, 700]) == 1700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000,left = [1000, 1500, 1600, 1700],right = [400, 500, 600, 700]) == 1700: {e}')
    
    total += 1
    try:
        result = candidate(n = 6000,left = [3000],right = [3000]) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6000,left = [3000],right = [3000]) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(n = 6000,left = [0, 1000, 2000, 3000, 4000, 5000],right = [1500, 2500, 3500, 4500, 5500]) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6000,left = [0, 1000, 2000, 3000, 4000, 5000],right = [1500, 2500, 3500, 4500, 5500]) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(n = 15000,left = [],right = [0, 3000, 6000, 9000, 12000, 15000]) == 15000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 15000,left = [],right = [0, 3000, 6000, 9000, 12000, 15000]) == 15000: {e}')
    
    total += 1
    try:
        result = candidate(n = 9000,left = [1000, 3000, 5000, 7000],right = [2000, 4000, 6000, 8000]) == 7000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9000,left = [1000, 3000, 5000, 7000],right = [2000, 4000, 6000, 8000]) == 7000: {e}')
    
    total += 1
    try:
        result = candidate(n = 6000,left = [50, 150, 250, 350, 450, 550],right = [5450, 5550, 5650, 5750, 5850, 5950]) == 550
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6000,left = [50, 150, 250, 350, 450, 550],right = [5450, 5550, 5650, 5750, 5850, 5950]) == 550: {e}')
    
    total += 1
    try:
        result = candidate(n = 8000,left = [1000, 2000, 3000, 4000, 5000],right = [3000, 4000, 5000, 6000, 7000]) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8000,left = [1000, 2000, 3000, 4000, 5000],right = [3000, 4000, 5000, 6000, 7000]) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(n = 9000,left = [100, 200, 300, 400, 500, 600, 700, 800],right = [8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900]) == 800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9000,left = [100, 200, 300, 400, 500, 600, 700, 800],right = [8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900]) == 800: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000,left = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900],right = [900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 1400, 1500, 1600, 1700, 1800, 1900, 1000, 100]) == 1900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000,left = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900],right = [900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 1400, 1500, 1600, 1700, 1800, 1900, 1000, 100]) == 1900: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [1, 10, 100, 1000, 10000],right = [2, 20, 200, 2000, 9999]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [1, 10, 100, 1000, 10000],right = [2, 20, 200, 2000, 9999]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000,left = [500, 1500],right = [100, 1900, 1600]) == 1900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000,left = [500, 1500],right = [100, 1900, 1600]) == 1900: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [1, 2, 3, 5000, 9999],right = [4, 6, 5002, 9997]) == 9999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [1, 2, 3, 5000, 9999],right = [4, 6, 5002, 9997]) == 9999: {e}')
    
    total += 1
    try:
        result = candidate(n = 8000,left = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000],right = [8000]) == 7000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8000,left = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000],right = [8000]) == 7000: {e}')
    
    total += 1
    try:
        result = candidate(n = 4000,left = [2000],right = [2000]) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4000,left = [2000],right = [2000]) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [],right = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [],right = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9999: {e}')
    
    total += 1
    try:
        result = candidate(n = 12000,left = [0, 2400, 4800, 7200, 9600, 12000],right = []) == 12000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12000,left = [0, 2400, 4800, 7200, 9600, 12000],right = []) == 12000: {e}')
    
    total += 1
    try:
        result = candidate(n = 7500,left = [100, 200, 300, 400, 500, 600, 700],right = [7400, 7300, 7200, 7100, 7000, 6900, 6800]) == 700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7500,left = [100, 200, 300, 400, 500, 600, 700],right = [7400, 7300, 7200, 7100, 7000, 6900, 6800]) == 700: {e}')
    
    total += 1
    try:
        result = candidate(n = 9000,left = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500],right = [8500, 8000, 7500, 7000, 6500, 6000, 5500, 5000, 4500]) == 4500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9000,left = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500],right = [8500, 8000, 7500, 7000, 6500, 6000, 5500, 5000, 4500]) == 4500: {e}')
    
    total += 1
    try:
        result = candidate(n = 7000,left = [100, 200, 300, 400],right = [6600, 6700, 6800, 6900]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7000,left = [100, 200, 300, 400],right = [6600, 6700, 6800, 6900]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,left = [2500, 2501, 2502, 2503],right = [2499, 2498, 2497, 2496]) == 2504
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,left = [2500, 2501, 2502, 2503],right = [2499, 2498, 2497, 2496]) == 2504: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,left = [10, 20, 30, 40, 50],right = [450, 460, 470, 480, 490]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,left = [10, 20, 30, 40, 50],right = [450, 460, 470, 480, 490]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(n = 8000,left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],right = [7990, 7991, 7992, 7993, 7994, 7995, 7996, 7997, 7998, 7999]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8000,left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],right = [7990, 7991, 7992, 7993, 7994, 7995, 7996, 7997, 7998, 7999]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 9000,left = [100, 200, 300, 400, 500, 600, 700, 800, 900],right = [8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900]) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9000,left = [100, 200, 300, 400, 500, 600, 700, 800, 900],right = [8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900]) == 900: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,left = [1000, 2000, 3000, 4000, 5000],right = [1, 2, 3, 4]) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,left = [1000, 2000, 3000, 4000, 5000],right = [1, 2, 3, 4]) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000,left = [500, 1000, 1500],right = [100, 600, 1100, 1600]) == 1900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000,left = [500, 1000, 1500],right = [100, 600, 1100, 1600]) == 1900: {e}')
    
    total += 1
    try:
        result = candidate(n = 1500,left = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],right = [1400, 1390, 1380, 1370, 1360, 1350, 1340, 1330, 1320, 1310]) == 190
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1500,left = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],right = [1400, 1390, 1380, 1370, 1360, 1350, 1340, 1330, 1320, 1310]) == 190: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,left = [10, 20, 30, 40, 50],right = [4950, 4960, 4970, 4980, 4990]) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,left = [10, 20, 30, 40, 50],right = [4950, 4960, 4970, 4980, 4990]) == 50: {e}')
    
    total += 1
    try:
        result = candidate(n = 12000,left = [6000, 6100, 6200, 6300],right = [5700, 5800, 5900, 6000]) == 6300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12000,left = [6000, 6100, 6200, 6300],right = [5700, 5800, 5900, 6000]) == 6300: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,left = [1, 2, 3, 4, 5],right = [4995, 4996, 4997, 4998, 4999]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,left = [1, 2, 3, 4, 5],right = [4995, 4996, 4997, 4998, 4999]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [2000, 4000, 6000, 8000],right = [1000, 3000, 5000, 7000, 9000]) == 9000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [2000, 4000, 6000, 8000],right = [1000, 3000, 5000, 7000, 9000]) == 9000: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [1, 100, 1000, 10000],right = [2, 200, 2000, 9999]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [1, 100, 1000, 10000],right = [2, 200, 2000, 9999]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,left = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],right = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 990
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,left = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],right = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 990: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000,left = [500, 1000, 1500, 2000],right = [10, 20, 30, 40, 50]) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000,left = [500, 1000, 1500, 2000],right = [10, 20, 30, 40, 50]) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(n = 4500,left = [500, 1500, 2500, 3500],right = [1000, 2000, 3000, 4000]) == 3500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4500,left = [500, 1500, 2500, 3500],right = [1000, 2000, 3000, 4000]) == 3500: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [0, 2500, 5000, 7500, 10000],right = [10000, 7500, 5000, 2500, 0]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [0, 2500, 5000, 7500, 10000],right = [10000, 7500, 5000, 2500, 0]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(n = 9500,left = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500],right = [1, 2, 3, 4, 5]) == 9500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9500,left = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500],right = [1, 2, 3, 4, 5]) == 9500: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [1, 3, 5, 7, 9],right = [2, 4, 6, 8, 10]) == 9998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [1, 3, 5, 7, 9],right = [2, 4, 6, 8, 10]) == 9998: {e}')
    
    total += 1
    try:
        result = candidate(n = 6000,left = [1000, 2000, 3000, 4000, 5000],right = [500, 1500, 2500, 3500, 4500]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6000,left = [1000, 2000, 3000, 4000, 5000],right = [500, 1500, 2500, 3500, 4500]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(n = 7500,left = [1000, 2000, 3000],right = [5000, 6000, 7000, 7499]) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7500,left = [1000, 2000, 3000],right = [5000, 6000, 7000, 7499]) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(n = 7500,left = [3000, 4000, 5000],right = [2000, 3000, 4000]) == 5500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7500,left = [3000, 4000, 5000],right = [2000, 3000, 4000]) == 5500: {e}')
    
    total += 1
    try:
        result = candidate(n = 12000,left = [12000],right = [6000]) == 12000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12000,left = [12000],right = [6000]) == 12000: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000],right = []) == 9000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000],right = []) == 9000: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500],right = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500]) == 9500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500],right = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500]) == 9500: {e}')
    
    total += 1
    try:
        result = candidate(n = 6000,left = [1000, 2000, 3000, 4000, 5000],right = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6000,left = [1000, 2000, 3000, 4000, 5000],right = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5900: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],right = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 9998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],right = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 9998: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,left = [500, 600, 700, 800, 900],right = [100, 200, 300, 400]) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,left = [500, 600, 700, 800, 900],right = [100, 200, 300, 400]) == 900: {e}')
    
    total += 1
    try:
        result = candidate(n = 7000,left = [0, 7000],right = [0, 7000]) == 7000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7000,left = [0, 7000],right = [0, 7000]) == 7000: {e}')
    
    total += 1
    try:
        result = candidate(n = 8000,left = [1, 2, 3, 4, 5, 6, 7, 8],right = [7992, 7993, 7994, 7995, 7996, 7997, 7998, 7999]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8000,left = [1, 2, 3, 4, 5, 6, 7, 8],right = [7992, 7993, 7994, 7995, 7996, 7997, 7998, 7999]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [5000],right = [5000]) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [5000],right = [5000]) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,left = [999],right = [0]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,left = [999],right = [0]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,left = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509],right = [499, 498, 497, 496, 495, 494, 493, 492, 491, 490]) == 510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,left = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509],right = [499, 498, 497, 496, 495, 494, 493, 492, 491, 490]) == 510: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,left = [100, 200, 300, 400, 500],right = [4500, 4600, 4700, 4800, 4900]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,left = [100, 200, 300, 400, 500],right = [4500, 4600, 4700, 4800, 4900]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,left = [0, 1250, 2500, 3750, 5000],right = [1249, 2499, 3749, 4998]) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,left = [0, 1250, 2500, 3750, 5000],right = [1249, 2499, 3749, 4998]) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(n = 4000,left = [100, 200, 300, 400],right = [3600, 3700, 3800, 3900]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 4000,left = [100, 200, 300, 400],right = [3600, 3700, 3800, 3900]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(n = 12000,left = [2000, 4000, 6000, 8000, 10000],right = [1000, 3000, 5000, 7000, 9000, 11000]) == 11000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12000,left = [2000, 4000, 6000, 8000, 10000],right = [1000, 3000, 5000, 7000, 9000, 11000]) == 11000: {e}')
    
    total += 1
    try:
        result = candidate(n = 9000,left = [1000, 2000, 3000, 4000, 5000],right = [6000, 7000, 8000, 9000]) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9000,left = [1000, 2000, 3000, 4000, 5000],right = [6000, 7000, 8000, 9000]) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999,left = [1, 2, 3, 4, 5, 6, 7, 8, 9],right = [9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990]) == 9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999,left = [1, 2, 3, 4, 5, 6, 7, 8, 9],right = [9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990]) == 9: {e}')
    
    total += 1
    try:
        result = candidate(n = 9000,left = [100, 200, 300, 400, 500, 600, 700, 800, 900],right = [8900, 8800, 8700, 8600, 8500, 8400, 8300, 8200, 8100]) == 900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9000,left = [100, 200, 300, 400, 500, 600, 700, 800, 900],right = [8900, 8800, 8700, 8600, 8500, 8400, 8300, 8200, 8100]) == 900: {e}')
    
    total += 1
    try:
        result = candidate(n = 7000,left = [100, 1000, 2000, 3000, 4000],right = [300, 1300, 2300, 3300, 4300]) == 6700
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7000,left = [100, 1000, 2000, 3000, 4000],right = [300, 1300, 2300, 3300, 4300]) == 6700: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,left = [2500, 2501, 2502, 2503, 2504],right = [2495, 2496, 2497, 2498, 2499]) == 2505
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,left = [2500, 2501, 2502, 2503, 2504],right = [2495, 2496, 2497, 2498, 2499]) == 2505: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,left = [100, 200, 300, 400, 500, 600, 700, 800, 900],right = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == 950
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,left = [100, 200, 300, 400, 500, 600, 700, 800, 900],right = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == 950: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999,left = [500, 1500, 2500, 3500, 4500],right = [5500, 6500, 7500, 8500, 9500]) == 4500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999,left = [500, 1500, 2500, 3500, 4500],right = [5500, 6500, 7500, 8500, 9500]) == 4500: {e}')
    
    total += 1
    try:
        result = candidate(n = 1000,left = [100, 200, 300, 400, 500],right = [600, 700, 800, 900]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 1000,left = [100, 200, 300, 400, 500],right = [600, 700, 800, 900]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],right = [9991, 9992, 9993, 9994, 9995, 9996, 9997, 9998, 9999, 10000]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],right = [9991, 9992, 9993, 9994, 9995, 9996, 9997, 9998, 9999, 10000]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [1, 2, 3, 4, 5],right = [9996, 9995, 9994, 9993, 9992]) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [1, 2, 3, 4, 5],right = [9996, 9995, 9994, 9993, 9992]) == 8: {e}')
    
    total += 1
    try:
        result = candidate(n = 8500,left = [8500],right = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 7500]) == 8500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8500,left = [8500],right = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 7500]) == 8500: {e}')
    
    total += 1
    try:
        result = candidate(n = 6000,left = [0, 6000],right = [3000]) == 6000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 6000,left = [0, 6000],right = [3000]) == 6000: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,left = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],right = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 4998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,left = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],right = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 4998: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,left = [4999, 4998, 4997, 4996],right = [1, 2, 3, 4]) == 4999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,left = [4999, 4998, 4997, 4996],right = [1, 2, 3, 4]) == 4999: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,left = [1000, 2000, 3000, 4000],right = [500, 1500, 2500, 3500, 4500]) == 4500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,left = [1000, 2000, 3000, 4000],right = [500, 1500, 2500, 3500, 4500]) == 4500: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [1000, 2000, 3000, 4000],right = [7000, 8000, 9000]) == 4000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [1000, 2000, 3000, 4000],right = [7000, 8000, 9000]) == 4000: {e}')
    
    total += 1
    try:
        result = candidate(n = 12000,left = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],right = [11900, 11800, 11700, 11600, 11500, 11400, 11300, 11200, 11100, 11000]) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 12000,left = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],right = [11900, 11800, 11700, 11600, 11500, 11400, 11300, 11200, 11100, 11000]) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,left = [0, 250, 500],right = [0, 250, 500]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,left = [0, 250, 500],right = [0, 250, 500]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(n = 9999,left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],right = [9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990, 9989]) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 9999,left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],right = [9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990, 9989]) == 10: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],right = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 9999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],right = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 9999: {e}')
    
    total += 1
    try:
        result = candidate(n = 500,left = [0, 100, 200, 300, 400],right = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 490
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 500,left = [0, 100, 200, 300, 400],right = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 490: {e}')
    
    total += 1
    try:
        result = candidate(n = 7000,left = [500, 1000, 1500, 2000, 2500],right = [6500, 7000, 6000, 6500, 7000]) == 2500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 7000,left = [500, 1000, 1500, 2000, 2500],right = [6500, 7000, 6000, 6500, 7000]) == 2500: {e}')
    
    total += 1
    try:
        result = candidate(n = 5000,left = [100, 200, 300, 400],right = [4600, 4700, 4800, 4900]) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 5000,left = [100, 200, 300, 400],right = [4600, 4700, 4800, 4900]) == 400: {e}')
    
    total += 1
    try:
        result = candidate(n = 10000,left = [1, 100, 1000, 10000],right = [50, 500, 5000, 9950]) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 10000,left = [1, 100, 1000, 10000],right = [50, 500, 5000, 9950]) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(n = 8000,left = [1, 2, 3, 4, 5],right = [7995, 7996, 7997, 7998, 7999]) == 5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 8000,left = [1, 2, 3, 4, 5],right = [7995, 7996, 7997, 7998, 7999]) == 5: {e}')
    
    total += 1
    try:
        result = candidate(n = 2000,left = [100, 200, 300, 400, 500],right = [1500, 1600, 1700, 1800, 1900]) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 2000,left = [100, 200, 300, 400, 500],right = [1500, 1600, 1700, 1800, 1900]) == 500: {e}')
    
    total += 1
    try:
        result = candidate(n = 3000,left = [500, 1000, 1500, 2000, 2500],right = [100, 600, 1100, 1600, 2100]) == 2900
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(n = 3000,left = [500, 1000, 1500, 2000, 2500],right = [100, 600, 1100, 1600, 2100]) == 2900: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(n = 15,left = [10, 11, 12],right = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 15
    assert candidate(n = 1,left = [],right = [0]) == 1
    assert candidate(n = 5,left = [5],right = [0]) == 5
    assert candidate(n = 1,left = [1],right = []) == 1
    assert candidate(n = 5,left = [1, 2],right = [3, 4]) == 2
    assert candidate(n = 1,left = [0],right = [1]) == 0
    assert candidate(n = 7,left = [0, 1, 2, 3, 4, 5, 6, 7],right = []) == 7
    assert candidate(n = 4,left = [4, 3],right = [0, 1]) == 4
    assert candidate(n = 10,left = [2, 6, 7],right = [1, 3, 5, 8]) == 9
    assert candidate(n = 100,left = [10, 20, 30, 40, 50],right = [60, 70, 80, 90, 100]) == 50
    assert candidate(n = 10,left = [2, 6],right = [3, 7]) == 7
    assert candidate(n = 7,left = [],right = [0, 1, 2, 3, 4, 5, 6]) == 7
    assert candidate(n = 100,left = [],right = [0, 100]) == 100
    assert candidate(n = 1000,left = [500, 501, 502],right = [497, 498, 499]) == 503
    assert candidate(n = 100,left = [50],right = [50]) == 50
    assert candidate(n = 1,left = [0],right = []) == 0
    assert candidate(n = 7,left = [],right = [0, 1, 2, 3, 4, 5, 6, 7]) == 7
    assert candidate(n = 7,left = [0, 1, 2, 3, 4, 5, 6],right = []) == 6
    assert candidate(n = 100,left = [0, 100],right = []) == 100
    assert candidate(n = 10,left = [5],right = [5]) == 5
    assert candidate(n = 10000,left = [1, 2, 3],right = [9997, 9998, 9999]) == 3
    assert candidate(n = 10,left = [1, 2, 3],right = [5, 6, 7]) == 5
    assert candidate(n = 200,left = [100, 150],right = [50, 100]) == 150
    assert candidate(n = 7000,left = [0, 7000],right = [3500]) == 7000
    assert candidate(n = 10000,left = [],right = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == 9000
    assert candidate(n = 1000,left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],right = [990, 991, 992, 993, 994, 995, 996, 997, 998, 999]) == 10
    assert candidate(n = 3000,left = [100, 200, 300, 400, 500, 600],right = [2400, 2500, 2600, 2700, 2800, 2900]) == 600
    assert candidate(n = 8000,left = [100, 200, 300, 400, 500],right = [7900, 7800, 7700, 7600, 7500]) == 500
    assert candidate(n = 3000,left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],right = [2999, 2998, 2997, 2996, 2995, 2994, 2993, 2992, 2991, 2990]) == 10
    assert candidate(n = 10000,left = [1000, 3000, 5000],right = [2000, 4000, 6000, 8000, 9000]) == 8000
    assert candidate(n = 5000,left = [1234, 2345, 3456, 4567],right = [1000, 2000, 3000, 4000]) == 4567
    assert candidate(n = 10000,left = [1000, 2000, 3000, 4000],right = [6000, 7000, 8000, 9000]) == 4000
    assert candidate(n = 10000,left = [9990, 9991, 9992, 9993, 9994, 9995, 9996, 9997, 9998, 9999],right = []) == 9999
    assert candidate(n = 6000,left = [1500, 2000, 2500, 3000],right = [3500, 4000, 4500, 5000, 5500]) == 3000
    assert candidate(n = 8000,left = [1, 100, 200, 300, 400, 500, 600, 700],right = [7999, 7899, 7799, 7699, 7599, 7499, 7399, 7299]) == 701
    assert candidate(n = 6000,left = [1000, 2000, 3000, 4000, 5000],right = [1500, 2500, 3500, 4500, 5500]) == 5000
    assert candidate(n = 3000,left = [300, 600, 900, 1200, 1500],right = [2700, 2400, 2100, 1800, 1500]) == 1500
    assert candidate(n = 9000,left = [9000],right = [0]) == 9000
    assert candidate(n = 10000,left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],right = [9990, 9991, 9992, 9993, 9994, 9995, 9996, 9997, 9998, 9999]) == 10
    assert candidate(n = 4000,left = [0, 800, 1600, 2400, 3200],right = [0, 800, 1600, 2400, 3200]) == 4000
    assert candidate(n = 8000,left = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],right = [7900, 7910, 7920, 7930, 7940, 7950, 7960, 7970, 7980, 7990]) == 100
    assert candidate(n = 10000,left = [5000, 6000, 7000, 8000, 9000],right = [1000, 2000, 3000, 4000]) == 9000
    assert candidate(n = 9999,left = [9998, 9997, 9996],right = [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 9998
    assert candidate(n = 7000,left = [1000, 2000, 3000, 4000, 5000, 6000],right = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 6999
    assert candidate(n = 2000,left = [1000, 1500, 1600, 1700],right = [400, 500, 600, 700]) == 1700
    assert candidate(n = 6000,left = [3000],right = [3000]) == 3000
    assert candidate(n = 6000,left = [0, 1000, 2000, 3000, 4000, 5000],right = [1500, 2500, 3500, 4500, 5500]) == 5000
    assert candidate(n = 15000,left = [],right = [0, 3000, 6000, 9000, 12000, 15000]) == 15000
    assert candidate(n = 9000,left = [1000, 3000, 5000, 7000],right = [2000, 4000, 6000, 8000]) == 7000
    assert candidate(n = 6000,left = [50, 150, 250, 350, 450, 550],right = [5450, 5550, 5650, 5750, 5850, 5950]) == 550
    assert candidate(n = 8000,left = [1000, 2000, 3000, 4000, 5000],right = [3000, 4000, 5000, 6000, 7000]) == 5000
    assert candidate(n = 9000,left = [100, 200, 300, 400, 500, 600, 700, 800],right = [8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900]) == 800
    assert candidate(n = 2000,left = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900],right = [900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 1400, 1500, 1600, 1700, 1800, 1900, 1000, 100]) == 1900
    assert candidate(n = 10000,left = [1, 10, 100, 1000, 10000],right = [2, 20, 200, 2000, 9999]) == 10000
    assert candidate(n = 2000,left = [500, 1500],right = [100, 1900, 1600]) == 1900
    assert candidate(n = 10000,left = [1, 2, 3, 5000, 9999],right = [4, 6, 5002, 9997]) == 9999
    assert candidate(n = 8000,left = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000],right = [8000]) == 7000
    assert candidate(n = 4000,left = [2000],right = [2000]) == 2000
    assert candidate(n = 10000,left = [],right = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9999
    assert candidate(n = 12000,left = [0, 2400, 4800, 7200, 9600, 12000],right = []) == 12000
    assert candidate(n = 7500,left = [100, 200, 300, 400, 500, 600, 700],right = [7400, 7300, 7200, 7100, 7000, 6900, 6800]) == 700
    assert candidate(n = 9000,left = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500],right = [8500, 8000, 7500, 7000, 6500, 6000, 5500, 5000, 4500]) == 4500
    assert candidate(n = 7000,left = [100, 200, 300, 400],right = [6600, 6700, 6800, 6900]) == 400
    assert candidate(n = 5000,left = [2500, 2501, 2502, 2503],right = [2499, 2498, 2497, 2496]) == 2504
    assert candidate(n = 500,left = [10, 20, 30, 40, 50],right = [450, 460, 470, 480, 490]) == 50
    assert candidate(n = 8000,left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],right = [7990, 7991, 7992, 7993, 7994, 7995, 7996, 7997, 7998, 7999]) == 10
    assert candidate(n = 9000,left = [100, 200, 300, 400, 500, 600, 700, 800, 900],right = [8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900]) == 900
    assert candidate(n = 5000,left = [1000, 2000, 3000, 4000, 5000],right = [1, 2, 3, 4]) == 5000
    assert candidate(n = 2000,left = [500, 1000, 1500],right = [100, 600, 1100, 1600]) == 1900
    assert candidate(n = 1500,left = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],right = [1400, 1390, 1380, 1370, 1360, 1350, 1340, 1330, 1320, 1310]) == 190
    assert candidate(n = 5000,left = [10, 20, 30, 40, 50],right = [4950, 4960, 4970, 4980, 4990]) == 50
    assert candidate(n = 12000,left = [6000, 6100, 6200, 6300],right = [5700, 5800, 5900, 6000]) == 6300
    assert candidate(n = 5000,left = [1, 2, 3, 4, 5],right = [4995, 4996, 4997, 4998, 4999]) == 5
    assert candidate(n = 10000,left = [2000, 4000, 6000, 8000],right = [1000, 3000, 5000, 7000, 9000]) == 9000
    assert candidate(n = 10000,left = [1, 100, 1000, 10000],right = [2, 200, 2000, 9999]) == 10000
    assert candidate(n = 1000,left = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],right = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 990
    assert candidate(n = 2000,left = [500, 1000, 1500, 2000],right = [10, 20, 30, 40, 50]) == 2000
    assert candidate(n = 4500,left = [500, 1500, 2500, 3500],right = [1000, 2000, 3000, 4000]) == 3500
    assert candidate(n = 10000,left = [0, 2500, 5000, 7500, 10000],right = [10000, 7500, 5000, 2500, 0]) == 10000
    assert candidate(n = 9500,left = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500],right = [1, 2, 3, 4, 5]) == 9500
    assert candidate(n = 10000,left = [1, 3, 5, 7, 9],right = [2, 4, 6, 8, 10]) == 9998
    assert candidate(n = 6000,left = [1000, 2000, 3000, 4000, 5000],right = [500, 1500, 2500, 3500, 4500]) == 5500
    assert candidate(n = 7500,left = [1000, 2000, 3000],right = [5000, 6000, 7000, 7499]) == 3000
    assert candidate(n = 7500,left = [3000, 4000, 5000],right = [2000, 3000, 4000]) == 5500
    assert candidate(n = 12000,left = [12000],right = [6000]) == 12000
    assert candidate(n = 10000,left = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000],right = []) == 9000
    assert candidate(n = 10000,left = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500],right = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500]) == 9500
    assert candidate(n = 6000,left = [1000, 2000, 3000, 4000, 5000],right = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 5900
    assert candidate(n = 10000,left = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],right = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 9998
    assert candidate(n = 1000,left = [500, 600, 700, 800, 900],right = [100, 200, 300, 400]) == 900
    assert candidate(n = 7000,left = [0, 7000],right = [0, 7000]) == 7000
    assert candidate(n = 8000,left = [1, 2, 3, 4, 5, 6, 7, 8],right = [7992, 7993, 7994, 7995, 7996, 7997, 7998, 7999]) == 8
    assert candidate(n = 10000,left = [5000],right = [5000]) == 5000
    assert candidate(n = 1000,left = [999],right = [0]) == 1000
    assert candidate(n = 1000,left = [500, 501, 502, 503, 504, 505, 506, 507, 508, 509],right = [499, 498, 497, 496, 495, 494, 493, 492, 491, 490]) == 510
    assert candidate(n = 5000,left = [100, 200, 300, 400, 500],right = [4500, 4600, 4700, 4800, 4900]) == 500
    assert candidate(n = 5000,left = [0, 1250, 2500, 3750, 5000],right = [1249, 2499, 3749, 4998]) == 5000
    assert candidate(n = 4000,left = [100, 200, 300, 400],right = [3600, 3700, 3800, 3900]) == 400
    assert candidate(n = 12000,left = [2000, 4000, 6000, 8000, 10000],right = [1000, 3000, 5000, 7000, 9000, 11000]) == 11000
    assert candidate(n = 9000,left = [1000, 2000, 3000, 4000, 5000],right = [6000, 7000, 8000, 9000]) == 5000
    assert candidate(n = 9999,left = [1, 2, 3, 4, 5, 6, 7, 8, 9],right = [9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990]) == 9
    assert candidate(n = 9000,left = [100, 200, 300, 400, 500, 600, 700, 800, 900],right = [8900, 8800, 8700, 8600, 8500, 8400, 8300, 8200, 8100]) == 900
    assert candidate(n = 7000,left = [100, 1000, 2000, 3000, 4000],right = [300, 1300, 2300, 3300, 4300]) == 6700
    assert candidate(n = 5000,left = [2500, 2501, 2502, 2503, 2504],right = [2495, 2496, 2497, 2498, 2499]) == 2505
    assert candidate(n = 1000,left = [100, 200, 300, 400, 500, 600, 700, 800, 900],right = [50, 150, 250, 350, 450, 550, 650, 750, 850, 950]) == 950
    assert candidate(n = 9999,left = [500, 1500, 2500, 3500, 4500],right = [5500, 6500, 7500, 8500, 9500]) == 4500
    assert candidate(n = 1000,left = [100, 200, 300, 400, 500],right = [600, 700, 800, 900]) == 500
    assert candidate(n = 10000,left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],right = [9991, 9992, 9993, 9994, 9995, 9996, 9997, 9998, 9999, 10000]) == 10
    assert candidate(n = 10000,left = [1, 2, 3, 4, 5],right = [9996, 9995, 9994, 9993, 9992]) == 8
    assert candidate(n = 8500,left = [8500],right = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 7500]) == 8500
    assert candidate(n = 6000,left = [0, 6000],right = [3000]) == 6000
    assert candidate(n = 5000,left = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],right = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 4998
    assert candidate(n = 5000,left = [4999, 4998, 4997, 4996],right = [1, 2, 3, 4]) == 4999
    assert candidate(n = 5000,left = [1000, 2000, 3000, 4000],right = [500, 1500, 2500, 3500, 4500]) == 4500
    assert candidate(n = 10000,left = [1000, 2000, 3000, 4000],right = [7000, 8000, 9000]) == 4000
    assert candidate(n = 12000,left = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],right = [11900, 11800, 11700, 11600, 11500, 11400, 11300, 11200, 11100, 11000]) == 1000
    assert candidate(n = 500,left = [0, 250, 500],right = [0, 250, 500]) == 500
    assert candidate(n = 9999,left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],right = [9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990, 9989]) == 10
    assert candidate(n = 10000,left = [9999, 9998, 9997, 9996, 9995, 9994, 9993, 9992, 9991, 9990],right = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 9999
    assert candidate(n = 500,left = [0, 100, 200, 300, 400],right = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 490
    assert candidate(n = 7000,left = [500, 1000, 1500, 2000, 2500],right = [6500, 7000, 6000, 6500, 7000]) == 2500
    assert candidate(n = 5000,left = [100, 200, 300, 400],right = [4600, 4700, 4800, 4900]) == 400
    assert candidate(n = 10000,left = [1, 100, 1000, 10000],right = [50, 500, 5000, 9950]) == 10000
    assert candidate(n = 8000,left = [1, 2, 3, 4, 5],right = [7995, 7996, 7997, 7998, 7999]) == 5
    assert candidate(n = 2000,left = [100, 200, 300, 400, 500],right = [1500, 1600, 1700, 1800, 1900]) == 500
    assert candidate(n = 3000,left = [500, 1000, 1500, 2000, 2500],right = [100, 600, 1100, 1600, 2100]) == 2900


