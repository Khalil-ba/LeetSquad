def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],veganFriendly = 0,maxPrice = 50,maxDistance = 10) == [4, 3, 2, 1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],veganFriendly = 0,maxPrice = 50,maxDistance = 10) == [4, 3, 2, 1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],veganFriendly = 0,maxPrice = 30,maxDistance = 3) == [4, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],veganFriendly = 0,maxPrice = 30,maxDistance = 3) == [4, 5]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],veganFriendly = 1,maxPrice = 50,maxDistance = 10) == [3, 1, 5]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],veganFriendly = 1,maxPrice = 50,maxDistance = 10) == [3, 1, 5]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[100, 95, 1, 10, 1], [200, 94, 0, 20, 2], [300, 93, 1, 30, 3], [400, 92, 0, 40, 4], [500, 91, 1, 50, 5]],veganFriendly = 1,maxPrice = 50,maxDistance = 5) == [100, 300, 500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[100, 95, 1, 10, 1], [200, 94, 0, 20, 2], [300, 93, 1, 30, 3], [400, 92, 0, 40, 4], [500, 91, 1, 50, 5]],veganFriendly = 1,maxPrice = 50,maxDistance = 5) == [100, 300, 500]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[101, 9, 1, 25, 7], [102, 7, 0, 35, 12], [103, 9, 1, 20, 5], [104, 5, 0, 20, 8], [105, 9, 1, 20, 5], [106, 8, 1, 30, 3], [107, 6, 0, 35, 6]],veganFriendly = 1,maxPrice = 30,maxDistance = 8) == [105, 103, 101, 106]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[101, 9, 1, 25, 7], [102, 7, 0, 35, 12], [103, 9, 1, 20, 5], [104, 5, 0, 20, 8], [105, 9, 1, 20, 5], [106, 8, 1, 30, 3], [107, 6, 0, 35, 6]],veganFriendly = 1,maxPrice = 30,maxDistance = 8) == [105, 103, 101, 106]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[1001, 45, 1, 30, 12], [2002, 65, 0, 20, 6], [3003, 50, 1, 25, 7], [4004, 40, 0, 15, 4], [5005, 75, 1, 5, 2], [6006, 55, 0, 40, 22], [7007, 45, 1, 10, 16], [8008, 35, 0, 25, 12], [9009, 25, 1, 35, 22], [10010, 80, 1, 10, 6]],veganFriendly = 0,maxPrice = 45,maxDistance = 20) == [10010, 5005, 2002, 3003, 7007, 1001, 4004, 8008]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[1001, 45, 1, 30, 12], [2002, 65, 0, 20, 6], [3003, 50, 1, 25, 7], [4004, 40, 0, 15, 4], [5005, 75, 1, 5, 2], [6006, 55, 0, 40, 22], [7007, 45, 1, 10, 16], [8008, 35, 0, 25, 12], [9009, 25, 1, 35, 22], [10010, 80, 1, 10, 6]],veganFriendly = 0,maxPrice = 45,maxDistance = 20) == [10010, 5005, 2002, 3003, 7007, 1001, 4004, 8008]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[10001, 10, 1, 100, 100], [20002, 20, 0, 80, 90], [30003, 30, 1, 70, 80], [40004, 40, 0, 60, 70], [50005, 50, 1, 50, 60], [60006, 60, 0, 40, 50], [70007, 70, 1, 30, 40], [80008, 80, 0, 20, 30], [90009, 90, 1, 10, 20], [100010, 100, 1, 0, 10]],veganFriendly = 0,maxPrice = 100,maxDistance = 100) == [100010, 90009, 80008, 70007, 60006, 50005, 40004, 30003, 20002, 10001]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[10001, 10, 1, 100, 100], [20002, 20, 0, 80, 90], [30003, 30, 1, 70, 80], [40004, 40, 0, 60, 70], [50005, 50, 1, 50, 60], [60006, 60, 0, 40, 50], [70007, 70, 1, 30, 40], [80008, 80, 0, 20, 30], [90009, 90, 1, 10, 20], [100010, 100, 1, 0, 10]],veganFriendly = 0,maxPrice = 100,maxDistance = 100) == [100010, 90009, 80008, 70007, 60006, 50005, 40004, 30003, 20002, 10001]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[11, 3, 1, 20, 10], [12, 8, 1, 18, 8], [13, 5, 0, 15, 7], [14, 7, 0, 12, 6], [15, 9, 1, 9, 5]],veganFriendly = 1,maxPrice = 20,maxDistance = 10) == [15, 12, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[11, 3, 1, 20, 10], [12, 8, 1, 18, 8], [13, 5, 0, 15, 7], [14, 7, 0, 12, 6], [15, 9, 1, 9, 5]],veganFriendly = 1,maxPrice = 20,maxDistance = 10) == [15, 12, 11]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[401, 5, 1, 10, 10], [402, 6, 1, 15, 9], [403, 7, 1, 20, 8], [404, 8, 1, 25, 7], [405, 9, 1, 30, 6], [406, 10, 1, 35, 5]],veganFriendly = 1,maxPrice = 20,maxDistance = 7) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[401, 5, 1, 10, 10], [402, 6, 1, 15, 9], [403, 7, 1, 20, 8], [404, 8, 1, 25, 7], [405, 9, 1, 30, 6], [406, 10, 1, 35, 5]],veganFriendly = 1,maxPrice = 20,maxDistance = 7) == []: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[101, 99, 1, 10, 5], [202, 98, 0, 20, 3], [303, 99, 1, 10, 2], [404, 98, 0, 25, 5], [505, 97, 1, 15, 4], [606, 98, 0, 10, 4]],veganFriendly = 1,maxPrice = 15,maxDistance = 5) == [303, 101, 505]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[101, 99, 1, 10, 5], [202, 98, 0, 20, 3], [303, 99, 1, 10, 2], [404, 98, 0, 25, 5], [505, 97, 1, 15, 4], [606, 98, 0, 10, 4]],veganFriendly = 1,maxPrice = 15,maxDistance = 5) == [303, 101, 505]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[401, 10, 0, 10, 1], [402, 9, 1, 15, 2], [403, 8, 0, 20, 3], [404, 7, 1, 25, 4], [405, 6, 0, 30, 5], [406, 5, 1, 12, 6]],veganFriendly = 1,maxPrice = 25,maxDistance = 5) == [402, 404]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[401, 10, 0, 10, 1], [402, 9, 1, 15, 2], [403, 8, 0, 20, 3], [404, 7, 1, 25, 4], [405, 6, 0, 30, 5], [406, 5, 1, 12, 6]],veganFriendly = 1,maxPrice = 25,maxDistance = 5) == [402, 404]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[10, 9, 1, 15, 5], [11, 7, 0, 20, 6], [12, 9, 1, 18, 3], [13, 8, 0, 25, 4], [14, 7, 1, 10, 2], [15, 10, 0, 5, 1]],veganFriendly = 1,maxPrice = 20,maxDistance = 5) == [12, 10, 14]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[10, 9, 1, 15, 5], [11, 7, 0, 20, 6], [12, 9, 1, 18, 3], [13, 8, 0, 25, 4], [14, 7, 1, 10, 2], [15, 10, 0, 5, 1]],veganFriendly = 1,maxPrice = 20,maxDistance = 5) == [12, 10, 14]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[30, 10, 1, 10, 1], [31, 9, 0, 15, 2], [32, 8, 1, 20, 3], [33, 7, 1, 25, 4], [34, 6, 0, 30, 5], [35, 5, 1, 35, 6]],veganFriendly = 1,maxPrice = 30,maxDistance = 5) == [30, 32, 33]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[30, 10, 1, 10, 1], [31, 9, 0, 15, 2], [32, 8, 1, 20, 3], [33, 7, 1, 25, 4], [34, 6, 0, 30, 5], [35, 5, 1, 35, 6]],veganFriendly = 1,maxPrice = 30,maxDistance = 5) == [30, 32, 33]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[301, 9, 0, 15, 10], [302, 8, 1, 20, 8], [303, 7, 0, 25, 6], [304, 6, 1, 30, 4], [305, 5, 0, 35, 2], [306, 4, 1, 40, 0]],veganFriendly = 1,maxPrice = 20,maxDistance = 8) == [302]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[301, 9, 0, 15, 10], [302, 8, 1, 20, 8], [303, 7, 0, 25, 6], [304, 6, 1, 30, 4], [305, 5, 0, 35, 2], [306, 4, 1, 40, 0]],veganFriendly = 1,maxPrice = 20,maxDistance = 8) == [302]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[26, 2, 1, 40, 10], [27, 8, 0, 35, 9], [28, 7, 1, 30, 8], [29, 9, 0, 25, 7], [30, 6, 1, 20, 6]],veganFriendly = 0,maxPrice = 35,maxDistance = 9) == [29, 27, 28, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[26, 2, 1, 40, 10], [27, 8, 0, 35, 9], [28, 7, 1, 30, 8], [29, 9, 0, 25, 7], [30, 6, 1, 20, 6]],veganFriendly = 0,maxPrice = 35,maxDistance = 9) == [29, 27, 28, 30]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[10001, 10, 1, 100, 100], [20002, 20, 0, 80, 90], [30003, 30, 1, 70, 80], [40004, 40, 0, 60, 70], [50005, 50, 1, 50, 60], [60006, 60, 0, 40, 50], [70007, 70, 1, 30, 40], [80008, 80, 0, 20, 30], [90009, 90, 1, 10, 20], [100010, 100, 1, 0, 10]],veganFriendly = 1,maxPrice = 60,maxDistance = 70) == [100010, 90009, 70007, 50005]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[10001, 10, 1, 100, 100], [20002, 20, 0, 80, 90], [30003, 30, 1, 70, 80], [40004, 40, 0, 60, 70], [50005, 50, 1, 50, 60], [60006, 60, 0, 40, 50], [70007, 70, 1, 30, 40], [80008, 80, 0, 20, 30], [90009, 90, 1, 10, 20], [100010, 100, 1, 0, 10]],veganFriendly = 1,maxPrice = 60,maxDistance = 70) == [100010, 90009, 70007, 50005]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[101, 80, 1, 10, 5], [202, 85, 0, 20, 3], [303, 80, 1, 10, 2], [404, 80, 0, 25, 5], [505, 85, 1, 15, 4], [606, 80, 0, 10, 4]],veganFriendly = 1,maxPrice = 20,maxDistance = 5) == [505, 303, 101]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[101, 80, 1, 10, 5], [202, 85, 0, 20, 3], [303, 80, 1, 10, 2], [404, 80, 0, 25, 5], [505, 85, 1, 15, 4], [606, 80, 0, 10, 4]],veganFriendly = 1,maxPrice = 20,maxDistance = 5) == [505, 303, 101]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[101, 50, 1, 10, 5], [202, 70, 0, 20, 3], [303, 70, 1, 10, 2], [404, 80, 0, 25, 5], [505, 60, 1, 15, 4], [606, 60, 0, 10, 4]],veganFriendly = 1,maxPrice = 15,maxDistance = 4) == [303, 505]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[101, 50, 1, 10, 5], [202, 70, 0, 20, 3], [303, 70, 1, 10, 2], [404, 80, 0, 25, 5], [505, 60, 1, 15, 4], [606, 60, 0, 10, 4]],veganFriendly = 1,maxPrice = 15,maxDistance = 4) == [303, 505]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[24, 9, 1, 20, 5], [25, 10, 0, 25, 3], [26, 8, 1, 15, 2], [27, 7, 1, 10, 1], [28, 6, 0, 5, 1], [29, 5, 1, 30, 4]],veganFriendly = 1,maxPrice = 20,maxDistance = 3) == [26, 27]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[24, 9, 1, 20, 5], [25, 10, 0, 25, 3], [26, 8, 1, 15, 2], [27, 7, 1, 10, 1], [28, 6, 0, 5, 1], [29, 5, 1, 30, 4]],veganFriendly = 1,maxPrice = 20,maxDistance = 3) == [26, 27]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[1, 100, 1, 1, 1], [2, 100, 1, 2, 2], [3, 100, 1, 3, 3], [4, 100, 1, 4, 4], [5, 100, 1, 5, 5], [6, 100, 1, 6, 6], [7, 100, 1, 7, 7], [8, 100, 1, 8, 8], [9, 100, 1, 9, 9], [10, 100, 1, 10, 10]],veganFriendly = 1,maxPrice = 5,maxDistance = 5) == [5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[1, 100, 1, 1, 1], [2, 100, 1, 2, 2], [3, 100, 1, 3, 3], [4, 100, 1, 4, 4], [5, 100, 1, 5, 5], [6, 100, 1, 6, 6], [7, 100, 1, 7, 7], [8, 100, 1, 8, 8], [9, 100, 1, 9, 9], [10, 100, 1, 10, 10]],veganFriendly = 1,maxPrice = 5,maxDistance = 5) == [5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[101, 10, 0, 100, 100], [102, 9, 1, 95, 95], [103, 8, 0, 90, 90], [104, 7, 1, 85, 85], [105, 6, 0, 80, 80]],veganFriendly = 0,maxPrice = 90,maxDistance = 90) == [103, 104, 105]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[101, 10, 0, 100, 100], [102, 9, 1, 95, 95], [103, 8, 0, 90, 90], [104, 7, 1, 85, 85], [105, 6, 0, 80, 80]],veganFriendly = 0,maxPrice = 90,maxDistance = 90) == [103, 104, 105]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[10001, 5, 0, 50, 50], [20002, 15, 1, 40, 40], [30003, 25, 0, 30, 30], [40004, 35, 1, 20, 20], [50005, 45, 0, 10, 10], [60006, 55, 1, 5, 5]],veganFriendly = 0,maxPrice = 40,maxDistance = 40) == [60006, 50005, 40004, 30003, 20002]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[10001, 5, 0, 50, 50], [20002, 15, 1, 40, 40], [30003, 25, 0, 30, 30], [40004, 35, 1, 20, 20], [50005, 45, 0, 10, 10], [60006, 55, 1, 5, 5]],veganFriendly = 0,maxPrice = 40,maxDistance = 40) == [60006, 50005, 40004, 30003, 20002]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[42, 10, 1, 10, 1], [43, 9, 0, 15, 2], [44, 8, 1, 20, 3], [45, 7, 1, 25, 4], [46, 6, 0, 30, 5], [47, 5, 1, 35, 6]],veganFriendly = 0,maxPrice = 5,maxDistance = 1) == []
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[42, 10, 1, 10, 1], [43, 9, 0, 15, 2], [44, 8, 1, 20, 3], [45, 7, 1, 25, 4], [46, 6, 0, 30, 5], [47, 5, 1, 35, 6]],veganFriendly = 0,maxPrice = 5,maxDistance = 1) == []: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[21, 6, 0, 30, 9], [22, 7, 0, 25, 7], [23, 9, 1, 18, 5], [24, 8, 1, 22, 4], [25, 10, 0, 15, 3]],veganFriendly = 1,maxPrice = 25,maxDistance = 6) == [23, 24]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[21, 6, 0, 30, 9], [22, 7, 0, 25, 7], [23, 9, 1, 18, 5], [24, 8, 1, 22, 4], [25, 10, 0, 15, 3]],veganFriendly = 1,maxPrice = 25,maxDistance = 6) == [23, 24]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[54, 10, 1, 10, 1], [55, 9, 0, 15, 2], [56, 8, 1, 20, 3], [57, 7, 1, 25, 4], [58, 6, 0, 30, 5], [59, 5, 1, 35, 6]],veganFriendly = 1,maxPrice = 35,maxDistance = 6) == [54, 56, 57, 59]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[54, 10, 1, 10, 1], [55, 9, 0, 15, 2], [56, 8, 1, 20, 3], [57, 7, 1, 25, 4], [58, 6, 0, 30, 5], [59, 5, 1, 35, 6]],veganFriendly = 1,maxPrice = 35,maxDistance = 6) == [54, 56, 57, 59]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[901, 9, 0, 10, 1], [902, 8, 1, 15, 2], [903, 7, 0, 20, 3], [904, 6, 1, 25, 4], [905, 5, 0, 12, 5]],veganFriendly = 0,maxPrice = 25,maxDistance = 5) == [901, 902, 903, 904, 905]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[901, 9, 0, 10, 1], [902, 8, 1, 15, 2], [903, 7, 0, 20, 3], [904, 6, 1, 25, 4], [905, 5, 0, 12, 5]],veganFriendly = 0,maxPrice = 25,maxDistance = 5) == [901, 902, 903, 904, 905]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[41, 2, 0, 45, 10], [42, 8, 1, 35, 9], [43, 7, 1, 30, 8], [44, 9, 0, 25, 7], [45, 6, 1, 20, 6]],veganFriendly = 1,maxPrice = 30,maxDistance = 7) == [45]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[41, 2, 0, 45, 10], [42, 8, 1, 35, 9], [43, 7, 1, 30, 8], [44, 9, 0, 25, 7], [45, 6, 1, 20, 6]],veganFriendly = 1,maxPrice = 30,maxDistance = 7) == [45]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[101, 80, 1, 10, 5], [202, 85, 0, 20, 3], [303, 80, 1, 10, 2], [404, 80, 0, 25, 5], [505, 85, 1, 15, 4], [606, 80, 0, 10, 4]],veganFriendly = 0,maxPrice = 10,maxDistance = 5) == [606, 303, 101]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[101, 80, 1, 10, 5], [202, 85, 0, 20, 3], [303, 80, 1, 10, 2], [404, 80, 0, 25, 5], [505, 85, 1, 15, 4], [606, 80, 0, 10, 4]],veganFriendly = 0,maxPrice = 10,maxDistance = 5) == [606, 303, 101]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[101, 50, 1, 30, 10], [202, 20, 0, 20, 5], [303, 40, 1, 25, 8], [404, 30, 0, 15, 3], [505, 60, 1, 5, 1], [606, 55, 0, 40, 20], [707, 45, 1, 10, 15], [808, 35, 0, 25, 10], [909, 25, 1, 35, 20], [1010, 70, 1, 10, 5]],veganFriendly = 1,maxPrice = 35,maxDistance = 15) == [1010, 505, 101, 707, 303]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[101, 50, 1, 30, 10], [202, 20, 0, 20, 5], [303, 40, 1, 25, 8], [404, 30, 0, 15, 3], [505, 60, 1, 5, 1], [606, 55, 0, 40, 20], [707, 45, 1, 10, 15], [808, 35, 0, 25, 10], [909, 25, 1, 35, 20], [1010, 70, 1, 10, 5]],veganFriendly = 1,maxPrice = 35,maxDistance = 15) == [1010, 505, 101, 707, 303]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[601, 7, 1, 25, 10], [602, 8, 0, 30, 15], [603, 9, 1, 45, 8], [604, 6, 0, 35, 15], [605, 8, 1, 50, 6], [606, 9, 1, 35, 10], [607, 7, 0, 40, 8]],veganFriendly = 0,maxPrice = 50,maxDistance = 20) == [606, 603, 605, 602, 607, 601, 604]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[601, 7, 1, 25, 10], [602, 8, 0, 30, 15], [603, 9, 1, 45, 8], [604, 6, 0, 35, 15], [605, 8, 1, 50, 6], [606, 9, 1, 35, 10], [607, 7, 0, 40, 8]],veganFriendly = 0,maxPrice = 50,maxDistance = 20) == [606, 603, 605, 602, 607, 601, 604]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[701, 10, 0, 20, 20], [702, 9, 0, 25, 25], [703, 8, 0, 30, 30], [704, 7, 0, 35, 35], [705, 6, 0, 40, 40], [706, 5, 0, 45, 45], [707, 4, 0, 50, 50], [708, 3, 0, 55, 55], [709, 2, 0, 60, 60], [710, 1, 0, 65, 65]],veganFriendly = 0,maxPrice = 40,maxDistance = 40) == [701, 702, 703, 704, 705]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[701, 10, 0, 20, 20], [702, 9, 0, 25, 25], [703, 8, 0, 30, 30], [704, 7, 0, 35, 35], [705, 6, 0, 40, 40], [706, 5, 0, 45, 45], [707, 4, 0, 50, 50], [708, 3, 0, 55, 55], [709, 2, 0, 60, 60], [710, 1, 0, 65, 65]],veganFriendly = 0,maxPrice = 40,maxDistance = 40) == [701, 702, 703, 704, 705]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[36, 5, 1, 15, 2], [37, 4, 0, 10, 3], [38, 3, 1, 5, 4], [39, 2, 1, 20, 5], [40, 1, 0, 25, 6], [41, 8, 1, 10, 1]],veganFriendly = 1,maxPrice = 20,maxDistance = 5) == [41, 36, 38, 39]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[36, 5, 1, 15, 2], [37, 4, 0, 10, 3], [38, 3, 1, 5, 4], [39, 2, 1, 20, 5], [40, 1, 0, 25, 6], [41, 8, 1, 10, 1]],veganFriendly = 1,maxPrice = 20,maxDistance = 5) == [41, 36, 38, 39]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[101, 95, 1, 20, 15], [202, 85, 0, 55, 18], [303, 95, 1, 25, 12], [404, 75, 0, 22, 14], [505, 88, 1, 18, 16], [606, 80, 0, 30, 10]],veganFriendly = 1,maxPrice = 30,maxDistance = 20) == [303, 101, 505]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[101, 95, 1, 20, 15], [202, 85, 0, 55, 18], [303, 95, 1, 25, 12], [404, 75, 0, 22, 14], [505, 88, 1, 18, 16], [606, 80, 0, 30, 10]],veganFriendly = 1,maxPrice = 30,maxDistance = 20) == [303, 101, 505]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[1, 5, 1, 10, 1], [2, 5, 1, 10, 1], [3, 5, 1, 10, 1], [4, 5, 1, 10, 1], [5, 5, 1, 10, 1]],veganFriendly = 1,maxPrice = 10,maxDistance = 1) == [5, 4, 3, 2, 1]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[1, 5, 1, 10, 1], [2, 5, 1, 10, 1], [3, 5, 1, 10, 1], [4, 5, 1, 10, 1], [5, 5, 1, 10, 1]],veganFriendly = 1,maxPrice = 10,maxDistance = 1) == [5, 4, 3, 2, 1]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[101, 80, 1, 10, 5], [202, 85, 0, 20, 3], [303, 80, 1, 10, 2], [404, 80, 0, 25, 5], [505, 85, 1, 15, 4], [606, 80, 0, 10, 4]],veganFriendly = 0,maxPrice = 25,maxDistance = 5) == [505, 202, 606, 404, 303, 101]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[101, 80, 1, 10, 5], [202, 85, 0, 20, 3], [303, 80, 1, 10, 2], [404, 80, 0, 25, 5], [505, 85, 1, 15, 4], [606, 80, 0, 10, 4]],veganFriendly = 0,maxPrice = 25,maxDistance = 5) == [505, 202, 606, 404, 303, 101]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[101, 5, 1, 100, 5], [102, 9, 0, 50, 4], [103, 6, 1, 40, 3], [104, 7, 0, 30, 2], [105, 8, 1, 20, 1], [106, 4, 0, 10, 6], [107, 9, 1, 15, 2]],veganFriendly = 0,maxPrice = 50,maxDistance = 4) == [107, 102, 105, 104, 103]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[101, 5, 1, 100, 5], [102, 9, 0, 50, 4], [103, 6, 1, 40, 3], [104, 7, 0, 30, 2], [105, 8, 1, 20, 1], [106, 4, 0, 10, 6], [107, 9, 1, 15, 2]],veganFriendly = 0,maxPrice = 50,maxDistance = 4) == [107, 102, 105, 104, 103]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[35, 6, 0, 20, 17], [36, 7, 1, 45, 21], [37, 6, 0, 35, 15], [38, 9, 1, 25, 10], [39, 8, 0, 45, 25], [40, 11, 1, 10, 4], [41, 13, 0, 22, 18]],veganFriendly = 1,maxPrice = 45,maxDistance = 25) == [40, 38, 36]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[35, 6, 0, 20, 17], [36, 7, 1, 45, 21], [37, 6, 0, 35, 15], [38, 9, 1, 25, 10], [39, 8, 0, 45, 25], [40, 11, 1, 10, 4], [41, 13, 0, 22, 18]],veganFriendly = 1,maxPrice = 45,maxDistance = 25) == [40, 38, 36]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[201, 10, 0, 1000, 50], [202, 9, 1, 900, 45], [203, 8, 0, 800, 40], [204, 7, 1, 700, 35], [205, 6, 0, 600, 30], [206, 5, 1, 500, 25], [207, 4, 0, 400, 20], [208, 3, 1, 300, 15], [209, 2, 0, 200, 10], [210, 1, 1, 100, 5]],veganFriendly = 1,maxPrice = 500,maxDistance = 30) == [206, 208, 210]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[201, 10, 0, 1000, 50], [202, 9, 1, 900, 45], [203, 8, 0, 800, 40], [204, 7, 1, 700, 35], [205, 6, 0, 600, 30], [206, 5, 1, 500, 25], [207, 4, 0, 400, 20], [208, 3, 1, 300, 15], [209, 2, 0, 200, 10], [210, 1, 1, 100, 5]],veganFriendly = 1,maxPrice = 500,maxDistance = 30) == [206, 208, 210]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[301, 7, 0, 20, 4], [302, 9, 1, 10, 2], [303, 6, 0, 25, 5], [304, 8, 1, 15, 3], [305, 9, 0, 30, 1], [306, 7, 1, 12, 6]],veganFriendly = 0,maxPrice = 15,maxDistance = 4) == [302, 304]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[301, 7, 0, 20, 4], [302, 9, 1, 10, 2], [303, 6, 0, 25, 5], [304, 8, 1, 15, 3], [305, 9, 0, 30, 1], [306, 7, 1, 12, 6]],veganFriendly = 0,maxPrice = 15,maxDistance = 4) == [302, 304]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[401, 8, 1, 25, 10], [402, 7, 0, 30, 15], [403, 9, 1, 20, 5], [404, 8, 0, 20, 8], [405, 6, 1, 20, 5], [406, 9, 1, 30, 3], [407, 5, 0, 35, 6]],veganFriendly = 1,maxPrice = 30,maxDistance = 15) == [406, 403, 401, 405]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[401, 8, 1, 25, 10], [402, 7, 0, 30, 15], [403, 9, 1, 20, 5], [404, 8, 0, 20, 8], [405, 6, 1, 20, 5], [406, 9, 1, 30, 3], [407, 5, 0, 35, 6]],veganFriendly = 1,maxPrice = 30,maxDistance = 15) == [406, 403, 401, 405]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[101, 90, 1, 30, 5], [202, 85, 0, 40, 10], [303, 90, 1, 30, 4], [404, 85, 0, 45, 8], [505, 85, 1, 25, 6], [606, 80, 0, 35, 7]],veganFriendly = 1,maxPrice = 35,maxDistance = 10) == [303, 101, 505]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[101, 90, 1, 30, 5], [202, 85, 0, 40, 10], [303, 90, 1, 30, 4], [404, 85, 0, 45, 8], [505, 85, 1, 25, 6], [606, 80, 0, 35, 7]],veganFriendly = 1,maxPrice = 35,maxDistance = 10) == [303, 101, 505]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[101, 50, 1, 30, 10], [202, 20, 0, 20, 5], [303, 40, 1, 25, 8], [404, 30, 0, 15, 3], [505, 60, 1, 5, 1], [606, 55, 0, 40, 20], [707, 45, 1, 10, 15], [808, 35, 0, 25, 10], [909, 25, 1, 35, 20], [1010, 70, 1, 10, 5]],veganFriendly = 0,maxPrice = 20,maxDistance = 5) == [1010, 505, 404, 202]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[101, 50, 1, 30, 10], [202, 20, 0, 20, 5], [303, 40, 1, 25, 8], [404, 30, 0, 15, 3], [505, 60, 1, 5, 1], [606, 55, 0, 40, 20], [707, 45, 1, 10, 15], [808, 35, 0, 25, 10], [909, 25, 1, 35, 20], [1010, 70, 1, 10, 5]],veganFriendly = 0,maxPrice = 20,maxDistance = 5) == [1010, 505, 404, 202]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[701, 6, 1, 25, 10], [702, 8, 0, 30, 15], [703, 7, 1, 45, 8], [704, 9, 0, 35, 15], [705, 5, 1, 50, 6], [706, 8, 1, 35, 10], [707, 6, 0, 40, 8]],veganFriendly = 1,maxPrice = 40,maxDistance = 15) == [706, 701]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[701, 6, 1, 25, 10], [702, 8, 0, 30, 15], [703, 7, 1, 45, 8], [704, 9, 0, 35, 15], [705, 5, 1, 50, 6], [706, 8, 1, 35, 10], [707, 6, 0, 40, 8]],veganFriendly = 1,maxPrice = 40,maxDistance = 15) == [706, 701]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[22, 6, 0, 20, 17], [23, 7, 1, 45, 21], [24, 6, 0, 35, 15], [25, 9, 1, 25, 10], [26, 8, 0, 45, 25], [27, 11, 1, 10, 4]],veganFriendly = 1,maxPrice = 40,maxDistance = 20) == [27, 25]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[22, 6, 0, 20, 17], [23, 7, 1, 45, 21], [24, 6, 0, 35, 15], [25, 9, 1, 25, 10], [26, 8, 0, 45, 25], [27, 11, 1, 10, 4]],veganFriendly = 1,maxPrice = 40,maxDistance = 20) == [27, 25]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[301, 6, 1, 30, 10], [302, 8, 0, 40, 12], [303, 7, 1, 45, 8], [304, 9, 1, 50, 6], [305, 5, 0, 35, 15], [306, 8, 1, 45, 10], [307, 7, 0, 40, 8]],veganFriendly = 0,maxPrice = 50,maxDistance = 15) == [304, 306, 302, 307, 303, 301, 305]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[301, 6, 1, 30, 10], [302, 8, 0, 40, 12], [303, 7, 1, 45, 8], [304, 9, 1, 50, 6], [305, 5, 0, 35, 15], [306, 8, 1, 45, 10], [307, 7, 0, 40, 8]],veganFriendly = 0,maxPrice = 50,maxDistance = 15) == [304, 306, 302, 307, 303, 301, 305]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[101, 100, 1, 5, 5], [102, 100, 1, 5, 6], [103, 100, 1, 5, 7], [104, 100, 1, 5, 8], [105, 100, 1, 5, 9]],veganFriendly = 1,maxPrice = 5,maxDistance = 9) == [105, 104, 103, 102, 101]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[101, 100, 1, 5, 5], [102, 100, 1, 5, 6], [103, 100, 1, 5, 7], [104, 100, 1, 5, 8], [105, 100, 1, 5, 9]],veganFriendly = 1,maxPrice = 5,maxDistance = 9) == [105, 104, 103, 102, 101]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[501, 10, 0, 50, 100], [502, 10, 0, 55, 95], [503, 10, 0, 60, 90], [504, 10, 0, 65, 85], [505, 10, 0, 70, 80], [506, 10, 0, 75, 75], [507, 10, 0, 80, 70], [508, 10, 0, 85, 65], [509, 10, 0, 90, 60]],veganFriendly = 0,maxPrice = 80,maxDistance = 70) == [507]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[501, 10, 0, 50, 100], [502, 10, 0, 55, 95], [503, 10, 0, 60, 90], [504, 10, 0, 65, 85], [505, 10, 0, 70, 80], [506, 10, 0, 75, 75], [507, 10, 0, 80, 70], [508, 10, 0, 85, 65], [509, 10, 0, 90, 60]],veganFriendly = 0,maxPrice = 80,maxDistance = 70) == [507]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[36, 6, 1, 40, 9], [37, 8, 0, 35, 8], [38, 7, 1, 30, 7], [39, 9, 0, 25, 6], [40, 10, 1, 20, 5]],veganFriendly = 1,maxPrice = 30,maxDistance = 8) == [40, 38]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[36, 6, 1, 40, 9], [37, 8, 0, 35, 8], [38, 7, 1, 30, 7], [39, 9, 0, 25, 6], [40, 10, 1, 20, 5]],veganFriendly = 1,maxPrice = 30,maxDistance = 8) == [40, 38]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[101, 1, 1, 5, 5], [102, 1, 1, 6, 6], [103, 1, 1, 7, 7], [104, 1, 1, 8, 8], [105, 1, 1, 9, 9]],veganFriendly = 1,maxPrice = 10,maxDistance = 10) == [105, 104, 103, 102, 101]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[101, 1, 1, 5, 5], [102, 1, 1, 6, 6], [103, 1, 1, 7, 7], [104, 1, 1, 8, 8], [105, 1, 1, 9, 9]],veganFriendly = 1,maxPrice = 10,maxDistance = 10) == [105, 104, 103, 102, 101]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[101, 50, 1, 30, 10], [202, 20, 0, 20, 5], [303, 40, 1, 25, 8], [404, 30, 0, 15, 3], [505, 60, 1, 5, 1], [606, 55, 0, 40, 20], [707, 45, 1, 10, 15], [808, 35, 0, 25, 10], [909, 25, 1, 35, 20], [1010, 70, 1, 10, 5]],veganFriendly = 1,maxPrice = 50,maxDistance = 20) == [1010, 505, 101, 707, 303, 909]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[101, 50, 1, 30, 10], [202, 20, 0, 20, 5], [303, 40, 1, 25, 8], [404, 30, 0, 15, 3], [505, 60, 1, 5, 1], [606, 55, 0, 40, 20], [707, 45, 1, 10, 15], [808, 35, 0, 25, 10], [909, 25, 1, 35, 20], [1010, 70, 1, 10, 5]],veganFriendly = 1,maxPrice = 50,maxDistance = 20) == [1010, 505, 101, 707, 303, 909]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[2001, 100, 0, 50, 50], [2002, 99, 1, 49, 49], [2003, 98, 0, 48, 48], [2004, 97, 1, 47, 47], [2005, 96, 0, 46, 46]],veganFriendly = 0,maxPrice = 50,maxDistance = 50) == [2001, 2002, 2003, 2004, 2005]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[2001, 100, 0, 50, 50], [2002, 99, 1, 49, 49], [2003, 98, 0, 48, 48], [2004, 97, 1, 47, 47], [2005, 96, 0, 46, 46]],veganFriendly = 0,maxPrice = 50,maxDistance = 50) == [2001, 2002, 2003, 2004, 2005]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[10, 10, 0, 100, 100], [20, 9, 1, 90, 90], [30, 8, 0, 80, 80], [40, 7, 1, 70, 70], [50, 6, 0, 60, 60]],veganFriendly = 0,maxPrice = 100,maxDistance = 100) == [10, 20, 30, 40, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[10, 10, 0, 100, 100], [20, 9, 1, 90, 90], [30, 8, 0, 80, 80], [40, 7, 1, 70, 70], [50, 6, 0, 60, 60]],veganFriendly = 0,maxPrice = 100,maxDistance = 100) == [10, 20, 30, 40, 50]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[31, 1, 0, 45, 10], [32, 3, 0, 30, 8], [33, 2, 1, 25, 6], [34, 4, 1, 20, 5], [35, 5, 0, 15, 4]],veganFriendly = 1,maxPrice = 25,maxDistance = 7) == [34, 33]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[31, 1, 0, 45, 10], [32, 3, 0, 30, 8], [33, 2, 1, 25, 6], [34, 4, 1, 20, 5], [35, 5, 0, 15, 4]],veganFriendly = 1,maxPrice = 25,maxDistance = 7) == [34, 33]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[101, 6, 0, 20, 5], [102, 9, 1, 18, 2], [103, 5, 0, 10, 3], [104, 8, 1, 12, 4], [105, 7, 1, 15, 6], [106, 9, 0, 22, 3]],veganFriendly = 0,maxPrice = 25,maxDistance = 6) == [106, 102, 104, 105, 101, 103]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[101, 6, 0, 20, 5], [102, 9, 1, 18, 2], [103, 5, 0, 10, 3], [104, 8, 1, 12, 4], [105, 7, 1, 15, 6], [106, 9, 0, 22, 3]],veganFriendly = 0,maxPrice = 25,maxDistance = 6) == [106, 102, 104, 105, 101, 103]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[101, 95, 1, 20, 15], [202, 85, 0, 55, 18], [303, 95, 1, 25, 12], [404, 75, 0, 22, 14], [505, 88, 1, 18, 16], [606, 80, 0, 30, 10]],veganFriendly = 0,maxPrice = 55,maxDistance = 20) == [303, 101, 505, 202, 606, 404]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[101, 95, 1, 20, 15], [202, 85, 0, 55, 18], [303, 95, 1, 25, 12], [404, 75, 0, 22, 14], [505, 88, 1, 18, 16], [606, 80, 0, 30, 10]],veganFriendly = 0,maxPrice = 55,maxDistance = 20) == [303, 101, 505, 202, 606, 404]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[601, 9, 1, 10, 1], [602, 8, 0, 15, 2], [603, 7, 1, 20, 3], [604, 6, 0, 25, 4], [605, 5, 1, 12, 5]],veganFriendly = 1,maxPrice = 15,maxDistance = 4) == [601]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[601, 9, 1, 10, 1], [602, 8, 0, 15, 2], [603, 7, 1, 20, 3], [604, 6, 0, 25, 4], [605, 5, 1, 12, 5]],veganFriendly = 1,maxPrice = 15,maxDistance = 4) == [601]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[10001, 5, 0, 50, 50], [20002, 15, 1, 40, 40], [30003, 25, 0, 30, 30], [40004, 35, 1, 20, 20], [50005, 45, 0, 10, 10], [60006, 55, 1, 5, 5]],veganFriendly = 1,maxPrice = 50,maxDistance = 50) == [60006, 40004, 20002]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[10001, 5, 0, 50, 50], [20002, 15, 1, 40, 40], [30003, 25, 0, 30, 30], [40004, 35, 1, 20, 20], [50005, 45, 0, 10, 10], [60006, 55, 1, 5, 5]],veganFriendly = 1,maxPrice = 50,maxDistance = 50) == [60006, 40004, 20002]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[801, 8, 1, 15, 3], [802, 9, 0, 10, 2], [803, 7, 1, 25, 4], [804, 6, 0, 20, 5], [805, 5, 1, 12, 1]],veganFriendly = 1,maxPrice = 20,maxDistance = 4) == [801, 805]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[801, 8, 1, 15, 3], [802, 9, 0, 10, 2], [803, 7, 1, 25, 4], [804, 6, 0, 20, 5], [805, 5, 1, 12, 1]],veganFriendly = 1,maxPrice = 20,maxDistance = 4) == [801, 805]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[48, 1, 1, 5, 1], [49, 2, 0, 10, 2], [50, 3, 1, 15, 3], [51, 4, 1, 20, 4], [52, 5, 0, 25, 5], [53, 6, 1, 30, 6]],veganFriendly = 1,maxPrice = 25,maxDistance = 5) == [51, 50, 48]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[48, 1, 1, 5, 1], [49, 2, 0, 10, 2], [50, 3, 1, 15, 3], [51, 4, 1, 20, 4], [52, 5, 0, 25, 5], [53, 6, 1, 30, 6]],veganFriendly = 1,maxPrice = 25,maxDistance = 5) == [51, 50, 48]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[10, 9, 1, 25, 7], [20, 8, 0, 35, 9], [30, 10, 1, 20, 5], [40, 7, 0, 45, 3], [50, 6, 1, 15, 2]],veganFriendly = 1,maxPrice = 30,maxDistance = 8) == [30, 10, 50]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[10, 9, 1, 25, 7], [20, 8, 0, 35, 9], [30, 10, 1, 20, 5], [40, 7, 0, 45, 3], [50, 6, 1, 15, 2]],veganFriendly = 1,maxPrice = 30,maxDistance = 8) == [30, 10, 50]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[1, 99, 0, 1, 1], [2, 98, 0, 2, 2], [3, 97, 0, 3, 3], [4, 96, 0, 4, 4], [5, 95, 0, 5, 5], [6, 94, 0, 6, 6], [7, 93, 0, 7, 7], [8, 92, 0, 8, 8], [9, 91, 0, 9, 9]],veganFriendly = 0,maxPrice = 9,maxDistance = 9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[1, 99, 0, 1, 1], [2, 98, 0, 2, 2], [3, 97, 0, 3, 3], [4, 96, 0, 4, 4], [5, 95, 0, 5, 5], [6, 94, 0, 6, 6], [7, 93, 0, 7, 7], [8, 92, 0, 8, 8], [9, 91, 0, 9, 9]],veganFriendly = 0,maxPrice = 9,maxDistance = 9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[3001, 9, 1, 9, 9], [3002, 8, 0, 8, 8], [3003, 7, 1, 7, 7], [3004, 6, 0, 6, 6], [3005, 5, 1, 5, 5], [3006, 4, 0, 4, 4], [3007, 3, 1, 3, 3], [3008, 2, 0, 2, 2], [3009, 1, 1, 1, 1]],veganFriendly = 1,maxPrice = 10,maxDistance = 10) == [3001, 3003, 3005, 3007, 3009]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[3001, 9, 1, 9, 9], [3002, 8, 0, 8, 8], [3003, 7, 1, 7, 7], [3004, 6, 0, 6, 6], [3005, 5, 1, 5, 5], [3006, 4, 0, 4, 4], [3007, 3, 1, 3, 3], [3008, 2, 0, 2, 2], [3009, 1, 1, 1, 1]],veganFriendly = 1,maxPrice = 10,maxDistance = 10) == [3001, 3003, 3005, 3007, 3009]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[51, 6, 1, 40, 10], [52, 8, 1, 35, 9], [53, 7, 1, 30, 8], [54, 9, 1, 25, 7], [55, 10, 1, 20, 6]],veganFriendly = 1,maxPrice = 30,maxDistance = 8) == [55, 54, 53]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[51, 6, 1, 40, 10], [52, 8, 1, 35, 9], [53, 7, 1, 30, 8], [54, 9, 1, 25, 7], [55, 10, 1, 20, 6]],veganFriendly = 1,maxPrice = 30,maxDistance = 8) == [55, 54, 53]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[501, 6, 1, 10, 5], [502, 7, 0, 15, 4], [503, 8, 1, 20, 3], [504, 9, 0, 25, 2], [505, 10, 1, 12, 1]],veganFriendly = 0,maxPrice = 25,maxDistance = 5) == [505, 504, 503, 502, 501]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[501, 6, 1, 10, 5], [502, 7, 0, 15, 4], [503, 8, 1, 20, 3], [504, 9, 0, 25, 2], [505, 10, 1, 12, 1]],veganFriendly = 0,maxPrice = 25,maxDistance = 5) == [505, 504, 503, 502, 501]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[101, 80, 1, 10, 5], [202, 85, 0, 20, 3], [303, 80, 1, 10, 2], [404, 80, 0, 25, 5], [505, 85, 1, 15, 4], [606, 80, 0, 10, 4]],veganFriendly = 1,maxPrice = 100,maxDistance = 100) == [505, 303, 101]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[101, 80, 1, 10, 5], [202, 85, 0, 20, 3], [303, 80, 1, 10, 2], [404, 80, 0, 25, 5], [505, 85, 1, 15, 4], [606, 80, 0, 10, 4]],veganFriendly = 1,maxPrice = 100,maxDistance = 100) == [505, 303, 101]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[201, 3, 0, 40, 15], [202, 5, 1, 45, 20], [203, 8, 1, 50, 10], [204, 4, 0, 50, 25], [205, 6, 0, 40, 15], [206, 7, 1, 45, 15], [207, 9, 1, 35, 10]],veganFriendly = 1,maxPrice = 50,maxDistance = 20) == [207, 203, 206, 202]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[201, 3, 0, 40, 15], [202, 5, 1, 45, 20], [203, 8, 1, 50, 10], [204, 4, 0, 50, 25], [205, 6, 0, 40, 15], [206, 7, 1, 45, 15], [207, 9, 1, 35, 10]],veganFriendly = 1,maxPrice = 50,maxDistance = 20) == [207, 203, 206, 202]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[100, 90, 1, 10, 20], [200, 85, 0, 15, 25], [300, 80, 1, 5, 15], [400, 75, 0, 25, 10], [500, 70, 1, 20, 5]],veganFriendly = 0,maxPrice = 25,maxDistance = 20) == [100, 300, 400, 500]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[100, 90, 1, 10, 20], [200, 85, 0, 15, 25], [300, 80, 1, 5, 15], [400, 75, 0, 25, 10], [500, 70, 1, 20, 5]],veganFriendly = 0,maxPrice = 25,maxDistance = 20) == [100, 300, 400, 500]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[201, 8, 1, 10, 4], [202, 6, 0, 15, 3], [203, 9, 1, 20, 2], [204, 7, 0, 25, 5], [205, 8, 1, 12, 3], [206, 9, 0, 30, 4]],veganFriendly = 1,maxPrice = 30,maxDistance = 5) == [203, 205, 201]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[201, 8, 1, 10, 4], [202, 6, 0, 15, 3], [203, 9, 1, 20, 2], [204, 7, 0, 25, 5], [205, 8, 1, 12, 3], [206, 9, 0, 30, 4]],veganFriendly = 1,maxPrice = 30,maxDistance = 5) == [203, 205, 201]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[17, 2, 0, 30, 13], [18, 5, 1, 40, 18], [19, 7, 1, 50, 22], [20, 1, 0, 60, 30], [21, 4, 0, 10, 2]],veganFriendly = 1,maxPrice = 55,maxDistance = 28) == [19, 18]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[17, 2, 0, 30, 13], [18, 5, 1, 40, 18], [19, 7, 1, 50, 22], [20, 1, 0, 60, 30], [21, 4, 0, 10, 2]],veganFriendly = 1,maxPrice = 55,maxDistance = 28) == [19, 18]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[11, 3, 1, 60, 20], [12, 8, 0, 70, 22], [13, 9, 1, 20, 10], [14, 10, 0, 5, 5], [15, 8, 1, 35, 12], [16, 12, 0, 15, 9]],veganFriendly = 0,maxPrice = 75,maxDistance = 25) == [16, 14, 13, 15, 12, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[11, 3, 1, 60, 20], [12, 8, 0, 70, 22], [13, 9, 1, 20, 10], [14, 10, 0, 5, 5], [15, 8, 1, 35, 12], [16, 12, 0, 15, 9]],veganFriendly = 0,maxPrice = 75,maxDistance = 25) == [16, 14, 13, 15, 12, 11]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[66, 1, 1, 1, 1], [77, 1, 0, 2, 2], [88, 2, 1, 3, 3], [99, 2, 0, 4, 4], [100, 3, 1, 5, 5]],veganFriendly = 0,maxPrice = 5,maxDistance = 5) == [100, 99, 88, 77, 66]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[66, 1, 1, 1, 1], [77, 1, 0, 2, 2], [88, 2, 1, 3, 3], [99, 2, 0, 4, 4], [100, 3, 1, 5, 5]],veganFriendly = 0,maxPrice = 5,maxDistance = 5) == [100, 99, 88, 77, 66]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[12, 3, 0, 60, 7], [13, 2, 1, 45, 6], [14, 5, 1, 55, 8], [15, 4, 0, 35, 5], [16, 6, 1, 40, 9], [17, 7, 1, 30, 3]],veganFriendly = 1,maxPrice = 50,maxDistance = 10) == [17, 16, 13]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[12, 3, 0, 60, 7], [13, 2, 1, 45, 6], [14, 5, 1, 55, 8], [15, 4, 0, 35, 5], [16, 6, 1, 40, 9], [17, 7, 1, 30, 3]],veganFriendly = 1,maxPrice = 50,maxDistance = 10) == [17, 16, 13]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[18, 9, 1, 20, 5], [19, 10, 0, 25, 3], [20, 8, 1, 15, 2], [21, 7, 1, 10, 1], [22, 6, 0, 5, 1], [23, 5, 1, 30, 4]],veganFriendly = 0,maxPrice = 100,maxDistance = 10) == [19, 18, 20, 21, 22, 23]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[18, 9, 1, 20, 5], [19, 10, 0, 25, 3], [20, 8, 1, 15, 2], [21, 7, 1, 10, 1], [22, 6, 0, 5, 1], [23, 5, 1, 30, 4]],veganFriendly = 0,maxPrice = 100,maxDistance = 10) == [19, 18, 20, 21, 22, 23]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[60, 10, 1, 10, 1], [61, 9, 0, 15, 2], [62, 8, 1, 20, 3], [63, 7, 1, 25, 4], [64, 6, 0, 30, 5], [65, 5, 1, 35, 6]],veganFriendly = 1,maxPrice = 10,maxDistance = 1) == [60]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[60, 10, 1, 10, 1], [61, 9, 0, 15, 2], [62, 8, 1, 20, 3], [63, 7, 1, 25, 4], [64, 6, 0, 30, 5], [65, 5, 1, 35, 6]],veganFriendly = 1,maxPrice = 10,maxDistance = 1) == [60]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[1001, 1, 1, 1, 1], [1002, 2, 0, 2, 2], [1003, 3, 1, 3, 3], [1004, 4, 0, 4, 4], [1005, 5, 1, 5, 5], [1006, 6, 0, 6, 6], [1007, 7, 1, 7, 7]],veganFriendly = 1,maxPrice = 7,maxDistance = 7) == [1007, 1005, 1003, 1001]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[1001, 1, 1, 1, 1], [1002, 2, 0, 2, 2], [1003, 3, 1, 3, 3], [1004, 4, 0, 4, 4], [1005, 5, 1, 5, 5], [1006, 6, 0, 6, 6], [1007, 7, 1, 7, 7]],veganFriendly = 1,maxPrice = 7,maxDistance = 7) == [1007, 1005, 1003, 1001]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[28, 5, 0, 30, 15], [29, 8, 1, 40, 20], [30, 6, 0, 25, 10], [31, 7, 1, 5, 5], [32, 9, 0, 10, 4], [33, 12, 1, 35, 12], [34, 10, 0, 15, 9]],veganFriendly = 0,maxPrice = 55,maxDistance = 28) == [33, 34, 32, 29, 31, 30, 28]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[28, 5, 0, 30, 15], [29, 8, 1, 40, 20], [30, 6, 0, 25, 10], [31, 7, 1, 5, 5], [32, 9, 0, 10, 4], [33, 12, 1, 35, 12], [34, 10, 0, 15, 9]],veganFriendly = 0,maxPrice = 55,maxDistance = 28) == [33, 34, 32, 29, 31, 30, 28]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[10, 9, 1, 20, 1], [20, 8, 0, 10, 2], [30, 7, 1, 5, 3], [40, 10, 1, 15, 2], [50, 6, 0, 25, 4], [60, 8, 1, 30, 1]],veganFriendly = 1,maxPrice = 30,maxDistance = 3) == [40, 10, 60, 30]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[10, 9, 1, 20, 1], [20, 8, 0, 10, 2], [30, 7, 1, 5, 3], [40, 10, 1, 15, 2], [50, 6, 0, 25, 4], [60, 8, 1, 30, 1]],veganFriendly = 1,maxPrice = 30,maxDistance = 3) == [40, 10, 60, 30]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[6, 5, 1, 20, 5], [7, 7, 0, 25, 3], [8, 6, 1, 15, 2], [9, 9, 1, 10, 1], [10, 10, 0, 5, 1], [11, 8, 1, 30, 4]],veganFriendly = 1,maxPrice = 25,maxDistance = 4) == [9, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[6, 5, 1, 20, 5], [7, 7, 0, 25, 3], [8, 6, 1, 15, 2], [9, 9, 1, 10, 1], [10, 10, 0, 5, 1], [11, 8, 1, 30, 4]],veganFriendly = 1,maxPrice = 25,maxDistance = 4) == [9, 8]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[1, 100, 1, 1, 1], [2, 99, 0, 2, 2], [3, 98, 1, 3, 3], [4, 97, 0, 4, 4], [5, 96, 1, 5, 5], [6, 95, 0, 6, 6], [7, 94, 1, 7, 7], [8, 93, 0, 8, 8], [9, 92, 1, 9, 9], [10, 91, 0, 10, 10]],veganFriendly = 1,maxPrice = 10,maxDistance = 10) == [1, 3, 5, 7, 9]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[1, 100, 1, 1, 1], [2, 99, 0, 2, 2], [3, 98, 1, 3, 3], [4, 97, 0, 4, 4], [5, 96, 1, 5, 5], [6, 95, 0, 6, 6], [7, 94, 1, 7, 7], [8, 93, 0, 8, 8], [9, 92, 1, 9, 9], [10, 91, 0, 10, 10]],veganFriendly = 1,maxPrice = 10,maxDistance = 10) == [1, 3, 5, 7, 9]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[6, 9, 0, 20, 6], [7, 7, 1, 15, 3], [8, 6, 1, 25, 2], [9, 10, 0, 5, 1], [10, 4, 1, 35, 8]],veganFriendly = 1,maxPrice = 30,maxDistance = 5) == [7, 8]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[6, 9, 0, 20, 6], [7, 7, 1, 15, 3], [8, 6, 1, 25, 2], [9, 10, 0, 5, 1], [10, 4, 1, 35, 8]],veganFriendly = 1,maxPrice = 30,maxDistance = 5) == [7, 8]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[1000, 95, 1, 40, 50], [2000, 90, 0, 50, 60], [3000, 85, 1, 30, 40], [4000, 80, 0, 40, 30], [5000, 75, 1, 20, 20], [6000, 70, 0, 30, 10]],veganFriendly = 1,maxPrice = 30,maxDistance = 30) == [5000]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[1000, 95, 1, 40, 50], [2000, 90, 0, 50, 60], [3000, 85, 1, 30, 40], [4000, 80, 0, 40, 30], [5000, 75, 1, 20, 20], [6000, 70, 0, 30, 10]],veganFriendly = 1,maxPrice = 30,maxDistance = 30) == [5000]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[501, 9, 1, 25, 7], [502, 6, 0, 40, 12], [503, 8, 1, 45, 8], [504, 7, 0, 35, 15], [505, 9, 1, 50, 6], [506, 6, 1, 35, 10], [507, 8, 0, 40, 8]],veganFriendly = 1,maxPrice = 50,maxDistance = 20) == [505, 501, 503, 506]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[501, 9, 1, 25, 7], [502, 6, 0, 40, 12], [503, 8, 1, 45, 8], [504, 7, 0, 35, 15], [505, 9, 1, 50, 6], [506, 6, 1, 35, 10], [507, 8, 0, 40, 8]],veganFriendly = 1,maxPrice = 50,maxDistance = 20) == [505, 501, 503, 506]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[11, 3, 1, 10, 10], [22, 2, 0, 9, 9], [33, 3, 1, 8, 8], [44, 2, 0, 7, 7], [55, 3, 1, 6, 6]],veganFriendly = 1,maxPrice = 10,maxDistance = 10) == [55, 33, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[11, 3, 1, 10, 10], [22, 2, 0, 9, 9], [33, 3, 1, 8, 8], [44, 2, 0, 7, 7], [55, 3, 1, 6, 6]],veganFriendly = 1,maxPrice = 10,maxDistance = 10) == [55, 33, 11]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[601, 5, 1, 5, 5], [602, 6, 1, 10, 10], [603, 7, 1, 15, 15], [604, 8, 1, 20, 20], [605, 9, 1, 25, 25], [606, 10, 1, 30, 30]],veganFriendly = 1,maxPrice = 25,maxDistance = 25) == [605, 604, 603, 602, 601]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[601, 5, 1, 5, 5], [602, 6, 1, 10, 10], [603, 7, 1, 15, 15], [604, 8, 1, 20, 20], [605, 9, 1, 25, 25], [606, 10, 1, 30, 30]],veganFriendly = 1,maxPrice = 25,maxDistance = 25) == [605, 604, 603, 602, 601]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[11, 50, 1, 20, 10], [12, 50, 1, 20, 9], [13, 50, 1, 20, 8], [14, 50, 1, 20, 7], [15, 50, 1, 20, 6], [16, 50, 1, 20, 5], [17, 50, 1, 20, 4], [18, 50, 1, 20, 3], [19, 50, 1, 20, 2], [20, 50, 1, 20, 1]],veganFriendly = 1,maxPrice = 20,maxDistance = 10) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[11, 50, 1, 20, 10], [12, 50, 1, 20, 9], [13, 50, 1, 20, 8], [14, 50, 1, 20, 7], [15, 50, 1, 20, 6], [16, 50, 1, 20, 5], [17, 50, 1, 20, 4], [18, 50, 1, 20, 3], [19, 50, 1, 20, 2], [20, 50, 1, 20, 1]],veganFriendly = 1,maxPrice = 20,maxDistance = 10) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[6, 6, 0, 55, 15], [7, 7, 1, 35, 7], [8, 9, 0, 25, 8], [9, 7, 1, 5, 1], [10, 5, 0, 10, 4]],veganFriendly = 1,maxPrice = 40,maxDistance = 10) == [9, 7]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[6, 6, 0, 55, 15], [7, 7, 1, 35, 7], [8, 9, 0, 25, 8], [9, 7, 1, 5, 1], [10, 5, 0, 10, 4]],veganFriendly = 1,maxPrice = 40,maxDistance = 10) == [9, 7]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[16, 1, 0, 40, 7], [17, 3, 1, 20, 5], [18, 2, 1, 30, 4], [19, 4, 0, 50, 3], [20, 5, 1, 45, 2]],veganFriendly = 0,maxPrice = 45,maxDistance = 7) == [20, 17, 18, 16]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[16, 1, 0, 40, 7], [17, 3, 1, 20, 5], [18, 2, 1, 30, 4], [19, 4, 0, 50, 3], [20, 5, 1, 45, 2]],veganFriendly = 0,maxPrice = 45,maxDistance = 7) == [20, 17, 18, 16]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[101, 95, 1, 20, 15], [202, 85, 0, 55, 18], [303, 95, 1, 25, 12], [404, 75, 0, 22, 14], [505, 88, 1, 18, 16], [606, 80, 0, 30, 10]],veganFriendly = 1,maxPrice = 55,maxDistance = 20) == [303, 101, 505]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[101, 95, 1, 20, 15], [202, 85, 0, 55, 18], [303, 95, 1, 25, 12], [404, 75, 0, 22, 14], [505, 88, 1, 18, 16], [606, 80, 0, 30, 10]],veganFriendly = 1,maxPrice = 55,maxDistance = 20) == [303, 101, 505]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[701, 10, 0, 20, 1], [702, 9, 1, 25, 2], [703, 8, 0, 30, 3], [704, 7, 1, 15, 4], [705, 6, 0, 10, 5]],veganFriendly = 0,maxPrice = 30,maxDistance = 5) == [701, 702, 703, 704, 705]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[701, 10, 0, 20, 1], [702, 9, 1, 25, 2], [703, 8, 0, 30, 3], [704, 7, 1, 15, 4], [705, 6, 0, 10, 5]],veganFriendly = 0,maxPrice = 30,maxDistance = 5) == [701, 702, 703, 704, 705]: {e}')
    
    total += 1
    try:
        result = candidate(restaurants = [[46, 1, 0, 50, 10], [47, 3, 1, 45, 9], [48, 2, 1, 40, 8], [49, 4, 0, 35, 7], [50, 5, 1, 30, 6]],veganFriendly = 0,maxPrice = 45,maxDistance = 9) == [50, 49, 47, 48]
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(restaurants = [[46, 1, 0, 50, 10], [47, 3, 1, 45, 9], [48, 2, 1, 40, 8], [49, 4, 0, 35, 7], [50, 5, 1, 30, 6]],veganFriendly = 0,maxPrice = 45,maxDistance = 9) == [50, 49, 47, 48]: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],veganFriendly = 0,maxPrice = 50,maxDistance = 10) == [4, 3, 2, 1, 5]
    assert candidate(restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],veganFriendly = 0,maxPrice = 30,maxDistance = 3) == [4, 5]
    assert candidate(restaurants = [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],veganFriendly = 1,maxPrice = 50,maxDistance = 10) == [3, 1, 5]
    assert candidate(restaurants = [[100, 95, 1, 10, 1], [200, 94, 0, 20, 2], [300, 93, 1, 30, 3], [400, 92, 0, 40, 4], [500, 91, 1, 50, 5]],veganFriendly = 1,maxPrice = 50,maxDistance = 5) == [100, 300, 500]
    assert candidate(restaurants = [[101, 9, 1, 25, 7], [102, 7, 0, 35, 12], [103, 9, 1, 20, 5], [104, 5, 0, 20, 8], [105, 9, 1, 20, 5], [106, 8, 1, 30, 3], [107, 6, 0, 35, 6]],veganFriendly = 1,maxPrice = 30,maxDistance = 8) == [105, 103, 101, 106]
    assert candidate(restaurants = [[1001, 45, 1, 30, 12], [2002, 65, 0, 20, 6], [3003, 50, 1, 25, 7], [4004, 40, 0, 15, 4], [5005, 75, 1, 5, 2], [6006, 55, 0, 40, 22], [7007, 45, 1, 10, 16], [8008, 35, 0, 25, 12], [9009, 25, 1, 35, 22], [10010, 80, 1, 10, 6]],veganFriendly = 0,maxPrice = 45,maxDistance = 20) == [10010, 5005, 2002, 3003, 7007, 1001, 4004, 8008]
    assert candidate(restaurants = [[10001, 10, 1, 100, 100], [20002, 20, 0, 80, 90], [30003, 30, 1, 70, 80], [40004, 40, 0, 60, 70], [50005, 50, 1, 50, 60], [60006, 60, 0, 40, 50], [70007, 70, 1, 30, 40], [80008, 80, 0, 20, 30], [90009, 90, 1, 10, 20], [100010, 100, 1, 0, 10]],veganFriendly = 0,maxPrice = 100,maxDistance = 100) == [100010, 90009, 80008, 70007, 60006, 50005, 40004, 30003, 20002, 10001]
    assert candidate(restaurants = [[11, 3, 1, 20, 10], [12, 8, 1, 18, 8], [13, 5, 0, 15, 7], [14, 7, 0, 12, 6], [15, 9, 1, 9, 5]],veganFriendly = 1,maxPrice = 20,maxDistance = 10) == [15, 12, 11]
    assert candidate(restaurants = [[401, 5, 1, 10, 10], [402, 6, 1, 15, 9], [403, 7, 1, 20, 8], [404, 8, 1, 25, 7], [405, 9, 1, 30, 6], [406, 10, 1, 35, 5]],veganFriendly = 1,maxPrice = 20,maxDistance = 7) == []
    assert candidate(restaurants = [[101, 99, 1, 10, 5], [202, 98, 0, 20, 3], [303, 99, 1, 10, 2], [404, 98, 0, 25, 5], [505, 97, 1, 15, 4], [606, 98, 0, 10, 4]],veganFriendly = 1,maxPrice = 15,maxDistance = 5) == [303, 101, 505]
    assert candidate(restaurants = [[401, 10, 0, 10, 1], [402, 9, 1, 15, 2], [403, 8, 0, 20, 3], [404, 7, 1, 25, 4], [405, 6, 0, 30, 5], [406, 5, 1, 12, 6]],veganFriendly = 1,maxPrice = 25,maxDistance = 5) == [402, 404]
    assert candidate(restaurants = [[10, 9, 1, 15, 5], [11, 7, 0, 20, 6], [12, 9, 1, 18, 3], [13, 8, 0, 25, 4], [14, 7, 1, 10, 2], [15, 10, 0, 5, 1]],veganFriendly = 1,maxPrice = 20,maxDistance = 5) == [12, 10, 14]
    assert candidate(restaurants = [[30, 10, 1, 10, 1], [31, 9, 0, 15, 2], [32, 8, 1, 20, 3], [33, 7, 1, 25, 4], [34, 6, 0, 30, 5], [35, 5, 1, 35, 6]],veganFriendly = 1,maxPrice = 30,maxDistance = 5) == [30, 32, 33]
    assert candidate(restaurants = [[301, 9, 0, 15, 10], [302, 8, 1, 20, 8], [303, 7, 0, 25, 6], [304, 6, 1, 30, 4], [305, 5, 0, 35, 2], [306, 4, 1, 40, 0]],veganFriendly = 1,maxPrice = 20,maxDistance = 8) == [302]
    assert candidate(restaurants = [[26, 2, 1, 40, 10], [27, 8, 0, 35, 9], [28, 7, 1, 30, 8], [29, 9, 0, 25, 7], [30, 6, 1, 20, 6]],veganFriendly = 0,maxPrice = 35,maxDistance = 9) == [29, 27, 28, 30]
    assert candidate(restaurants = [[10001, 10, 1, 100, 100], [20002, 20, 0, 80, 90], [30003, 30, 1, 70, 80], [40004, 40, 0, 60, 70], [50005, 50, 1, 50, 60], [60006, 60, 0, 40, 50], [70007, 70, 1, 30, 40], [80008, 80, 0, 20, 30], [90009, 90, 1, 10, 20], [100010, 100, 1, 0, 10]],veganFriendly = 1,maxPrice = 60,maxDistance = 70) == [100010, 90009, 70007, 50005]
    assert candidate(restaurants = [[101, 80, 1, 10, 5], [202, 85, 0, 20, 3], [303, 80, 1, 10, 2], [404, 80, 0, 25, 5], [505, 85, 1, 15, 4], [606, 80, 0, 10, 4]],veganFriendly = 1,maxPrice = 20,maxDistance = 5) == [505, 303, 101]
    assert candidate(restaurants = [[101, 50, 1, 10, 5], [202, 70, 0, 20, 3], [303, 70, 1, 10, 2], [404, 80, 0, 25, 5], [505, 60, 1, 15, 4], [606, 60, 0, 10, 4]],veganFriendly = 1,maxPrice = 15,maxDistance = 4) == [303, 505]
    assert candidate(restaurants = [[24, 9, 1, 20, 5], [25, 10, 0, 25, 3], [26, 8, 1, 15, 2], [27, 7, 1, 10, 1], [28, 6, 0, 5, 1], [29, 5, 1, 30, 4]],veganFriendly = 1,maxPrice = 20,maxDistance = 3) == [26, 27]
    assert candidate(restaurants = [[1, 100, 1, 1, 1], [2, 100, 1, 2, 2], [3, 100, 1, 3, 3], [4, 100, 1, 4, 4], [5, 100, 1, 5, 5], [6, 100, 1, 6, 6], [7, 100, 1, 7, 7], [8, 100, 1, 8, 8], [9, 100, 1, 9, 9], [10, 100, 1, 10, 10]],veganFriendly = 1,maxPrice = 5,maxDistance = 5) == [5, 4, 3, 2, 1]
    assert candidate(restaurants = [[101, 10, 0, 100, 100], [102, 9, 1, 95, 95], [103, 8, 0, 90, 90], [104, 7, 1, 85, 85], [105, 6, 0, 80, 80]],veganFriendly = 0,maxPrice = 90,maxDistance = 90) == [103, 104, 105]
    assert candidate(restaurants = [[10001, 5, 0, 50, 50], [20002, 15, 1, 40, 40], [30003, 25, 0, 30, 30], [40004, 35, 1, 20, 20], [50005, 45, 0, 10, 10], [60006, 55, 1, 5, 5]],veganFriendly = 0,maxPrice = 40,maxDistance = 40) == [60006, 50005, 40004, 30003, 20002]
    assert candidate(restaurants = [[42, 10, 1, 10, 1], [43, 9, 0, 15, 2], [44, 8, 1, 20, 3], [45, 7, 1, 25, 4], [46, 6, 0, 30, 5], [47, 5, 1, 35, 6]],veganFriendly = 0,maxPrice = 5,maxDistance = 1) == []
    assert candidate(restaurants = [[21, 6, 0, 30, 9], [22, 7, 0, 25, 7], [23, 9, 1, 18, 5], [24, 8, 1, 22, 4], [25, 10, 0, 15, 3]],veganFriendly = 1,maxPrice = 25,maxDistance = 6) == [23, 24]
    assert candidate(restaurants = [[54, 10, 1, 10, 1], [55, 9, 0, 15, 2], [56, 8, 1, 20, 3], [57, 7, 1, 25, 4], [58, 6, 0, 30, 5], [59, 5, 1, 35, 6]],veganFriendly = 1,maxPrice = 35,maxDistance = 6) == [54, 56, 57, 59]
    assert candidate(restaurants = [[901, 9, 0, 10, 1], [902, 8, 1, 15, 2], [903, 7, 0, 20, 3], [904, 6, 1, 25, 4], [905, 5, 0, 12, 5]],veganFriendly = 0,maxPrice = 25,maxDistance = 5) == [901, 902, 903, 904, 905]
    assert candidate(restaurants = [[41, 2, 0, 45, 10], [42, 8, 1, 35, 9], [43, 7, 1, 30, 8], [44, 9, 0, 25, 7], [45, 6, 1, 20, 6]],veganFriendly = 1,maxPrice = 30,maxDistance = 7) == [45]
    assert candidate(restaurants = [[101, 80, 1, 10, 5], [202, 85, 0, 20, 3], [303, 80, 1, 10, 2], [404, 80, 0, 25, 5], [505, 85, 1, 15, 4], [606, 80, 0, 10, 4]],veganFriendly = 0,maxPrice = 10,maxDistance = 5) == [606, 303, 101]
    assert candidate(restaurants = [[101, 50, 1, 30, 10], [202, 20, 0, 20, 5], [303, 40, 1, 25, 8], [404, 30, 0, 15, 3], [505, 60, 1, 5, 1], [606, 55, 0, 40, 20], [707, 45, 1, 10, 15], [808, 35, 0, 25, 10], [909, 25, 1, 35, 20], [1010, 70, 1, 10, 5]],veganFriendly = 1,maxPrice = 35,maxDistance = 15) == [1010, 505, 101, 707, 303]
    assert candidate(restaurants = [[601, 7, 1, 25, 10], [602, 8, 0, 30, 15], [603, 9, 1, 45, 8], [604, 6, 0, 35, 15], [605, 8, 1, 50, 6], [606, 9, 1, 35, 10], [607, 7, 0, 40, 8]],veganFriendly = 0,maxPrice = 50,maxDistance = 20) == [606, 603, 605, 602, 607, 601, 604]
    assert candidate(restaurants = [[701, 10, 0, 20, 20], [702, 9, 0, 25, 25], [703, 8, 0, 30, 30], [704, 7, 0, 35, 35], [705, 6, 0, 40, 40], [706, 5, 0, 45, 45], [707, 4, 0, 50, 50], [708, 3, 0, 55, 55], [709, 2, 0, 60, 60], [710, 1, 0, 65, 65]],veganFriendly = 0,maxPrice = 40,maxDistance = 40) == [701, 702, 703, 704, 705]
    assert candidate(restaurants = [[36, 5, 1, 15, 2], [37, 4, 0, 10, 3], [38, 3, 1, 5, 4], [39, 2, 1, 20, 5], [40, 1, 0, 25, 6], [41, 8, 1, 10, 1]],veganFriendly = 1,maxPrice = 20,maxDistance = 5) == [41, 36, 38, 39]
    assert candidate(restaurants = [[101, 95, 1, 20, 15], [202, 85, 0, 55, 18], [303, 95, 1, 25, 12], [404, 75, 0, 22, 14], [505, 88, 1, 18, 16], [606, 80, 0, 30, 10]],veganFriendly = 1,maxPrice = 30,maxDistance = 20) == [303, 101, 505]
    assert candidate(restaurants = [[1, 5, 1, 10, 1], [2, 5, 1, 10, 1], [3, 5, 1, 10, 1], [4, 5, 1, 10, 1], [5, 5, 1, 10, 1]],veganFriendly = 1,maxPrice = 10,maxDistance = 1) == [5, 4, 3, 2, 1]
    assert candidate(restaurants = [[101, 80, 1, 10, 5], [202, 85, 0, 20, 3], [303, 80, 1, 10, 2], [404, 80, 0, 25, 5], [505, 85, 1, 15, 4], [606, 80, 0, 10, 4]],veganFriendly = 0,maxPrice = 25,maxDistance = 5) == [505, 202, 606, 404, 303, 101]
    assert candidate(restaurants = [[101, 5, 1, 100, 5], [102, 9, 0, 50, 4], [103, 6, 1, 40, 3], [104, 7, 0, 30, 2], [105, 8, 1, 20, 1], [106, 4, 0, 10, 6], [107, 9, 1, 15, 2]],veganFriendly = 0,maxPrice = 50,maxDistance = 4) == [107, 102, 105, 104, 103]
    assert candidate(restaurants = [[35, 6, 0, 20, 17], [36, 7, 1, 45, 21], [37, 6, 0, 35, 15], [38, 9, 1, 25, 10], [39, 8, 0, 45, 25], [40, 11, 1, 10, 4], [41, 13, 0, 22, 18]],veganFriendly = 1,maxPrice = 45,maxDistance = 25) == [40, 38, 36]
    assert candidate(restaurants = [[201, 10, 0, 1000, 50], [202, 9, 1, 900, 45], [203, 8, 0, 800, 40], [204, 7, 1, 700, 35], [205, 6, 0, 600, 30], [206, 5, 1, 500, 25], [207, 4, 0, 400, 20], [208, 3, 1, 300, 15], [209, 2, 0, 200, 10], [210, 1, 1, 100, 5]],veganFriendly = 1,maxPrice = 500,maxDistance = 30) == [206, 208, 210]
    assert candidate(restaurants = [[301, 7, 0, 20, 4], [302, 9, 1, 10, 2], [303, 6, 0, 25, 5], [304, 8, 1, 15, 3], [305, 9, 0, 30, 1], [306, 7, 1, 12, 6]],veganFriendly = 0,maxPrice = 15,maxDistance = 4) == [302, 304]
    assert candidate(restaurants = [[401, 8, 1, 25, 10], [402, 7, 0, 30, 15], [403, 9, 1, 20, 5], [404, 8, 0, 20, 8], [405, 6, 1, 20, 5], [406, 9, 1, 30, 3], [407, 5, 0, 35, 6]],veganFriendly = 1,maxPrice = 30,maxDistance = 15) == [406, 403, 401, 405]
    assert candidate(restaurants = [[101, 90, 1, 30, 5], [202, 85, 0, 40, 10], [303, 90, 1, 30, 4], [404, 85, 0, 45, 8], [505, 85, 1, 25, 6], [606, 80, 0, 35, 7]],veganFriendly = 1,maxPrice = 35,maxDistance = 10) == [303, 101, 505]
    assert candidate(restaurants = [[101, 50, 1, 30, 10], [202, 20, 0, 20, 5], [303, 40, 1, 25, 8], [404, 30, 0, 15, 3], [505, 60, 1, 5, 1], [606, 55, 0, 40, 20], [707, 45, 1, 10, 15], [808, 35, 0, 25, 10], [909, 25, 1, 35, 20], [1010, 70, 1, 10, 5]],veganFriendly = 0,maxPrice = 20,maxDistance = 5) == [1010, 505, 404, 202]
    assert candidate(restaurants = [[701, 6, 1, 25, 10], [702, 8, 0, 30, 15], [703, 7, 1, 45, 8], [704, 9, 0, 35, 15], [705, 5, 1, 50, 6], [706, 8, 1, 35, 10], [707, 6, 0, 40, 8]],veganFriendly = 1,maxPrice = 40,maxDistance = 15) == [706, 701]
    assert candidate(restaurants = [[22, 6, 0, 20, 17], [23, 7, 1, 45, 21], [24, 6, 0, 35, 15], [25, 9, 1, 25, 10], [26, 8, 0, 45, 25], [27, 11, 1, 10, 4]],veganFriendly = 1,maxPrice = 40,maxDistance = 20) == [27, 25]
    assert candidate(restaurants = [[301, 6, 1, 30, 10], [302, 8, 0, 40, 12], [303, 7, 1, 45, 8], [304, 9, 1, 50, 6], [305, 5, 0, 35, 15], [306, 8, 1, 45, 10], [307, 7, 0, 40, 8]],veganFriendly = 0,maxPrice = 50,maxDistance = 15) == [304, 306, 302, 307, 303, 301, 305]
    assert candidate(restaurants = [[101, 100, 1, 5, 5], [102, 100, 1, 5, 6], [103, 100, 1, 5, 7], [104, 100, 1, 5, 8], [105, 100, 1, 5, 9]],veganFriendly = 1,maxPrice = 5,maxDistance = 9) == [105, 104, 103, 102, 101]
    assert candidate(restaurants = [[501, 10, 0, 50, 100], [502, 10, 0, 55, 95], [503, 10, 0, 60, 90], [504, 10, 0, 65, 85], [505, 10, 0, 70, 80], [506, 10, 0, 75, 75], [507, 10, 0, 80, 70], [508, 10, 0, 85, 65], [509, 10, 0, 90, 60]],veganFriendly = 0,maxPrice = 80,maxDistance = 70) == [507]
    assert candidate(restaurants = [[36, 6, 1, 40, 9], [37, 8, 0, 35, 8], [38, 7, 1, 30, 7], [39, 9, 0, 25, 6], [40, 10, 1, 20, 5]],veganFriendly = 1,maxPrice = 30,maxDistance = 8) == [40, 38]
    assert candidate(restaurants = [[101, 1, 1, 5, 5], [102, 1, 1, 6, 6], [103, 1, 1, 7, 7], [104, 1, 1, 8, 8], [105, 1, 1, 9, 9]],veganFriendly = 1,maxPrice = 10,maxDistance = 10) == [105, 104, 103, 102, 101]
    assert candidate(restaurants = [[101, 50, 1, 30, 10], [202, 20, 0, 20, 5], [303, 40, 1, 25, 8], [404, 30, 0, 15, 3], [505, 60, 1, 5, 1], [606, 55, 0, 40, 20], [707, 45, 1, 10, 15], [808, 35, 0, 25, 10], [909, 25, 1, 35, 20], [1010, 70, 1, 10, 5]],veganFriendly = 1,maxPrice = 50,maxDistance = 20) == [1010, 505, 101, 707, 303, 909]
    assert candidate(restaurants = [[2001, 100, 0, 50, 50], [2002, 99, 1, 49, 49], [2003, 98, 0, 48, 48], [2004, 97, 1, 47, 47], [2005, 96, 0, 46, 46]],veganFriendly = 0,maxPrice = 50,maxDistance = 50) == [2001, 2002, 2003, 2004, 2005]
    assert candidate(restaurants = [[10, 10, 0, 100, 100], [20, 9, 1, 90, 90], [30, 8, 0, 80, 80], [40, 7, 1, 70, 70], [50, 6, 0, 60, 60]],veganFriendly = 0,maxPrice = 100,maxDistance = 100) == [10, 20, 30, 40, 50]
    assert candidate(restaurants = [[31, 1, 0, 45, 10], [32, 3, 0, 30, 8], [33, 2, 1, 25, 6], [34, 4, 1, 20, 5], [35, 5, 0, 15, 4]],veganFriendly = 1,maxPrice = 25,maxDistance = 7) == [34, 33]
    assert candidate(restaurants = [[101, 6, 0, 20, 5], [102, 9, 1, 18, 2], [103, 5, 0, 10, 3], [104, 8, 1, 12, 4], [105, 7, 1, 15, 6], [106, 9, 0, 22, 3]],veganFriendly = 0,maxPrice = 25,maxDistance = 6) == [106, 102, 104, 105, 101, 103]
    assert candidate(restaurants = [[101, 95, 1, 20, 15], [202, 85, 0, 55, 18], [303, 95, 1, 25, 12], [404, 75, 0, 22, 14], [505, 88, 1, 18, 16], [606, 80, 0, 30, 10]],veganFriendly = 0,maxPrice = 55,maxDistance = 20) == [303, 101, 505, 202, 606, 404]
    assert candidate(restaurants = [[601, 9, 1, 10, 1], [602, 8, 0, 15, 2], [603, 7, 1, 20, 3], [604, 6, 0, 25, 4], [605, 5, 1, 12, 5]],veganFriendly = 1,maxPrice = 15,maxDistance = 4) == [601]
    assert candidate(restaurants = [[10001, 5, 0, 50, 50], [20002, 15, 1, 40, 40], [30003, 25, 0, 30, 30], [40004, 35, 1, 20, 20], [50005, 45, 0, 10, 10], [60006, 55, 1, 5, 5]],veganFriendly = 1,maxPrice = 50,maxDistance = 50) == [60006, 40004, 20002]
    assert candidate(restaurants = [[801, 8, 1, 15, 3], [802, 9, 0, 10, 2], [803, 7, 1, 25, 4], [804, 6, 0, 20, 5], [805, 5, 1, 12, 1]],veganFriendly = 1,maxPrice = 20,maxDistance = 4) == [801, 805]
    assert candidate(restaurants = [[48, 1, 1, 5, 1], [49, 2, 0, 10, 2], [50, 3, 1, 15, 3], [51, 4, 1, 20, 4], [52, 5, 0, 25, 5], [53, 6, 1, 30, 6]],veganFriendly = 1,maxPrice = 25,maxDistance = 5) == [51, 50, 48]
    assert candidate(restaurants = [[10, 9, 1, 25, 7], [20, 8, 0, 35, 9], [30, 10, 1, 20, 5], [40, 7, 0, 45, 3], [50, 6, 1, 15, 2]],veganFriendly = 1,maxPrice = 30,maxDistance = 8) == [30, 10, 50]
    assert candidate(restaurants = [[1, 99, 0, 1, 1], [2, 98, 0, 2, 2], [3, 97, 0, 3, 3], [4, 96, 0, 4, 4], [5, 95, 0, 5, 5], [6, 94, 0, 6, 6], [7, 93, 0, 7, 7], [8, 92, 0, 8, 8], [9, 91, 0, 9, 9]],veganFriendly = 0,maxPrice = 9,maxDistance = 9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert candidate(restaurants = [[3001, 9, 1, 9, 9], [3002, 8, 0, 8, 8], [3003, 7, 1, 7, 7], [3004, 6, 0, 6, 6], [3005, 5, 1, 5, 5], [3006, 4, 0, 4, 4], [3007, 3, 1, 3, 3], [3008, 2, 0, 2, 2], [3009, 1, 1, 1, 1]],veganFriendly = 1,maxPrice = 10,maxDistance = 10) == [3001, 3003, 3005, 3007, 3009]
    assert candidate(restaurants = [[51, 6, 1, 40, 10], [52, 8, 1, 35, 9], [53, 7, 1, 30, 8], [54, 9, 1, 25, 7], [55, 10, 1, 20, 6]],veganFriendly = 1,maxPrice = 30,maxDistance = 8) == [55, 54, 53]
    assert candidate(restaurants = [[501, 6, 1, 10, 5], [502, 7, 0, 15, 4], [503, 8, 1, 20, 3], [504, 9, 0, 25, 2], [505, 10, 1, 12, 1]],veganFriendly = 0,maxPrice = 25,maxDistance = 5) == [505, 504, 503, 502, 501]
    assert candidate(restaurants = [[101, 80, 1, 10, 5], [202, 85, 0, 20, 3], [303, 80, 1, 10, 2], [404, 80, 0, 25, 5], [505, 85, 1, 15, 4], [606, 80, 0, 10, 4]],veganFriendly = 1,maxPrice = 100,maxDistance = 100) == [505, 303, 101]
    assert candidate(restaurants = [[201, 3, 0, 40, 15], [202, 5, 1, 45, 20], [203, 8, 1, 50, 10], [204, 4, 0, 50, 25], [205, 6, 0, 40, 15], [206, 7, 1, 45, 15], [207, 9, 1, 35, 10]],veganFriendly = 1,maxPrice = 50,maxDistance = 20) == [207, 203, 206, 202]
    assert candidate(restaurants = [[100, 90, 1, 10, 20], [200, 85, 0, 15, 25], [300, 80, 1, 5, 15], [400, 75, 0, 25, 10], [500, 70, 1, 20, 5]],veganFriendly = 0,maxPrice = 25,maxDistance = 20) == [100, 300, 400, 500]
    assert candidate(restaurants = [[201, 8, 1, 10, 4], [202, 6, 0, 15, 3], [203, 9, 1, 20, 2], [204, 7, 0, 25, 5], [205, 8, 1, 12, 3], [206, 9, 0, 30, 4]],veganFriendly = 1,maxPrice = 30,maxDistance = 5) == [203, 205, 201]
    assert candidate(restaurants = [[17, 2, 0, 30, 13], [18, 5, 1, 40, 18], [19, 7, 1, 50, 22], [20, 1, 0, 60, 30], [21, 4, 0, 10, 2]],veganFriendly = 1,maxPrice = 55,maxDistance = 28) == [19, 18]
    assert candidate(restaurants = [[11, 3, 1, 60, 20], [12, 8, 0, 70, 22], [13, 9, 1, 20, 10], [14, 10, 0, 5, 5], [15, 8, 1, 35, 12], [16, 12, 0, 15, 9]],veganFriendly = 0,maxPrice = 75,maxDistance = 25) == [16, 14, 13, 15, 12, 11]
    assert candidate(restaurants = [[66, 1, 1, 1, 1], [77, 1, 0, 2, 2], [88, 2, 1, 3, 3], [99, 2, 0, 4, 4], [100, 3, 1, 5, 5]],veganFriendly = 0,maxPrice = 5,maxDistance = 5) == [100, 99, 88, 77, 66]
    assert candidate(restaurants = [[12, 3, 0, 60, 7], [13, 2, 1, 45, 6], [14, 5, 1, 55, 8], [15, 4, 0, 35, 5], [16, 6, 1, 40, 9], [17, 7, 1, 30, 3]],veganFriendly = 1,maxPrice = 50,maxDistance = 10) == [17, 16, 13]
    assert candidate(restaurants = [[18, 9, 1, 20, 5], [19, 10, 0, 25, 3], [20, 8, 1, 15, 2], [21, 7, 1, 10, 1], [22, 6, 0, 5, 1], [23, 5, 1, 30, 4]],veganFriendly = 0,maxPrice = 100,maxDistance = 10) == [19, 18, 20, 21, 22, 23]
    assert candidate(restaurants = [[60, 10, 1, 10, 1], [61, 9, 0, 15, 2], [62, 8, 1, 20, 3], [63, 7, 1, 25, 4], [64, 6, 0, 30, 5], [65, 5, 1, 35, 6]],veganFriendly = 1,maxPrice = 10,maxDistance = 1) == [60]
    assert candidate(restaurants = [[1001, 1, 1, 1, 1], [1002, 2, 0, 2, 2], [1003, 3, 1, 3, 3], [1004, 4, 0, 4, 4], [1005, 5, 1, 5, 5], [1006, 6, 0, 6, 6], [1007, 7, 1, 7, 7]],veganFriendly = 1,maxPrice = 7,maxDistance = 7) == [1007, 1005, 1003, 1001]
    assert candidate(restaurants = [[28, 5, 0, 30, 15], [29, 8, 1, 40, 20], [30, 6, 0, 25, 10], [31, 7, 1, 5, 5], [32, 9, 0, 10, 4], [33, 12, 1, 35, 12], [34, 10, 0, 15, 9]],veganFriendly = 0,maxPrice = 55,maxDistance = 28) == [33, 34, 32, 29, 31, 30, 28]
    assert candidate(restaurants = [[10, 9, 1, 20, 1], [20, 8, 0, 10, 2], [30, 7, 1, 5, 3], [40, 10, 1, 15, 2], [50, 6, 0, 25, 4], [60, 8, 1, 30, 1]],veganFriendly = 1,maxPrice = 30,maxDistance = 3) == [40, 10, 60, 30]
    assert candidate(restaurants = [[6, 5, 1, 20, 5], [7, 7, 0, 25, 3], [8, 6, 1, 15, 2], [9, 9, 1, 10, 1], [10, 10, 0, 5, 1], [11, 8, 1, 30, 4]],veganFriendly = 1,maxPrice = 25,maxDistance = 4) == [9, 8]
    assert candidate(restaurants = [[1, 100, 1, 1, 1], [2, 99, 0, 2, 2], [3, 98, 1, 3, 3], [4, 97, 0, 4, 4], [5, 96, 1, 5, 5], [6, 95, 0, 6, 6], [7, 94, 1, 7, 7], [8, 93, 0, 8, 8], [9, 92, 1, 9, 9], [10, 91, 0, 10, 10]],veganFriendly = 1,maxPrice = 10,maxDistance = 10) == [1, 3, 5, 7, 9]
    assert candidate(restaurants = [[6, 9, 0, 20, 6], [7, 7, 1, 15, 3], [8, 6, 1, 25, 2], [9, 10, 0, 5, 1], [10, 4, 1, 35, 8]],veganFriendly = 1,maxPrice = 30,maxDistance = 5) == [7, 8]
    assert candidate(restaurants = [[1000, 95, 1, 40, 50], [2000, 90, 0, 50, 60], [3000, 85, 1, 30, 40], [4000, 80, 0, 40, 30], [5000, 75, 1, 20, 20], [6000, 70, 0, 30, 10]],veganFriendly = 1,maxPrice = 30,maxDistance = 30) == [5000]
    assert candidate(restaurants = [[501, 9, 1, 25, 7], [502, 6, 0, 40, 12], [503, 8, 1, 45, 8], [504, 7, 0, 35, 15], [505, 9, 1, 50, 6], [506, 6, 1, 35, 10], [507, 8, 0, 40, 8]],veganFriendly = 1,maxPrice = 50,maxDistance = 20) == [505, 501, 503, 506]
    assert candidate(restaurants = [[11, 3, 1, 10, 10], [22, 2, 0, 9, 9], [33, 3, 1, 8, 8], [44, 2, 0, 7, 7], [55, 3, 1, 6, 6]],veganFriendly = 1,maxPrice = 10,maxDistance = 10) == [55, 33, 11]
    assert candidate(restaurants = [[601, 5, 1, 5, 5], [602, 6, 1, 10, 10], [603, 7, 1, 15, 15], [604, 8, 1, 20, 20], [605, 9, 1, 25, 25], [606, 10, 1, 30, 30]],veganFriendly = 1,maxPrice = 25,maxDistance = 25) == [605, 604, 603, 602, 601]
    assert candidate(restaurants = [[11, 50, 1, 20, 10], [12, 50, 1, 20, 9], [13, 50, 1, 20, 8], [14, 50, 1, 20, 7], [15, 50, 1, 20, 6], [16, 50, 1, 20, 5], [17, 50, 1, 20, 4], [18, 50, 1, 20, 3], [19, 50, 1, 20, 2], [20, 50, 1, 20, 1]],veganFriendly = 1,maxPrice = 20,maxDistance = 10) == [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
    assert candidate(restaurants = [[6, 6, 0, 55, 15], [7, 7, 1, 35, 7], [8, 9, 0, 25, 8], [9, 7, 1, 5, 1], [10, 5, 0, 10, 4]],veganFriendly = 1,maxPrice = 40,maxDistance = 10) == [9, 7]
    assert candidate(restaurants = [[16, 1, 0, 40, 7], [17, 3, 1, 20, 5], [18, 2, 1, 30, 4], [19, 4, 0, 50, 3], [20, 5, 1, 45, 2]],veganFriendly = 0,maxPrice = 45,maxDistance = 7) == [20, 17, 18, 16]
    assert candidate(restaurants = [[101, 95, 1, 20, 15], [202, 85, 0, 55, 18], [303, 95, 1, 25, 12], [404, 75, 0, 22, 14], [505, 88, 1, 18, 16], [606, 80, 0, 30, 10]],veganFriendly = 1,maxPrice = 55,maxDistance = 20) == [303, 101, 505]
    assert candidate(restaurants = [[701, 10, 0, 20, 1], [702, 9, 1, 25, 2], [703, 8, 0, 30, 3], [704, 7, 1, 15, 4], [705, 6, 0, 10, 5]],veganFriendly = 0,maxPrice = 30,maxDistance = 5) == [701, 702, 703, 704, 705]
    assert candidate(restaurants = [[46, 1, 0, 50, 10], [47, 3, 1, 45, 9], [48, 2, 1, 40, 8], [49, 4, 0, 35, 7], [50, 5, 1, 30, 6]],veganFriendly = 0,maxPrice = 45,maxDistance = 9) == [50, 49, 47, 48]


