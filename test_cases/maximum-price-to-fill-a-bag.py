def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(items = [[50, 1], [10, 8]],capacity = 5) == 55.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[50, 1], [10, 8]],capacity = 5) == 55.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 10000], [10000, 1]],capacity = 5000) == 10000.4999
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 10000], [10000, 1]],capacity = 5000) == 10000.4999: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [1, 1], [1, 1]],capacity = 2) == 2.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [1, 1], [1, 1]],capacity = 2) == 2.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[20, 1], [30, 2], [10, 1]],capacity = 4) == 60.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[20, 1], [30, 2], [10, 1]],capacity = 4) == 60.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 30]],capacity = 50) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 30]],capacity = 50) == -1: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 1], [5, 1], [5, 1]],capacity = 3) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 1], [5, 1], [5, 1]],capacity = 3) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 100], [2, 200], [3, 300]],capacity = 150) == 1.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 100], [2, 200], [3, 300]],capacity = 150) == 1.5: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 2], [5, 3], [15, 5]],capacity = 10) == 30.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 2], [5, 3], [15, 5]],capacity = 10) == 30.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 5], [10, 10], [15, 15]],capacity = 30) == 30.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 5], [10, 10], [15, 15]],capacity = 30) == 30.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 2], [20, 3], [30, 5]],capacity = 10) == 60.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 2], [20, 3], [30, 5]],capacity = 10) == 60.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [2, 2], [3, 3]],capacity = 3) == 3.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [2, 2], [3, 3]],capacity = 3) == 3.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[20, 5], [30, 10], [5, 1]],capacity = 12) == 43.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[20, 5], [30, 10], [5, 1]],capacity = 12) == 43.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 5], [20, 10], [30, 15]],capacity = 20) == 40.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 5], [20, 10], [30, 15]],capacity = 20) == 40.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 10], [10, 20], [15, 30]],capacity = 50) == 25.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 10], [10, 20], [15, 30]],capacity = 50) == 25.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 10], [7, 5], [8, 4]],capacity = 15) == 18.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 10], [7, 5], [8, 4]],capacity = 15) == 18.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 2], [20, 5], [30, 10]],capacity = 7) == 30.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 2], [20, 5], [30, 10]],capacity = 7) == 30.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[500, 100], [300, 60], [100, 20], [200, 40]],capacity = 150) == 750.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[500, 100], [300, 60], [100, 20], [200, 40]],capacity = 150) == 750.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[30, 10], [20, 5], [50, 20], [40, 15]],capacity = 40) == 115.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[30, 10], [20, 5], [50, 20], [40, 15]],capacity = 40) == 115.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 9999], [2, 9998], [3, 9997], [4, 9996], [5, 9995]],capacity = 25000) == 10.503150945283585
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 9999], [2, 9998], [3, 9997], [4, 9996], [5, 9995]],capacity = 25000) == 10.503150945283585: {e}')
    
    total += 1
    try:
        result = candidate(items = [[40, 4], [25, 3], [10, 2], [15, 1]],capacity = 10) == 90.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[40, 4], [25, 3], [10, 2], [15, 1]],capacity = 10) == 90.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[123, 456], [789, 1011], [1213, 1415], [1617, 1819], [2021, 2223]],capacity = 500) == 454.565901934323
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[123, 456], [789, 1011], [1213, 1415], [1617, 1819], [2021, 2223]],capacity = 500) == 454.565901934323: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 50], [200, 100], [300, 150], [400, 200], [500, 250]],capacity = 600) == 1200.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 50], [200, 100], [300, 150], [400, 200], [500, 250]],capacity = 600) == 1200.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 20], [20, 40], [30, 60], [40, 80], [50, 100]],capacity = 50) == 25.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 20], [20, 40], [30, 60], [40, 80], [50, 100]],capacity = 50) == 25.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[9999, 1000], [8888, 2000], [7777, 3000], [6666, 4000], [5555, 5000]],capacity = 10000) == 33330.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[9999, 1000], [8888, 2000], [7777, 3000], [6666, 4000], [5555, 5000]],capacity = 10000) == 33330.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 10], [200, 20], [150, 15], [50, 5]],capacity = 40) == 400.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 10], [200, 20], [150, 15], [50, 5]],capacity = 40) == 400.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],capacity = 15) == 1500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],capacity = 15) == 1500.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[2, 1], [4, 2], [6, 3], [8, 4], [10, 5], [12, 6], [14, 7], [16, 8], [18, 9], [20, 10], [22, 11], [24, 12], [26, 13], [28, 14], [30, 15]],capacity = 75) == 150.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[2, 1], [4, 2], [6, 3], [8, 4], [10, 5], [12, 6], [14, 7], [16, 8], [18, 9], [20, 10], [22, 11], [24, 12], [26, 13], [28, 14], [30, 15]],capacity = 75) == 150.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[9999, 1000], [8888, 900], [7777, 800], [6666, 700], [5555, 600], [4444, 500]],capacity = 5000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[9999, 1000], [8888, 900], [7777, 800], [6666, 700], [5555, 600], [4444, 500]],capacity = 5000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(items = [[40, 20], [25, 15], [15, 10], [10, 5]],capacity = 50) == 90.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[40, 20], [25, 15], [15, 10], [10, 5]],capacity = 50) == 90.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 2], [20, 5], [30, 7], [40, 10]],capacity = 20) == 84.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 2], [20, 5], [30, 7], [40, 10]],capacity = 20) == 84.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]],capacity = 500) == 500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]],capacity = 500) == 500.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],capacity = 10) == 100.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],capacity = 10) == 100.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 10], [90, 9], [80, 8], [70, 7], [60, 6], [50, 5], [40, 4], [30, 3], [20, 2], [10, 1]],capacity = 50) == 500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 10], [90, 9], [80, 8], [70, 7], [60, 6], [50, 5], [40, 4], [30, 3], [20, 2], [10, 1]],capacity = 50) == 500.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[500, 100], [100, 20], [200, 40], [300, 60]],capacity = 150) == 750.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[500, 100], [100, 20], [200, 40], [300, 60]],capacity = 150) == 750.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 50], [200, 100], [300, 150], [400, 200], [500, 250]],capacity = 100) == 200.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 50], [200, 100], [300, 150], [400, 200], [500, 250]],capacity = 100) == 200.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[25, 10], [20, 8], [15, 6], [10, 4], [5, 2]],capacity = 20) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[25, 10], [20, 8], [15, 6], [10, 4], [5, 2]],capacity = 20) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],capacity = 15) == 150.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],capacity = 15) == 150.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 1], [10, 2], [15, 3], [20, 4], [25, 5], [30, 6], [35, 7], [40, 8], [45, 9], [50, 10]],capacity = 45) == 225.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 1], [10, 2], [15, 3], [20, 4], [25, 5], [30, 6], [35, 7], [40, 8], [45, 9], [50, 10]],capacity = 45) == 225.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000, 1000], [2000, 2000], [3000, 3000], [4000, 4000], [5000, 5000], [6000, 6000], [7000, 7000], [8000, 8000], [9000, 9000], [10000, 10000]],capacity = 15000) == 15000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000, 1000], [2000, 2000], [3000, 3000], [4000, 4000], [5000, 5000], [6000, 6000], [7000, 7000], [8000, 8000], [9000, 9000], [10000, 10000]],capacity = 15000) == 15000.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000, 1000], [500, 500], [250, 250], [125, 125], [62, 62], [31, 31]],capacity = 2500) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000, 1000], [500, 500], [250, 250], [125, 125], [62, 62], [31, 31]],capacity = 2500) == -1: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 5], [10, 10], [15, 15], [20, 20], [25, 25]],capacity = 40) == 40.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 5], [10, 10], [15, 15], [20, 20], [25, 25]],capacity = 40) == 40.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[50, 10], [40, 9], [30, 8], [20, 7], [10, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]],capacity = 30) == 128.57142857142858
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[50, 10], [40, 9], [30, 8], [20, 7], [10, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]],capacity = 30) == 128.57142857142858: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000, 500], [2000, 1000], [3000, 1500], [4000, 2000], [5000, 2500]],capacity = 1500) == 3000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000, 500], [2000, 1000], [3000, 1500], [4000, 2000], [5000, 2500]],capacity = 1500) == 3000.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000, 1000], [2000, 2000], [3000, 3000], [4000, 4000], [5000, 5000]],capacity = 15000) == 15000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000, 1000], [2000, 2000], [3000, 3000], [4000, 4000], [5000, 5000]],capacity = 15000) == 15000.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500], [600, 600], [700, 700], [800, 800], [900, 900], [1000, 1000]],capacity = 4500) == 4500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500], [600, 600], [700, 700], [800, 800], [900, 900], [1000, 1000]],capacity = 4500) == 4500.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 10], [20, 15], [30, 20], [40, 25]],capacity = 30) == 47.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 10], [20, 15], [30, 20], [40, 25]],capacity = 30) == 47.5: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10000, 10000], [9000, 9000], [8000, 8000], [7000, 7000], [6000, 6000]],capacity = 25000) == 25000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10000, 10000], [9000, 9000], [8000, 8000], [7000, 7000], [6000, 6000]],capacity = 25000) == 25000.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10000, 1000], [20000, 2000], [30000, 3000]],capacity = 1500) == 15000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10000, 1000], [20000, 2000], [30000, 3000]],capacity = 1500) == 15000.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000, 100], [2000, 200], [1500, 150]],capacity = 250) == 2500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000, 100], [2000, 200], [1500, 150]],capacity = 250) == 2500.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],capacity = 50) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],capacity = 50) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5000, 500], [3000, 300], [7000, 700]],capacity = 1000) == 10000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5000, 500], [3000, 300], [7000, 700]],capacity = 1000) == 10000.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000, 1], [500, 2], [250, 4], [125, 8], [62, 16]],capacity = 16) == 1878.875
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000, 1], [500, 2], [250, 4], [125, 8], [62, 16]],capacity = 16) == 1878.875: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],capacity = 50) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],capacity = 50) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],capacity = 50) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],capacity = 50) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[9999, 10000], [9998, 9999], [9997, 9998], [9996, 9997]],capacity = 30000) == 29996.99969990997
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[9999, 10000], [9998, 9999], [9997, 9998], [9996, 9997]],capacity = 30000) == 29996.99969990997: {e}')
    
    total += 1
    try:
        result = candidate(items = [[500, 1000], [1000, 500], [250, 250], [750, 750]],capacity = 2500) == 2500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[500, 1000], [1000, 500], [250, 250], [750, 750]],capacity = 2500) == 2500.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 9999], [2, 9998], [3, 9997], [4, 9996], [5, 9995]],capacity = 20000) == 9.002700810243073
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 9999], [2, 9998], [3, 9997], [4, 9996], [5, 9995]],capacity = 20000) == 9.002700810243073: {e}')
    
    total += 1
    try:
        result = candidate(items = [[9999, 10000], [8888, 9000], [7777, 8000], [6666, 7000], [5555, 6000], [4444, 5000], [3333, 4000], [2222, 3000], [1111, 2000], [1000, 1000]],capacity = 35000) == 34330.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[9999, 10000], [8888, 9000], [7777, 8000], [6666, 7000], [5555, 6000], [4444, 5000], [3333, 4000], [2222, 3000], [1111, 2000], [1000, 1000]],capacity = 35000) == 34330.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[7, 3], [6, 2], [5, 1], [4, 2]],capacity = 6) == 18.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[7, 3], [6, 2], [5, 1], [4, 2]],capacity = 6) == 18.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],capacity = 30) == 3000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],capacity = 30) == 3000.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],capacity = 1) == 100.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],capacity = 1) == 100.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[500, 100], [300, 60], [200, 40], [100, 20]],capacity = 250) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[500, 100], [300, 60], [200, 40], [100, 20]],capacity = 250) == -1: {e}')
    
    total += 1
    try:
        result = candidate(items = [[40, 20], [30, 15], [20, 10], [10, 5]],capacity = 25) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[40, 20], [30, 15], [20, 10], [10, 5]],capacity = 25) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],capacity = 15) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],capacity = 15) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 100], [2, 200], [3, 300], [4, 400], [5, 500]],capacity = 1000) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 100], [2, 200], [3, 300], [4, 400], [5, 500]],capacity = 1000) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10000, 10000], [9000, 9000], [8000, 8000], [7000, 7000], [6000, 6000], [5000, 5000], [4000, 4000], [3000, 3000], [2000, 2000], [1000, 1000]],capacity = 50000) == 50000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10000, 10000], [9000, 9000], [8000, 8000], [7000, 7000], [6000, 6000], [5000, 5000], [4000, 4000], [3000, 3000], [2000, 2000], [1000, 1000]],capacity = 50000) == 50000.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 10000], [2, 9000], [3, 8000], [4, 7000], [5, 6000]],capacity = 15000) == 9.75
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 10000], [2, 9000], [3, 8000], [4, 7000], [5, 6000]],capacity = 15000) == 9.75: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000, 1000], [2000, 2000], [3000, 3000], [4000, 4000], [5000, 5000]],capacity = 6000) == 6000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000, 1000], [2000, 2000], [3000, 3000], [4000, 4000], [5000, 5000]],capacity = 6000) == 6000.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 1], [5, 1], [5, 1], [5, 1], [5, 1]],capacity = 2) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 1], [5, 1], [5, 1], [5, 1], [5, 1]],capacity = 2) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],capacity = 15) == 40.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],capacity = 15) == 40.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1]],capacity = 10) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1]],capacity = 10) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 2], [10, 4], [15, 6], [20, 8], [25, 10]],capacity = 20) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 2], [10, 4], [15, 6], [20, 8], [25, 10]],capacity = 20) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],capacity = 15) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],capacity = 15) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25]],capacity = 25) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25]],capacity = 25) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],capacity = 15) == 15.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],capacity = 15) == 15.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1]],capacity = 10) == 100000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1]],capacity = 10) == 100000.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],capacity = 20) == 20.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],capacity = 20) == 20.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[200, 100], [150, 50], [100, 20], [50, 10]],capacity = 150) == 440.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[200, 100], [150, 50], [100, 20], [50, 10]],capacity = 150) == 440.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[25, 10], [40, 20], [15, 5], [35, 15]],capacity = 30) == 75.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[25, 10], [40, 20], [15, 5], [35, 15]],capacity = 30) == 75.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000, 500], [750, 300], [500, 200], [250, 100]],capacity = 800) == 1900.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000, 500], [750, 300], [500, 200], [250, 100]],capacity = 800) == 1900.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[500, 250], [300, 150], [200, 100], [100, 50]],capacity = 300) == 600.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[500, 250], [300, 150], [200, 100], [100, 50]],capacity = 300) == 600.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [50, 0.5], [200, 2], [150, 1.5], [300, 3]],capacity = 5) == 500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [50, 0.5], [200, 2], [150, 1.5], [300, 3]],capacity = 5) == 500.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 100000], [2, 100000], [3, 100000], [4, 100000], [5, 100000], [6, 100000], [7, 100000], [8, 100000], [9, 100000], [10, 100000]],capacity = 100000) == 10.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 100000], [2, 100000], [3, 100000], [4, 100000], [5, 100000], [6, 100000], [7, 100000], [8, 100000], [9, 100000], [10, 100000]],capacity = 100000) == 10.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[123, 456], [789, 1011], [1213, 1415], [1617, 1819], [2021, 2223]],capacity = 3000) == 2711.714128642111
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[123, 456], [789, 1011], [1213, 1415], [1617, 1819], [2021, 2223]],capacity = 3000) == 2711.714128642111: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 10000], [2, 10000], [3, 10000], [4, 10000], [5, 10000], [6, 10000], [7, 10000], [8, 10000], [9, 10000], [10, 10000]],capacity = 50000) == 40.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 10000], [2, 10000], [3, 10000], [4, 10000], [5, 10000], [6, 10000], [7, 10000], [8, 10000], [9, 10000], [10, 10000]],capacity = 50000) == 40.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 5], [20, 15], [30, 25], [40, 35], [50, 45]],capacity = 100) == 122.22222222222223
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 5], [20, 15], [30, 25], [40, 35], [50, 45]],capacity = 100) == 122.22222222222223: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5000, 1000], [4000, 800], [3000, 600], [2000, 400], [1000, 200]],capacity = 2200) == 11000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5000, 1000], [4000, 800], [3000, 600], [2000, 400], [1000, 200]],capacity = 2200) == 11000.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 20], [200, 40], [50, 10], [150, 30]],capacity = 50) == 250.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 20], [200, 40], [50, 10], [150, 30]],capacity = 50) == 250.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],capacity = 5000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],capacity = 5000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(items = [[500, 10], [500, 20], [500, 30], [500, 40], [500, 50], [500, 60], [500, 70], [500, 80], [500, 90], [500, 100]],capacity = 300) == 3625.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[500, 10], [500, 20], [500, 30], [500, 40], [500, 50], [500, 60], [500, 70], [500, 80], [500, 90], [500, 100]],capacity = 300) == 3625.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[9999, 9999], [8888, 8888], [7777, 7777], [6666, 6666], [5555, 5555]],capacity = 10000) == 10000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[9999, 9999], [8888, 8888], [7777, 7777], [6666, 6666], [5555, 5555]],capacity = 10000) == 10000.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10000, 1], [20000, 2], [30000, 3], [40000, 4], [50000, 5], [60000, 6], [70000, 7], [80000, 8], [90000, 9], [100000, 10]],capacity = 50000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10000, 1], [20000, 2], [30000, 3], [40000, 4], [50000, 5], [60000, 6], [70000, 7], [80000, 8], [90000, 9], [100000, 10]],capacity = 50000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(items = [[50, 1], [20, 3], [15, 2], [10, 5]],capacity = 10) == 93.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[50, 1], [20, 3], [15, 2], [10, 5]],capacity = 10) == 93.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000, 1000], [500, 500], [250, 250], [125, 125]],capacity = 2000) == -1
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000, 1000], [500, 500], [250, 250], [125, 125]],capacity = 2000) == -1: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [10, 1], [10, 1], [10, 1], [10, 1], [10, 1], [10, 1], [10, 1], [10, 1], [10, 1]],capacity = 5) == 50.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [10, 1], [10, 1], [10, 1], [10, 1], [10, 1], [10, 1], [10, 1], [10, 1], [10, 1]],capacity = 5) == 50.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],capacity = 55) == 5500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],capacity = 55) == 5500.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[9000, 10000], [8000, 9000], [7000, 8000], [6000, 7000], [5000, 6000]],capacity = 5000) == 4500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[9000, 10000], [8000, 9000], [7000, 8000], [6000, 7000], [5000, 6000]],capacity = 5000) == 4500.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 10000], [2, 9000], [3, 8000], [4, 7000], [5, 6000], [6, 5000], [7, 4000], [8, 3000], [9, 2000], [10, 1000]],capacity = 5000) == 24.333333333333332
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 10000], [2, 9000], [3, 8000], [4, 7000], [5, 6000], [6, 5000], [7, 4000], [8, 3000], [9, 2000], [10, 1000]],capacity = 5000) == 24.333333333333332: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000, 1], [2000, 2], [3000, 3], [4000, 4], [5000, 5], [6000, 6], [7000, 7], [8000, 8], [9000, 9], [10000, 10]],capacity = 50) == 50000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000, 1], [2000, 2], [3000, 3], [4000, 4], [5000, 5], [6000, 6], [7000, 7], [8000, 8], [9000, 9], [10000, 10]],capacity = 50) == 50000.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[500, 100], [200, 50], [300, 75]],capacity = 120) == 580.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[500, 100], [200, 50], [300, 75]],capacity = 120) == 580.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 10000], [2, 9000], [3, 8000], [4, 7000], [5, 6000], [6, 5000], [7, 4000], [8, 3000], [9, 2000], [10, 1000]],capacity = 50000) == 54.5
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 10000], [2, 9000], [3, 8000], [4, 7000], [5, 6000], [6, 5000], [7, 4000], [8, 3000], [9, 2000], [10, 1000]],capacity = 50000) == 54.5: {e}')
    
    total += 1
    try:
        result = candidate(items = [[5000, 10000], [4000, 8000], [3000, 6000], [2000, 4000], [1000, 2000]],capacity = 20000) == 10000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[5000, 10000], [4000, 8000], [3000, 6000], [2000, 4000], [1000, 2000]],capacity = 20000) == 10000.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000, 1000], [500, 500], [250, 250]],capacity = 1500) == 1500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000, 1000], [500, 500], [250, 250]],capacity = 1500) == 1500.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],capacity = 5) == 5.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],capacity = 5) == 5.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 50], [200, 100], [150, 75], [50, 25]],capacity = 200) == 400.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 50], [200, 100], [150, 75], [50, 25]],capacity = 200) == 400.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],capacity = 55) == 550.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],capacity = 55) == 550.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8]],capacity = 20) == 2000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8]],capacity = 20) == 2000.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[500, 250], [400, 200], [300, 150], [200, 100], [100, 50]],capacity = 600) == 1200.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[500, 250], [400, 200], [300, 150], [200, 100], [100, 50]],capacity = 600) == 1200.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 20], [200, 10], [50, 5], [300, 15]],capacity = 30) == 550.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 20], [200, 10], [50, 5], [300, 15]],capacity = 30) == 550.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[8, 2], [16, 4], [24, 6], [32, 8], [40, 10]],capacity = 20) == 80.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[8, 2], [16, 4], [24, 6], [32, 8], [40, 10]],capacity = 20) == 80.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],capacity = 25) == 2500.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],capacity = 25) == 2500.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000, 100], [2000, 200], [3000, 300], [4000, 400], [5000, 500]],capacity = 1000) == 10000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000, 100], [2000, 200], [3000, 300], [4000, 400], [5000, 500]],capacity = 1000) == 10000.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[3, 1], [12, 3], [7, 2], [9, 4], [15, 5], [18, 6]],capacity = 15) == 49.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[3, 1], [12, 3], [7, 2], [9, 4], [15, 5], [18, 6]],capacity = 15) == 49.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[1000, 500], [2000, 1000], [500, 250], [1500, 750]],capacity = 1500) == 3000.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[1000, 500], [2000, 1000], [500, 250], [1500, 750]],capacity = 1500) == 3000.0: {e}')
    
    total += 1
    try:
        result = candidate(items = [[500, 100], [200, 50], [100, 25], [50, 10]],capacity = 120) == 590.0
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(items = [[500, 100], [200, 50], [100, 25], [50, 10]],capacity = 120) == 590.0: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(items = [[50, 1], [10, 8]],capacity = 5) == 55.0
    assert candidate(items = [[1, 10000], [10000, 1]],capacity = 5000) == 10000.4999
    assert candidate(items = [[1, 1], [1, 1], [1, 1]],capacity = 2) == 2.0
    assert candidate(items = [[20, 1], [30, 2], [10, 1]],capacity = 4) == 60.0
    assert candidate(items = [[100, 30]],capacity = 50) == -1
    assert candidate(items = [[5, 1], [5, 1], [5, 1]],capacity = 3) == 15.0
    assert candidate(items = [[1, 100], [2, 200], [3, 300]],capacity = 150) == 1.5
    assert candidate(items = [[10, 2], [5, 3], [15, 5]],capacity = 10) == 30.0
    assert candidate(items = [[5, 5], [10, 10], [15, 15]],capacity = 30) == 30.0
    assert candidate(items = [[10, 2], [20, 3], [30, 5]],capacity = 10) == 60.0
    assert candidate(items = [[1, 1], [2, 2], [3, 3]],capacity = 3) == 3.0
    assert candidate(items = [[20, 5], [30, 10], [5, 1]],capacity = 12) == 43.0
    assert candidate(items = [[10, 5], [20, 10], [30, 15]],capacity = 20) == 40.0
    assert candidate(items = [[5, 10], [10, 20], [15, 30]],capacity = 50) == 25.0
    assert candidate(items = [[5, 10], [7, 5], [8, 4]],capacity = 15) == 18.0
    assert candidate(items = [[10, 2], [20, 5], [30, 10]],capacity = 7) == 30.0
    assert candidate(items = [[500, 100], [300, 60], [100, 20], [200, 40]],capacity = 150) == 750.0
    assert candidate(items = [[30, 10], [20, 5], [50, 20], [40, 15]],capacity = 40) == 115.0
    assert candidate(items = [[1, 9999], [2, 9998], [3, 9997], [4, 9996], [5, 9995]],capacity = 25000) == 10.503150945283585
    assert candidate(items = [[40, 4], [25, 3], [10, 2], [15, 1]],capacity = 10) == 90.0
    assert candidate(items = [[123, 456], [789, 1011], [1213, 1415], [1617, 1819], [2021, 2223]],capacity = 500) == 454.565901934323
    assert candidate(items = [[100, 50], [200, 100], [300, 150], [400, 200], [500, 250]],capacity = 600) == 1200.0
    assert candidate(items = [[10, 20], [20, 40], [30, 60], [40, 80], [50, 100]],capacity = 50) == 25.0
    assert candidate(items = [[9999, 1000], [8888, 2000], [7777, 3000], [6666, 4000], [5555, 5000]],capacity = 10000) == 33330.0
    assert candidate(items = [[100, 10], [200, 20], [150, 15], [50, 5]],capacity = 40) == 400.0
    assert candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],capacity = 15) == 1500.0
    assert candidate(items = [[2, 1], [4, 2], [6, 3], [8, 4], [10, 5], [12, 6], [14, 7], [16, 8], [18, 9], [20, 10], [22, 11], [24, 12], [26, 13], [28, 14], [30, 15]],capacity = 75) == 150.0
    assert candidate(items = [[9999, 1000], [8888, 900], [7777, 800], [6666, 700], [5555, 600], [4444, 500]],capacity = 5000) == -1
    assert candidate(items = [[40, 20], [25, 15], [15, 10], [10, 5]],capacity = 50) == 90.0
    assert candidate(items = [[10, 2], [20, 5], [30, 7], [40, 10]],capacity = 20) == 84.0
    assert candidate(items = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50], [60, 60], [70, 70], [80, 80], [90, 90], [100, 100]],capacity = 500) == 500.0
    assert candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],capacity = 10) == 100.0
    assert candidate(items = [[100, 10], [90, 9], [80, 8], [70, 7], [60, 6], [50, 5], [40, 4], [30, 3], [20, 2], [10, 1]],capacity = 50) == 500.0
    assert candidate(items = [[500, 100], [100, 20], [200, 40], [300, 60]],capacity = 150) == 750.0
    assert candidate(items = [[100, 50], [200, 100], [300, 150], [400, 200], [500, 250]],capacity = 100) == 200.0
    assert candidate(items = [[25, 10], [20, 8], [15, 6], [10, 4], [5, 2]],capacity = 20) == 50.0
    assert candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5]],capacity = 15) == 150.0
    assert candidate(items = [[5, 1], [10, 2], [15, 3], [20, 4], [25, 5], [30, 6], [35, 7], [40, 8], [45, 9], [50, 10]],capacity = 45) == 225.0
    assert candidate(items = [[1000, 1000], [2000, 2000], [3000, 3000], [4000, 4000], [5000, 5000], [6000, 6000], [7000, 7000], [8000, 8000], [9000, 9000], [10000, 10000]],capacity = 15000) == 15000.0
    assert candidate(items = [[1000, 1000], [500, 500], [250, 250], [125, 125], [62, 62], [31, 31]],capacity = 2500) == -1
    assert candidate(items = [[5, 5], [10, 10], [15, 15], [20, 20], [25, 25]],capacity = 40) == 40.0
    assert candidate(items = [[50, 10], [40, 9], [30, 8], [20, 7], [10, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]],capacity = 30) == 128.57142857142858
    assert candidate(items = [[1000, 500], [2000, 1000], [3000, 1500], [4000, 2000], [5000, 2500]],capacity = 1500) == 3000.0
    assert candidate(items = [[1000, 1000], [2000, 2000], [3000, 3000], [4000, 4000], [5000, 5000]],capacity = 15000) == 15000.0
    assert candidate(items = [[100, 100], [200, 200], [300, 300], [400, 400], [500, 500], [600, 600], [700, 700], [800, 800], [900, 900], [1000, 1000]],capacity = 4500) == 4500.0
    assert candidate(items = [[10, 10], [20, 15], [30, 20], [40, 25]],capacity = 30) == 47.5
    assert candidate(items = [[10000, 10000], [9000, 9000], [8000, 8000], [7000, 7000], [6000, 6000]],capacity = 25000) == 25000.0
    assert candidate(items = [[10000, 1000], [20000, 2000], [30000, 3000]],capacity = 1500) == 15000.0
    assert candidate(items = [[1000, 100], [2000, 200], [1500, 150]],capacity = 250) == 2500.0
    assert candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],capacity = 50) == 50.0
    assert candidate(items = [[5000, 500], [3000, 300], [7000, 700]],capacity = 1000) == 10000.0
    assert candidate(items = [[1000, 1], [500, 2], [250, 4], [125, 8], [62, 16]],capacity = 16) == 1878.875
    assert candidate(items = [[10, 10], [20, 20], [30, 30], [40, 40], [50, 50]],capacity = 50) == 50.0
    assert candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],capacity = 50) == 50.0
    assert candidate(items = [[9999, 10000], [9998, 9999], [9997, 9998], [9996, 9997]],capacity = 30000) == 29996.99969990997
    assert candidate(items = [[500, 1000], [1000, 500], [250, 250], [750, 750]],capacity = 2500) == 2500.0
    assert candidate(items = [[1, 9999], [2, 9998], [3, 9997], [4, 9996], [5, 9995]],capacity = 20000) == 9.002700810243073
    assert candidate(items = [[9999, 10000], [8888, 9000], [7777, 8000], [6666, 7000], [5555, 6000], [4444, 5000], [3333, 4000], [2222, 3000], [1111, 2000], [1000, 1000]],capacity = 35000) == 34330.0
    assert candidate(items = [[7, 3], [6, 2], [5, 1], [4, 2]],capacity = 6) == 18.0
    assert candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],capacity = 30) == 3000.0
    assert candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],capacity = 1) == 100.0
    assert candidate(items = [[500, 100], [300, 60], [200, 40], [100, 20]],capacity = 250) == -1
    assert candidate(items = [[40, 20], [30, 15], [20, 10], [10, 5]],capacity = 25) == 50.0
    assert candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],capacity = 15) == 15.0
    assert candidate(items = [[1, 100], [2, 200], [3, 300], [4, 400], [5, 500]],capacity = 1000) == 10.0
    assert candidate(items = [[10000, 10000], [9000, 9000], [8000, 8000], [7000, 7000], [6000, 6000], [5000, 5000], [4000, 4000], [3000, 3000], [2000, 2000], [1000, 1000]],capacity = 50000) == 50000.0
    assert candidate(items = [[1, 10000], [2, 9000], [3, 8000], [4, 7000], [5, 6000]],capacity = 15000) == 9.75
    assert candidate(items = [[1000, 1000], [2000, 2000], [3000, 3000], [4000, 4000], [5000, 5000]],capacity = 6000) == 6000.0
    assert candidate(items = [[5, 1], [5, 1], [5, 1], [5, 1], [5, 1]],capacity = 2) == 10.0
    assert candidate(items = [[10, 1], [9, 2], [8, 3], [7, 4], [6, 5], [5, 6], [4, 7], [3, 8], [2, 9], [1, 10]],capacity = 15) == 40.0
    assert candidate(items = [[5, 5], [4, 4], [3, 3], [2, 2], [1, 1]],capacity = 10) == 10.0
    assert candidate(items = [[5, 2], [10, 4], [15, 6], [20, 8], [25, 10]],capacity = 20) == 50.0
    assert candidate(items = [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],capacity = 15) == 15.0
    assert candidate(items = [[10, 5], [20, 10], [30, 15], [40, 20], [50, 25]],capacity = 25) == 50.0
    assert candidate(items = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],capacity = 15) == 15.0
    assert candidate(items = [[10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1], [10000, 1]],capacity = 10) == 100000.0
    assert candidate(items = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],capacity = 20) == 20.0
    assert candidate(items = [[200, 100], [150, 50], [100, 20], [50, 10]],capacity = 150) == 440.0
    assert candidate(items = [[25, 10], [40, 20], [15, 5], [35, 15]],capacity = 30) == 75.0
    assert candidate(items = [[1000, 500], [750, 300], [500, 200], [250, 100]],capacity = 800) == 1900.0
    assert candidate(items = [[500, 250], [300, 150], [200, 100], [100, 50]],capacity = 300) == 600.0
    assert candidate(items = [[100, 1], [50, 0.5], [200, 2], [150, 1.5], [300, 3]],capacity = 5) == 500.0
    assert candidate(items = [[1, 100000], [2, 100000], [3, 100000], [4, 100000], [5, 100000], [6, 100000], [7, 100000], [8, 100000], [9, 100000], [10, 100000]],capacity = 100000) == 10.0
    assert candidate(items = [[123, 456], [789, 1011], [1213, 1415], [1617, 1819], [2021, 2223]],capacity = 3000) == 2711.714128642111
    assert candidate(items = [[1, 10000], [2, 10000], [3, 10000], [4, 10000], [5, 10000], [6, 10000], [7, 10000], [8, 10000], [9, 10000], [10, 10000]],capacity = 50000) == 40.0
    assert candidate(items = [[10, 5], [20, 15], [30, 25], [40, 35], [50, 45]],capacity = 100) == 122.22222222222223
    assert candidate(items = [[5000, 1000], [4000, 800], [3000, 600], [2000, 400], [1000, 200]],capacity = 2200) == 11000.0
    assert candidate(items = [[100, 20], [200, 40], [50, 10], [150, 30]],capacity = 50) == 250.0
    assert candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],capacity = 5000) == -1
    assert candidate(items = [[500, 10], [500, 20], [500, 30], [500, 40], [500, 50], [500, 60], [500, 70], [500, 80], [500, 90], [500, 100]],capacity = 300) == 3625.0
    assert candidate(items = [[9999, 9999], [8888, 8888], [7777, 7777], [6666, 6666], [5555, 5555]],capacity = 10000) == 10000.0
    assert candidate(items = [[10000, 1], [20000, 2], [30000, 3], [40000, 4], [50000, 5], [60000, 6], [70000, 7], [80000, 8], [90000, 9], [100000, 10]],capacity = 50000) == -1
    assert candidate(items = [[50, 1], [20, 3], [15, 2], [10, 5]],capacity = 10) == 93.0
    assert candidate(items = [[1000, 1000], [500, 500], [250, 250], [125, 125]],capacity = 2000) == -1
    assert candidate(items = [[10, 1], [10, 1], [10, 1], [10, 1], [10, 1], [10, 1], [10, 1], [10, 1], [10, 1], [10, 1]],capacity = 5) == 50.0
    assert candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],capacity = 55) == 5500.0
    assert candidate(items = [[9000, 10000], [8000, 9000], [7000, 8000], [6000, 7000], [5000, 6000]],capacity = 5000) == 4500.0
    assert candidate(items = [[1, 10000], [2, 9000], [3, 8000], [4, 7000], [5, 6000], [6, 5000], [7, 4000], [8, 3000], [9, 2000], [10, 1000]],capacity = 5000) == 24.333333333333332
    assert candidate(items = [[1000, 1], [2000, 2], [3000, 3], [4000, 4], [5000, 5], [6000, 6], [7000, 7], [8000, 8], [9000, 9], [10000, 10]],capacity = 50) == 50000.0
    assert candidate(items = [[500, 100], [200, 50], [300, 75]],capacity = 120) == 580.0
    assert candidate(items = [[1, 10000], [2, 9000], [3, 8000], [4, 7000], [5, 6000], [6, 5000], [7, 4000], [8, 3000], [9, 2000], [10, 1000]],capacity = 50000) == 54.5
    assert candidate(items = [[5000, 10000], [4000, 8000], [3000, 6000], [2000, 4000], [1000, 2000]],capacity = 20000) == 10000.0
    assert candidate(items = [[1000, 1000], [500, 500], [250, 250]],capacity = 1500) == 1500.0
    assert candidate(items = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],capacity = 5) == 5.0
    assert candidate(items = [[100, 50], [200, 100], [150, 75], [50, 25]],capacity = 200) == 400.0
    assert candidate(items = [[10, 1], [20, 2], [30, 3], [40, 4], [50, 5], [60, 6], [70, 7], [80, 8], [90, 9], [100, 10]],capacity = 55) == 550.0
    assert candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8]],capacity = 20) == 2000.0
    assert candidate(items = [[500, 250], [400, 200], [300, 150], [200, 100], [100, 50]],capacity = 600) == 1200.0
    assert candidate(items = [[100, 20], [200, 10], [50, 5], [300, 15]],capacity = 30) == 550.0
    assert candidate(items = [[8, 2], [16, 4], [24, 6], [32, 8], [40, 10]],capacity = 20) == 80.0
    assert candidate(items = [[100, 1], [200, 2], [300, 3], [400, 4], [500, 5], [600, 6], [700, 7], [800, 8], [900, 9], [1000, 10]],capacity = 25) == 2500.0
    assert candidate(items = [[1000, 100], [2000, 200], [3000, 300], [4000, 400], [5000, 500]],capacity = 1000) == 10000.0
    assert candidate(items = [[3, 1], [12, 3], [7, 2], [9, 4], [15, 5], [18, 6]],capacity = 15) == 49.0
    assert candidate(items = [[1000, 500], [2000, 1000], [500, 250], [1500, 750]],capacity = 1500) == 3000.0
    assert candidate(items = [[500, 100], [200, 50], [100, 25], [50, 10]],capacity = 120) == 590.0


