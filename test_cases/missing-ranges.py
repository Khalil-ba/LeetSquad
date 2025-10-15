def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1],lower = -2,upper = 2) == [[-2, -2], [2, 2]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1],lower = -2,upper = 2) == [[-2, -2], [2, 2]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 7, 11, 14],lower = 0,upper = 15) == [[0, 4], [6, 6], [8, 10], [12, 13], [15, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 7, 11, 14],lower = 0,upper = 15) == [[0, 4], [6, 6], [8, 10], [12, 13], [15, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5],lower = 1,upper = 5) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5],lower = 1,upper = 5) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 2, 4, 6, 8],lower = 0,upper = 10) == [[1, 1], [3, 3], [5, 5], [7, 7], [9, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 2, 4, 6, 8],lower = 0,upper = 10) == [[1, 1], [3, 3], [5, 5], [7, 7], [9, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1, 0, 1],lower = -3,upper = 3) == [[-3, -2], [2, 3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1, 0, 1],lower = -3,upper = 3) == [[-3, -2], [2, 3]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [],lower = 1,upper = 1) == [[1, 1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [],lower = 1,upper = 1) == [[1, 1]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7],lower = 0,upper = 8) == [[0, 0], [2, 2], [4, 4], [6, 6], [8, 8]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7],lower = 0,upper = 8) == [[0, 0], [2, 2], [4, 4], [6, 6], [8, 8]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30],lower = 5,upper = 35) == [[5, 9], [11, 19], [21, 29], [31, 35]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30],lower = 5,upper = 35) == [[5, 9], [11, 19], [21, 29], [31, 35]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 8, 16],lower = 0,upper = 31) == [[0, 0], [3, 3], [5, 7], [9, 15], [17, 31]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 8, 16],lower = 0,upper = 31) == [[0, 0], [3, 3], [5, 7], [9, 15], [17, 31]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 0, 10],lower = -20,upper = 20) == [[-20, -11], [-9, -1], [1, 9], [11, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 0, 10],lower = -20,upper = 20) == [[-20, -11], [-9, -1], [1, 9], [11, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9],lower = 0,upper = 10) == [[0, 0], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9],lower = 0,upper = 10) == [[0, 0], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [],lower = -3,upper = 3) == [[-3, 3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [],lower = -3,upper = 3) == [[-3, 3]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 1,upper = 10) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 1,upper = 10) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 4, 6, 8],lower = 0,upper = 10) == [[0, 0], [3, 3], [5, 5], [7, 7], [9, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 4, 6, 8],lower = 0,upper = 10) == [[0, 0], [3, 3], [5, 5], [7, 7], [9, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1],lower = 0,upper = 3) == [[0, 0], [2, 3]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1],lower = 0,upper = 3) == [[0, 0], [2, 3]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3],lower = 0,upper = 5) == [[0, 0], [4, 5]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3],lower = 0,upper = 5) == [[0, 0], [4, 5]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-1],lower = -1,upper = -1) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-1],lower = -1,upper = -1) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],lower = 5,upper = 55) == [[5, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 55]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],lower = 5,upper = 55) == [[5, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 55]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 3, 50, 75],lower = 0,upper = 99) == [[2, 2], [4, 49], [51, 74], [76, 99]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 3, 50, 75],lower = 0,upper = 99) == [[2, 2], [4, 49], [51, 74], [76, 99]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 6, 7, 9, 11, 15, 19],lower = 1,upper = 19) == [[2, 3], [5, 5], [8, 8], [10, 10], [12, 14], [16, 18]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 6, 7, 9, 11, 15, 19],lower = 1,upper = 19) == [[2, 3], [5, 5], [8, 8], [10, 10], [12, 14], [16, 18]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 5, 7, 9, 12, 15],lower = -5,upper = 20) == [[-5, 0], [3, 4], [6, 6], [8, 8], [10, 11], [13, 14], [16, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 5, 7, 9, 12, 15],lower = -5,upper = 20) == [[-5, 0], [3, 4], [6, 6], [8, 8], [10, 11], [13, 14], [16, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45],lower = 0,upper = 50) == [[0, 0], [2, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 34], [36, 39], [41, 44], [46, 50]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45],lower = 0,upper = 50) == [[0, 0], [2, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 34], [36, 39], [41, 44], [46, 50]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000],lower = 999999999,upper = 1000000001) == [[999999999, 999999999], [1000000001, 1000000001]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000],lower = 999999999,upper = 1000000001) == [[999999999, 999999999], [1000000001, 1000000001]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [],lower = -1000,upper = 1000) == [[-1000, 1000]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [],lower = -1000,upper = 1000) == [[-1000, 1000]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],lower = 0,upper = 65) == [[0, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 34], [36, 39], [41, 44], [46, 49], [51, 54], [56, 59], [61, 65]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],lower = 0,upper = 65) == [[0, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 34], [36, 39], [41, 44], [46, 49], [51, 54], [56, 59], [61, 65]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = -10,upper = 20) == [[-10, 0], [11, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = -10,upper = 20) == [[-10, 0], [11, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45],lower = 0,upper = 50) == [[0, 4], [6, 14], [16, 24], [26, 34], [36, 44], [46, 50]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45],lower = 0,upper = 50) == [[0, 4], [6, 14], [16, 24], [26, 34], [36, 44], [46, 50]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21],lower = 1,upper = 25) == [[1, 2], [4, 5], [7, 8], [10, 11], [13, 14], [16, 17], [19, 20], [22, 25]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21],lower = 1,upper = 25) == [[1, 2], [4, 5], [7, 8], [10, 11], [13, 14], [16, 17], [19, 20], [22, 25]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 8, 13, 21, 34, 55, 89],lower = 1,upper = 100) == [[1, 1], [4, 4], [6, 7], [9, 12], [14, 20], [22, 33], [35, 54], [56, 88], [90, 100]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 8, 13, 21, 34, 55, 89],lower = 1,upper = 100) == [[1, 1], [4, 4], [6, 7], [9, 12], [14, 20], [22, 33], [35, 54], [56, 88], [90, 100]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],lower = 0,upper = 10) == [[0, 0], [10, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],lower = 0,upper = 10) == [[0, 0], [10, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],lower = 1,upper = 50) == [[1, 1], [4, 4], [6, 6], [8, 10], [12, 12], [14, 16], [18, 18], [20, 22], [24, 28], [30, 30], [32, 36], [38, 40], [42, 42], [44, 46], [48, 50]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],lower = 1,upper = 50) == [[1, 1], [4, 4], [6, 6], [8, 10], [12, 12], [14, 16], [18, 18], [20, 22], [24, 28], [30, 30], [32, 36], [38, 40], [42, 42], [44, 46], [48, 50]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 10],lower = -20,upper = 20) == [[-20, -11], [-9, 9], [11, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 10],lower = -20,upper = 20) == [[-20, -11], [-9, 9], [11, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55],lower = 0,upper = 60) == [[0, 4], [6, 14], [16, 24], [26, 34], [36, 44], [46, 54], [56, 60]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55],lower = 0,upper = 60) == [[0, 4], [6, 14], [16, 24], [26, 34], [36, 44], [46, 54], [56, 60]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 9, 14, 19, 24, 29],lower = 0,upper = 34) == [[0, 4], [6, 8], [10, 13], [15, 18], [20, 23], [25, 28], [30, 34]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 9, 14, 19, 24, 29],lower = 0,upper = 34) == [[0, 4], [6, 8], [10, 13], [15, 18], [20, 23], [25, 28], [30, 34]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 100, 150, 200, 250],lower = 0,upper = 300) == [[0, 49], [51, 99], [101, 149], [151, 199], [201, 249], [251, 300]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 100, 150, 200, 250],lower = 0,upper = 300) == [[0, 49], [51, 99], [101, 149], [151, 199], [201, 249], [251, 300]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25],lower = 1,upper = 29) == [[1, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25],lower = 1,upper = 29) == [[1, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],lower = 0,upper = 33) == [[0, 2], [4, 5], [7, 8], [10, 11], [13, 14], [16, 17], [19, 20], [22, 23], [25, 26], [28, 29], [31, 33]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],lower = 0,upper = 33) == [[0, 2], [4, 5], [7, 8], [10, 11], [13, 14], [16, 17], [19, 20], [22, 23], [25, 26], [28, 29], [31, 33]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = -5,upper = 15) == [[-5, 0], [11, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = -5,upper = 15) == [[-5, 0], [11, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],lower = 50,upper = 550) == [[50, 99], [101, 199], [201, 299], [301, 399], [401, 499], [501, 550]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],lower = 50,upper = 550) == [[50, 99], [101, 199], [201, 299], [301, 399], [401, 499], [501, 550]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],lower = 0,upper = 21) == [[0, 0], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16], [18, 18], [20, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],lower = 0,upper = 21) == [[0, 0], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16], [18, 18], [20, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],lower = -10,upper = 25) == [[-10, 0], [16, 25]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],lower = -10,upper = 25) == [[-10, 0], [16, 25]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55],lower = 0,upper = 60) == [[0, 4], [6, 14], [16, 24], [26, 34], [36, 44], [46, 54], [56, 60]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55],lower = 0,upper = 60) == [[0, 4], [6, 14], [16, 24], [26, 34], [36, 44], [46, 54], [56, 60]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],lower = 0,upper = 60) == [[0, 0], [2, 2], [4, 5], [7, 9], [11, 14], [16, 20], [22, 27], [29, 35], [37, 44], [46, 54], [56, 60]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],lower = 0,upper = 60) == [[0, 0], [2, 2], [4, 5], [7, 9], [11, 14], [16, 20], [22, 27], [29, 35], [37, 44], [46, 54], [56, 60]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [8, 16, 24, 32, 40, 48],lower = 0,upper = 56) == [[0, 7], [9, 15], [17, 23], [25, 31], [33, 39], [41, 47], [49, 56]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [8, 16, 24, 32, 40, 48],lower = 0,upper = 56) == [[0, 7], [9, 15], [17, 23], [25, 31], [33, 39], [41, 47], [49, 56]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000],lower = 0,upper = 100000) == [[0, 0], [2, 9], [11, 99], [101, 999], [1001, 9999], [10001, 100000]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000],lower = 0,upper = 100000) == [[0, 0], [2, 9], [11, 99], [101, 999], [1001, 9999], [10001, 100000]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 6, 9, 12, 15],lower = 2,upper = 18) == [[2, 2], [4, 5], [7, 8], [10, 11], [13, 14], [16, 18]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 6, 9, 12, 15],lower = 2,upper = 18) == [[2, 2], [4, 5], [7, 8], [10, 11], [13, 14], [16, 18]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],lower = 0,upper = 500) == [[0, 99], [101, 199], [201, 299], [301, 399], [401, 499]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],lower = 0,upper = 500) == [[0, 99], [101, 199], [201, 299], [301, 399], [401, 499]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],lower = 1,upper = 51) == [[1, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 34], [36, 39], [41, 44], [46, 49], [51, 51]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],lower = 1,upper = 51) == [[1, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 34], [36, 39], [41, 44], [46, 49], [51, 51]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 0,upper = 10) == [[0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 0,upper = 10) == [[0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [],lower = 0,upper = 0) == [[0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [],lower = 0,upper = 0) == [[0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400],lower = 50,upper = 500) == [[50, 99], [101, 199], [201, 299], [301, 399], [401, 500]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400],lower = 50,upper = 500) == [[50, 99], [101, 199], [201, 299], [301, 399], [401, 500]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1000000000],lower = 0,upper = 1000000000) == [[0, 999999999]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1000000000],lower = 0,upper = 1000000000) == [[0, 999999999]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 0,upper = 0) == [[0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 0,upper = 0) == [[0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 0,upper = 25) == [[21, 25]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 0,upper = 25) == [[21, 25]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 0,upper = 15) == [[11, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 0,upper = 15) == [[11, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],lower = 99,upper = 501) == [[99, 99], [101, 199], [201, 299], [301, 399], [401, 499], [501, 501]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],lower = 99,upper = 501) == [[99, 99], [101, 199], [201, 299], [301, 399], [401, 499], [501, 501]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 9, 16, 25, 36],lower = 0,upper = 49) == [[0, 0], [2, 3], [5, 8], [10, 15], [17, 24], [26, 35], [37, 49]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 9, 16, 25, 36],lower = 0,upper = 49) == [[0, 0], [2, 3], [5, 8], [10, 15], [17, 24], [26, 35], [37, 49]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60],lower = 5,upper = 65) == [[5, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 65]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60],lower = 5,upper = 65) == [[5, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 65]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25],lower = 1,upper = 30) == [[1, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 30]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25],lower = 1,upper = 30) == [[1, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 30]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],lower = 0,upper = 120) == [[0, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 69], [71, 79], [81, 89], [91, 99], [101, 109], [111, 120]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],lower = 0,upper = 120) == [[0, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 69], [71, 79], [81, 89], [91, 99], [101, 109], [111, 120]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000],lower = 2,upper = 9999) == [[2, 9], [11, 99], [101, 999], [1001, 9999]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000],lower = 2,upper = 9999) == [[2, 9], [11, 99], [101, 999], [1001, 9999]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 11, 15],lower = 0,upper = 20) == [[0, 0], [2, 2], [4, 6], [8, 10], [12, 14], [16, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 11, 15],lower = 0,upper = 20) == [[0, 0], [2, 2], [4, 6], [8, 10], [12, 14], [16, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],lower = 0,upper = 120) == [[0, 0], [2, 3], [5, 8], [10, 15], [17, 24], [26, 35], [37, 48], [50, 63], [65, 80], [82, 99], [101, 120]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],lower = 0,upper = 120) == [[0, 0], [2, 3], [5, 8], [10, 15], [17, 24], [26, 35], [37, 48], [50, 63], [65, 80], [82, 99], [101, 120]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 1,upper = 10) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 1,upper = 10) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 8, 16, 32, 64, 128],lower = 0,upper = 255) == [[0, 0], [2, 3], [5, 7], [9, 15], [17, 31], [33, 63], [65, 127], [129, 255]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 8, 16, 32, 64, 128],lower = 0,upper = 255) == [[0, 0], [2, 3], [5, 7], [9, 15], [17, 31], [33, 63], [65, 127], [129, 255]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],lower = 0,upper = 15) == [[0, 4], [15, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],lower = 0,upper = 15) == [[0, 4], [15, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10],lower = 10,upper = 10) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10],lower = 10,upper = 10) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 0,upper = 15) == [[0, 0], [11, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 0,upper = 15) == [[0, 0], [11, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],lower = 0,upper = 60) == [[0, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 60]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],lower = 0,upper = 60) == [[0, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 60]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 3, 6, 9, 12, 15, 18, 21],lower = -1,upper = 25) == [[-1, -1], [1, 2], [4, 5], [7, 8], [10, 11], [13, 14], [16, 17], [19, 20], [22, 25]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 3, 6, 9, 12, 15, 18, 21],lower = -1,upper = 25) == [[-1, -1], [1, 2], [4, 5], [7, 8], [10, 11], [13, 14], [16, 17], [19, 20], [22, 25]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 5,upper = 105) == [[5, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 69], [71, 79], [81, 89], [91, 99], [101, 105]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 5,upper = 105) == [[5, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 69], [71, 79], [81, 89], [91, 99], [101, 105]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 7, 11, 15, 19],lower = 1,upper = 24) == [[1, 2], [4, 6], [8, 10], [12, 14], [16, 18], [20, 24]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 7, 11, 15, 19],lower = 1,upper = 24) == [[1, 2], [4, 6], [8, 10], [12, 14], [16, 18], [20, 24]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 5, 10, 20, 30],lower = 1,upper = 35) == [[1, 1], [3, 4], [6, 9], [11, 19], [21, 29], [31, 35]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 5, 10, 20, 30],lower = 1,upper = 35) == [[1, 1], [3, 4], [6, 9], [11, 19], [21, 29], [31, 35]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000],lower = -1000,upper = 20000) == [[-1000, 0], [2, 9], [11, 99], [101, 999], [1001, 9999], [10001, 20000]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000],lower = -1000,upper = 20000) == [[-1000, 0], [2, 9], [11, 99], [101, 999], [1001, 9999], [10001, 20000]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],lower = 0,upper = 50) == [[0, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 34], [36, 39], [41, 44], [46, 49]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],lower = 0,upper = 50) == [[0, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 34], [36, 39], [41, 44], [46, 49]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],lower = 1,upper = 21) == [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17], [19, 19], [21, 21]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],lower = 1,upper = 21) == [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17], [19, 19], [21, 21]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 5,upper = 105) == [[5, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 69], [71, 79], [81, 89], [91, 99], [101, 105]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 5,upper = 105) == [[5, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 69], [71, 79], [81, 89], [91, 99], [101, 105]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, -5, -1, 3, 7, 10, 20],lower = -20,upper = 25) == [[-20, -11], [-9, -6], [-4, -2], [0, 2], [4, 6], [8, 9], [11, 19], [21, 25]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, -5, -1, 3, 7, 10, 20],lower = -20,upper = 25) == [[-20, -11], [-9, -6], [-4, -2], [0, 2], [4, 6], [8, 9], [11, 19], [21, 25]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],lower = 5,upper = 105) == [[5, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 34], [36, 39], [41, 44], [46, 49], [51, 54], [56, 59], [61, 64], [66, 69], [71, 74], [76, 79], [81, 84], [86, 89], [91, 94], [96, 99], [101, 105]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],lower = 5,upper = 105) == [[5, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 34], [36, 39], [41, 44], [46, 49], [51, 54], [56, 59], [61, 64], [66, 69], [71, 74], [76, 79], [81, 84], [86, 89], [91, 94], [96, 99], [101, 105]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 0,upper = 25) == [[0, 0], [21, 25]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 0,upper = 25) == [[0, 0], [21, 25]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 6, 8, 9, 11],lower = 0,upper = 15) == [[0, 0], [4, 4], [7, 7], [10, 10], [12, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 6, 8, 9, 11],lower = 0,upper = 15) == [[0, 0], [4, 4], [7, 7], [10, 10], [12, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],lower = 1,upper = 2048) == [[1, 1], [3, 3], [5, 7], [9, 15], [17, 31], [33, 63], [65, 127], [129, 255], [257, 511], [513, 1023], [1025, 2048]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],lower = 1,upper = 2048) == [[1, 1], [3, 3], [5, 7], [9, 15], [17, 31], [33, 63], [65, 127], [129, 255], [257, 511], [513, 1023], [1025, 2048]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [2, 6, 10, 14, 18],lower = 0,upper = 25) == [[0, 1], [3, 5], [7, 9], [11, 13], [15, 17], [19, 25]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [2, 6, 10, 14, 18],lower = 0,upper = 25) == [[0, 1], [3, 5], [7, 9], [11, 13], [15, 17], [19, 25]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000],lower = 5,upper = 9995) == [[2, 9], [11, 99], [101, 999], [1001, 9999]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000],lower = 5,upper = 9995) == [[2, 9], [11, 99], [101, 999], [1001, 9999]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 0,upper = 20) == [[0, 0]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 0,upper = 20) == [[0, 0]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],lower = -5,upper = 15) == [[-5, -1], [10, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],lower = -5,upper = 15) == [[-5, -1], [10, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 101, 102, 103, 104, 105],lower = 95,upper = 110) == [[95, 99], [106, 110]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 101, 102, 103, 104, 105],lower = 95,upper = 110) == [[95, 99], [106, 110]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 5, 10, 20, 30, 40, 50],lower = 0,upper = 55) == [[0, 0], [4, 4], [6, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 55]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 5, 10, 20, 30, 40, 50],lower = 0,upper = 55) == [[0, 0], [4, 4], [6, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 55]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90],lower = 5,upper = 95) == [[5, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 69], [71, 79], [81, 89], [91, 95]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90],lower = 5,upper = 95) == [[5, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 69], [71, 79], [81, 89], [91, 95]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],lower = 99,upper = 500) == [[99, 99], [101, 199], [201, 299], [301, 399], [401, 499]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],lower = 99,upper = 500) == [[99, 99], [101, 199], [201, 299], [301, 399], [401, 499]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],lower = 0,upper = 10) == [[10, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],lower = 0,upper = 10) == [[10, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45],lower = 0,upper = 55) == [[0, 4], [6, 14], [16, 24], [26, 34], [36, 44], [46, 55]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45],lower = 0,upper = 55) == [[0, 4], [6, 14], [16, 24], [26, 34], [36, 44], [46, 55]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5],lower = 0,upper = 10) == [[0, 4], [6, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5],lower = 0,upper = 10) == [[0, 4], [6, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 7, 15, 31, 63, 127],lower = 0,upper = 255) == [[0, 0], [2, 2], [4, 6], [8, 14], [16, 30], [32, 62], [64, 126], [128, 255]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 7, 15, 31, 63, 127],lower = 0,upper = 255) == [[0, 0], [2, 2], [4, 6], [8, 14], [16, 30], [32, 62], [64, 126], [128, 255]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25],lower = 0,upper = 100) == [[0, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 100]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25],lower = 0,upper = 100) == [[0, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 100]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 0,upper = 10) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 0,upper = 10) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [50, 100, 150, 200, 250],lower = 45,upper = 255) == [[45, 49], [51, 99], [101, 149], [151, 199], [201, 249], [251, 255]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [50, 100, 150, 200, 250],lower = 45,upper = 255) == [[45, 49], [51, 99], [101, 149], [151, 199], [201, 249], [251, 255]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [],lower = -10,upper = 10) == [[-10, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [],lower = -10,upper = 10) == [[-10, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],lower = 5,upper = 25) == [[5, 9], [20, 25]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],lower = 5,upper = 25) == [[5, 9], [20, 25]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [3, 8, 13, 18, 23, 28],lower = 0,upper = 30) == [[0, 2], [4, 7], [9, 12], [14, 17], [19, 22], [24, 27], [29, 30]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [3, 8, 13, 18, 23, 28],lower = 0,upper = 30) == [[0, 2], [4, 7], [9, 12], [14, 17], [19, 22], [24, 27], [29, 30]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 21,upper = 30) == [[21, 30]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 21,upper = 30) == [[21, 30]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],lower = 0,upper = 9) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],lower = 0,upper = 9) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000],lower = 1,upper = 10000) == [[2, 9], [11, 99], [101, 999], [1001, 9999]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000],lower = 1,upper = 10000) == [[2, 9], [11, 99], [101, 999], [1001, 9999]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 20, 25, 30],lower = 0,upper = 50) == [[0, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 50]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 20, 25, 30],lower = 0,upper = 50) == [[0, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 50]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50],lower = 5,upper = 55) == [[5, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 55]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50],lower = 5,upper = 55) == [[5, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 55]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [],lower = -100,upper = 100) == [[-100, 100]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [],lower = -100,upper = 100) == [[-100, 100]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-5, -3, -1, 1, 3, 5],lower = -10,upper = 10) == [[-10, -6], [-4, -4], [-2, -2], [0, 0], [2, 2], [4, 4], [6, 10]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-5, -3, -1, 1, 3, 5],lower = -10,upper = 10) == [[-10, -6], [-4, -4], [-2, -2], [0, 0], [2, 2], [4, 4], [6, 10]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 20,upper = 20) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 20,upper = 20) == []: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],lower = 101,upper = 499) == [[101, 199], [201, 299], [301, 399], [401, 499]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],lower = 101,upper = 499) == [[101, 199], [201, 299], [301, 399], [401, 499]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [],lower = -1,upper = 1) == [[-1, 1]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [],lower = -1,upper = 1) == [[-1, 1]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [500000000, 1000000000],lower = 400000000,upper = 1100000000) == [[400000000, 499999999], [500000001, 999999999], [1000000001, 1100000000]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [500000000, 1000000000],lower = 400000000,upper = 1100000000) == [[400000000, 499999999], [500000001, 999999999], [1000000001, 1100000000]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300],lower = 50,upper = 350) == [[50, 99], [101, 199], [201, 299], [301, 350]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300],lower = 50,upper = 350) == [[50, 99], [101, 199], [201, 299], [301, 350]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],lower = 0,upper = 30) == [[0, 0], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16], [18, 18], [20, 20], [22, 22], [24, 24], [26, 26], [28, 28], [30, 30]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],lower = 0,upper = 30) == [[0, 0], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16], [18, 18], [20, 20], [22, 22], [24, 24], [26, 26], [28, 28], [30, 30]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 2, 3, 6, 10, 15, 21, 25, 30, 35, 40, 45, 50],lower = 1,upper = 50) == [[4, 5], [7, 9], [11, 14], [16, 20], [22, 24], [26, 29], [31, 34], [36, 39], [41, 44], [46, 49]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 2, 3, 6, 10, 15, 21, 25, 30, 35, 40, 45, 50],lower = 1,upper = 50) == [[4, 5], [7, 9], [11, 14], [16, 20], [22, 24], [26, 29], [31, 34], [36, 39], [41, 44], [46, 49]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [-10, 0, 10, 20, 30],lower = -20,upper = 40) == [[-20, -11], [-9, -1], [1, 9], [11, 19], [21, 29], [31, 40]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [-10, 0, 10, 20, 30],lower = -20,upper = 40) == [[-20, -11], [-9, -1], [1, 9], [11, 19], [21, 29], [31, 40]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 6, 9, 11, 13, 16, 19],lower = 0,upper = 20) == [[0, 0], [2, 3], [5, 5], [7, 8], [10, 10], [12, 12], [14, 15], [17, 18], [20, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 6, 9, 11, 13, 16, 19],lower = 0,upper = 20) == [[0, 0], [2, 3], [5, 5], [7, 8], [10, 10], [12, 12], [14, 15], [17, 18], [20, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 11, 17, 23, 29, 35, 41, 47],lower = 0,upper = 52) == [[0, 4], [6, 10], [12, 16], [18, 22], [24, 28], [30, 34], [36, 40], [42, 46], [48, 52]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 11, 17, 23, 29, 35, 41, 47],lower = 0,upper = 52) == [[0, 4], [6, 10], [12, 16], [18, 22], [24, 28], [30, 34], [36, 40], [42, 46], [48, 52]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90],lower = 0,upper = 100) == [[0, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 69], [71, 79], [81, 89], [91, 100]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90],lower = 0,upper = 100) == [[0, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 69], [71, 79], [81, 89], [91, 100]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 10, 15, 25, 30],lower = 0,upper = 50) == [[0, 4], [6, 9], [11, 14], [16, 24], [26, 29], [31, 50]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 10, 15, 25, 30],lower = 0,upper = 50) == [[0, 4], [6, 9], [11, 14], [16, 24], [26, 29], [31, 50]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 10, 100, 1000, 10000],lower = 0,upper = 10001) == [[0, 0], [2, 9], [11, 99], [101, 999], [1001, 9999], [10001, 10001]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 10, 100, 1000, 10000],lower = 0,upper = 10001) == [[0, 0], [2, 9], [11, 99], [101, 999], [1001, 9999], [10001, 10001]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],lower = 0,upper = 20) == [[0, 0], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16], [18, 18], [20, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],lower = 0,upper = 20) == [[0, 0], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16], [18, 18], [20, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [100, 200, 300, 400, 500],lower = 100,upper = 500) == [[101, 199], [201, 299], [301, 399], [401, 499]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [100, 200, 300, 400, 500],lower = 100,upper = 500) == [[101, 199], [201, 299], [301, 399], [401, 499]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],lower = 0,upper = 20) == [[0, 0], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16], [18, 18], [20, 20]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],lower = 0,upper = 20) == [[0, 0], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16], [18, 18], [20, 20]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],lower = 0,upper = 100) == [[0, 4], [6, 14], [16, 24], [26, 34], [36, 44], [46, 54], [56, 64], [66, 74], [76, 84], [86, 94], [96, 100]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],lower = 0,upper = 100) == [[0, 4], [6, 14], [16, 24], [26, 34], [36, 44], [46, 54], [56, 64], [66, 74], [76, 84], [86, 94], [96, 100]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 4, 7, 10, 13],lower = 0,upper = 15) == [[0, 0], [2, 3], [5, 6], [8, 9], [11, 12], [14, 15]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 4, 7, 10, 13],lower = 0,upper = 15) == [[0, 0], [2, 3], [5, 6], [8, 9], [11, 12], [14, 15]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 0,upper = 100) == [[0, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 69], [71, 79], [81, 89], [91, 99]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 0,upper = 100) == [[0, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 69], [71, 79], [81, 89], [91, 99]]: {e}')
    
    total += 1
    try:
        result = candidate(nums = [1, 5, 10, 15, 20, 25, 30],lower = -5,upper = 35) == [[-5, 0], [2, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 35]]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(nums = [1, 5, 10, 15, 20, 25, 30],lower = -5,upper = 35) == [[-5, 0], [2, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 35]]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(nums = [-1, 0, 1],lower = -2,upper = 2) == [[-2, -2], [2, 2]]
    assert candidate(nums = [5, 7, 11, 14],lower = 0,upper = 15) == [[0, 4], [6, 6], [8, 10], [12, 13], [15, 15]]
    assert candidate(nums = [1, 2, 3, 4, 5],lower = 1,upper = 5) == []
    assert candidate(nums = [0, 2, 4, 6, 8],lower = 0,upper = 10) == [[1, 1], [3, 3], [5, 5], [7, 7], [9, 10]]
    assert candidate(nums = [-1, 0, 1],lower = -3,upper = 3) == [[-3, -2], [2, 3]]
    assert candidate(nums = [],lower = 1,upper = 1) == [[1, 1]]
    assert candidate(nums = [1, 3, 5, 7],lower = 0,upper = 8) == [[0, 0], [2, 2], [4, 4], [6, 6], [8, 8]]
    assert candidate(nums = [10, 20, 30],lower = 5,upper = 35) == [[5, 9], [11, 19], [21, 29], [31, 35]]
    assert candidate(nums = [1, 2, 4, 8, 16],lower = 0,upper = 31) == [[0, 0], [3, 3], [5, 7], [9, 15], [17, 31]]
    assert candidate(nums = [-10, 0, 10],lower = -20,upper = 20) == [[-20, -11], [-9, -1], [1, 9], [11, 20]]
    assert candidate(nums = [1, 3, 5, 7, 9],lower = 0,upper = 10) == [[0, 0], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10]]
    assert candidate(nums = [],lower = -3,upper = 3) == [[-3, 3]]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 1,upper = 10) == []
    assert candidate(nums = [1, 2, 4, 6, 8],lower = 0,upper = 10) == [[0, 0], [3, 3], [5, 5], [7, 7], [9, 10]]
    assert candidate(nums = [1],lower = 0,upper = 3) == [[0, 0], [2, 3]]
    assert candidate(nums = [1, 2, 3],lower = 0,upper = 5) == [[0, 0], [4, 5]]
    assert candidate(nums = [-1],lower = -1,upper = -1) == []
    assert candidate(nums = [10, 20, 30, 40, 50],lower = 5,upper = 55) == [[5, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 55]]
    assert candidate(nums = [0, 1, 3, 50, 75],lower = 0,upper = 99) == [[2, 2], [4, 49], [51, 74], [76, 99]]
    assert candidate(nums = [1, 4, 6, 7, 9, 11, 15, 19],lower = 1,upper = 19) == [[2, 3], [5, 5], [8, 8], [10, 10], [12, 14], [16, 18]]
    assert candidate(nums = [1, 2, 5, 7, 9, 12, 15],lower = -5,upper = 20) == [[-5, 0], [3, 4], [6, 6], [8, 8], [10, 11], [13, 14], [16, 20]]
    assert candidate(nums = [1, 5, 10, 15, 20, 25, 30, 35, 40, 45],lower = 0,upper = 50) == [[0, 0], [2, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 34], [36, 39], [41, 44], [46, 50]]
    assert candidate(nums = [1000000000],lower = 999999999,upper = 1000000001) == [[999999999, 999999999], [1000000001, 1000000001]]
    assert candidate(nums = [],lower = -1000,upper = 1000) == [[-1000, 1000]]
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],lower = 0,upper = 65) == [[0, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 34], [36, 39], [41, 44], [46, 49], [51, 54], [56, 59], [61, 65]]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = -10,upper = 20) == [[-10, 0], [11, 20]]
    assert candidate(nums = [5, 15, 25, 35, 45],lower = 0,upper = 50) == [[0, 4], [6, 14], [16, 24], [26, 34], [36, 44], [46, 50]]
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21],lower = 1,upper = 25) == [[1, 2], [4, 5], [7, 8], [10, 11], [13, 14], [16, 17], [19, 20], [22, 25]]
    assert candidate(nums = [2, 3, 5, 8, 13, 21, 34, 55, 89],lower = 1,upper = 100) == [[1, 1], [4, 4], [6, 7], [9, 12], [14, 20], [22, 33], [35, 54], [56, 88], [90, 100]]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9],lower = 0,upper = 10) == [[0, 0], [10, 10]]
    assert candidate(nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],lower = 1,upper = 50) == [[1, 1], [4, 4], [6, 6], [8, 10], [12, 12], [14, 16], [18, 18], [20, 22], [24, 28], [30, 30], [32, 36], [38, 40], [42, 42], [44, 46], [48, 50]]
    assert candidate(nums = [-10, 10],lower = -20,upper = 20) == [[-20, -11], [-9, 9], [11, 20]]
    assert candidate(nums = [5, 15, 25, 35, 45, 55],lower = 0,upper = 60) == [[0, 4], [6, 14], [16, 24], [26, 34], [36, 44], [46, 54], [56, 60]]
    assert candidate(nums = [5, 9, 14, 19, 24, 29],lower = 0,upper = 34) == [[0, 4], [6, 8], [10, 13], [15, 18], [20, 23], [25, 28], [30, 34]]
    assert candidate(nums = [50, 100, 150, 200, 250],lower = 0,upper = 300) == [[0, 49], [51, 99], [101, 149], [151, 199], [201, 249], [251, 300]]
    assert candidate(nums = [5, 10, 15, 20, 25],lower = 1,upper = 29) == [[1, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29]]
    assert candidate(nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],lower = 0,upper = 33) == [[0, 2], [4, 5], [7, 8], [10, 11], [13, 14], [16, 17], [19, 20], [22, 23], [25, 26], [28, 29], [31, 33]]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = -5,upper = 15) == [[-5, 0], [11, 15]]
    assert candidate(nums = [100, 200, 300, 400, 500],lower = 50,upper = 550) == [[50, 99], [101, 199], [201, 299], [301, 399], [401, 499], [501, 550]]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],lower = 0,upper = 21) == [[0, 0], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16], [18, 18], [20, 20]]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],lower = -10,upper = 25) == [[-10, 0], [16, 25]]
    assert candidate(nums = [5, 15, 25, 35, 45, 55],lower = 0,upper = 60) == [[0, 4], [6, 14], [16, 24], [26, 34], [36, 44], [46, 54], [56, 60]]
    assert candidate(nums = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55],lower = 0,upper = 60) == [[0, 0], [2, 2], [4, 5], [7, 9], [11, 14], [16, 20], [22, 27], [29, 35], [37, 44], [46, 54], [56, 60]]
    assert candidate(nums = [8, 16, 24, 32, 40, 48],lower = 0,upper = 56) == [[0, 7], [9, 15], [17, 23], [25, 31], [33, 39], [41, 47], [49, 56]]
    assert candidate(nums = [1, 10, 100, 1000, 10000],lower = 0,upper = 100000) == [[0, 0], [2, 9], [11, 99], [101, 999], [1001, 9999], [10001, 100000]]
    assert candidate(nums = [3, 6, 9, 12, 15],lower = 2,upper = 18) == [[2, 2], [4, 5], [7, 8], [10, 11], [13, 14], [16, 18]]
    assert candidate(nums = [100, 200, 300, 400, 500],lower = 0,upper = 500) == [[0, 99], [101, 199], [201, 299], [301, 399], [401, 499]]
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],lower = 1,upper = 51) == [[1, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 34], [36, 39], [41, 44], [46, 49], [51, 51]]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 0,upper = 10) == [[0, 0]]
    assert candidate(nums = [],lower = 0,upper = 0) == [[0, 0]]
    assert candidate(nums = [100, 200, 300, 400],lower = 50,upper = 500) == [[50, 99], [101, 199], [201, 299], [301, 399], [401, 500]]
    assert candidate(nums = [1000000000],lower = 0,upper = 1000000000) == [[0, 999999999]]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 0,upper = 0) == [[0, 0]]
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 0,upper = 25) == [[21, 25]]
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 0,upper = 15) == [[11, 15]]
    assert candidate(nums = [100, 200, 300, 400, 500],lower = 99,upper = 501) == [[99, 99], [101, 199], [201, 299], [301, 399], [401, 499], [501, 501]]
    assert candidate(nums = [1, 4, 9, 16, 25, 36],lower = 0,upper = 49) == [[0, 0], [2, 3], [5, 8], [10, 15], [17, 24], [26, 35], [37, 49]]
    assert candidate(nums = [10, 20, 30, 40, 50, 60],lower = 5,upper = 65) == [[5, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 65]]
    assert candidate(nums = [5, 10, 15, 20, 25],lower = 1,upper = 30) == [[1, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 30]]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],lower = 0,upper = 120) == [[0, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 69], [71, 79], [81, 89], [91, 99], [101, 109], [111, 120]]
    assert candidate(nums = [1, 10, 100, 1000, 10000],lower = 2,upper = 9999) == [[2, 9], [11, 99], [101, 999], [1001, 9999]]
    assert candidate(nums = [1, 3, 7, 11, 15],lower = 0,upper = 20) == [[0, 0], [2, 2], [4, 6], [8, 10], [12, 14], [16, 20]]
    assert candidate(nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],lower = 0,upper = 120) == [[0, 0], [2, 3], [5, 8], [10, 15], [17, 24], [26, 35], [37, 48], [50, 63], [65, 80], [82, 99], [101, 120]]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 1,upper = 10) == []
    assert candidate(nums = [1, 4, 8, 16, 32, 64, 128],lower = 0,upper = 255) == [[0, 0], [2, 3], [5, 7], [9, 15], [17, 31], [33, 63], [65, 127], [129, 255]]
    assert candidate(nums = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],lower = 0,upper = 15) == [[0, 4], [15, 15]]
    assert candidate(nums = [10],lower = 10,upper = 10) == []
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 0,upper = 15) == [[0, 0], [11, 15]]
    assert candidate(nums = [10, 20, 30, 40, 50],lower = 0,upper = 60) == [[0, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 60]]
    assert candidate(nums = [0, 3, 6, 9, 12, 15, 18, 21],lower = -1,upper = 25) == [[-1, -1], [1, 2], [4, 5], [7, 8], [10, 11], [13, 14], [16, 17], [19, 20], [22, 25]]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 5,upper = 105) == [[5, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 69], [71, 79], [81, 89], [91, 99], [101, 105]]
    assert candidate(nums = [3, 7, 11, 15, 19],lower = 1,upper = 24) == [[1, 2], [4, 6], [8, 10], [12, 14], [16, 18], [20, 24]]
    assert candidate(nums = [2, 5, 10, 20, 30],lower = 1,upper = 35) == [[1, 1], [3, 4], [6, 9], [11, 19], [21, 29], [31, 35]]
    assert candidate(nums = [1, 10, 100, 1000, 10000],lower = -1000,upper = 20000) == [[-1000, 0], [2, 9], [11, 99], [101, 999], [1001, 9999], [10001, 20000]]
    assert candidate(nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],lower = 0,upper = 50) == [[0, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 34], [36, 39], [41, 44], [46, 49]]
    assert candidate(nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],lower = 1,upper = 21) == [[1, 1], [3, 3], [5, 5], [7, 7], [9, 9], [11, 11], [13, 13], [15, 15], [17, 17], [19, 19], [21, 21]]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 5,upper = 105) == [[5, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 69], [71, 79], [81, 89], [91, 99], [101, 105]]
    assert candidate(nums = [-10, -5, -1, 3, 7, 10, 20],lower = -20,upper = 25) == [[-20, -11], [-9, -6], [-4, -2], [0, 2], [4, 6], [8, 9], [11, 19], [21, 25]]
    assert candidate(nums = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],lower = 5,upper = 105) == [[5, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 34], [36, 39], [41, 44], [46, 49], [51, 54], [56, 59], [61, 64], [66, 69], [71, 74], [76, 79], [81, 84], [86, 89], [91, 94], [96, 99], [101, 105]]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 0,upper = 25) == [[0, 0], [21, 25]]
    assert candidate(nums = [1, 2, 3, 5, 6, 8, 9, 11],lower = 0,upper = 15) == [[0, 0], [4, 4], [7, 7], [10, 10], [12, 15]]
    assert candidate(nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024],lower = 1,upper = 2048) == [[1, 1], [3, 3], [5, 7], [9, 15], [17, 31], [33, 63], [65, 127], [129, 255], [257, 511], [513, 1023], [1025, 2048]]
    assert candidate(nums = [2, 6, 10, 14, 18],lower = 0,upper = 25) == [[0, 1], [3, 5], [7, 9], [11, 13], [15, 17], [19, 25]]
    assert candidate(nums = [1, 10, 100, 1000, 10000],lower = 5,upper = 9995) == [[2, 9], [11, 99], [101, 999], [1001, 9999]]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 0,upper = 20) == [[0, 0]]
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],lower = -5,upper = 15) == [[-5, -1], [10, 15]]
    assert candidate(nums = [100, 101, 102, 103, 104, 105],lower = 95,upper = 110) == [[95, 99], [106, 110]]
    assert candidate(nums = [1, 2, 3, 5, 10, 20, 30, 40, 50],lower = 0,upper = 55) == [[0, 0], [4, 4], [6, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 55]]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90],lower = 5,upper = 95) == [[5, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 69], [71, 79], [81, 89], [91, 95]]
    assert candidate(nums = [100, 200, 300, 400, 500],lower = 99,upper = 500) == [[99, 99], [101, 199], [201, 299], [301, 399], [401, 499]]
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],lower = 0,upper = 10) == [[10, 10]]
    assert candidate(nums = [5, 15, 25, 35, 45],lower = 0,upper = 55) == [[0, 4], [6, 14], [16, 24], [26, 34], [36, 44], [46, 55]]
    assert candidate(nums = [5],lower = 0,upper = 10) == [[0, 4], [6, 10]]
    assert candidate(nums = [1, 3, 7, 15, 31, 63, 127],lower = 0,upper = 255) == [[0, 0], [2, 2], [4, 6], [8, 14], [16, 30], [32, 62], [64, 126], [128, 255]]
    assert candidate(nums = [5, 10, 15, 20, 25],lower = 0,upper = 100) == [[0, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 100]]
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],lower = 0,upper = 10) == []
    assert candidate(nums = [50, 100, 150, 200, 250],lower = 45,upper = 255) == [[45, 49], [51, 99], [101, 149], [151, 199], [201, 249], [251, 255]]
    assert candidate(nums = [],lower = -10,upper = 10) == [[-10, 10]]
    assert candidate(nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],lower = 5,upper = 25) == [[5, 9], [20, 25]]
    assert candidate(nums = [3, 8, 13, 18, 23, 28],lower = 0,upper = 30) == [[0, 2], [4, 7], [9, 12], [14, 17], [19, 22], [24, 27], [29, 30]]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 21,upper = 30) == [[21, 30]]
    assert candidate(nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],lower = 0,upper = 9) == []
    assert candidate(nums = [1, 10, 100, 1000, 10000],lower = 1,upper = 10000) == [[2, 9], [11, 99], [101, 999], [1001, 9999]]
    assert candidate(nums = [5, 10, 15, 20, 25, 30],lower = 0,upper = 50) == [[0, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 50]]
    assert candidate(nums = [10, 20, 30, 40, 50],lower = 5,upper = 55) == [[5, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 55]]
    assert candidate(nums = [],lower = -100,upper = 100) == [[-100, 100]]
    assert candidate(nums = [-5, -3, -1, 1, 3, 5],lower = -10,upper = 10) == [[-10, -6], [-4, -4], [-2, -2], [0, 0], [2, 2], [4, 4], [6, 10]]
    assert candidate(nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],lower = 20,upper = 20) == []
    assert candidate(nums = [100, 200, 300, 400, 500],lower = 101,upper = 499) == [[101, 199], [201, 299], [301, 399], [401, 499]]
    assert candidate(nums = [],lower = -1,upper = 1) == [[-1, 1]]
    assert candidate(nums = [500000000, 1000000000],lower = 400000000,upper = 1100000000) == [[400000000, 499999999], [500000001, 999999999], [1000000001, 1100000000]]
    assert candidate(nums = [100, 200, 300],lower = 50,upper = 350) == [[50, 99], [101, 199], [201, 299], [301, 350]]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29],lower = 0,upper = 30) == [[0, 0], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16], [18, 18], [20, 20], [22, 22], [24, 24], [26, 26], [28, 28], [30, 30]]
    assert candidate(nums = [1, 2, 3, 6, 10, 15, 21, 25, 30, 35, 40, 45, 50],lower = 1,upper = 50) == [[4, 5], [7, 9], [11, 14], [16, 20], [22, 24], [26, 29], [31, 34], [36, 39], [41, 44], [46, 49]]
    assert candidate(nums = [-10, 0, 10, 20, 30],lower = -20,upper = 40) == [[-20, -11], [-9, -1], [1, 9], [11, 19], [21, 29], [31, 40]]
    assert candidate(nums = [1, 4, 6, 9, 11, 13, 16, 19],lower = 0,upper = 20) == [[0, 0], [2, 3], [5, 5], [7, 8], [10, 10], [12, 12], [14, 15], [17, 18], [20, 20]]
    assert candidate(nums = [5, 11, 17, 23, 29, 35, 41, 47],lower = 0,upper = 52) == [[0, 4], [6, 10], [12, 16], [18, 22], [24, 28], [30, 34], [36, 40], [42, 46], [48, 52]]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90],lower = 0,upper = 100) == [[0, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 69], [71, 79], [81, 89], [91, 100]]
    assert candidate(nums = [5, 10, 15, 25, 30],lower = 0,upper = 50) == [[0, 4], [6, 9], [11, 14], [16, 24], [26, 29], [31, 50]]
    assert candidate(nums = [1, 10, 100, 1000, 10000],lower = 0,upper = 10001) == [[0, 0], [2, 9], [11, 99], [101, 999], [1001, 9999], [10001, 10001]]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],lower = 0,upper = 20) == [[0, 0], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16], [18, 18], [20, 20]]
    assert candidate(nums = [100, 200, 300, 400, 500],lower = 100,upper = 500) == [[101, 199], [201, 299], [301, 399], [401, 499]]
    assert candidate(nums = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],lower = 0,upper = 20) == [[0, 0], [2, 2], [4, 4], [6, 6], [8, 8], [10, 10], [12, 12], [14, 14], [16, 16], [18, 18], [20, 20]]
    assert candidate(nums = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95],lower = 0,upper = 100) == [[0, 4], [6, 14], [16, 24], [26, 34], [36, 44], [46, 54], [56, 64], [66, 74], [76, 84], [86, 94], [96, 100]]
    assert candidate(nums = [1, 4, 7, 10, 13],lower = 0,upper = 15) == [[0, 0], [2, 3], [5, 6], [8, 9], [11, 12], [14, 15]]
    assert candidate(nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],lower = 0,upper = 100) == [[0, 9], [11, 19], [21, 29], [31, 39], [41, 49], [51, 59], [61, 69], [71, 79], [81, 89], [91, 99]]
    assert candidate(nums = [1, 5, 10, 15, 20, 25, 30],lower = -5,upper = 35) == [[-5, 0], [2, 4], [6, 9], [11, 14], [16, 19], [21, 24], [26, 29], [31, 35]]


