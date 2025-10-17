def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(baseCosts = [10, 20],toppingCosts = [1, 2, 3],target = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [10, 20],toppingCosts = [1, 2, 3],target = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [5, 9],toppingCosts = [2, 3, 7],target = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [5, 9],toppingCosts = [2, 3, 7],target = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1, 7],toppingCosts = [3, 4],target = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1, 7],toppingCosts = [3, 4],target = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [10, 20, 30],toppingCosts = [1, 2, 3, 4, 5],target = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [10, 20, 30],toppingCosts = [1, 2, 3, 4, 5],target = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [4, 8],toppingCosts = [1, 3],target = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [4, 8],toppingCosts = [1, 3],target = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [5],toppingCosts = [1, 2, 3],target = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [5],toppingCosts = [1, 2, 3],target = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [4],toppingCosts = [1, 2, 3],target = 8) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [4],toppingCosts = [1, 2, 3],target = 8) == 8: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [10, 20],toppingCosts = [5, 15, 25],target = 50) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [10, 20],toppingCosts = [5, 15, 25],target = 50) == 50: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1],toppingCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1],toppingCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [5, 8],toppingCosts = [6, 1, 2],target = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [5, 8],toppingCosts = [6, 1, 2],target = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [10],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [10],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [2, 3],toppingCosts = [4, 5, 100],target = 18) == 17
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [2, 3],toppingCosts = [4, 5, 100],target = 18) == 17: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [3, 10],toppingCosts = [2, 5],target = 9) == 8
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [3, 10],toppingCosts = [2, 5],target = 9) == 8: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [4, 8, 12, 16, 20],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 30) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [4, 8, 12, 16, 20],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 30) == 30: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [50, 75, 100, 125],toppingCosts = [10, 15, 20, 25, 30],target = 300) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [50, 75, 100, 125],toppingCosts = [10, 15, 20, 25, 30],target = 300) == 300: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],toppingCosts = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1023) == 1023
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],toppingCosts = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1023) == 1023: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 1500) == 1500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 1500) == 1500: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1234, 5678, 9101],toppingCosts = [111, 222, 333, 444, 555, 666],target = 10000) == 10007
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1234, 5678, 9101],toppingCosts = [111, 222, 333, 444, 555, 666],target = 10000) == 10007: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [5000, 7500, 10000],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 15000) == 15000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [5000, 7500, 10000],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 15000) == 15000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1000, 2000, 3000, 4000, 5000],toppingCosts = [50, 100, 150, 200, 250, 300, 350],target = 10000) == 7800
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1000, 2000, 3000, 4000, 5000],toppingCosts = [50, 100, 150, 200, 250, 300, 350],target = 10000) == 7800: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [15, 25, 35, 45],toppingCosts = [2, 4, 6, 8, 10],target = 50) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [15, 25, 35, 45],toppingCosts = [2, 4, 6, 8, 10],target = 50) == 49: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [100, 200, 300, 400],toppingCosts = [10, 20, 30, 40, 50],target = 500) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [100, 200, 300, 400],toppingCosts = [10, 20, 30, 40, 50],target = 500) == 500: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [123, 456, 789],toppingCosts = [987, 654, 321, 654, 321, 987],target = 1000) == 1086
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [123, 456, 789],toppingCosts = [987, 654, 321, 654, 321, 987],target = 1000) == 1086: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [10, 20, 30, 40, 50],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 150) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [10, 20, 30, 40, 50],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 150) == 150: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1000, 2000, 3000, 4000, 5000],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 7500) == 7500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1000, 2000, 3000, 4000, 5000],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 7500) == 7500: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1, 5, 10, 15],toppingCosts = [3, 6, 9, 12],target = 30) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1, 5, 10, 15],toppingCosts = [3, 6, 9, 12],target = 30) == 30: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [7, 14, 21],toppingCosts = [3, 6, 9, 12, 15, 18],target = 30) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [7, 14, 21],toppingCosts = [3, 6, 9, 12, 15, 18],target = 30) == 30: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [500, 1000, 1500],toppingCosts = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],target = 3000) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [500, 1000, 1500],toppingCosts = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],target = 3000) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1000, 2000],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 5000) == 5000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1000, 2000],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 5000) == 5000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [8, 16, 24],toppingCosts = [2, 4, 6, 8, 10, 12, 14, 16],target = 35) == 34
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [8, 16, 24],toppingCosts = [2, 4, 6, 8, 10, 12, 14, 16],target = 35) == 34: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1000, 2000, 3000, 4000, 5000],toppingCosts = [100, 200, 300, 400, 500],target = 12345) == 8000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1000, 2000, 3000, 4000, 5000],toppingCosts = [100, 200, 300, 400, 500],target = 12345) == 8000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [3, 6, 9, 12, 15],toppingCosts = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1024) == 1024
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [3, 6, 9, 12, 15],toppingCosts = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1024) == 1024: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [300, 600, 900],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 1200) == 1200
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [300, 600, 900],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 1200) == 1200: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1, 2, 3, 4, 5],toppingCosts = [5, 10, 15, 20, 25],target = 50) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1, 2, 3, 4, 5],toppingCosts = [5, 10, 15, 20, 25],target = 50) == 50: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 50) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 50) == 50: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [100, 200, 300],toppingCosts = [50, 75, 100, 125, 150],target = 600) == 600
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [100, 200, 300],toppingCosts = [50, 75, 100, 125, 150],target = 600) == 600: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1, 10000],toppingCosts = [5000, 3000, 2000, 1000, 500, 100],target = 9000) == 9001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1, 10000],toppingCosts = [5000, 3000, 2000, 1000, 500, 100],target = 9000) == 9001: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [15, 25, 35],toppingCosts = [5, 7, 11, 13, 17],target = 50) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [15, 25, 35],toppingCosts = [5, 7, 11, 13, 17],target = 50) == 50: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [100, 150, 200, 250],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90],target = 750) == 750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [100, 150, 200, 250],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90],target = 750) == 750: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [999, 1999, 2999],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5000) == 3109
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [999, 1999, 2999],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5000) == 3109: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1, 1, 1, 1, 1],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1, 1, 1, 1, 1],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [150, 250, 350],toppingCosts = [5, 15, 25, 35, 45, 55],target = 400) == 400
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [150, 250, 350],toppingCosts = [5, 15, 25, 35, 45, 55],target = 400) == 400: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [2000, 4000, 6000],toppingCosts = [100, 200, 300, 400, 500],target = 7000) == 7000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [2000, 4000, 6000],toppingCosts = [100, 200, 300, 400, 500],target = 7000) == 7000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1, 10, 100],toppingCosts = [9, 90, 900, 9000],target = 10000) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1, 10, 100],toppingCosts = [9, 90, 900, 9000],target = 10000) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 1000) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 1000) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [7500, 8000],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 15000) == 15000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [7500, 8000],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 15000) == 15000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [15, 25, 35, 45],toppingCosts = [1, 2, 3, 4, 5, 6, 7],target = 30) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [15, 25, 35, 45],toppingCosts = [1, 2, 3, 4, 5, 6, 7],target = 30) == 30: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [10, 20, 30],toppingCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 45) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [10, 20, 30],toppingCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 45) == 45: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1, 1, 1, 1, 1],toppingCosts = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 100) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1, 1, 1, 1, 1],toppingCosts = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 100) == 101: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1000, 2000, 3000, 4000, 5000],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 10000) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1000, 2000, 3000, 4000, 5000],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 10000) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 100) == 100
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 100) == 100: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [5000, 7000, 9000],toppingCosts = [1000, 2000, 3000, 4000],target = 18000) == 18000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [5000, 7000, 9000],toppingCosts = [1000, 2000, 3000, 4000],target = 18000) == 18000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [500, 250],toppingCosts = [100, 200, 300, 400, 500],target = 1000) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [500, 250],toppingCosts = [100, 200, 300, 400, 500],target = 1000) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [10000],toppingCosts = [10000, 10000, 10000, 10000, 10000],target = 50000) == 50000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [10000],toppingCosts = [10000, 10000, 10000, 10000, 10000],target = 50000) == 50000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 500) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 500) == 210: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [100, 200, 300],toppingCosts = [10, 20, 30, 40, 50, 60],target = 500) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [100, 200, 300],toppingCosts = [10, 20, 30, 40, 50, 60],target = 500) == 500: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1000, 2000, 3000],toppingCosts = [500, 100, 250, 125, 75],target = 4500) == 4500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1000, 2000, 3000],toppingCosts = [500, 100, 250, 125, 75],target = 4500) == 4500: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [123, 456, 789],toppingCosts = [11, 22, 33, 44, 55, 66, 77, 88, 99],target = 1000) == 998
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [123, 456, 789],toppingCosts = [11, 22, 33, 44, 55, 66, 77, 88, 99],target = 1000) == 998: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [5, 10, 15, 20, 25],toppingCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 20) == 20
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [5, 10, 15, 20, 25],toppingCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 20) == 20: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [9999],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 10000) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [9999],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 10000) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [123, 456, 789],toppingCosts = [987, 654, 321, 123, 456, 789, 100, 200, 300],target = 2000) == 2000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [123, 456, 789],toppingCosts = [987, 654, 321, 123, 456, 789, 100, 200, 300],target = 2000) == 2000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [500, 501, 502],toppingCosts = [250, 251, 252, 253],target = 1000) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [500, 501, 502],toppingCosts = [250, 251, 252, 253],target = 1000) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [777, 888],toppingCosts = [55, 44, 33, 22, 11, 1, 2, 3, 4, 5],target = 2000) == 1248
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [777, 888],toppingCosts = [55, 44, 33, 22, 11, 1, 2, 3, 4, 5],target = 2000) == 1248: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [10, 20, 30, 40, 50],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 25) == 25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [10, 20, 30, 40, 50],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 25) == 25: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [10, 20, 30, 40, 50],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 50) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [10, 20, 30, 40, 50],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 50) == 50: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],toppingCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 10
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],toppingCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 10: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],toppingCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 30) == 30
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],toppingCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 30) == 30: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [123, 456, 789],toppingCosts = [11, 22, 33, 44, 55],target = 700) == 698
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [123, 456, 789],toppingCosts = [11, 22, 33, 44, 55],target = 700) == 698: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [100, 200, 300, 400],toppingCosts = [10, 20, 30, 40, 50, 60],target = 750) == 750
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [100, 200, 300, 400],toppingCosts = [10, 20, 30, 40, 50, 60],target = 750) == 750: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [100, 200],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 500) == 310
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [100, 200],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 500) == 310: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1000, 1001, 1002, 1003],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 10000) == 1113
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1000, 1001, 1002, 1003],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 10000) == 1113: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [23, 45, 67, 89, 10],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 200) == 199
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [23, 45, 67, 89, 10],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 200) == 199: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [5, 10, 15, 20],toppingCosts = [1, 3, 5, 7, 9, 11, 13],target = 40) == 40
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [5, 10, 15, 20],toppingCosts = [1, 3, 5, 7, 9, 11, 13],target = 40) == 40: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [100, 200, 300, 400, 500],toppingCosts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 1000) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [100, 200, 300, 400, 500],toppingCosts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 1000) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],toppingCosts = [2, 4, 6, 8, 10],target = 50) == 49
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],toppingCosts = [2, 4, 6, 8, 10],target = 50) == 49: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [100, 200, 300, 400],toppingCosts = [10, 20, 30, 40, 50, 60],target = 1500) == 820
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [100, 200, 300, 400],toppingCosts = [10, 20, 30, 40, 50, 60],target = 1500) == 820: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [100, 200, 300, 400],toppingCosts = [50, 10, 15, 20, 25, 30, 35, 40, 45, 55],target = 1500) == 1050
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [100, 200, 300, 400],toppingCosts = [50, 10, 15, 20, 25, 30, 35, 40, 45, 55],target = 1500) == 1050: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1, 2, 3, 4, 5],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 100) == 101
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1, 2, 3, 4, 5],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 100) == 101: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],toppingCosts = [500, 1500, 2500, 3500],target = 7500) == 7500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],toppingCosts = [500, 1500, 2500, 3500],target = 7500) == 7500: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [2000, 3000, 4000, 5000],toppingCosts = [50, 100, 150, 200, 250],target = 8500) == 6500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [2000, 3000, 4000, 5000],toppingCosts = [50, 100, 150, 200, 250],target = 8500) == 6500: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [50, 100, 150, 200, 250, 300],toppingCosts = [5, 10, 15, 20, 25, 30],target = 750) == 510
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [50, 100, 150, 200, 250, 300],toppingCosts = [5, 10, 15, 20, 25, 30],target = 750) == 510: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [100, 200],toppingCosts = [50, 25, 10, 5, 1],target = 300) == 300
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [100, 200],toppingCosts = [50, 25, 10, 5, 1],target = 300) == 300: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 5000) == 5001
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 5000) == 5001: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1000, 2000, 3000],toppingCosts = [500, 1000, 1500, 2000, 2500],target = 6000) == 6000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1000, 2000, 3000],toppingCosts = [500, 1000, 1500, 2000, 2500],target = 6000) == 6000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 50) == 50
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 50) == 50: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [800, 1600, 2400],toppingCosts = [100, 200, 300, 400, 500, 600],target = 3000) == 3000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [800, 1600, 2400],toppingCosts = [100, 200, 300, 400, 500, 600],target = 3000) == 3000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [5000, 10000],toppingCosts = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],target = 20000) == 20000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [5000, 10000],toppingCosts = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],target = 20000) == 20000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1000, 2000, 3000],toppingCosts = [500, 100, 250, 150, 200],target = 4500) == 4500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1000, 2000, 3000],toppingCosts = [500, 100, 250, 150, 200],target = 4500) == 4500: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [4, 8, 12, 16, 20],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 45) == 45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [4, 8, 12, 16, 20],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 45) == 45: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1, 2, 3, 4, 5],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 500) == 501
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1, 2, 3, 4, 5],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 500) == 501: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [50, 60, 70, 80, 90],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 150) == 150
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [50, 60, 70, 80, 90],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 150) == 150: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [100, 200, 300],toppingCosts = [50, 75, 100, 125, 150],target = 500) == 500
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [100, 200, 300],toppingCosts = [50, 75, 100, 125, 150],target = 500) == 500: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [5000],toppingCosts = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],target = 20000) == 20000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [5000],toppingCosts = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],target = 20000) == 20000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [10, 20],toppingCosts = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1000) == 1000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [10, 20],toppingCosts = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1000) == 1000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 500) == 210
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 500) == 210: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],toppingCosts = [9999],target = 10000) == 10000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],toppingCosts = [9999],target = 10000) == 10000: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [5, 10],toppingCosts = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 15) == 15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [5, 10],toppingCosts = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 15) == 15: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [500, 1000, 1500],toppingCosts = [5, 10, 15, 20, 25, 30, 35, 40],target = 2000) == 1860
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [500, 1000, 1500],toppingCosts = [5, 10, 15, 20, 25, 30, 35, 40],target = 2000) == 1860: {e}')
    
    total += 1
    try:
        result = candidate(baseCosts = [999, 1000],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 4000) == 4000
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(baseCosts = [999, 1000],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 4000) == 4000: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(baseCosts = [10, 20],toppingCosts = [1, 2, 3],target = 15) == 15
    assert candidate(baseCosts = [5, 9],toppingCosts = [2, 3, 7],target = 15) == 15
    assert candidate(baseCosts = [1, 7],toppingCosts = [3, 4],target = 10) == 10
    assert candidate(baseCosts = [10, 20, 30],toppingCosts = [1, 2, 3, 4, 5],target = 25) == 25
    assert candidate(baseCosts = [4, 8],toppingCosts = [1, 3],target = 15) == 15
    assert candidate(baseCosts = [5],toppingCosts = [1, 2, 3],target = 8) == 8
    assert candidate(baseCosts = [4],toppingCosts = [1, 2, 3],target = 8) == 8
    assert candidate(baseCosts = [10, 20],toppingCosts = [5, 15, 25],target = 50) == 50
    assert candidate(baseCosts = [1],toppingCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 10
    assert candidate(baseCosts = [5, 8],toppingCosts = [6, 1, 2],target = 20) == 20
    assert candidate(baseCosts = [10],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 20) == 20
    assert candidate(baseCosts = [2, 3],toppingCosts = [4, 5, 100],target = 18) == 17
    assert candidate(baseCosts = [3, 10],toppingCosts = [2, 5],target = 9) == 8
    assert candidate(baseCosts = [4, 8, 12, 16, 20],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 30) == 30
    assert candidate(baseCosts = [50, 75, 100, 125],toppingCosts = [10, 15, 20, 25, 30],target = 300) == 300
    assert candidate(baseCosts = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],toppingCosts = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1023) == 1023
    assert candidate(baseCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 1500) == 1500
    assert candidate(baseCosts = [1234, 5678, 9101],toppingCosts = [111, 222, 333, 444, 555, 666],target = 10000) == 10007
    assert candidate(baseCosts = [5000, 7500, 10000],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 15000) == 15000
    assert candidate(baseCosts = [1000, 2000, 3000, 4000, 5000],toppingCosts = [50, 100, 150, 200, 250, 300, 350],target = 10000) == 7800
    assert candidate(baseCosts = [15, 25, 35, 45],toppingCosts = [2, 4, 6, 8, 10],target = 50) == 49
    assert candidate(baseCosts = [100, 200, 300, 400],toppingCosts = [10, 20, 30, 40, 50],target = 500) == 500
    assert candidate(baseCosts = [123, 456, 789],toppingCosts = [987, 654, 321, 654, 321, 987],target = 1000) == 1086
    assert candidate(baseCosts = [10, 20, 30, 40, 50],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 150) == 150
    assert candidate(baseCosts = [1000, 2000, 3000, 4000, 5000],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 7500) == 7500
    assert candidate(baseCosts = [1, 5, 10, 15],toppingCosts = [3, 6, 9, 12],target = 30) == 30
    assert candidate(baseCosts = [7, 14, 21],toppingCosts = [3, 6, 9, 12, 15, 18],target = 30) == 30
    assert candidate(baseCosts = [500, 1000, 1500],toppingCosts = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500],target = 3000) == 3000
    assert candidate(baseCosts = [1000, 2000],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 5000) == 5000
    assert candidate(baseCosts = [8, 16, 24],toppingCosts = [2, 4, 6, 8, 10, 12, 14, 16],target = 35) == 34
    assert candidate(baseCosts = [1000, 2000, 3000, 4000, 5000],toppingCosts = [100, 200, 300, 400, 500],target = 12345) == 8000
    assert candidate(baseCosts = [3, 6, 9, 12, 15],toppingCosts = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1024) == 1024
    assert candidate(baseCosts = [300, 600, 900],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 1200) == 1200
    assert candidate(baseCosts = [1, 2, 3, 4, 5],toppingCosts = [5, 10, 15, 20, 25],target = 50) == 50
    assert candidate(baseCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 50) == 50
    assert candidate(baseCosts = [100, 200, 300],toppingCosts = [50, 75, 100, 125, 150],target = 600) == 600
    assert candidate(baseCosts = [1, 10000],toppingCosts = [5000, 3000, 2000, 1000, 500, 100],target = 9000) == 9001
    assert candidate(baseCosts = [15, 25, 35],toppingCosts = [5, 7, 11, 13, 17],target = 50) == 50
    assert candidate(baseCosts = [100, 150, 200, 250],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90],target = 750) == 750
    assert candidate(baseCosts = [999, 1999, 2999],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 5000) == 3109
    assert candidate(baseCosts = [1, 1, 1, 1, 1],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 25) == 25
    assert candidate(baseCosts = [150, 250, 350],toppingCosts = [5, 15, 25, 35, 45, 55],target = 400) == 400
    assert candidate(baseCosts = [2000, 4000, 6000],toppingCosts = [100, 200, 300, 400, 500],target = 7000) == 7000
    assert candidate(baseCosts = [1, 10, 100],toppingCosts = [9, 90, 900, 9000],target = 10000) == 10000
    assert candidate(baseCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 1000) == 1000
    assert candidate(baseCosts = [7500, 8000],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 15000) == 15000
    assert candidate(baseCosts = [15, 25, 35, 45],toppingCosts = [1, 2, 3, 4, 5, 6, 7],target = 30) == 30
    assert candidate(baseCosts = [10, 20, 30],toppingCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 45) == 45
    assert candidate(baseCosts = [1, 1, 1, 1, 1],toppingCosts = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],target = 100) == 101
    assert candidate(baseCosts = [1000, 2000, 3000, 4000, 5000],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 10000) == 10000
    assert candidate(baseCosts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 100) == 100
    assert candidate(baseCosts = [5000, 7000, 9000],toppingCosts = [1000, 2000, 3000, 4000],target = 18000) == 18000
    assert candidate(baseCosts = [500, 250],toppingCosts = [100, 200, 300, 400, 500],target = 1000) == 1000
    assert candidate(baseCosts = [10000],toppingCosts = [10000, 10000, 10000, 10000, 10000],target = 50000) == 50000
    assert candidate(baseCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 500) == 210
    assert candidate(baseCosts = [100, 200, 300],toppingCosts = [10, 20, 30, 40, 50, 60],target = 500) == 500
    assert candidate(baseCosts = [1000, 2000, 3000],toppingCosts = [500, 100, 250, 125, 75],target = 4500) == 4500
    assert candidate(baseCosts = [123, 456, 789],toppingCosts = [11, 22, 33, 44, 55, 66, 77, 88, 99],target = 1000) == 998
    assert candidate(baseCosts = [5, 10, 15, 20, 25],toppingCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 20) == 20
    assert candidate(baseCosts = [9999],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 10000) == 10000
    assert candidate(baseCosts = [123, 456, 789],toppingCosts = [987, 654, 321, 123, 456, 789, 100, 200, 300],target = 2000) == 2000
    assert candidate(baseCosts = [500, 501, 502],toppingCosts = [250, 251, 252, 253],target = 1000) == 1000
    assert candidate(baseCosts = [777, 888],toppingCosts = [55, 44, 33, 22, 11, 1, 2, 3, 4, 5],target = 2000) == 1248
    assert candidate(baseCosts = [10, 20, 30, 40, 50],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 25) == 25
    assert candidate(baseCosts = [10, 20, 30, 40, 50],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 50) == 50
    assert candidate(baseCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],toppingCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 10) == 10
    assert candidate(baseCosts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],toppingCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],target = 30) == 30
    assert candidate(baseCosts = [123, 456, 789],toppingCosts = [11, 22, 33, 44, 55],target = 700) == 698
    assert candidate(baseCosts = [100, 200, 300, 400],toppingCosts = [10, 20, 30, 40, 50, 60],target = 750) == 750
    assert candidate(baseCosts = [100, 200],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 500) == 310
    assert candidate(baseCosts = [1000, 1001, 1002, 1003],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 10000) == 1113
    assert candidate(baseCosts = [23, 45, 67, 89, 10],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 200) == 199
    assert candidate(baseCosts = [5, 10, 15, 20],toppingCosts = [1, 3, 5, 7, 9, 11, 13],target = 40) == 40
    assert candidate(baseCosts = [100, 200, 300, 400, 500],toppingCosts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],target = 1000) == 1000
    assert candidate(baseCosts = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],toppingCosts = [2, 4, 6, 8, 10],target = 50) == 49
    assert candidate(baseCosts = [100, 200, 300, 400],toppingCosts = [10, 20, 30, 40, 50, 60],target = 1500) == 820
    assert candidate(baseCosts = [100, 200, 300, 400],toppingCosts = [50, 10, 15, 20, 25, 30, 35, 40, 45, 55],target = 1500) == 1050
    assert candidate(baseCosts = [1, 2, 3, 4, 5],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 100) == 101
    assert candidate(baseCosts = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],toppingCosts = [500, 1500, 2500, 3500],target = 7500) == 7500
    assert candidate(baseCosts = [2000, 3000, 4000, 5000],toppingCosts = [50, 100, 150, 200, 250],target = 8500) == 6500
    assert candidate(baseCosts = [50, 100, 150, 200, 250, 300],toppingCosts = [5, 10, 15, 20, 25, 30],target = 750) == 510
    assert candidate(baseCosts = [100, 200],toppingCosts = [50, 25, 10, 5, 1],target = 300) == 300
    assert candidate(baseCosts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 5000) == 5001
    assert candidate(baseCosts = [1000, 2000, 3000],toppingCosts = [500, 1000, 1500, 2000, 2500],target = 6000) == 6000
    assert candidate(baseCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 50) == 50
    assert candidate(baseCosts = [800, 1600, 2400],toppingCosts = [100, 200, 300, 400, 500, 600],target = 3000) == 3000
    assert candidate(baseCosts = [5000, 10000],toppingCosts = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],target = 20000) == 20000
    assert candidate(baseCosts = [1000, 2000, 3000],toppingCosts = [500, 100, 250, 150, 200],target = 4500) == 4500
    assert candidate(baseCosts = [4, 8, 12, 16, 20],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 45) == 45
    assert candidate(baseCosts = [1, 2, 3, 4, 5],toppingCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],target = 500) == 501
    assert candidate(baseCosts = [50, 60, 70, 80, 90],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 150) == 150
    assert candidate(baseCosts = [100, 200, 300],toppingCosts = [50, 75, 100, 125, 150],target = 500) == 500
    assert candidate(baseCosts = [5000],toppingCosts = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],target = 20000) == 20000
    assert candidate(baseCosts = [10, 20],toppingCosts = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512],target = 1000) == 1000
    assert candidate(baseCosts = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],toppingCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],target = 500) == 210
    assert candidate(baseCosts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],toppingCosts = [9999],target = 10000) == 10000
    assert candidate(baseCosts = [5, 10],toppingCosts = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],target = 15) == 15
    assert candidate(baseCosts = [500, 1000, 1500],toppingCosts = [5, 10, 15, 20, 25, 30, 35, 40],target = 2000) == 1860
    assert candidate(baseCosts = [999, 1000],toppingCosts = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],target = 4000) == 4000


