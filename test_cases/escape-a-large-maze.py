def calculate_accuracy(candidate):
    """
    Calculate accuracy by running all test cases and counting pass/fail
    Returns: (passed_count, total_count, accuracy_percentage)
    """
    passed = 0
    total = 0
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]],source = [0, 0],target = [6, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]],source = [0, 0],target = [6, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[5, 5]],source = [4, 4],target = [6, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[5, 5]],source = [4, 4],target = [6, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [],source = [0, 0],target = [999999, 999999]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [],source = [0, 0],target = [999999, 999999]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 2], [2, 1], [2, 3], [3, 2]],source = [0, 0],target = [4, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 2], [2, 1], [2, 3], [3, 2]],source = [0, 0],target = [4, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[10, 10], [11, 10], [12, 10], [13, 10]],source = [9, 9],target = [14, 14]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[10, 10], [11, 10], [12, 10], [13, 10]],source = [9, 9],target = [14, 14]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[500000, 500000]],source = [499999, 499999],target = [500001, 500001]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[500000, 500000]],source = [499999, 499999],target = [500001, 500001]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[10, 10], [10, 11], [10, 12], [11, 10], [11, 11], [11, 12], [12, 10], [12, 11], [12, 12]],source = [9, 9],target = [13, 13]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[10, 10], [10, 11], [10, 12], [11, 10], [11, 11], [11, 12], [12, 10], [12, 11], [12, 12]],source = [9, 9],target = [13, 13]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[0, 1], [1, 0], [2, 0], [0, 2]],source = [0, 0],target = [3, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[0, 1], [1, 0], [2, 0], [0, 2]],source = [0, 0],target = [3, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 7], [7, 5], [7, 6], [7, 7]],source = [4, 4],target = [8, 8]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 7], [7, 5], [7, 6], [7, 7]],source = [4, 4],target = [8, 8]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [2, 2], [3, 3]],source = [0, 0],target = [3, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [2, 2], [3, 3]],source = [0, 0],target = [3, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[10, 10], [11, 10], [10, 11], [11, 11]],source = [0, 0],target = [20, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[10, 10], [11, 10], [10, 11], [11, 11]],source = [0, 0],target = [20, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[0, 3], [1, 3], [2, 3], [3, 3]],source = [0, 0],target = [0, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[0, 3], [1, 3], [2, 3], [3, 3]],source = [0, 0],target = [0, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[0, 1], [1, 0]],source = [0, 0],target = [0, 2]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[0, 1], [1, 0]],source = [0, 0],target = [0, 2]) == False: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[0, 1], [1, 1], [2, 1], [3, 1]],source = [0, 0],target = [0, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[0, 1], [1, 1], [2, 1], [3, 1]],source = [0, 0],target = [0, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [1, 2], [2, 1]],source = [0, 0],target = [3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [1, 2], [2, 1]],source = [0, 0],target = [3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[100, 100], [100, 101], [101, 100], [101, 101], [200, 200], [200, 201], [201, 200], [201, 201]],source = [0, 0],target = [300, 300]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[100, 100], [100, 101], [101, 100], [101, 101], [200, 200], [200, 201], [201, 200], [201, 201]],source = [0, 0],target = [300, 300]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],source = [0, 0],target = [11, 11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],source = [0, 0],target = [11, 11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[999997, 999998], [999998, 999998], [999999, 999998], [999997, 999999], [999998, 999999], [999999, 999999]],source = [999995, 999995],target = [999999, 999999]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[999997, 999998], [999998, 999998], [999999, 999998], [999997, 999999], [999998, 999999], [999999, 999999]],source = [999995, 999995],target = [999999, 999999]) == False: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[50, 50], [50, 51], [50, 52], [50, 53], [51, 50], [51, 51], [51, 52], [51, 53], [52, 50], [52, 51], [52, 52], [52, 53], [53, 50], [53, 51], [53, 52], [53, 53]],source = [0, 0],target = [100, 100]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[50, 50], [50, 51], [50, 52], [50, 53], [51, 50], [51, 51], [51, 52], [51, 53], [52, 50], [52, 51], [52, 52], [52, 53], [53, 50], [53, 51], [53, 52], [53, 53]],source = [0, 0],target = [100, 100]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[500, 500], [501, 500], [502, 500], [500, 501], [501, 501], [502, 501], [500, 502], [501, 502], [502, 502]],source = [500, 499],target = [502, 503]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[500, 500], [501, 500], [502, 500], [500, 501], [501, 501], [502, 501], [500, 502], [501, 502], [502, 502]],source = [500, 499],target = [502, 503]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1000, 1000], [1001, 1000], [1000, 1001], [1001, 1001], [1002, 1000], [1000, 1002], [1002, 1002], [1001, 1002], [1003, 1001], [1001, 1003]],source = [500, 500],target = [1500, 1500]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1000, 1000], [1001, 1000], [1000, 1001], [1001, 1001], [1002, 1000], [1000, 1002], [1002, 1002], [1001, 1002], [1003, 1001], [1001, 1003]],source = [500, 500],target = [1500, 1500]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[999998, 999998], [999998, 999999], [999999, 999998], [999999, 999999]],source = [999997, 999997],target = [999998, 999997]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[999998, 999998], [999998, 999999], [999999, 999998], [999999, 999999]],source = [999997, 999997],target = [999998, 999997]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],source = [0, 0],target = [9, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],source = [0, 0],target = [9, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[5, 4], [4, 5], [6, 5], [5, 6]],source = [5, 5],target = [6, 6]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[5, 4], [4, 5], [6, 5], [5, 6]],source = [5, 5],target = [6, 6]) == False: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[500000, 500000], [500001, 500001], [500002, 500002], [500003, 500003]],source = [499999, 499999],target = [500004, 500004]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[500000, 500000], [500001, 500001], [500002, 500002], [500003, 500003]],source = [499999, 499999],target = [500004, 500004]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 2], [2, 1], [2, 3], [3, 2], [4, 3], [5, 4]],source = [0, 0],target = [6, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 2], [2, 1], [2, 3], [3, 2], [4, 3], [5, 4]],source = [0, 0],target = [6, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [3, 2], [3, 3]],source = [10, 10],target = [0, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [3, 2], [3, 3]],source = [10, 10],target = [0, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[999998, 999998], [999997, 999998], [999996, 999998], [999998, 999997], [999997, 999997], [999996, 999997], [999998, 999996], [999997, 999996], [999996, 999996]],source = [999995, 999995],target = [999999, 999999]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[999998, 999998], [999997, 999998], [999996, 999998], [999998, 999997], [999997, 999997], [999996, 999997], [999998, 999996], [999997, 999996], [999996, 999996]],source = [999995, 999995],target = [999999, 999999]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[500000, 500000], [500001, 500000], [500002, 500000], [500000, 500001], [500001, 500001], [500002, 500001]],source = [499999, 499999],target = [500001, 500001]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[500000, 500000], [500001, 500000], [500002, 500000], [500000, 500001], [500001, 500001], [500002, 500001]],source = [499999, 499999],target = [500001, 500001]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[10, 10], [11, 10], [12, 10], [10, 11], [10, 12], [11, 11], [11, 12], [12, 11], [12, 12], [13, 13], [14, 14], [13, 14], [14, 13]],source = [0, 0],target = [20, 20]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[10, 10], [11, 10], [12, 10], [10, 11], [10, 12], [11, 11], [11, 12], [12, 11], [12, 12], [13, 13], [14, 14], [13, 14], [14, 13]],source = [0, 0],target = [20, 20]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[999999, 999998], [999998, 999999]],source = [0, 0],target = [999998, 999997]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[999999, 999998], [999998, 999999]],source = [0, 0],target = [999998, 999997]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4]],source = [0, 0],target = [0, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4]],source = [0, 0],target = [0, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [2, 1], [3, 1], [1, 2], [2, 2], [3, 2], [1, 3], [2, 3], [3, 3], [1, 4], [2, 4], [3, 4], [1, 5], [2, 5], [3, 5]],source = [0, 0],target = [3, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [2, 1], [3, 1], [1, 2], [2, 2], [3, 2], [1, 3], [2, 3], [3, 3], [1, 4], [2, 4], [3, 4], [1, 5], [2, 5], [3, 5]],source = [0, 0],target = [3, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[999999, 999999]],source = [0, 0],target = [999998, 999998]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[999999, 999999]],source = [0, 0],target = [999998, 999998]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 2], [2, 3], [2, 4], [2, 5]],source = [0, 0],target = [6, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 2], [2, 3], [2, 4], [2, 5]],source = [0, 0],target = [6, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]],source = [0, 0],target = [10, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]],source = [0, 0],target = [10, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[100000, 100000], [100001, 100000], [100002, 100000], [100003, 100000], [100004, 100000], [100005, 100000], [100006, 100000], [100007, 100000]],source = [99999, 99999],target = [100008, 100008]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[100000, 100000], [100001, 100000], [100002, 100000], [100003, 100000], [100004, 100000], [100005, 100000], [100006, 100000], [100007, 100000]],source = [99999, 99999],target = [100008, 100008]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [1, 2], [2, 1], [2, 2]],source = [0, 0],target = [3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [1, 2], [2, 1], [2, 2]],source = [0, 0],target = [3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3]],source = [0, 0],target = [5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3]],source = [0, 0],target = [5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[500000, 0], [500001, 0], [500002, 0], [500003, 0], [500004, 0], [500005, 0], [500006, 0], [500007, 0], [500008, 0], [500009, 0]],source = [499990, 0],target = [500010, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[500000, 0], [500001, 0], [500002, 0], [500003, 0], [500004, 0], [500005, 0], [500006, 0], [500007, 0], [500008, 0], [500009, 0]],source = [499990, 0],target = [500010, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[0, 0], [1, 0], [2, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 1], [2, 2], [1, 3], [2, 3]],source = [0, 3],target = [3, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[0, 0], [1, 0], [2, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 1], [2, 2], [1, 3], [2, 3]],source = [0, 3],target = [3, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[0, 1], [1, 0], [1, 1]],source = [2, 2],target = [3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[0, 1], [1, 0], [1, 1]],source = [2, 2],target = [3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[10, 10], [11, 10], [12, 10], [10, 11], [11, 11], [10, 12]],source = [9, 9],target = [13, 13]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[10, 10], [11, 10], [12, 10], [10, 11], [11, 11], [10, 12]],source = [9, 9],target = [13, 13]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 1], [4, 2], [4, 3]],source = [0, 0],target = [5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 1], [4, 2], [4, 3]],source = [0, 0],target = [5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[500000, 500000], [500001, 500001], [500002, 500002]],source = [500000, 500001],target = [500002, 500000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[500000, 500000], [500001, 500001], [500002, 500002]],source = [500000, 500001],target = [500002, 500000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[500000, 500000], [500001, 500000], [500002, 500000], [500003, 500000], [500004, 500000], [500005, 500000], [500000, 500001], [500000, 500002], [500000, 500003], [500000, 500004], [500000, 500005]],source = [499999, 500000],target = [500006, 500006]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[500000, 500000], [500001, 500000], [500002, 500000], [500003, 500000], [500004, 500000], [500005, 500000], [500000, 500001], [500000, 500002], [500000, 500003], [500000, 500004], [500000, 500005]],source = [499999, 500000],target = [500006, 500006]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8]],source = [0, 0],target = [5, 9]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8]],source = [0, 0],target = [5, 9]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[100, 100], [101, 100], [102, 100], [100, 101], [101, 101], [102, 101], [100, 102], [101, 102], [102, 102]],source = [99, 99],target = [103, 103]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[100, 100], [101, 100], [102, 100], [100, 101], [101, 101], [102, 101], [100, 102], [101, 102], [102, 102]],source = [99, 99],target = [103, 103]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],source = [0, 0],target = [3, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],source = [0, 0],target = [3, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[0, 1], [1, 0], [1, 1], [2, 1], [1, 2], [2, 2], [3, 2], [2, 3], [3, 3], [4, 3], [3, 4], [4, 4], [5, 4], [4, 5], [5, 5], [6, 5], [5, 6], [6, 6], [7, 6], [6, 7], [7, 7]],source = [0, 0],target = [10, 10]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[0, 1], [1, 0], [1, 1], [2, 1], [1, 2], [2, 2], [3, 2], [2, 3], [3, 3], [4, 3], [3, 4], [4, 4], [5, 4], [4, 5], [5, 5], [6, 5], [5, 6], [6, 6], [7, 6], [6, 7], [7, 7]],source = [0, 0],target = [10, 10]) == False: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [2, 1], [1, 2], [2, 2]],source = [0, 0],target = [3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [2, 1], [1, 2], [2, 2]],source = [0, 0],target = [3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[100, 100], [101, 100], [102, 100], [100, 101], [101, 101], [102, 101], [100, 102], [101, 102], [102, 102]],source = [50, 50],target = [150, 150]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[100, 100], [101, 100], [102, 100], [100, 101], [101, 101], [102, 101], [100, 102], [101, 102], [102, 102]],source = [50, 50],target = [150, 150]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[100, 100], [101, 100], [102, 100], [103, 100], [104, 100], [100, 101], [100, 102], [100, 103], [100, 104], [101, 101], [101, 102], [101, 103], [102, 101], [102, 102], [103, 101]],source = [100, 100],target = [104, 104]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[100, 100], [101, 100], [102, 100], [103, 100], [104, 100], [100, 101], [100, 102], [100, 103], [100, 104], [101, 101], [101, 102], [101, 103], [102, 101], [102, 102], [103, 101]],source = [100, 100],target = [104, 104]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[999999, 999998], [999998, 999999], [999998, 999998]],source = [999997, 999997],target = [999999, 999999]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[999999, 999998], [999998, 999999], [999998, 999998]],source = [999997, 999997],target = [999999, 999999]) == False: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[999999, 999999], [999998, 999998], [999997, 999997]],source = [999996, 999996],target = [0, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[999999, 999999], [999998, 999998], [999997, 999997]],source = [999996, 999996],target = [0, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4]],source = [0, 5],target = [5, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4]],source = [0, 5],target = [5, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[500000, 500000], [500001, 500000], [500000, 500001], [500001, 500001]],source = [499999, 499999],target = [500002, 500002]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[500000, 500000], [500001, 500000], [500000, 500001], [500001, 500001]],source = [499999, 499999],target = [500002, 500002]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[10, 10], [11, 10], [10, 11], [11, 11], [12, 10], [10, 12], [12, 12], [11, 12], [13, 11], [11, 13]],source = [0, 0],target = [14, 14]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[10, 10], [11, 10], [10, 11], [11, 11], [12, 10], [10, 12], [12, 12], [11, 12], [13, 11], [11, 13]],source = [0, 0],target = [14, 14]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[999999, 999999], [999998, 999998], [999997, 999997], [999996, 999996], [999995, 999995]],source = [0, 0],target = [999999, 999999]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[999999, 999999], [999998, 999998], [999997, 999997], [999996, 999996], [999995, 999995]],source = [0, 0],target = [999999, 999999]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],source = [0, 0],target = [0, 11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],source = [0, 0],target = [0, 11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9]],source = [0, 0],target = [999999, 999999]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9]],source = [0, 0],target = [999999, 999999]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[0, 500000], [0, 500001], [0, 500002], [0, 500003], [0, 500004], [0, 500005], [0, 500006], [0, 500007], [0, 500008], [0, 500009]],source = [0, 499990],target = [0, 500010]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[0, 500000], [0, 500001], [0, 500002], [0, 500003], [0, 500004], [0, 500005], [0, 500006], [0, 500007], [0, 500008], [0, 500009]],source = [0, 499990],target = [0, 500010]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [2, 1], [3, 1], [1, 2], [2, 2], [3, 2], [1, 3], [2, 3], [3, 3]],source = [0, 0],target = [3, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [2, 1], [3, 1], [1, 2], [2, 2], [3, 2], [1, 3], [2, 3], [3, 3]],source = [0, 0],target = [3, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[100, 100], [101, 100], [100, 101], [101, 101], [102, 100], [100, 102], [102, 102], [101, 102], [103, 101], [101, 103], [104, 101], [101, 104], [105, 101], [101, 105]],source = [50, 50],target = [150, 150]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[100, 100], [101, 100], [100, 101], [101, 101], [102, 100], [100, 102], [102, 102], [101, 102], [103, 101], [101, 103], [104, 101], [101, 104], [105, 101], [101, 105]],source = [50, 50],target = [150, 150]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[50, 50], [51, 51], [52, 52], [53, 53], [54, 54], [55, 55], [56, 56], [57, 57], [58, 58]],source = [49, 49],target = [59, 59]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[50, 50], [51, 51], [52, 52], [53, 53], [54, 54], [55, 55], [56, 56], [57, 57], [58, 58]],source = [49, 49],target = [59, 59]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],source = [0, 0],target = [9, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],source = [0, 0],target = [9, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9]],source = [0, 0],target = [2, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9]],source = [0, 0],target = [2, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[200, 200], [201, 200], [202, 200], [203, 200], [204, 200], [205, 200], [206, 200], [207, 200], [208, 200], [209, 200]],source = [100, 100],target = [300, 300]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[200, 200], [201, 200], [202, 200], [203, 200], [204, 200], [205, 200], [206, 200], [207, 200], [208, 200], [209, 200]],source = [100, 100],target = [300, 300]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]],source = [0, 0],target = [0, 10]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]],source = [0, 0],target = [0, 10]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[500, 500], [501, 500], [502, 500], [503, 500], [504, 500], [500, 501], [501, 501], [502, 501], [503, 501], [504, 501]],source = [499, 499],target = [505, 505]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[500, 500], [501, 500], [502, 500], [503, 500], [504, 500], [500, 501], [501, 501], [502, 501], [503, 501], [504, 501]],source = [499, 499],target = [505, 505]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[999998, 999999], [999999, 999998]],source = [0, 0],target = [999997, 999998]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[999998, 999999], [999999, 999998]],source = [0, 0],target = [999997, 999998]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[500000, 500000], [500001, 500001], [500002, 500002], [500003, 500003], [500004, 500004]],source = [499999, 499999],target = [500005, 500005]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[500000, 500000], [500001, 500001], [500002, 500002], [500003, 500003], [500004, 500004]],source = [499999, 499999],target = [500005, 500005]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[500000, 500000], [500001, 500000], [500000, 500001], [500001, 500001], [500002, 500000], [500000, 500002], [500002, 500002]],source = [500000, 499999],target = [500002, 500003]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[500000, 500000], [500001, 500000], [500000, 500001], [500001, 500001], [500002, 500000], [500000, 500002], [500002, 500002]],source = [500000, 499999],target = [500002, 500003]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4]],source = [0, 0],target = [5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4]],source = [0, 0],target = [5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[500, 500], [501, 500], [500, 501], [501, 501]],source = [400, 400],target = [600, 600]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[500, 500], [501, 500], [500, 501], [501, 501]],source = [400, 400],target = [600, 600]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[100000, 100000], [100001, 100000], [100002, 100000], [100000, 100001], [100000, 100002]],source = [99999, 99999],target = [100003, 100003]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[100000, 100000], [100001, 100000], [100002, 100000], [100000, 100001], [100000, 100002]],source = [99999, 99999],target = [100003, 100003]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[500, 500], [500, 501], [500, 502], [500, 503], [500, 504], [501, 500], [501, 501], [501, 502], [501, 503], [501, 504], [502, 500], [502, 501], [502, 502], [502, 503], [502, 504], [503, 500], [503, 501], [503, 502], [503, 503], [503, 504]],source = [500, 499],target = [504, 504]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[500, 500], [500, 501], [500, 502], [500, 503], [500, 504], [501, 500], [501, 501], [501, 502], [501, 503], [501, 504], [502, 500], [502, 501], [502, 502], [502, 503], [502, 504], [503, 500], [503, 501], [503, 502], [503, 503], [503, 504]],source = [500, 499],target = [504, 504]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [1, 2], [2, 1], [2, 2], [2, 3], [3, 2], [3, 3], [3, 4], [4, 3], [4, 4]],source = [0, 0],target = [5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [1, 2], [2, 1], [2, 2], [2, 3], [3, 2], [3, 3], [3, 4], [4, 3], [4, 4]],source = [0, 0],target = [5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[500000, 500000], [500001, 500000], [500002, 500000], [500000, 500001], [500000, 500002]],source = [499999, 499999],target = [500003, 500003]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[500000, 500000], [500001, 500000], [500002, 500000], [500000, 500001], [500000, 500002]],source = [499999, 499999],target = [500003, 500003]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[100, 100], [101, 100], [102, 100], [103, 100], [104, 100], [100, 101], [100, 102], [100, 103], [100, 104]],source = [99, 99],target = [105, 105]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[100, 100], [101, 100], [102, 100], [103, 100], [104, 100], [100, 101], [100, 102], [100, 103], [100, 104]],source = [99, 99],target = [105, 105]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9]],source = [0, 0],target = [3, 0]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9]],source = [0, 0],target = [3, 0]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[999998, 999998], [999998, 999999], [999999, 999998], [999997, 999999], [999999, 999997]],source = [999997, 999997],target = [999998, 999999]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[999998, 999998], [999998, 999999], [999999, 999998], [999997, 999999], [999999, 999997]],source = [999997, 999997],target = [999998, 999999]) == False: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[0, 1], [1, 0], [2, 0], [3, 0], [0, 2], [1, 2], [2, 2], [3, 2]],source = [0, 0],target = [3, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[0, 1], [1, 0], [2, 0], [3, 0], [0, 2], [1, 2], [2, 2], [3, 2]],source = [0, 0],target = [3, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 0], [0, 1], [2, 0], [0, 2], [3, 0], [0, 3], [4, 0], [0, 4]],source = [0, 0],target = [4, 4]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 0], [0, 1], [2, 0], [0, 2], [3, 0], [0, 3], [4, 0], [0, 4]],source = [0, 0],target = [4, 4]) == False: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[50000, 50000], [50000, 50001], [50000, 50002], [50001, 50000], [50001, 50001], [50001, 50002], [50002, 50000], [50002, 50001], [50002, 50002]],source = [0, 0],target = [99999, 99999]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[50000, 50000], [50000, 50001], [50000, 50002], [50001, 50000], [50001, 50001], [50001, 50002], [50002, 50000], [50002, 50001], [50002, 50002]],source = [0, 0],target = [99999, 99999]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [2, 1], [3, 1], [4, 1], [1, 2], [2, 2], [3, 2], [4, 2], [1, 3], [2, 3], [3, 3], [4, 3]],source = [0, 0],target = [5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [2, 1], [3, 1], [4, 1], [1, 2], [2, 2], [3, 2], [4, 2], [1, 3], [2, 3], [3, 3], [4, 3]],source = [0, 0],target = [5, 5]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[2, 1], [2, 2], [3, 2], [4, 2], [5, 2]],source = [1, 1],target = [6, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[2, 1], [2, 2], [3, 2], [4, 2], [5, 2]],source = [1, 1],target = [6, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[100000, 100000], [100001, 100000], [100002, 100000], [100000, 100001], [100001, 100001], [100002, 100001], [100000, 100002], [100001, 100002], [100002, 100002]],source = [99999, 99999],target = [100003, 100003]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[100000, 100000], [100001, 100000], [100002, 100000], [100000, 100001], [100001, 100001], [100002, 100001], [100000, 100002], [100001, 100002], [100002, 100002]],source = [99999, 99999],target = [100003, 100003]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[50, 50], [50, 51], [50, 52], [51, 50], [52, 50], [51, 52], [52, 51]],source = [49, 49],target = [53, 53]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[50, 50], [50, 51], [50, 52], [51, 50], [52, 50], [51, 52], [52, 51]],source = [49, 49],target = [53, 53]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[200, 200], [201, 200], [202, 200], [200, 201], [200, 202], [201, 202], [202, 202]],source = [100, 100],target = [250, 250]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[200, 200], [201, 200], [202, 200], [200, 201], [200, 202], [201, 202], [202, 202]],source = [100, 100],target = [250, 250]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],source = [0, 0],target = [11, 11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],source = [0, 0],target = [11, 11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[500, 500], [501, 500], [502, 500], [503, 500], [504, 500], [505, 500], [506, 500], [500, 501], [500, 502], [500, 503], [500, 504], [500, 505], [500, 506]],source = [500, 499],target = [506, 506]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[500, 500], [501, 500], [502, 500], [503, 500], [504, 500], [505, 500], [506, 500], [500, 501], [500, 502], [500, 503], [500, 504], [500, 505], [500, 506]],source = [500, 499],target = [506, 506]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 0], [0, 1], [2, 0], [0, 2], [3, 0], [0, 3]],source = [0, 0],target = [3, 3]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 0], [0, 1], [2, 0], [0, 2], [3, 0], [0, 3]],source = [0, 0],target = [3, 3]) == False: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[500000, 500000], [500001, 500000], [500002, 500000], [500000, 500001], [500001, 500001], [500002, 500001]],source = [499999, 499999],target = [500003, 500003]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[500000, 500000], [500001, 500000], [500002, 500000], [500000, 500001], [500001, 500001], [500002, 500001]],source = [499999, 499999],target = [500003, 500003]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[999999, 0], [999998, 0], [999997, 0], [999998, 1], [999999, 1]],source = [999995, 0],target = [999999, 999999]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[999999, 0], [999998, 0], [999997, 0], [999998, 1], [999999, 1]],source = [999995, 0],target = [999999, 999999]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]],source = [0, 1],target = [11, 1]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]],source = [0, 1],target = [11, 1]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [2, 1], [3, 1], [1, 2], [2, 2], [3, 2], [1, 3], [2, 3], [3, 3]],source = [0, 0],target = [6, 6]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [2, 1], [3, 1], [1, 2], [2, 2], [3, 2], [1, 3], [2, 3], [3, 3]],source = [0, 0],target = [6, 6]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 0], [1, 1], [2, 0], [2, 1]],source = [0, 0],target = [2, 2]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 0], [1, 1], [2, 0], [2, 1]],source = [0, 0],target = [2, 2]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [3, 2]],source = [0, 3],target = [3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [3, 2]],source = [0, 3],target = [3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10]],source = [0, 0],target = [3, 3]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10]],source = [0, 0],target = [3, 3]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1000, 1000], [1001, 1001], [1002, 1002], [1000, 1001], [1001, 1000], [1002, 1001], [1001, 1002], [1000, 1002], [1002, 1000]],source = [999, 999],target = [1003, 1003]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1000, 1000], [1001, 1001], [1002, 1002], [1000, 1001], [1001, 1000], [1002, 1001], [1001, 1002], [1000, 1002], [1002, 1000]],source = [999, 999],target = [1003, 1003]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7], [7, 5], [7, 6], [7, 7], [8, 8], [8, 9], [8, 10], [9, 8], [9, 9], [9, 10], [10, 8], [10, 9], [10, 10]],source = [4, 4],target = [11, 11]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7], [7, 5], [7, 6], [7, 7], [8, 8], [8, 9], [8, 10], [9, 8], [9, 9], [9, 10], [10, 8], [10, 9], [10, 10]],source = [4, 4],target = [11, 11]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[100, 100], [101, 100], [102, 100], [103, 100], [104, 100], [105, 100], [106, 100], [107, 100], [108, 100], [109, 100], [100, 101], [100, 102], [100, 103], [100, 104], [100, 105], [100, 106], [100, 107], [100, 108], [100, 109]],source = [99, 99],target = [109, 109]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[100, 100], [101, 100], [102, 100], [103, 100], [104, 100], [105, 100], [106, 100], [107, 100], [108, 100], [109, 100], [100, 101], [100, 102], [100, 103], [100, 104], [100, 105], [100, 106], [100, 107], [100, 108], [100, 109]],source = [99, 99],target = [109, 109]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[100000, 100000], [100001, 100001], [100002, 100002], [100003, 100003], [100004, 100004]],source = [0, 0],target = [200000, 200000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[100000, 100000], [100001, 100001], [100002, 100002], [100003, 100003], [100004, 100004]],source = [0, 0],target = [200000, 200000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]],source = [0, 0],target = [4, 4]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]],source = [0, 0],target = [4, 4]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[100000, 100000], [100000, 100001], [100000, 100002], [100000, 100003], [100000, 100004], [100001, 100000], [100001, 100001], [100001, 100002], [100001, 100003], [100001, 100004]],source = [0, 0],target = [200000, 200000]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[100000, 100000], [100000, 100001], [100000, 100002], [100000, 100003], [100000, 100004], [100001, 100000], [100001, 100001], [100001, 100002], [100001, 100003], [100001, 100004]],source = [0, 0],target = [200000, 200000]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[500000, 500000], [500001, 500000], [500002, 500000], [500000, 500001], [500001, 500001], [500002, 500001], [500000, 500002], [500001, 500002], [500002, 500002]],source = [499990, 499990],target = [500010, 500010]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[500000, 500000], [500001, 500000], [500002, 500000], [500000, 500001], [500001, 500001], [500002, 500001], [500000, 500002], [500001, 500002], [500002, 500002]],source = [499990, 499990],target = [500010, 500010]) == True: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]],source = [0, 0],target = [5, 5]) == False
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]],source = [0, 0],target = [5, 5]) == False: {e}')
    
    total += 1
    try:
        result = candidate(blocked = [[1, 1], [2, 1], [3, 1], [1, 2], [2, 2], [1, 3]],source = [0, 0],target = [5, 5]) == True
        if result:
            passed += 1
    except Exception as e:
        print(f'Error in candidate(blocked = [[1, 1], [2, 1], [3, 1], [1, 2], [2, 2], [1, 3]],source = [0, 0],target = [5, 5]) == True: {e}')
    
    accuracy = (passed / total * 100) if total > 0 else 0
    return passed, total, accuracy

