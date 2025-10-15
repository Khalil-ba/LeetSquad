def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [[-10, -5, -3, -1], [0, 2, 4, 6], [5, 10, 15, 20]]) == [-1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-10, -5, -3, -1], [0, 2, 4, 6], [5, 10, 15, 20]]) == [-1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 5, 9], [2, 6, 10], [3, 7, 11]]) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 5, 9], [2, 6, 10], [3, 7, 11]]) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[5, 10, 15], [3, 6, 9], [12, 14, 18]]) == [9, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[5, 10, 15], [3, 6, 9], [12, 14, 18]]) == [9, 12]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-10, -9, -8], [-7, -6, -5], [-4, -3, -2]]) == [-8, -4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-10, -9, -8], [-7, -6, -5], [-4, -3, -2]]) == [-8, -4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-10, -9, -8], [-4, -3, -2], [-1, 0, 1]]) == [-8, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-10, -9, -8], [-4, -3, -2], [-1, 0, 1]]) == [-8, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-10, -5, 0, 5, 10], [-5, 0, 5, 10, 15], [0, 5, 10, 15, 20]]) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-10, -5, 0, 5, 10], [-5, 0, 5, 10, 15], [0, 5, 10, 15, 20]]) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 5, 9], [0, 6, 8], [2, 3, 7]]) == [0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 5, 9], [0, 6, 8], [2, 3, 7]]) == [0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-5, -3], [-1, -2], [4, 5, 6]]) == [-3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-5, -3], [-1, -2], [4, 5, 6]]) == [-3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[10, 10, 10], [10, 10, 10], [10, 10, 10]]) == [10, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[10, 10, 10], [10, 10, 10], [10, 10, 10]]) == [10, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]) == [20, 24]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]) == [20, 24]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]) == [0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]) == [0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-10, -8, -6], [-6, -4, -2], [0, 2, 4]]) == [-6, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-10, -8, -6], [-6, -4, -2], [0, 2, 4]]) == [-6, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1], [2], [3], [4], [5]]) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1], [2], [3], [4], [5]]) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[5, 10, 15], [3, 6, 9], [12, 18, 24]]) == [9, 12]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[5, 10, 15], [3, 6, 9], [12, 18, 24]]) == [9, 12]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 4, 7, 10, 13], [2, 5, 8, 11, 14], [3, 6, 9, 12, 15], [0, 16, 17, 18, 19]]) == [0, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 4, 7, 10, 13], [2, 5, 8, 11, 14], [3, 6, 9, 12, 15], [0, 16, 17, 18, 19]]) == [0, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]) == [2, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]) == [2, 19]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]) == [-1, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]) == [-1, 15]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1000, 2000, 3000], [500, 1500, 2500, 3500], [-1000, 0, 1000, 2000]]) == [500, 1000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1000, 2000, 3000], [500, 1500, 2500, 3500], [-1000, 0, 1000, 2000]]) == [500, 1000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1], [2], [3], [4], [5]]) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1], [2], [3], [4], [5]]) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-1000, -900, -800, -700, -600, -500], [-950, -850, -750, -650, -550, -450], [-900, -800, -700, -600, -500, -400], [-850, -750, -650, -550, -450, -350]]) == [-900, -850]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-1000, -900, -800, -700, -600, -500], [-950, -850, -750, -650, -550, -450], [-900, -800, -700, -600, -500, -400], [-850, -750, -650, -550, -450, -350]]) == [-900, -850]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]]) == [10, 31]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]]) == [10, 31]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]]) == [9, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]]) == [9, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[5], [10], [15], [20], [25], [30], [35], [40], [45], [50]]) == [5, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[5], [10], [15], [20], [25], [30], [35], [40], [45], [50]]) == [5, 50]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-100, -99, -98], [-97, -96, -95], [-94, -93, -92], [-91, -90, -89], [-88, -87, -86]]) == [-98, -88]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-100, -99, -98], [-97, -96, -95], [-94, -93, -92], [-91, -90, -89], [-88, -87, -86]]) == [-98, -88]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-1, -2, -3, -4, -5], [-10, -20, -30, -40, -50], [-100, -200, -300, -400, -500], [-1000, -2000, -3000, -4000, -5000]]) == [-1000, -5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-1, -2, -3, -4, -5], [-10, -20, -30, -40, -50], [-100, -200, -300, -400, -500], [-1000, -2000, -3000, -4000, -5000]]) == [-1000, -5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1000, 2000, 3000, 4000, 5000], [1500, 2500, 3500, 4500, 5500], [2000, 3000, 4000, 5000, 6000], [2500, 3500, 4500, 5500, 6500]]) == [2000, 2500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1000, 2000, 3000, 4000, 5000], [1500, 2500, 3500, 4500, 5500], [2000, 3000, 4000, 5000, 6000], [2500, 3500, 4500, 5500, 6500]]) == [2000, 2500]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-1, 0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9]]) == [3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-1, 0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9]]) == [3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-10, -5, 0], [0, 5, 10], [10, 15, 20], [20, 25, 30], [30, 35, 40]]) == [0, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-10, -5, 0], [0, 5, 10], [10, 15, 20], [20, 25, 30], [30, 35, 40]]) == [0, 30]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [-95, -85, -75, -65, -55, -45, -35, -25, -15, -5, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]]) == [-100, -95]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [-95, -85, -75, -65, -55, -45, -35, -25, -15, -5, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]]) == [-100, -95]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]]) == [6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]]) == [6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]]) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]]) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[10, 20, 30, 40, 50], [15, 25, 35, 45, 55], [20, 30, 40, 50, 60], [25, 35, 45, 55, 65]]) == [20, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[10, 20, 30, 40, 50], [15, 25, 35, 45, 55], [20, 30, 40, 50, 60], [25, 35, 45, 55, 65]]) == [20, 25]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [1, 6, 11, 16, 21, 26, 31, 36, 41, 46], [2, 7, 12, 17, 22, 27, 32, 37, 42, 47]]) == [5, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [1, 6, 11, 16, 21, 26, 31, 36, 41, 46], [2, 7, 12, 17, 22, 27, 32, 37, 42, 47]]) == [5, 7]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-100, -50, 0, 50, 100], [-200, -150, -100, -50, 0], [50, 100, 150, 200, 250]]) == [0, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-100, -50, 0, 50, 100], [-200, -150, -100, -50, 0], [50, 100, 150, 200, 250]]) == [0, 50]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-100, -50, -25, 0, 25, 50, 100], [5, 15, 25, 35, 45, 55, 65], [10, 20, 30, 40, 50, 60, 70]]) == [20, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-100, -50, -25, 0, 25, 50, 100], [5, 15, 25, 35, 45, 55, 65], [10, 20, 30, 40, 50, 60, 70]]) == [20, 25]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 5, 9, 13, 17], [2, 6, 10, 14, 18], [3, 7, 11, 15, 19], [4, 8, 12, 16, 20]]) == [1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 5, 9, 13, 17], [2, 6, 10, 14, 18], [3, 7, 11, 15, 19], [4, 8, 12, 16, 20]]) == [1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-5, -3, -1], [-4, -2, 0], [-3, -1, 1], [-2, 0, 2], [-1, 1, 3], [0, 2, 4], [1, 3, 5], [2, 4, 6], [3, 5, 7], [4, 6, 8]]) == [-1, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-5, -3, -1], [-4, -2, 0], [-3, -1, 1], [-2, 0, 2], [-1, 1, 3], [0, 2, 4], [1, 3, 5], [2, 4, 6], [3, 5, 7], [4, 6, 8]]) == [-1, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-100, -90, -80, -70, -60], [-50, -40, -30, -20, -10], [0, 10, 20, 30, 40], [50, 60, 70, 80, 90], [100, 110, 120, 130, 140]]) == [-60, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-100, -90, -80, -70, -60], [-50, -40, -30, -20, -10], [0, 10, 20, 30, 40], [50, 60, 70, 80, 90], [100, 110, 120, 130, 140]]) == [-60, 100]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-100, 0, 100], [50, 60, 70], [90, 100, 110], [200, 210, 220]]) == [70, 200]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-100, 0, 100], [50, 60, 70], [90, 100, 110], [200, 210, 220]]) == [70, 200]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 20, 30, 40, 50], [1, 11, 21, 31, 41, 51]]) == [10, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 20, 30, 40, 50], [1, 11, 21, 31, 41, 51]]) == [10, 11]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-1, -2, -3, -4, -5], [-5, -4, -3, -2, -1], [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 5, 6, 7]]) == [-1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-1, -2, -3, -4, -5], [-5, -4, -3, -2, -1], [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 5, 6, 7]]) == [-1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-10, -5, -1], [0, 1, 5], [10, 15, 20], [25, 30, 35], [40, 45, 50]]) == [-1, 40]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-10, -5, -1], [0, 1, 5], [10, 15, 20], [25, 30, 35], [40, 45, 50]]) == [-1, 40]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-10, -5, 0, 5, 10], [0, 2, 4, 6, 8], [3, 7, 11, 15, 19], [1, 3, 5, 7, 9]]) == [3, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-10, -5, 0, 5, 10], [0, 2, 4, 6, 8], [3, 7, 11, 15, 19], [1, 3, 5, 7, 9]]) == [3, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-10, -5, -1], [0, 1, 5, 10, 15], [20, 25, 30, 35, 40], [45, 50, 55, 60, 65]]) == [-1, 45]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-10, -5, -1], [0, 1, 5, 10, 15], [20, 25, 30, 35, 40], [45, 50, 55, 60, 65]]) == [-1, 45]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996], [6, 99995], [7, 99994], [8, 99993], [9, 99992], [10, 99991]]) == [1, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996], [6, 99995], [7, 99994], [8, 99993], [9, 99992], [10, 99991]]) == [1, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-100, -50, 0, 50, 100], [-90, -40, -10, 40, 90], [-80, -30, -20, 30, 80]]) == [-100, -80]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-100, -50, 0, 50, 100], [-90, -40, -10, 40, 90], [-80, -30, -20, 30, 80]]) == [-100, -80]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-100, -50, -25, -10, 0, 10, 25, 50, 100], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]]) == [5, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-100, -50, -25, -10, 0, 10, 25, 50, 100], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]]) == [5, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [0, 21, 22, 23, 24, 25, 26, 27, 28, 29]]) == [0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [0, 21, 22, 23, 24, 25, 26, 27, 28, 29]]) == [0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == [5, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == [5, 21]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[10, 20, 30, 40, 50], [11, 21, 31, 41, 51], [12, 22, 32, 42, 52], [13, 23, 33, 43, 53], [14, 24, 34, 44, 54]]) == [10, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[10, 20, 30, 40, 50], [11, 21, 31, 41, 51], [12, 22, 32, 42, 52], [13, 23, 33, 43, 53], [14, 24, 34, 44, 54]]) == [10, 14]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-10, 0, 10, 20], [0, 1, 2, 3], [5, 6, 7, 8, 9]]) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-10, 0, 10, 20], [0, 1, 2, 3], [5, 6, 7, 8, 9]]) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-1, -2, -3, -4, -5], [-10, -20, -30, -40, -50], [-100, -200, -300, -400, -500]]) == [-100, -5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-1, -2, -3, -4, -5], [-10, -20, -30, -40, -50], [-100, -200, -300, -400, -500]]) == [-100, -5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 10, 20, 30, 40], [2, 12, 22, 32, 42], [3, 13, 23, 33, 43]]) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 10, 20, 30, 40], [2, 12, 22, 32, 42], [3, 13, 23, 33, 43]]) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10, 12], [0, 9, 12, 20, 24, 26], [5, 18, 22, 30, 35, 40]]) == [5, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10, 12], [0, 9, 12, 20, 24, 26], [5, 18, 22, 30, 35, 40]]) == [5, 9]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-1000, -500, -250, -100, -50, -25, -10, -5, -2, -1, 0, 1, 2, 5, 10, 25, 50, 100, 250, 500, 1000], [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]]) == [1000, 1000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-1000, -500, -250, -100, -50, -25, -10, -5, -2, -1, 0, 1, 2, 5, 10, 25, 50, 100, 250, 500, 1000], [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]]) == [1000, 1000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-1000, -500, -250, -100, -50, -25, 0, 25, 50, 100, 250, 500, 1000], [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000], [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500]]) == [500, 500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-1000, -500, -250, -100, -50, -25, 0, 25, 50, 100, 250, 500, 1000], [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000], [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500]]) == [500, 500]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]) == [1, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]) == [1, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 20, 30], [2, 25, 35], [3, 30, 40], [4, 35, 45], [5, 40, 50]]) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 20, 30], [2, 25, 35], [3, 30, 40], [4, 35, 45], [5, 40, 50]]) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[100, 200, 300, 400, 500], [50, 150, 250, 350, 450], [25, 75, 125, 175, 225]]) == [50, 100]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[100, 200, 300, 400, 500], [50, 150, 250, 350, 450], [25, 75, 125, 175, 225]]) == [50, 100]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 5, 7, 9, 11], [4, 6, 8, 10, 12]]) == [3, 4]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 5, 7, 9, 11], [4, 6, 8, 10, 12]]) == [3, 4]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 4, 10, 14], [0, 9, 10, 20, 24], [5, 18, 22, 30], [3, 13, 15, 17]]) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 4, 10, 14], [0, 9, 10, 20, 24], [5, 18, 22, 30], [3, 13, 15, 17]]) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 4, 7, 10, 13], [2, 5, 8, 11, 14], [3, 6, 9, 12, 15]]) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 4, 7, 10, 13], [2, 5, 8, 11, 14], [3, 6, 9, 12, 15]]) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100], [0, 100, 200, 300, 400, 500, 600, 700, 800, 900], [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]]) == [-100, 1000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100], [0, 100, 200, 300, 400, 500, 600, 700, 800, 900], [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]]) == [-100, 1000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 10, 19, 28, 37], [2, 11, 20, 29, 38], [3, 12, 21, 30, 39], [4, 13, 22, 31, 40], [5, 14, 23, 32, 41]]) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 10, 19, 28, 37], [2, 11, 20, 29, 38], [3, 12, 21, 30, 39], [4, 13, 22, 31, 40], [5, 14, 23, 32, 41]]) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-10, -5, 0, 5, 10], [-20, -15, -10, -5, 0], [1, 6, 11, 16, 21]]) == [0, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-10, -5, 0, 5, 10], [-20, -15, -10, -5, 0], [1, 6, 11, 16, 21]]) == [0, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[10, 20, 30, 40, 50], [15, 25, 35, 45, 55], [20, 30, 40, 50, 60], [5, 10, 15, 20, 25]]) == [15, 20]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[10, 20, 30, 40, 50], [15, 25, 35, 45, 55], [20, 30, 40, 50, 60], [5, 10, 15, 20, 25]]) == [15, 20]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4], [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3]]) == [-5, -5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4], [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3]]) == [-5, -5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]]) == [6, 6]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]]) == [6, 6]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[100, 200, 300, 400], [50, 150, 250, 350], [25, 125, 225, 325, 425]]) == [100, 150]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[100, 200, 300, 400], [50, 150, 250, 350], [25, 125, 225, 325, 425]]) == [100, 150]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 4, 7, 10, 13, 16, 19, 22, 25, 28], [2, 5, 8, 11, 14, 17, 20, 23, 26, 29], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]]) == [1, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 4, 7, 10, 13, 16, 19, 22, 25, 28], [2, 5, 8, 11, 14, 17, 20, 23, 26, 29], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]]) == [1, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-100000, 0, 100000], [-99999, 99999], [-99998, 99998], [-99997, 99997]]) == [-100000, -99997]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-100000, 0, 100000], [-99999, 99999], [-99998, 99998], [-99997, 99997]]) == [-100000, -99997]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]) == [50, 51]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]) == [50, 51]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]]) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]]) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996]]) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996]]) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == [1, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == [1, 1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-100, -50, 0, 50, 100], [5, 15, 25, 35, 45], [1, 2, 3, 4, 5], [0, 0, 0, 0, 0]]) == [0, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-100, -50, 0, 50, 100], [5, 15, 25, 35, 45], [1, 2, 3, 4, 5], [0, 0, 0, 0, 0]]) == [0, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]) == [0, 0]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]) == [0, 0]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-1, -2, -3, -4, -5], [-6, -7, -8, -9, -10], [-11, -12, -13, -14, -15], [-16, -17, -18, -19, -20]]) == [-16, -5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-1, -2, -3, -4, -5], [-6, -7, -8, -9, -10], [-11, -12, -13, -14, -15], [-16, -17, -18, -19, -20]]) == [-16, -5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5]]) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5]]) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 10, 20, 30, 40], [5, 15, 25, 35, 45], [10, 20, 30, 40, 50], [5, 15, 25, 35, 45]]) == [5, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 10, 20, 30, 40], [5, 15, 25, 35, 45], [10, 20, 30, 40, 50], [5, 15, 25, 35, 45]]) == [5, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]) == [1, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]) == [1, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]) == [3, 3]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]) == [3, 3]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[10, 20, 30], [11, 21, 31], [12, 22, 32], [13, 23, 33], [14, 24, 34], [15, 25, 35], [16, 26, 36], [17, 27, 37], [18, 28, 38], [19, 29, 39]]) == [10, 19]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[10, 20, 30], [11, 21, 31], [12, 22, 32], [13, 23, 33], [14, 24, 34], [15, 25, 35], [16, 26, 36], [17, 27, 37], [18, 28, 38], [19, 29, 39]]) == [10, 19]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [2, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101], [3, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102], [4, 13, 23, 33, 43, 53, 63, 73, 83, 93, 103], [5, 14, 24, 34, 44, 54, 64, 74, 84, 94, 104]]) == [1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [2, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101], [3, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102], [4, 13, 23, 33, 43, 53, 63, 73, 83, 93, 103], [5, 14, 24, 34, 44, 54, 64, 74, 84, 94, 104]]) == [1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-1, 0, 1], [-2, -1, 0, 1, 2], [-3, -2, -1, 0, 1, 2, 3]]) == [-1, -1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-1, 0, 1], [-2, -1, 0, 1, 2], [-3, -2, -1, 0, 1, 2, 3]]) == [-1, -1]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == [5, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == [5, 21]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-100, -90, -80, -70, -60], [-95, -85, -75, -65, -55], [-90, -80, -70, -60, -50], [-85, -75, -65, -55, -45]]) == [-90, -85]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-100, -90, -80, -70, -60], [-95, -85, -75, -65, -55], [-90, -80, -70, -60, -50], [-85, -75, -65, -55, -45]]) == [-90, -85]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]) == [10, 21]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]) == [10, 21]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-10, -5, 0, 5, 10], [1, 3, 6, 9, 12], [2, 4, 7, 11, 13], [0, 8, 16, 24, 32]]) == [0, 2]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-10, -5, 0, 5, 10], [1, 3, 6, 9, 12], [2, 4, 7, 11, 13], [0, 8, 16, 24, 32]]) == [0, 2]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]) == [1, 10]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]) == [1, 10]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[100, 200, 300], [150, 250, 350], [200, 250, 300, 350]]) == [150, 200]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[100, 200, 300], [150, 250, 350], [200, 250, 300, 350]]) == [150, 200]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[-100000, 100000], [-90000, 90000], [-80000, 80000], [-70000, 70000], [-60000, 60000]]) == [-100000, -60000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[-100000, 100000], [-90000, 90000], [-80000, 80000], [-70000, 70000], [-60000, 60000]]) == [-100000, -60000]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15]]) == [1, 15]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15]]) == [1, 15]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [[-10, -5, -3, -1], [0, 2, 4, 6], [5, 10, 15, 20]]) == [-1, 5]
    assert candidate(nums = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]) == [1, 1]
    assert candidate(nums = [[1, 5, 9], [2, 6, 10], [3, 7, 11]]) == [1, 3]
    assert candidate(nums = [[5, 10, 15], [3, 6, 9], [12, 14, 18]]) == [9, 12]
    assert candidate(nums = [[-10, -9, -8], [-7, -6, -5], [-4, -3, -2]]) == [-8, -4]
    assert candidate(nums = [[-10, -9, -8], [-4, -3, -2], [-1, 0, 1]]) == [-8, -1]
    assert candidate(nums = [[-10, -5, 0, 5, 10], [-5, 0, 5, 10, 15], [0, 5, 10, 15, 20]]) == [0, 0]
    assert candidate(nums = [[1, 5, 9], [0, 6, 8], [2, 3, 7]]) == [0, 2]
    assert candidate(nums = [[-5, -3], [-1, -2], [4, 5, 6]]) == [-3, 4]
    assert candidate(nums = [[10, 10, 10], [10, 10, 10], [10, 10, 10]]) == [10, 10]
    assert candidate(nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]) == [20, 24]
    assert candidate(nums = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]) == [0, 2]
    assert candidate(nums = [[-10, -8, -6], [-6, -4, -2], [0, 2, 4]]) == [-6, 0]
    assert candidate(nums = [[1], [2], [3], [4], [5]]) == [1, 5]
    assert candidate(nums = [[5, 10, 15], [3, 6, 9], [12, 18, 24]]) == [9, 12]
    assert candidate(nums = [[1, 4, 7, 10, 13], [2, 5, 8, 11, 14], [3, 6, 9, 12, 15], [0, 16, 17, 18, 19]]) == [0, 3]
    assert candidate(nums = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]) == [2, 19]
    assert candidate(nums = [[-5, -4, -3, -2, -1], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]) == [-1, 15]
    assert candidate(nums = [[1000, 2000, 3000], [500, 1500, 2500, 3500], [-1000, 0, 1000, 2000]]) == [500, 1000]
    assert candidate(nums = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], [3, 3, 3, 3, 3, 3, 3, 3, 3, 3], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]]) == [1, 4]
    assert candidate(nums = [[1], [2], [3], [4], [5]]) == [1, 5]
    assert candidate(nums = [[-1000, -900, -800, -700, -600, -500], [-950, -850, -750, -650, -550, -450], [-900, -800, -700, -600, -500, -400], [-850, -750, -650, -550, -450, -350]]) == [-900, -850]
    assert candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]]) == [10, 31]
    assert candidate(nums = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]]) == [9, 10]
    assert candidate(nums = [[5], [10], [15], [20], [25], [30], [35], [40], [45], [50]]) == [5, 50]
    assert candidate(nums = [[-100, -99, -98], [-97, -96, -95], [-94, -93, -92], [-91, -90, -89], [-88, -87, -86]]) == [-98, -88]
    assert candidate(nums = [[-1, -2, -3, -4, -5], [-10, -20, -30, -40, -50], [-100, -200, -300, -400, -500], [-1000, -2000, -3000, -4000, -5000]]) == [-1000, -5]
    assert candidate(nums = [[1000, 2000, 3000, 4000, 5000], [1500, 2500, 3500, 4500, 5500], [2000, 3000, 4000, 5000, 6000], [2500, 3500, 4500, 5500, 6500]]) == [2000, 2500]
    assert candidate(nums = [[-1, 0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7, 8], [3, 4, 5, 6, 7, 8, 9]]) == [3, 3]
    assert candidate(nums = [[-10, -5, 0], [0, 5, 10], [10, 15, 20], [20, 25, 30], [30, 35, 40]]) == [0, 30]
    assert candidate(nums = [[-100, -90, -80, -70, -60, -50, -40, -30, -20, -10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [-95, -85, -75, -65, -55, -45, -35, -25, -15, -5, 5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]]) == [-100, -95]
    assert candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]]) == [6, 6]
    assert candidate(nums = [[1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]]) == [1, 5]
    assert candidate(nums = [[10, 20, 30, 40, 50], [15, 25, 35, 45, 55], [20, 30, 40, 50, 60], [25, 35, 45, 55, 65]]) == [20, 25]
    assert candidate(nums = [[5, 10, 15, 20, 25, 30, 35, 40, 45, 50], [1, 6, 11, 16, 21, 26, 31, 36, 41, 46], [2, 7, 12, 17, 22, 27, 32, 37, 42, 47]]) == [5, 7]
    assert candidate(nums = [[-100, -50, 0, 50, 100], [-200, -150, -100, -50, 0], [50, 100, 150, 200, 250]]) == [0, 50]
    assert candidate(nums = [[-100, -50, -25, 0, 25, 50, 100], [5, 15, 25, 35, 45, 55, 65], [10, 20, 30, 40, 50, 60, 70]]) == [20, 25]
    assert candidate(nums = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]) == [1, 2]
    assert candidate(nums = [[1, 5, 9, 13, 17], [2, 6, 10, 14, 18], [3, 7, 11, 15, 19], [4, 8, 12, 16, 20]]) == [1, 4]
    assert candidate(nums = [[-5, -3, -1], [-4, -2, 0], [-3, -1, 1], [-2, 0, 2], [-1, 1, 3], [0, 2, 4], [1, 3, 5], [2, 4, 6], [3, 5, 7], [4, 6, 8]]) == [-1, 4]
    assert candidate(nums = [[-100, -90, -80, -70, -60], [-50, -40, -30, -20, -10], [0, 10, 20, 30, 40], [50, 60, 70, 80, 90], [100, 110, 120, 130, 140]]) == [-60, 100]
    assert candidate(nums = [[-100, 0, 100], [50, 60, 70], [90, 100, 110], [200, 210, 220]]) == [70, 200]
    assert candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 20, 30, 40, 50], [1, 11, 21, 31, 41, 51]]) == [10, 11]
    assert candidate(nums = [[-1, -2, -3, -4, -5], [-5, -4, -3, -2, -1], [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 5, 6, 7]]) == [-1, 1]
    assert candidate(nums = [[-10, -5, -1], [0, 1, 5], [10, 15, 20], [25, 30, 35], [40, 45, 50]]) == [-1, 40]
    assert candidate(nums = [[-10, -5, 0, 5, 10], [0, 2, 4, 6, 8], [3, 7, 11, 15, 19], [1, 3, 5, 7, 9]]) == [3, 5]
    assert candidate(nums = [[-10, -5, -1], [0, 1, 5, 10, 15], [20, 25, 30, 35, 40], [45, 50, 55, 60, 65]]) == [-1, 45]
    assert candidate(nums = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996], [6, 99995], [7, 99994], [8, 99993], [9, 99992], [10, 99991]]) == [1, 10]
    assert candidate(nums = [[-100, -50, 0, 50, 100], [-90, -40, -10, 40, 90], [-80, -30, -20, 30, 80]]) == [-100, -80]
    assert candidate(nums = [[-100, -50, -25, -10, 0, 10, 25, 50, 100], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]]) == [5, 10]
    assert candidate(nums = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [0, 21, 22, 23, 24, 25, 26, 27, 28, 29]]) == [0, 2]
    assert candidate(nums = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == [5, 21]
    assert candidate(nums = [[10, 20, 30, 40, 50], [11, 21, 31, 41, 51], [12, 22, 32, 42, 52], [13, 23, 33, 43, 53], [14, 24, 34, 44, 54]]) == [10, 14]
    assert candidate(nums = [[-10, 0, 10, 20], [0, 1, 2, 3], [5, 6, 7, 8, 9]]) == [0, 5]
    assert candidate(nums = [[-1, -2, -3, -4, -5], [-10, -20, -30, -40, -50], [-100, -200, -300, -400, -500]]) == [-100, -5]
    assert candidate(nums = [[1, 10, 20, 30, 40], [2, 12, 22, 32, 42], [3, 13, 23, 33, 43]]) == [1, 3]
    assert candidate(nums = [[1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10, 12], [0, 9, 12, 20, 24, 26], [5, 18, 22, 30, 35, 40]]) == [5, 9]
    assert candidate(nums = [[-1000, -500, -250, -100, -50, -25, -10, -5, -2, -1, 0, 1, 2, 5, 10, 25, 50, 100, 250, 500, 1000], [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]]) == [1000, 1000]
    assert candidate(nums = [[-1000, -500, -250, -100, -50, -25, 0, 25, 50, 100, 250, 500, 1000], [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000], [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500]]) == [500, 500]
    assert candidate(nums = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]) == [1, 10]
    assert candidate(nums = [[1, 20, 30], [2, 25, 35], [3, 30, 40], [4, 35, 45], [5, 40, 50]]) == [1, 5]
    assert candidate(nums = [[100, 200, 300, 400, 500], [50, 150, 250, 350, 450], [25, 75, 125, 175, 225]]) == [50, 100]
    assert candidate(nums = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 5, 7, 9, 11], [4, 6, 8, 10, 12]]) == [3, 4]
    assert candidate(nums = [[1, 4, 10, 14], [0, 9, 10, 20, 24], [5, 18, 22, 30], [3, 13, 15, 17]]) == [0, 5]
    assert candidate(nums = [[1, 4, 7, 10, 13], [2, 5, 8, 11, 14], [3, 6, 9, 12, 15]]) == [1, 3]
    assert candidate(nums = [[-1000, -900, -800, -700, -600, -500, -400, -300, -200, -100], [0, 100, 200, 300, 400, 500, 600, 700, 800, 900], [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]]) == [-100, 1000]
    assert candidate(nums = [[1, 10, 19, 28, 37], [2, 11, 20, 29, 38], [3, 12, 21, 30, 39], [4, 13, 22, 31, 40], [5, 14, 23, 32, 41]]) == [1, 5]
    assert candidate(nums = [[-10, -5, 0, 5, 10], [-20, -15, -10, -5, 0], [1, 6, 11, 16, 21]]) == [0, 1]
    assert candidate(nums = [[10, 20, 30, 40, 50], [15, 25, 35, 45, 55], [20, 30, 40, 50, 60], [5, 10, 15, 20, 25]]) == [15, 20]
    assert candidate(nums = [[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4], [-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3]]) == [-5, -5]
    assert candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]]) == [6, 6]
    assert candidate(nums = [[100, 200, 300, 400], [50, 150, 250, 350], [25, 125, 225, 325, 425]]) == [100, 150]
    assert candidate(nums = [[1, 4, 7, 10, 13, 16, 19, 22, 25, 28], [2, 5, 8, 11, 14, 17, 20, 23, 26, 29], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]]) == [1, 3]
    assert candidate(nums = [[-100000, 0, 100000], [-99999, 99999], [-99998, 99998], [-99997, 99997]]) == [-100000, -99997]
    assert candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]) == [50, 51]
    assert candidate(nums = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105]]) == [0, 5]
    assert candidate(nums = [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [5, 5, 5, 5, 5]]) == [1, 5]
    assert candidate(nums = [[1, 100000], [2, 99999], [3, 99998], [4, 99997], [5, 99996]]) == [1, 5]
    assert candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]) == [1, 1]
    assert candidate(nums = [[-100, -50, 0, 50, 100], [5, 15, 25, 35, 45], [1, 2, 3, 4, 5], [0, 0, 0, 0, 0]]) == [0, 5]
    assert candidate(nums = [[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]) == [0, 0]
    assert candidate(nums = [[-1, -2, -3, -4, -5], [-6, -7, -8, -9, -10], [-11, -12, -13, -14, -15], [-16, -17, -18, -19, -20]]) == [-16, -5]
    assert candidate(nums = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5]]) == [1, 5]
    assert candidate(nums = [[1, 10, 20, 30, 40], [5, 15, 25, 35, 45], [10, 20, 30, 40, 50], [5, 15, 25, 35, 45]]) == [5, 10]
    assert candidate(nums = [[1, 3, 5, 7, 9, 11, 13, 15, 17, 19], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]) == [1, 2]
    assert candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]) == [3, 3]
    assert candidate(nums = [[10, 20, 30], [11, 21, 31], [12, 22, 32], [13, 23, 33], [14, 24, 34], [15, 25, 35], [16, 26, 36], [17, 27, 37], [18, 28, 38], [19, 29, 39]]) == [10, 19]
    assert candidate(nums = [[1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], [2, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101], [3, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102], [4, 13, 23, 33, 43, 53, 63, 73, 83, 93, 103], [5, 14, 24, 34, 44, 54, 64, 74, 84, 94, 104]]) == [1, 5]
    assert candidate(nums = [[-1, 0, 1], [-2, -1, 0, 1, 2], [-3, -2, -1, 0, 1, 2, 3]]) == [-1, -1]
    assert candidate(nums = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]) == [5, 21]
    assert candidate(nums = [[-100, -90, -80, -70, -60], [-95, -85, -75, -65, -55], [-90, -80, -70, -60, -50], [-85, -75, -65, -55, -45]]) == [-90, -85]
    assert candidate(nums = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]]) == [10, 21]
    assert candidate(nums = [[-10, -5, 0, 5, 10], [1, 3, 6, 9, 12], [2, 4, 7, 11, 13], [0, 8, 16, 24, 32]]) == [0, 2]
    assert candidate(nums = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]) == [1, 10]
    assert candidate(nums = [[100, 200, 300], [150, 250, 350], [200, 250, 300, 350]]) == [150, 200]
    assert candidate(nums = [[-100000, 100000], [-90000, 90000], [-80000, 80000], [-70000, 70000], [-60000, 60000]]) == [-100000, -60000]
    assert candidate(nums = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15]]) == [1, 15]


