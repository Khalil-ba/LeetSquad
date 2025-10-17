def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(brackets = [[3, 50], [7, 10], [12, 25]],income = 10) == 2.65
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[3, 50], [7, 10], [12, 25]],income = 10) == 2.65: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[5, 10], [10, 20], [15, 30], [20, 40]],income = 25) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[5, 10], [10, 20], [15, 30], [20, 40]],income = 25) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 20]],income = 50) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 20]],income = 50) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[50, 0], [100, 20], [150, 25]],income = 175) == 22.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[50, 0], [100, 20], [150, 25]],income = 175) == 22.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[1, 100], [2, 50]],income = 1) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[1, 100], [2, 50]],income = 1) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[5, 5], [10, 15], [15, 25]],income = 15) == 2.25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[5, 5], [10, 15], [15, 25]],income = 15) == 2.25: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[1, 100]],income = 1) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[1, 100]],income = 1) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[2, 50]],income = 0) == 0.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[2, 50]],income = 0) == 0.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[1, 100], [2, 0], [3, 50]],income = 1) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[1, 100], [2, 0], [3, 50]],income = 1) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[1, 0], [4, 25], [5, 50]],income = 2) == 0.25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[1, 0], [4, 25], [5, 50]],income = 2) == 0.25: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 10], [20, 20], [30, 30], [40, 40]],income = 35) == 8.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 10], [20, 20], [30, 30], [40, 40]],income = 35) == 8.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[1, 1], [2, 2], [3, 3]],income = 3) == 0.06
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[1, 1], [2, 2], [3, 3]],income = 3) == 0.06: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[1, 100], [2, 50], [3, 25]],income = 1) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[1, 100], [2, 50], [3, 25]],income = 1) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 20], [20, 30], [30, 40]],income = 15) == 3.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 20], [20, 30], [30, 40]],income = 15) == 3.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[5, 50], [10, 30], [15, 20]],income = 12) == 4.4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[5, 50], [10, 30], [15, 20]],income = 12) == 4.4: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[500, 10], [1000, 20]],income = 750) == 100.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[500, 10], [1000, 20]],income = 750) == 100.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 50]],income = 10) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 50]],income = 10) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[50, 10], [100, 20], [150, 30]],income = 75) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[50, 10], [100, 20], [150, 30]],income = 75) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 20], [20, 30], [30, 25]],income = 25) == 6.25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 20], [20, 30], [30, 25]],income = 25) == 6.25: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 5]],income = 100) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 5]],income = 100) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 10]],income = 100) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 10]],income = 100) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 10], [20, 20], [30, 30]],income = 15) == 2.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 10], [20, 20], [30, 30]],income = 15) == 2.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[1, 1], [2, 2], [3, 3], [4, 4]],income = 4) == 0.1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[1, 1], [2, 2], [3, 3], [4, 4]],income = 4) == 0.1: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 10]],income = 50) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 10]],income = 50) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[500, 10], [750, 20], [1000, 30]],income = 1000) == 175.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[500, 10], [750, 20], [1000, 30]],income = 1000) == 175.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[5, 100]],income = 5) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[5, 100]],income = 5) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],income = 5) == 0.15
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],income = 5) == 0.15: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 10], [20, 20], [30, 30]],income = 25) == 4.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 10], [20, 20], [30, 30]],income = 25) == 4.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[3, 0], [6, 10], [9, 20]],income = 9) == 0.9
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[3, 0], [6, 10], [9, 20]],income = 9) == 0.9: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[1, 100], [2, 100], [3, 100]],income = 3) == 3.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[1, 100], [2, 100], [3, 100]],income = 3) == 3.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[50, 10], [100, 20], [200, 30], [500, 40]],income = 400) == 125.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[50, 10], [100, 20], [200, 30], [500, 40]],income = 400) == 125.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 10], [200, 20], [300, 30], [400, 40]],income = 350) == 80.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 10], [200, 20], [300, 30], [400, 40]],income = 350) == 80.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 0], [20, 10], [30, 20], [40, 30], [50, 40], [60, 50]],income = 60) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 0], [20, 10], [30, 20], [40, 30], [50, 40], [60, 50]],income = 60) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],income = 45) == 12.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],income = 45) == 12.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[500, 25], [1000, 30]],income = 800) == 215.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[500, 25], [1000, 30]],income = 800) == 215.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[5, 0], [10, 5], [15, 10], [20, 15], [25, 20]],income = 18) == 1.2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[5, 0], [10, 5], [15, 10], [20, 15], [25, 20]],income = 18) == 1.2: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 5], [20, 10], [30, 15], [40, 20]],income = 25) == 2.25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 5], [20, 10], [30, 15], [40, 20]],income = 25) == 2.25: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[500, 0], [1000, 20], [1500, 40]],income = 2000) == 300.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[500, 0], [1000, 20], [1500, 40]],income = 2000) == 300.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[50, 1], [100, 2], [150, 3], [200, 4], [250, 5]],income = 100) == 1.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[50, 1], [100, 2], [150, 3], [200, 4], [250, 5]],income = 100) == 1.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[5, 25], [15, 50], [25, 75], [35, 100]],income = 35) == 23.75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[5, 25], [15, 50], [25, 75], [35, 100]],income = 35) == 23.75: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[2, 50], [4, 75], [6, 100], [8, 125], [10, 150]],income = 10) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[2, 50], [4, 75], [6, 100], [8, 125], [10, 150]],income = 10) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 25], [200, 30], [300, 35]],income = 250) == 72.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 25], [200, 30], [300, 35]],income = 250) == 72.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90], [10, 100]],income = 10) == 5.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90], [10, 100]],income = 10) == 5.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 0], [20, 5], [30, 10], [40, 15], [50, 20], [60, 25]],income = 55) == 6.25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 0], [20, 5], [30, 10], [40, 15], [50, 20], [60, 25]],income = 55) == 6.25: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 5], [200, 10], [300, 15], [400, 20], [500, 25]],income = 500) == 75.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 5], [200, 10], [300, 15], [400, 20], [500, 25]],income = 500) == 75.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 10], [20, 20], [30, 30], [40, 40]],income = 25) == 4.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 10], [20, 20], [30, 30], [40, 40]],income = 25) == 4.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 10], [200, 20], [300, 30], [400, 40], [500, 50], [600, 60], [700, 70], [800, 80], [900, 90], [1000, 100]],income = 1000) == 550.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 10], [200, 20], [300, 30], [400, 40], [500, 50], [600, 60], [700, 70], [800, 80], [900, 90], [1000, 100]],income = 1000) == 550.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[150, 5], [250, 10], [350, 15], [450, 20], [550, 25]],income = 600) == 77.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[150, 5], [250, 10], [350, 15], [450, 20], [550, 25]],income = 600) == 77.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[500, 10], [1000, 15], [1500, 20], [2000, 25], [2500, 30]],income = 2200) == 410.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[500, 10], [1000, 15], [1500, 20], [2000, 25], [2500, 30]],income = 2200) == 410.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],income = 45) == 1.25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],income = 45) == 1.25: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 5], [150, 10], [200, 15], [250, 20], [300, 25], [350, 30], [400, 35], [450, 40], [500, 45]],income = 499) == 114.55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 5], [150, 10], [200, 15], [250, 20], [300, 25], [350, 30], [400, 35], [450, 40], [500, 45]],income = 499) == 114.55: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 15], [200, 25], [300, 35], [400, 45]],income = 350) == 97.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 15], [200, 25], [300, 35], [400, 45]],income = 350) == 97.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[500, 1], [1000, 2]],income = 750) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[500, 1], [1000, 2]],income = 750) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[50, 5], [150, 15], [300, 25]],income = 200) == 30.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[50, 5], [150, 15], [300, 25]],income = 200) == 30.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[50, 15], [100, 20], [150, 25], [200, 30]],income = 175) == 37.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[50, 15], [100, 20], [150, 25], [200, 30]],income = 175) == 37.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 50], [20, 75], [30, 100]],income = 10) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 50], [20, 75], [30, 100]],income = 10) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30], [70, 35]],income = 65) == 12.25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30], [70, 35]],income = 65) == 12.25: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[1, 100]],income = 1000) == 1.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[1, 100]],income = 1000) == 1.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[5, 10], [15, 20], [25, 30], [35, 40], [45, 50], [55, 60], [65, 70], [75, 80], [85, 90], [95, 100]],income = 100) == 54.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[5, 10], [15, 20], [25, 30], [35, 40], [45, 50], [55, 60], [65, 70], [75, 80], [85, 90], [95, 100]],income = 100) == 54.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[200, 10], [400, 20], [600, 30], [800, 40], [1000, 50]],income = 750) == 180.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[200, 10], [400, 20], [600, 30], [800, 40], [1000, 50]],income = 750) == 180.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 0], [200, 5], [300, 10], [400, 15], [500, 20]],income = 0) == 0.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 0], [200, 5], [300, 10], [400, 15], [500, 20]],income = 0) == 0.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30], [70, 35], [80, 40], [90, 45], [100, 50]],income = 30) == 3.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30], [70, 35], [80, 40], [90, 45], [100, 50]],income = 30) == 3.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 10], [200, 20], [300, 30], [400, 40], [500, 50]],income = 450) == 125.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 10], [200, 20], [300, 30], [400, 40], [500, 50]],income = 450) == 125.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 5], [200, 10], [300, 15], [400, 20], [500, 25], [600, 30], [700, 35], [800, 40], [900, 45], [1000, 50]],income = 800) == 180.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 5], [200, 10], [300, 15], [400, 20], [500, 25], [600, 30], [700, 35], [800, 40], [900, 45], [1000, 50]],income = 800) == 180.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 25], [20, 25], [30, 25], [40, 25], [50, 25]],income = 40) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 25], [20, 25], [30, 25], [40, 25], [50, 25]],income = 40) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],income = 25) == 0.45
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],income = 25) == 0.45: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 100], [20, 100], [30, 100], [40, 100], [50, 100]],income = 45) == 45.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 100], [20, 100], [30, 100], [40, 100], [50, 100]],income = 45) == 45.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[50, 0], [100, 10], [150, 20], [200, 30], [250, 40]],income = 250) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[50, 0], [100, 10], [150, 20], [200, 30], [250, 40]],income = 250) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10]],income = 5) == 0.3
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10]],income = 5) == 0.3: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5]],income = 400) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5]],income = 400) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 10], [50, 20], [100, 30], [200, 40], [500, 50]],income = 600) == 214.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 10], [50, 20], [100, 30], [200, 40], [500, 50]],income = 600) == 214.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[50, 1], [100, 2], [150, 3], [200, 4], [250, 5], [300, 6]],income = 175) == 4.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[50, 1], [100, 2], [150, 3], [200, 4], [250, 5], [300, 6]],income = 175) == 4.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[15, 0], [30, 10], [45, 20], [60, 30], [75, 40]],income = 70) == 13.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[15, 0], [30, 10], [45, 20], [60, 30], [75, 40]],income = 70) == 13.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 50], [20, 40], [30, 30], [40, 20], [50, 10]],income = 50) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 50], [20, 40], [30, 30], [40, 20], [50, 10]],income = 50) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 50], [20, 40], [30, 30], [40, 20], [50, 10]],income = 45) == 14.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 50], [20, 40], [30, 30], [40, 20], [50, 10]],income = 45) == 14.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[50, 0], [100, 5], [150, 10], [200, 15], [250, 20], [300, 25]],income = 120) == 4.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[50, 0], [100, 5], [150, 10], [200, 15], [250, 20], [300, 25]],income = 120) == 4.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 25], [20, 25], [30, 25], [40, 25], [50, 25], [60, 25], [70, 25], [80, 25], [90, 25], [100, 25]],income = 95) == 23.75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 25], [20, 25], [30, 25], [40, 25], [50, 25], [60, 25], [70, 25], [80, 25], [90, 25], [100, 25]],income = 95) == 23.75: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 50], [20, 50], [30, 50], [40, 50], [50, 50], [60, 50], [70, 50], [80, 50], [90, 50], [100, 50]],income = 55) == 27.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 50], [20, 50], [30, 50], [40, 50], [50, 50], [60, 50], [70, 50], [80, 50], [90, 50], [100, 50]],income = 55) == 27.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],income = 100) == 5.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],income = 100) == 5.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[1000, 100]],income = 1000) == 1000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[1000, 100]],income = 1000) == 1000.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30], [70, 35], [80, 40], [90, 45], [100, 50]],income = 85) == 20.25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30], [70, 35], [80, 40], [90, 45], [100, 50]],income = 85) == 20.25: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 0], [20, 0], [30, 0], [40, 0], [50, 0]],income = 50) == 0.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 0], [20, 0], [30, 0], [40, 0], [50, 0]],income = 50) == 0.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[5, 10], [15, 15], [25, 20], [35, 25], [45, 30]],income = 30) == 5.25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[5, 10], [15, 15], [25, 20], [35, 25], [45, 30]],income = 30) == 5.25: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 5], [20, 10], [30, 15]],income = 5) == 0.25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 5], [20, 10], [30, 15]],income = 5) == 0.25: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[50, 10], [100, 20], [150, 30], [200, 40], [250, 50]],income = 300) == 75.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[50, 10], [100, 20], [150, 30], [200, 40], [250, 50]],income = 300) == 75.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[50, 10], [100, 20], [150, 30], [200, 40], [250, 50]],income = 220) == 60.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[50, 10], [100, 20], [150, 30], [200, 40], [250, 50]],income = 220) == 60.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[2, 5], [5, 10], [10, 20], [20, 30], [50, 40]],income = 30) == 8.4
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[2, 5], [5, 10], [10, 20], [20, 30], [50, 40]],income = 30) == 8.4: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 0], [20, 10], [30, 20], [40, 30], [50, 40], [60, 50], [70, 60], [80, 70], [90, 80], [100, 90]],income = 95) == 40.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 0], [20, 10], [30, 20], [40, 30], [50, 40], [60, 50], [70, 60], [80, 70], [90, 80], [100, 90]],income = 95) == 40.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[300, 5], [600, 10], [900, 15]],income = 900) == 90.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[300, 5], [600, 10], [900, 15]],income = 900) == 90.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 10], [200, 20], [300, 30], [400, 40], [500, 50], [600, 60]],income = 650) == 210.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 10], [200, 20], [300, 30], [400, 40], [500, 50], [600, 60]],income = 650) == 210.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[5, 0], [10, 10], [15, 20], [20, 30], [25, 40]],income = 25) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[5, 0], [10, 10], [15, 20], [20, 30], [25, 40]],income = 25) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 15], [200, 25], [300, 35], [400, 45], [500, 55]],income = 600) == 175.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 15], [200, 25], [300, 35], [400, 45], [500, 55]],income = 600) == 175.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 100], [20, 90], [30, 80], [40, 70], [50, 60]],income = 15) == 14.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 100], [20, 90], [30, 80], [40, 70], [50, 60]],income = 15) == 14.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[200, 15], [400, 25], [600, 30]],income = 550) == 125.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[200, 15], [400, 25], [600, 30]],income = 550) == 125.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 25], [20, 35], [30, 45], [40, 55], [50, 65]],income = 35) == 13.25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 25], [20, 35], [30, 45], [40, 55], [50, 65]],income = 35) == 13.25: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 15], [20, 25], [30, 35], [40, 45], [50, 55]],income = 50) == 17.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 15], [20, 25], [30, 35], [40, 45], [50, 55]],income = 50) == 17.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[500, 1], [1000, 2], [1500, 3], [2000, 4], [2500, 5]],income = 2400) == 70.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[500, 1], [1000, 2], [1500, 3], [2000, 4], [2500, 5]],income = 2400) == 70.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[1, 100], [2, 90], [3, 80], [4, 70], [5, 60]],income = 5) == 4.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[1, 100], [2, 90], [3, 80], [4, 70], [5, 60]],income = 5) == 4.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 0], [20, 5], [30, 10], [40, 15], [50, 20], [60, 25], [70, 30], [80, 35], [90, 40], [100, 45]],income = 50) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 0], [20, 5], [30, 10], [40, 15], [50, 20], [60, 25], [70, 30], [80, 35], [90, 40], [100, 45]],income = 50) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[30, 5], [60, 10], [90, 15], [120, 20], [150, 25]],income = 150) == 22.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[30, 5], [60, 10], [90, 15], [120, 20], [150, 25]],income = 150) == 22.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]],income = 100) == 55.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]],income = 100) == 55.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 0], [20, 5], [30, 10], [40, 15], [50, 20]],income = 40) == 3.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 0], [20, 5], [30, 10], [40, 15], [50, 20]],income = 40) == 3.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],income = 10) == 0.55
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],income = 10) == 0.55: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 0], [200, 50], [300, 100], [400, 150]],income = 400) == 300.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 0], [200, 50], [300, 100], [400, 150]],income = 400) == 300.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[50, 5], [150, 10], [250, 15], [350, 20], [450, 25], [550, 30]],income = 300) == 37.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[50, 5], [150, 10], [250, 15], [350, 20], [450, 25], [550, 30]],income = 300) == 37.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 100], [20, 0], [30, 100], [40, 0]],income = 35) == 20.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 100], [20, 0], [30, 100], [40, 0]],income = 35) == 20.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[5, 10], [15, 20], [25, 30], [35, 40], [45, 50], [55, 60]],income = 55) == 20.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[5, 10], [15, 20], [25, 30], [35, 40], [45, 50], [55, 60]],income = 55) == 20.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 10], [200, 20], [300, 30], [400, 40], [500, 50]],income = 500) == 150.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 10], [200, 20], [300, 30], [400, 40], [500, 50]],income = 500) == 150.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30], [70, 35], [80, 40], [90, 45], [100, 50]],income = 100) == 27.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30], [70, 35], [80, 40], [90, 45], [100, 50]],income = 100) == 27.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[50, 5], [150, 15], [250, 25], [350, 35], [450, 45]],income = 450) == 122.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[50, 5], [150, 15], [250, 25], [350, 35], [450, 45]],income = 450) == 122.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[200, 10], [500, 20], [800, 30], [1000, 40]],income = 750) == 155.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[200, 10], [500, 20], [800, 30], [1000, 40]],income = 750) == 155.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 0], [200, 0], [300, 0], [400, 0], [500, 0]],income = 500) == 0.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 0], [200, 0], [300, 0], [400, 0], [500, 0]],income = 500) == 0.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 5], [200, 10], [300, 15], [400, 20], [500, 25], [600, 30]],income = 600) == 105.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 5], [200, 10], [300, 15], [400, 20], [500, 25], [600, 30]],income = 600) == 105.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 0], [200, 5], [300, 10], [400, 15], [500, 20], [600, 25]],income = 150) == 2.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 0], [200, 5], [300, 10], [400, 15], [500, 20], [600, 25]],income = 150) == 2.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60]],income = 6) == 2.1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60]],income = 6) == 2.1: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25]],income = 45) == 6.25
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25]],income = 45) == 6.25: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],income = 35) == 8.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],income = 35) == 8.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[1, 100], [10, 90], [100, 80], [1000, 70]],income = 500) == 361.1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[1, 100], [10, 90], [100, 80], [1000, 70]],income = 500) == 361.1: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 5], [200, 10], [300, 15], [400, 20], [500, 25], [600, 30], [700, 35], [800, 40], [900, 45], [1000, 50]],income = 950) == 250.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 5], [200, 10], [300, 15], [400, 20], [500, 25], [600, 30], [700, 35], [800, 40], [900, 45], [1000, 50]],income = 950) == 250.0: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[50, 5], [100, 15], [200, 25], [300, 35]],income = 250) == 52.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[50, 5], [100, 15], [200, 25], [300, 35]],income = 250) == 52.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[100, 5], [200, 10], [300, 15], [400, 20], [500, 25], [600, 30], [700, 35], [800, 40], [900, 45], [1000, 50]],income = 999) == 274.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[100, 5], [200, 10], [300, 15], [400, 20], [500, 25], [600, 30], [700, 35], [800, 40], [900, 45], [1000, 50]],income = 999) == 274.5: {e}')
    
    total += 1
    try:
        result = candidate(brackets = [[5, 10], [10, 20], [15, 30], [20, 40], [25, 50]],income = 18) == 4.2
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(brackets = [[5, 10], [10, 20], [15, 30], [20, 40], [25, 50]],income = 18) == 4.2: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(brackets = [[3, 50], [7, 10], [12, 25]],income = 10) == 2.65
    assert candidate(brackets = [[5, 10], [10, 20], [15, 30], [20, 40]],income = 25) == 5.0
    assert candidate(brackets = [[100, 20]],income = 50) == 10.0
    assert candidate(brackets = [[50, 0], [100, 20], [150, 25]],income = 175) == 22.5
    assert candidate(brackets = [[1, 100], [2, 50]],income = 1) == 1.0
    assert candidate(brackets = [[5, 5], [10, 15], [15, 25]],income = 15) == 2.25
    assert candidate(brackets = [[1, 100]],income = 1) == 1.0
    assert candidate(brackets = [[2, 50]],income = 0) == 0.0
    assert candidate(brackets = [[1, 100], [2, 0], [3, 50]],income = 1) == 1.0
    assert candidate(brackets = [[1, 0], [4, 25], [5, 50]],income = 2) == 0.25
    assert candidate(brackets = [[10, 10], [20, 20], [30, 30], [40, 40]],income = 35) == 8.0
    assert candidate(brackets = [[1, 1], [2, 2], [3, 3]],income = 3) == 0.06
    assert candidate(brackets = [[1, 100], [2, 50], [3, 25]],income = 1) == 1.0
    assert candidate(brackets = [[10, 20], [20, 30], [30, 40]],income = 15) == 3.5
    assert candidate(brackets = [[5, 50], [10, 30], [15, 20]],income = 12) == 4.4
    assert candidate(brackets = [[500, 10], [1000, 20]],income = 750) == 100.0
    assert candidate(brackets = [[10, 50]],income = 10) == 5.0
    assert candidate(brackets = [[50, 10], [100, 20], [150, 30]],income = 75) == 10.0
    assert candidate(brackets = [[10, 20], [20, 30], [30, 25]],income = 25) == 6.25
    assert candidate(brackets = [[100, 5]],income = 100) == 5.0
    assert candidate(brackets = [[100, 10]],income = 100) == 10.0
    assert candidate(brackets = [[10, 10], [20, 20], [30, 30]],income = 15) == 2.0
    assert candidate(brackets = [[1, 1], [2, 2], [3, 3], [4, 4]],income = 4) == 0.1
    assert candidate(brackets = [[100, 10]],income = 50) == 5.0
    assert candidate(brackets = [[500, 10], [750, 20], [1000, 30]],income = 1000) == 175.0
    assert candidate(brackets = [[5, 100]],income = 5) == 5.0
    assert candidate(brackets = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],income = 5) == 0.15
    assert candidate(brackets = [[10, 10], [20, 20], [30, 30]],income = 25) == 4.5
    assert candidate(brackets = [[3, 0], [6, 10], [9, 20]],income = 9) == 0.9
    assert candidate(brackets = [[1, 100], [2, 100], [3, 100]],income = 3) == 3.0
    assert candidate(brackets = [[50, 10], [100, 20], [200, 30], [500, 40]],income = 400) == 125.0
    assert candidate(brackets = [[100, 10], [200, 20], [300, 30], [400, 40]],income = 350) == 80.0
    assert candidate(brackets = [[10, 0], [20, 10], [30, 20], [40, 30], [50, 40], [60, 50]],income = 60) == 15.0
    assert candidate(brackets = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],income = 45) == 12.5
    assert candidate(brackets = [[500, 25], [1000, 30]],income = 800) == 215.0
    assert candidate(brackets = [[5, 0], [10, 5], [15, 10], [20, 15], [25, 20]],income = 18) == 1.2
    assert candidate(brackets = [[10, 5], [20, 10], [30, 15], [40, 20]],income = 25) == 2.25
    assert candidate(brackets = [[500, 0], [1000, 20], [1500, 40]],income = 2000) == 300.0
    assert candidate(brackets = [[50, 1], [100, 2], [150, 3], [200, 4], [250, 5]],income = 100) == 1.5
    assert candidate(brackets = [[5, 25], [15, 50], [25, 75], [35, 100]],income = 35) == 23.75
    assert candidate(brackets = [[2, 50], [4, 75], [6, 100], [8, 125], [10, 150]],income = 10) == 10.0
    assert candidate(brackets = [[100, 25], [200, 30], [300, 35]],income = 250) == 72.5
    assert candidate(brackets = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60], [7, 70], [8, 80], [9, 90], [10, 100]],income = 10) == 5.5
    assert candidate(brackets = [[10, 0], [20, 5], [30, 10], [40, 15], [50, 20], [60, 25]],income = 55) == 6.25
    assert candidate(brackets = [[100, 5], [200, 10], [300, 15], [400, 20], [500, 25]],income = 500) == 75.0
    assert candidate(brackets = [[10, 10], [20, 20], [30, 30], [40, 40]],income = 25) == 4.5
    assert candidate(brackets = [[100, 10], [200, 20], [300, 30], [400, 40], [500, 50], [600, 60], [700, 70], [800, 80], [900, 90], [1000, 100]],income = 1000) == 550.0
    assert candidate(brackets = [[150, 5], [250, 10], [350, 15], [450, 20], [550, 25]],income = 600) == 77.5
    assert candidate(brackets = [[500, 10], [1000, 15], [1500, 20], [2000, 25], [2500, 30]],income = 2200) == 410.0
    assert candidate(brackets = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],income = 45) == 1.25
    assert candidate(brackets = [[100, 5], [150, 10], [200, 15], [250, 20], [300, 25], [350, 30], [400, 35], [450, 40], [500, 45]],income = 499) == 114.55
    assert candidate(brackets = [[100, 15], [200, 25], [300, 35], [400, 45]],income = 350) == 97.5
    assert candidate(brackets = [[500, 1], [1000, 2]],income = 750) == 10.0
    assert candidate(brackets = [[50, 5], [150, 15], [300, 25]],income = 200) == 30.0
    assert candidate(brackets = [[50, 15], [100, 20], [150, 25], [200, 30]],income = 175) == 37.5
    assert candidate(brackets = [[10, 50], [20, 75], [30, 100]],income = 10) == 5.0
    assert candidate(brackets = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30], [70, 35]],income = 65) == 12.25
    assert candidate(brackets = [[1, 100]],income = 1000) == 1.0
    assert candidate(brackets = [[5, 10], [15, 20], [25, 30], [35, 40], [45, 50], [55, 60], [65, 70], [75, 80], [85, 90], [95, 100]],income = 100) == 54.5
    assert candidate(brackets = [[200, 10], [400, 20], [600, 30], [800, 40], [1000, 50]],income = 750) == 180.0
    assert candidate(brackets = [[100, 0], [200, 5], [300, 10], [400, 15], [500, 20]],income = 0) == 0.0
    assert candidate(brackets = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30], [70, 35], [80, 40], [90, 45], [100, 50]],income = 30) == 3.0
    assert candidate(brackets = [[100, 10], [200, 20], [300, 30], [400, 40], [500, 50]],income = 450) == 125.0
    assert candidate(brackets = [[100, 5], [200, 10], [300, 15], [400, 20], [500, 25], [600, 30], [700, 35], [800, 40], [900, 45], [1000, 50]],income = 800) == 180.0
    assert candidate(brackets = [[10, 25], [20, 25], [30, 25], [40, 25], [50, 25]],income = 40) == 10.0
    assert candidate(brackets = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],income = 25) == 0.45
    assert candidate(brackets = [[10, 100], [20, 100], [30, 100], [40, 100], [50, 100]],income = 45) == 45.0
    assert candidate(brackets = [[50, 0], [100, 10], [150, 20], [200, 30], [250, 40]],income = 250) == 50.0
    assert candidate(brackets = [[1, 2], [2, 4], [3, 6], [4, 8], [5, 10]],income = 5) == 0.3
    assert candidate(brackets = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5]],income = 400) == 10.0
    assert candidate(brackets = [[10, 10], [50, 20], [100, 30], [200, 40], [500, 50]],income = 600) == 214.0
    assert candidate(brackets = [[50, 1], [100, 2], [150, 3], [200, 4], [250, 5], [300, 6]],income = 175) == 4.0
    assert candidate(brackets = [[15, 0], [30, 10], [45, 20], [60, 30], [75, 40]],income = 70) == 13.0
    assert candidate(brackets = [[10, 50], [20, 40], [30, 30], [40, 20], [50, 10]],income = 50) == 15.0
    assert candidate(brackets = [[10, 50], [20, 40], [30, 30], [40, 20], [50, 10]],income = 45) == 14.5
    assert candidate(brackets = [[50, 0], [100, 5], [150, 10], [200, 15], [250, 20], [300, 25]],income = 120) == 4.5
    assert candidate(brackets = [[10, 25], [20, 25], [30, 25], [40, 25], [50, 25], [60, 25], [70, 25], [80, 25], [90, 25], [100, 25]],income = 95) == 23.75
    assert candidate(brackets = [[10, 50], [20, 50], [30, 50], [40, 50], [50, 50], [60, 50], [70, 50], [80, 50], [90, 50], [100, 50]],income = 55) == 27.5
    assert candidate(brackets = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],income = 100) == 5.5
    assert candidate(brackets = [[1000, 100]],income = 1000) == 1000.0
    assert candidate(brackets = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30], [70, 35], [80, 40], [90, 45], [100, 50]],income = 85) == 20.25
    assert candidate(brackets = [[10, 0], [20, 0], [30, 0], [40, 0], [50, 0]],income = 50) == 0.0
    assert candidate(brackets = [[5, 10], [15, 15], [25, 20], [35, 25], [45, 30]],income = 30) == 5.25
    assert candidate(brackets = [[10, 5], [20, 10], [30, 15]],income = 5) == 0.25
    assert candidate(brackets = [[50, 10], [100, 20], [150, 30], [200, 40], [250, 50]],income = 300) == 75.0
    assert candidate(brackets = [[50, 10], [100, 20], [150, 30], [200, 40], [250, 50]],income = 220) == 60.0
    assert candidate(brackets = [[2, 5], [5, 10], [10, 20], [20, 30], [50, 40]],income = 30) == 8.4
    assert candidate(brackets = [[10, 0], [20, 10], [30, 20], [40, 30], [50, 40], [60, 50], [70, 60], [80, 70], [90, 80], [100, 90]],income = 95) == 40.5
    assert candidate(brackets = [[300, 5], [600, 10], [900, 15]],income = 900) == 90.0
    assert candidate(brackets = [[100, 10], [200, 20], [300, 30], [400, 40], [500, 50], [600, 60]],income = 650) == 210.0
    assert candidate(brackets = [[5, 0], [10, 10], [15, 20], [20, 30], [25, 40]],income = 25) == 5.0
    assert candidate(brackets = [[100, 15], [200, 25], [300, 35], [400, 45], [500, 55]],income = 600) == 175.0
    assert candidate(brackets = [[10, 100], [20, 90], [30, 80], [40, 70], [50, 60]],income = 15) == 14.5
    assert candidate(brackets = [[200, 15], [400, 25], [600, 30]],income = 550) == 125.0
    assert candidate(brackets = [[10, 25], [20, 35], [30, 45], [40, 55], [50, 65]],income = 35) == 13.25
    assert candidate(brackets = [[10, 15], [20, 25], [30, 35], [40, 45], [50, 55]],income = 50) == 17.5
    assert candidate(brackets = [[500, 1], [1000, 2], [1500, 3], [2000, 4], [2500, 5]],income = 2400) == 70.0
    assert candidate(brackets = [[1, 100], [2, 90], [3, 80], [4, 70], [5, 60]],income = 5) == 4.0
    assert candidate(brackets = [[10, 0], [20, 5], [30, 10], [40, 15], [50, 20], [60, 25], [70, 30], [80, 35], [90, 40], [100, 45]],income = 50) == 5.0
    assert candidate(brackets = [[30, 5], [60, 10], [90, 15], [120, 20], [150, 25]],income = 150) == 22.5
    assert candidate(brackets = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]],income = 100) == 55.0
    assert candidate(brackets = [[10, 0], [20, 5], [30, 10], [40, 15], [50, 20]],income = 40) == 3.0
    assert candidate(brackets = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],income = 10) == 0.55
    assert candidate(brackets = [[100, 0], [200, 50], [300, 100], [400, 150]],income = 400) == 300.0
    assert candidate(brackets = [[50, 5], [150, 10], [250, 15], [350, 20], [450, 25], [550, 30]],income = 300) == 37.5
    assert candidate(brackets = [[10, 100], [20, 0], [30, 100], [40, 0]],income = 35) == 20.0
    assert candidate(brackets = [[5, 10], [15, 20], [25, 30], [35, 40], [45, 50], [55, 60]],income = 55) == 20.5
    assert candidate(brackets = [[100, 10], [200, 20], [300, 30], [400, 40], [500, 50]],income = 500) == 150.0
    assert candidate(brackets = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25], [60, 30], [70, 35], [80, 40], [90, 45], [100, 50]],income = 100) == 27.5
    assert candidate(brackets = [[50, 5], [150, 15], [250, 25], [350, 35], [450, 45]],income = 450) == 122.5
    assert candidate(brackets = [[200, 10], [500, 20], [800, 30], [1000, 40]],income = 750) == 155.0
    assert candidate(brackets = [[100, 0], [200, 0], [300, 0], [400, 0], [500, 0]],income = 500) == 0.0
    assert candidate(brackets = [[100, 5], [200, 10], [300, 15], [400, 20], [500, 25], [600, 30]],income = 600) == 105.0
    assert candidate(brackets = [[100, 0], [200, 5], [300, 10], [400, 15], [500, 20], [600, 25]],income = 150) == 2.5
    assert candidate(brackets = [[1, 10], [2, 20], [3, 30], [4, 40], [5, 50], [6, 60]],income = 6) == 2.1
    assert candidate(brackets = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25]],income = 45) == 6.25
    assert candidate(brackets = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],income = 35) == 8.0
    assert candidate(brackets = [[1, 100], [10, 90], [100, 80], [1000, 70]],income = 500) == 361.1
    assert candidate(brackets = [[100, 5], [200, 10], [300, 15], [400, 20], [500, 25], [600, 30], [700, 35], [800, 40], [900, 45], [1000, 50]],income = 950) == 250.0
    assert candidate(brackets = [[50, 5], [100, 15], [200, 25], [300, 35]],income = 250) == 52.5
    assert candidate(brackets = [[100, 5], [200, 10], [300, 15], [400, 20], [500, 25], [600, 30], [700, 35], [800, 40], [900, 45], [1000, 50]],income = 999) == 274.5
    assert candidate(brackets = [[5, 10], [10, 20], [15, 30], [20, 40], [25, 50]],income = 18) == 4.2