def check(candidate):
    assert candidate(blocked = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]],source = [0, 0],target = [6, 6]) == True
    assert candidate(blocked = [[5, 5]],source = [4, 4],target = [6, 6]) == True
    assert candidate(blocked = [],source = [0, 0],target = [999999, 999999]) == True
    assert candidate(blocked = [[1, 2], [2, 1], [2, 3], [3, 2]],source = [0, 0],target = [4, 4]) == True
    assert candidate(blocked = [[10, 10], [11, 10], [12, 10], [13, 10]],source = [9, 9],target = [14, 14]) == True
    assert candidate(blocked = [[500000, 500000]],source = [499999, 499999],target = [500001, 500001]) == True
    assert candidate(blocked = [[10, 10], [10, 11], [10, 12], [11, 10], [11, 11], [11, 12], [12, 10], [12, 11], [12, 12]],source = [9, 9],target = [13, 13]) == True
    assert candidate(blocked = [[0, 1], [1, 0], [2, 0], [0, 2]],source = [0, 0],target = [3, 3]) == False
    assert candidate(blocked = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 7], [7, 5], [7, 6], [7, 7]],source = [4, 4],target = [8, 8]) == True
    assert candidate(blocked = [[1, 1], [2, 2], [3, 3]],source = [0, 0],target = [3, 4]) == True
    assert candidate(blocked = [[10, 10], [11, 10], [10, 11], [11, 11]],source = [0, 0],target = [20, 20]) == True
    assert candidate(blocked = [[0, 3], [1, 3], [2, 3], [3, 3]],source = [0, 0],target = [0, 4]) == True
    assert candidate(blocked = [[0, 1], [1, 0]],source = [0, 0],target = [0, 2]) == False
    assert candidate(blocked = [[0, 1], [1, 1], [2, 1], [3, 1]],source = [0, 0],target = [0, 4]) == True
    assert candidate(blocked = [[1, 1], [1, 2], [2, 1]],source = [0, 0],target = [3, 3]) == True
    assert candidate(blocked = [[100, 100], [100, 101], [101, 100], [101, 101], [200, 200], [200, 201], [201, 200], [201, 201]],source = [0, 0],target = [300, 300]) == True
    assert candidate(blocked = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]],source = [0, 0],target = [11, 11]) == True
    assert candidate(blocked = [[999997, 999998], [999998, 999998], [999999, 999998], [999997, 999999], [999998, 999999], [999999, 999999]],source = [999995, 999995],target = [999999, 999999]) == False
    assert candidate(blocked = [[50, 50], [50, 51], [50, 52], [50, 53], [51, 50], [51, 51], [51, 52], [51, 53], [52, 50], [52, 51], [52, 52], [52, 53], [53, 50], [53, 51], [53, 52], [53, 53]],source = [0, 0],target = [100, 100]) == True
    assert candidate(blocked = [[500, 500], [501, 500], [502, 500], [500, 501], [501, 501], [502, 501], [500, 502], [501, 502], [502, 502]],source = [500, 499],target = [502, 503]) == True
    assert candidate(blocked = [[1000, 1000], [1001, 1000], [1000, 1001], [1001, 1001], [1002, 1000], [1000, 1002], [1002, 1002], [1001, 1002], [1003, 1001], [1001, 1003]],source = [500, 500],target = [1500, 1500]) == True
    assert candidate(blocked = [[999998, 999998], [999998, 999999], [999999, 999998], [999999, 999999]],source = [999997, 999997],target = [999998, 999997]) == True
    assert candidate(blocked = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],source = [0, 0],target = [9, 9]) == True
    assert candidate(blocked = [[5, 4], [4, 5], [6, 5], [5, 6]],source = [5, 5],target = [6, 6]) == False
    assert candidate(blocked = [[500000, 500000], [500001, 500001], [500002, 500002], [500003, 500003]],source = [499999, 499999],target = [500004, 500004]) == True
    assert candidate(blocked = [[1, 2], [2, 1], [2, 3], [3, 2], [4, 3], [5, 4]],source = [0, 0],target = [6, 6]) == True
    assert candidate(blocked = [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [3, 2], [3, 3]],source = [10, 10],target = [0, 2]) == True
    assert candidate(blocked = [[999998, 999998], [999997, 999998], [999996, 999998], [999998, 999997], [999997, 999997], [999996, 999997], [999998, 999996], [999997, 999996], [999996, 999996]],source = [999995, 999995],target = [999999, 999999]) == True
    assert candidate(blocked = [[500000, 500000], [500001, 500000], [500002, 500000], [500000, 500001], [500001, 500001], [500002, 500001]],source = [499999, 499999],target = [500001, 500001]) == True
    assert candidate(blocked = [[10, 10], [11, 10], [12, 10], [10, 11], [10, 12], [11, 11], [11, 12], [12, 11], [12, 12], [13, 13], [14, 14], [13, 14], [14, 13]],source = [0, 0],target = [20, 20]) == True
    assert candidate(blocked = [[999999, 999998], [999998, 999999]],source = [0, 0],target = [999998, 999997]) == True
    assert candidate(blocked = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4]],source = [0, 0],target = [0, 5]) == True
    assert candidate(blocked = [[1, 1], [2, 1], [3, 1], [1, 2], [2, 2], [3, 2], [1, 3], [2, 3], [3, 3], [1, 4], [2, 4], [3, 4], [1, 5], [2, 5], [3, 5]],source = [0, 0],target = [3, 5]) == True
    assert candidate(blocked = [[999999, 999999]],source = [0, 0],target = [999998, 999998]) == True
    assert candidate(blocked = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 2], [2, 3], [2, 4], [2, 5]],source = [0, 0],target = [6, 0]) == True
    assert candidate(blocked = [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]],source = [0, 0],target = [10, 1]) == True
    assert candidate(blocked = [[100000, 100000], [100001, 100000], [100002, 100000], [100003, 100000], [100004, 100000], [100005, 100000], [100006, 100000], [100007, 100000]],source = [99999, 99999],target = [100008, 100008]) == True
    assert candidate(blocked = [[1, 1], [1, 2], [2, 1], [2, 2]],source = [0, 0],target = [3, 3]) == True
    assert candidate(blocked = [[0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3]],source = [0, 0],target = [5, 5]) == False
    assert candidate(blocked = [[500000, 0], [500001, 0], [500002, 0], [500003, 0], [500004, 0], [500005, 0], [500006, 0], [500007, 0], [500008, 0], [500009, 0]],source = [499990, 0],target = [500010, 0]) == True
    assert candidate(blocked = [[0, 0], [1, 0], [2, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 1], [2, 2], [1, 3], [2, 3]],source = [0, 3],target = [3, 0]) == True
    assert candidate(blocked = [[0, 1], [1, 0], [1, 1]],source = [2, 2],target = [3, 3]) == True
    assert candidate(blocked = [[10, 10], [11, 10], [12, 10], [10, 11], [11, 11], [10, 12]],source = [9, 9],target = [13, 13]) == True
    assert candidate(blocked = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3], [4, 1], [4, 2], [4, 3]],source = [0, 0],target = [5, 5]) == True
    assert candidate(blocked = [[500000, 500000], [500001, 500001], [500002, 500002]],source = [500000, 500001],target = [500002, 500000]) == True
    assert candidate(blocked = [[500000, 500000], [500001, 500000], [500002, 500000], [500003, 500000], [500004, 500000], [500005, 500000], [500000, 500001], [500000, 500002], [500000, 500003], [500000, 500004], [500000, 500005]],source = [499999, 500000],target = [500006, 500006]) == True
    assert candidate(blocked = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8]],source = [0, 0],target = [5, 9]) == True
    assert candidate(blocked = [[100, 100], [101, 100], [102, 100], [100, 101], [101, 101], [102, 101], [100, 102], [101, 102], [102, 102]],source = [99, 99],target = [103, 103]) == True
    assert candidate(blocked = [[0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],source = [0, 0],target = [3, 3]) == False
    assert candidate(blocked = [[0, 1], [1, 0], [1, 1], [2, 1], [1, 2], [2, 2], [3, 2], [2, 3], [3, 3], [4, 3], [3, 4], [4, 4], [5, 4], [4, 5], [5, 5], [6, 5], [5, 6], [6, 6], [7, 6], [6, 7], [7, 7]],source = [0, 0],target = [10, 10]) == False
    assert candidate(blocked = [[1, 1], [2, 1], [1, 2], [2, 2]],source = [0, 0],target = [3, 3]) == True
    assert candidate(blocked = [[100, 100], [101, 100], [102, 100], [100, 101], [101, 101], [102, 101], [100, 102], [101, 102], [102, 102]],source = [50, 50],target = [150, 150]) == True
    assert candidate(blocked = [[100, 100], [101, 100], [102, 100], [103, 100], [104, 100], [100, 101], [100, 102], [100, 103], [100, 104], [101, 101], [101, 102], [101, 103], [102, 101], [102, 102], [103, 101]],source = [100, 100],target = [104, 104]) == True
    assert candidate(blocked = [[999999, 999998], [999998, 999999], [999998, 999998]],source = [999997, 999997],target = [999999, 999999]) == False
    assert candidate(blocked = [[999999, 999999], [999998, 999998], [999997, 999997]],source = [999996, 999996],target = [0, 0]) == True
    assert candidate(blocked = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4]],source = [0, 5],target = [5, 0]) == True
    assert candidate(blocked = [[500000, 500000], [500001, 500000], [500000, 500001], [500001, 500001]],source = [499999, 499999],target = [500002, 500002]) == True
    assert candidate(blocked = [[10, 10], [11, 10], [10, 11], [11, 11], [12, 10], [10, 12], [12, 12], [11, 12], [13, 11], [11, 13]],source = [0, 0],target = [14, 14]) == True
    assert candidate(blocked = [[999999, 999999], [999998, 999998], [999997, 999997], [999996, 999996], [999995, 999995]],source = [0, 0],target = [999999, 999999]) == True
    assert candidate(blocked = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]],source = [0, 0],target = [0, 11]) == True
    assert candidate(blocked = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9]],source = [0, 0],target = [999999, 999999]) == True
    assert candidate(blocked = [[0, 500000], [0, 500001], [0, 500002], [0, 500003], [0, 500004], [0, 500005], [0, 500006], [0, 500007], [0, 500008], [0, 500009]],source = [0, 499990],target = [0, 500010]) == True
    assert candidate(blocked = [[1, 1], [2, 1], [3, 1], [1, 2], [2, 2], [3, 2], [1, 3], [2, 3], [3, 3]],source = [0, 0],target = [3, 0]) == True
    assert candidate(blocked = [[100, 100], [101, 100], [100, 101], [101, 101], [102, 100], [100, 102], [102, 102], [101, 102], [103, 101], [101, 103], [104, 101], [101, 104], [105, 101], [101, 105]],source = [50, 50],target = [150, 150]) == True
    assert candidate(blocked = [[50, 50], [51, 51], [52, 52], [53, 53], [54, 54], [55, 55], [56, 56], [57, 57], [58, 58]],source = [49, 49],target = [59, 59]) == True
    assert candidate(blocked = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]],source = [0, 0],target = [9, 10]) == True
    assert candidate(blocked = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9]],source = [0, 0],target = [2, 0]) == True
    assert candidate(blocked = [[200, 200], [201, 200], [202, 200], [203, 200], [204, 200], [205, 200], [206, 200], [207, 200], [208, 200], [209, 200]],source = [100, 100],target = [300, 300]) == True
    assert candidate(blocked = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]],source = [0, 0],target = [0, 10]) == True
    assert candidate(blocked = [[500, 500], [501, 500], [502, 500], [503, 500], [504, 500], [500, 501], [501, 501], [502, 501], [503, 501], [504, 501]],source = [499, 499],target = [505, 505]) == True
    assert candidate(blocked = [[999998, 999999], [999999, 999998]],source = [0, 0],target = [999997, 999998]) == True
    assert candidate(blocked = [[500000, 500000], [500001, 500001], [500002, 500002], [500003, 500003], [500004, 500004]],source = [499999, 499999],target = [500005, 500005]) == True
    assert candidate(blocked = [[500000, 500000], [500001, 500000], [500000, 500001], [500001, 500001], [500002, 500000], [500000, 500002], [500002, 500002]],source = [500000, 499999],target = [500002, 500003]) == True
    assert candidate(blocked = [[1, 1], [1, 2], [1, 3], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 1], [3, 2], [3, 3], [3, 4]],source = [0, 0],target = [5, 5]) == True
    assert candidate(blocked = [[500, 500], [501, 500], [500, 501], [501, 501]],source = [400, 400],target = [600, 600]) == True
    assert candidate(blocked = [[100000, 100000], [100001, 100000], [100002, 100000], [100000, 100001], [100000, 100002]],source = [99999, 99999],target = [100003, 100003]) == True
    assert candidate(blocked = [[500, 500], [500, 501], [500, 502], [500, 503], [500, 504], [501, 500], [501, 501], [501, 502], [501, 503], [501, 504], [502, 500], [502, 501], [502, 502], [502, 503], [502, 504], [503, 500], [503, 501], [503, 502], [503, 503], [503, 504]],source = [500, 499],target = [504, 504]) == True
    assert candidate(blocked = [[1, 1], [1, 2], [2, 1], [2, 2], [2, 3], [3, 2], [3, 3], [3, 4], [4, 3], [4, 4]],source = [0, 0],target = [5, 5]) == True
    assert candidate(blocked = [[500000, 500000], [500001, 500000], [500002, 500000], [500000, 500001], [500000, 500002]],source = [499999, 499999],target = [500003, 500003]) == True
    assert candidate(blocked = [[100, 100], [101, 100], [102, 100], [103, 100], [104, 100], [100, 101], [100, 102], [100, 103], [100, 104]],source = [99, 99],target = [105, 105]) == True
    assert candidate(blocked = [[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9]],source = [0, 0],target = [3, 0]) == True
    assert candidate(blocked = [[999998, 999998], [999998, 999999], [999999, 999998], [999997, 999999], [999999, 999997]],source = [999997, 999997],target = [999998, 999999]) == False
    assert candidate(blocked = [[0, 1], [1, 0], [2, 0], [3, 0], [0, 2], [1, 2], [2, 2], [3, 2]],source = [0, 0],target = [3, 3]) == False
    assert candidate(blocked = [[1, 0], [0, 1], [2, 0], [0, 2], [3, 0], [0, 3], [4, 0], [0, 4]],source = [0, 0],target = [4, 4]) == False
    assert candidate(blocked = [[50000, 50000], [50000, 50001], [50000, 50002], [50001, 50000], [50001, 50001], [50001, 50002], [50002, 50000], [50002, 50001], [50002, 50002]],source = [0, 0],target = [99999, 99999]) == True
    assert candidate(blocked = [[1, 1], [2, 1], [3, 1], [4, 1], [1, 2], [2, 2], [3, 2], [4, 2], [1, 3], [2, 3], [3, 3], [4, 3]],source = [0, 0],target = [5, 5]) == True
    assert candidate(blocked = [[2, 1], [2, 2], [3, 2], [4, 2], [5, 2]],source = [1, 1],target = [6, 1]) == True
    assert candidate(blocked = [[100000, 100000], [100001, 100000], [100002, 100000], [100000, 100001], [100001, 100001], [100002, 100001], [100000, 100002], [100001, 100002], [100002, 100002]],source = [99999, 99999],target = [100003, 100003]) == True
    assert candidate(blocked = [[50, 50], [50, 51], [50, 52], [51, 50], [52, 50], [51, 52], [52, 51]],source = [49, 49],target = [53, 53]) == True
    assert candidate(blocked = [[200, 200], [201, 200], [202, 200], [200, 201], [200, 202], [201, 202], [202, 202]],source = [100, 100],target = [250, 250]) == True
    assert candidate(blocked = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],source = [0, 0],target = [11, 11]) == True
    assert candidate(blocked = [[500, 500], [501, 500], [502, 500], [503, 500], [504, 500], [505, 500], [506, 500], [500, 501], [500, 502], [500, 503], [500, 504], [500, 505], [500, 506]],source = [500, 499],target = [506, 506]) == True
    assert candidate(blocked = [[1, 0], [0, 1], [2, 0], [0, 2], [3, 0], [0, 3]],source = [0, 0],target = [3, 3]) == False
    assert candidate(blocked = [[500000, 500000], [500001, 500000], [500002, 500000], [500000, 500001], [500001, 500001], [500002, 500001]],source = [499999, 499999],target = [500003, 500003]) == True
    assert candidate(blocked = [[999999, 0], [999998, 0], [999997, 0], [999998, 1], [999999, 1]],source = [999995, 0],target = [999999, 999999]) == True
    assert candidate(blocked = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]],source = [0, 1],target = [11, 1]) == True
    assert candidate(blocked = [[1, 1], [2, 1], [3, 1], [1, 2], [2, 2], [3, 2], [1, 3], [2, 3], [3, 3]],source = [0, 0],target = [6, 6]) == True
    assert candidate(blocked = [[1, 0], [1, 1], [2, 0], [2, 1]],source = [0, 0],target = [2, 2]) == True
    assert candidate(blocked = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0], [3, 1], [3, 2]],source = [0, 3],target = [3, 3]) == True
    assert candidate(blocked = [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10]],source = [0, 0],target = [3, 3]) == True
    assert candidate(blocked = [[1000, 1000], [1001, 1001], [1002, 1002], [1000, 1001], [1001, 1000], [1002, 1001], [1001, 1002], [1000, 1002], [1002, 1000]],source = [999, 999],target = [1003, 1003]) == True
    assert candidate(blocked = [[5, 5], [5, 6], [5, 7], [6, 5], [6, 6], [6, 7], [7, 5], [7, 6], [7, 7], [8, 8], [8, 9], [8, 10], [9, 8], [9, 9], [9, 10], [10, 8], [10, 9], [10, 10]],source = [4, 4],target = [11, 11]) == True
    assert candidate(blocked = [[100, 100], [101, 100], [102, 100], [103, 100], [104, 100], [105, 100], [106, 100], [107, 100], [108, 100], [109, 100], [100, 101], [100, 102], [100, 103], [100, 104], [100, 105], [100, 106], [100, 107], [100, 108], [100, 109]],source = [99, 99],target = [109, 109]) == True
    assert candidate(blocked = [[100000, 100000], [100001, 100001], [100002, 100002], [100003, 100003], [100004, 100004]],source = [0, 0],target = [200000, 200000]) == True
    assert candidate(blocked = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]],source = [0, 0],target = [4, 4]) == True
    assert candidate(blocked = [[100000, 100000], [100000, 100001], [100000, 100002], [100000, 100003], [100000, 100004], [100001, 100000], [100001, 100001], [100001, 100002], [100001, 100003], [100001, 100004]],source = [0, 0],target = [200000, 200000]) == True
    assert candidate(blocked = [[500000, 500000], [500001, 500000], [500002, 500000], [500000, 500001], [500001, 500001], [500002, 500001], [500000, 500002], [500001, 500002], [500002, 500002]],source = [499990, 499990],target = [500010, 500010]) == True
    assert candidate(blocked = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]],source = [0, 0],target = [5, 5]) == False
    assert candidate(blocked = [[1, 1], [2, 1], [3, 1], [1, 2], [2, 2], [1, 3]],source = [0, 0],target = [5, 5]) == True


